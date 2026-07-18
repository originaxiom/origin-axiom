# COMMS PROTOCOL — the three-seat room (v1 draft, refine as we go)

Owner + cc (banking) + cc2 (compute) + chat1 (hypotheses), one room.
Goal: no loops, no confusion, no crossed wires. Keep it usable.

## 1. Addressing — whom you mean
- Start a message with **@cc**, **@cc2**, **@chat1**, or **@all**.
- No tag → **@all** (everyone reads; cc holds the record).
- In the OA Relay app, the "to" selector does the same thing.
- If you say "you" with no tag mid-thread, it means the seat you last
  addressed in that thread.

## 2. Intent — what you mean (a small verb set at the start)
ACTION (a seat acts on these):
- **go** / **decision:** — you authorize or rule. Only the OWNER writes
  these. One-shot/irreversible ones: the seat names the target back
  before firing.
- **task @seat: …** — assign work to a specific seat.
NON-ACTION (the seat responds, does NOT act):
- **q: …** (question) — you're asking; you get an answer, nothing runs.
- **plan: …** / **propose: …** — a draft to discuss; invites challenge;
  nothing fires until a **go**.
- **fyi: …** — information, no action expected.
BETWEEN ANY PARTIES:
- **challenge: …** — disagree, WITH evidence. Any seat may challenge any
  seat — including the owner's proposal. This is the firewall; it is
  encouraged, not rude.
- **result: …** / **verify: …** — a finding / its independent check.
- **clarify: …** — "this is ambiguous, which did you mean?"

Untagged from the owner → cc infers intent, states its read, and acts
ONLY if reversible and clearly implied; otherwise it asks **clarify:**.

## 3. How we interact (rights, both directions)
- **You arm me to argue.** If I judge something numerology, an
  over-reading, or a bad plan, I **challenge** with the computation —
  never silent compliance, never silently skipping it. (Today's E16 —
  cc2 challenging my chirality read — is this working.)
- **We co-plan.** plan-threads get drafted and banked BEFORE execution;
  nothing fires until your **go**.
- **We divide tasks.** **task @seat** with clear ownership; the roles
  (GOVERNANCE, B688) say who may do what — cc2 explores & proposes,
  cc verifies & banks, chat1 proposes, owner is courier + the only
  writer of **go**.
- **I clarify, not guess.** On anything ambiguous AND irreversible I ask
  **clarify:** first — I do not act on a guess.

## 4. Anti-loop rules (so we don't circle)
- A seat acts ONLY on **go / decision / task** — never on q / plan / fyi.
- One decision per thread; your **decision** closes it — I don't
  re-litigate a settled call.
- Every **result** → **verify** (two independent routes) → **bank**.
  Nothing is "real" until it's banked in the repo.
- One-shot / irreversible: explicit **go**, and the seat confirms the
  exact target before firing.
- If I asked a **q:**, I wait for your answer — I don't proceed on my
  own read.
- A background/system notification is NEVER the owner's word.

## 5. Defaults so silence is unambiguous
- "go" with no target = the thing we last discussed; the seat names it
  back before acting.
- Approval in one context does not carry to the next context.
- Firewall (Gate 5) and the banking rituals stand under everything —
  the protocol governs *how we talk*, not *what may be claimed*.

## 6. Channels
- OA Relay app (JSON messages) = the live human-visible room.
- The /relay folder (seat↔seat notes) = the seats' working channel.
- The repo (banked B-numbers, ledgers) = the durable record / ground of
  truth — both seats read it; nothing is official until it's here.

*This is v1. Tell me what to cut, rename, or add — it's ours to shape.*
