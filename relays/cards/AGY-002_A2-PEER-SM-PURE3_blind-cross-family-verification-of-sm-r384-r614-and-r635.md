# SCOPE CARD — Card A2-PEER-SM-PURE3: Blind Cross-Family Independent Verification of `SM-R384` (`P-384`), `SM-R614` (`P-614`), and `SM-R635` (`P-635`) (seat code: `fam3-v1-high-03`, `0 of 19`)

- **card id:** A2-PEER-SM-PURE3 (pre-registration; blind cross-family `fam3-v1-high-03` second computation of three `fam1-v1-unset-04` `imports: none` `P-885` cards on `origin/sm/cards @ 1c5b13d0a` that carry `second computation: none`)
- **seat code:** `fam3-v1-high-03`
- **date:** 2026-11-27
- **touches:** `P-384`, `P-845`, `P-614`, `P-635`, `P-567`
- **imports:** `none`
- **premises on main (zero trial arcs):** `B299`, `B1303`, `B1656`, `B1723`, `B1753`, `B1836`, `B1934`, `B1943`, `P-384`, `P-567`, `P-614`, `P-635`, `P-845`
- **blindness & custody:** Strictly `0 of 19`. ZERO files of `origin/sm/cards` scripts or outputs opened prior to committing both this Scope Card, the independent verifier script, and its unread sealed outputs. Only the claim card statements and named `origin/main` premise `FINDINGS.md` were read.

## Pre-Registered Blind Expectations & Falsification Criteria

1. **Module V1 — Blind Verification of `SM-R384` (`CLAIM_2026-11-27_two_fifths_class_one_bit_refiled.md`, `kind: negative`, `P-384, P-845`):**
   - Enumerate all lines `v = (a, b) in (Q/Z)^2 / {+-1}` of exact order `1 <= N <= 12` from pure `Fraction` arithmetic (expected total: `266` lines; `36` of order `10`).
   - Verify exact `K = {(2/5, odd/10)}` has size `5`, forms a single `<T, -I>`-orbit (one cusp under `T(a, b) = (a, b - a)`), and its unit closure under `(Z/10Z)^x = {1, 3, 7, 9}` is `K union K'` of size `10` (`K' = {(1/5, odd/10)} = 3*K`), proving universally (not merely over a finite menu) that NO unit-invariant rule can select `K` alone.
   - Verify least multiple of `5` where `(L, e) = (-3, 6)` is not `(Q, d) = (1, 2)` transposed mod `N` is `N = 10` (checked through `N = 60`).
   - Verify `Pi` (`order == 10` and `3a == +-1/5 mod 1`) selects **exactly `K`** (`5` lines), while `Pi_inv` (`order == 10` and `3a in (1/5)Z/Z \ {0}`) selects **exactly `K union K'`** (`10` lines, two cusps, `1` Galois bit), and test a comprehensive family of `14` unit-invariant predicates on all `266` lines confirming `0/14` select `K`.
   - *Disagreement criterion:* any line count mismatch, `K` not a single cusp, `K` unit-closed, `least_level != 10`, `Pi != K`, or any unit-invariant rule selecting `K`.

2. **Module V2 — Blind Verification of `SM-R614` (`CLAIM_2026-11-27_discrete_remnant_27_refiled.md`, `kind: computation`, `P-614, P-414, P-157`):**
   - Independently construct the Bourbaki `6 x 6` `E_6` Cartan matrix, all `72` roots (`78`-dim adjoint), and all `27` weights of the fundamental representation `V(omega_1)` from pure integer/rational arithmetic (zero `B299` script imported).
   - Construct exact coroot directions `psi = 3 * fundamental_coweight(node 1)`, `chi`, `Y`, and `eta = (3*chi - 5*psi)/4`, confirming exact `eta` charges (`-2` on `Q, u^c, e^c`; `+1` on `d^c, L, H_d, Dbar`; `-5` on `nu^c, N`; `+4` on `H_u, D`) and exact `nu^c == N` equality under `eta`.
   - Compute exact Smith Normal Form of the discrete residual quotient `{x in V : w.x in Z} / ((V cap ker w) + (V cap Z^6))` inside `V_5 = V_SM + R*eta` (and also report the full rank-6 `E_6` Cartan torus `R^6` for completeness!) for vev sets `{nu^c}`, `{N}`, and `{nu^c, N}`.
   - Verify explicitly that `exp(2 pi i eta / 5)` lies inside `G_SM` (finding the exact `x_SM in V_SM` with `eta/5 - x_SM in Z^6`), prove zero matter-parity solutions in `V_5` (while checking full `R^6` separately), compute exact compact `E_6` (`78`-dim) Lie-algebra stabilizer dimensions & ranks for `nu^c`, `N`, and `(nu^c, N)` via explicit Chevalley raising/lowering matrices on the `27` (`dim 45, rank 5` = `Spin(10)` for single singlet; `dim 24, rank 4` = `SU(5)` for both), and run the exact `E5` mod-2 census (`h in F_2^6` with `h.nu^c == h.N == 0 mod 2`).
   - *Disagreement criterion:* nontrivial discrete residual in `V_5`, `exp(2 pi i eta / 5)` not in `G_SM`, matter parity existing in `V_5`, `eta(nu^c) != eta(N)`, or stabilizer `(dim, rank)` deviating from `Spin(10) (45, 5)` / `SU(5) (24, 4)`.

3. **Module V3 — Blind Verification of `SM-R635` (`CLAIM_2026-11-27_boundary_free_classes_refiled.md`, `kind: computation`, `P-635, P-567`):**
   - Independently build the flat `SU(2)` representation `rho(a) = Q_I = -i sigma_1`, `rho(b) = Q_J = -i sigma_2` (`rho(c) = rho(a b a^{-1} b^{-1}) = -I_2`) and `Ad rho` on `su(2) = R^3` in exact symbolic `SymPy` (zero `b1656_funcs` imported).
   - Compute exact Fox-calculus dimensions: `dim H^0 = 0`, `dim H^1(Z^2; ad rho) = 0`, `dim H^1(F_2; ad rho) = 3`, `dim H^1_par(F_2; ad rho) = 0`, boundary restriction rank `= 3` on `H^1(F_2; ad rho)`, and boundary restriction rank `= 0` on trivial `u(1)` lines (`dim H^1(Z^2; R) = dim H^1(F_2; R) = 2`).
   - Compute `kappa(s) = tr(A(s) B(s) A(s)^{-1} B(s)^{-1})` symbolically for `A(s) = Q_I exp(s_1 Q_I) exp(s_3 Q_K)`, `B(s) = Q_J exp(s_2 Q_J)`, verifying exact `kappa(0) = -2`, `grad kappa(0) = 0`, and exact `3 x 3` Hessian `H_kappa(0)` positive-definite (recording exact eigenvalues!).
   - Compute exact `3 x 3` `m004` monodromy action `phi^*` (`a -> ab, b -> bab`, unique `P in SO(3)` with `P Ad rho(phi x) P^{-1} = Ad rho(x)`) on `H^1(F_2; ad rho)`, its exact characteristic polynomial, and `dim ker(phi^* - I)` (`expected: 1`).
   - *Disagreement criterion:* any cohomology dimension mismatch, boundary restriction rank `< 3` (or `!= 0` on lines), `H_kappa(0)` not positive definite, or `dim ker(phi^* - I) != 1`.

4. **Controls & Hygiene:** `5/5` independent planted fault controls (`PF1..PF5`), `0` AST float literals, `0` JSON float literals, standalone exit-1 control with `0` stderr bytes, `0` refused imports under `T7b Part 1`.
