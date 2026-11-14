# Card `X-EXACT-W`: Whole-Weave Read-Out in Both Higgs Worlds (`W_-` and `W_+`) Under Theorem `90`'s Channel Weight vs the Small-Cut Weight (`B1667`, `B1838`, `B1919`, `B1927`, `B1928`, `P-847`)

- **Seat:** `agy-exp`
- **Status:** Expectations committed before coding or running `relays/x_exact_w_verify/verify_x_exact_w.py`
- **Blindness & Independence Lock:** Zero imports from `main`. `B1928`'s values (`fiber_ergodic_fine.json`) remain unread until Commit `3` seals all raw output JSON files in git.
- **Empirical & Naming Firewall:** `0 of 19.` All numerical values are written exclusively to JSON; zero measured values are touched anywhere; all outputs are named strictly by `(sector, index)` position, never by particle names.

---

## 1. Exact Mathematical Specification Sealed Before Coding

1. **Move-Count Whole-Weave Read-Out (`P-845`, `B1928`) & Canonical End (`B1667`, `B1927`):**
   - Measure: uniform move-count measure on hyperbolic words in $\{L, R\}^n$ weighted by closed-geodesic hyperbolic length $\ell(w)$, evaluated both via **Route `1`** (exhaustive allowed populations at level `5` for even $n \in \{2, \dots, 18\}$ and odd $n \in \{3, \dots, 17\}$, plus sampled populations at $n \in \{24, 32\}$) and **Route `2`** (`64` independent periodic ergodic trajectories of `2000` moves each = `128000` move steps, integrating the `24`-point primitive order-`5` torsion average over local semicircle charts).
   - Canonical end: `B1667` / `B1927`'s punctured-torus Fuchsian length-`2` horocycle parameter $L_2(\tau) = \pi - \frac{2\pi}{\lambda}\operatorname{Im} B(\tau)$ on $\mathcal{F}$, related to its $\mathrm{SL}(2, \mathbb{Z})$-invariant counterpart by
     $$\tilde{L}_2(\tau) = L_2(\tau) + \tfrac{1}{2}\ln\operatorname{Im}\tau - (\gamma_E + \ln\pi), \qquad e^{-2 L_2(\tau)} = \frac{\operatorname{Im}\tau}{\pi^2 e^{2\gamma_E}}\, e^{-2\tilde{L}_2(\tau)}.$$

2. **Both Higgs Worlds (`P-847`):**
   - Let $S(\tau)$ denote `B1691`'s weight-$3/2$ covariant Higgs triplet (`DR = B[1]`) and $\tilde{S}(\tau) = \varepsilon S(\tau)^* \varepsilon^T$ its hypercharge-conjugate doublet partner:
     - **World $W_-$:** $(\text{up}: \tilde{S},\; \text{down}: S,\; \text{lepton}: S)$,
     - **World $W_+$:** $(\text{up}: S,\; \text{down}: \tilde{S},\; \text{lepton}: \tilde{S})$.

