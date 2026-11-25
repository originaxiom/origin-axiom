# B1985 — Listening 3: up the tower the whole repeats the cube at every scale and unfolds out of the common point only along its tangent cone; at 3, the whole's prime, that cone is the cube's four body diagonals, on which the Markoff point (3, 3, 3) lies

**Verdict: PROVED (exact on the towers run; two readings post hoc, labelled, each checked exactly).** Main, 2026-11-25.
Unattended, on the listening line. Data-free. Register rows P-882 and P-694 (FK15). **0 of 19.**

## Seen first

- **B1984:** the one place the whole leaves structure is the common point. Mod p² its neighbourhood carries the cube's
  rotation group (B1687's Aut(Q₈) = S₄), and mod 9 the cusp's leaf is the cube.
- **B1601's lemma:** the moves' linear part at the origin is the cube group, and its body diagonals are isotropic for
  x² + y² + z² exactly in characteristic 3.
- **Swept:** `VERDICT topic-sweep /tangent cone|singular point|isotropic|Hensel|lift(s|ing)? (of|to) the|Markoff tree|\(3, ?3, ?3\)/: 28 of 1726 arcs on main match (NEGATIVE 4, OPEN 3, PROVED 21); 20 register rows match (DECLINED 1, DONE 15, QU`. The matches are B1601's lemma, B1796 (the cusp unit), B603 and P-163, in other senses. No arc
  follows the common point's neighbourhood up the tower or finds its tangent cone governing the lifts.
- **The literature (standard):** the cusp's leaf x² + y² + z² = xyz is singular at the origin, with tangent cone
  x² + y² + z² = 0; points over a singular point need not lift (Hensel's lemma fails there). (3, 3, 3) is the root of the
  integer Markoff tree.

## The results (`verification/listen3.py`, `listen3_run.txt`; exact, under 1 s)

- **The system.** The moves L, R on the cusp's leaf mod p^k, restricted to the points over the common point (all
  coordinates ≡ 0 mod p).
- **The towers:** p = 3 at k = 2 to 5; p = 5 and 7 at k = 2 and 3.

| level | points over the common point | orbits (size × count) |
|---|---|---|
| mod 9 | 27 | 12, 8, 6, 1 |
| mod 27 | 243 | 72 × 3, then 12, 8, 6, 1 |
| mod 81 | 2673 | 648 × 3, 24 × 26, 12 × 4, 8 × 4, 6 × 4, 1 |
| mod 243 | 24057 | 5832 × 3, 216 × 24, 72 × 9, 24 × 26, 12 × 4, 8 × 4, 6 × 4, 1 |
| mod 25 / 125 | 125 / 3125 | 24 × 3, 12 × 2, 8 × 2, 6 × 2, 1 / 120 × 25, and the same below |
| mod 49 / 343 | 343 / 16807 | 24 × 11, 12 × 3, 8 × 3, 6 × 3, 1 / 1176 × 14, and the same below |

- **C1 holds:** mod 9, 25 and 49 the run reproduces B1984.
- **C2 holds:** every orbit reduces into one orbit of the level below.
- **G1 holds:** the centre's lifts are again the cube's orbit types (1, 6, 8, 12) at every level. The cube nests at
  every scale.
- **G2 holds:** at p = 3 the big orbits grow ×9 per level (72, 648, 5832).
- **Most directions die.** From mod 9 to mod 27, the face and edge orbits (6 and 12) have no lifts on the leaf. Only
  the vertices (8) lift, into three orbits of 72. Higher up, the same.

## Post hoc, labelled (`cone_posthoc.py`, `cone_posthoc_run.txt`; written after the run was read; exact)

- **From mod p² to mod p³ the lifting directions are exactly the tangent cone.** At p = 3, 5 and 7, the directions u
  over the common point that lift to the leaf mod p³ are exactly the isotropic vectors of x² + y² + z² over 𝔽_p:
  9, 25 and 49 of them, equal as sets.
- **At p = 3 the nonzero isotropic directions are exactly the cube's 8 vertices,** its four body diagonals.
- **(3, 3, 3) is on the leaf over the integers** (9 + 9 + 9 = 27 = 3·3·3), and its direction over the common point
  mod 9 is (1, 1, 1), a vertex.

## What the whole does, read in its own terms

- **The common point is a singular point, and the whole is self-similar there.** At every scale its neighbourhood is
  the cube again, with the cube's rotations acting.
- **The whole unfolds out of the common point only along its tangent cone.** Every other direction is a dead end at
  the next level.
- **At 3, the whole's own prime, the cone is the cube's four body diagonals,** the axes of its third turns (B1601: odd
  threads act at the origin as third turns about a body diagonal).
- **Along them lies (3, 3, 3), the root of the integer Markoff tree.** One Vieta move away is (3, 3, 6) =
  (tr LR, tr RL, tr LR·RL), since LR·RL = [[3, 4], [2, 3]]: the grammar's own words are nodes of that tree.
- **So, read from behaviour,** the one structure the whole forces, the common point, does not stay a point:
  - it repeats itself at every scale as the cube;
  - it opens outward only along the body diagonals;
  - and that opening leads to the arithmetic of the threads.

  None of this was asked for.

## What is open

- **A proof for all k and p** of the cone law, and of the nesting.
- **The next listening step:** what the unweighted unfolding (all histories, the law's "everything that is allowed
  happens") does to functions on this self-similar structure. Its spectrum and what persists is the first place a
  field, FK15, could be read from behaviour. Then the loop (PF5).
