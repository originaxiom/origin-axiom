# Card A2-M51 (`M51` Follow-Up): Short Term-by-Term Proof of `P-873 Q3`'s Exact Cusp-Mixing Limit and `80`-Digit Resolution of `P-871`'s `c = +-2` Plain-Sum Observation

- **Seat:** `agy-002` (`branch: agy-002/verify`, appended onto `55f72ee3f` without rebase, read at `main`'s `f1efc59dd`)
- **Custody:** Expectations card at `ac8392b59` (`relays/cards/AGY-002_A2-M51_p873-q3-exact-limit-proof-and-p871-c2-precision-masking.md`); zero-float-literal script and `SCRIPT_SHA256.txt` at `19ca41b14` (`relays/a2_m51/verify_a2_m51.py`); raw outputs and `OUTPUT_SHA256.txt` at `5f857aa6b` (`relays/a2_m51/verify_a2_m51_out.json`, `relays/a2_m51/verify_a2_m51_out.txt`). Zero other-seat code opened or run; `0 of 19`.

---

## 1. Short Term-by-Term Proof of `P-873 Q3`'s Exact Limit (`Answering M51`, `docs/seats/agy-002.md:39-40`)

With $A = 1/\sqrt{2}$, $B = e^{i\pi/12}/2$, $p = e^{i\pi/3}$, and $\Theta_c(\tau, \xi) = \exp(6\pi i \xi \operatorname{Im}\xi / y)\,\vartheta[c/6, 0](6\xi, 6\tau)$ ($y = \operatorname{Im}\tau > 0$), omitting the positive scalar $(3 y)^{1/4}$ gives the contracted matrix at $h_* = (A, B, 0, 0, 0, B)$:
$$M(h_*) = \begin{pmatrix} p B \Theta_0 & p^{-1} B \Theta_2 & A \Theta_1 \\ p^{-1} B \Theta_4 & A \Theta_3 & p B \Theta_2 \\ A \Theta_5 & p B \Theta_4 & p^{-1} B \Theta_0 \end{pmatrix}.$$

1. **Exact index-reflection identity in `up` at the mark `(2/5, 4/5)` (holds at every $\tau \in \mathbb{H}$):**
   At $(a, b) = (2/5, 4/5)$ (unshifted lift), $\xi_{\text{up}} = \frac{5}{2}(\frac{2}{5}\tau + \frac{4}{5}) = \tau + 2$, so $6\xi_{\text{up}} = 6\tau + 12$ and $\operatorname{Im}\xi_{\text{up}} / y = 1$. For every $n, c \in \mathbb{Z}$,
   $$6\pi i(n + c/6)^2\tau + 2\pi i(n + c/6)(6\tau + 12) = 6\pi i(n + 1 + c/6)^2\tau - 6\pi i\tau + 24\pi i n + 4\pi i c,$$
   and $\exp(6\pi i(\tau + 2) - 6\pi i\tau) = \exp(12\pi i) = 1$, hence $\Theta_c(\tau, \tau + 2) = \vartheta[c/6, 0](0, 6\tau)$ identically on $\mathbb{H}$. Re-indexing $m \mapsto -m - 1$ in $\sum_{m \in \mathbb{Z}} \exp(6\pi i(m + c/6)^2\tau)$ yields $\Theta_{6 - c}(\tau) = \Theta_c(\tau)$ identically for all $\tau \in \mathbb{H}$, and in particular $\Theta_5 = \Theta_1$ and $\Theta_4 = \Theta_2$.

2. **Exact finite-$\tau$ reflection symmetry of $G_u(\tau) = M_{\text{up}}(h_*) M_{\text{up}}(h_*)^\dagger$ and exact eigenvector $u_-$:**
   Substituting $\Theta_5 = \Theta_1$ and $\Theta_4 = \Theta_2$ into $G_u = M_{\text{up}}(h_*) M_{\text{up}}(h_*)^\dagger$ gives three exact polynomial identities valid for all $\tau \in \mathbb{H}$ (using $p^3 = -1$, so $p^{-2} = -p$ and $p^2 = -p^{-1}$):
   $$(G_u)_{0,0} - (G_u)_{2,2} = 0, \qquad (G_u)_{0,1} = -e^{i\pi/3} (G_u)_{2,1}, \qquad (G_u)_{0,2} = e^{i\pi/3}\!\left[\frac{1}{\sqrt{2}}\operatorname{Re}\!\big(e^{i\pi/12}\Theta_0\overline{\Theta_1}\big) - \frac{1}{4}|\Theta_2|^2\right].$$
   Therefore $G_u(\tau)$ commutes **identically at every finite $\tau \in \mathbb{H}$** ($[R_*, G_u(\tau)] = 0$) with the Hermitian unitary involution
   $$R_* = \begin{pmatrix} 0 & 0 & -e^{i\pi/3} \\ 0 & 1 & 0 \\ -e^{-i\pi/3} & 0 & 0 \end{pmatrix} \qquad (R_*^\dagger = R_*,\; R_*^2 = I_3).$$
   Because $\ker(R_* + I_3)$ is `1`-dimensional (`since R_* e_1 = +e_1`), the unit vector $u_- = \frac{1}{\sqrt{2}}(1,\, 0,\, e^{-i\pi/3})^T$ is an **exact eigenvector of $G_u(\tau)$ at every $\tau \in \mathbb{H}$** with exact eigenvalue
   $$\lambda_-(\tau) = \left|\frac{1}{2}\Theta_0(\tau) + \frac{e^{-i\pi/12}}{\sqrt{2}}\Theta_1(\tau)\right|^2.$$

3. **Non-degenerate $2\times 2$ block on $\ker(R_* - I_3) = \operatorname{span}(u_+, e_1)$ (`for every Re(tau) in R`):**
   With $u_+ = \frac{1}{\sqrt{2}}(1,\, 0,\, -e^{-i\pi/3})^T$, the restriction $B_+(\tau)$ of $G_u(\tau)$ to the orthonormal basis $(u_+, e_1)$ is
   $$B_+(\tau) = \begin{pmatrix} \big|\frac{1}{2}\Theta_0 - \frac{e^{-i\pi/12}}{\sqrt{2}}\Theta_1\big|^2 + \frac{1}{2}|\Theta_2|^2 & u_+^\dagger G_u e_1 \\ e_1^\dagger G_u u_+ & \frac{1}{2}|\Theta_2|^2 + \frac{1}{2}|\Theta_3|^2 \end{pmatrix}.$$
   As $y \to +\infty$ at any fixed $\operatorname{Re}\tau \in \mathbb{R}$, $\Theta_0 \to 1$, $|\Theta_1| \sim e^{-\pi y / 6}$, $|\Theta_2| \sim e^{-2\pi y / 3}$, and $|\Theta_3| \sim e^{-3\pi y / 2}$, so $(B_+)_{0,0} \to 1/4$, $(B_+)_{1,1} = O(e^{-4\pi y / 3})$, and $|(B_+)_{0,1}| = O(e^{-2\pi y / 3})$. Across the $O(1)$ eigenvalue gap $1/4$, the two unit eigenvectors of $B_+(\tau)$ converge to $u_+ + O(e^{-2\pi y / 3}) e_1$ (`eigenvalue -> 1/4`) and $e_1 + O(e^{-2\pi y / 3}) u_+$ (`eigenvalue ~ O(e^{-4 pi y / 3})`). Moreover, $\lambda_-(\tau)$ and the top eigenvalue $\lambda_+(\tau)$ of $B_+(\tau)$ never stay equal at large $y$: if $\cos(\frac{\pi(1 - 2\operatorname{Re}\tau)}{12}) \neq 0$ (`including Re(tau) = 13/100`), $|\lambda_- - \lambda_+| \asymp \sqrt{2}|\cos(\frac{\pi(1 - 2\operatorname{Re}\tau)}{12})| e^{-\pi y / 6}$, while on the lines $\cos(\frac{\pi(1 - 2\operatorname{Re}\tau)}{12}) = 0$ (`Re(tau) == -5/2 mod 3`), $\lambda_+(\tau) - \lambda_-(\tau) = |\Theta_2|^2(1 + o(1)) \asymp e^{-4\pi y / 3} > 0$. Since $|u_-|$ and $|u_+|$ have the **same** component moduli $(1/\sqrt{2},\, 0,\, 1/\sqrt{2})^T$, whichever of $\lambda_\mp$ is larger leaves the ordered left singular moduli of `up` approaching $\big((1/\sqrt{2}, 0, 1/\sqrt{2})^T,\; (1/\sqrt{2}, 0, 1/\sqrt{2})^T,\; (0, 1, 0)^T\big)$.

4. **Exact rank-`1` Schur factorization in `down` at `(2/5, 4/5)` and combined limit:**
   At $\xi_{\text{down}} = -\frac{1}{5}\tau - \frac{2}{5}$, the six distances $r_c \equiv c/6 - 1/5 \pmod 1$ in $(-1/2, 1/2]$ are $(-1/5, -1/30, 2/15, 3/10, 7/15, -11/30)$, giving leading decay exponents $6 r_c^2 = (36, 1, 16, 81, 196, 121)/150$ in units of $\pi y$. Entry $(0, 2) = A\Theta_1$ (`exponent 1/150`) strictly dominates every other entry (`next is Theta_2 at 16/150`), so $\|M_d / (A\Theta_1) - e_0 e_2^T\| = O(|\Theta_2/\Theta_1|) = O(e^{-\pi y / 10})$ and $u_1^{\text{down}} = e^{i\alpha_0} e_0 + O(e^{-\pi y / 10})$. Eliminating column `2` via $(0, 2) = A\Theta_1$ gives the exact algebraic Schur complement in rows `(1, 2)` and columns `(0, 1)`:
   $$S_{12} = \begin{pmatrix} p^{-1} B \Theta_4 & A \Theta_3 \\ A \Theta_5 & p B \Theta_4 \end{pmatrix} - \frac{B^2}{A\Theta_1} \begin{pmatrix} \Theta_2 \\ p^{-2}\Theta_0 \end{pmatrix} \begin{pmatrix} p^2 \Theta_0 & \Theta_2 \end{pmatrix}.$$
   The rank-`1` outer product has leading entry $-(B^2/A)\Theta_2^2/\Theta_1$ of exponent $(32 - 1)/150 = 31/150$, strictly dominating $A\Theta_3$ (`81/150`), $A\Theta_5$ (`121/150`), and $B\Theta_4$ (`196/150`), and its left factor $(\Theta_2,\, p^{-2}\Theta_0)^T = \Theta_2(1,\, O(e^{-2\pi y / 15}))^T$ aligns with $e_1$. By orthonormality of $\{u_1^{\text{down}}, u_2^{\text{down}}, u_3^{\text{down}}\}$, $U_{\text{down}}(y) = (e_0, e_1, e_2)\operatorname{diag}(e^{i\alpha_0}, e^{i\alpha_1}, e^{i\alpha_2}) + O(e^{-\pi y / 10})$. Multiplying $|U_{\text{up}}(y)^\dagger U_{\text{down}}(y)|$ proves unconditionally for every $\operatorname{Re}\tau \in \mathbb{R}$:
   $$\lim_{\operatorname{Im}\tau \to +\infty} |V_{\text{mark}}(h_*)| = \begin{pmatrix} 1/\sqrt{2} & 0 & 1/\sqrt{2} \\ 1/\sqrt{2} & 0 & 1/\sqrt{2} \\ 0 & 1 & 0 \end{pmatrix}, \qquad \big\||V_{\text{mark}}(h_*)| - V_{\lim}\big\|_{\max} = O(e^{-\pi y / 10}).$$

---

## 2. Why `c = +-2` Appeared Unchanged in `p871_plain_sum.py` (`Answering f1efc59dd`)

1. **Exact dynamic-range scaling across uncentered torsion rows $a \in \{0, 1/5, 2/5, 3/5, 4/5\}$:**
   By `web_wb2_d1.py`'s identity `D2`, shifting $u = 0 \mapsto -h = -c q_H(a\tau + b)$ ($q_H = \pm 3$, $q_H^2 = 9$) multiplies Frame `C`'s $O(1)$ bilinear at $q' = q - \frac{c}{2} q_H$ (`for each spinor factor, eps = c q_H a / 2`) by a scalar of modulus $\exp(\pi c^2 q_H^2 y a^2) = \exp(9\pi c^2 y a^2)$. At $c = \pm 2$ and $y = 17/10$, row $5a = 4$ ($a = 4/5$) exceeds row $5a = 3$ ($a = 3/5$) by the factor
   $$\exp\!\left(36\pi \cdot \frac{17}{10} \cdot \frac{16 - 9}{25}\right) = \exp\!\left(\frac{2142\pi}{125}\right) > 2 \cdot 10^{23} \gg 2^{53}.$$
   When `p871_plain_sum.py` casts each point's $3\times 3$ matrix to `IEEE-754` double precision (`53`-bit significand, machine epsilon $2^{-52} \approx 2 \cdot (1/10)^{16}$) before summing, rows $5a = 0, 1, 2, 3$ are lost below rounding in `S0` and `S5`, reducing the `float64` sum to row $5a = 4$ alone — and under $\tau \mapsto \tau + 5$, a single row $5a = 4$ acquires one uniform phase $\zeta_5^{16 E} = \zeta_5^E$, leaving its singular-value ratios unchanged in `float64`.

2. **Exact `80`-digit `mpmath` drift (with and without `D4`'s flat Hermitian bundle metric $\exp(-9\pi c^2 y a^2)$) at $\tau = 13/100 + (17/10) i \mapsto \tau + 5$:**
   - **Unobstructed cases ($E \equiv 0 \pmod 5$ — `c = 0 down, lepton` and `c = +2 up`):** `0` drift (`< (1/10)^78` in both `S` and `tilde_S`, uncentered and metric-weighted).
   - **All `10` obstructed cases ($E \not\equiv 0 \pmod 5$) at $c = \pm 2$ (`both readings S and tilde_S`):** **every single one drifts at `80` digits** (`uncentered drift between (1/10)^26 and (1/10)^23`, suppressed solely by $\exp(-2142\pi / 125)$), and **every single one drifts at macroscopic order (`between 39/10000 and 3549/10000`) when weighted by `D4`'s flat bundle metric $\exp(-9\pi c^2 y a^2)$**:
     * `c = +2, down (E = 3)`: `80`-digit uncentered drift `> 3 * (1/10)^26` (`S`) and `> (1/10)^26` (`tilde_S`); metric-weighted drift `40/10000` (`S`) and `136/10000` (`tilde_S`) (`nearest 1/10000`).
     * `c = +2, lepton (E = 3)`: `80`-digit uncentered drift `> 8 * (1/10)^26` (`S`) and `> 3 * (1/10)^25` (`tilde_S`); metric-weighted drift `352/10000` (`S`) and `242/10000` (`tilde_S`).
     * `c = -2, up (E = 4)`: `80`-digit uncentered drift `> 6 * (1/10)^24` (`S`) and `> 7 * (1/10)^24` (`tilde_S`); metric-weighted drift `728/10000` (`S`) and `974/10000` (`tilde_S`).
     * `c = -2, down (E = 2)`: `80`-digit uncentered drift `> (1/10)^24` (`S`) and `> 2 * (1/10)^24` (`tilde_S`); metric-weighted drift `2016/10000` (`S`) and `3549/10000` (`tilde_S`).
     * `c = -2, lepton (E = 2)`: `80`-digit uncentered drift `> 2 * (1/10)^24` (`S`) and `> (1/10)^24` (`tilde_S`); metric-weighted drift `353/10000` (`S`) and `1312/10000` (`tilde_S`).
   - **Why $s_3 / s_1 = 0$ identically (`< (1/10)^75`) at $c = +2$ in `down` and `lepton`:** At $c = +2$, $q' = q - q_H$ yields `down` $(4, 5)$ (`q'_R = 5 == 0 mod 5`) and `lepton` $(0, 9)$ (`q'_L = 0 == 0 mod 5`). Having one shifted charge divisible by `5` locks that spinor factor to the point-independent vector $(\vartheta[0,0](0, 2\tau),\, -i\vartheta[1/2,0](0, 2\tau))^T$ across all `24` order-`5` points, making the summed $2\times 2$ residue bilinear exact rank `1` and its $3\times 3$ quaternion contraction exact rank `2`.

`0 of 19.`
