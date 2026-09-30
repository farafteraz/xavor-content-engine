# V2 opportunity review

The opt-in `opportunities.py` command proposes August content opportunities,
critiques each one, and stops for human review. It does not call `run.py`, fetch
Sentinel, generate a calendar, write posts, or record approval. Production's
scheduled workflow and default v1 routing remain unchanged.

## Inputs and stages

The runner loads the confirmed strategy, offering catalog, and website proof
library. It validates their references and assigns stable paragraph IDs to the
original August corpus. The corpus must match `output/2026-08/0-corpus.md` byte
for byte. This milestone supports August only so a different month's inputs
cannot be mistaken for the agreed comparison.

The strategy role proposes up to eight format-aware opportunities, each with a
reader benefit, a Xavor connection, and support for the claims it actually makes.
Commercial direction, buyer questions, experience, competitive observations, and
external signals are separate starting points. Business/technical comparisons
and news hooks are optional. It does not see the baseline. The editor role
then independently reviews the original sources and every candidate. It can
recommend, request revision, or reject all candidates. Its comparison with v1
must cite actual excerpts from the preserved briefs, calendar, or five posts.

Both calls use the existing hybrid router. By default only `OPENAI_API_KEY` is
needed for these two roles. The writer is never called. Existing strategy and
editor provider/model overrides still apply; changing a provider requires a
compatible model and its credential. The new optional role argument to router
validation leaves existing callers' validation of all roles unchanged.

The prompts in `prompts/opportunities/` apply the confirmed 50–1,000-employee
audience without importing the old Fortune 500 positioning. They preserve an
advanced register and explicitly distinguish user strategy from suggestions
embedded in digest text. Production's existing style file is unchanged.

## Prepare without credits

Install the repository requirements, then run:

```bash
python opportunities.py --month 2026-08 \
  --corpus output/2026-08/0-corpus.md \
  --output-dir work/august-opportunities-prepared --prepare-only
```

This validates and snapshots the inputs without making API calls. `PREPARED.md`
is explicit that no candidates or quality findings exist yet. Use a new, empty
directory on each run. Protected source and production directories are rejected,
including paths redirected there by symlinks.

## Generate for review

With funded access and the required credentials available:

```bash
python opportunities.py --month 2026-08 \
  --corpus output/2026-08/0-corpus.md \
  --output-dir work/august-opportunities-review
```

No calendar or writing stage follows this command. There is no automatic
continuation or approval flag. A future implementation needs explicit direction
to take reviewed opportunities further.

The `V2 opportunity review` GitHub workflow runs offline tests and prepares
inputs on relevant branch pushes. Its manual `generate` option defaults to
false. Enabling it calls the two funded model roles and uploads the results as
an artifact. The manual provider selector defaults to Claude (`anthropic`),
using the existing Anthropic secret for both roles. Select `openai` to compare
with the OpenAI configuration when funded. The local command retains its
existing hybrid defaults; use `STRATEGY_PROVIDER=anthropic`,
`EDITOR_PROVIDER=anthropic`, `STRATEGY_MODEL=claude-opus-4-8`, and
`EDITOR_MODEL=claude-opus-4-8` for the equivalent local Claude run. The workflow has read-only repository permissions and commits
nothing. Artifacts expire after 14 days.

## Artifacts

| File | Purpose |
| --- | --- |
| `inputs.json` | Exact strategy, evidence, corpus paragraphs, and baseline used |
| `corpus.md` | Original corpus paragraphs with linkable IDs |
| `prompt-snapshot.json` | Exact stage prompts used |
| `manifest.json` | Input and prompt hashes, code revision, model routes, run status, and empty human-approval field |
| `opportunities.json` | Validated candidate structure |
| `critique.json` | Validated critic assessments and baseline comparison |
| `review.md` | Human-readable recommendations, revisions, rejections, evidence, and comparison |
| `generator-response.txt`, `critic-response.txt` | Raw responses for diagnosing invalid output |

Raw responses are diagnostic material, never approved output. If parsing,
validation, or a provider call fails, the manifest records failure and no review
is produced. The completed earlier stage remains available for inspection.
Rerun into a new directory after resolving the issue. There is no automatic
schema-repair call or resumable generation in this milestone.

## Interpretation and limits

Reference validation and exact quote matching establish traceability. They do
not establish that a digest report is true or that a quoted source entails the
model's argument. The critic evaluates scope and reasoning, but remains a model
judgment. Human review and source verification remain necessary before publication.

Keep decisions require all five editorial dimensions to score at least 3 of 5,
no blocking evidence issues and no required changes. Writer notes, qualified
evidence that can be narrowly worded, and unused client-specific context do not
block a viable idea. Unsupported central claims still block; removable peripheral
claims need explicit writer instructions. These thresholds are implementation defaults, not measured
performance or user-confirmed campaign policy. Rejected ideas remain visible.

Publication history is unknown. The control sample is generated v1 work, not a
record of what was published. Novelty can be assessed against that sample and
within the candidate set only. The critic cannot prove improved finished-post
quality because this stage produces no finished posts. No content-history claims or invented market facts fill those gaps. The initial
competitive sample contains access-limited public examples, not complete history.

## Validation

```bash
python -m unittest discover -s tests -v
```

Tests exercise reference and quote rejection, review completeness, blocked
recommendations, all-rejected outcomes, output protection, partial failures,
credential selection, and the review stop with simulated model responses.
The existing v1 and hybrid pipeline regression tests also run. Passing these
checks demonstrates workflow behavior, not live model access or content quality.

## Input and review revision, September 30

`knowledge/editorial-inputs.yml` separates confirmed commercial/buyer context
from case-derived editorial questions. `knowledge/competitive-context.yml`
records a small, provisional public sample and its limits. These are loaded in
both model stages. The generator can support an evergreen idea without citing
a Sentinel paragraph. A competitive-gap hypothesis must cite an observed example.

The revised review distinguishes blocking problems, writer notes, and context.
The human report keeps the argument and editorial decision visible, with evidence
and optional planning details in expandable sections. Numeric scores remain
diagnostic model judgments, not the main review interface.

Schema version 2 adds format, reader value, starting point, writer notes, and
evidence impact. The archived first Claude run remains unchanged and uses the
older schema. No new live quality comparison has yet validated these changes.
The CLI is still the August controlled-comparison runner; October planning needs
a separately configured September research input, not relabeled August data.
