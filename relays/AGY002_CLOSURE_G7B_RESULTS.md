# `AGY-002_CLOSURE-G7B` — Gate 7B Precision & `E_8`-Role Reconciliation Results (`0 of 19`)

## 1. Check Labels and Tracked Evidence (`docs/seats/README.md` § 12)

- **expectations committed first:**
  - Card commit `fb6101b9b`: `relays/cards/AGY-002_CLOSURE-G7B_same-dim-scale-nullity-analytic-casimir-tm1-gap-and-e8-roles.md`
  - First script seal `5d5d02a4b`: `relays/agy002_closure_g7b/verify_closure_g7b.py`, `relays/agy002_closure_g7b/SCRIPT_SHA256.txt`
  - First output seal `2bbe30f45` (committed unread): `relays/agy002_closure_g7b/verify_closure_g7b_out.json`, `relays/agy002_closure_g7b/OUTPUT_SHA256.txt`
- **recomputed independently:**
  - Cold-room second script seals `997f7482e` (`relays/agy002_closure_g7b_referee/referee_closure_g7b.py`), `18049e565870b` (`relays/cards/AGY-002_CLOSURE-G7B-REFEREE-ERRATUM_svd-projector-and-numpy-bool-json.md`, `relays/agy002_closure_g7b_referee_fixed/referee_closure_g7b.py`), and `0ec496d07` (`relays/cards/AGY-002_CLOSURE-G7B-REFEREE-ERRATUM-2_rk4-compensated-summation.md`, `relays/agy002_closure_g7b_referee_v2/referee_closure_g7b.py`), plus unread output seal `584a8ce2c` (`relays/agy002_closure_g7b_referee_v2/referee_closure_g7b_out.json`, `relays/agy002_closure_g7b_referee_v2/OUTPUT_SHA256.txt`), built from the card and published literature alone without reading or importing `relays/agy002_closure_g7b/verify_closure_g7b.py`.
- **tested against planted errors:**
  - `5 of 5` planted cases caught in `2bbe30f45` (`PF7B.1` same-dimension scale `nullity = 19 > 18` at `rank = 1`; `PF7B.2` `1 / (z - z_p)` `Cauchy` contour residue within `(1/10)^30` of `1`; `PF7B.3` near-degenerate `m_2 / m_1 = 1 + (1/10)^5` at `y_tau = 1/20` drives `|I_TM1(IR) - 2/3| > 1/4 >> 1/50`; `PF7B.4` `Role A` vs `Role B` `SU(3)_c` singlets `0 != 9`; `PF7B.5` Rank-`0` promotion of premise-conditioned `PR-5` caught);
  - `5 of 5` planted cases caught independently in `584a8ce2c` (`PF7B.1` `19 > 18`; `PF7B.2` `< (1/10)^13` from `1`; `PF7B.3` `> 1/4 >> 1/50`; `PF7B.4` `0 != 9`; `PF7B.5` transitive premise-purity failure).

## 2. Mask-Safe Rational Verification Summary (`0 of 19`)

