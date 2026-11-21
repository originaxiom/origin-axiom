# Pre-Registration Card: `AGY-002_A2-OW9` — `T^2 / Z_2` KK-Tower Cosmological Constant, Positive de Sitter `X_0(5)` Casimir Stabilization of `tau_*`, and Open-Weave Dark-Matter Stabilizer Census (`0 of 19`)

- **Seat:** `AGY-002` (`agy-002/verify`)
- **Card ID:** `A2-OW9`
- **Empirical Firewall:** Strict `0 of 19` (purely mathematical/topological/algebraic QFT audit; zero empirical PDG inputs).
- **Prerequisite Custody:** Builds on `A2-OW2` (`b400fc161` / `a31eb8051`), `A2-OW3` (`2294c03c3` / `2fcde558a`), `A2-OW4` (`08315469d` / `1192ed854`), `A2-OW5` (`b47f02450` / `efeabdbc7`), and directly closes the open non-abelian / KK-parity stabilizer fence in `docs/COSMOLOGY_LEDGER.md` Row 4.

## 1. Scientific Objective & Hypotheses Committed Before Run

This card settles Hard Wall 2 (whether the massive `T^2 / Z_2` Kaluza-Klein tower softens `A2-OW4`'s `a_0 = -64` cosmological constant wall, what sign and minimum its finite `4D` Casimir energy has on `X_0(5)`, and whether any strictly stable dark-matter candidate exists on the open weave without ad-hoc symmetries):

1. **Exact `T^2 / Z_2` KK-Tower Supertrace No-Go Theorem (`OW9-A1`):**
   - Count every exact real bosonic and fermionic degree of freedom of the `N = 5` `2H` open-weave spectrum on `M_4 x (T^2 / Z_2)` (`48` `6D` chiral Weyl fermions `= 3 x 16_+`, `12` `6D` `G_SM` gauge bosons with `A_mu` even and `A_5, A_6` odd under `hat_iota`, and `2H = 8` real Higgs scalars in both bulk-`2H` and brane-`2H` localizations).
   - **Pass bar `OW9-A1`:**
     - Zero mode `(0, 0)`: `n_B(0) = 24 + 8 = 32`, `n_F(0) = 96`, `n_B(0) - n_F(0) = -64 != 0` (`4D` quartic `Lambda^4` wall persists).
     - Every unordered nonzero KK pair `{(m, n), (-m, -n)}` (`(m, n) != (0, 0)`): `48` massive `4D` Dirac fermions (`192` real `F` per pair = `96` per `T^2` lattice point); `12` massive `4D` Proca vectors (`36` real `B`, eating `12` odd Goldstones) plus `12` physical odd real scalars (`12` real `B`) = `48` real `B` per pair (`24` per `T^2` lattice point, zero massless `4D` adjoint scalars); plus `+8` real `B` per pair (`+4` per `T^2` lattice point) for bulk `2H` or `0` for brane `2H`.
     - Exact supertrace per `T^2` lattice point at every massive KK shell: `n_B - n_F = 28 - 96 = -68` (bulk `2H`, `-136` per unordered pair) and `24 - 96 = -72` (brane `2H`, `-144` per unordered pair) — strictly nonzero at every level, certifying an exact **KK-Tower `a_0` No-Go Theorem** (no misaligned or KK-tower Bose-Fermi cancellation softens `a_0`).

2. **Positive de Sitter `4D` Casimir Energy & Guardrail-1 Dynamical Stabilization of `tau_*^{+-} = (+-2 + i) / 5` on `X_0(5)` (`OW9-A2`):**
   - From Poisson resummation of the `6D -> 4D` proper-time heat kernel on unit-area `T^2`, the finite `4D` Casimir vacuum energy density per real bulk bosonic d.o.f. is `rho_1B(tau) = -(1 / pi^3) * E_3(tau) < 0` (AdS) and per real bulk fermionic d.o.f. (opposite Berezin sign) is `rho_1F(tau) = +(1 / pi^3) * E_3(tau) > 0` (dS), where `E_3(tau) = y^3 * sum'_{(m, n) != (0, 0)} |m + n tau|^(-6)`.
   - Thus the total finite `4D` Casimir density on `M_4 x (T^2 / Z_2)` has the **strictly positive de Sitter sign**: `rho_Casimir(tau) = +(68 / pi^3) * E_3(tau) > 0` (bulk `2H`) and `+(72 / pi^3) * E_3(tau) > 0` (brane `2H`).
   - Define the level-`5` Atkin-Lehner symmetric Casimir sum `F_3(tau) = E_3(tau) + E_3(5 tau)` on `X_0(5) = H / Gamma_0(5)` — a first-principles action containing **zero** reference to `tau_*` (Guardrail 1 compliant).
   - **Pass bar `OW9-A2`:**
     - `45`-dps `SL_2(Z)`-reduced Chowla-Selberg evaluation matches direct lattice sum (`R = 25`) at `tau in {i, rho, (2+i)/5, 2+i, i/sqrt(5), i*sqrt(5)}` to `< 1 / 10^4`, and proves `E_3((2+i)/5) = E_3(2+i) = E_3(i)` to `< 1 / 10^35` (`46589136156 / 10^10` to `< 1 / 10^9`) and `E_3(rho) < E_3(i)` (`41412565472 / 10^10` to `< 1 / 10^9`).
     - On `SL_2(Z)` alone, `tau = i` is a **saddle point** of `E_3(tau)` (`Hessian eigs`: `a < -7`, `b > +35`, `a * b < 0`).
     - On `X_0(5)`, at BOTH spontaneously CP-breaking order-`2` elliptic points `tau_*^{+-} = (+-2 + i) / 5` (`A2-OW2`), `|grad F_3(tau_*^{+-})| < 1 / 10^11`, AND the conformal map `gamma(tau) = +-2 - 1 / tau` (`gamma'(tau_*^+) = 3 - 4 i`) rotates the saddle Hessian of `E_3(tau)` relative to `E_3(5 tau)` by the exact `(3, 4, 5)` Pythagorean right-triangle angle (`sin^2(theta) = 16 / 25`), interlocking the two saddles into a **strictly positive-definite minimum** with eigenvalues `e_1 > 60`, `e_2 > 1300` matching the exact analytic `(3, 4, 5)` formula `Tr = 50 (a + b)`, `Det = 625 (4 a b + (16 / 25) (b - a)^2)` to `< 1 / 10^7` relative error.
     - Global `6`-coset scan across `H / Gamma_0(5)` proves `F_3(tau_*^{+-}) = 2 E_3(i)` beats ALL `6` `Gamma_0(5)` coset images of `rho` (minimum coset value `> 114 / 10`, gap `> 2`, because `5 == 2 (mod 3)` is inert in `Q(sqrt(-3))` while `5 = 2^2 + 1^2` splits in `Q(i)`) AND beats the CP-conserving `W_5`-fixed point `i / sqrt(5)` (`F_3 > 464 / 10`, gap `> 37`, nearly `5x` deeper), AND unbiased coordinate descent from `6` distinct starting points across `X_0(5)` converges to `F_3(tau_*^{+-})` within `< 1 / 10^10`.

3. **Exact Dark-Matter Stabilizer Census & `COSMOLOGY_LEDGER` Row 4 Closure (`OW9-B`):**
   - **`OW9-B1` (Zero-Mode `nu^c` / `N2` No-Go Theorem):**
     - Construct all `60` even permutations of `A_5` explicitly, partition into exact conjugacy classes (`1 + 12 + 12 + 15 + 20 = 60`), and prove directly that zero nontrivial proper class unions containing the identity have order dividing `60` (`A_5` is simple -> zero index-`2` subgroup, zero `A_5`-induced `Z_2` dark-matter parity).
     - Verify across all `8` species `(Q, u^c, d^c, L, e^c, nu^c, H_u, H_d)` in non-SUSY `Spin(10)` `16 + 10 + 45` that `P_M = (-1)^{3(B-L)}` equals fermion number `(-1)^F` on `8 / 8` species (zero protection beyond Lorentz invariance).
     - Exhaustively enumerate all `G_SM x SL(2, C)` invariant single-`nu^c` decay operators (`1` `nu^c`, `0` `nu^c_bar`, `SU(3)` triality `0 mod 3`, `SU(2)` doublets `0 mod 2`, `6Y = 0`, exact chiral Weyl parities `(n_L, n_R)`) up to mass dimension `6`:
       - Exact count: **`17`** `0`-derivative Lorentz-scalar decay operators (`14` strictly `B-L`-conserving, led by `dim 4` `nu^c L H_u` already forced by `A2-OW3` `X:HOL` and `nu^c L H_d_bar`, plus `3` `|Delta(B-L)| = 2` at `dim 5`) and **`5`** `1`-derivative (`D_mu`) decay operators (`3` strictly `B-L`-conserving at `dim 6`, `2` `|Delta(B-L)| = 2` at `dim 5`).
     - Verdict: zero-mode `nu^c` has **no** forced exact stabilizing symmetry.
   - **`OW9-B2` (Exact `T^2 / Z_2` Gaussian-Norm KK Shells & Conditional `GL(2, Z)`-Invariant `Z_2 x Z_2` LKP Stabilizer):**
     - Verify exact integer identity `Q(m, n) = |m + n tau_*|^2 / Im(tau_*) = 5 m^2 + 4 m n + n^2 = (2 m + n)^2 + m^2` (exact `Z[i]` Gaussian norm) for all `|m|, |n| <= 6`.
     - Certify lowest nonzero `T^2 / Z_2` unordered pairs: `Q = 1` (`{(0, 1)}` grade `(0, 1)` and `{(1, -2)}` grade `(1, 0)`), `Q = 2` (`{(1, -1)}` and `{(1, -3)}`, both grade `(1, 1)`), `Q = 4` (first trivial `(0, 0)`-grade KK shell, mass ratio `2`).
     - Enumerate all `547` primitive hyperbolic `GL(2, Z)` mapping-torus classes of `trace <= 50` (`363` `PSL(2, Z)` `det = +1` plus `184` `PGL(2, Z) \ PSL(2, Z)` `det = -1`, matching `A2-OW5`) and verify directly that `547 / 547` induce `M mod 2 in GL(2, F_2) = S_3` fixing `(0, 0)` and bijectively permuting `{(1, 0), (0, 1), (1, 1)}` (`0` failures), while `m004` (`[[2, 1], [1, 1]]`) acts as a `3`-cycle fixing `0` single `Z_2` characters.
     - Therefore, the `Q = 1` lightest KK particle (LKP) is **conditionally strictly stable** against decay to any finite number of `(0, 0)` SM zero modes at all orders — **if and only if** fixed-point brane operators respect `E[2]` half-period democracy (`sum_{p in E[2]} (-1)^{m p_1 + n p_2} = 0` for every non-trivial grade, whereas a single-puncture `(0, 0)` operator evaluates to `+1` on every grade and opens LKP decay).

4. **Planted-Fault Self-Checks (`OW9-C`, `4 / 4`):**
   - `PF-OW9-1`: Dropping internal `A_5, A_6` odd gauge polarizations shifts bulk KK `n_B - n_F` per `T^2` lattice point (bulk `2H`) from `-68` to `-80` (`caught`).
   - `PF-OW9-2`: Flipping the Berezin fermion Casimir sign makes `rho_Casimir` negative (`AdS`, `< 0`) instead of positive (`dS`, `> 0`) (`caught`).
   - `PF-OW9-3`: Ignoring chiral `(n_L, n_R)` `SL(2, C)` parity inflates `0`-derivative single-`nu^c` decay operators from `17` to `34` (`caught`).
   - `PF-OW9-4`: Breaking `E[2]` half-period democracy with a single-puncture `(0, 0)` brane operator gives nonzero coupling `+1` on `(0, 1)` and `(1, 0)` grades, opening LKP decay (`caught`).

## 2. Guardrails & Cold-Room Protocol

- Strict `0` float/complex AST literals and `0` `frontier/` imports; `A`-only `SHA-256` manifests; zero hardcoded proof flags; independent Cold-Room Referee built solely from this card using disjoint methods (e.g. Poisson-resummed theta-function / direct Mellin quadrature for `E_3(tau)`, disjoint explicit `A_5` normal-subgroup check via `SL(2, F_5) / {+-I}` or Cayley permutations, disjoint `SU(3) x SU(2) x SL(2, C)` operator enumerator, and disjoint continued-fraction/Lagrange-Gauss `547`-class `GL(2, F_2)` audit). `0 of 19.`
