# CLAIM CARD — Card AGY-C45: Second-seat verification of agy-002 (P-135, FV2 F-U1/U4, OW27 v8, FL8-F1..F3) & physical (32514763f), with B1972/Sadov refutations & A2-FV2-N1/OW27-N2 notes (0 of 19)

- seat, branch, commit: agy, origin/agy/cusp-action-2026-11-20, e7d3d8279 (Producer C45, computed once) & fb3d3c7f3 (Cold-Room Countercheck C45)
- kind: negative
- touches: P-135, P-862, A01, A03, A08, S01, LAMBDA, PMNS, Higgs, coupling
- effect: refutes — A01, A03, LAMBDA, PMNS (independent second-seat refutation of agy-exp LINK8 F_6 [n_16 = -2], U_e^H U_T^* SU(2)_L Haar break [> 1/2], 0-bit K_6 [S swaps K_6^+ <-> K_6^-], & 10-sheet 3-cusp claim [regular D_5 cover has 5 cusps & b_1 = 5]; independent second-seat confirmation of agy-002 P-135, FV2 F-U1/U4, OW27 +16/9, & physical 32514763f, plus A2-FV2-N1 & A2-OW27-N2 notes)
- imports: Simpson (1990, p. 720) tame correspondence; E8 -> A5 + A2 + A1 root lattice & Bourbaki Cartan matrix; 6D Spin(10) Sadov/KMT anomaly cancellation; Fox/Reidemeister-Schreier covering homology; 1D/3D Yang-Mills cusp collar energy
- premises on main: B1650, B1832, B1836, B1955, B1972, P-135, P-862, docs/TOTAL_INPUTS_SCOREBOARD.md
- decisive script: relays/agy_2026-11-24_c45/c45_verify_peer_seats_p571_and_m13_claims.py, SHA-256 e65322f9f4bc7a8e, depends on standard library, sympy, and mpmath (100% python3 -I sandbox-runnable; zero external files/subprocess), run as python3 -I relays/agy_2026-11-24_c45/c45_verify_peer_seats_p571_and_m13_claims.py, output SHA-256 32cf522c262d75da
- second computation: agy disjoint cold-room countercheck relays/agy_2026-11-24_c45/c45_countercheck.py (SHA-256 e36f478ea744cfc9: GL4 Jordan holonomy, Bourbaki 8x8 Weyl-BFS, Cholesky SOS, rational Vandermonde Tr F^4, quintic C^2 bump); provides cross-seat second computation for agy-002 A2-P135 (096499514), FV2 U1/U4 (1560b2645), A2-PEER-AUDIT-V2 (4b8a123a8), & physical (32514763f)
- already on main?: topic-sweep /P-135|Simpson|Sadov|Hirzebruch|B1972|P-862|Cholesky|double-return/ on main (27a9353e5): closest B1650, B1955, and B1972 (second-seat pure-Python confirmation of P-135, P-862, physical 32514763f, and FL8-F1..F3)
- what would make it fail: 5/5 producer + 5/5 countercheck planted controls (c_0 = 1 breaks nilpotent Hitchin flatness & Jordan (M+I)^2 == 0; n_10 = n_16 + 3 breaks Spin(10) Tr F^4; U_e^H U_T^* breaks SU(2)_L Haar > 1/2; fixed cusp cut L = ell stays O(eps^4) vs complete-cusp O(eps^5))

## Key Second-Seat Verification & Audit Findings (`0 of 19`, `recomputed independently`)

1. **`agy-002` (`29f9d1699` & `foundations-v2 @ 1560b2645`) Confirmed + Two Constructive Notes:**
   - **Confirmed `THE SAME` (`zero shared code`):** `P-135` (`Simpson 1990 p. 720`, `B1650 O3` requires `b == 0`, nilpotent Jordan `M = -[[1, 2 pi i], [0, 1]]`, `112` p-odd `E_8` roots, complete SM singlet `su(2)_Q`, `6` unique hypercharges `(1 / 6, -5 / 6, 2 / 3)` over `C^3`, `k_Y = 14 / 3`), `FV2` `F-U1` (`8^3_4` unique `p = 5` irregular `D_p` cover, orbits `[1, 2, 2]`), `F-U4` (`P-862` `det(I_3 + M M^dagger) > 1` via Faddeev-LeVerrier & Cholesky), and `OW27 v8` `5`-flavor QED top beta `+16 / 9` (`119 / 119` new `verify` SHA-256 manifests intact).
   - **Notes `A2-FV2-N1` & `A2-OW27-N2`:** `foundations-v2` JSON outputs contain `numpy` binary64 floats and `F-U4` rests on imported Fock weights breaking `A08: H = I`; in `OW27 v8` (`y_t(M_{GUT}) = g_{UV}`), `m_c < Lambda_{QCD}^{(4)}` clamps `Lambda_{QCD}^{(3)} == Lambda_{QCD}^{(4)}`.
2. **`agy-exp` (`9b34bfc03`) & `physical` (`32514763f`):**
   - **Confirmed Refutations (`FL8-F1..F3` & `B1972`):** `6D` Sadov/KMT `SO(10)` gives `k = 4 - n_{16}` (`F_4` at `n_{16} = 0`, refuting `F_6` `n_{16} = -2`); `U_e^dagger U_T^*` breaks `SU(2)_L` Haar (`> 1 / 2`); `S` swaps `K_6^+ <-> K_6^-` (`>= 1` bit); pure-Python Fox/Schreier homology proves `5`-sheet `8^3_4` has `(3 cusps, b_1 = 3)` whereas `10`-sheet regular `ker(pi_1 -> D_5)` has `(5 cusps, b_1 = 5)`; `11` non-`relays/` manuscript edits noted.
   - **Confirmed `physical` (`32514763f`):** `W_2 + W_{-2}` offset-`2` ratio product `1`, `K_2` double-return `(z + 1)^2`, and complete-cusp `||F(A_eps)||^2 = o(eps^4)` (`cubic Hermite 6 / 5 & quintic C^2 10 / 7` vs fixed-cut `O(eps^4)`).

0 of 19.
