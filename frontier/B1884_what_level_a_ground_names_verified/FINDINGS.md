# B1884 — The web seat's card on what level a ground names, verified on main

*Main, 2026-11-11 (S306p). The record now holds, as a postulate, that a ground is the act itself: the tick, at level
5. The web seat stress-tested the sentence that gives the tick its level, with a sealed card pushed before its run.
This arc verifies the card with main's own code. Integers only. A thread result: it is about one history, the
ground. 0 of 19.*

## 1. The answer first

- **Every prediction of the card is reproduced:** 17 checks, none failing, on the first run.
- **The tick has its level by one reading only, the discriminant.** The tick and its square have the same
  discriminant, 5. That is the reading B1876 used, and it stands.
- **A second reading on record does not reach the tick.** The rule of a history's own lines gives the tick no line
  at any level. The line of order 5 that this rule finds belongs to the tick's square.
- **A third reading singles out 5, if it is worded exactly.** The ground carries a line to itself, as a set, at many
  levels. Only at 5 is there exactly one.
- **So the foundation's entry for the ground must say which reading it uses.** Given the ground and the
  discriminant, the level follows and is not a further input. It may not cite the own-line rule for the tick's
  level: that rule gives the tick none.

## 2. The card, prediction by prediction

Rows as vectors, as the seat writes them. L has rows (1, 0), (1, 1); R has rows (1, 1), (0, 1); P exchanges the
sides; the tick is F = L·P, with rows (0, 1), (1, 1); F′ = P·F·P is its other side. N runs from 2 to 200.

| the seat's prediction | main's result |
|---|---|
| P0: the controls | F² = L·R, F′² = R·L, P·L·P = R, F′ = R·F·R⁻¹, both of determinant −1. v₀ = (1, 3) has v₀·L·R = −v₀ and v₀·F = 3v₀ modulo 5 |
| P1: the invariants | det(F − I) = −1 and det(F + I) = 1. det(L·R − I) = −1 and det(L·R + I) = 5 |
| P1b: by brute force | to N = 200 the tick and its other side keep no primitive vector up to sign at any N. The square keeps four at N = 5 and none elsewhere |
| P2: lines kept as sets | for each of the four and every N to 200, as many as the roots of x² − x − 1 modulo N. Exactly one at N = 5 and at no other N. Two at 11, 19, 29, 31, 41, 55, 59, 61, 71, 79, 89, 95 and on; none elsewhere |
| P3: at level 5 | the tick moves the four vectors of its line in one orbit of length 4. Its square moves them in two of length 2 |
| P4: among odd histories | of the 87 non-negative matrices of determinant −1 with entries to 8, exactly two have no line of their own at any level: the tick and its other side |

**Why P1b and P4 hold beyond the card's range.** For determinant −1 and trace s, det(g − I) = −s and
det(g + I) = s. Main checked that identity on all 87. So a history with an odd number of ticks has no line of its
own exactly when its trace is 1, and that is the tick.

**The seat's table of the seven other root histories** (reported there, not predicted) is reproduced to N = 60:

| history | trace | discriminant | exactly one line kept at N = | a vector kept up to sign at N = |
|---|---|---|---|---|
| L²R, LR² | 4 | 12 | 2, 3, 6 | 2, 3, 6 |
| L³R, LR³ | 5 | 21 | 3, 7, 21 | 3, 7 |
| L⁴R, LR⁴ | 6 | 32 | 2 | 2, 4, 8 |
| L²R² | 6 | 32 | none | 2, 4 |

So "exactly one line" is not a rule that finds a ground: two of these histories name one level by it, four name
three, and one names none.

## 3. What main adds

- **The same counts in B1872's convention** (columns, the ground [[2, 1], [1, 1]], the mark (1, 2)): the ground keeps
  four vectors up to sign at N = 5 and none at another N to 60, and its tick keeps none.
- **The brute-force form of P4** to N = 40: the same two matrices and no other.

## 4. What it does to the budget, and to the foundation's next version

- **Nothing leaves the budget.** The ground is a postulate.
- **The entry to be written (P-767) says:** the ground is the tick; its level is the prime its discriminant is, 5;
  that reading is part of the postulate; the mark is not fixed by it.
- **Two sentences it must not contain:** that the tick has a line of its own at level 5 (it has none at any level),
  and that "a canonical invariant" selects 5 without the word "only".
- **"Exactly one" and "least" cannot be told apart by this card:** 5 is also the least N at which a line is kept.
  The first is a property of that level alone; the second compares levels.

## Seen first

- **The repo sweep:** the seat's ten sweeps of main stand in its relay, with the four of its referee. On record and
  used: B1876 (the atoms, the discriminants, H13 at level 5), B1845 § 1 and § 2, B1733's rule of own lines, P-721,
  P-738, P-718, B1323. Not on record before: the own-line rule applied to the tick at every level; the count across
  levels of the lines kept as sets; that among odd histories only the tick has no line of its own.
- **The literature:** the count of roots of x² − x − 1 modulo N is classical. Main computed it and proves nothing.

## Disclosed

- **The card was read by main about an hour after it was pushed,** in the same harvest as the seat's two earlier
  relays.
- **The expectations were written before the run,** in the script's header. All held; none was a surprise, since the
  card's own arguments are short.
- **The seat reports that the owner asked it to stress-test his rulings** ("id love if we can stress teat some of
  them", "order ok"). Under the rule of 2026-11-11 that is an order of work said to a seat; main enters it as his
  and lists it in its report.

## Reproduce

```
python3 -B frontier/B1884_what_level_a_ground_names_verified/verification/ground_level_on_main.py
python3 -m pytest -q frontier/B1884_what_level_a_ground_names_verified/verification/
```
