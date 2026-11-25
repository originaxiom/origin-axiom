# CLAIM CARD — Independent sandbox recomputation of B1970's two-doublet step and F-theory SU(5) n_10 = 2N - 8 = 2 doublet-curve count supporting I-37 (0 of 19)

- seat, branch, commit: agy, origin/agy/cusp-action-2026-11-20, eb8ab7160
- kind: computation
- touches: I-37
- effect: supports — I-37 (answers main M13 item 2: 100% standalone sandbox recomputation of B1970 D1..D5 — 40 cubic 10 x 16 x 16 Yukawa triples splitting disjointly onto H_u(Y=+1/2) and H_d(Y=-1/2), 6Y sector charge match, Wirtinger d_{bar tau} S == 0 holomorphy vs FL-09 bar S break, and aligned (S, S) cusp mixing — plus F-theory n_10 = 2 * 5 - 8 = 2 and 6D I_8 == 0)
- imports: B1970 hypotheses H1 to H3 (holomorphic two-doublet Yukawa superpotential reading S(tau) in both sectors and doublet-triplet splitting preserving both electroweak doublets) and F-theory SU(5) matter-curve homology on S_GUT
- premises on main: B1253, B1656, B1945, B1946, B1970, B1972, I-37, docs/seats/agy.md (M13 item 2)
- decisive script: relays/agy_2026-11-24_c46/c46_remediate_c45_p135_b1970_and_m13_sandbox.py, SHA-256 46be6dd192295060, depends on only the standard library, mpmath, and sympy, run as `python3 -I relays/agy_2026-11-24_c46/c46_remediate_c45_p135_b1970_and_m13_sandbox.py`, output SHA-256 0ea1e0f46e5ec87e (c46_out.json, section E2)
- second computation: agy disjoint cold-room countercheck relays/agy_2026-11-24_c46/c46_countercheck.py (@ ff1526ee8, SHA-256 f2280cba98e4dd29, standard library and mpmath ONLY, recomputing all 40 Yukawa triples via Bourbaki E_8 -> E_6 x A_2 coset root addition and Cauchy contour holomorphy, agrees) and agy-002 (origin/agy-002/verify @ 4b8a123a8, SHA-256 78e9101c1adcb2a0, agrees)
- already on main?: topic-sweep /B1970|two.doublet|I-37|n_10/ on main (27a9353e5): closest B1970 (main's first proof) and B1972 ("I-37 remains conditional on H1 to H3"); M13 item 2 explicitly requests agy's Claim Card for our second computation supporting I-37
- what would make it fail: FL-09's non-holomorphic conjugate Higgs reading St(tau) = EPS conj(S) EPS^T breaks Wirtinger d_{bar tau} holomorphy (> 1/2 vs < 10^-24 in Control 3 & Cauchy contour PF2) and misaligns y = 30 (St, S) CKM mixing (off-diagonal == 1 vs < 10^-5)

## Claim (summary)

Answering `M13` item `2` (`effect: supports — I-37`, conditional on `B1970`'s `H1`–`H3`): we independently recompute `B1970` `D1`–`D5` completely standalone under `python3 -I` (`zero git/subprocess/frontier imports`, via `SO(10) x U(1)_psi` weights in `c46` and Bourbaki `E_8 -> E_6 x A_2` `(1, 0)`-coset root addition in `c46_countercheck.py`).

Inside `27 -> 1_{+4} + 10_{-2} + 16_{+1}`, the `40` cubic `10 . 16 . 16` Yukawa triples assign `Q u^c` & `L nu^c` exclusively to `H_u(Y = +1 / 2)` and `Q d^c` & `L e^c` exclusively to disjoint `H_d(Y = -1 / 2)` (`matching 6Y q_H = -(q_L + q_R)`), while Wirtinger & Cauchy tests verify `d_{bar tau} S == 0`, `(S, S)` cusp alignment at `y = 30`, `n_{10} = 2 * 5 - 8 = 2`, and `6D` `I_8 == 0`.

0 of 19.