3. **Both Channel Weights (`B1919` Small-Cut vs `B1838` / Theorem `90` Completed-Square Weight):**
   - For each sector and quaternion channel $s \in \{1, i, j, k\}$ with active residue $R_s(\tau, a, b) \neq 0$, let $K_s(z; \tau) = P_s(z; \tau) / R_s(\tau) = \frac{1}{z} + a_{0,s}(\tau) + a_{1,s}(\tau) z + \cdots$ be the normalized channel kernel at characteristic $c_s = u_s + (1/2, 1/2)$.
   - By elliptic quasi-periodicity (`Theorem 89` / `Theorem 93`), $K_s(z; \tau) = \frac{\theta_1'(0|\tau)\,\vartheta[c_s](z|\tau)}{\vartheta[c_s](0|\tau)\,\theta_1(z|\tau)}$ and $\theta_1'(0)/\theta_1(z)$ is odd in $z$, so the exact Laurent constant term is
     $$a_{0,s}(\tau, a, b) = \left.\frac{\partial}{\partial z} \ln \vartheta[c_s](z \mid \tau)\right|_{z=0}.$$
   - Under $\gamma = \bigl[\begin{smallmatrix} p & q \\ c & d \end{smallmatrix}\bigr] \in \mathrm{SL}(2, \mathbb{Z})$, $|a_{0, \gamma\cdot s}(\gamma\tau)|^2 = |c\tau + d|^2 |a_{0,s}(\tau)|^2$ while $e^{-2 L_2(\gamma\tau)} = |c\tau + d|^{-2} e^{-2 L_2(\tau)}$, rendering the product $\pi |a_{0,s}(\tau)|^2 e^{-2 L_2(\tau)}$ strictly $\mathrm{SL}(2, \mathbb{Z})$-invariant (modular weight zero).
   - On the exact same trajectories, evaluate both channel weights side by side in both worlds $W_-$ and $W_+$:
     - **Old small-cut weight:** $N_s^{\mathrm{old}} = 2\pi L_2(\tau) + c_s(\tau) = 2\pi \tilde{L}_2(\tau) + F_{u_s}(\tau)$,
     - **Theorem `90` channel weight:** $N_s^{\mathrm{T90}} = 2\pi L_2(\tau) + c_s(\tau) - \pi |a_{0,s}(\tau)|^2 e^{-2 L_2(\tau)}$.

4. **Seven Claimed Outputs (`(sector, index)` Positions Only):**
   - With singular values ordered ascending $0 \le \sigma_1 \le \sigma_2 \le \sigma_3$ and $V = U_{\mathrm{up}}^\dagger U_{\mathrm{down}}$ in the same `(1, 2, 3)` order, record both ratio conventions (`("up", "2_over_3")`, `("up", "1_over_3")`, `("down", "2_over_3")`, `("down", "1_over_3")` and adjacent `("up", "1_over_2")`, `("up", "2_over_3")`, `("down", "1_over_2")`, `("down", "2_over_3")`) together with the three mixing moduli `("mixing", "1_2")`, `("mixing", "2_3")`, `("mixing", "1_3")`, plus `lepton` ratios to check level-`5` `lepton == down`.

---

## 2. Pre-Registered Expectations & Planted Controls

- **Expectation `EX1` (Contour & Modular Gates):** Closed-form $a_{0,s}$ matches `mpmath` Cauchy circle averages of $P_s(z)/R_s - 1/z$ across all sectors and channels (including high cusp height) to residual below $10^{-13}$; $\pi |a_{0,s}|^2 e^{-2 L_2}$ is invariant under $T$ and $S$ to residual below $10^{-12}$; and $N_s^{\mathrm{T90}} > 0$ holds across all active channels at level `5`.
- **Expectation `EX2` (Sub-Percent Scale Yet High-Significance Paired Shift):** The Theorem `90` correction $-\pi |a_{0,s}|^2 e^{-2 L_2}$ shifts the seven read-out values at the sub-percent scale relative to $2\pi L_2 + c_s$, while paired evaluation along identical paths resolves $\Delta_{\mathrm{T90}} = \mathcal{R}(N^{\mathrm{T90}}) - \mathcal{R}(N^{\mathrm{old}})$ at greater than five paired standard errors in both $W_-$ and $W_+$.
- **Expectation `EX3` (World Split Survives Theorem `90`):** In Theorem `90`'s exact channel weight $N_s^{\mathrm{T90}}$, the difference between $W_-$ and $W_+$ remains macroscopic (`|z| > 4` across the seven claimed outputs) and closely tracks the $W_- - W_+$ split under $2\pi L_2 + c_s$.
- **Expectation `EX4` (Exact Level-`5` `lepton == down` Under Theorem `90`):** Because $6 q_{\mathrm{lep}} \equiv -6 q_{\mathrm{down}}^{\mathrm{rev}} \pmod 5$ sends $c_s \mapsto -c_s \pmod 1$, negating $a_{0,s}$ while preserving $|a_{0,s}|^2$, the equality of `lepton` and `down` singular-value ratios at level `5` holds to machine precision ($< 10^{-14}$) under $N_s^{\mathrm{T90}}$ in both $W_-$ and $W_+$.
- **Planted Controls (`PC_EX_1`–`PC_EX_4`):**
  - `PC_EX_1`: Flipping $-\pi |a_{0,s}|^2 e^{-2 L_2} \mapsto +\pi |a_{0,s}|^2 e^{-2 L_2}$ reverses the sign of $\Delta_{\mathrm{T90}}$ across all shifted outputs.
  - `PC_EX_2`: Omitting the $\operatorname{Im}\tau$ modular factor in $e^{-2 L_2(\tau)} = \frac{\operatorname{Im}\tau}{\pi^2 e^{2\gamma_E}} e^{-2\tilde{L}_2(\tau)}$ breaks $S$-invariance by more than $10^{-2}$.
  - `PC_EX_3`: Replacing $L_2(\tau)$ by constant invariant ends shifts the claimed outputs by more than five standard errors.
  - `PC_EX_4`: Swapping $W_- \leftrightarrow W_+$ shifts the claimed outputs by more than four standard errors.

`0 of 19.`
