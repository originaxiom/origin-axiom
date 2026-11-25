# B1989 — Listening 6: the whole's bound states over ℂ sit at the frustration levels κ = 2cos(2πk/n), n ∈ {1, 2, 3, 4, 5, 6, 10}; the golden levels ±φ and ±1/φ come only from the icosahedral ones

**Verdict: PROVED (exact over cyclotomic fields; the source of finite orbits is certain, its completeness not claimed).**
Main, 2026-11-25. Unattended, on the listening line. Data-free. Register rows P-882 and P-630. **0 of 19.**

## Seen first

- **B1988:** the one self-consistent outcome is the common point, and values can only live in the flow away from it.
- **B1983:** over 𝔽_p the leaves κ = 0, ±1 and 2 split into several orbits.
- **Swept:** `VERDICT topic-sweep /finite orbit|bound state|binary icosahedral|2I|icosian|finite image|2cos\(2/: 48 of 1730 arcs on main match (NEGATIVE 6, OPEN 1, PROVED 41); 16 register rows match (DONE 12, LEAD 1, QUEUED 3)`. The record knows the icosahedral group and finite images in other frames. None lists the moves'
  bound states with their frustration levels.
- **The literature:** a representation into a finite group has a finite orbit under the moves (standard). The
  classification of all finite orbits of the moves on the one-holed torus's characters is in the literature (Previte
  and Xia; Cantat and Loray, among others), cited from memory and not checked at source. Completeness is not claimed
  here.

## The results (`verification/bound.py`, `bound_run.txt`; exact, 30 s)

- **For each finite subgroup G of SU(2)** (Q₈, 2T, 2O, 2I, built exactly), every pair (a, b) in G gives a reading
  (tr a, tr b, tr ab), and the moves' orbits group them.

| G | order | readings | orbits | κ carrying a bound state (orbit sizes) |
|---|---|---|---|---|
| Q₈ | 8 | 11 | 4 | −2 (1, the common point); 2 (1, 3, 6) |
| 2T | 24 | 43 | 7 | −2 (1); **0 (16)**; 2 (1, 3, 4, 6, 12) |
| 2O | 48 | 115 | 11 | −2 (1); **−1 (6)**; 0 (6, 16); **1 (36)**; 2 (1, 3, 4, 6, 12, 24) |
| 2I | 120 | 261 | 15 | −2 (1); **−φ (6)**; −1 (6); **−1/φ (40)**; 0 (16); **1/φ (6)**; 1 (72); **φ (40)**; 2 (1, 3, 4, 6, 12, 12, 36) |

- **B1 holds:** the common point is Q₈'s κ = −2 orbit, of size 1.
- **B2 holds:** 2I's orbits sit at κ ∈ ℚ(√5) \ ℚ (±φ and ±1/φ, with φ = (1 + √5)/2), and at 0, ±1 and ±2.

## What the whole does, read in its own terms

- **Its bound states sit at a discrete set of frustration levels:** κ = 2cos(2πk/n), n ∈ {1, 2, 3, 4, 5, 6, 10}. These are
  the levels at which the commutator of the two records has finite order. This is forced for a finite image, and the set
  of n is the set of element orders that finite rotations of the sphere allow.
- **Each finite group adds levels:**
  - the cusp's level (−2, the common point) and "nothing" (2) come from Q₈;
  - 2T adds 0, and 2O adds ±1;
  - **only the icosahedral bound states carry the golden levels,** ±φ and ±1/φ.

  So ℚ(√5), the golden field the record has treated as one thread's (m004's), enters the whole as the frustration level
  of its icosahedral bound states, with no thread chosen.
- **No level is read as physical. No Standard Model shape was asked for or read.**

## What is open

- **Completeness:** whether these are all the whole's finite orbits (the literature's classification, to be read at
  source), and the binary dihedral families.
- **The flow from the common point to these bound states.** How the unfolding connects the cusp's level to the other
  quantised levels, if it does. The moves conserve κ, so a connection needs whatever changes κ, which the grammar's
  moves do not.
