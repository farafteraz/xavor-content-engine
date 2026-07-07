# Xavor Content Engine

One command turns a month of weekly Sentinel digests into a finished LinkedIn content
calendar with publishable post drafts. Everything up to your review is automated; the
one human step is reading `output/<month>/3-calendar.md` and `output/<month>/posts/`,
lightly refining, and handing to design.

## How it works

A staged pipeline. Each stage takes structured input, emits a human-readable artifact to
`output/<month>/`, and is driven by an editable prompt file in `prompts/` — so when
quality slips, you can see exactly which stage broke and tune exactly one file.

| Stage | Artifact | What it does |
|---|---|---|
| 0 ingest | `0-corpus.md` | Fetches the last ~4 weekly digests from the Sentinel repo (or `--corpus <file>`) |
| 1 strategic brief | `1-strategic-brief.md` | Clusters/dedupes the month's signals, discards noise, distills 5–8 developments into implications ("so what / now what"), names the tensions, and builds the numbered EVIDENCE LEDGER every later stage is bound to |
| 2 creative brief | `2-creative-brief.md` | Generates three candidate big ideas, judges them, commits to ONE single-minded thesis + 3–5 territories that ladder to it, plus deliberate exclusions |
| 3 calendar | `3-calendar.md` | 15 dated LinkedIn slots across 4 weekly arcs; every slot has a job, ONE angle, audience, CTA, evidence refs, and a reason to exist |
| 4 drafts | `posts/drafts-v1/` | Writes finished copy for every slot, in parallel, bound to the style spec and the ledger |
| 5 QC + revise | `posts/`, `qc/`, `5-qc-report.md` | A fresh-context independent editor grades every draft against the 10-check rubric in `brand/style-spec.md`; failures get rewritten and re-graded (max 2 rounds); survivors that still fail are marked NEEDS HUMAN |

The style contract lives in `brand/style-spec.md` — the distilled, checkable fusion of
the voice profile and the anti-AI writing rules. It is injected as the system prompt of
every generation call and used verbatim as the QC rubric.

**Evidence rule:** no stat, market claim, or dated event appears anywhere unless it
traces to a numbered entry in the strategic brief's evidence ledger (built only from the
Sentinel corpus), or is explicitly flagged `[verify: ...]` for you to confirm. The QC
report collects all verify flags in one place.

## Setup

```bash
python3 -m venv .venv && .venv/bin/pip install anthropic
cp .env.example .env   # then put your real ANTHROPIC_API_KEY in .env
```

Config is env-only (`.env` is gitignored): `ANTHROPIC_API_KEY` (required),
`CONTENT_MODEL` (default `claude-opus-4-8`), `SENTINEL_REPO` (default
`farafteraz/Xavor-Sentinel`).

## Run

```bash
.venv/bin/python run.py                     # digests auto-fetched; targets the current month when run in its first half, else the next
.venv/bin/python run.py --month 2026-07 --corpus digests/2026-06-corpus-raw.txt
.venv/bin/python run.py --month 2026-07 --from-stage 3   # reuse stages 0-2, regenerate from calendar on
```

`--from-stage N` is the tuning loop: edit a prompt in `prompts/`, rerun from that stage,
and every earlier artifact is reused as-is.

Then review `output/<month>/3-calendar.md` + `output/<month>/posts/` and check
`5-qc-report.md` for anything marked NEEDS HUMAN and for facts flagged `[verify]`.

## Monthly trigger

`.github/workflows/content-engine.yml` runs the pipeline on the 1st of each month and
commits the output to this repo. To activate: push this directory to a GitHub repo, add
`ANTHROPIC_API_KEY` as an Actions secret, done. Manual runs also work from the Actions
tab (workflow_dispatch, with an optional month input).

The automatic digest feed requires one small change to the Sentinel repo — the Action
currently emails digests and saves nothing. Apply `sentinel-patch/README.md` (about ten
lines) so each weekly digest is also committed to `digests/` in Xavor-Sentinel, where
Stage 0 fetches it. Until that's merged, run with `--corpus`.

## Tuning each stage

- Drafts feel flat or generic → `prompts/4-draft.md` (the bar, calibration examples) and
  `brand/style-spec.md` (litmus tests).
- Month feels muddled / multi-theme → `prompts/2-creative-brief.md` (tighten the
  single-mindedness judging criteria).
- Insights read as news summaries → `prompts/1-strategic-brief.md` (the insight test and
  tension-finding instructions).
- Wrong cadence/format mix → the "Cadence and mix" block in `prompts/3-calendar.md`.
- QC too lenient or too brutal → `prompts/5-qc.md` (severity rules) and the rubric at the
  bottom of `brand/style-spec.md`.

Prompt edits are the intended maintenance path; `run.py` is just plumbing and should
rarely need to change.
