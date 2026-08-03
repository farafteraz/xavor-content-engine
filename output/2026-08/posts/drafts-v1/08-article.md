# Post 8 — 2026-08-18 — article
**Angle:** Agents fail in production on the context layer, and the operators who fixed it did semantic and data work the platform never shipped, which is why unified semantics moves accuracy and cost.

## Copy

### The reason your agents hallucinate is the layer no vendor sold you

Onstage at the Databricks summit this summer, Ali Ghodsi said the thing most AI budgets are built to avoid hearing. AI does not have an intelligence problem. It has a context problem. The model on your desk is smart enough. It just doesn't know what your columns mean, which of two tables is the source of truth, or that "active customer" is defined four different ways across four systems. So it guesses, confidently, and calls it an answer.

That guess is the failure mode nobody put in the pilot deck. When an agent works in a demo and falls over in production, the reflex is to reach for a better model or a longer prompt. The people running agents at scale have already learned that the model was never the constraint. At VB Transform this year, engineering leaders from LinkedIn, Walmart, and Zendesk landed on the same point independently: legacy infrastructure, not model choice, is what slows agents in production. KPMG has been tracking deployment blockers for eight straight quarters, and system complexity, orchestration, reliability, and traceability now sit above every other obstacle on the list.

Here is the part a data platform will not tell you when it sells you the runtime. The runtime executes agents. It does not define what your data means. That definition, the semantic layer, is work that stays on your side of the contract no matter how much platform you buy.

Gartner put a number on the cost of skipping it. Rita Sallam told the London Data and Analytics Summit that without unified semantics, agents are more likely to hallucinate, and that organizations who build that semantic foundation will see agent accuracy climb by up to 80% and agentic AI costs fall by up to 60% by 2027 [verify: exact figures and phrasing of the two Gartner projections]. Read those two numbers together and the shape of the problem changes. Accuracy and cost are not separate tuning knobs. A hallucinating agent retries, escalates, and burns tokens on answers it has to redo. When it can query a definition instead of inferring one, it gets the answer the first time and stops spending. The semantic layer is where both curves bend at once.

This is why the "we have a data problem" line has quietly become the honest opening for AI programs. Accenture's Manish Sharma said at Snowflake Summit that roughly 85% of clients have a data problem before they have an AI problem. Accenture then did the work that follows from believing it. The firm reorganized its 750,000-person workforce around seven C-suite personas on a single Snowflake data foundation, so an agent asking about talent or supply or finance queries one governed definition rather than reconciling seven. That is not a model project. That is semantics.

The uncomfortable insight for a VP of Data is what this reorders. You have probably been treating the agent program as a modeling and orchestration effort with a data dependency somewhere upstream. It is the reverse. The semantic and data foundation is the program. The agent is the thin layer that runs on top of it, and the platform ships that thin layer, not the foundation. Every dollar of accuracy and every dollar of cost the agent produces traces back to whether it could ask a clean question and get a governed answer. The vendors have every reason to leave that part to you. It is the part that carries their number and does not carry yours.

So the question to bring into your 2027 planning is not which agent platform to standardize on. Both major runtimes are capable. The question is whether an agent inside your environment can ask what a customer is, what revenue means, which record wins a conflict, and get one answer your governance team would defend at audit. If it can't, no model upgrade closes that gap, because the gap was never in the model.

Give your agents a data layer they can query without hallucinating, and the accuracy and the bill both move in your favor. Begin an assessment now. Get in touch.

## Evidence used
- [E36]: Ghodsi's "context problem, not intelligence problem" as the opening frame.
- [E37]: LinkedIn/Walmart/Zendesk at VB Transform — legacy infrastructure slows agents in production.
- [E38]: KPMG eight-quarter pulse — system complexity, orchestration, reliability, traceability as top deployment blockers.
- [E34]: Gartner/Sallam unified-semantics projection (up to 80% accuracy gain, up to 60% cost cut by 2027) — the core quantified claim, tied together to make the accuracy-and-cost point. Flagged [verify] on exact figures/phrasing.
- [E33]: Accenture/Sharma ~85% data-problem-before-AI-problem, and the 750,000-person / seven-persona / Snowflake foundation reorganization as the named operator proof.
- [verify: exact figures and phrasing of the two Gartner projections] repeated here for the reviewer.

## Design note
Plain sentence-case headline card, no stock robotics imagery. If a single visual is needed, use a clean typographic treatment of the two Gartner numbers (up to 80% accuracy, up to 60% cost) stacked, in the brand palette, nothing decorative.