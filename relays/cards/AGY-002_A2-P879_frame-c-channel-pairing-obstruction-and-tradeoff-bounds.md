# agy-002 Pre-Run Expectations Card — Card A2-P879: Analytical & Global-Certifier Settlement of `P-879` on `Frame C` Channel Pairing

- **Seat:** `agy-002` (`branch: agy-002/verify`, appended directly onto `98bd560d9` without rebase)
- **Date:** `2026-11-20`
- **Card:** `A2-P879` (`settling origin/main register row P-879 from B1966–B1969, 0 of 19`)
- **Custody & Independence:**
  - Read from `origin/main` (`60a52d359`): `frontier/B1966_the_tradeoff_is_not_in_the_couplings_form/FINDINGS.md`, `frontier/B1967_the_tradeoff_is_not_in_the_couplings_form/FINDINGS.md`, `frontier/B1968_frame_cs_channels_never_reach_the_tuned_region_on_a_grid/FINDINGS.md`, `frontier/B1969_.../FINDINGS.md`, `frontier/B1945_the_frames_cusp_exponents/verification/determinant_law.py`, and `frontier/B1940_.../verification/frame_mp.py`.
  - Both producer (`relays/a2_p879/verify_a2_p879.py`) and cold-room referee (`relays/a2_p879_referee/referee_a2_p879.py`) must be **100% standalone** (`0` imports from `frontier/`), contain **`0` `float` or `complex` AST literals**, and enforce all six formal verification guardrails (`including random Haar unitary basis-scrambling invariance < 10^{-12} and zero literal boolean/zero flags`).
  - Empirical firewall: **`0 of 19`** (zero experimental or PDG inputs).

---

## 1. Self-Contained Mathematical Setup (`Frame C` Coupling & Channels)

1. **Quaternion Basis & Yukawa Operator:**
   Let $\varepsilon = Q_J = \begin{pmatrix}0&1\\-1&0\end{pmatrix}$, $Q_I = \begin{pmatrix}i&0\\0&-i\end{pmatrix}$, $Q_K = Q_I Q_J = \begin{pmatrix}0&i\\i&0\end{pmatrix}$, generation blocks $(C_0, C_1, C_2) = (Q_J, Q_I, Q_K)$, and dual channel basis $E_{\text{dual}} = \{E_1, E_i, E_j, E_k\}$ given by:
   $$E_1 = \frac{1}{2}\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad E_i = \frac{1}{2}\begin{pmatrix}0&i\\i&0\end{pmatrix},\quad E_j = \frac{1}{2}\begin{pmatrix}-1&0\\0&-1\end{pmatrix},\quad E_k = \frac{1}{2}\begin{pmatrix}-i&0\\0&i\end{pmatrix}.$$
   For a pure-triplet Higgs vector $h \in \mathbb{C}^3$ with $\|h\|_2 = 1$ and $S(h) = h_1 Q_I + h_0 Q_J + h_2 Q_K$, and any $2\times 2$ complex channel matrix $M_w = \sum_{s \in \{1,i,j,k\}} u_s E_s$, write
   $$m_0 = \frac{M_{w,00} + M_{w,11}}{2},\quad m_1 = \frac{M_{w,00} - M_{w,11}}{2i},\quad m_2 = \frac{M_{w,01} - M_{w,10}}{2},\quad m_3 = \frac{M_{w,01} + M_{w,10}}{2i},$$
   and set $(u, w) = \big(-2(m_0, -m_3, m_1),\, -2 m_2\big) \in \mathbb{C}^3 \times \mathbb{C}$. Then the spinor-block contraction $Y_{ab}^{\text{spin}}(S(h), M_w) = \operatorname{tr}\!\big((C_a^T \varepsilon S(h) C_b)^T M_w\big)$ coincides identically with
   $$Y(h; u, w) = u h^T + h u^T - (u\cdot h) I_3 + w [h]_\times,\qquad [h]_\times v := h \times v,$$
   and under the `B1966`/`B1968` single-doublet conjugate charge rule, **down** couples to $h_d = h$ via $Y_d = Y^{\text{spin}}(S(h), M_{w,d}) = Y(h; u_d, w_d)$ and **up** couples via $S_u = \varepsilon \overline{S(h)} \varepsilon^T = -\big(\bar{h}_1 Q_I + \bar{h}_0 Q_J + \bar{h}_2 Q_K\big)$, so $Y^{\text{spin}}(S_u, M_{w,u}) = -Y(\bar{h}; u_u, w_u)$ (whose overall minus sign leaves singular values and $|V_{\text{CKM}}|$ invariant).
   - *Convention check (`Guardrail 4`):* Check $|Y^{\text{spin}}(S(h), M_w) - Y(h; u, w)| < 10^{-13}$ and $|Y^{\text{spin}}(\varepsilon\overline{S(h)}\varepsilon^T, M_w) + Y(\bar{h}; u, w)| < 10^{-13}$ explicitly for random $(h, M_w)$ (an overall sign $-1$ shifts neither singular values nor left-unitary $|U_u^\dagger U_d|$). Singular values are ordered ascending $0 \le m_1 \le m_2 \le m_3$ (or descending $s_1 \ge s_2 \ge s_3$ where stated), with $V_{\text{CKM}} = U_u^\dagger U_d$ matching columns in matching sort order.

