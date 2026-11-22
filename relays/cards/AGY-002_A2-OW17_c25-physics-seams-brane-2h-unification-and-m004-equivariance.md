# Pre-Registration Card `AGY-002_A2-OW17`: Probing the Three `AGY-C25` Physics Seams (`S2`, `S3`, `S1`)

- **Seat / Branch:** `agy-002` on `agy-002/verify`
- **Date:** `2026-11-22`
- **Empirical Inputs:** `0 of 19` (strict blindness firewall per `docs/seats/README.md` Section 9;
  zero PDG, NuFIT, Planck, or lattice inputs)
- **Motivation:** After accepting and applying all `10 / 10` ledger and hygiene fixes from peer
  review `AGY-C25` (`ff243a545`), this card tests mathematically whether the three substantive
  physics seams identified by `AGY-C25` (`S2`: `10_R = 1H` vs `2H = 10_C`; `S3`: `B = 5 / 7`
  unification vs unpriced `M_{PS} / M_X` & extra scalars; `S1`: `m004` `3`-cycle equivariance on
  `E[2] \ {0}` vs non-degenerate flavor hierarchy) admit clean internal closures or exact no-gos.

## 1. Pre-Registered Tasks, Expectations, and Failure Conditions

### Task `OW17-A` (Seam `S2`: Bulk vs `4D` Brane `2H` Across `Spin(10)` and `E_6` in `6D` Casimir + `4D` FRG)

1. Compute exact `6D` bulk Casimir supertraces `n_B - n_F` per `T^2` lattice point (`rho_Casimir
   propto (n_F - n_B) E_3(tau)`) for six configurations:
   - `Spin(10)` (`N_V = 45, N_W = 48`): `4D` brane `2H` (`h_pt = 0`), bulk `2H` (`h_pt = 4`),
     bulk `10_R` (`h_pt = 5`, `1H` only), bulk `10_C` (`h_pt = 10`, `2H`).
   - `E_6` (`N_V = 78, N_W = 81`): `4D` brane `2H` (`h_pt = 0`), bulk `27_H` (`h_pt = 27`).
   - **Expectation:** Exact Lie-algebraic equality `N_V - N_W = -3` holds for BOTH `Spin(10)` and
     `E_6`, yielding `n_B - n_F = -6` (de Sitter stabilizing `tau_*^{+-}`) for BOTH `Spin(10)` and
     `E_6` with `4D` brane `2H`, while bulk `10_C` (`+4`) and bulk `27_H` (`+21`) are AdS.
2. Solve the exact `4D` Litim FRG `Type II` (`f_W = 1`) and `Type I` (`f_W = 2`) gravity-matter
   fixed points `(g_*, lam_*)` and gravitational quartic anomalous dimension `f_lam` (both `dD` and
   `LDW` gauges, central-FD agreement `< 10^{-12}`) for all configurations, especially `Spin(10) +
   brane 2H` (`N_S = 8`) and `E_6 + brane 2H` (`N_S = 8`).
   - **Expectation:** `Spin(10) + brane 2H` (`N_S = 8`, `N_eff = -6`) AND `E_6 + brane 2H`
     (`N_S = 8`, `N_eff = -6`) each possess unique weak-coupling UV fixed points (`g_* > 0`,
     residual `< 10^{-40}`) with `f_lam > f_crit` in BOTH `Type II` and `Type I` (`dD` and `LDW`),
     preserving UV irrelevance (`lam_0 -> 0`) AND closing Seam `S2` without `10_R` or bulk `10_C`.
3. Solve the coupled `4`-quartic `2H` Type-II UV fixed points at `Spin(10) + brane 2H` (`N_S = 8`,
   blind UV benchmark `g_UV = 13/25, y_t = 11/20, y_b in {1/100, 9/20}`) and run exact `1`-loop
   downward `2H` RGE (`t = 0 -> -38`), checking IR convergence diff vs `lam_UV = 0` (`< 3 / 1000`).
