# STAGE 3 — MONTHLY CONTENT CALENDAR

You are Xavor's content lead. Using the creative brief below, populate the full monthly
LinkedIn calendar for {MONTH}. Every slot must have a clear reason to exist and a visible
connection to the month's big idea. A slot that merely "covers a topic" is dead weight.

## Cadence and mix (match Xavor's operating pattern)

- **15 posts** across 4 publishing weeks. LinkedIn only, organic only.
- Post on weekdays, roughly Tue–Fri, ~4 posts per week (one week may carry 3).
- **Format mix for the month** (exactly): 4 carousels, 2 case-study carousels,
  4 explainer reels, 2 video features, 2 articles, 1 static post.
- Every week ships at least one carousel and one explainer reel.
- The two articles anchor: one launches the big idea in week 1, one lands a deeper
  proof-of-thesis in week 3 or 4. No two consecutive posts share a format.
- Each week has a named sub-narrative (an arc): week 1 sets the thesis, weeks 2–3
  develop territories, week 4 lands the proof and converts. The four weekly arcs must
  read as one argument unfolding, and each must ladder to the big idea.

Publishing weeks for {MONTH}: {WEEKS}

## Slot discipline

For every post define:
- **date** (YYYY-MM-DD, a weekday within the week)
- **format** (one of the six above)
- **territory** (N# from the creative brief)
- **job**: what this post does to the reader in one sentence — the change it causes
  (e.g. "makes a CTO question whether their agent rollout has an owner"), never "raise
  awareness of X".
- **angle**: the ONE thing the post says, as a full claim-sentence. This is the
  single-mindedness contract: the drafting stage may not add a second idea. Two slots
  may share a territory; they may never share an angle.
- **audience**: the specific roles this post is for.
- **cta**: the closing move, in the "[Outcome] now" register. Vary wording across the
  month; never "learn more".
- **evidence**: the E# ledger entries the post will lean on (1–4 of them). Only slots
  whose angle needs a stat get stats; a point-of-view slot may carry none.
- **why_this_slot**: one sentence on why this post exists in this week of this month —
  the reason it earns its place in the arc.

Sequencing logic matters: time-sensitive evidence (deadlines, GAs, events) must land
before it expires; proof and conversion posts come after the thesis has been argued,
not before.

## Output format

First, the human-readable calendar in markdown:

# Content Calendar — {MONTH}
## The big idea (one line, restated)
## Week 1: {arc name} ({dates})
(one line on the week's sub-narrative and how it ladders)
Then each post: **Post NN — {date} — {format}** followed by the slot fields.
(Repeat for weeks 2–4.)

Then, EXACTLY this machine-readable block, fenced, as the last thing in your reply:

```json
{"posts": [{"n": 1, "date": "...", "format": "...", "territory": "...", "job": "...",
"angle": "...", "audience": "...", "cta": "...", "evidence": ["E1"],
"why_this_slot": "..."}]}
```

The JSON must contain all 15 posts and match the markdown exactly.

---

## CREATIVE BRIEF

{CREATIVE_BRIEF}

## EVIDENCE LEDGER (from the strategic brief)

{LEDGER}
