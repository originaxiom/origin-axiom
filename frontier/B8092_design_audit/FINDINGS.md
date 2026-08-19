# B8092 — THE DESIGN AUDIT: three places the prompts could only remove candidates

**Date:** 2026-08-19 · **Seat:** cc3 (audit) · **Verdict: NEGATIVE** for the design's neutrality on
three specific points; **no evidence of intentional bias anywhere.** Gate 5 untouched.

The owner routed the question: has **systematic negative bias** — in the seats or the gates —
shaped the outcomes? cc supplied the B1074 and B1076 orchestration scripts verbatim, and asked
that a design flaw producing *"a positive that ours structurally could not"* **outrank any
recomputation**. This is that audit. **The recomputations came back clean** (B1076's λ²(I), D_a=16,
D_b=11 all reproduced in-sandbox); these are findings about the *instructions*, not the arithmetic.

---

## FINDING 1 (headline) — the B1016 guard is STRICTER than the reopening condition it quotes

**cc did not name this one.**

The GUARDS block quotes the banked reopening condition **verbatim**:

> *"a crossing here must first exhibit a **FRAME-INVARIANT RESIDUE**, which B1016 says is **NOT the
> coupling's Re h** — none is currently banked; this lane is CLOSED until one is."*

The Hunt prompt then imposes:

> *"(4) THE B1016 GUARD per candidate: show it is not the coupling's Re h **(or any coupling-channel
> quantity)** in costume — the residue **must be PAIR-CHANNEL-NATIVE**."*

**The condition disqualifies one named quantity. The prompt disqualifies an entire class and adds a
positive requirement.** A residue that is genuinely **frame-invariant** but built from *both*
channels would **satisfy the banked reopening condition** and be **structurally excluded** by the
prompt before it could be evaluated.

**This is the shape cc asked for**: a defensible alternative design — one that filtered on
frame-invariance alone, exactly as the condition states, and disqualified `Re h` by name — could
have surfaced a candidate this one cannot. The strengthening is **defensible in spirit** (the lane
is the pair channel) but it is **a strengthening**, it is **undisclosed in the arc**, and it can
**only remove candidates, never add them**.

**What it does not show:** that such a residue exists. The lane may be genuinely closed. **The
finding is that the design could not have told us either way.**

---

## FINDING 2 — the MB12 bite-witness is per-candidate and redundant with the non-triviality test

cc probed this and answered *no*. **I think the answer is "no, except at one edge."**

The GUARDS demand *"every candidate needs both an invariance proof AND a companion frame-VARIANT
quantity as the bite-witness."* But the Hunt prompt **separately** demands *"(3) THE NON-TRIVIALITY
test per candidate (MB12): exhibit that the invariant's VALUE depends on the object."*

**(3) is the correct test for vacuity** — an invariant whose value would survive object-deletion is
empty, and (3) catches exactly that. The **companion-variant demand is a second, different filter**:
it asks that something *near the candidate* also vary. A real invariant **all of whose natural
companions happen to be invariant too** fails the second test while passing the first.

**A defensible alternative:** require **one global** bite-witness — the instrument demonstrably
detects frame-variance *somewhere* — rather than one per candidate. That establishes non-vacuity of
the instrument without letting a candidate's neighbourhood veto it.

*Recorded with a self-implicating note:* I strengthened exactly this kind of control in my own
B8089 today, from a bite covering 2 of 6 channels to all 6. **The purposes differ** — there I was
proving the *instrument* could bite; here the demand attaches to *each candidate*. Broad instrument
bites are right; per-candidate companion demands are the ones that over-kill.

---

## FINDING 3 — the grade enum has no rung for a positive-in-progress

cc probed the schema constraint and answered *no*. **The `notes` and `fail_witnesses` fields do give
qualitative content a home, so that half is right.** But look at the grade ladder:

```
grade: enum ['THEOREM-EXACT', 'COMPUTED-EXACT', 'COMPUTED-FLOAT-ORIENTATION', 'NOT-COMPUTABLE-HERE']
```

**Every claim must be exact, float-oriented, or not-computable.** There is **no grade for
established-but-partial** — no PARTIAL, no SUGGESTIVE, no PROMISING-UNPROVEN. A candidate that is
*real but only partly nailed down* has exactly one place to go: **NOT-COMPUTABLE-HERE**, which reads
downstream as a negative.

**This is asymmetric.** A partial *negative* is fully expressible ("computed exactly: not
invariant"). A partial *positive* is not. **The ladder is exact-or-nothing in a lane where the
honest answer is often "not yet".**

*The corpus has live tension here and I am part of it:* I invented a `PARTIAL` status earlier this
session and the B8076 lock **correctly rejected** it, because statuses must be enumerated and
enforced. **The lesson is not that PARTIAL is wrong — it is that an intermediate grade must be
designed in, not improvised.** Adding one rung to this enum is cheap; discovering post hoc that
every near-miss was filed as *not computable* is not.

---

## WHAT I DID NOT FIND

- **No evidence of intentional bias**, in the prompts or the gates. Every guard traces to a banked
  discipline (MB12, Gate 5, B1016, the exactness demand) applied consistently.
- **Gate 5's classes-only phrasing is sound** — cc's *"no-by-construction"* holds. The reopening
  condition asks for a frame-invariant *residue*, not a value match, so a classes-only search is
  faithful to it. A value-level search would be **value-matching**, which B724's look-elsewhere
  theorem already shows is worthless here.
- **The adversarial Verify phases are genuinely adversarial** — independent implementation, attacks
  on the inventory itself, and named classic defects (hardcoded-D2 reuse, absorbed normalizations,
  eigenvalue-ordering conventions). This is better verification design than most of what I audit.
- **The B1076 prompt's honesty clause is exemplary:** *"Either answer is the result — computed, not
  hoped."* That is the opposite of a biased instruction.

## THE SHAPE OF ALL THREE FINDINGS

Each is a place where a guard **can only remove candidates, never add them**, and where the
strengthening beyond the banked condition is **undisclosed in the resulting arc**. None of the three
shows the negatives are wrong. **All three show the design could not have produced the positive if
one existed** — which is precisely the question the owner asked, and the answer is *"in these three
places, no."*

## SCOPE

The B1074 and B1076 orchestration scripts as supplied verbatim, plus B1075's sealed preregistration
as its design record. **Not a re-audit of the arithmetic** — that ran separately and came back
clean. Says nothing about whether a frame-invariant residue exists.