2. **`Frame C` Channel Construction at $(\tau, a, b)$:**
   - Sector left/right rational hypercharges: `up` has $(q_L, q_R) = (1, -4)$, `down` has $(q_L, q_R) = (1, 2)$.
   - Shifts for $(a, b) \in (\mathbb{Q}/\mathbb{Z})^2 \setminus \{(0,0)\}$: $x = (q_L a,\, 2 q_L b)$, $y_{\text{sh}} = (q_R a,\, 2 q_R b)$, $a_\pm = x_0 \pm y_{\text{sh},0}$, $b_\pm = \frac{x_1 \pm y_{\text{sh},1}}{2}$, $H = 1/2$, $e = e^{-2\pi i x_0}$, $\kappa = (1: -i e,\, i: -1,\, j: -e,\, k: i)$, and characteristics
     $$c_s = (a_+ + H,\, b_+ + H)_{1},\; (a_+ + H,\, b_+)_{i},\; (a_+,\, b_+ + H)_{j},\; (a_+,\, b_+)_{k},$$
     $$d_s = (a_- + H,\, b_- + H)_{1},\; (a_- + H,\, b_-)_{i},\; (a_-,\, b_- + H)_{j},\; (a_-,\, b_-)_{k}.$$
   - Unweighted theta residue ($R_s$): `0` if $(c_{s,0}-H, c_{s,1}-H) \in \mathbb{Z}^2$ OR $(d_{s,0}-H, d_{s,1}-H) \in \mathbb{Z}^2$ (exact odd spin-structure zero law), otherwise
     $$R_s(\tau) = \kappa_s \frac{\theta_c(c_{s,0}, c_{s,1}, 0, \tau)\,\theta_c(d_{s,0}, d_{s,1}, 0, \tau)}{2\pi\,\eta(\tau)^3}, \qquad \theta_c(\alpha,\beta,0,\tau) = \sum_{n\in\mathbb{Z}} e^{\pi i (n+\alpha)^2 \tau + 2\pi i (n+\alpha)\beta}.$$
   - Theorem `90` exact channel weight ($u_s = \sqrt{\max(0,\, N_s)}\, R_s$): with $\alpha_s = c_{s,0}-H$, $\beta_s = c_{s,1}-H$, and exact $\mathbb{Z}^2$-periodic reduced Kronecker constant term $a_{0,s} = 2\pi i \alpha_{s,r} + \theta_1'(\alpha_{s,r}\tau + \beta_{s,r})/\theta_1(\alpha_{s,r}\tau + \beta_{s,r})$ ($\alpha_{s,r} = \alpha_s \bmod 1$, $\beta_{s,r} = \beta_s \bmod 1$),
     $$N_s(\tau, L_2) = 2\pi L_2 + F_u(\alpha_{s,r}, \beta_{s,r}, \tau) + \pi\ln(\operatorname{Im}\tau) - 2\pi(\gamma_E + \ln\pi) - \pi |a_{0,s}|^2 e^{-2 L_2},$$
     where $F_u$ is the exact regularized periodic Green sum (`zero-row term` $+\operatorname{Im}\tau \cdot \pi^2/\sin^2(\pi\beta_{s,r})$ when $\alpha_{s,r} = 0$, digamma term when $\alpha_{s,r} \neq 0$, plus exponential Fourier sum), and $L_2(\tau)$ is the canonical length-`2` punctured-torus hyperbolic horocycle parameter solved directly via Gauss `SL_2(Z)` reduction to the fundamental domain (`with exact cusp seed \pi^2/12 in the Weierstrass ODE solver below Im tau = 12, and exact cusp formula \pi + \ln\pi - 3\ln 2 for Im tau >= 12`).

