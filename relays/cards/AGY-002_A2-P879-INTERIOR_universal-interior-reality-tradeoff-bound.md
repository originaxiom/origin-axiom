# Scope Card `A2-P879-INTERIOR` — Exact Universal Interior ($0 \le r \le 1$) One-Doublet Trade-Off Bound (`M58` / `P-879`; `0 of 19`)

- **Seat:** `agy-002` (branch `agy-002/verify`)
- **Date:** `2026-11-24`
- **Responds to:** `main` `B1973` (`4418092a3`) and seat message **`M58`** (*"The interior $0 < r < 1$ stays open on main. A bound that holds for every $r$ is the natural next card, if you want it."*), closing register row **`P-879`** (`B1965`–`B1969`, `B1727`, `B1973`) analytically across the entire Higgs reality interval $r = |h \cdot h| / \|h\|^2 \in [0, 1]$ without grid search or box subdivision over $h \in \mathbb{CP}^2$.
- **Empirical Firewall:** **Strictly `0 of 19`.** Zero empirical inputs (no PDG, NuFIT, Planck, DESI, or CODATA values), zero Python `float` or `complex` AST literals, zero binary64 casts, zero JSON float tokens, zero `frontier/` imports, zero edits outside `relays/`.

---

## 1. Setup and Exact Conventions

Let $h \in \mathbb{C}^3 \setminus \{0\}$ be a pure triplet Higgs with unit-normalized reality parameter and Möbius-ratio parameter
$$r \;\equiv\; \frac{|h \cdot h|}{\|h\|^2} \in [0, 1], \qquad t \;\equiv\; \frac{r}{1 + \sqrt{1 - r^2}} \in [0, 1], \qquad r = \frac{2t}{1 + t^2}.$$
Here $a \cdot b = \sum_{j=1}^3 a_j b_j$ is the bilinear (unconjugated) dot product and $\|h\|^2 = \sum_{j=1}^3 |h_j|^2$.
For any channel $(u, w) \in \mathbb{C}^3 \times \mathbb{C}$, `B1736`'s pure-triplet Yukawa matrix is
$$Y(h; u, w) \;=\; u h^T + h u^T - (u \cdot h) I_3 + w [h]_\times, \qquad ([h]_\times x)_a = \sum_{j,k=1}^3 \varepsilon_{ajk} h_j x_k.$$
Under the one-doublet conjugate charge rule (`B1965`–`B1973`), down reads $h$ with channels $(u_d, w_d)$ and up reads $\bar{h}$ with channels $(u_u, w_u)$:
$$Y_d = Y(h; u_d, w_d), \qquad Y_u = Y(\bar{h}; u_u, w_u).$$
Let $m_3^{(f)} \ge m_2^{(f)} \ge m_1^{(f)} \ge 0$ be the singular values of $Y_f$ ($f \in \{u, d\}$), $u_{3,f} \in \mathbb{C}^3$ be the unit top left singular vector (unique up to phase whenever $m_3^{(f)} > m_2^{(f)}$), and $|V_{33}| = |\langle u_{3,u} | u_{3,d}\rangle|$ be the heavy-generation CKM magnitude (with $\min_i |V_{ii}| \le |V_{33}|$). Define $\rho_f \equiv m_2^{(f)} / m_3^{(f)}$ and $\rho \equiv \max(\rho_u, \rho_d)$.

Define the $2 \times 2$ matrices
$$H(h) \equiv \sum_{j=1}^3 h_j \sigma_j \in \mathfrak{sl}_2(\mathbb{C}), \qquad M(u, w) \equiv -i w I_2 + \sum_{j=1}^3 u_j \sigma_j \in M_2(\mathbb{C}),$$
where $\sigma_1 = \bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$, $\sigma_2 = \bigl(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\bigr)$, $\sigma_3 = \bigl(\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\bigr)$.
The singular values of $H(h)$ are $\sigma_1(H) = \|h\|\sqrt{1 + \sqrt{1 - r^2}}$ and $\sigma_2(H) = \|h\|\sqrt{1 - \sqrt{1 - r^2}}$, so $\sigma_2(H)/\sigma_1(H) = t$.
Let $\mu_1(M) \ge \mu_2(M) \ge 0$ be the singular values of $M(u, w)$ and $\kappa(M) \equiv \mu_2(M)/\mu_1(M) \in [0, 1]$.

