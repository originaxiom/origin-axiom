# B1993 — Listening 9: the cusp's integer readings all lie over the common point mod 3 and are one torus shape, the modular (hexagonal) torus, τ = ω, in four lifts that the moves split 1 + 3

**Verdict: PROVED (exact within |entries| ≤ 3000; the shape's identification cited as standard; one expectation failed as
worded, read post hoc).** Main, 2026-11-25, in the author's /loop "continue the listening line". Data-free. Register rows
P-882, P-845 and the retired τ = ω (GENESIS v1.35). **0 of 19.**

## Seen first

- **B1992:** what the whole selects is algebraic. The cusp's Fuchsian component (the shapes τ) carries the analytic map,
  and the two parts of the cusp meet mod 3.
- **B1601, B1983, B1985:** mod 3 the cusp's leaf collapses onto the common point, and the whole opens along the body
  diagonals towards (3, 3, 3).
- **GENESIS v1.35:** τ = ω, the author's tagged working postulate of 2026-10-08, was retired as tested. B1617 and B1618
  found no hierarchy at ω, a test shaped by the Standard Model.
- **B1691:** i and ω have no 2–3 hierarchy in B1656's frame.
- **B482:** the det −1 Markov spectrum below 3.
- **B553:** the odd-Fibonacci Markoff cluster.
- **Swept:** `VERDICT topic-sweep /Markoff|modular torus|hexagonal|tau = omega|τ = ω|commutator subgroup|spin structure/: 46 of 1734 arcs on main match (NEGATIVE 6, OPEN 1, PROVED 39); 27 register rows match (DECLINED 2, DONE 14, QUEU`. The record knows Markoff triples, the Markov spectrum and ω. None reads the cusp's integer readings as
  the whole's own arithmetic selection of one shape.
- **The literature (standard, cited):**
  - the integer solutions of x² + y² + z² = xyz are 0 and three times the Markoff triples (Markoff, Cassels);
  - the Markoff triples form one tree under Vieta moves;
  - the punctured torus with readings (3, 3, 3) is the modular torus H/[SL(2, ℤ), SL(2, ℤ)], the hexagonal one,
    τ = ω up to SL(2, ℤ).

## The results (`verification/integers.py`, `integers_run.txt`; exact)

| cell | outcome |
|---|---|
| M1: every integer solution with entries up to 3000 has all entries ≡ 0 mod 3 | **holds**: 281 solutions, the origin among them |
| M2: the positive ones form one orbit of L, R, L⁻¹, R⁻¹ | **holds**: all 70 with max ≤ 3000 are reached from (3, 3, 3) |
| M3: four sign patterns, kept apart by L and R alone | **fails as worded**: four patterns of 70 each, but the moves carry readings between them |
| M4 (cited): (3, 3, 3) is the one positive solution fixed by the cyclic exchange of the readings | **holds** |

## Post hoc, labelled (`signs_posthoc.py`, `signs_posthoc_run.txt`; written after the run was read)

- **The 280 nonzero readings form exactly two orbits of L, R and their inverses** within the box:
  - the positive ones (70), the Markoff tree from (3, 3, 3);
  - one orbit of 210 that mixes the three patterns with two negative readings.

  So the moves fix one sign pattern and permute the other three.
- **The sign patterns are the four lifts of one representation from PSL(2) to SL(2),** the record's spin structures (a reading, cited, not computed here; Review 87). The
  central sign actions (GM5b's candidate) would join the two orbits.

## What the whole does, read in its own terms

- **All of the cusp's integer readings lie over the common point mod 3,** in its 3-adic neighbourhood, where the whole
  opens along the body diagonals (B1985).
- **They are one torus shape:** the Markoff tree is one orbit, the modular torus, the hexagonal punctured torus, τ = ω.
  The shape comes in four lifts, split by the moves 1 + 3: the three once more.
- **So, given the records' integrality (GENESIS GM1, postulated), the whole's own arithmetic selects one point of the
  shapes' space,** with no thread and no frame chosen. That point is ω, which the record retired after a Standard Model
  test. In listening mode no such test is applied, and none is applied here.
- **No Standard Model shape was asked for or read.**

## What is open

- **What the whole does at ω in its own terms:** the unfolding, the persistent modes and the levels there, before any
  frame is laid on it.
- **A proof of M1 to M3 beyond the box.** The literature covers the positive tree; the mixed orbit's single-ness is to
  be proved.
