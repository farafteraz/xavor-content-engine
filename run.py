"""
Xavor Content Engine — monthly pipeline from Sentinel digests to a finished
LinkedIn calendar with publishable post drafts.

Stages (each saves a human-readable artifact to output/<month>/):
  0 ingest           -> 0-corpus.md
  1 strategic brief  -> 1-strategic-brief.md
  2 creative brief   -> 2-creative-brief.md
  3 calendar         -> 3-calendar.md (+ parsed slots)
  4 drafts           -> posts/drafts-v1/*.md (parallel)
  5 qc + revise      -> posts/*.md, qc/*.md, 5-qc-report.md

Usage:
  python run.py                          # digests fetched from the Sentinel repo; targets the
                                         # current month if run in its first half, else the next
  python run.py --month 2026-07          # explicit target month
  python run.py --corpus digests/x.txt   # explicit corpus file instead of fetching
  python run.py --from-stage 3           # reuse saved artifacts for stages < 3

Environment (env vars or a local .env file; never hardcoded):
  ANTHROPIC_API_KEY   required
  OPENAI_API_KEY      required for --profile hybrid
  CONTENT_MODEL       default: claude-opus-4-8
  SENTINEL_REPO       default: farafteraz/Xavor-Sentinel (digests/ dir is fetched)
  SENTINEL_TOKEN      required while the Sentinel repo is private — a GitHub token
                      with read access to its contents (GH_TOKEN/GITHUB_TOKEN also work)
"""

import argparse
import calendar as calmod
import concurrent.futures
import json
import os
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
PROMPTS = ROOT / "prompts"
STYLE_SPEC = (ROOT / "brand" / "style-spec.md").read_text()