In `Frame C` (`B1945` / `B1973`), the $2 \times 2$ channel matrix is $M_w = \sum_{s \in \{1, i, j, k\}} u_s E_s^{\text{dual}}$ with
$$E_1^{\text{dual}} = \frac{1}{2}\begin{pmatrix}1&0\\0&1\end{pmatrix}, \quad E_i^{\text{dual}} = \frac{1}{2}\begin{pmatrix}-i&0\\0&i\end{pmatrix}, \quad E_j^{\text{dual}} = \frac{1}{2}\begin{pmatrix}0&1\\-1&0\end{pmatrix}, \quad E_k^{\text{dual}} = \frac{1}{2}\begin{pmatrix}0&-i\\-i&0\end{pmatrix},$$
and $(u, w)$ extracted via `m_0 = (M_w[0,0]+M_w[1,1])/2`, `m_1 = (M_w[0,0]-M_w[1,1])/(2i)`, `m_2 = (M_w[0,1]-M_w[1,0])/2`, `m_3 = (M_w[0,1]+M_w[1,0])/(2i)`, $u = -2(m_0, -m_3, m_1)^T$, $w = -2 m_2$.

---

## 2. Theorems to Verify and Certify (`M1`–`M4`)

### `M1` — Exact $4 \times 4$ Kronecker Compression, Unitary Frame Equivalence, and Bell-State Constant Projection
1. **Exact Kronecker Identity:** For all $(h, u, w) \in \mathbb{C}^7$,
   $$Y(h; u, w)_{ab} \;=\; \frac{1}{2}\operatorname{Tr}\!\bigl(\sigma_a\, H(h)\, \sigma_b\, M(u, w)\bigr) \qquad (a, b \in \{1, 2, 3\}).$$
   On the 4D Hilbert space $M_2(\mathbb{C})$ with inner product $\langle A, B\rangle = \frac{1}{2}\operatorname{Tr}(A^\dagger B)$ and orthonormal basis $\{e_0 = I_2,\; e_1 = \sigma_1,\; e_2 = \sigma_2,\; e_3 = \sigma_3\}$, the linear map $\mathcal{T}(H, M): X \mapsto H X M$ is unitarily equivalent to $H \otimes M^T$ with exact singular values $\sigma_1(H)\mu_1(M)\cdot(1,\; \max(t,\kappa),\; \min(t,\kappa),\; t\kappa)$, and $Y(h; u, w) = P_{\mathfrak{sl}_2} \mathcal{T}(H, M) P_{\mathfrak{sl}_2}$ where $P_{\mathfrak{sl}_2} = I_4 - e_0 e_0^\dagger$.
2. **Exact Unitary Equivalence with `Frame C`'s $M_w$:**
   $$M(u, w) \;=\; 2\, L_u\, M_w^T\, R_u, \qquad L_u = \begin{pmatrix}1&0\\0&i\end{pmatrix} H_2, \quad R_u = H_2 \begin{pmatrix}0&-1\\i&0\end{pmatrix}, \quad H_2 = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix},$$
   with $L_u^\dagger L_u = R_u^\dagger R_u = I_2$. Hence $\kappa(M) = \kappa(M_w)$ identically, and the dominant right singular vector $\rho_1(M)$ is $R_u^\dagger \overline{\ell_1(M_w)}$, so the dominant spinor-pairing invariant satisfies
   $$s_L \;\equiv\; \sqrt{1 - |\langle \rho_{1,u} \mid \rho_{1,d}\rangle|^2} \;=\; \sqrt{1 - |\langle \ell_{1,u}(M_w) \mid \ell_{1,d}(M_w)\rangle|^2}$$
   identically (matching `B1973` `t4b_check.py`).
