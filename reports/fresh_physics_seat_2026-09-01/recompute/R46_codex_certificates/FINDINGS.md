# R46 — codex certificates (origin/codex/seat-r001 @ 9c2c2c9a) rerun on this bench (Phase D, tier D-2)

The certificates behind the SM end of the chain live on codex's head and are cited on main. Reran here (Python 3.11,
sympy; no Sage) in an isolated worktree; outputs in `*_output.txt`.

| certificate | what it certifies (in its own terms) | result here |
|---|---|---|
| `r019_hypercharge/hypercharge_trinification_scope.py` | hostile reproduction of cloud memo 70: over the branch-local E6/27 stack (r006), all three colour A2 choices × weak roots × SM-shaped 15-state assignments give 36 solutions each, all SM-shaped, hypercharge ratios (Yl,Ye,Yu+Yd)/Yq = (−3, 6, −2) with cubic −18(Yu/Yq−2)(Yu/Yq+4); three-colour-frame covariance PASS; **the ratio theorem is universal once SM multiplet multiplicities are assumed ("independently of E6")**; SCOPE VERDICT: frame, physical 15-plet, gauging and normalisation are not selected | reproduces: all PASS lines; agrees with the seat's R03/R10 (−18(t−3)(t+3) in the other chart) and with B8143's three-branch finding |
| `r017_yukawa_primary/verify_yukawa_exact_spectrum_no_go.py` | exact one-H_u spectrum forces the unique Higgs into the ambient image; naturality forces the renormalisable up-type Yukawa rank to zero; OA-C1055: same-monad coefficient variation cannot repair Y_u without changing the spectrum | reproduces: RESULT/PASS lines as banked (B1167's "up-Yukawa vanishing μ_u = 0") |

(The remaining chain-critical codex certificates — r006 twisted_double, r023 generation obstruction, r017 cup-product
scope, r010 gl_class_m12, r024 lepton datum, r026 determinant frame, r013 rung transfer, r020 beat64, the vendored
check_charge_bracket — are running; rows are appended when their outputs land.)
