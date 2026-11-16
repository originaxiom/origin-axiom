# `AGY-002_CLOSURE-G6` — Gate 6 Results (`0 of 19`)

## 1. Check Labels and Tracked Evidence (`docs/seats/README.md` § 12)

- **expectations committed first:**
  - Card commit `d4084f86b`: `relays/cards/AGY-002_CLOSURE-G6_covariant-majorana-seesaw-tm1-and-2loop-ir-surfaces.md`
  - First script seal `c41a7f346`: `relays/agy002_closure_g6/verify_closure_g6.py`, `relays/agy002_closure_g6/SCRIPT_SHA256.txt`
  - First output seal `e751f2f9d` (committed unread): `relays/agy002_closure_g6/verify_closure_g6_out.json`, `relays/agy002_closure_g6/OUTPUT_SHA256.txt`
  - Bergman rank-`1` reproducing-kernel erratum & fixed script seal `664cdc35f` (`preserving c41a7f346..e751f2f9d untouched under seal-immutable`): `relays/cards/AGY-002_CLOSURE-G6-ERRATUM_reproducing-kernel-rank1-vs-g6v0.md`, `relays/agy002_closure_g6_fixed/verify_closure_g6_fixed.py`, `relays/agy002_closure_g6_fixed/SCRIPT_SHA256.txt`
  - Fixed output seal `c79c57728` (committed unread): `relays/agy002_closure_g6_fixed/verify_closure_g6_fixed_out.json`, `relays/agy002_closure_g6_fixed/OUTPUT_SHA256.txt`
- **recomputed independently:**
  - Cold-room second script seal `cff52cd0a` (built from `hep-th/0404229`, `Weinberg 1979`, `Machacek-Vaughn 1983-1985`, `Bednyakov-Pikelner-Velizhanin 2014`, and the card + erratum alone without reading or importing `verify_closure_g6*.py`, while verifying all `4` producer `SHA-256` manifests): `relays/agy002_closure_g6_referee/referee_closure_g6.py`, `relays/agy002_closure_g6_referee/SCRIPT_SHA256.txt`
  - Cold-room second output seal `0973af996` (committed unread): `relays/agy002_closure_g6_referee/referee_closure_g6_out.json`, `relays/agy002_closure_g6_referee/OUTPUT_SHA256.txt`
- **tested against planted errors:**
  - `5 of 5` planted cases caught in `c79c57728` (`PF6.1` `SO(3)` rotation of `Frobenius`-orthonormalized all-ones sum `> 16/100 > 1/10`; `PF6.2` `TM2` column swap `|I_TM1 - 2/3| = 1/3 > 1/4`; `PF6.3` `N_g = 6` `alpha_3^{-1}(IR)` shift `> 17 > 15`; `PF6.4` `-24` vs `-48 lambda^2 Tr_Y` shift `> 2/1000 > 1/1000`; `PF6.5` asymmetric `Bloch-Wigner` `|D(z) + D(conj(z))| = 0 < (1/10)^15`);
  - `5 of 5` planted cases caught independently in `0973af996` (`PF6.1` `> 65/100 > 1/10`; `PF6.2` `1/3 > 1/4`; `PF6.3` `> 18 > 15`; `PF6.4` `> 19/10000 > 1/1000`; `PF6.5` `0 < (1/10)^15`).

## 2. Mask-Safe Rational Verification Summary (`0 of 19`)