---

## 2. Pre-Registered Theorems & Verification Bars (`T1`–`T5`)

### `T1`: Exact Null-Basis $2\times 2$ Reduction & Algebraic Proof of `B1966 E4`
- For any unit null $h_0 \in \mathbb{C}^3$ ($h_0\cdot h_0 = 0, \|h_0\|_2 = 1$), $e_3 := -i(h_0 \times \bar{h}_0)$ is a real unit vector orthogonal to both $h_0$ and $\bar{h}_0$, so $B = [h_0, \bar{h}_0, e_3] \in \mathrm{U}(3)$.
- Expanding $u = \alpha h_0 + \beta \bar{h}_0 + \gamma e_3$ ($\alpha = u\cdot\bar{h}_0, \beta = u\cdot h_0, \gamma = u\cdot e_3$), the unitary change of basis $B^\dagger Y(h_0; u, w) B$ has identically zero first column and second row (`exact 1-dim right kernel h_0 and left kernel \bar{h}_0`), reducing to the active $2\times 2$ matrix (`rows [h_0, e_3], cols [\bar{h}_0, e_3]`):
  $$A = \begin{pmatrix} 2\alpha & \gamma + i w \\ \gamma - i w & -\beta \end{pmatrix}, \qquad \det A = -(2\alpha\beta + \gamma^2 + w^2) = -(w^2 + u\cdot u).$$
- **Bar:** Verify identically to `0` symbolically (`SymPy`) and to `< 10^{-12}` numerically across `12` random null $h_0$ and complex $(u, w)$ that $\det A + (w^2 + u\cdot u) = 0$ and $m_2 m_3 = \|h_0\|^2 |w^2 + u\cdot u|$ (`with rescaling ||h||^2` for non-unit null $h$).

### `T2`: Exact $4\times 4$ Kronecker Lift & Rank-`1` Wedin/Weyl Remainder Law
- On the orthonormal Hermitian-scaled basis $\frac{1}{\sqrt{2}}\{I_2, Q_J, Q_I, Q_K\}$ of $\mathbb{C}^{2\times 2}$, the extended bilinear map $\frac{1}{2}\widehat{Y}_{AB}(S(h), M_w) := \frac{1}{2}\operatorname{tr}\!\big((C_A^T H C_B)^T M_w\big)$ ($H = \varepsilon S(h)$) is unitarily equivalent to $H \otimes M_w$.
- Consequently, the singular values of $\frac{1}{2}\widehat{Y}$ are exactly the `4`-element multiset $\{\sigma_+\mu_1, \sigma_+\mu_2, \sigma_-\mu_1, \sigma_-\mu_2\}$, where $\sigma_\pm(r) = \frac{\sqrt{1+r} \pm \sqrt{1-r}}{\sqrt{2}}$ ($r = |h\cdot h| \in [0, 1]$) and $\mu_1 \ge \mu_2 \ge 0$ are the singular values of $M_w$.
- Restricting to the $3\times 3$ triplet block $\{Q_J, Q_I, Q_K\}$ writes $\frac{1}{2}Y_f = A_{f,0} + E_f$, where $H_f = \sigma_+ \xi_f \eta_f^T + \sigma_- \tilde{\xi}_f \tilde{\eta}_f^T$ and $M_{w,f} = \mu_{1,f} l_f r_f^T + \mu_{2,f} \tilde{l}_f \tilde{r}_f^T$ induce the rank-`1` leading term $A_{f,0} = \frac{1}{2}\sigma_+\mu_{1,f}\, v(l_f, \xi_f) v(r_f, \eta_f)^T$ with $\|v(l, \xi)\|_2^2 = 1 + |l^T \varepsilon \xi|^2 \in [1, 2]$ and remainder operator norm $\|E_f\|_2 \le \max(\sigma_+\mu_{2,f}, \sigma_-\mu_{1,f})$.
- **Bar:** Verify the `4`-singular-value Kronecker identity to `< 10^{-12}`, the norm bound $\| \frac{1}{2}Y_f - A_{f,0} \|_2 \le \max(\sigma_+\mu_{2,f}, \sigma_-\mu_{1,f})$ across `50` random $(h, M_w)$, and $\|v(l,\xi)\|_2^2 = 1 + |l^T\varepsilon\xi|^2$ to `< 10^{-12}`.

