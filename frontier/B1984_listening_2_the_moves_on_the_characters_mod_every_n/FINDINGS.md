# B1984 — Listening 2: mod every N ≤ 64 the moves acting together leave structure in one place, the common point, where they act as the cube's rotation group at every prime; mod 9 the cusp's leaf is the cube

**Verdict: PROVED (exact for every N from 2 to 64; three readings post hoc, labelled, each checked exactly).** Main,
2026-11-25. The goal resumed unattended at the author's word, on the listening line. Data-free. Register rows P-882,
P-845 and FK15's row (P-694). **0 of 19.**

## Seen first

- **B1983 (listening 1):** over every prime p ≤ 47, the moves fix only the common point and the trivial character, and
  connect the cusp's leaf from 5 on. At 3 the leaf is the common point alone.
- **B1601's lemma:** the moves' linear parts at the origin, dL and dR, are quarter turns about two axes, and generate
  the cube's rotation group S₄.
- **B1600 (W1 to W4):** the three lines, the common point, and the triplet as one irreducible triplet of A₄.
- **GENESIS FK15:** the field's genesis, open: "forced to exist, not forced which".
- **Swept:** `VERDICT topic-sweep /cube|rotation group of the cube|S_?4|common point.{0,40}neighbourhood|mod 9|p\^2|prime power/: 58 of 1725 arcs on main match (NEGATIVE 10, OPEN 1, PROVED 46, RETRACTED 1); 16 register rows match (DONE 10, QUEU`.
  - **The decisive match is B1687.** The moves induce automorphisms of the common point Q₈, and L and R generate all of
    Aut(Q₈) = S₄ of order 24, the one-qubit Clifford group modulo phases. The group found here is that one.
  - Also B1680 (the common point in higher rank) and B1746 (the cube group's forms as the Higgs, NEGATIVE for its question).
  - No arc computes the moves' orbits on the characters modulo prime powers or composites, or finds the common point the
    only place the whole leaves structure.
- **The literature:** the moves' orbits on the Markov surface modulo prime powers are treated in the strong-approximation
  literature after Bourgain, Gamburd and Sarnak. Cited from memory and not checked at source; nothing here rests on it.

## The results (`verification/listen2.py`, `listen2_run.txt`, `listen2_run.json`; exact, 18 s)

| cell | outcome |
|---|---|
| C1 (the primes reproduce B1983) | holds: connected for 5 ≤ p ≤ 47; at 3 the leaf is the common point alone |
| F1 (every N coprime to 6 connected) | **fails as worded**: 16 of 20. N = 25, 35, 49 and 55 are not |
| F2 (some N divisible by 2 or 3 splits) | holds: every even N ≥ 4 except 6, and 3 and every multiple of 9 |

## Post hoc, labelled (`common_point_posthoc.py`, `common_point_posthoc_run.txt`; written after the run was read; exact)

1. **The composites carry nothing new.** At N = 10, 12, 15, 18, 35 and 55, every orbit on the cusp's leaf is the CRT
   product of orbits modulo the prime-power factors. F1's failures at 35 and 55 are this: each prime's big orbit
   combined with the other prime's common point.
2. **Over the common point the moves act as the cube's rotation group, at every prime tested.**
   - At N = 9, 25 and 49, the points of the cusp's leaf congruent to the common point mod p number p³.
   - Their orbits are one to one with those of the linear group ⟨dL, dR⟩ on 𝔽_p³, which has order 24.
   - The orbit sizes are 12, 8, 6, 1 at p = 3; 24³, 12², 8², 6², 1 at p = 5; and 24¹¹, 12³, 8³, 6³, 1 at p = 7.
   - F1's failures at 25 and 49 are this structure. The big orbit lifts as one piece.
3. **Mod 9 the cusp's leaf is the cube.** At 3 the whole leaf is the common point, so mod 9 it is the common point's
   neighbourhood alone: 27 points in four orbits, the centre (1), the faces ±eᵢ (6), the vertices (±1, ±1, ±1) (8),
   and the edges (12).

- **The 2-adic tower** (N = 4, 8, 16, 32, 64) splits further. At 2 the common point and the trivial character coincide,
  and mod 2^k the moves fix (0, 0, 0), (2, 2, 2), (2^(k−1), …) and (2^(k−1) + 2, …). It is described here and not
  read further.

## What the whole does, read in its own terms

- **It leaves structure in one place.**
  - At every prime it connects the cusp's leaf, and composite moduli are only products.
  - What it does not connect is the neighbourhood of the common point. There it acts at every prime as one finite
    group, the cube's rotation group S₄, on a three-dimensional space: three axes, four body diagonals, six edge axes.
  - At 3, the whole's own level, the cusp's leaf modulo the next power is that cube and nothing else.
- **A three, from behaviour.** Nothing asked for three. The common point's neighbourhood carries three axes, permuted
  by the cube's rotations, at every level. On record this group is the weave's (W4; B1601; B1687's Aut(Q₈) = S₄, the one-qubit Clifford
  group modulo phases), and GENESIS reads the generations as the triplet (FK14, a reading). This arc adds that the whole
  leaves its structure nowhere else, at every modulus to 64.
- **A candidate for FK15, as a reading.** "Forced to exist": the only structure the whole forces is the common point and
  the three-dimensional space around it, acted on by the cube's rotations, at every level. Whether a field is this,
  that is, sections over the weave carrying this representation, is the next question. It is not established here.
- **No Standard Model shape was asked for or read.**

## What is open

- **The 2-adic tower,** where the common point and "nothing" meet.
- **The next listening step:** with nothing chosen, what the whole does to functions on the common point's neighbourhood
  (the S₄ space) as all histories unfold. Then the loop (PF5).
