# Card `AGY-002_FOUND-G9` — `4D` Amphicheiral Domain-Wall / `APS` Chiral Localization, `SU(2)_L`-Invariant `2HDM` `Strong-CP = 0`, and Complete `P-864` Canonical-End Repair (`0 of 19`)

## 1. Package and Question

Resolving the amphicheiral zero-index / `SU(2)_L` `Strong-CP` bridge on `X_4 = m004 x~ [-L_4, L_4]` and discharging `P-864` `Q1(a)-(c)` on `origin/main` (`ff8e1ca57`) under strict `0 of 19` firewall, `Guardrails 1-6`, and `100%` mask-safe rational prose:
1. Does a parity-odd `4D` `Callan-Harvey` / `Kaplan` bulk mass kink `M(s) = M_0 tanh(M_0 s)` (`M(-s) = -M(s)`) localize an exponentially trapped left-handed zero mode (`psi_0(s) propto sech(M_0 s)`, `lambda_{L,0} = 0`) while gapping all bulk `3D` `KK` modes (`lambda_{L,n>=1}, lambda_{R,n>=0} >= M_0^2`), yielding `N_g = 3` chiral generations when tensored with `CIM (3, 3, -6)` without bulk `Left-Right` cancellation?
2. On `Re(tau_cusp) = 0`, does a **single `SU(2)_L`-gauge-invariant** doublet holonomy `xi = i eta` (`zeta_R = conj(zeta_L)`) contracted with `2` `D`-parity-symmetric `Pati-Salam` `(1, 2, 2)` bidoublet vectors (`v_{(-k) mod 6} = conj(v_k)`) yield `Y_u = Y_u^dag, Y_d = Y_d^dag` (`< (1/10)^14`), `|bar_theta_QCD(IR)| < (1/10)^13` at `2`-loop (`on the +1 det-sign branch`), **and** `|J_CKM| > 1/100` without breaking `SU(2)_L`?
3. Does `SL(2, Z)` `Gauss` reduction `L(t) = L(tau_FD) - ln|c t + d|` eliminate both `NearestNDInterpolator` fallback below `y = sqrt(3)/2` (`-1/(13/100 + 17/10 i)`) **and** the spurious Delaunay chord-lens error (`at 9/10 i` and `-1/(3/10 + 96/100 i)`) to `< (1/10)^14`, and what does a read-only sweep of `B1927..B1949` JSON coordinates find?

## 2. Deliverables and Definition of Done

1. **Parity-Odd `4D` Domain-Wall Localization (`Symbolic + 160-Node Chebyshev Spectral Solver`):**
   - Prove symbolically in `SymPy` `(-d/ds + M_0 tanh(M_0 s)) sech(M_0 s) == 0` and verify on a `160`-node `Chebyshev` grid (`[-8, 8], M_0 = 3`) that `|lambda_{L,0}| < (1/10)^4`, `lambda_{L,1} > 9`, `lambda_{R,0} > 9`, and `|<psi_{L,0} | sech>| > 99999/100000` (`gapping all bulk 3D spinors above M_0^2 = 9`).
2. **`SU(2)_L`-Invariant `Pati-Salam` `(1, 2, 2)` `Strong-CP` & `CKM` Theorem (`Guardrails 2, 3, 4`):**
   - Verify `Y_{2-i, 2-j, (-k) mod 6}(2 sqrt(3) i, i eta) = conj(Y_{j, i, k})` to `< (1/10)^14` with **shared `z_{Q_L}`** (`100% SU(2)_L invariant`); verify `Y_u = Y_u^dag, Y_d = Y_d^dag` (`< (1/10)^14`), `|J_CKM| > 1/50 > 1/100` from `2` `D`-parity-even bidoublet vectors `(v_u, v_d)`, `2`-loop `|bar_theta_QCD(IR)| < (1/10)^13`, and `10`-trial `U(3)^3` `Haar` invariance `< (1/10)^13`.
3. **Complete `P-864` `Q1(a)-(c)` Repair, Chord-Lens Diagnosis, & `B1927..B1949` Coordinate Sweep:**
   - Implement `canon_gauss_reduced(t)` (`reducing |Re z| <= 1/2, |z| >= 1 before interpolation, raising explicit above_ymax flag`); verify `|L(gamma t) - L(t) - ln|c t + d|| < (1/10)^14` across `SL(2, Z)` words at `13/100 + 17/10 i`, `9/10 i`, and `3/10 + 96/100 i` (`diagnosing the Delaunay chord lens sqrt(3)/2 <= y < sqrt(1 - x^2)`), sweep all tracked `tau` coordinates in `B1927..B1949` JSON files for `|tau| < 1`, and verify all `6` prior `Gate 8` `SHA-256` manifests.

## 3. Five Planted Fault Controls That Must Fail When Broken

1. **`PF9.1` (`Parity-Even Constant Mass M(s) = +M_0`):** Replacing odd kink `M_0 tanh(M_0 s)` by constant `+M_0` destroys the chiral zero mode (`lambda_{L,0} > 9 >> 1`).
2. **`PF9.2` (`SU(2)_L-Violating Doublet Holonomy Split`):** Splitting `z_{u_L} != z_{d_L}` inside `Q_L` breaks `SU(2)_L` gauge covariance (`||U_L Q_L - Q_L'|| > 1/10`).
3. **`PF9.3` (`Opposite D-Parity Determinant-Sign Branch`):** Flipping `v_d -> -v_d` on `N_g = 3` odd families flips `sgn det(Y_u Y_d) = -1` (`|bar_theta_QCD| = pi > 3`).
4. **`PF9.4` (`Unreduced canon(t) Below Unit Circle` — `P-864`):** Calling unreduced `LinearNDInterpolator`/`NearestNDInterpolator` at `-1/(13/100 + 17/10 i)` violates `L(-1/t) = L(t) + ln|t|` by `> 1/4` (`and at 9/10 i inside the chord lens by > 1/1000`).
5. **`PF9.5` (`Unflagged Above-Grid Clamping`):** Evaluating at `Im(tau_FD) = 10 > Y_max` triggers `above_ymax == true`.

## 4. Dependencies and Firewall Boundaries

Addresses `P-864` and `X_4` chiral localization on `origin/main` (`ff8e1ca57`). Strict `0 of 19` firewall; touches only `relays/` (`reads B1927/B1667..B1949 JSON data read-only with 0 Python repo imports`). Expectations committed first (`0 of 19`).
