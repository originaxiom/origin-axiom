# R46 — codex certificates (origin/codex/seat-r001 @ 9c2c2c9a) rerun on this bench (Phase D, tier D-2)

The certificates behind the SM end of the chain live on codex's head and are cited on main. Reran here (Python 3.11,
sympy; no Sage) in an isolated worktree; outputs in `*_output.txt`.

| certificate | what it certifies (in its own terms) | result here |
|---|---|---|
| `r019_hypercharge/hypercharge_trinification_scope.py` | hostile reproduction of cloud memo 70: over the branch-local E6/27 stack (r006), all three colour A2 choices × weak roots × SM-shaped 15-state assignments give 36 solutions each, all SM-shaped, hypercharge ratios (Yl,Ye,Yu+Yd)/Yq = (−3, 6, −2) with cubic −18(Yu/Yq−2)(Yu/Yq+4); three-colour-frame covariance PASS; **the ratio theorem is universal once SM multiplet multiplicities are assumed ("independently of E6")**; SCOPE VERDICT: frame, physical 15-plet, gauging and normalisation are not selected | reproduces: all PASS lines; agrees with the seat's R03/R10 (−18(t−3)(t+3) in the other chart) and with B8143's three-branch finding |
| `r017_yukawa_primary/verify_yukawa_exact_spectrum_no_go.py` | exact one-H_u spectrum forces the unique Higgs into the ambient image; naturality forces the renormalisable up-type Yukawa rank to zero; OA-C1055: same-monad coefficient variation cannot repair Y_u without changing the spectrum | reproduces: RESULT/PASS lines as banked (B1167's "up-Yukawa vanishing μ_u = 0") |

| `r006_e6_invariants/twisted_double.py` (8 m 49 s) | the branch-local E6/27 stack every other codex certificate imports: e6 loaded (72 roots, dim 78), principal sl2 + dial slots embedded, 27 weights (crystal of ω₁), ρ27 respects all 3003 Chevalley brackets, principal strings [16,8,0], m004 relator acts as identity on the 27, h¹(M;27) = 3, longitude verified symbolically (off-diagonal 2√3 i), torus h⁰ = 3 / h¹ = 6, mirror rep = Galois twist at the cusp, Mayer–Vietoris tables for identity/mirror doubles, h¹(M;27̄) = 3, adjoint sweep closure dim 78 for every dial/t | every "expect" line met (h¹ = 3 matches the seat's R08/R11 and B1031) |
| `r006_e6_invariants/paper/verify/check_charge_bracket.py` (26 s) | \|2T\| = 24; t (deg 6) and W (deg 8) 2T-invariant; charge degrees 8, 14, 16, 22; x14, x22 nonzero; [x14, x22] = 0 exactly | PASS ("the one certificate the cascade consumes reproduces exactly") |
| `r013_rung_transfer.py` (1 m 26 s) | dim z(C) = 12 (6 roots restrict to zero); 30 distinct nonzero weights, multiplicity profile 12×1 + 18×3; 109 flats; the centraliser-dimension spectrum is exactly Paper II's eleven values [12,14,16,18,20,26,28,30,36,46,78], every one an ambient Levi dimension; dim z(S) = 14 attained at 3-dim S | PASS (every check reproduced exactly) |
| `r010_gl_class_m12.py` (0.02 s) | proper (SL(2,ℤ)) class counts m = 1..12: (1,1,1,1,1,2,1,1,2,2,1,**3**); full GL(2,ℤ) counts: (…,1,**2**); D = 148 representatives (−7,6,4), (−7,8,3), (−1,12,1); improper swap det −1 | runs clean; **agrees with the seat's corrected R42 and contradicts B8148's "3 under both"** |
| `r017_yukawa_primary/verify_yukawa_cup_product_308_scope.py` (0.03 s) | exact naturality factorisation gives μ_u = 0, rank 0 | PASS |
| `r023_b1196_generation_obstruction.py` (1 m 42 s) | B1196 generation obstruction | PASS |
| `r024_lepton_character_datum.py` (0.04 s) | lepton character datum (its own scope line: no Čech representative, cyclic/Serre map, nonzero entry, determinant or physical Yukawa) | PASS |
| `r026_yukawa_determinant_frame/determinant_frame.py` (1 s) | quotient-lift invariance of the Yukawa determinant frame | PASS |
| `r020_beat64/r020_beat64_principal.py` (43 s) | principal generator = sum of the six simple-root vectors; a wrong single-root generator differs; **R020 VERDICT: REFUTED — no restricted Σ or restricted tick endomorphism of V64** (the certificate's own negative result) | runs clean; its verdict is a negative, as banked |

**Summary.** All 11 codex certificates run on this bench and print their own PASS/verdict lines; none fails. Two carry
content for the seat: r010 corrects the m = 12 GL(2,ℤ) count (see R42), and r019's universal-ratio theorem states in
its own words that the hypercharge ratios follow from the SM multiplet multiplicities "independently of E6" — the same
scoping the seat gave in R03/R10.
