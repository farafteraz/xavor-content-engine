# Xavor Content Engine — project notes

## What this is
A monthly pipeline: weekly Sentinel digests in, a finished LinkedIn calendar + 15
publishable post drafts out. `README.md` covers setup, running, and tuning. The one
human step is reviewing `output/<month>/3-calendar.md` and `output/<month>/posts/`.

## Commands
- Full run: `.venv/bin/python run.py --month YYYY-MM [--corpus file]`
- Tuning loop: edit a file in `prompts/`, then rerun with `--from-stage N` (artifacts
  from earlier stages are reused; finished drafts/QC are skipped, so delete a post file
  to regenerate it).

## Binding rules for any writing in this project
- `brand/style-spec.md` is the style contract (distilled from `brand/about-me.md` and
  `brand/ANTI AI WRITING STYLE.md`). It binds Claude in chat here too, not just the
  pipeline: no em dashes, no reframe structures ("not X but Y" in any form), no banned
  vocabulary, one idea per piece.
- Every market claim must trace to the month's Sentinel corpus (the evidence ledger in
  `1-strategic-brief.md`) or carry a `[verify]` flag. Never invent figures.
- Watch for base-population transplants: a real number attached to the wrong statistic
  is the failure mode per-post QC is most likely to miss. After a run, a fresh-context
  audit of final posts against the raw corpus (not the ledger) is worth doing.

## Facts about the setup
- Sentinel (github.com/farafteraz/Xavor-Sentinel) runs Sundays via GitHub Actions and
  emails digests. Digest persistence to the repo's `digests/` folder requires the patch
  in `sentinel-patch/README.md`; until merged, runs need `--corpus`.
- `samples/june-sentinel.md` is RTF despite the extension; converted copy lives at
  `digests/2026-06-corpus-raw.txt`.
- Generation model is Opus-class via `CONTENT_MODEL` (default `claude-opus-4-8`); key
  comes from `.env` (gitignored) or the `ANTHROPIC_API_KEY` env var.
- Monthly trigger: `.github/workflows/content-engine.yml`, activates once this folder is
  pushed to GitHub with the `ANTHROPIC_API_KEY` Actions secret set.
- Channel truth: LinkedIn organic only, ~15 posts/month, formats limited to carousel,
  case-study carousel, explainer reel, video feature, article, static. No webinars, no
  paid, no other social platforms.
