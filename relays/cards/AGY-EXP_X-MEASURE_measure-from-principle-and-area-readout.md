# Card `X-MEASURE` (with `M23` Area Readout and `M24` Cold Read of `B1936`) — Pre-Registered Expectations

- **Seat:** `agy-exp`
- **Messages:** `M23` (area measure with cusp treatment), `M24` (cold read of `B1936`), and `M25` (`X-MEASURE`: move-count vs hyperbolic area measure from principle)
- **Empirical firewall:** `0 of 19.` All numerical values will be written exclusively to `relays/x_measure_verify/verify_x_measure_out.json` using position-indexed `(sector, index)` names (`up`, `down`, `lepton`, `mixing` with ascending singular-value indices `1, 2, 3`). `B1932`'s `area_measure.json` is untouched before sealing our output commit.

---

## 1. Scope and Mathematical Setup

1. **Exact Hyperbolic Area-Measure Readout and Cusp Treatment (`M23`, `M25`):**
   - Integrate the `P_5`-averaged canonical-end (`L_2`) frame over the modular fundamental domain `F = {|tau| >= 1, |Re tau| <= 1/2}` against normalized Poincaré area `(3 / pi) dx dy / y^2` across all four `(world, weight)` combinations: `(W_-, W_+) x (Theorem 90 exact weight, old small-cut weight)`.
   - **Cusp compactification and precision split:** Substitute `u = 1 / y in (0, 1 / sqrt(1 - x^2)]` so `(3 / pi) dx dy / y^2 = (3 / pi) dx du` has constant nonsingular Jacobian and exact unit total measure on `F`:
     - **Bulk (`y <= 12`, `u >= 1/12`):** Evaluated via `float64` tensor Gauss–Legendre quadrature using our `4`-patch Chebyshev + `4`-trace Gauss–Newton `tilde_L2` evaluator (checked across two quadrature resolutions).
     - **Cusp (`y > 12`, `0 < u < 1/12`):** At large `y`, singular-value ratios `sigma_1 / sigma_3` decay exponentially (`exp(-pi c y)`) and cross IEEE `float64` machine epsilon around `y ~ 25`, scrambling `float64` singular vectors `U_u, U_d` and corrupting mixing moduli `|V_{ij}|` in the cusp tail (which holds `3 / (12 pi)` — nearly eight percent — of `F`'s hyperbolic area). On `0 < u < 1/12`, we therefore evaluate the frame and complex SVD in arbitrary-precision `mpmath` (where `tilde_L2(tau)` equals its asymptotic punctured-torus cusp limit `tilde_L2(infty)` up to `O(exp(-2 pi y))`, verified directly against the Lamé solver at `y = 12` and `y = 16`).

2. **Testing `M25`'s Three Candidate Principles for Selecting Between Move-Count and Area Measure:**
   - **Candidate A — Maximal Entropy:** Compare symbolic move entropy vs geodesic-flow entropy per unit hyperbolic length via Abramov's suspension formula `h_flow(mu_move) = ln(2) / <ell_step>` against the Bowen–Margulis / Liouville bound `h_flow(mu_area) = 1`.
   - **Candidate B — Invariance Under Refining the Level (`5 -> 10 -> 15`):** Prove and test numerically whether conditioning closed `{L, R}^+` trajectories on admissibility at composite levels `10` and `15` changes the whole-weave `P_5` readout relative to level `5`.
   - **Candidate C — The Pairs Rule (`P-Q7`) and Same-Monoid Dual Filtration:**
     - Test literal `{J, K}` (`J = LP` tick, `K = S^{-1}` undoing), tick-and-swap even-`P` reduced words `{J, J^{-1}, P}`, and undoing-symmetrized reduced words `{L, R, L^{-1}, R^{-1}}` (`K L K^{-1} = R^{-1}`, `K R K^{-1} = L^{-1}`) against `{L, R}^+` move-count and generator-free `mu_area`.
     - **Same-Monoid Dual Filtration Test:** On the *exact same* allowed `{L, R}^+` monoid, exhaustively enumerate all allowed hyperbolic words ordered by **hyperbolic geodesic length `ell(w) <= L_0`** (`tr(W) <= T_max`, exploiting trace monotonicity in `{L, R}^+`) and test whether geodesic-length filtration moves the `{L, R}^+` sum away from `mu_move` toward `mu_area` (Prime Geodesic Theorem).

3. **Cold Read and Algebraic Audit of `B1936` (`M24`):**
   - Exhaustively test all four group automorphisms `m in (Z / 5Z)^x = {1, 2, 3, 4}` and both parity-to-holomorphy pairing signs (`kh mod 2 == mp` vs `kh mod 2 != mp`) on chiral Weyl charges vs Frame C's Dirac charges.

---

## 2. Pre-Registered Expectations (`M1`–`M5`) and Planted Controls (`PC_MEAS_1`–`PC_MEAS_4`)

- **`M1` (Area Measure vs Move-Count & Cusp Behavior):**
  1. Naive `float64` SVD at high `y` (`y >= 45`, `PC_MEAS_1`) exhibits macroscopic singular-vector underflow error on `|V_{12}|, |V_{13}|` relative to high-precision `mpmath` SVD, whereas `mpmath` SVD approaches a smooth finite cusp limit `O_bar(infty)` as `u -> 0^+`.
  2. Hard cusp cutoffs `Y_cut in {5, 10, 20}` (`PC_MEAS_2`) exhibit `O(1 / Y_cut)` truncation bias relative to the full `u in (0, 1 / sqrt(1 - x^2)]` integral.
  3. Exact `mu_area` shifts the seven claimed outputs substantially (`10%` to `80%`, tens to hundreds of SEs) relative to `mu_move` in both `W_-` and `W_+`, pulling singular-value ratios downward because `mu_area`'s `1 / y^2` cusp tail weights large-`y` hierarchical regimes much more heavily than `mu_move`'s `2^{-k}` geometric cusp tail.

- **`M2` (Maximal Entropy Dichotomy):**
  `h_flow(mu_move) = ln(2) / <ell_step>` is strictly less than `1`, confirming `mu_move` and `mu_area` are mutually singular measures maximizing entropy with respect to *different clocks* (`ln 2` per discrete `{L, R}` act vs `1` per unit hyperbolic arclength).

- **`M3` (Level-Refinement Invariance Selects Neither):**
  Both `mu_area` (identically) and `mu_move` (in the `n -> infty` ergodic limit, within `3` SE across levels `5`, `10`, and `15`) are invariant under level refinement on `F`. Thus level refinement selects **neither** measure.

- **`M4` (Pairs Rule `P-Q7` & Same-Monoid Dual Filtration — `"Neither from the three principles alone without a clock axiom; ONE PICKS for area if generator changes beyond {L, R}^+ are admitted"`):**
  1. Literal `<J, K>` (`PC_MEAS_3`) satisfies `K J K^{-1} = -J^{-1}` and stays trapped on the single golden geodesic of `LR`, failing *"every allowed history takes part"*.
  2. Replacing `{L, R}^+` by tick-and-swap `{J, J^{-1}, P}` or undoing-closed `{L, R, L^{-1}, R^{-1}}` shifts the move-count readout by more than `10` SE (`PC_MEAS_4`), whereas `mu_area` is generator-invariant.
  3. Exhaustively filtering the **same** `{L, R}^+` allowed monoid by hyperbolic length `ell(w) <= L_0` (`tr(W) <= T_max`) shifts all four singular-value ratios systematically away from finite-`n` `{L, R}^+` move-count in the direction of `mu_area`, proving both measures sum the same allowed histories under different clocks (`|w|` vs `ell(w)`).

- **`M5` (`B1936` Cold Read — Eliminates Hypercharge Convention, Repackages the One Frame-C Bit in Its Parity-Sign Premise):**
  Only `m in {2, 3}` in `(Z / 5Z)^x` place one chiral Weyl generation into a single parity class of `{1, 2, 3, 4}`. Under same-parity (`kh mod 2 == mp`), both signs of `6Y` give `W_-`; under super-graded opposite parity (`kh mod 2 != mp`, putting the holomorphic fundamental vector boson `Lambda^1(C^5)` opposite even-degree spinor fermions), both signs of `6Y` give `W_+`. Thus in Frame C, choosing same-parity over super-graded opposite-parity carries the exact `1` global bit proved by `X-SCAR`.

`0 of 19.`
