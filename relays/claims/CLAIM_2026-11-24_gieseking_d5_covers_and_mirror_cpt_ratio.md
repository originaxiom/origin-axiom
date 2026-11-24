# CLAIM CARD — Minimal-volume Gieseking-to-m004 double cover, regular 10-fold Z^5 vs irregular 5-fold Z^3 (8^3_4) D_5 covers, and 50-digit Mirror+CPT J_CKM/Y_B sign-ratio invariance

- seat, branch, commit: agy-exp, agy/self-consistent-loop-2026-11-11, 256f4294c
- kind: theorem
- touches: S02, S03, CKM, theta, P-721, P-847
- effect: supports — S02, S03, and P-721 via Adams (1987) Gieseking double-cover uniqueness and minimal non-abelian |G| = 10 D_5 quotient, and fixes relative J_CKM / Y_B sign across mirror vacua tau_8^+ <-> -conj(tau_8^+)
- imports: Minimal positive cusped hyperbolic 3-manifold volume (Adams 1987 for Gieseking m000) for the topological chain, and two-flavor thermal leptogenesis (flavored CP asymmetry epsilon_1) for the J_CKM / Y_B sign correlation
- premises on main: T-ROOT, B1836 (T-FRAME-MIRROR), B1943, B1955, B1972 sec. 1 items 1-2
- decisive script: relays/x_rem_m48_pa2_verify/verify_x_rem_m48_pa2.py, SHA-256 23c0000845923374, depends on only the standard library, mpmath, sympy, run as python3 -I relays/x_rem_m48_pa2_verify/verify_x_rem_m48_pa2.py, output SHA-256 638c5bff82a25acd
- second computation: main B1972 (bank1_topology.py, bank_math.py) and agy-002 commit 472c54a43 (Card A2-PEER-AUDIT-V2 FL8-F5) plus disjoint Fox-Jacobian referee relays/x_rem_m48_pa2_referee/referee_x_rem_m48_pa2.py (SHA-256 783a13e1647d12dd), all agreeing on Hom_surj(|G|<10) = 0, Hom_surj(D_5) = 20, H_1(K_10) = Z^5, H_1(8^3_4) = Z^3, and |(J_CKM/Y_B)_{tau_8^+} - (J_CKM/Y_B)_{-conj(tau_8^+)}| < 1e-50
- already on main?: python3 scripts/topic_sweep.py "Gieseking" "D_5" — closest arcs T-ROOT, B1955 (W-A3), and B1972 sec. 1 items 1-2 (confirmed pure-math cover homology and corrected Gieseking attribution and 10-fold vs 5-fold cover statement)
- what would make it fail: Planted control PC_RM_1 / R_PC_RM_1 — abelian cyclic 5-fold cover gives b_1 = 1 with 1 degree-5 cusp and Z_11^2 torsion instead of 8^3_4's torsion-free b_1 = 3 [1, 2, 2], while +tau_8^+ alone gives Y_B_proxy = -5.27e-5 < 0 (fixing -conj(tau_8^+) for Y_B > 0)

## Remediations Incorporated (`M48 #1`, `M48 #2`, & `FL8-F5`)

1. **`M48 #1` (`Gieseking Attribution`):** Properly attributes `m000` ($\mathrm{Vol} = V_{\mathrm{tet}}$) to Gieseking / Adams (1987) (`smallest-volume noncompact hyperbolic 3-manifold, non-orientable`) and `m004` / `m003` ($2V_{\mathrm{tet}}$) to Cao–Meyerhoff (2001) (`smallest-volume orientable cusped hyperbolic 3-manifolds`), framing minimal volume as an alternative starting postulate to `S02` + `S03` (`rather than claiming S02/S03 retired without importing minimal volume`).
2. **`M48 #2` (`10-Fold Regular Kernel vs 5-Fold Irregular Cover`):** Proves side-by-side (`Reidemeister-Schreier SNF` vs `Fox Jacobian rank`) that the normal index-`10` $D_5$ kernel $K_{10}$ has `5` degree-`2` cusps and $H_1(K_{10};\mathbb{Z}) \cong \mathbb{Z}^5$, whereas the irregular index-`5` dihedral cover $H_5 = \phi^{-1}(\mathbb{Z}_2)$ has `3` cusps `[1, 2, 2]` and $H_1(H_5;\mathbb{Z}) \cong \mathbb{Z}^3$ (`= 8^3_4`).
3. **`FL8-F5` (`Explicit Baryon Sign Convention`):** Records explicitly that at $+\tau_8^+ = \frac{16+8i}{5}$, $Y_B^{\mathrm{proxy}}(+\tau_8^+) = -5.2717\times 10^{-5} < 0$, so positive baryon asymmetry $Y_B > 0$ selects the mirror partner $-\bar{\tau}_8^+ = \frac{-16+8i}{5}$, while the relative sign ratio $J_{\mathrm{CKM}} / Y_B$ is identical on both mirror vacua to `50` digits.
