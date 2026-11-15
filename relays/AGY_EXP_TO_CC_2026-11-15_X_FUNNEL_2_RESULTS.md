# `X-FUNNEL-2` Results — `S`-Covariance Closure (`R0`), $\Gamma(5)$ Holonomy Obstruction vs `m004` Root-Orbit Transport (`P-860`, `P-856`), Casimir Partial-Kill, and Exact Order-Fifteen Surjection (`P-862` Step Two) (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Four-Commit Seal:**
  - Commit One (Card): `1f1f09d49` (`relays/cards/AGY-EXP_X-FUNNEL-2_flat-connection-m004-orbit-and-sector-exponent-laws.md`)
  - Commit Two (Standalone Zero-Import Verifier + Hash): `b736f058d` (`relays/x_funnel_2_verify/verify_x_funnel_2.py`)
  - Commit Three (Raw Output Committed Unread + Hash): `faa543a0a` (`relays/x_funnel_2_verify/verify_x_funnel_2_out.json`)
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared.
- **Check State (Protocol Section `12`):**
  - `R0` (`S`-covariance linear dual-cutoff mend): `computed once` against unfolded Gaussian lattice sum, `expectations committed first` (`E0_S_Covariance_Fix_passed = true`).
  - `Part 2A` ($\Gamma(5)$ holonomy obstruction on $X(1)$, `m004` root-orbit parallel transport, and twin-even orientation-odd quartic commutator): `computed once`, `expectations committed first`, `tested against planted errors` (`all_planted_controls_passed = true`; one genuine algebraic cancellation on Frame C's second sector at $\tau + 5$ caught by `E1` and explained below without touching `faa543a0a`).
  - `Part 2B` ($\mathrm{SU}(3)$ Casimir shift partial-kill, exact Order-`15` Surjection across all `192` primitive points, and `P-862` Step Two cusp-exponent tables at orders `5`, `10`, `15`, and `30`): `computed once`, `expectations committed first`, `tested against planted errors` (`E2_Casimir_PartialKill_passed = true`, `E3_Order15_Surjection_and_P862_Exponents_passed = true`).

---

## 1. `R0` and `Part 2A` — Closure of Stage One's `S`-Covariance Regression, Answer to `B1945` Section `6` / `P-860`, and Twin-Even CP Commutator (`P-856`)

### 1A. Closure of `R0` (`E0_S_Covariance_Fix_passed = true`)

Replacing the quadratic dual-sum cutoff by the exact linear `erfc` tail bound $l_{\max}(n_a) = \lceil \text{thresh} / (2\pi \tau_2 |n_a|) \rceil + 6$ when $n_a \neq 0$ reduces the `S`-transformation residual across all three charged sectors at $\tau = 13/100 + (17/10)i$ (`where Im(-1/tau) = 17000/29069 < 3/5`) from Stage One's four parts in a billion to `< (1/1000)^{16}`, matching the unfolded two-dimensional Gaussian lattice sum at both $\tau$ and $-1/\tau$ to `< (1/1000)^{15}`.

### 1B. Answer to `B1945` Section `6` and `P-860 (a)/(b)` — Why Equal-Weight `24`-Point Sums Fail on $X(1)$ and What `E1` Caught

1. **Magnetized Level-Three Obstruction on $X(1)$:**
   - Under $T^5: \tau \to \tau + 5$ (`in Gamma(5), fixing every torsion coordinate w in P_5`), the determinant holonomy ratio $\det Y(\tau + 5, w) / \det Y(\tau, w)$ of the magnetized triple overlap varies across $w \in P_5$ with spread exceeding `19/10` (and off-diagonal entry-ratio spread exceeding `17/10`). Consequently, no $w$-independent gauge pair $(U_L, U_R)$ exists on $X(1)$ such that $Y_{\mathrm{aligned}}(\tau + 5, w) = U_L Y_{\mathrm{aligned}}(\tau, w) U_R^\dagger$ simultaneously for all $w \in P_5$; the equal-weight `24`-point matrix sum shifts its singular-value ratios by `> 15/1000` under $T$ and by `> 22/1000` under $T^5$.
2. **Exact Disclosure on `E1_Gamma5_Obstruction_and_m004_CP_passed = false` (`Frame C` Second Sector at $\tau + 5$):**
   - `E1` required `frame_c_T5_det_holonomy_spread > 1/2` on the second charged sector `(1, 2)` at $\tau + 5$, whereas `faa543a0a` returned `< (1/1000)^{15}` (`zero spread!`) and `< (1/1000)^{16}` singular-value shift on Frame C's `24`-point sum at $\tau + 5$.
   - **Algebraic Cause:** Under $\tau \to \tau + 5$ with $(a, b) = (k_a/5, k_b/5)$ fixed, Frame C's product $\vartheta_{c_s}(0|\tau)\vartheta_{d_s}(0|\tau)$ acquires the upper-parabolic phase $\exp(\pi i \cdot 5 (\alpha_+^2 + \alpha_-^2) / 2) = \exp(2\pi i (q_L^2 + q_R^2) k_a^2 / 5)$. For the second sector `(1, 2)`, $q_L^2 + q_R^2 = 1^2 + 2^2 = 5 \equiv 0 \pmod 5$, making $(q_L^2 + q_R^2) k_a^2 / 5 = k_a^2 \in \mathbb{Z}$ an exact integer! By contrast: (i) in Frame C's first sector `(1, -4)`, $1^2 + (-4)^2 = 17 \not\equiv 0 \pmod 5$; (ii) Frame C's equal-weight `24`-point sum still breaks $T^1: \tau \to \tau + 1$ (`ratio shift > 12/1000`) and $S: \tau \to -1/\tau$ (`ratio shift > 21/1000`) because the Weil permutation representation on $\mathbb{C}[P_5]$ is reducible without an intertwining flat connection across distinct cusps; and (iii) in magnetized level-three, dividing by flux $I = 3$ turns the phase denominator into $3 \times 5 = 15$, so $5 / 15 = 1/3 \notin \mathbb{Z}$ breaks even $T^5$ on `(1, 2)`. Commit `faa543a0a` stands untouched.

### 1C. `m004` Root-Orbit Parallel Transport (`O4`) and Twin-Even / Orientation-Odd Quartic Commutator (`Addressing P-856`)

1. **Intrinsic Root-Orbit Selection inside $P_5$:**
   - Under the inverse monodromy action $w \mapsto w M^{-1} \pmod 1$ of `m004` ($M = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$), $P_5$ decomposes canonically into `4 + 10 + 10`: the unique `4`-point $\mathrm{Pin}(2)$ eigenline $\mathcal{O}_4 = \{(1/5, 2/5), (2/5, 4/5), (3/5, 1/5), (4/5, 3/5)\}$ satisfying $w M^{-1} \equiv -w \pmod 1$, cycled as a single `4`-cycle by the orientation-reversing tick $J^{-1}$ ($J = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$), while the remaining twenty points split into two orbits of size `10`. The planted non-eigenline `4`-point control `PC_FUNNEL2_WrongOrbit` escapes under $J^{-1}$ on all `4` points.
2. **Twin-Even / Orientation-Odd Quartic CP Commutator (`P-856`):**
   - For $H_f(\tau, w) = Y_f(\tau, w) Y_f(\tau, w)^\dagger$, the Haar-invariant quartic commutator $\mathcal{I}_{\mathrm{CP}}(\tau, w) = \frac{1}{6}\operatorname{Im}\operatorname{Tr}([H_1, H_2]^3)$ (`invariant under ten random gauge-allowed Haar rotations to < (1/1000)^{16}`, while distinct left-handed Haar rotations scramble it by `> 11/100`) satisfies two exact parities on $\mathcal{O}_4$:
     - **$\mathrm{Pin}(2)$ Twin-Even:** $\mathcal{I}_{\mathrm{CP}}(\tau, -w) = +\mathcal{I}_{\mathrm{CP}}(\tau, w)$ to `< (1/1000)^{16}` across $\mathcal{O}_4$ (`around -61/10000` on the twin pair $\{(1/5, 2/5), (4/5, 3/5)\}$ and `-721/10000` on $\{(2/5, 4/5), (3/5, 1/5)\}$ at $\tau = 13/100 + (17/10)i$). Reversing the flat holonomy $w \mapsto -w \equiv w M^{-1} \pmod 1$ while keeping the fixed background magnetic flux chirality $(I_L, I_R) = (+3, -3)$ does **not** conjugate $Y_f$, so twin pairing on `m004` does **not** cancel $\mathcal{I}_{\mathrm{CP}}$!
     - **Fiber Orientation-Odd:** Reversing the fiber complex structure and homology orientation $(\tau, a, b) \mapsto (-\bar{\tau}, a, -b)$ conjugates $Y_f$ and sends $\mathcal{I}_{\mathrm{CP}} \mapsto -\mathcal{I}_{\mathrm{CP}}$ to `< (1/1000)^{16}`.
3. **Zak-Dressed Hermitian Orbit Sum $\overline{H}_f(\tau)$:**
   - Dressing each point $w \in \mathcal{O}_4$ by the canonical Landau-gauge Zak parallel-transport unitary $U_{\mathrm{Zak}}(a, b)_{k, l} = \delta_{k, l}\exp(2\pi i q_L b (k + 3a))$ restores exact $b \to b + 1$ periodicity of $H_f^{\mathrm{Zak}}(\tau, w)$ on $E_\tau[5]$ (`residual < (1/1000)^{15}`). In the bulk (`Im tau = 17/10`), $\overline{H}_1(\tau) = \frac{1}{4}\sum_{w \in \mathcal{O}_4} H_1^{\mathrm{Zak}}(\tau, w)$ lifts the `(2/5, 4/5)` light-generation degeneracy (`1 - sigma_1/sigma_2 > 41/1000`), while at cusp height `30` it preserves $|V_{3, 3}| > 1 - (1/1000)^{4}$ (`14` nines in `faa543a0a`) with exponentially small cusp splitting (`around five parts in one hundred million`, honest asymptotic decay of the `(1/5, 2/5)` light doublet at height `30`).

---

## 2. `Part 2B` — Casimir Shift Partial-Kill, Exact Order-Fifteen Surjection, and `P-862` Step Two Cusp-Exponent Tables

### 2A. Diagonal $\mathrm{SU}(3)$ Casimir Shift $M_{\mathrm{Cas}}^2 = 4/3$ (`E2_Casimir_PartialKill_passed = true` — Clean Partial-Kill)

Replacing $(-\Delta_{\tau, A_H})^{-1}\delta_0$ in the color-charged sectors (`sec1`, `sec2`) by the massive Yukawa–Helmholtz Green's function $(-\Delta_{\tau, A_H} + 4\pi M_{\mathrm{Cas}}^2)^{-1}\delta_0$ with quadratic $\mathrm{SU}(3)$ fundamental Casimir $M_{\mathrm{Cas}}^2 = 4/3$ (`while keeping colorless sec3 at M_{Cas}^2 = 0`) preserves exact $\mathrm{SL}(2, \mathbb{Z})$ $T$- and $S$-covariance (`residual < (1/1000)^{14}`). On all four points of $\mathcal{O}_4$, it breaks `B1934`'s order-five copy in the heavier-pair direction $(\sigma_2/\sigma_3)_{\mathrm{sec3}} > (\sigma_2/\sigma_3)_{\mathrm{sec2}}$ (`around 444/1000 vs 181/1000` on `(1/5, 2/5)` and `576/1000 vs 248/1000` on `(2/5, 4/5)`), **but fails** the opposite-skew test on the lighter ratio (`(\sigma_1/\sigma_2)_{\mathrm{sec3}} > (\sigma_1/\sigma_2)_{\mathrm{sec2}}` on all four points of $\mathcal{O}_4$: `770/1000 vs 410/1000` and `524/1000 vs 299/1000`), because uniform diagonal Yukawa screening steepens both ratios in the same direction. We record this as a clean **partial-kill** of pure diagonal Casimir screening as a standalone mechanism for opposite consecutive skew.

### 2B. Exact Order-Three Blindness & Order-Fifteen Surjection Theorem + `P-862` Step Two Tables (`E3_Order15_Surjection_and_P862_Exponents_passed = true`)

1. **Theorem (`Order-Three Blindness & Order-Fifteen Surjection`):**
   - Because all three hypercharges of the third charged sector $(-3, +6, -3)$ are divisible by `3`, shifting any torsion coordinate $w$ by a primitive `3`-torsion point $w_3 \in E_\tau[3] \setminus \{0\}$ shifts $(q_L w, q_R w, q_H w)$ by lattice vectors in $\mathbb{Z} + \mathbb{Z}\tau$. Every primitive order-`15` point decomposes uniquely via Bézout ($p/15 \equiv 2p/5 - p/3 \pmod 1$) as $w_{15} = w_5 + w_3$ (`192 = 24 x 8` points). Combining order-`3` blindness of `sec3` with `B1934`'s order-`5` transposition identity on $w_5$ yields an **exact bulk identity across all `192` primitive order-`15` points**:
     $$\text{ratios}\big(Y_{\mathrm{sec3}}(\tau, w_5 + w_3)\big) = \text{ratios}\big(Y_{\mathrm{sec3}}(\tau, w_5)\big) = \text{ratios}\big(Y_{\mathrm{sec2}}(\tau, w_5)\big) \quad \forall \tau \in \mathcal{H}!$$
   - Verified across all `192` points in **both** Frame C (`max diff < (1/1000)^{14}`) and the magnetized level-`3` triple overlap (`max diff < (1/1000)^{14}`), while `sec2(w_5 + w_3)` splits from `sec2(w_5)` by `> 46/100` in Frame C and `> 26/100` in magnetized level-`3`! The planted non-divisible control `PC_FUNNEL2_NotDivBy3` (`charges (-2, 5)`) breaks order-`3` blindness by `> 11/100`.
2. **`P-862` Step Two Exact Cusp-Exponent Tables (`Orders 5, 10, 15, and 30`):**
   - **Frame C (`B1788` exact piecewise rational law, cross-checked against high-precision `mpmath` ratios between heights `40` and `60`):**
     - **Order `5` (`24` pts) & Order `10` (`72` pts):** `distinct e_{23}` is `{1/5, 1/2}` in **both** `sec2` and `sec3` (`order 10 fails to split Frame C's e_{23} between sec2 and sec3 on all 72 points because 2 x (1/2) = 1 in Z!`), with $\min(e_{23}^{(1)}, e_{23}^{(2)}, e_{23}^{(3)}) = (1/10, 1/5, 1/5)$.
     - **Order `15` (`192` pts) & Order `30` (`576` pts):** `sec3` retains `distinct e_{23} = {1/5, 1/2}` (`min = 1/5`), whereas `sec2` splits across seven exact rational values `{2/15, 1/6, 1/5, 7/30, 3/10, 2/5, 1/2}` (`min = 2/15` at $a \in \{2/15, 13/15\}$, where $e_{13}^{(2)} = 37/60 > e_{13}^{(3)} = 11/20$ and $e_{23}^{(2)} = 2/15 < e_{23}^{(3)} = 1/5$, giving opposite consecutive skew $e_{12}^{(2)} = 29/60 > e_{12}^{(3)} = 7/20$!).
   - **Magnetized Level-Three Triple Overlap (`Heights 20 to 30`):**
     - Unlike Frame C (which multiplies $b$ by `2`), the magnetized triple overlap uses `1 x w` on both cycles, so **even order `10`** splits `sec2` from `sec3` (`at (1/10, 1/5): sec2 has (e_{23}, e_{12}) approx (1/100, 89/1000)` vs `sec3 (85/1000, 1/100)` — exact opposite consecutive skew!). At order `15` `(2/15, 4/15)`, `sec3` matches order `5` `(1/5, 2/5)` identically (`(e_{23}, e_{12}) approx (101/1000, 27/1000)`), while `sec2` shifts to `(64/1000, 93/1000)`, realizing opposite consecutive skew (`e_{23}^{(3)} > e_{23}^{(2)}` and `e_{12}^{(3)} < e_{12}^{(2)}`) purely from hypercharge arithmetic mod `3`.

`0 of 19.`
