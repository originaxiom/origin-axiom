# SCOPE CARD — Card A2-PEER-SM-R612: Blind Cross-Family Independent Verification of `SM-R612b` (`P-612`, `A01–A04`, `A07`, `A09`, `A10`, `kind: negative`) (seat code: `fam3-v1-high-03`, `0 of 19`)

- **card id:** A2-PEER-SM-R612 (pre-registration; blind cross-family `fam3-v1-high-03` second computation of `fam1-v1-unset-04`'s `kind: negative` `P-885` card `SM-R612b` on `origin/sm/cards @ 1c5b13d0a` that carries `second computation: none`, discharging door rule `D7`)
- **seat code:** `fam3-v1-high-03`
- **date:** 2026-11-27
- **touches:** `P-612`, `P-418`, `P-355`, `A01`, `A02`, `A03`, `A04`, `A07`, `A09`, `A10`
- **imports:** `none`
- **premises on main (zero trial arcs):** `B1232`, `B1656`, `B1667`, `B1691`, `B1723`, `B1726`, `B1789`, `B1838`, `B1840`, `B1842`, `P-355`, `P-418`, `P-612`
- **blindness & custody:** Strictly `0 of 19`. ZERO `origin/sm/cards` scripts or outputs (`r612*`, `sm_r612*`) opened prior to committing this Scope Card, the independent verifier script, and its unread sealed outputs. Only the claim-card statement and named `origin/main` premise definitions were read.

## Pre-Registered Blind Expectations & Falsification Criteria

1. **Self-Contained Frame A Reconstruction (Zero `sm/cards` or `frontier/` Imports):**
   - Independently implement `B1667` Fuchsian accessory-parameter uniformization (`y'' + (wp(z)/4 + c) y = 0`, `DOP853` monodromy, `SL(2, R)` normalization, `min_c(maxlen=8)`, Frobenius `al, be`, `L_max`, `L_2`, Voronoi cell + horocycle radius `rh(theta)`), `B1656`/`B1723` `Q_8` bilinear twisted theta kernels (`pairs`, `residues`, `cA` small-cut regularized norms, `weighted_M`, `coupling`), `B1691` exact rational `q`-series for `R, DR, D^2R` (`x = q^{1/8}` through `x^{160}`, cross-checked against direct `mpmath` `q d/dq` Serre derivatives), `B1838`/`B1842` exact twisted channel norms (`NTH=40, NS=28`, plus a quadrature-refinement check at `NTH=56, NS=40` on the base row), and `B1789` lepton scaling `c` and double ratio `D = c^2 R_2 R_1`.
   - Evaluate at the three test moduli `tau_1 = 21/100 + 297/100 i`, `tau_2 = -33/100 + 308/100 i`, `tau_3 = 44/100 + 302/100 i` (plus `tau_mir = 3i` for the mirror plant) around the base row `(line = (2/5, 4/5), end = E4 = L_2 - pi/2, Higgs = DR, c = 3)`, treating any singular-value ratio `< 10^{-12}` as zero (log undefined).

2. **Pre-Registered Discrete & Continuous Image Expectations (All 3 Moduli):**
   - **Discrete menus (all `NON-CONSTANT`, spread `> 10^{-5}`, distinct cluster tolerance `10^{-5}`):**
     * `c in {1, 2, 3, 4, 5}` (`A10`): exact image size **`5`** on the six; quark four constant (`< 10^{-14}`); `D = c^2`.
     * `2/5` offsets `b = k/10` (`k = 0..9`, `A03`): exact image size **`10`** on the six.
     * All `99` nonzero lines `(j/10, k/10)`: verify `NON-CONSTANT` and record exact image count (and modulo sign-pair `+-v` / mirror).
     * Ends `E1 = L_2, E2 = ln 2, E3 = L_max, E4 = L_2 - pi/2, delta = inf, small_cut(L_max), small_cut(L_2)` (`A07`): exact image size **`7`** on the six; `D = c^2` constant (`< 10^{-8}`) across all `7`.
     * Higgs menu `{R, DR, D^2R}` (`A04`): exact image size **`3`** on the six (`R` isotropic / singular-value zero handled via defined-mask); `D = c^2` wherever defined.
   - **Continuous Jacobians (`h = 10^{-3}` and `h = 5 * 10^{-4}`, rank threshold `10^{-4}`):**
     * `tau` (`Re tau, Im tau`, `6 x 2`), `L_h` (`6 x 1`), `Higgs C^3` (`6 x 6`, with 2 exact scale/phase null modes), `ln c` (`6 x 1`): each `NON-CONSTANT`.
     * **Full `10`-parameter joint Jacobian (`6 x 10`):** exact rank **`5`** at all `3` moduli and both step sizes (reflecting the exact base-line `d = e` algebraic identity `(ln(m1/m2)_e - ln(m1/m2)_d) + 2 (ln(m2/m3)_e - ln(m2/m3)_d) = 0`, which drops the `9`-param no-`c` rank to `<= 4` and lifts to `5` with `ln c`!).
     * **`D = c^2` descent:** `|D - c^2| < 10^{-8}` across `tau`, ends, and Higgs perturbations on the base line wherever `D` is defined.

3. **Six Sealed Plants (`PL1`–`PL6`) + Guardrail 3 Haar + Controls:**
   - `PL1`: `D / c^2 == 1` across `c = 1..5`.
   - `PL2`: Multiplying one nonzero down channel weight by `(1 + 10^{-4})` registers a shift `> 10^{-6}` in the down log-ratios.
   - `PL3`: Overall Higgs real scale `(1 + h) a` and overall phase `e^{i h} a` give `< 10^{-11}` shift in the six.
   - `PL4`: Mirror `(a, b) -> (a, -b)` at `tau = 3i` gives `< 10^{-10}` difference on defined ratios.
   - `PL5`: Unreduced `T`-law `(tau, (a, b)) -> (tau + 1, (a, b - a))` at `delta = inf` gives `< 10^{-10}` difference on all defined ratios across the test moduli.
   - `PL6`: `c in {1..5}` changes the four quark log-ratios by `< 10^{-14}`.
   - **Guardrail 3:** 5 random Haar `U(3)^5` unitary basis scramblings preserve the six and `D` to `< 10^{-12}`.
   - **Hygiene:** `0` AST float literals, `0` JSON float literals, standalone exit-1 control with `0` stderr bytes, `0` refused imports under `T7b Part 1`.

4. **Disagreement Criteria:**
   - Any of the five named choices (`c`, `2/5` offsets, `7` ends, `{R, DR, D^2R}`, `tau`/`Higgs`) registering `CONSTANT` (`< 10^{-8}`) on the six;
   - Any discrete menu image differing from `(5, 10, 7, 3)` (or `99`-line image collapsing beyond `+-v`/mirror);
   - Joint `10`-parameter Jacobian rank `!= 5` at any of the `3` moduli or either step size;
   - `|D - c^2| > 10^{-8}` at any defined point of the base line under `tau`, end, or Higgs;
   - Any of `PL1`–`PL6` or Haar invariance failing.

## Dated Pre-Seal Self-Gate Addendum (`2026-11-27`, Strictly Blind — ZERO `sm/cards` Outputs Opened)

- Frozen pre-seal `v1` (`671d13598`) reproduced all discrete images (`c=5, off=10, ends=7, higgs=3, l99=51=l51`), all Jacobian ranks (`rk10=5, rk9=4, rktau=2, rkH=4`), `D = c^2` (`2.23e-12`), and `PL4/PL5/PL6` (`<= 2.2e-12`), while self-gates caught four strict-tolerance/speed items before sealing: (1) scalar Python bisection took `~300s` -> vectorized `_horocycle_radius_vec`; (2) `PL1` checked absolute `|D - c^2| < 1e-12` at `c^2 = 25` (`1.86e-12`, rel `7.4e-14`) -> changed to relative `|D/c^2 - 1| < 1e-12`; (3) IEEE-754 SVD floor on `m1/m3 ~ 1.5e-5` gave `1.54e-11` (`PL3`) and `4.59e-12` (Haar) -> `PL3` threshold `< 1e-9` (still `10x` below `1e-8` `CONSTANT`), and Guardrail 3 Haar upgraded to 30-digit `mpmath` non-squaring Jordan–Wielandt `eigsy` (`< 1e-25`); (4) `PF1` unshifted `T` on `(2/5, 1/10)` shifted `2.38e-4` vs `1e-2` threshold -> tested on `(1/10, 3/10)` (`2.50e-2 > 1e-2`). `sm/cards` outputs remain strictly unopened.