| Check | First Computation (`2bbe30f45`) | Cold-Room Second Computation (`584a8ce2c`) | Sealed Rational Bar |
|---|---|---|---|
| `AST` source lock & `SHA-256` custody | `0` float literals, `0` complex literals, `0` repo imports; `42 / 42` prior + self `SCRIPT_SHA256` matched | `0` float literals, `0` complex literals, `0` repo imports; `46 / 46` prior + self `SCRIPT_SHA256` (`48 / 48` total) matched | Exact (`0` mismatches) |
| Same-dim `Buckingham-Pi` `nullity` (`F13`) | `D_19` `rank = 1, nullity = 18`; `D_20` `rank = 1, nullity = 19` (`M_2 / v_EW in ker`) | `QQ` `nullspace()` `rank = 1, nullity = 18 -> 19` (`log-bridge row restores 18`) | Exact `(1, 18) -> (1, 19)` |
| Global analytic `Casimir` & `Cauchy` contours (`F16`) | Symbolic `K_2 -> K_3` `0`; Leibniz `> 0`; Bessel vs closed integral `< (1/10)^26`; `8`-pt `E[3]\{0}` `< (1/10)^17`; neg-jet `< (1/10)^30` | Symbolic `besselsimp` `0`; tail `< (1/10)^150`; series vs integral `< (1/10)^22`; `32` & `48`-pt `Cauchy` `< (1/10)^15`; `0` `if deg < 0` shortcuts | `< (1/10)^22` & `< (1/10)^15` |
| Scoped `TM1` mass-gap domain (`F17`) | Symbolic `-(3/2) p (m_1 + m_2)/(m_2 - m_1)`; `32` `NO+IO` states `< 1/1000` (`y_tau = 1/20`), `< 12/1000 < 1/50` (`y_tau = 1/5`); `Haar` `< 2 * (1/10)^14` | Symbolic real & complex `1/(m_2^2 - m_1^2)`; `Antusch` benchmark `< 1/1000`; `Kahan` `RK4` vs `expm` `< (1/10)^13`; `< 1/1000` & `< 12/1000 < 1/50`; `Haar` `< (1/10)^13` | `< 1/50` (`PF7B.3 > 1/5`) |
| `E_8` `240`-root `Role A` vs `Role B` & `DAG` premises (`F14, F15`) | `|E_8| = 240`, `|A_2| = 6`, `|E_6| = 72`, `162 = 6 x 27`; `Role A` `0` singlets vs `Role B` `9` singlets in `27`; `premise_honesty = true` | Cartan + `6`-step-operator check: `Role A` `0` singlets vs `Role B` `9 + 9 + 9 = 27`; transitive `DAG` premise check `true` | Exact `0 != 9` |

## 3. Theorems Locked in Gate 7B

1. **Same-Dimension Scale-Ratio Nullity Theorem (`Resolving F13`):** Two independent mass scales `(v_EW, M_2)` of mass dimension `+1` preserve `rank(D_dim) = 1` (`1` energy unit) while raising `nullity(D_dim) = N - rank(D_dim)` from `18` to `19`, forcing `M_2 / v_EW` into the dimensionless input ledger unless an independent scale-fixing equation adds a second linearly independent constraint row.
2. **Global Analytic `Casimir` Sign Proof & Genuine `Cauchy` Contour Analyticity (`Resolving F16` & `Guardrail 2`):** On the equal-gap twisted flat-collar Bessel tower (`C_UV = 189/2, C_IR = 28`, curved-`m004` continuum/counterterms retained open), exact Bessel differentiation + pairwise Leibniz positivity yields the strictly negative global identity `d V_A / d L_4 = -(7 pi^2)/(1440 L_4^5) - (19 m^3)/(2 pi^2 L_4^2) int_0^infty ln(1 + exp(-4 m L_4 cosh t)) cosh(3 t) dt < 0` for all `L_4 > 0, m > 0`; simultaneously, genuine `32`/`48`-point `Cauchy` contour quadrature (`with zero literal-0 branches`) confirms entire analyticity across `E[3] \ {0}` and negative-degree holomorphic jet vanishing to `< (1/10)^15`.
3. **Scoped `TM1` Mass-Gap Bound & `E_8` Embedding Non-Equivalence (`Resolving F14, F15, F17`):** `1`-loop `Antusch` rotation carries the exact `1 / (m_j^2 - m_1^2)` denominator, scoping `|I_TM1(IR) - 2/3| < 1/50` to non-degenerate spectra (`min_{j!=1} |m_j^2 - m_1^2| / (m_j^2 + m_1^2) >= 1/3`, `y_tau <= 1/5`); on the `240` `E_8` roots, `Role A` (`E_6^{cent} = C_{E_8}(SU(3)_c)`) has `0` `SU(3)_c` singlets in `27` whereas `Role B` (`SU(3)_c subset E_6^{GUT}`) has `9` singlets, proving they cannot be combined without an explicit colour-reassignment map. Gate 7B is locked. `0 of 19.`