3. **Bell-State Constant Projection Lemma:** Under $M_2(\mathbb{C}) \cong \mathbb{C}^2 \otimes \mathbb{C}^2$, the removed vector $e_0 = I_2$ is maximally entangled ($\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$). Therefore every product singular vector $u_j = \alpha \otimes \beta$ obeys $|\langle e_0 | u_j\rangle|^2 = \frac{1}{2}|\alpha^T \beta|^2 \le \frac{1}{2}$, and every factor-sharing 2D singular subspace $U_{12} = \operatorname{span}\{u_1, u_2\}$ (and $V_{12} = \operatorname{span}\{v_1, v_2\}$) satisfies the exact constant identity
   $$\|\Pi_{U_{12}} e_0\|^2 \;=\; \|\Pi_{V_{12}} e_0\|^2 \;=\; \frac{1}{2}.$$

### `M2` — Exact, Sharp Two-Variable Heavy-Pair Floor & Universal Interior Generalization of `B1727`
Let $\widehat{Y} \equiv Y(h; M) / (\sigma_1(H)\mu_1(M))$ with singular values $\hat{m}_3 \ge \hat{m}_2 \ge \hat{m}_1 \ge 0$.
1. **Sharp $(t, \kappa)$ Floor:** For every $h \in \mathbb{C}^3 \setminus \{0\}$ ($t \in [0, 1]$) and every $M \in M_2(\mathbb{C}) \setminus \{0\}$ ($\kappa \in [0, 1]$):
   $$\hat{m}_2(\widehat{Y}) \;\ge\; \max\!\left(t \kappa,\;\; \frac{|t - \kappa|}{2}\right), \qquad \frac{m_2(Y)}{m_3(Y)} \;\ge\; \max\!\left(t \kappa,\;\; \frac{|t - \kappa|}{2}\right).$$
   - Proof sketch (6 lines): $\hat{m}_2 \ge \Sigma_4(\widehat{\mathcal{T}}) = t\kappa$ by Thompson's interlacing for a $(4-1)\times(4-1)$ compression; by $t \leftrightarrow \kappa$ symmetry assume $t \ge \kappa$, split $\widehat{\mathcal{T}} = T_{12} + T_{34}$, restrict to the 2D subspaces $W = \operatorname{span}\{w_1, z_2\} \subset \mathfrak{sl}_2$ and $W' = \operatorname{span}\{u_1', \tilde{z}_2\} \subset \mathfrak{sl}_2$ built from $e_0 = \frac{1}{\sqrt{2}}(w_2 + w_2')$, giving $\sigma_2(\Pi_{W'} T_{12} \Pi_W) \ge t/2$ and $\|\Pi_{W'} T_{34} \Pi_W\|_2 \le \kappa/2$, so $\hat{m}_2 \ge \sigma_2(\Pi_{W'} \widehat{Y} \Pi_W) \ge (t - \kappa)/2$; finally $\hat{m}_3 \le \Sigma_1(\widehat{\mathcal{T}}) = 1$.
2. **Sharp Universal Reality Floor (Eliminating $\kappa$):** Minimizing over $\kappa \in [0, 1]$ at $\kappa_* = t/(1 + 2t)$ gives, for every $r \in [0, 1]$ and every channel $(u, w) \in \mathbb{C}^4 \setminus \{0\}$:
   $$\frac{m_2\bigl(Y(h; u, w)\bigr)}{m_3\bigl(Y(h; u, w)\bigr)} \;\ge\; \frac{t^2}{1 + 2t}, \qquad t = \frac{r}{1 + \sqrt{1 - r^2}}.$$
   - Recovers `B1727` + `B1966` `E3` ($1/3$) at $r = 1$ ($t = 1$), $\kappa/2$ at $r = 0$, and $t/2$ at $\kappa = 0$ (rank-1 channel).
3. **Exact Sharpness Witness for Every $(t, \kappa) \in [0, 1]^2$:** In the canonical null triad $B = [e_+, e_-, e_3]$ with $h = c_+ e_- + c_- e_+$ ($c_-/c_+ = t$), the channel $a = b = 0, x = 1, y = -\kappa$ ($u = e_- - \kappa e_+, w = 0$) yields $B^\dagger Y B / c_+ = \bigl(\begin{smallmatrix}0&-2t\kappa&0\\2&0&0\\0&0&-(t-\kappa)\end{smallmatrix}\bigr)$ with exact singular values $(2,\; \max(2t\kappa, |t-\kappa|),\; \min(2t\kappa, |t-\kappa|))$, attaining equality $\frac{m_2}{m_3} = \max(t\kappa, \frac{|t-\kappa|}{2})$ everywhere on $[0, 1]^2$ and $\frac{t^2}{1+2t}$ at $\kappa = \frac{t}{1+2t}$.
4. **Symmetric Bottleneck Corollary:** With $M_{\max} \equiv \max(t, \kappa)$,
   $$\hat{m}_2(\widehat{Y}) \;\ge\; \frac{M_{\max}^2}{1 + 2 M_{\max}}, \qquad \hat{m}_3(\widehat{Y}) \;\ge\; \frac{M_{\max}^2}{\rho (1 + 2 M_{\max})}, \qquad M_{\max} \;\le\; \rho + \sqrt{\rho^2 + \rho}.$$

### `M3` — Exact Single-Sector Heavy-State Perturbation & Complete Interior ($0 \le r \le 1$) Trade-Off Theorem
1. **Automatic Non-Degeneracy for $\rho < 1/6$:** By `M2`, $\rho < 1/6 \implies \max(t, \kappa) < (1 + \sqrt{7})/6 < 1$ and $\hat{m}_3 > 6 \hat{m}_2$, so $\alpha_1(H)$, $\rho_1(M)$, $u_3(Y)$, and $\hat{v} \equiv P_{\mathfrak{sl}_2}(\alpha_1 \rho_1^\dagger) / \|P_{\mathfrak{sl}_2}(\alpha_1 \rho_1^\dagger)\|$ are all strictly unique up to phase.
2. **Exact Single-Sector Perturbation Bound:** Writing $\widehat{Y} = A_0 + E$ with rank-1 $A_0 = (P_{\mathfrak{sl}_2} u_1)(P_{\mathfrak{sl}_2} v_1)^\dagger$ ($\|A_0\|_2 \in [1/2, 1]$ by `M1`) and $\|E\|_2 \le M_{\max} = \max(t, \kappa)$, $P_{\hat{v}^\perp} A_0 = 0$ yields $\sin\theta(u_3, \hat{v}) \le M_{\max} / \hat{m}_3$. Combining $\hat{m}_3 \ge \max(\frac{1}{2} - M_{\max},\; \frac{M_{\max}^2}{\rho(1 + 2 M_{\max})})$ over $M_{\max} \in [t, 1]$ gives the unique crossing $M_*(\rho) = \sqrt{\frac{\rho}{2(1 + 2\rho)}}$ and the exact closed-form bound
   $$\sin\theta\bigl(u_3(Y),\; \hat{v}\bigr) \;\le\; S_t(\rho) \;\equiv\; \begin{cases} \sqrt{2\rho(1 + 2\rho)} + 2\rho & \text{if } t \le \sqrt{\dfrac{\rho}{2(1 + 2\rho)}}, \\[8pt] \dfrac{\rho(1 + 2t)}{t} & \text{if } t > \sqrt{\dfrac{\rho}{2(1 + 2\rho)}}, \end{cases}$$
   with uniform ceiling $S(\rho) = \sqrt{2\rho(1 + 2\rho)} + 2\rho < 1$ for all $\rho < 1/6$, and exact inverse $\rho(S) = \frac{S^2}{2(1 + 2S)}$.
3. **Master Two-Sector Interior Trade-Off Theorem (Every $r \in [0, 1]$, Every Channel Pair $(M_u, M_d)$):**
   For every $r \in [0, 1)$, under $h \mapsto \bar{h}$ the top left singular vectors of $H(h)$ and $H(\bar{h})$ are $\xi$ and $\varepsilon \bar{\xi}$ (for the same unit spinor $\xi$), so by `B1973` / `A2-P879` `T3`, $|\langle \hat{v}_u | \hat{v}_d\rangle| \le \frac{1 + s_L}{3 - s_L}$. By the spherical triangle inequality on $\mathbb{CP}^2$, if $\rho = \max(\rho_u, \rho_d) < 1/6$:
   $$|V_{33}| \;\le\; \cos\!\left(\max\!\left(0,\;\; \arccos\!\left(\frac{1 + s_L}{3 - s_L}\right) \;-\; 2\arcsin\min\!\bigl(1,\; S_t(\rho)\bigr)\right)\right).$$
   Equivalently, for **every** $r \in [0, 1]$ ($t = \frac{r}{1 + \sqrt{1 - r^2}}$) and **every** channel pair $(M_u, M_d)$ with pairing $s_L$, requiring $|V_{33}| \ge a$ forces the continuous, monotonic three-regime floor
   $$\max\!\left(\frac{m_2^{(u)}}{m_3^{(u)}},\; \frac{m_2^{(d)}}{m_3^{(d)}}\right) \;\ge\; F(t;\; s_L, a) \;\equiv\; \begin{cases}
   \dfrac{S_{\text{req}}^2}{2(1 + 2 S_{\text{req}})} & \text{if } 0 \le t \le \dfrac{S_{\text{req}}}{2(1 + S_{\text{req}})}, \\[10pt]
   \dfrac{S_{\text{req}}\, t}{1 + 2t} & \text{if } \dfrac{S_{\text{req}}}{2(1 + S_{\text{req}})} \le t \le S_{\text{req}}, \\[10pt]
   \dfrac{t^2}{1 + 2t} & \text{if } S_{\text{req}} \le t \le 1,
   \end{cases}$$
   where $S_{\text{req}}(s_L, a) \equiv \sin\!\left(\frac{1}{2}\max\!\left(0,\; \arccos\!\frac{1+s_L}{3-s_L} - \arccos a\right)\right)$.
   - At $a = 9/10$ and $\rho = 1/100$, alignment requires the universal critical pairing $s_L \ge s_L^{\text{crit}}(9/10, 1/100) \approx 0.6596$ (exceeded by `B1967`'s witness $s_L \approx 0.976$ and `C1-A`'s witness $s_L = 1$, both verified inside the bound!).

### `M4` — Zero-Grid Analytic Certification of `Frame C` Across ALL $r \in [0, 1]$ (`B1973` 30-Point & `B1968` Full 2,016-Point Grids)
1. Recompute `Frame C`'s exact $M_w$ (standalone `mpmath` `L_2` Gauss–Legendre + theta series + cached `F_u`, zero `frontier/` imports) on:
   - **Benchmark A (`B1973` 30 points):** All `24` order-5 points + `6` mixed-order points `(1/7,3/7), (2/7,1/7), (1/3,1/3), (1/4,3/4), (1/6,1/6), (3/8,1/8)` at $x = 13/100$, $y \in \{2, 6\}$ (`60` pairs, `dps = 35`). Verify $\max s_L^{\text{res}} < 10^{-25}$ (unweighted) and weighted $\max s_L \le 39/100$.
   - **Benchmark B (`B1968` full 2,016-point grid):** All `24` order-5 + `48` order-7 points across all `4` columns $x \in \{0, 13/100, 1/4, 1/2\}$ and all `7` heights $y \in \{1, 3/2, 2, 3, 4, 6, 10\}$ (`2,016` points, `dps = 25`).
2. Apply `M3` directly to every point to certify **without any grid search or box subdivision over $h \in \mathbb{CP}^2$** that for **every** $h \in \mathbb{C}^3 \setminus \{0\}$ ($0 \le r \le 1$):
   - $\max s_L < 39/100 < 65/100 < s_L^{\text{crit}}(9/10, 1/100)$;
   - $|V_{33}| \ge 9/10 \implies \max(m_2^{(u)}/m_3^{(u)}, m_2^{(d)}/m_3^{(d)}) \ge F(t; s_L, 9/10) \ge 24/1000 > 1/100$;
   - $\max(m_2^{(u)}/m_3^{(u)}, m_2^{(d)}/m_3^{(d)}) \le 1/100 \implies |V_{33}| \le 78/100 < 9/10$.
3. Verify positive controls `B1973` `C1-A` (`r = 1/2000`, $s_L = 1$) and `B1967` (`r = 3/1000`, $s_L > 9/10$) satisfy all inequalities of `M2` and `M3` with zero contradiction.

---

## 3. Pre-Registered Falsification Gates (`G1`–`G7`) & Planted Faults (`PF1`–`PF6`)

| Gate | Requirement | Kill / Fail Criterion |
| :--- | :--- | :--- |
| `G0` | AST / Custody / Firewall | Any `float`/`complex` AST literal, `float(`/`complex(` call, `frontier/` import, or JSON float token fails. |
| `G1` (`M1`) | Exact SymPy Kronecker, $M = 2 L_u M_w^T R_u$, unitarity, Bell constant $1/2$ | Any nonzero symbolic residual or numeric error $> 10^{-30}$ fails. |
| `G2` (`M2`) | SymPy algebraic identities + `2,000` random `(r, M)` trials + `11` witness checks (`dps = 50`) | Any violation of $\hat{m}_2 \ge \max(t\kappa, |t-\kappa|/2)$ or $\rho \ge t^2/(1+2t)$ beyond $10^{-25}$, or witness discrepancy $> 10^{-45}$, fails. |
| `G3` (`M3`) | `2,000` random two-sector trials across $r \in [0, 1)$ + `3` boundary regimes (`C1-A`, `B1967`, `r = 1`) | Any violation of $\sin\theta(u_3, \hat{v}) \le S_t(\rho)$, $|V_{33}| \le \text{bound}$, or $\rho \ge F(t; s_L, a)$ beyond $10^{-25}$ fails. |
| `G4` (`M4-A`) | `B1973` `30`-point $\times$ `2`-height benchmark (`60` pairs, `dps = 35`) | Unweighted $s_L^{\text{res}} > 10^{-25}$ or $\mu_2^{\text{res}}/\mu_1^{\text{res}} > 10^{-25}$, or weighted $\max s_L \ge 39/100$, or `|V33|` ceiling at $\rho=1/100$ $\ge 78/100$, or $\rho$ floor at $a=9/10$ $\le 24/1000$, fails. |
| `G5` (`M4-B`) | `B1968` full `2,016`-point grid (`dps = 25`) | Any point with $s_L \ge 39/100$ (or `|V33|` ceiling $\ge 78/100$, or $\rho$ floor $\le 24/1000$) fails. |
| `G6` (`Guardrail 3`) | `10` random Haar $\mathrm{U}(3)_Q \times \mathrm{U}(3)_u \times \mathrm{U}(3)_d$ basis scramblings (`dps = 35`) | Any drift $> 10^{-30}$ in singular values, $\rho_f$, or $|V_{ij}|$ fails. |
| `G7` (`PF1`–`PF6`) | `6` planted faults must all be caught cleanly | Any undetected planted fault fails: `PF1` corrupting $M$ sign ($+iw$ vs $-iw$ breaks `M1`), `PF2` using wrong floor $t/2$ at $\kappa = t/(1+2t)$ violates witness, `PF3` swapping $q_L$ between up/down breaks `M4` residue $s_L^{\text{res}} = 0$, `PF4` dropping `2` in $2\arcsin S_t$ fails two-sector test / witness check, `PF5` breaking shared $U_Q$ in Haar scrambling (`U_{Q,u} != U_{Q,d}`) fails `Guardrail 3`, `PF6` dropping conjugate $\bar{h} \to h$ allows aligned rank-1 $s_L=0$ counterexample ($|V_{33}| = 1 > 1/3$). |

0 of 19.
