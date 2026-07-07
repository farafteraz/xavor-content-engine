# Editor's Memo — Post 11 (carousel, N5)

**Overall verdict: FAIL.** One mechanical hit on structures (§6.6, the "This is" unveiling) and one on formatting/word-adjacent — actually the structure hit is the clean fail. The draft is otherwise strong: specific, well-sourced, and it earns its cognitive-depth moment. The fix is small and surgical.

---

## Per-check results

**V — Vocabulary: PASS.** Scanned word by word. No banned terms. "Dynamic" appears only inside the ledger-sourced phrase "short-lived dynamic agents" (E47) as a technical descriptor of agent behavior, not the banned figurative "dynamic." Acceptable. No "seamless," "robust," "scalable," etc.

**S — Structures: FAIL.**
- Slide 5: "This is identity engineering, not a policy checkbox." Two hits in one sentence. First, a §6.6 "This is" unveiling opener. Second, a §6.1 contrastive negation ("X, not Y") that is not correcting a specific fact, number, date, name, or scope — it's the rhetorical reframe the spec bans outright.
- Slide 3 opens "So the identity you have to govern is..." — the "So" is a legitimate real transition carrying the argument forward, not a cliffhanger pivot. Passes.
- Slide 1: "An external agent is neither." This corrects a specific scope claim (IAM governs people and services; an agent is neither category) — allowed under the §6.1 exception for correcting scope. Passes.

**M — Metaphor: PASS.** No analogies, no banned setups, no metaphor verbs. "Touches forty systems," "nothing to bind to," "load-bearing phrase" (design note only) are literal. Clean.

**F — Formatting: PASS.** No emojis, hashtags, exclamations, bold/italics/caps in body copy, no em dashes. Slide word counts: S1 ~30 — **borderline over the ~25 cap.** Count: "Your IAM governs people and services. An external agent is neither. It spins up, touches forty systems, and is gone before your access review runs." = 29 words. S2 = 28. S3 = 27. S4 = 26. These exceed the ~25 guide. The tilde makes this soft, and the sentences are full thoughts rather than confetti, which the spec prefers. Not failing F on this alone, but see edit notes — tighten.

**E — Evidence: PASS.**
- "MCP is now standard across ServiceNow, Salesforce, and Oracle" — E43 (ServiceNow), E45 (Salesforce), E9 (Oracle Integration, projects as MCP servers). Supported. Note E9 carries a [verify: single-source] flag; the draft's Oracle claim is soft enough ("standard across") to survive, but flag it.
- "ServiceNow's Action Fabric opens the workflow runtime to external agents" — E43, exact.
- "Salesforce hosts MCP servers Claude and ChatGPT can query directly" — E45, exact.
- "Traditional IAM and RBAC were not built for that speed or that spread" — E47, exact.
- "touches forty systems" and "spanning hundreds of services" — E47 says "hundreds of services." The "forty systems" in S1 is a concrete illustrative number not in the ledger. It reads as invented specificity. Minor, but flag it: either source it or make it "dozens" / align to the "hundreds" the ledger supports.

**O — One thing: PASS.** The post argues one thing: identity for agents is now its own engineering problem because IAM/RBAC can't govern short-lived, dynamic, multi-service agents. Matches the slot angle exactly and ladders to the operability gap (the constraint moved up a layer to operation, here specifically identity). Clean.

**L1 — Interchangeability: PASS.** Swap MCP for another protocol and the argument breaks — the whole point is that MCP's win is what put external agents against your workflow runtime. Swap RBAC and the mechanism (role assigned once, audited later, nothing to bind to) stops being true. Specific to the named tech.

**L2 — CTO respect: PASS.** A security architect would nod at "The role model has nothing to bind to" and "scoped to one task, expiring on completion." This is real engineering, not content marketing.

**L3 — Cognitive depth: PASS.** The "I hadn't considered that" moment: Slide 4, "RBAC assumes a role you assign once and audit later. An agent's scope changes per task, per data source, per invocation. The role model has nothing to bind to." That reframes IAM's failure as structural, not a tooling gap. Lands.

**R — Rhythm/human: PASS.** Varied lengths, real transitions, reads like a sharp person talking. Not metronomic. CTA lands naturally in the "now" register.

---

## Edit notes

The draft fails on one sentence. Fix it and it ships.

1. **Slide 5, rewrite the opener.** Cut "This is identity engineering, not a policy checkbox." It's both a "This is" unveiling and a banned contrastive negation. Replace with a direct positive claim that leads with the subject. Suggested: "Identity engineering is the work here. Every agent needs its own credential, scoped to one task, expiring on completion, logged to a system that can answer who touched what." If you want the "not a checkbox" force, you must earn it with a specific rather than a rhetorical negation — but simplest is to just delete the negation entirely; the positive sentence carries the weight alone.

2. **Slide 1, resolve "touches forty systems."** No ledger support for "forty." Either change to language the ledger backs ("touches dozens of systems" is safer, or align to E47's "hundreds of services") or accept it as illustrative and flag. Cleanest: "It spins up, touches dozens of services, and is gone before your access review runs." This also trims the word count.

3. **Tighten slides 1–4 to the ~25-word cap.** All four run 26–29. Trim without staccato-chopping. E.g. S1: "Your IAM governs people and services. An agent is neither. It spins up, touches dozens of services, and is gone before your access review runs." (25).

4. **Optional verify:** the Oracle MCP claim rests on E9, which is single-source/[verify]. The draft's phrasing survives, but a human should confirm Oracle Integration's MCP-server capability before publish.

```json
{"verdict": "FAIL",
 "checks": {"V": "PASS", "S": "FAIL", "M": "PASS", "F": "PASS", "E": "PASS",
            "O": "PASS", "L1": "PASS", "L2": "PASS", "L3": "PASS", "R": "PASS"},
 "verify_flags": ["E9: Oracle Integration MCP-server capability is single-source/Strength Medium — confirm before publish", "Slide 1 'forty systems' has no ledger support — source or replace with ledger-backed figure"],
 "edit_notes": "Slide 5: delete 'This is identity engineering, not a policy checkbox.' — it is both a §6.6 'This is' unveiling and a §6.1 banned contrastive negation (not correcting a fact/number/date/name/scope). Replace with a direct positive claim leading with the subject, e.g. 'Identity engineering is the work here. Every agent needs its own credential, scoped to one task, expiring on completion, logged to a system that can answer who touched what.' Slide 1: 'touches forty systems' is invented specificity with no ledger entry (E47 supports 'hundreds of services'); change to 'touches dozens of services' or align to E47. Tighten slides 1-4, which run 26-29 words, back under the ~25 cap by trimming words, not by chopping into fragments. Optional: human should verify the Oracle MCP claim (E9 is single-source/[verify])."}
```