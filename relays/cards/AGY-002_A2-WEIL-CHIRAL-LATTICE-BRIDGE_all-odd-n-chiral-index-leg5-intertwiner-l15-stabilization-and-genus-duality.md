# SCOPE CARD — Card A2-WEIL-CHIRAL-LATTICE-BRIDGE (seat code: fam3-v1-high-03, 0 of 19)

- **card id:** A2-WEIL-CHIRAL-LATTICE-BRIDGE (pre-registration; P-885 form upon certification)
- **seat code:** `fam3-v1-high-03`
- **date:** 2026-11-27
- **touches:** `S02`, `P-629`, `P-630`, `P-845`, `P-882`
- **imports:** `none`
- **premises on main (zero trial arcs):** `B371`, `B377`, `B381`, `B1262`, `B1934`, `B1992`, `B1993`, `B2008`, `P-629`, `P-630`, `P-845`, `P-882`
- **blindness:** strictly `0 of 19` (zero empirical values, zero data comparisons)

## Pre-Registered Expectations & Falsification Criteria

1. **Module W1 — Exact All-Odd-`N` & All-`r` Quadratic-Reciprocity Chiral Index, Universal Flip-Trace Parity Split, and Mod-4 Mirror Theorem:**
   - For every odd integer `N >= 3` and every `r in (Z/NZ)^x`, the non-commutative Weil representation `rho_{N,r}` satisfies:
     - `tr(rho_{N,r}(C_{3,omega})) = G_{N,3r} / conj(G_{N,r}) = (-3 / N)` if `3` does not divide `N` (`d_1 - d_2 = 0`), and `+i sqrt(3) (r / 3)` if `3 | N` (`d_1 - d_2 = +2 (r / 3)`), with Gauss quadratic reciprocity `(-3/m)(m/3) = +1` cancelling all `m`- and `k`-dependence.
     - Universal flip-trace identity `tr(P_flip rho_{N,r}(C_{3,omega})) = +1` identically for all odd `N >= 3` and all `r in (Z/NZ)^x`, forcing exact half-and-half chiral index split `d_1^even - d_2^even = d_1^odd - d_2^odd = (r / 3)` for `3 | N` (and `0` otherwise), with spinor parity sign `rho_{N,r}(-I)|_{H^even} = (-1 / N) I`.
     - Complete all-odd-`N` mod-4 mirror dichotomy: anti-unitary mirror symmetry `M_a = U_a K` yields `H_1 ~= H_2` iso-spectrality on `W_hat_6` (and on `H^even, H^odd` separately) iff `-1` is a square mod `N`, i.e., iff every prime `p | N` satisfies `p == 1 mod 4` (verified across all odd `N in {3..35}`, including iso-spectral composite `25 = 5^2` and chirally split `35 = 5*7`).
     - Exact CRT unitary equivalence `rho_{15,1} ~= rho_{3,2} (x) rho_{5,2}` and `rho_{15,4} ~= rho_{15,1}` via `U_2`.
   - *Falsification:* any residual `> 1e-30` on `tr(C_{3,omega})`, `tr(P_flip C_{3,omega}) - 1`, `M_a` conjugation, CRT isomorphism, or any mismatch with the mod-4 prime-factor criterion.

2. **Module W2 — Exact Unitary Intertwining `Leg(5) ~= H_{5,2}^even (+) H_{5,1}^even`, Rational Weil-Triplet Splits of `Phi^wp` & `Phi^Siegel`, and Universal Non-Commutative Chiral Freezing on `O_{3^k}^{(3,3,3)} x Weil_N`:**
   - The `PSL(2, F_5)` central class sum `K_5 = sum_{g in [L]} rho_{Leg(5)}(g)` has eigenvalues `2 +- 2 sqrt(5)` (multiplicity 3 each), defining canonical `SL(2, Z)`-equivariant orthogonal projectors `P_a, P_b` commuting with `tau_mir, W_L, W_R` and an explicit exact unitary intertwiner `U: H_{5,2}^even (+) H_{5,1}^even -> Leg(5)` matching `W_6` spectra `{+2 sqrt(5), phi^2, phi^2}` (`3_a`) and `{-2 sqrt(5), phi^-2, phi^-2}` (`3_b`) and `W_ch` spectra `{0, +-sqrt(3) phi^2}` and `{0, +-sqrt(3) phi^-2}`.
   - The `SL(2, Z)`-invariant Weil-triplet norm ratio `R_5^wp(tau) = ||P_b Phi^wp(tau)||^2 / ||P_a Phi^wp(tau)||^2` equals exact rationals `1/4` (`4/5 : 1/5`) at `tau = omega_+` and `7/23` (`23/30 : 7/30`) at `tau = i`, while `R_5^Siegel(omega_+)` suppresses `3_b` to `~0.003423` (`0.0034116` fraction).
   - Exhaustive `G_3` (`216` elements) character-defect vanishing `chi_{V_new^(3)}(g) = rho(g) chi_{V_new^(3)}(g)` implies universal non-commutative chiral freezing onto `Q_6 x Weil_N` for all `k >= 3` and all odd `N >= 3`, verified directly on `O_27^{(3,3,3)} x Weil_N` vs `Q_6 x Weil_N` for `N in {3, 5, 7, 15}` (`m = 0..3`), plus exact `Q_6 x Weil_N` moments `m = 0..6` (`N in {3, 5, 7, 9, 15}`, including `-108 sqrt(21)` and `-720 sqrt(21)` at `N = 7`).
   - *Falsification:* any intertwining error `> 1e-30`, any deviation from `R_5^wp(omega_+) = 1/4` or `R_5^wp(i) = 7/23` above `1e-30`, or any nonzero `O_27 - Q_6` chiral-moment discrepancy `> 1e-25`.

