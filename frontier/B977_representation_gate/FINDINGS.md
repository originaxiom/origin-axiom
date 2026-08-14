# B977 — L143 EXECUTED: the gate for rows that were never written

**Date:** 2026-08-08 · **Seat:** cc (banking) · **Lane:** INSTRUMENT / GOVERNANCE.
Gate 5 untouched. **Built at the owner's instruction**, after B976 confirmed their report that
work around B862 had been lost.

---

## The rule

> Every **substantial** banked arc — non-instrument, PROVED or NEGATIVE, `claim_one_line` ≥ 500
> characters — that is cited on **no** synthesis surface must carry a disposition in
> `docs/REPRESENTATION_TRIAGE.md`: **PENDING** (a debt), **PROCESS** (correctly absent from an
> object atlas), or **SURFACE** (the arc *is* a surface).

Registered both directions: gate `representation-sweep` + a `docs/PRACTICES.md` row.

## The gap it closes — and why the other two gates could not

`lawmap-scope` (B966) and `retraction-sweep` (B967) both police the **content of rows that
exist**. **Neither notices a row that was never written.** That is exactly how eleven cascade
arcs — including **B864, which derives hypercharge** — sat invisible while a ledger row written
five days later called hypercharge *"OPEN — the sharpest available target"*, sending a lead, a
literature panel and a running workflow phase after a solved problem.

## The calibration, which is the interesting part

My first instinct was **file size**. It is wrong, and measurably so:

| criterion | catches, of the 11 lost arcs |
|---|---|
| FINDINGS ≥ 6 KB | **1 of 11** |
| `claim_one_line` ≥ 500 chars | **11 of 11** |

**B864's FINDINGS is only 3.7 KB** — short and dense. The result that cost us most was one of
the *smallest files*. What tracks substance is **how much the seat had to say about the claim**,
not how much prose surrounded it. Corpus median claim length is 161 characters; the lost block's
median is **918**.

At that floor: 99 substantial arcs, **17** cited nowhere, now all triaged.

## The debt, itemised rather than absorbed

**13 arcs sit at PENDING** — banked object results with no representation anywhere: the
cascade's ONE principle (B861), the Sakharov gate (B867), gates G4 and G7 (B869, B870), the
coset leg (B872), the measurement ladder (B874), the triality-tiling theorem (B875), the
period-5 hearing law (B856), the commensurability fact (B855), descent stage 2 (B881), the
composition hunt (B935), the flip-sign coset invariant (B938), and the OP theorem inside B859.

**Marking an arc PENDING does not discharge it.** It records that we know.

## Non-vacuity — demonstrated

Removing a triage row makes the gate **FAIL**; restoring it makes it **PASS**; the file was
restored byte-identical.

## Honest limits

1. **It enforces knowledge, not action.** An arc parked at PENDING forever satisfies the gate.
   The debt is visible; nothing forces its payment.
2. **The 500-character floor is calibrated on one incident.** A substantial result written
   tersely would slip under it. It is a floor, not a filter.
3. **Surfaces are a fixed list.** A result represented somewhere *not* on that list reads as
   unrepresented.
4. Being cited is not being cited *correctly* — that is `lawmap-scope`'s job, and it only
   inspects rows that exist.

---

**Verdict: INSTRUMENT.** The third gate is live, calibrated against the incident that motivated
it, and proven able to fail. **The day's three gates now cover: does the row say too much
(`lawmap-scope`), does a dead claim still live (`retraction-sweep`), and does the row exist at
all (`representation-sweep`).** None of them removes the need to read — but the class of loss
the owner described, and reported facing constantly, is now detectable rather than invisible.
