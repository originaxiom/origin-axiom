# B1439 PREREGISTRATION — THE CENSUS BY SLOPE: every signed word state to length twelve, by the slope law

**Sealed 2026-10-01, before the slope of any character is computed on a level outside B1434's population. Seat: cc
(main). Occasion: B1438 reduced the architecture census to one function and twenty seconds. The census's limit of
length six was a limit of compute. This arc removes it and asks the questions B1434 and B1435 left as residue
(lead L229): which states carry a generation at their own level, with which couplings.**

## 0. The quantifier (P0)

For every signed cyclic word state s = (ε, w), w of length 2 to 12 in L, R (both letters, primitive, up to rotation
and swap), and every level k ≤ 12 whose fibre torsion is at most 2 000: the generation-shaped backgrounds of the
level and, for each, which of its allowed couplings vanish. 758 states, 988 levels; 68 of them are B1434's and
serve as the control; **920 levels are new, 734 of them own levels (k = 1).** The scope sentence names no manifold.

## 1. The instrument

`verification/census_by_slope.py` (sha-256 in `ARTIFACT_HASHES.txt`), on B1438's `slope_census.py`:

- the monodromy-fixed characters by Smith form, each checked against the definition;
- s(χ) from its definition modulo two primes above 2·10⁹; two characters have equal slope when they agree at both;
- the index of every candidate module by B1438's Theorem A, the backgrounds assembled as in B1432's census;
- for every background and every allowed pair of firing sectors, whether s(ℓ) − s(η) vanishes (Theorem C).

No index and no cup product is computed. The two theorems are proved in B1438 and verified there on 942 268 modules
and 140 448 couplings.

**C1, the binding control, run before the seal:** the instrument on B1434's 68 levels returns B1434's record on
every field, and on B1435's 30 levels returns the sealed run's block totals of vanishing and non-vanishing
couplings. Record `control_run.txt`.

## 2. What has been seen before the seal (disclosed)

- Everything in B1434, B1435 and B1438: word length ≤ 6, torsion ≤ 330, k ≤ 6. In particular: two states fire at
  their own level, both with sign −: −LLRLR (8 backgrounds, none lifting, no ν^c) and −LLLRLR (16, all lifting,
  ν^c with the generation's sign); on all 24 the ten·ten couplings are non-zero and every coupling touching the
  five-bar or ν^c is zero. Ten of twelve three-fold levels carry backgrounds, all in deck orbits of three.
- One timing run on a level of the new population, the root's level seven (torsion 841): **only its torsion and its
  run time were printed** (7.9 s). No count was read.
- The sizes above (traces and torsions, from 2 × 2 integer matrices).

## 3. Sealed predictions (each can come out either way)

Own-level statements are about the **734 new own levels**. A block (ten·ten: Q·Q, Q·u^c, u^c·e^c; ten·five: Q·d^c,
Q·L, u^c·d^c, e^c·L) is *non-zero* when every coupling in it is, and *vanishes* when every coupling in it does.

| | prediction | prior |
|---|---|---|
| E1 | Some state with sign **+** carries a generation-shaped background at its own level. (None of twelve does to length six.) | 60% |
| E2 | At least 5% of the new states carry a generation-shaped background at their own level (37 or more of 734). | 60% |
| E3 | On **every** own-level background of a new state the ten·ten block is non-zero (an up-type coupling exists). | 55% |
| E4 | On **every** own-level background of a new state the ten·five block vanishes (no down or lepton coupling at the own level). | 35% |
| E5 | Some own-level background of a new state has Q·u^c, Q·d^c, e^c·L and L·ν^c all non-zero. | 30% |
| E6 | Every new state that fires at its own level has fibre torsion divisible by 3. (12 and 15 for the two known.) | 35% |
| E7 | On every new three-fold level (k = 3) that carries generation-shaped backgrounds, every deck orbit has size three. | 75% |
| E8 | Some background of a new level has the ten·five block non-zero and the ten·ten block zero (down and lepton without up). | 45% |

## 4. What each outcome would mean (written before the data)

- **E1 NO** on 367 new + states would make the sign a condition for carrying a generation at the own level, and
  the Gieseking-type half of the grammar the half that does.
- **E3 YES with E4 YES** would make "an up-type coupling and no down-type coupling" the law of the own level, on
  hundreds of states; either failing names the states that break it.
- **E5 YES** would exhibit a single state, at its own level, whose one generation has all four coupling types.
- **E6** is a guess at the law of which states fire; its failure is as useful as its success, because the list of
  firing states is the datum.
- None of the outcomes is a physical statement. The fence is B1438's: main's class index, non-semisimple
  backgrounds, an index is not a generation count, a coupling here is a number of the frame in the longitude
  normalisation and not a Yukawa coupling, the Clebsch–Gordan constants are not computed. 0 of 19.

## 5. Not in this arc

The values of the non-zero couplings (they are recorded modulo the two primes, not identified); words longer than
twelve; levels with torsion above 2 000; non-cyclic covers; fillings; the half-step states.

## 6. Hashes at seal

See `ARTIFACT_HASHES.txt`.