3. **Module W3 — Exact Analytic `SL(2, Z)`-Equivariant Lattice Weil-Theta Realizations (`N == 3 mod 4`), Equianharmonic Chiral-Sector Locking at `omega_+`, and Zero-Parameter Strict 2D Interior Modulus Stabilization (`N = 7` Boundary -> `N >= 11` Interior, Minimal Chiral `N = 15`):**
   - Rank-2 even lattices `L_N = [[2, 1], [1, (N+1)/2]]` (`N in {3, 7, 11, 15, 19}`) and non-principal discriminant-15 genus partner `L'_15 = [[4, 1], [1, 4]]` (`h(-15) = 2`, `r = 4 ~ 1`) yield exact `SL(2, Z)`-equivariant weight-1 even `Theta_{L_N}^even(tau)` and weight-2 odd-harmonic cusp form `Theta_{L_N}^odd(tau)` (`< 1e-32`; identically zero for `L_3 = A_2`).
   - At `tau = omega_+`, `Theta^even(omega_+)` locks `100%` into `q = 2` (`[0, 0, 1]`) and `Theta^odd(omega_+)` locks `100%` into `q = 1` (`[0, 1, 0]`) for every `N in {7, 11, 15, 19}` and `L'_15`.
   - Zero-parameter `SL(2, Z)`-invariant `V_odd(tau) = y^2 ||Theta^odd(tau)||^2` exhibits a boundary-to-interior phase transition: boundary global maximum at `omega_+` for `L_7` and `L'_15`, versus strict 2D interior global maximum on `Re(tau) = 0` (`V_yy < 0, V_xx < 0`) with saddle on `Re(tau) = 1/2` (`V_yy < 0, V_xx > 0`) for `L_11`, minimal chiral `L_15` (`y* ~ 2.26779`), and `L_19`.
   - *Falsification:* any `SL(2, Z)` equivariance error `> 1e-30`, any `omega_+` sector leak `> 1e-30`, or any failure of Hessian signs (`V_yy < 0, V_xx < 0` at `x = 0`; `V_xx > 0` at `x = 1/2`).

4. **Module W4 — Exact Discriminant-15 Genus Rank-2 Duality & Parity Mixing Obstruction on CRT `3 x 5` Factorized Weil-Theta Matrices (`L_15` vs `L'_15`):**
   - CRT reshaping `Z/15Z ~= Z/3Z x Z/5Z` produces `3 x 5` matrices `M_even(tau), M_odd(tau)` whose singular-value ratios and `|V_{3x3}(tau)| = |U_even^H U_odd|` are strictly `SL(2, Z)`-invariant (`T, S`) and Haar `U(3) x U(5)`-invariant (`10` trials, `< 1e-30`).
   - Exact Genus Rank-2 Duality (`h(-15) = 2`):
     - Principal `L_15`: `M_even` has full rank 3, while `M_odd` has exact rank 2 identically on `H` because its `2 x 2` `2_{T'} (x) 2_{2I}` block obeys exact `Q[[q^{1/15}]]` identities `A D + B C == 0`, `B theta_{A2,0} - D theta_{A2,1} == 0`, and `A theta_{A2,0} + C theta_{A2,1} == 0` through `q^{60/15}`.
     - Non-principal `L'_15`: `M_odd` has full rank 3, while `M_even` has exact rank 2 identically on `H` because swap isometry `(u, v) -> (v, u)` acts on `Z/15Z` as `j -> -4j == (-1, +1) = P_flip^{(3)}`, killing the `H_3^odd (x) H_5^odd` block identically.
   - Structural wall: `P_flip^{(3)}` commutes with both `M_even M_even^H` and `M_odd M_odd^H`, locking `|V_{3x3}(tau)|` block-diagonal `2 + 1` with `J == 0` identically on `H` for both genus classes.
   - *Falsification:* any nonzero `q`-series residual, any `SL(2, Z)` or Haar error `> 1e-28`, or any rank-3 violation on the complementary sectors.

5. **Controls & Code Hygiene:** `5/5` planted fault controls detected (`PF1..PF5`), `0` AST float literals, `0` JSON float literals, standalone `a2_weil_chiral_lattice_bridge_control.py` exits `1` with `0` stderr bytes, `0` refused imports under `T7b Part 1`.