### `T3`: Exact Spinor Möbius Heavy-Alignment Theorem (`The Missing Channel-Pairing Law`)
- Under the conjugate charge rule at $r = |h\cdot h| = 0$ ($\xi_u = \varepsilon \xi_d^*$, up to phase), define the canonical left-spinor pairing invariant
  $$s_L := |l_u^T \varepsilon l_d| = \sqrt{1 - |\langle l_u \mid l_d \rangle|^2} \in [0, 1].$$
- **Theorem (`Sharp Closed-Form Bound`):** Optimizing $\frac{|\langle v(l_u, \varepsilon\xi^*) \mid v(l_d, \xi)\rangle|}{\|v(l_u, \varepsilon\xi^*)\|_2 \|v(l_d, \xi)\|_2}$ over all unit spinors $\xi \in \mathbb{C}^2$ yields the exact closed-form ceiling:
  $$\sup_{\|\xi\|_2 = 1} |V_{33}^{(0)}(\xi; l_u, l_d)| = \frac{1 + s_L}{3 - s_L},$$
  attained analytically at $\xi = (\cos t_*, -\sin t_*)$ in the $\mathrm{SU}(2)$ gauge $(l_d = e_1,\, l_u = \sqrt{1-s_L^2}\, e_1 + s_L\, e_2)$, where $\alpha = \arcsin(s_L)$ and $t_* = \frac{\pi}{4} - \frac{\alpha}{2}$.
- **Corollaries:**
  1. Heavy-generation alignment $|V_{33}^{(0)}| \ge 9/10$ requires $s_L \ge 17/19$ (since $\frac{1+s_L}{3-s_L} \ge \frac{9}{10} \iff 19 s_L \ge 17$).
  2. When the sectors share a left spinor ($s_L = 0$, $|\langle l_u \mid l_d \rangle| = 1$), $|V_{33}^{(0)}| \le 1/3$ identically for all $h_0$ and all right-handed spinors $(r_u, r_d)$.
  3. On `B1967`'s counterexample channels ($r = 3/1000$), verify $s_L > 17/19$ (`specifically s_L > 19/20`), whereas collinear channels force $|V_{33}| \le 1/3$.
- **Bar:** Prove analytically via SymPy (`show numerator/denominator polynomial identity and critical value at t_* = pi/4 - arcsin(s_L)/2`) AND verify over fine $2\text{D}$ `(t, phi)` spinor grids at $s_L \in \{0, 1/4, 1/2, 3/4, 17/19, 1\}$ to `< 10^{-8}` grid error (`exact equality at t_* to < 10^{-13}`).

