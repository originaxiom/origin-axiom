# B1439 — THE CENSUS BY SLOPE: every signed word state to length twelve — one state in eight carries a generation at its own level, and fourteen carry one with every coupling

cc, 2026-10-01. Sealed at f80f0754 before the slope of any character was computed on a new level
(`PREREGISTRATION.md`, sha-256 `cdcbcfc8…`, SEAL_LEDGER). The instrument is B1438's slope law; no index and no cup
product is computed. **Verdict: PROVED** (the run is complete; slopes agree at two primes above 2·10⁹ with no
coincidence at one prime only; the control returned B1434 and B1435). **Predictions: E1, E2, E5, E8 YES; E3, E4,
E6, E7 NO.**

## The run

758 signed word states (length 2 to 12), 988 levels with fibre torsion to 2 000 — the 68 of B1434 as control and
920 new. Fifteen minutes of compute in total. **61 648 generation-shaped backgrounds; 52 848 on new levels.**

| level k | levels in range | carrying generation-shaped backgrounds |
|---|---|---|
| 1 (own) | 758 | **95** |
| 2 | 180 | 100 |
| 3 | 32 | 25 |
| 4 | 10 | 10 |
| 5 | 4 | 3 |
| 6, 7 | 2, 2 | 2, 2 |

## The own level (lead L229 (i))

**95 of 758 states carry a generation-shaped background at their own level: 49 of sign + and 46 of sign −.** B1434
had two, both of sign −, to length six. By word length (firing / all): 0/2, 0/2, 0/4, 1/6, 1/10, 3/18, 5/32,
10/56, 16/102, 27/186, 32/340 for lengths 2 to 12. The first of sign + is +LLLLRRR (length seven, torsion 12).

**Their couplings.** 9 376 own-level backgrounds:

| up (Q·u^c) | down (Q·d^c) = lepton (e^c·L) | neutrino (L·ν^c) | backgrounds |
|---|---|---|---|
| yes | no | no, or no ν^c mode | 4 232 |
| no | no | no, or no ν^c mode | 3 800 |
| yes | yes | no ν^c mode | 584 |
| no | yes | yes, or no ν^c mode | 504 |
| **yes** | **yes** | **yes** | **256** |

**Fourteen states carry, at their own level, a background with all four couplings non-zero.** The shortest:

| state | torsion | exponent | backgrounds (lifting) | complete ones |
|---|---|---|---|---|
| **+LLRLRRLR** | 36 | 6 | 16 (0) | **all 16** |
| +LLLRLLLRR | 36 | 12 | 40 (8) | 8 |
| +LLLLLRLRLR | 48 | 12 | 24 (0) | all 24 |
| −LLLLLRRLRR | 48 | 12 | 24 (0) | all 24 |
| −LLLRLRLRRR | 72 | 12 | 80 (16) | 16 |

and nine more at lengths eleven and twelve (`census_summary.json`). On +LLRLRRLR every background is one
generation with its ν^c and with an up, a down, a lepton and a neutrino coupling, on a manifold that is its own
level: nothing is covered and no deck acts.

**No criterion found.** Torsion divisible by 3 holds for 71 of the 95 and fails for 24 (it holds for 209 of the
663 that do not fire). Non-cyclic fibre torsion is enriched (54 of 95, against 194 of 758) and is neither necessary
nor sufficient. The list is the datum.

## The three-fold levels

Of the 20 new three-fold levels in range, 15 carry backgrounds. On 14 every deck orbit has size three. On the
fifteenth, the three-fold level of −LLRLR, the eight backgrounds are the state's own, pulled back and fixed by the
deck: no new one appears. Five are silent (+LLRLR, +LLLRR, −LLLRR, +LLLLRR, −LLLLLRR).

The root's tower continues as B1427 found it on lifted backgrounds: level seven, torsion 841, 3 136 backgrounds,
all lifting, in orbits of seven.

## The sealed predictions, read (`verification/read_census.py`, record `census_summary.json`)

| | prediction | prior | outcome |
|---|---|---|---|
| E1 | some + state fires at its own level | 60% | **YES** (49 do) |
| E2 | at least 5% of new states fire at their own level | 60% | **YES** (93 of 734, 12.7%) |
| E3 | ten·ten non-zero on every own-level background of a new state | 55% | **NO** |
| E4 | ten·five zero on every own-level background of a new state | 35% | **NO** |
| E5 | some own-level background has Q·u^c, Q·d^c, e^c·L and L·ν^c all non-zero | 30% | **YES** (256 backgrounds on 14 states) |
| E6 | every new state firing at its own level has torsion divisible by 3 | 35% | **NO** |
| E7 | every new firing three-fold level has all deck orbits of size three | 75% | **NO** (one level: pulled-back, deck-fixed) |
| E8 | some background has ten·five non-zero and ten·ten zero | 45% | **YES** |

Four of eight came true where 3.95 were expected. E7 failed on a case its wording did not exclude and its author
should have seen: a state that fires at its own level carries those backgrounds to every cover.

**A defect in the sealed reader, recorded.** `read_census.py` collects `census_by_slope_*.json`, a pattern that also
matches the summary it writes beside them; a second run then fails on its own output. The reader is sealed and is
not edited: its summary is kept at the arc's root as `census_summary.json`, outside the pattern. The reading above
was made by the first run, before the file existed, and the lock re-runs the reader on the four records and
compares. ERROR_LEDGER E52 (a verifier defect), self-caught by the lock.

## What it means, and the fence

- **B1434's two own-level states were the first of many.** "The root cannot carry a generation at its own level"
  stands; "few states can" does not. The pattern "up without down", which the two showed, is the commonest and is
  not the law.
- **A complete single generation exists at an own level** — on fourteen states to length twelve, the shortest of
  length eight. By B1440 no flat bundle of rank five or less on such a manifold carries three, and by B1438 a
  generation's copies on a cover do not mix. So this is the frame's best single object, not a route to three.
- **The fence is unchanged:** main's class index on non-semisimple backgrounds; an index is not a generation count;
  the frame is carried to every state as an instrument; a coupling is a number of the frame; E₆'s Clebsch–Gordan
  constants are not computed; nothing selects a state. 0 of 19.

## Registered

L229 (i) has its data and no law. The values of the non-zero couplings on the fourteen complete states are
differences of slopes and are recorded modulo two primes, not identified.

## Verification

`verification/census_by_slope.py`, `read_census.py` (sealed), records `census_by_slope_0..3.json`,
`census_slice_*_run.txt`, `control_run.txt`; `census_summary.json` at the arc's root. Lock:
`tests/test_b1439_census_by_slope.py`.