| Check | First Computation (`c79c57728`) | Cold-Room Second Computation (`0973af996`) | Sealed Rational Bar |
|---|---|---|---|
| `AST` source lock & `SHA-256` custody | `0` float literals, `0` complex literals, `0` repo imports | `0` float literals, `0` complex literals, `4 / 4` producer manifests matched | Exact (`0`) |
| `(J_0, J_1, J_2)` symmetry, `T/S` covariance, & `Sym^2` span | Symmetry `< (1/10)^14`, `T/S` `< 2 * (1/10)^13`, ranks `[1, 3, 3]`, span `3`, `CP^2` shift `> 1/100 > 1/200` | `48 x 48` quadrature `< (1/10)^14`, Bergman `< 2 * (1/10)^15`, `T/S` `< 2 * (1/10)^13`, ranks `[1, 3, 3]`, span `3`, `CP^2` shift `> 3/100 > 1/200` | `< (1/10)^12` |
| `Type-I` seesaw `U(3)^6` `Haar` invariance (`v_1 = G_6 v_0`) | `10`-trial `Haar` `< 2 * (1/10)^14` (`vs rank-1 v_0 nullspace drift caught by Guardrail 3`) | `10`-trial `Haar` `< (1/10)^14` (`confirms rank-1 v_0 nullspace drift > 1`) | `< (1/10)^13` |
| Trimaximal `TM1` `UV` sum rule & `RGE` corridor (`dt = -30`) | `UV` `|I_TM1 - 2/3| < (1/10)^15` at `|U_{e3}|^2 = 1/48`; `IR` `< 1/2000` (`y_tau <= 1/20`), `< 4/1000 < 1/200` (`y_tau <= 1/5`) | `Antusch` integral `< 3 * (1/10)^14`; `UV` `< 4 * (1/10)^15`; `IR` `< 3/10000 < 1/2000` (`y_tau <= 1/20`), `< 4/1000 < 1/200` (`y_tau <= 1/5`) | `< 1/200` |
| `243`-history `3`-family `Pati-Salam x Z2^D` `Strong-CP` | `max |bar_theta_QCD(IR)| < 7 * (1/10)^14` with `|J_CKM| > 5/1000 > 1/1000` | `RK4` vs `DOP853` `< 5 * (1/10)^12`; `max |bar_theta_QCD(IR)| < 2 * (1/10)^15` with `|J_CKM| > 3/1000` | `< (1/10)^13` |
| `243`-history `delta_{2-loop}` & `D`-term `sqrt(2 lambda_IR)` | `delta_{2-loop}` strictly inside `[7/10000, 3/1000]`; `sqrt(2 lambda_IR)` strictly inside `[35/100, 78/100]`, `min lambda_IR > 1/20` | `delta_{2-loop}` strictly inside `[7/10000, 3/1000]`; `sqrt(2 lambda_IR)` strictly inside `[35/100, 78/100]`, `min lambda_IR > 1/20` | Exact rational envelopes |

## 3. Theorems Locked in Gate 6

1. **Cutoff-Free `SL(2, Z)`-Covariant `Majorana` Basis & Bergman Rank-`1` Theorem:** Contracting `Y_0(tau) = Y_cim(tau; 0, 0)` with `v_0(tau) = psi^{(6)}(0; tau, 0)`, `v_1 = G_6 v_0`, and cubic `J_1 J_1^dag J_1` yields `3` weight-`0`, `SL(2, Z)`-covariant symmetric `3 x 3` `Majorana` tensors `(J_0, J_1, J_2)` of ranks `(1, 3, 3)` spanning `3D` in `Sym^2(C^3)` without Eisenstein/Dedekind cutoffs. By the Bergman reproducing property, `Y_cim(tau; xi) . v_0(tau) = psi^{(3)}(0; z_L) psi^{(3)}(0; z_R)^T` has exact rank `1`, whereas `v_1 = G_6 v_0` lifts `Y_e, Y_nu` to full rank `3` (`Haar` `< (1/10)^14`). Relative phases in `(c_0 : c_1 : c_2) in CP^2` are physical (`4` real projective ratios + `1` scale `M_0 / v_EW` generally; `2 + 1` on `Re(tau) = 0`), and `SO(3)` rotations shift all-ones orthonormal sums (`PF6.1`), refuting `0`-parameter kinetic-isotropy claims.
2. **Universal `TM1` Survival Under `RGE` Running:** Whenever a `Z_2` residual symmetry aligns the `1`st `PMNS` column to `(2, -1, -1)^T / sqrt(6)` (`I_TM1 = cos^2 theta_12 cos^2 theta_13 = 2/3`), downward evolution over `dt = -30` shifts `I_TM1` by `< 1/2000` for `y_tau <= 1/20` (`and < 1/200` up to `y_tau = 1/5`).
3. **Repaired `3`-Family `Pati-Salam x Z2^D` `2`-Loop `IR` Envelopes:** Across all `243` `N_g = 3` perturbative histories, `|bar_theta_QCD(IR)| < (1/10)^13` (`without N_g = 6 doubling, PF6.3; and without tautological Bloch-Wigner D(z) + D(conj(z)) = 0 diagnostics, PF6.5`), `delta_{2-loop} in [7/10000, 3/1000]`, and `D`-term `sqrt(2 lambda_IR) = m_H / v_EW in [35/100, 78/100]` (`with exact -48 lambda^2 Tr_Y, PF6.4`). Gate 6 is locked. `0 of 19.`