### `T4`: Exact Structural Obstructions of `Frame C`'s Own Channels
- **`T4(a)` (`Order-5 Exact Zero Law`):** For every point $(a, b) \in (\frac{1}{5}\mathbb{Z}/\mathbb{Z})^2 \setminus \{(0,0)\}$ (`24` points) and `up` hypercharges $(q_L, q_R) = (1, -4)$, $(a_-, b_-) = (5a, 5b) \equiv (0, 0) \pmod 1$, so $d_1 = (a_- + 1/2, b_- + 1/2)$ hits the odd spin structure $(1/2, 1/2)$ everywhere, forcing $u_1 = 0$ and **$w_u = 0$ identically (`< 10^{-14}`)** across all `24` points and every $\tau \in \mathbb{H}$.
- **`T4(b)` (`Shared-Q_L Rank-1 Residue & Cusp s_L Decay Theorem`):** Because `up` $(1, -4)$ and `down` $(1, 2)$ share $q_L = 1$ (identical left twist $x = (a, 2b)$ and opposite summed twists modulo signs up to modular theta relations), verify across all `36` torsion test points (`all 24 of order 5 plus 12 representative points of orders 3, 4, 6, 7, 8`) at $\tau = 13/100 + 2 i$:
  1. Unweighted theta-residue matrices $M_{w,u}^{\text{res}}$ and $M_{w,d}^{\text{res}}$ each have exact rank `1` ($\mu_2^{\text{res}} / \mu_1^{\text{res}} < 10^{-13}$);
  2. Their left singular spinors coincide identically: $s_L^{\text{res}} = |(l_u^{\text{res}})^T \varepsilon l_d^{\text{res}}| < 10^{-13}$!
  3. Consequently, nonzero $s_L$ in `Frame C` arises *solely* from the logarithmic subleading splitting across the `4` Theorem `90` channel weights $\sqrt{N_s(\tau, L_2)}$, which decays as $\tau \to i\infty$. Verify explicitly at $x \in \{0, 1/4\}$ and $y \in \{1, 3, 6, 15, 30\}$ on order-`5` and order-`7` points that $\max s_L < 2/5 \ll 17/19$ (monotonically shrinking below `1/5` at $y = 6$ and below `1/8` at $y = 30$).

### `T5`: Deterministic Vectorized $\mathbb{C}\mathbb{P}^2$ Weyl + Davis–Kahan Global Certifier + Positive Control
- Since global complex phase $h \mapsto e^{i\phi} h$ leaves $m_k/m_3$ and $|V_{\text{CKM}}|$ invariant, cover $\mathbb{C}\mathbb{P}^2$ completely by `3` compact affine charts $C_k = \{v \in \mathbb{C}^3 : v_k = 1,\; \operatorname{Re}(v_j), \operatorname{Im}(v_j) \in [-1, 1] \text{ for } j \neq k\} \cong [-1, 1]^4$ (`k \in \{0, 1, 2\}`).
- On any $4\text{D}$ box $B(c, \text{hw}) \subset [-1, 1]^4$ (`center c, half-width hw`), let $h(x) = v(x)/\|v(x)\|_2$. Because $\|v(x)\|_2 \ge 1$ everywhere on $C_k$, the Jacobian derivative of $v \mapsto v/\|v\|_2$ has operator norm $\le 1/\|v(x)\|_2$, yielding the exact Mean-Value bound for every $x \in B(c, \text{hw})$:
  $$\Delta h_{\max}(c, \text{hw}) := \sup_{x \in B(c, \text{hw})} \|h(x) - h(c)\|_2 \le \frac{2\,\text{hw}}{\max\!\big(1,\, \|v(c)\|_2 - 2\,\text{hw}\big)}.$$
