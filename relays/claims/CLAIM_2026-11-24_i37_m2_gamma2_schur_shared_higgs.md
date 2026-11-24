# CLAIM CARD — Independent second computation of AGY-C13: +P_5 = +1 filters B1253's 40 Spin(10) trilinears to the 16 SM Yukawas and S_3 Schur uniqueness on M_2(Gamma(2)) forces H_u and H_d to share S(tau)

- seat, branch, commit: agy-exp, agy/self-consistent-loop-2026-11-11, 256f4294c
- kind: theorem
- touches: I-37, A04, Higgs, Yukawa, P-847
- effect: supports — I-37 and shared Higgs profile S(tau) via zero-shared-code second computation of AGY-C13 (queued in B1972 sec. 3)
- imports: Horava-Witten E_8 -> E_6 x SU(3) -> Spin(10) embedding and 1 discrete Kawamura parity sign bit (+P_5 = +1 selecting the 4 electroweak doublets over the 6 color triplets)
- premises on main: B1253, B1691, B1742, B1970 (D2 two-doublets bridge), B1972 sec. 3
- decisive script: relays/x_rem_m48_pa2_verify/verify_x_rem_m48_pa2.py, SHA-256 23c0000845923374, depends on only the standard library, mpmath, sympy, run as python3 -I relays/x_rem_m48_pa2_verify/verify_x_rem_m48_pa2.py, output SHA-256 638c5bff82a25acd
- second computation: Independent of agy commit b06c8fc1e (relays/c13_e8_i37_bridge_verify/verify_c13_e8_i37_bridge.py, zero shared code), plus disjoint numerical modular referee relays/x_rem_m48_pa2_referee/referee_x_rem_m48_pa2.py (SHA-256 783a13e1647d12dd), all three agreeing: 40 -> 16 SM Yukawas (6 Q u^c + 6 Q d^c + 2 L e^c + 2 L nu^c) and dim Hom_{S_3}(2_std, M_2(Gamma(2))) = 1
- already on main?: python3 scripts/topic_sweep.py "I-37" "two_doublets" — closest arcs B1742, B1970 (two_doublets.py), and B1972 sec. 3 (queued AGY-C13 for a second computation)
- what would make it fail: Planted control PC_RM_2 / R_PC_RM_2 — flipping +P_5 = +1 to -P_5 = +1 retains 24 color-triplet proton-decay operators instead of the 16 SM Yukawas, and replacing weight-2 M_2(Gamma(2)) by weight-4 Sym^2(M_2) = 1_+ + 2_std breaks S_3 irreducibility

## Verification Details (`RM_2` & `R_RM_2`)

1. **Kawamura Parity Sign Remedied (`M48 #3`) & `B1253` `40 -> 16` Yukawa Filter:** On $\mathbf{10}_H = \mathbf{5}\oplus\overline{\mathbf{5}}$ with $P_5 = \mathrm{diag}(-1,-1,-1,+1,+1)$, $+P_5 = +1$ (`priced explicitly at 1 discrete bit`) retains the `4` electroweak doublet states ($6Y = \pm 3$) and filters the `40` $\mathrm{Spin}(10)$-invariant $\mathbf{10}_H\cdot\mathbf{16}\cdot\mathbf{16}$ trilinears down to the exact `16` Standard Model Yukawa channels (`6 Q u^c + 6 Q d^c + 2 L e^c + 2 L \nu^c`), eliminating all `24` color-triplet proton-decay operators (`whereas -P_5 = +1 keeps the 6 triplets and 24 triplet operators`).
2. **`S_3` Schur Uniqueness on $M_2(\Gamma(2))$ (`D-1` over `B1742`):** Both symbolic $q^{1/8}$-series character projection (`RM_2`) and `45`-digit numerical modular $(T, S)$ intertwiner rank (`R_RM_2`, max modular error `2.48e-46`) confirm $\dim_{\mathbb{C}}\mathrm{Hom}_{S_3}(\mathbf{2}_{\mathrm{std}}, M_2(\Gamma(2))) = 1$, forcing $H_u$ and $H_d$ in Frame C to share the unique modular Higgs profile $S(\tau)$ (`zero second Higgs-profile menu`).
3. **`E_8 -> SU(5)_GUT x SU(5)_perp` Branching Corrected (`FL8-F7`):** Exact `240`-root $\mathbb{Z}_5$-center decomposition (`248 = 48 + 50 + 50 + 50 + 50`) confirms that **both** $\mathbf{5}_H \in (\mathbf{5},\overline{\mathbf{10}}_\perp)$ and $\overline{\mathbf{5}}_H \in (\overline{\mathbf{5}},\mathbf{10}_\perp)$ carry $\dim_\perp = 10$ (`retracting Link 8's "(5, 5_perp)" prose`).
