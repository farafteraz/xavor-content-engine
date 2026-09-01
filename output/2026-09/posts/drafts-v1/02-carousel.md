# Post 2 — 2026-09-02 — carousel
**Angle:** Each of the four blockers between pilot and production kills a specific class of pilot, and evaluation gaps kill the most at 64%.

## Caption
"Not ready" is what a stalled pilot looks like from the outside. From the inside, it's usually one of four specific failures, and you can name which one killed each of yours. Evaluation gaps kill the most.

## Copy

**Slide 1:**
88% of agent pilots never reach production (Forrester/Anaconda). They don't all die the same death. Four blockers, and you can match each stalled pilot to the one that killed it.

**Slide 2:**
Evaluation gaps: 64% of failures. The agent worked in a demo and no one built the pipeline to prove it kept working on real inputs. This is the biggest killer by far.

**Slide 3:**
Governance friction: 57%. The agent passed testing and stalled at the approval it couldn't clear. No decision boundary, no escalation path, no owner who could sign off.

**Slide 4:**
Model reliability: 51%. The agent held up on clean cases and broke on the messy ones production actually sends. The demo hid the failure modes that mattered.

**Slide 5:**
Sort your stalled pilots into those three and the pattern shows: you didn't have a model problem. You had an engineering problem you can now scope. The ones that shipped paid it back in a median of 5.1 months.

**Slide 6:**
Map your stalled pilots to their blocker now. Get in touch.

## Evidence used
- [E17]: 88% of agent pilots fail to reach production; evaluation gaps 64%, governance friction 57%, model reliability 51% — used as the four-blocker spine across slides 1–4.
- [E18]: Origin/replication of the 88% figure (Anaconda/Forrester, replicated by a16z and MIT Sloan) — supports the confidence of the headline claim; not quoted directly.
- [E21]: Median payback of 5.1 months on agent deployments — used on slide 5 to close on the upside of getting through.
- Note: the three named blockers (64/57/51) sum past 88% because failures overlap, so slides frame them as classes of failure, not mutually exclusive buckets. No composite claim invented.

## Design note
Six clean slides on a consistent grid. Slide 1 leads with 88% at large scale; slides 2–4 each anchor on their single percentage (64, 57, 51) in the same position so the reader's eye tracks the descending count. Keep type sentence case, no icons that imply a metaphor.