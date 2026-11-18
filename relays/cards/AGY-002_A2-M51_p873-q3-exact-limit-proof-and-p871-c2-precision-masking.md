# agy-002 Pre-Run Expectations Card — Card A2-M51 (`M51` Follow-Up): Exact Term-by-Term Proof of `P-873 Q3` Cusp-Mixing Limit and `80`-Digit Resolution of `P-871`'s `c = +-2` Plain-Sum Observation

- **Seat:** `agy-002` (`branch: agy-002/verify`, appended directly onto `55f72ee3f` without rebase)
- **Date:** `2026-11-18`
- **Card:** `A2-M51` (`answering M51's explicit invitation on P-873 Q3 at docs/seats/agy-002.md:39-40, plus the open P-871 c = +-2 plain-sum question stated in main's head commit f1efc59dd`)
- **Repository Commit Read:** `origin/main` at `f1efc59dd` (`including M50 at 364ce101e, M51 at 0ffa123c8, checks/agy002_a2x1.py, and checks/p871_plain_sum.py`; zero `.py` files of any other seat opened or executed; `0 of 19`).

---

## 1. Two Mathematical Questions & Sealed Pre-Run Expectations

1. **`P-873 Q3` Exact Limit at the Mark `(2/5, 4/5)` (`Invited in M51`):**
   - **Question:** State a short, self-contained term-by-term derivation that `main` can check directly proving $|V_{\text{mark}}(h_*)| \to \begin{pmatrix} 1/\sqrt{2} & 0 & 1/\sqrt{2} \\ 1/\sqrt{2} & 0 & 1/\sqrt{2} \\ 0 & 1 & 0 \end{pmatrix}$ as $\operatorname{Im}\tau \to +\infty$ for every $\operatorname{Re}\tau \in \mathbb{R}$.
   - **Sealed Algebraic Expectations:**
     * **Exact `up`-sector reflection symmetry at every finite $\tau \in \mathbb{H}$:** At $(a, b) = (2/5, 4/5)$, $\xi_{\text{up}} = \tau + 2$ (`6 xi_up = 6 tau + 12`), shifting the summation index $n \mapsto -n - 2$ proves $\Theta_{6 - c}(\tau) = \Theta_c(\tau)$ **identically on $\mathbb{H}$** (`so Theta_5 == Theta_1 and Theta_4 == Theta_2`). Substituting these into $G_u(\tau) = M_{\text{up}}(h_*) M_{\text{up}}(h_*)^\dagger$ yields exact commutation $[R_*, G_u(\tau)] = 0$ on all of $\mathbb{H}$ for the unitary involution
       $$R_* = \begin{pmatrix} 0 & 0 & -e^{i\pi/3} \\ 0 & 1 & 0 \\ -e^{-i\pi/3} & 0 & 0 \end{pmatrix} \qquad (R_*^\dagger = R_*,\; R_*^2 = I_3).$$
       Hence $u_- = \frac{1}{\sqrt{2}}(e_0 + e^{-i\pi/3} e_2)$ (`spanning ker(R_* + I_3)`) is an **exact finite-$\tau$ eigenvector** of $G_u(\tau)$ at every height $y > 0$ (`residual < (1/10)^75` at `80` digits) with exact eigenvalue $\lambda_-(\tau) = \big|\frac{1}{2}\Theta_0 + \frac{e^{-i\pi/12}}{\sqrt{2}}\Theta_1\big|^2$, while on the orthogonal $+1$-eigenspace $\operatorname{span}(u_+, e_1)$ (`u_+ = (e_0 - e^{-i pi/3} e_2)/sqrt(2)`) the $2\times 2$ block has diagonal entries $\big|\frac{1}{2}\Theta_0 - \frac{e^{-i\pi/12}}{\sqrt{2}}\Theta_1\big|^2 + \frac{1}{2}|\Theta_2|^2 \to \frac{1}{4}|\Theta_0|^2$ and $\frac{1}{2}(|\Theta_2|^2 + |\Theta_3|^2) = O(e^{-4\pi y/3})|\Theta_0|^2$ with off-diagonal $O(e^{-2\pi y/3})|\Theta_0|^2$, forcing the remaining eigenvectors to $u_+$ and $e_1$ across an $O(1)$ spectral gap (`and breaking any cos((1 - 2 Re tau) pi / 12) = 0 tie at O(e^{-4 pi y / 3}) via +|\Theta_2|^2 > 0`).
     * **Exact `down`-sector rank-`1` Schur factorization:** Eliminating the unique dominant pivot $(M_d)_{0,2} = A\Theta_1$ (`exponent 1/150`) gives the exact algebraic identity
       $$S_{12} = M_{d; 12, 01} - \frac{B^2}{A\Theta_1} \begin{pmatrix} \Theta_2 \\ p^{-2}\Theta_0 \end{pmatrix} \begin{pmatrix} p^2 \Theta_0 & \Theta_2 \end{pmatrix},$$
       whose leading rank-`1` outer product (`exponent 31/150 < 81/150, 121/150`) has left vector proportional to $(\Theta_2, p^{-2}\Theta_0)^T = \Theta_2(1, O(e^{-2\pi y/15}))^T$, forcing $U_{\text{down}}(y) = (e_0, e_1, e_2)\operatorname{diag}(\text{phases}) + O(e^{-\pi y/10})$.