4. Recompute conformal `xi = 1 / 6` induced gravity `c_log` and replica BH entropy
   `c_log_ent + c_log_contact == c_log` for `Spin(10) + brane 2H` (`33` massive Proca, `0` heavy
   color-triplet scalars, `3` RHN).
   - **Expectation:** `c_log = 33 / 2 > 0` (attractive; exact `c_log_ent + c_log_contact == 33 / 2`)
     and `1`-loop `Spin(10)` beta with brane `2H` stays asymptotically free (`b = -76 / 3 < 0`).
- **Failure condition:** Any fixed-point residual `>= 10^{-35}`, FD mismatch `>= 10^{-12}`,
  `f_lam <= f_crit` for `Spin(10) + brane 2H`, IR quartic diff `>= 3 / 1000`, or `c_log` mismatch.

### Task `OW17-B` (Seam `S3`: Exact `B = 5 / 7` Closure Census — `2`-Loop `2H` SM, `6D` KK, & `45`/`27` Cosets)

1. Compute the exact `1`-loop vector `b_i` and `2`-loop Machacek-Vaughn gauge matrix `B_{ij}` and
   Yukawa matrix `c_{i,f}` from first-principles Dynkin/Casimir sums over `3 x 16 + n_H` doublets
   (`n_H = 1` and `n_H = 2`), verifying exact rational agreement against the textbook SM (`n_H = 1`)
   and `2H` SM (`n_H = 2`) matrices.
2. Integrate exact `2`-loop `2H` SM gauge-Yukawa RGE downward from unified `g_1 = g_2 = g_3 = g_UV`
   across blind `1 / alpha_UV in {20, 25, 30, 35, 40}` (`t = 0 -> -35`, `y_t(0) = 1/2`, `y_b = 1/20`,
   `y_tau = 1/20`, zero PDG inputs) and compute `B_eff^{(2-loop)} = (a_2^-1 - a_3^-1)/(a_1^-1 - a_2^-1)`.
   - **Expectation:** Across the entire blind grid, `|B_eff^{(2-loop)} - 5/9| < 5 / 100`, strictly
     below `5 / 7` (`B_eff^{(2-loop)} < 62 / 100 < 5 / 7`), proving exact `2`-loop running alone
     cannot close `B = 5 / 7`.
3. Enumerate exact `1`-loop `(Delta b_1, Delta b_2, Delta b_3)` and exact threshold fraction
   `r = (5/7 - 5/9) / (B_{int} - 5/9)` for EVERY irreducible SM/PS sub-multiplet inside:
   - `Spin(10)` `45` adjoint (specifically including the `6D` gauge `A_5, A_6` coset scalars:
     `(15, 1, 1)_R` of `PS(4, 2, 2)`, `(8, 1, 0)_R`, `(1, 3, 0)_R`, and `(6, 2, 2)`),
   - `Spin(10)` `10`, `16`, and `E_6` `27` exotics (`(3, 1, -1/3)`, `(1, 2, -1/2)`).
   - Also compute exact `6D` KK-tower `B_{KK}` for complete `Spin(10)`, `PS(4, 2, 2)`, and `E_6`
     bulk parity sectors.
   - **Expectation:** Complete `Spin(10)` and `E_6` bulk KK multiplets shift `(b_1, b_2, b_3)`
     universally (`Delta b_1 = Delta b_2 = Delta b_3`, zero shift to `B`). Inside `45` ALREADY
     present in `Spin(10)`, check whether `(15, 1, 1)_R` or `(1, 3, 0)_R` / `(8, 1, 0)_R` achieves
     `0 < r < 1` (requiring NO representation outside `45 + 3 x 16 + 2H`!), while still proving
     the exact Guardrail-5 theorem that whenever `B_{IR} = 5 / 9 != 5 / 7`, ANY single intermediate
     threshold requires `0 < r < 1` and therefore mathematically forces `1` continuous mass ratio
     `M_{int} / M_X` (unless `M_{int} / M_X` is fixed dynamically by a separate mechanism).
- **Failure condition:** First-principles `B_{ij}` mismatch vs textbook `n_H = 1, 2` matrices, ODE
  step-halving error `>= 10^{-10}`, or missing/incorrect Dynkin index in any representation.

