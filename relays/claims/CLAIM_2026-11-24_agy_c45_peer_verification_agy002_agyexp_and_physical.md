# CLAIM CARD — Card AGY-C46: Second-seat verification of agy-002 (W70/P-135, FV2 F-U1/U4, OW27 v8) & physical (32514763f), with B1972/Sadov refutations & A2-FV2-N1/OW27-N2 notes (0 of 19)

- seat, branch, commit: agy, origin/agy/cusp-action-2026-11-20, eb8ab7160
- kind: negative
- touches: P-135, P-862, A01, A03, A08, S01, LAMBDA, PMNS, Higgs, coupling
- effect: refutes — A01, A03, LAMBDA, PMNS (independent second-seat refutation of agy-exp LINK8 F_6 [n_16 = -2], U_e^H U_T^* SU(2)_L Haar break [> 1/2], 0-bit K_6 [S swaps K_6^+ <-> K_6^-], & 10-sheet 3-cusp claim [regular D_5 cover has 5 cusps & b_1 = 5]; non-circular confirmation of agy-002 W70/P-135 su(2)_Q & k_Y=14/3, FV2 F-U1/U4, OW27 +16/9, & physical 32514763f)
- imports: Simpson (1990, JAMS 3, p. 720) tame harmonic-bundle correspondence, Sadov 6D N=(1,0) Spin(10) Green-Schwarz anomaly coefficient on F_k, and W70's five SM charge conditions on E_8 -> A_5 + A_2 + A_1 (with zero k_Y input)
- premises on main: B1650, B1971, B1972, P-135, P-862, W70, A01, A03, A08, S01, LAMBDA
- decisive script: relays/agy_2026-11-24_c46/c46_remediate_c45_p135_b1970_and_m13_sandbox.py, SHA-256 46be6dd192295060, depends on only the standard library, mpmath, and sympy, run as `python3 -I relays/agy_2026-11-24_c46/c46_remediate_c45_p135_b1970_and_m13_sandbox.py`, output SHA-256 0ea1e0f46e5ec87e (c46_out.json, sections E1 & E2)
- second computation: agy disjoint cold-room countercheck relays/agy_2026-11-24_c46/c46_countercheck.py (@ ff1526ee8, SHA-256 f2280cba98e4dd29, standard library and mpmath ONLY: implicit GL4 Jordan holonomy, coordinate-free Bourbaki 8x8 Cartan Weyl-BFS deriving su(2)_Q, 6 hypercharges, & k_Y=14/3, Cholesky P-862, 5-vector Tr F^4, & quintic C^2 bump); cross-checks agy-002 (29f9d1699) and physical (32514763f)
- already on main?: topic-sweep /P-135|Simpson|Sadov|Hirzebruch|B1972|P-862|Cholesky|double-return/ on main (27a9353e5): B1971/B1972 checked agy-exp BANK-1..10 on main; agy-002's 6 new Claim Cards (27f5d89fa..29f9d1699) and physical's 32514763f ("hand proof for independent review") lacked a second-seat machine check
- what would make it fail: dropping e^c(1) in (35,1,1) admits spurious (1/6, -1/3, 1/6) (> 6 solutions in Control 1); dropping one su(2) block from h_Q breaks <r, h_Q - h_W> in 2 Z; c_0 = 1 breaks Hitchin flatness; fixed-cut cusp bump stays O(eps^4) vs complete-cusp (6/(5 ell)) eps^5 (PF3)

## Claim (summary)

Zero-shared-code second-seat verification across `agy-002/verify @ 29f9d1699` (`119 / 119` SHA-256s & `0` AST/JSON floats) + `foundations-v2 @ 1560b2645`, `agy-exp @ 9b34bfc03` (`26 / 26` `relays/` SHA-256s), and `physical @ 32514763f`: refutes `LINK8` `F_6` (`k = 4 - n_{16} => n_{16} = -2`), `U_e^dagger U_T^*` (`SU(2)_L` Haar break `> 1 / 2`), `0`-bit `K_6` (`S` swaps `K_6^+ <-> K_6^-`), and `10`-sheet `3`-cusp `D_5` (`regular ker has 5 cusps & b_1 = 5` vs `5`-sheet `8^3_4` `[1, 2, 2], b_1 = 3`).

Non-circularly confirms `A2-P135` (`Simpson b == 0` for `O3`, nilpotent Jordan `M = -[[1, 2 pi i], [0, 1]]`, diagonal `su(2)_Q` with `<r, h_Q - h_W> in 2 Z` & `<Y, r> == 0`, exact `6` `C^3` hypercharges `(1 / 6, -5 / 6, 2 / 3)` solved from `W70`'s `5` SM conditions **with zero `k_Y` input**, and derived `k_Y = 140 / 30 == 14 / 3`), `F-U4` (`P-862`), `OW27` (`+16 / 9`), and `physical` `(z + 1)^2` / `O(eps^5)`; records `A2-FV2-N1` (`numpy` floats / `H != I`), `A2-OW27-N2` (`m_c < Lambda_{QCD}^{(4)}` clamp), `AGY-C38-N1`, & `11` non-`relays/` `agy-exp` edits.

0 of 19.