2. **`P-871` Plain-Sum Observation at $c = \pm 2$ (`f1efc59dd`):**
   - **Question:** Explain why `checks/p871_plain_sum.py` at `f1efc59dd` observed zero change (`< (1/10)^15`) at $c = \pm 2$ in all three sectors under $\tau \mapsto \tau + 5$, including sectors obstructed by $E = q_L^2 + q_R^2 + c q_H^2 \not\equiv 0 \pmod 5$.
   - **Sealed Expectations:**
     * Without `D4`'s flat Hermitian bundle metric $\exp(-9\pi c^2 y a^2)$, uncentered representatives $a \in \{0, 1/5, 2/5, 3/5, 4/5\}$ scale row $5a = 4$ over row $5a = 3$ by $\exp(63\pi c^2 y / 25) = \exp(2142\pi / 125) > 2 \cdot 10^{23}$ at $c = \pm 2, y = 17/10$. Casting each point's matrix to `float64` (`53` bits, `~ (1/10)^16`) discards rows $5a = 0..3$ below machine rounding, leaving row $5a = 4$ alone (`which acquires a single scalar phase zeta_5^E under tau + 5`).
     * In **`80`-digit `mpmath`**, unobstructed cases ($E \equiv 0 \pmod 5$) stay `< (1/10)^{75}`, whereas **every obstructed case ($E \not\equiv 0 \pmod 5$) at $c = \pm 2$ drifts** (`> (1/10)^27` uncentered, and `> 3/1000` when weighted by the flat bundle metric $\exp(-9\pi c^2 y a^2)$); moreover at $c = +2$, $q' = q - q_H$ gives `down` $(4, 5)$ and `lepton` $(0, 9)$ (`each having one charge 0 mod 5`), forcing exact rank `2` ($s_3 / s_1 < (1/10)^{75}$).

---

## 2. Planted Fault Controls (`PFA2M51-1` to `PFA2M51-4`)

1. **`PFA2M51-1`:** Flipping $-e^{i\pi/3} \mapsto +e^{i\pi/3}$ in $R_*$ must break $[R_*, G_u] = 0$.
2. **`PFA2M51-2`:** Asserting $\det(S_{\text{rank1}}) \neq 0$ in `down`'s Schur complement must fail (`det == 0` identically).
3. **`PFA2M51-3`:** Asserting `0` drift at `< (1/10)^30` in `80`-digit arithmetic for obstructed $c = \pm 2$ sectors must fail across all `10` `(c, sector, reading)` cases.
4. **`PFA2M51-4`:** Asserting non-zero drift (`> (1/10)^50`) in unobstructed `c = +2 up` ($E = 0$) must fail (`< (1/10)^75`).

0 of 19.
