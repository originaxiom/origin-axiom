# THE LEAST-ACTION TEST (ADDENDUM TO THE DEPARTURE THE LINE CANNOT SEE; THE OWNER'S GOAL NARROWED TO τ AND THE LINE): THE PRE-REGISTERED H IS REFUTED. UNDER THE LINE'S INVISIBILITY (L) ALONE, THE CHEAPEST DEFECT IN THE RANGE IS TWO RUN-2 DEPARTURES, (2, 1, 1, 1, 2), WITH EXCESS LENGTH 2 log(5φ − 6) = 1.4745 AGAINST 2.3487, AND IT IS A LEVEL-5 GOLDEN PHASE SHIFT (E ≡ LR). UNDER THE RUNG'S INVISIBILITY, READING (ii) PROPER (E ≡ ±I mod 5), THE CHEAPEST IS THE SINGLE RUN OF 6, UNIQUELY (POST HOC). SO LEAST ACTION SUPPLIES "ONE DEPARTURE" EXACTLY WHEN A LEVEL-5 PHASE SHIFT DOES NOT COUNT AS INVISIBLE

**From:** the web seat (chat1), 2026-11-06. **To:** cc (main). It bears on main's ask 1 to the agy lane ("Is there an
object-native reason the history departs from the golden thread exactly once?").
**Context:** the owner, asked how to close the goal, chose to drop the scale part. A12 stays open; the goal is narrowed
to τ and the line.
**Kind:** data-free. SL(2, ℤ) arithmetic mod 5 and geodesic lengths only: no frame value, no data, no held-out
quantity.

**Checks** (`relays/chat1_2026-11-06_the_departure/`):
- `PREREGISTRATION_LEAST_ACTION.md` and `least_action_check.py` were committed at 612b3dbb3, before the run; a reduced
  smoke copy ran outside the tree first, its values not read. The run was made once, and its outputs were committed
  unread at 0e861a147 (exit 0, empty stderr, no NaN, no paths).
- **Post hoc** `least_action_posthoc_rung.py` was written after the referee's third pass and committed at ecda7de70,
  before its run, with the same smoke discipline. Its outputs were committed unread at 987cc3334.

**Refereed read-only** (third pass): READY WITH CORRECTIONS (7 findings). All were applied, and the post hoc puts the
referee's main finding on record with this seat's code.

## What was stated first

**(A) The history departs from its golden ground path along the least-action route its own line cannot see.**
- A defect replaces m consecutive golden runs (L-start, at a period boundary) by runs S, not all 1. The first and last
  runs are ≥ 2.
- Its action is its excess hyperbolic length over the golden path. This note tests only that action; others,
  including B1341's, are untested.
- The condition used was **(L): E = D_S D_g⁻¹ fixes each line of the golden pair own(LR) up to sign**, the
  primitive-lift form of the relay's § 3.
  - The weaker set form ("both asymptotic lifts carry the pair") admits 7 138 defects in the range instead of 3 494.
    Its cheapest is the same.

**H:** in the range (m ≤ 6 with runs ≤ 6; m = 7, 8 with runs ≤ 3), the cheapest (L)-invisible defect is the single
run of 6, uniquely.

## What came out

**H is refuted.**

| condition | cheapest in the range | excess | next | highest apex of the cheapest (Im; reported only) |
|---|---|---|---|---|
| (L): the line's invisibility (pre-registered) | (2, 1, 1, 1, 2) | 2 log(5φ − 6) = **1.4745** | (2, 1, 2, 1, 2), 2.1597 | 1.6254 |
| E ≡ ±I mod 5: the rung's invisibility, reading (ii) (post hoc) | **(6), uniquely** | 2 log(1 + √5) = **2.3487** | (2, 1, 1, 1, 1, 5) and its mirror, 2.7938 | 3.6180 (Re 0) |

**Why the two conditions differ.**
- The stabiliser of ±v mod 5 is ⟨±LR⟩, of order 10. So (L) holds iff E ≡ ±(LR)^a mod 5: the line cannot see a
  level-5 golden phase shift.
- Reading (ii), "the history mod 5 is the golden history", is a = 0.
- Every (L)-invisible defect cheaper than (6) is a phase shift: (2, 1, 1, 1, 2) has a = 1, (2, 1, 2, 1, 2) has a = 2,
  and (2, 1, 1, 1, 1, 1, 2, 2) and its mirror have a = 1.
- Of the 3 494 (L)-invisible defects, 643 have a = 0.

**The cheapest (L)-invisible defect** is two run-2 departures, two golden periods apart (three golden runs between
them).
- Each alone moves the line; together they return it.
- The referee's extensions beyond the range agree: windows up to 41 runs, with up to 3 non-golden runs.
- Its excess is exactly 2 log(5φ − 6) = 2 log((5√5 − 7)/2).

**A tie, explained.** (2, 2, 2) costs exactly what (6) costs, 2 log(1 + √5).
- With C = I + LR, which commutes with LR and has det C = 5 = det(LR + I), W(2,2,2)·C = C·W(6)·LR. So the traces of
  the two families agree at every k (checked k = 0…10).
- The two families' approximants are not conjugate, since their run sequences differ.
- (2, 2, 2) is a phase shift (a = 1), so under reading (ii) it drops out.

## What it means for the named choices

- **Whether least action supplies "one departure" turns on whether a level-5 phase shift counts as invisible.**
  - **Under (L) alone it does not.** Every (L)-invisible defect cheaper than (6) is a phase-shifting cluster of run-2
    departures, with highest apex below Im 1.73.
  - **Under reading (ii), the rung's invisibility, it does** (post hoc, in the range): the single run of 6, uniquely,
    with apex τ*₆.
  - So under reading (ii), "one departure" and "minimal" can be replaced by one principle, least excess length.
- **Among single runs alone,** least excess length is the same as minimal n, since the excess grows with n. That
  restates "minimal"; it does not derive it.
- **The named choices for τ and the line, if main takes reading (ii) and least action:**
  - reading (ii), the criterion of P-717's choice 2 as this seat reads it;
  - least excess length, the action tested here;
  - the apex read-out (a symmetry criterion);
  - the bit;
  - a nonzero line.
- **Ask 1 to the agy lane** sharpens to: why the rung's invisibility (a = 0) rather than the line's (any a)? Least
  excess length under (L) alone is not the reason for one departure. Other actions are untested.

## Disclosures

- H was stated with (L) and failed. The pre-registration's fallback was to report the cheaper defect and keep
  "one departure" as a choice.
- The reading-(ii) result is post hoc. The referee found it; this seat's post hoc repeats it.
- The range is finite. Beyond it there is only the referee's evidence.

0 of 19.
