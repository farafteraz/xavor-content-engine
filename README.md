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
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
cp .env.example .env   # then put your real ANTHROPIC_API_KEY in .env
```

Config is env-only (`.env` is gitignored): `ANTHROPIC_API_KEY` (required),
`SENTINEL_TOKEN` (required for auto-fetch — see below), `CONTENT_MODEL` (default
`claude-opus-4-8`), `SENTINEL_REPO` (default `farafteraz/Xavor-Sentinel`).

`Xavor-Sentinel` is a private repo, so Stage 0 has to authenticate to read its digests.
Without a token GitHub returns 404 — indistinguishable from the directory not existing.
Locally, the simplest option is to borrow your `gh` login instead of storing a key:

```bash
SENTINEL_TOKEN="$(gh auth token)" .venv/bin/python run.py
```

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
commits the output to this repo. Manual runs also work from the Actions tab
(workflow_dispatch, with an optional month input).

It needs two Actions secrets:

- `ANTHROPIC_API_KEY`
- `SENTINEL_TOKEN` — a token with read access to `Xavor-Sentinel`'s contents. The job's
  built-in `GITHUB_TOKEN` will not do: it is scoped to this repo only, so it cannot read
  a second private repo.

The digest feed is live — `sentinel-patch/` was merged into Xavor-Sentinel as PR #1, and
each Sunday's digest is committed to `digests/YYYY-MM-DD.md` there. That folder is kept
only as a record of the change; nothing needs applying.

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

## V2 provider routing (opt-in)

The default `--profile v1` keeps all stages on Claude using `CONTENT_MODEL`.
The scheduled workflow continues to use this profile. Adding `OPENAI_API_KEY`
does not switch the production pipeline.

`--profile hybrid` routes stages 1-3 and QC to OpenAI; drafting and revisions stay
on Claude. This step changes provider routing only. Opportunity generation,
strategic rejection, and approval gates are not implemented yet.

| Role | Default provider | Model setting | Default model |
| --- | --- | --- | --- |
| Strategy | OpenAI | `STRATEGY_MODEL` | `gpt-5.6-sol` |
| Writer | Anthropic | `DRAFTING_MODEL` | `CONTENT_MODEL`, then `claude-opus-4-8` |
| Editor | OpenAI | `EDITOR_MODEL` | `STRATEGY_MODEL`, then `gpt-5.6-sol` |

Provider overrides are `STRATEGY_PROVIDER`, `DRAFTING_PROVIDER`, and
`EDITOR_PROVIDER` (`openai` or `anthropic`). Set the matching model when changing
a provider. `STRATEGY_REASONING_EFFORT` controls OpenAI calls and defaults to
`medium`. Both API keys are required for the default hybrid configuration.
OpenAI calls use the [Responses API](https://developers.openai.com/api/docs/guides/text)
and disable response storage. [GPT-5.6 Sol model documentation](https://developers.openai.com/api/docs/models/gpt-5.6-sol).

Use a new, empty directory outside `output/` and `samples/` for a comparison run:

```bash
.venv/bin/python run.py --profile hybrid --month 2026-08 \
  --corpus output/2026-08/0-corpus.md --output-dir work/august-hybrid
```

Hybrid runs currently start fresh; resume with `--from-stage` remains available
for v1. The archived baseline stays unchanged. Add `OPENAI_API_KEY` to the
repository's Actions secrets for the branch validation workflow.

### Validation

```bash
python -m unittest discover -s tests -v
python scripts/check_providers.py
```

The first command uses simulated provider responses to exercise all pipeline
stages, revisions, v1 resume, routing, and error handling without API charges.
The second makes a tiny live request to OpenAI and Anthropic using environment
keys. `.github/workflows/validate-engine.yml` runs both after relevant pushes to
`v2-strategy-engine`. It has read-only repository access and writes no content.
Passing these checks confirms integration behavior and basic provider access;
a full live monthly generation and content-quality comparison remain separate gates.

## V2 marketing foundation

The confirmed commercial direction, audience, and communication standards are
saved in [strategy/marketing-strategy.yml](strategy/marketing-strategy.yml).
The [offering catalog](knowledge/offers.yml) records the portfolio, shared service
roles, and development status. See the [foundation notes](strategy/README.md) for
source boundaries, open items, and conflicts to resolve before v2 integration.
These files are not yet loaded by the pipeline.
