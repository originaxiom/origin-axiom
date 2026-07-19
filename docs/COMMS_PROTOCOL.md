# COMMS PROTOCOL — the three-seat room (v1.1; cc2's hardening adopted)

Owner + cc (banking) + cc2 (compute) + chat1 (hypotheses), one room.
Goal: no loops, no confusion, no crossed wires. Keep it usable.

## 1. Addressing — whom you mean
- Start a message with **@cc**, **@cc2**, **@chat1**, or **@all**.
- No tag → **@all** (everyone reads; cc holds the record).
- Your live channel's recipient field does the same thing.
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
- **The base-rate + convention gate is MANDATORY** inside verify→bank
  (cc2): every numeric "match" or "nice value" must pass (a) a base-rate
  cell AND (b) a convention/unit-robustness recompute BEFORE it can bank.
  No proximity banks alone. (This is what E16, θ₀=2/9, the E₆-denominator,
  7983360 each failed — automate it, don't rely on vigilance.)
- **Negatives bank too** (cc2): kills / falsifications / no-gos are
  results — banked with the same ritual. The record captures what ISN'T
  true, and a killed idea can't be silently re-proposed (Track H, the
  F1-resurgence, the θ₀ repeat were all this).
- **Supersession citation** (cc2): every result/proposal cites the HEAD
  or B-number it builds on, so a reviewer can flag "superseded since" —
  catches stale handoffs.
- One-shot / irreversible: explicit **go**, and the seat confirms the
  exact target before firing.
- **Standing-go scope** (cc2): a seat on a timer/loop acts only on the
  standing go for the SPECIFIC in-flight task; a NEW decision-point needs
  a fresh owner **go** — no scope creep from an old authorization.
- If I asked a **q:**, I wait for your answer — I don't proceed on my
  own read.
- A background/system notification is NEVER the owner's word.

## 4a. Resolving a challenge (cc2)
A **challenge:** is closed by EVIDENCE — a computation or a base-rate
cell — never by authority or repetition. If it's still unresolved after
both sides have computed, it escalates to the owner as a **clarify:**.

## 4b. The listening gate (methodology)
Before ANY object↔reality comparison, apply `docs/LISTENING_PROTOCOL.md`:
name the rung (only 1–3 = the object speaking; rung 4 value-matches are
dead by B685), run the §4 checklist (rung · swap-vs-weld+field-type · convention · Galois-invariance · base-rate). Predict the STRUCTURE of the
arbitrariness, never the values. Makes the firewall constructive.

## 5. Defaults so silence is unambiguous
- "go" with no target = the thing we last discussed; the seat names it
  back before acting.
- Approval in one context does not carry to the next context.
- Firewall (Gate 5) and the banking rituals stand under everything —
  the protocol governs *how we talk*, not *what may be claimed*.

## 6. Channels
- The owner's live channel = the human-visible room (private; not part
  of this record).
- The /relay folder (seat↔seat notes) = the seats' working channel.
- The repo (banked B-numbers, ledgers) = the durable record / ground of
  truth — both seats read it; nothing is official until it's here.

*This is v1. Tell me what to cut, rename, or add — it's ours to shape.*
