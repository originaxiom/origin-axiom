# SCOPE CARD — Card A2-PEER-SM-LIE2: Blind Cross-Family Independent Verification of `SM-C11` (`P-290, I-31, I-37`) and `SM-R610` (`P-610, P-302, P-288`) (seat code: `fam3-v1-high-03`, `0 of 19`)

- **card id:** A2-PEER-SM-LIE2 (pre-registration; blind cross-family `fam3-v1-high-03` second computation of `fam1-v1-unset-04`'s two Lie-theoretic / modular-anomaly `P-885` cards `SM-C11` and `SM-R610` on `origin/sm/cards @ 1c5b13d0a` that carry `second computation: none`)
- **seat code:** `fam3-v1-high-03`
- **date:** 2026-11-27
- **touches:** `P-290`, `I-31`, `I-37`, `P-610`, `P-302`, `P-288`
- **imports:** `none` (self-contained exact algebra over `Q(zeta_24)`, exact `E_6` / `E_8` Cartan roots, and Borcherds–Skoruppa Riemann–Roch)
- **premises on main (zero trial arcs):** `B1252`, `B1253`, `B1600`, `B1632`, `B1641`, `B1674`, `B1689`, `B1730`, `B1736`, `B1796`, `B1797`, `B1970`, `B1974`, `P-288`, `P-290`, `P-302`, `P-610`, `I-31`, `I-37`
- **blindness & custody:** Strictly `0 of 19`. ZERO `origin/sm/cards` scripts or outputs (`r290*`, `r610*`, `sm_r290*`, `sm_r610*`) opened prior to committing this Scope Card, the independent verifier script, and its unread sealed outputs.

## Pre-Registered Blind Expectations & Falsification Criteria

1. **Module W2A — Blind Verification of `SM-C11` (`CLAIM_2026-11-27_c11_two_doublets_refiled.md`, `P-290, I-31, I-37`):**
   - Independently construct `rho_T = chi_eta^{21} (x) rho_u` in exact cyclotomic arithmetic over `Q(zeta_24)`, verify `det rho_T = chi_eta^9`, generate the full matrix group `G_T = <rho_T(t), rho_T(s)>` (`|G_T| = 96`), and prove its scalar subgroup `Z = {g in G_T : g = zeta I_3}` is **exactly `mu_4 = {1, i, -1, -i}`** (order `4`, zero elements outside `mu_4`).
   - Enumerate all `64` sign dictionaries `s in {+-1}^6` on `{Q, u^c, d^c, L, e^c, nu^c}`:
     * Verify `B1674` moves' anomaly counts (`SU(3)`-free: `16/64`, `SU(2)`-free: `0/64`, `grav`-free given `SU(3)`-free: `4/16`, `0` without `nu^c`) and for `I-31` (`all +1`): QCD exponent `n_{SU(3)} = 12 (mod 24)`, `m = 12 (mod 24)`, Dedekind counterterm `6 K_W == m (mod 24) <=> K_W = k_u + k_d == 2 (mod 4)`.
     * Independently verify Frame C's Higgs triplet transformation `rho_H(t) = R_T, rho_H(s) = e^{-3 pi i / 4} R_S` from `DR(tau)` at `30`-digit `mpmath`, confirming `rho_H` fixes neither `K_F` nor `k_u + k_d`.
     * Verify `F_c` (`Z = mu_4`) restricted discrete anomaly phase `zeta^{3 sum_f w_G(f) s_f}` is identically `1` for `I-31` across all `G in {SU(3), SU(2), grav}` (and count all `F_c`-free dictionaries out of `64`).
     * Verify `F_S` (`SU(3)_F^3`) cubic anomaly `A = sum_f d_f s_f` (`d = (6, 3, 3, 2, 1, 1)`) gives **`A = 16 != 0`** for `I-31` (excluding `I-31` in `F_S` without extra fermions), and count all `A = 0` dictionaries out of `64`.
     * Prove via exact modular linear algebra that `G_SM = (SU(3) x SU(2) x U(1)_Y)/Z_6` realizes **no non-trivial uniform scalar `zeta != 1`** on any dictionary when `nu^c` is present (and for `I-31` even without `nu^c`!), while `E_6`'s `U(1)_psi` (`27 -> 16_{+1} + 10_{-2} + 1_{+4}`) realizes every uniform scalar `zeta` on `I-31` as positive control.
   - *Disagreement criterion:* `|G_T| != 96`, `Z != mu_4`, `I-31` QCD exponent `!= 12` or `K_W != 2 (mod 4)`, `I-31` anomalous on `Z`, `A(I-31) != 16`, or `G_SM` realizing a non-trivial uniform scalar with `nu^c`.

2. **Module W2B — Blind Verification of `SM-R610` (`CLAIM_2026-11-27_w134_against_c8_refiled.md`, `P-610, P-302, P-288`):**
   - Independently construct `rho(S) = zeta_8 P`, `rho(T) = zeta_8 L^{-1}`, prove exact `Mp_2(Z)` relations, prove explicit unitary equivalence `rho ~= rho_T`, verify `det rho = chi_eta^9`, and prove allowed weight-`3/2` twists are exactly `r in {0, 4, 8, 12, 16, 20}` (`r == 0 mod 4`).
   - Implement exact rational Borcherds–Skoruppa Riemann–Roch `chi_k(rho)` (using exact cyclotomic eigenvalue turns in `Fraction`, zero float rounding ambiguity!), calibrate on trivial rep (`k=0,2,4,6,12 -> 1,0,1,1,2`), `eta` (`chi_{1/2} = 1`), and `eta^2` (`chi_1 = 1`).
   - Independently construct `L_6 = V_2 (+) V_4` (`B1641`) from `A_L = P_L (x) g_L`, `A_R = P_R (x) g_R`, `A_St = P_St (x) (g_R g_L^{-1} g_R)` in exact `Q(zeta_8)`, verify `chi_1(V_2) = chi_1(V_4) = chi_1(L_6) = 0` and `B1641` `W3` table (`index(Lambda+, n) = n(|Lambda+| - 3)` for `n = -1, 0, 1`).
   - Evaluate `I(r, cond, m) = -chi_{3/2 + m/2}(rho (x) chi_eta^{r+m}) + sum_{p in cond} chi_{1 + m/2}(p (x) chi_eta^{r+m})` across ALL `6` allowed `r`, ALL `4` conditions `{0, V2, V4, L6}`, and ALL `|m| <= 24`:
     * Prove `E_8` det-1 admissibility `det(rho (x) chi_eta^{r+m}) = chi_eta^c`, `c = 9 + 3(r + m) == 0 (mod 24)` (`<=> m == 5 - r mod 8`) **excludes every whole unit `m = 24 n`** for every allowed twist `r`!
     * Prove C8's count `chi_{3/2 + 12 n}(rho) = 3 n` (`n = 0, 1, 2, 3, 4`) matches `-I(r=0, cond=0, m=24 n)` identically (`m = 24 n <-> O(n delta)`).
     * Find the exact minimum admissible `|m|` yielding `|I| = 3` (expected: **`|m| = 17`**, i.e., `17/24`, with zero admissible three-`27` solutions at `|m| < 17`!).
   - Independently construct all `240` roots of `E_8` from the Bourbaki `8 x 8` Cartan matrix, branch `E_8 -> E_6 x A_2` (`72 + 6 + 162 = 240`) and `27 -> SU(3) x SU(2)` to derive exact `w(27) = (6, 6, 27)` and `w(16) = (4, 4, 16)` from the roots, and prove `K2` (`n_G = w_G * c == 0 mod 24` for `SU(3), SU(2), grav` on the full `27`) is **100% equivalent to `c == 0 (mod 24)`** (given `3 | c` from `det(rho (x) chi_eta^{r+m})`).
   - *Disagreement criterion:* any whole unit admissible, any admissible three-`27` datum at `|m| < 17`, C8 count `!= 3n`, `W134` `m = 24n` differing from C8, or `K2` on the `27` vanishing at any `c != 0 (mod 24)`.

3. **Controls & Hygiene:** `5/5` independent planted fault controls, `0` AST float literals, `0` JSON float literals, standalone exit-1 control with `0` stderr bytes, `0` refused imports under `T7b Part 1`.
