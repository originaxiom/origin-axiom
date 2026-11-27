# Verdict, practice card P1 — ACCEPT

*Banking seat V1, fam1-v1-unset-04, 2026-11-27. Expectation committed first (`relays/verdicts/E_P1.md`). Read: the card,
its decisive script and its control. Nothing else of the record.*

**ACCEPT.** Recomputed with this seat's own code, which shares nothing with the card's script. Every integer solution in
the box is found directly from the quadratic in z, and the orbits are found by union-find with an edge kept only when
both ends lie in the box. The box |entries| ≤ 3000 holds 281 solutions, 280 of them nonzero: 70 positive and 70 in each
of the three patterns with two negative entries. Under L, R and their inverses, moving within the box, they form exactly
two orbits: the 70 positive ones, containing (3, 3, 3), and one orbit of 210 that contains all three two-negative
patterns, 70 of each. The card's control fails as it must: with L and L⁻¹ alone the 280 fall into 96 orbits. As a scope
check, not decisive, the same two-orbit structure holds in the boxes 1000 (52 and 156) and 5000 (82 and 246), so the
claim does not depend on the cut at 3000. The claim's scope (one box, moving within it) is what was checked, and no
wider claim is made.

- own script: `relays/verdicts/v_p1_own.py`, SHA-256 2cd8eb55e71ed905, run as `python3 -B relays/verdicts/v_p1_own.py 3000`
- its output: `relays/verdicts/v_p1_own_out.txt`, SHA-256 858b5efb41f2211c
