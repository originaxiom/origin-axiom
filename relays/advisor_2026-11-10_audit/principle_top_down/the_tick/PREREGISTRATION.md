# PREREGISTRATION — two acts or one tick: what the tick gains and what it breaks

**From:** the advisor seat. **Written and committed before `tick_facts.py` is run.** Data-free: integers and SnapPy;
nothing is compared with measurement.
**The owner's word it follows:** 2026-11-10, R16.4 — the elementary act is not ruled until this is computed.
**Swept first:** B14 (the tick F = LP is the only integer square root of LR up to sign), B469 (every metallic bundle
double-covers a non-orientable one), B1607 (the owner's rule a ↦ ab, b ↦ a is the tick; its manifold is m000),
B1234 (eight banked walls pass through amphichirality, which an orientation double cover has by construction: 40 of
40), `GENESIS.md` SE2 ("the most fragile link"; "what dropping SE2 would break is not computed") and FK2. This run
does not redo them. It asks what changes in *what exists* and *what is told apart* if the tick is an act.

## The question, after R14 and R15

Not "which comes first": nothing is ranked. The question is **which acts the grammar has**. With two acts, a history
is a cyclic word in L and R. With the tick, a history is a cyclic sequence of run lengths of any length; the
sequences with an even number of runs are exactly the two-act histories, and those with an odd number are new.

## Definitions

As in `tick_facts.py`. The instrument's control was run before this file was committed, with no hypothesis read:
SnapPy's `b-+L` is the Gieseking manifold m000, non-orientable, of volume 1.014942, and its orientation cover is m004.

## What is run, with the seat's expectation of each

| # | Computed | Expectation (some derived by hand before sealing; the run is the check) |
|---|---|---|
| **T1** | the number of histories with n letters, n ≤ 12, with an even and with an odd number of runs | the tick adds roughly as many histories again as there are; no exact figure expected |
| **T2** | for every two-act history with at most 8 letters: amphichiral or not (SnapPy), against a combinatorial prediction — a history is its own mirror exactly when its cyclic run sequence returns to itself under a rotation by an odd number of places, or under a reflection that changes the parity of positions | the prediction agrees with SnapPy on every history. Every double of an odd sequence is amphichiral. Histories that are their own mirror in another way exist; the first history with a mirror partner has 3 letters |
| **T2b** | the histories with an odd number of runs, at most 5 letters: orientable or not; whether the orientation cover is the doubled sequence | none is orientable; every cover is the doubled sequence |
| **T3** | the groups generated mod N by {L, R} and by {L, P}, for N = 2, 3, 4, 5, 7, 8; the tick's action on the golden line mod 5; the fibre characters fixed or inverted by one tick and by two | the exchange is already inside ⟨L, R⟩ at N = 2 and at no other N, where the group doubles. Mod 5 the tick is 3 times a unipotent: it keeps the golden line and multiplies its points by 3, so it exchanges the two points-up-to-sign that the record treats as a binary choice of line. One tick fixes no non-trivial character and inverts none; two ticks invert the group of order 5 |
| **T4** | for a single act alone — L, R, the bare exchange, the tick — whether its fixed direction is rational | L, R and the bare exchange: rational, the subtraction ends. The tick: irrational, it never ends |

## What each outcome would mean (written first)

- **T4 as expected** bears on the owner's own clauses: under clause 3 and W3 ("not single objects alone") a single act
  that survives alone needs a reading. Either the tick is not an elementary act, or the objects in relationship are
  the two sides inside one tick and not two kinds of act.
- **T3 as expected** gives the tick's gain and its cost at the level in one fact: the two lines become one orbit, so
  the choice between them is not a choice; and the frame's line is no longer single-valued over one tick, only over
  two.
- **T2 and T2b as expected** say what the tick does to handedness: it adds histories with no hand at all, and the
  histories that are their own mirror "by construction" are exactly the doubles of those.
- **If the combinatorial prediction of T2 fails** on some history, the seat's account of the mirror is wrong there and
  the history is reported.

## Not computed here

Which of B1234's eight walls stand or fall with the tick; pin structures on the non-orientable histories; what the
record's structural chain needs of orientability. These are named in the result as owed.