MONTH_NAMES = ["", "January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]


def load_env():
    env_file = ROOT / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


load_env()

SENTINEL_REPO = os.environ.get("SENTINEL_REPO", "farafteraz/Xavor-Sentinel")
SENTINEL_TOKEN = (os.environ.get("SENTINEL_TOKEN")
                  or os.environ.get("GH_TOKEN")
                  or os.environ.get("GITHUB_TOKEN"))

from llm import ModelRouter

router = None


def run_strategy(prompt, label=""):
    return router.generate("strategy", prompt, label)


def run_writer(prompt, label=""):
    return router.generate("writer", prompt, label)


def run_editor(prompt, label=""):
    return router.generate("editor", prompt, label)


def prompt_template(name):
    return (PROMPTS / name).read_text()


# ── Parsing helpers ───────────────────────────────────────────────────────────

def extract_section(md, heading):
    """Return the body of a '## heading' section (up to the next '## ')."""
    pattern = rf"^##\s+{re.escape(heading)}.*?$(.*?)(?=^##\s|\Z)"
    m = re.search(pattern, md, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    return m.group(1).strip() if m else ""


def extract_json_block(md):
    blocks = re.findall(r"```json\s*(.*?)```", md, re.DOTALL)
    if not blocks:
        raise ValueError("no fenced json block found")
    return json.loads(blocks[-1])


def extract_territory(creative_brief, territory_id):
    pattern = rf"^(###\s+{re.escape(territory_id)}\b.*?)(?=^###\s|^##\s|\Z)"
    m = re.search(pattern, creative_brief, re.MULTILINE | re.DOTALL)
    return m.group(1).strip() if m else creative_brief


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


# ── Stage 0: ingest ───────────────────────────────────────────────────────────

def _github_get(url, raw=False):
    """GET a GitHub API URL, authenticated when a token is available.

    The Sentinel repo is private, and GitHub answers a private repo with 404 rather
    than 403 when the request is unauthenticated — so a missing token looks exactly
    like a missing directory. fetch_digests_from_github() says so in its error.
    """
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github.raw"
                             if raw else "application/vnd.github+json")
    if SENTINEL_TOKEN:
        req.add_header("Authorization", f"Bearer {SENTINEL_TOKEN}")
    with urllib.request.urlopen(req) as r:
        return r.read()


def fetch_digests_from_github():
    url = f"https://api.github.com/repos/{SENTINEL_REPO}/contents/digests"
    try:
        listing = json.loads(_github_get(url))
    except Exception as e:
        hint = (
            "SENTINEL_TOKEN is not set. The Sentinel repo is private, so an "
            "unauthenticated read returns 404 even though the digests exist. Set "
            "SENTINEL_TOKEN to a GitHub token with read access to its contents."
            if not SENTINEL_TOKEN else
            "Check that SENTINEL_TOKEN is valid, unexpired, and has contents read "
            "access to this repo."
        )
        sys.exit(
            f"Could not list digests in {SENTINEL_REPO} ({e}).\n{hint}\n"
            "Or pass --corpus <file> with the month's digests."
        )
    files = sorted(
        (f for f in listing if f["name"].endswith((".md", ".txt"))),
        key=lambda f: f["name"],
    )[-4:]
    if not files:
        sys.exit(f"No digest files found in {SENTINEL_REPO}/digests.")
    parts = []
    for f in files:
        body = _github_get(f["url"], raw=True).decode()
        parts.append(f"<!-- digest: {f['name']} -->\n\n{body}")
        print(f"  fetched {f['name']}")
    return "\n\n---\n\n".join(parts)


def stage0(outdir, corpus_file):
    print("Stage 0 — ingest")
    if corpus_file:
        corpus = Path(corpus_file).read_text()
        print(f"  using corpus file {corpus_file}")
    else:
        corpus = fetch_digests_from_github()
    (outdir / "0-corpus.md").write_text(corpus)
    return corpus


# ── Stages 1–3 ────────────────────────────────────────────────────────────────

def stage1(outdir, corpus, month_label):
    print("Stage 1 — strategic brief")
    prompt = (prompt_template("1-strategic-brief.md")
              .replace("{MONTH}", month_label).replace("{CORPUS}", corpus))
    brief = run_strategy(prompt, "strategic-brief")
    (outdir / "1-strategic-brief.md").write_text(brief)
    return brief


def stage2(outdir, strategic_brief, month_label):
    print("Stage 2 — creative brief")
    prompt = (prompt_template("2-creative-brief.md")
              .replace("{MONTH}", month_label)
              .replace("{STRATEGIC_BRIEF}", strategic_brief))
    brief = run_strategy(prompt, "creative-brief")
    (outdir / "2-creative-brief.md").write_text(brief)
    return brief


def publishing_weeks(year, month):
    last = calmod.monthrange(year, month)[1]
    weeks = []
    for w in range(4):
        start = date(year, month, min(1 + 7 * w, last))
        end = date(year, month, min(7 + 7 * w, last))
        weeks.append(f"Week {w + 1}: {start.isoformat()} to {end.isoformat()}")
    return "\n".join(weeks)


def stage3(outdir, creative_brief, ledger, month_label, year, month):
    print("Stage 3 — calendar")
    prompt = (prompt_template("3-calendar.md")
              .replace("{MONTH}", month_label)
              .replace("{WEEKS}", publishing_weeks(year, month))
              .replace("{CREATIVE_BRIEF}", creative_brief)
              .replace("{LEDGER}", ledger))
    cal = run_strategy(prompt, "calendar")
    (outdir / "3-calendar.md").write_text(cal)
    slots = extract_json_block(cal)["posts"]
    if len(slots) != 15:
        print(f"  warning: calendar returned {len(slots)} slots, expected 15")
    return slots


# ── Stage 4: drafts ───────────────────────────────────────────────────────────

def draft_prompt(slot, big_idea, territory, ledger, revision=""):
    return (prompt_template("4-draft.md")
            .replace("{N}", str(slot["n"]))
            .replace("{date}", slot["date"])
            .replace("{format}", slot["format"])
            .replace("{BIG_IDEA}", big_idea)
            .replace("{SLOT}", json.dumps(slot, indent=2))
            .replace("{TERRITORY}", territory)
            .replace("{LEDGER}", ledger)
            .replace("{REVISION}", revision))


def stage4(outdir, slots, big_idea, creative_brief, ledger):
    print(f"Stage 4 — drafting {len(slots)} posts (parallel)")
    draftdir = outdir / "posts" / "drafts-v1"
    draftdir.mkdir(parents=True, exist_ok=True)

    def draft_one(slot):
        path = draftdir / f"{slot['n']:02d}-{slug(slot['format'])}.md"
        if path.exists():
            print(f"  post {slot['n']:02d}: draft exists, skipping")
            return slot["n"], path.read_text()
        territory = extract_territory(creative_brief, slot["territory"])
        text = run_writer(draft_prompt(slot, big_idea, territory, ledger),
                          f"draft-{slot['n']:02d}")
        path.write_text(text)
        print(f"  drafted post {slot['n']:02d} ({slot['format']})")
        return slot["n"], text

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        return dict(ex.map(draft_one, slots))


# ── Stage 5: QC + revise ──────────────────────────────────────────────────────

MAX_REVISIONS = 2


def qc_one(slot, draft, big_idea, ledger):
    prompt = (prompt_template("5-qc.md")
              .replace("{BIG_IDEA}", big_idea)
              .replace("{SLOT}", json.dumps(slot, indent=2))
              .replace("{LEDGER}", ledger)
              .replace("{DRAFT}", draft))
    memo = run_editor(prompt, f"qc-{slot['n']:02d}")
    try:
        verdict = extract_json_block(memo)
    except Exception:
        verdict = {"verdict": "FAIL", "checks": {}, "verify_flags": [],
                   "edit_notes": "QC memo was unparseable; rewrite per the memo text:\n" + memo}
    return memo, verdict


def stage5(outdir, slots, drafts, big_idea, creative_brief, ledger):
    print(f"Stage 5 — independent QC and revision (parallel)")
    qcdir = outdir / "qc"
    qcdir.mkdir(exist_ok=True)
    postdir = outdir / "posts"

    def qc_and_fix(slot):
        n = slot["n"]
        done = postdir / f"{n:02d}-{slug(slot['format'])}.md"
        if done.exists():
            text = done.read_text()
            m = re.match(r"<!-- QC: (PASS|NEEDS HUMAN) after (\d+) round\(s\)(?: \| verify: (.*?))? -->", text)
            if m:
                print(f"  post {n:02d}: already QC'd ({m.group(1)}), skipping")
                return n, {"status": m.group(1), "rounds": int(m.group(2)),
                           "verify_flags": m.group(3).split("; ") if m.group(3) else [],
                           "checks": {}}
        draft = drafts[n]
        territory = extract_territory(creative_brief, slot["territory"])
        history = []
        for round_ in range(MAX_REVISIONS + 1):
            memo, verdict = qc_one(slot, draft, big_idea, ledger)
            (qcdir / f"{n:02d}-round{round_ + 1}.md").write_text(memo)
            history.append(verdict)
            if verdict["verdict"] == "PASS":
                break
            if round_ == MAX_REVISIONS:
                break
            print(f"  post {n:02d} failed QC round {round_ + 1}; rewriting")
            revision = (
                "## REVISION REQUIRED\n"
                "A previous version of this post failed independent QC. Rewrite it, "
                "executing every edit note below. Keep what the editor did not flag.\n\n"
                f"### Editor's notes\n{verdict['edit_notes']}\n\n"
                f"### The failed draft\n{draft}"
            )
            draft = run_writer(
                draft_prompt(slot, big_idea, territory, ledger, revision),
                f"rewrite-{n:02d}")
        final = history[-1]
        status = "PASS" if final["verdict"] == "PASS" else "NEEDS HUMAN"
        flags = final.get("verify_flags") or []
        header = f"<!-- QC: {status} after {len(history)} round(s)"
        if flags:
            header += f" | verify: {'; '.join(flags)}"
        header += " -->\n\n"
        (postdir / f"{n:02d}-{slug(slot['format'])}.md").write_text(header + draft)
        print(f"  post {n:02d}: {status} ({len(history)} QC round(s))")
        return n, {"status": status, "rounds": len(history), "verify_flags": flags,
                   "checks": final.get("checks", {})}

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        results = dict(ex.map(qc_and_fix, slots))

    lines = [f"# QC Report — {outdir.name}", ""]
    fails = [n for n, r in results.items() if r["status"] != "PASS"]
    verifies = [(n, f) for n, r in results.items() for f in r["verify_flags"]]
    lines.append(f"{len(results) - len(fails)}/{len(results)} posts passed independent QC.")
    if fails:
        lines.append(f"\n## Needs human attention\n")
        lines += [f"- Post {n:02d}: still failing after {results[n]['rounds']} rounds "
                  f"(see qc/{n:02d}-round{results[n]['rounds']}.md)" for n in sorted(fails)]
    if verifies:
        lines.append("\n## Facts flagged for human verification before publishing\n")
        lines += [f"- Post {n:02d}: {f}" for n, f in verifies]
    lines.append("\n## Per-post results\n")
    for n in sorted(results):
        r = results[n]
        failed_checks = [c for c, v in r.get("checks", {}).items() if v != "PASS"]
        note = f" — final failed checks: {', '.join(failed_checks)}" if failed_checks else ""
        lines.append(f"- Post {n:02d}: {r['status']}, {r['rounds']} round(s){note}")
    report = "\n".join(lines) + "\n"
    (outdir / "5-qc-report.md").write_text(report)
    print(report)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    global router
    p = argparse.ArgumentParser()
    p.add_argument("--month", help="target month YYYY-MM (default: next month)")
    p.add_argument("--corpus", help="corpus file instead of fetching from the Sentinel repo")
    p.add_argument("--from-stage", type=int, default=0,
                   help="reuse saved artifacts for earlier stages (0-4)")
    p.add_argument("--profile", choices=("v1", "hybrid"), default="v1",
                   help="v1: Claude for all roles; hybrid: OpenAI strategy/review, Claude writing")
    p.add_argument("--output-dir", help="separate output directory (required for hybrid)")
    args = p.parse_args()
    if args.profile == "hybrid" and not args.output_dir:
        p.error("--profile hybrid requires --output-dir to protect existing outputs")
    router = ModelRouter(args.profile, STYLE_SPEC)
    router.validate()


    if args.month:
        year, month = map(int, args.month.split("-"))
    else:
        # Default: the month being planned. Run on the 1st (the cron case) or in the
        # first half of a month, that's the current month; late in a month, the next.
        today = date.today()
        if today.day <= 15:
            year, month = today.year, today.month
        else:
            year, month = (today.year + (today.month == 12), today.month % 12 + 1)
    month_label = f"{MONTH_NAMES[month]} {year}"
    outdir = (Path(args.output_dir).resolve() if args.output_dir
              else ROOT / "output" / f"{year}-{month:02d}")
    if args.profile == "hybrid":
        for protected in (ROOT / "output", ROOT / "samples"):
            if outdir == protected.resolve() or protected.resolve() in outdir.parents:
                p.error("hybrid output must be outside output/ and samples/")
        if outdir.exists() and any(outdir.iterdir()):
            p.error("hybrid output directory must be empty to avoid mixing runs")
    outdir.mkdir(parents=True, exist_ok=True)
    print(f"Xavor Content Engine — {month_label} — {router.describe()}\n")

    fs = args.from_stage
    corpus = (outdir / "0-corpus.md").read_text() if fs > 0 else stage0(outdir, args.corpus)
    strategic = ((outdir / "1-strategic-brief.md").read_text() if fs > 1
                 else stage1(outdir, corpus, month_label))
    ledger = extract_section(strategic, "EVIDENCE LEDGER")
    if not ledger:
        sys.exit("Strategic brief has no EVIDENCE LEDGER section; inspect 1-strategic-brief.md")
    creative = ((outdir / "2-creative-brief.md").read_text() if fs > 2
                else stage2(outdir, strategic, month_label))
    big_idea = extract_section(creative, "The big idea") or creative
    if fs > 3:
        slots = extract_json_block((outdir / "3-calendar.md").read_text())["posts"]
    else:
        slots = stage3(outdir, creative, ledger, month_label, year, month)
    if fs > 4:
        drafts = {}
        for f in sorted((outdir / "posts" / "drafts-v1").glob("*.md")):
            drafts[int(f.name[:2])] = f.read_text()
    else:
        drafts = stage4(outdir, slots, big_idea, creative, ledger)
    stage5(outdir, slots, drafts, big_idea, creative, ledger)

    print(f"\nDone. Review {outdir}/3-calendar.md and {outdir}/posts/ — the one human step.")


if __name__ == "__main__":
    main()