- Since $\|Y(dh; u_f, w_f)\|_2 \le 2\sqrt{2}\,\mu_{1,f}\,\|dh\|_2$ (exact from `T2`'s Kronecker lift since $\|S(dh)\|_2 = \|dh\|_2$ gives $\sigma_+ \le \sqrt{2}$ and factor `2`), set $\Delta_f = 2\sqrt{2}\,\mu_{1,f}\,\Delta h_{\max}$. By Weyl's singular-value inequality and Davis–Kahan on $Y_f Y_f^\dagger$:
  - Prune $B$ if $s_{2,u}(c) - \Delta_u > \frac{1}{100}\big(s_{1,u}(c) + \Delta_u\big)$ (`impossible to have m_2/m_3 <= 1/100 in up`), OR
  - Prune $B$ if $s_{2,d}(c) - \Delta_d > \frac{1}{100}\big(s_{1,d}(c) + \Delta_d\big)$ (`impossible to have m_2/m_3 <= 1/100 in down`), OR
  - When $s_{1,f}(c) - \Delta_f > s_{2,f}(c)$ in both sectors, set $\theta_f = \arcsin\!\Big(\min\!\Big(1,\, \frac{\Delta_f(2 s_{1,f}(c) + \Delta_f)}{(s_{1,f}(c) - \Delta_f)^2 - s_{2,f}(c)^2}\Big)\Big)$ and prune $B$ if $\arccos |V_{33}(c)| - \theta_u - \theta_d > \arccos(9/10)$ (`impossible to have |V_{33}| >= 9/10, a fortiori impossible to have min_k |V_{kk}| >= 9/10`).
- **Scope Certified Without Heuristic Search:**
  1. **Frame `C` Exclusion (`0` unpruned boxes at every grid point):** Certify all `24` order-`5` points + `12` representative points of orders `3, 4, 6, 7, 8` (`total 36 points`, e.g. `(1/3,1/3), (1/3,0), (1/4,1/2), (1/4,1/4), (1/6,1/6), (1/6,5/6), (3/7,1/7), (1/7,6/7), (2/7,3/7), (1/7,0), (1/8,3/8), (3/8,1/8)`) across columns $x \in \{0, 13/100, 1/4, 1/2\}$ and heights $y \in \{1, 3/2, 2, 3, 6, 15, 30\}$ (`at balanced sampling covering low/mid/cusp heights, >= 150 (tau, a, b) pairs including full 24-pt order-5 + 12-pt order-3..8 slices across y = 1, 3/2, 2, 6, 15, 30`), plus $L_2 \pm 1/50$ stability sensitivity test bracketing `B1927`'s table at $x = 13/100, y = 2$!
  2. **Mandatory Positive Control (`B1967`'s `16`-Rational Counterexample Channels):** Construct `(u_u, w_u), (u_d, w_d)` from these exact `16` rational pairs `(num, den)`:
     - `u_u`: `Re` = `(8112623/23657898, -32191861/58976063, 8361869/35299624)`, `Im` = `(29517392/42170071, 10109002/39589433, 201121/6549724)`;
     - `w_u`: `32621059/80596130 + i(-2122066/7900781)`;
     - `u_d`: `Re` = `(8253345/14846974, 13917810/48354631, 29492199/87199192)`, `Im` = `(32273371/84797632, -69799368/69016585, -23893336/16802917)`;
     - `w_d`: `126906246/75918835 + i(16923861/50797165)`.
     Assert BOTH that evaluating at $h(3/1000) = (\cos t, i\sin t, 0)$ ($\cos 2t = 3/1000$) satisfies `min_k |V_{kk}| >= 9/10`, `both m_2/m_3 <= 1/100`, `both m_1/m_2 <= 1/2`, AND that running the **exact same** `CP^2` certifier on these channels does **not** prune away the box containing $h(3/1000)$ (`proving zero over-pruning!`).

---

## 3. Mandatory Formal-Verification Guardrails & `5` Planted Faults (`PF1`–`PF5`)

- **Haar Basis-Scrambling Test (`Guardrail 3`):** Apply `10` independent random Haar $\mathrm{U}(3)$ basis transformations $(U_L, U_{R,u}, U_{R,d})$ to $(Y_u, Y_d)$ (`Y_f -> U_L Y_f U_{R,f}^\dagger`) across both `Frame C` points and the `B1967` positive control, verifying that all singular-value ratios $m_k/m_3$, $|V_{\text{CKM}}|$, and the certifier's pruning metrics remain invariant to `< 10^{-12}`.
- **`5` Planted Faults (`ALL 5 must be caught by automated assertions`):**
  - `PF1`: Replace the Möbius heavy-alignment bound $\frac{1+s_L}{3-s_L}$ with an inflated bound `1/2` at $s_L = 0$ -> caught (`true max at s_L = 0 is 1/3 < 1/2`).
  - `PF2`: Switch `up` sector from conjugate reading $\bar{h}$ to same reading $h$ in `Frame C` -> caught (`alignment + hierarchy becomes artificially easy when both sectors read h, failing the conjugate-rule test`).
  - `PF3`: Corrupt the Weyl Lipschitz constant in the `CP^2` certifier downward by factor `1/10` and run it on the `B1967` `16`-rational positive control -> caught (`over-prunes the genuine counterexample box!`).
  - `PF4`: Corrupt `up` right hypercharge from `-4` to `+2` (`making up == down`) -> caught (`breaks B1968 channel matrix reproduction & order-5 w_u = 0 zero law`).
  - `PF5`: Apply *unequal* left-handed unitary scrambling $U_{L,u} \neq U_{L,d}$ and claim $|V_{\text{CKM}}|$ invariance -> caught (`|V_{CKM}| drifts by > 1/10, caught by Haar Guardrail 3 check`).

0 of 19.