### Task `OW17-C` (Seam `S1`: `m004` `E[2] \ {0}` Equivariance No-Go, Complex Circulants, & `E[n]` Orbits)

1. Construct the exact `3 x 3` permutation matrix `P` of `m004 = [[2, 1], [1, 1]] mod 2` on
   `E[2] \ {0}` and compute its exact rational commutant in `M_3(Q)` (dimension `3`: circulants
   `a I + b P + c P^2`) and diagonal commutant (dimension `1`: `a I_3`), plus exact `3 x 3` DFT
   diagonalization `F_3^* C F_3 = diag(lam_0, lam_1, lam_2)`.
   - **Expectation:** Prove exact degeneracy `|lam_1| == |lam_2|` for ALL real symmetric circulants
     (`b = c in R`, exact `m_1 == m_2` No-Go) and compute exact singular-value sensitivity showing
     that achieving `m_1 / m_3 < 10^{-4}` in a complex `m004`-equivariant circulant requires
     `O(10^{-4})` fine-tuning of `a + b omega + c omega^2 -> 0`.
2. Test `m004`-equivariant complex circulant right-handed dressings `Y_f' = Y_f^{(0)} C_{R,f}` on
   `A2-OW6`'s exact `E[5] + E[6]` (`m_L = 8`) Yukawa matrices at `tau_*^+ = (2 + i) / 5`, with a
   `10`-trial Haar `U(3)_L x U(3)_R` basis-scrambling check (Guardrail 3, drift `< 10^{-35}`):
   - Compare natural `O(1)` complex circulants (`|a|, |b|, |c| ~ 1`, zero fine-tuning) against
     `m004`-breaking exponential localization `D_{R,f}`.
   - **Expectation:** Natural `O(1)` `m004`-equivariant circulants preserve `m004` symmetry and
     Haar invariance but CANNOT generate `m_1 << m_2 << m_3` (`min sigma_1 / sigma_3 > 1 / 100`
     without fine-tuning), proving the exact `S1` Dichotomy: exponential flavor hierarchies require
     explicitly breaking `m004`'s `3`-cycle on `E[2] \ {0}`.
3. Compute the exact orbit decomposition of `m004 = [[2, 1], [1, 1]]` on `(Z / n Z)^2` for
   `n in {2, 3, 4, 5, 6, 8}`, identifying exact invariant lines / short orbits (e.g., on `E[5]`,
   char poly `(x - 4)^2 mod 5` gives invariant 1D eigenline `span((1, 2))` of orbit size `2`; on
   `E[3]`, `M^2 = -I mod 3` gives `2` orbits of size `4`; on `E[6]`, exact product structure).
- **Failure condition:** Commutant dimension mismatch, DFT residual `>= 10^{-40}`, Haar invariance
  drift `>= 10^{-35}`, or orbit partition sum `!= n^2`.

### Task `OW17-D` (`4 / 4` Planted Fault Controls `PF-OW17-1..4`)

1. `PF-OW17-1`: Replace brane `2H` (`h_pt = 0`) with bulk `10_C` (`h_pt = 10`) -> `6D` Casimir dS
   check MUST fail (`n_B - n_F = +4 > 0`).
2. `PF-OW17-2`: Scale `B_{ij}` by `2` -> textbook `n_H = 1` Casimir identity MUST fail.
3. `PF-OW17-3`: Pass `D = diag(1, 2, 4)` to `[P, D] == 0` -> commutant check MUST fail.
4. `PF-OW17-4`: Replace `U_L` with non-unitary `diag(2, 1, 1)` in Guardrail-3 test -> invariance
   check MUST fail (`drift > 1 / 10`).

## 2. Custody & Hygiene Rules

- Strictly `0` Python `float` or `complex` AST literals; `0` imports from `frontier/` or between
  producer and referee; `mp.mp.dps = 55`.
- Pre-hash script BEFORE running; zero in-place edits after pre-hashing.
- Every line of every markdown file strictly `<= 680` characters; neutral section-12 check labels.

0 of 19.
