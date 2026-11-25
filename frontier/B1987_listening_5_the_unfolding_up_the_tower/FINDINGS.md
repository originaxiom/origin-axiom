# B1987 — Listening 5: up the tower the whole's unfolding keeps exactly two modes forever at every level, the constant and the alternation, which lives on every orbit that continues outward; no other clock appears; larger orbits forget more slowly

**Verdict: PROVED (eigenvalues of finite permutation sums, every orbit at the levels run).** Main, 2026-11-25.
Unattended, on the listening line. Data-free. Register rows P-882 and P-769. **0 of 19.**

## Seen first

- **B1986:** over the common point mod p², the unweighted unfolding W₊ = P_L + P_R keeps the constant and the sign
  undamped. The sign flips with every move and lives on the body diagonals. It damps the rest at ½ and 1/√2.
- **B1985:** above p² the orbits grow along the tangent cone.
- **Swept** with B1986's sweep (`undamped|alternat…|parity clock|sign character|even ticks|spectral gap|expander`). No
  arc computes the unfolding's spectrum on the tower.
- **The literature:** none needed. The computation is exact finite linear algebra.

## The results (`verification/listen5.py`, `listen5_run.txt`; 14 s)

The table lists, for each orbit over the common point on the cusp's leaf: the undamped modes of W₊ (their arguments in
turns), and the slowest decay per move (|eigenvalue|/2).

| level | orbits (size × count) | undamped modes | slowest decay |
|---|---|---|---|
| mod 27 | 1; 6; 8; 12; 72 × 3 | 0 everywhere; **0.5 on 8 and 72** | 1/√2 on 6, 8, 12 and 72 |
| mod 81 | 1; 6 × 4; 8 × 4; 12 × 4; 24 × 26; 648 × 3 | **0.5 on 8, 24 and 648** | 1/√2 on 6, 8, 12, 24; **0.958** on 648 |
| mod 125 | 1; 6 × 2; 8 × 2; 12 × 2; 24 × 3; 120 × 25 | **0.5 on 8, 24 and 120** | 1/√2; **0.839** on 120 |
| mod 343 | 1; 6 × 3; 8 × 3; 12 × 3; 24 × 11; 1176 × 14 | **0.5 on 8, 24 and 1176** | 1/√2; **0.928** on 1176 |

- **T1 holds:** over every orbit at every level run, the undamped modes of W₊ are at arguments 0 (the constant) and ½
  (the alternation), and nowhere else. No clock of another period appears.
- **T2 holds:** on the grown orbits the slowest decay is at least 1/√2: 0.707 (72), 0.958 (648), 0.839 (120) and 0.928
  (1176).
- **W±'s gap below its top** is 2 on every cube-level orbit, and small on the grown ones: 0.35, 0.041, 0.13 and 0.067.

## What the whole does, read in its own terms

- **Exactly two things are never forgotten, at every level:** the constant, and the alternation that flips with every
  move.
- **The alternation lives on every orbit that continues outward,** and only there:
  - the body diagonals, the free orbits, and the orbits that grow along the tangent cone;
  - never the centre, the faces or the edges, which are the dead ends of B1985.

  So the whole's one clock rides exactly on the structure that unfolds.
- **Everything else is forgotten.** The cube's own structures decay at 1/√2 per move at every level. The large outward
  orbits forget more slowly, 0.84 to 0.96 per move, and more slowly as they grow.
- **No rate is read as physical.** Whether the alternation is the record's tick (P-769) is still open, as a reading.
- **No Standard Model shape was asked for or read.**

## What is open

- **The loop (PF5):** the whole read back on itself, stated before computing, with nothing chosen. The persistent
  alternation and the slow outward modes are what any self-consistent state would have to carry.
