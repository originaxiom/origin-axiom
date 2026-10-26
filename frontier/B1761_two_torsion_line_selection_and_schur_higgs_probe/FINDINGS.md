# B1761 — Data-Free 2-Torsion Line-Selection Theorem & Yukawa-Gram Higgs Dressing Probe

**Points addressed:** `P-349` (why order $N = 10$ without data), `P-357` (principled parameter-free Higgs doublet dressing), `P-366` (backreaction / Gram dressing on $v_{\mathrm{DR}}$), `P-373` (non-fitted order-10 selection), `P-377` (two Higgs doublets at the strip), `P-384` (order-13..20 comparison and unique status of $(2/5, 1/10)$).

---

## 1. Theorem 1 (Attack 2 — Data-Free Asymmetric 2-Torsion $e_1$-Kernel Selects Order $N = 10$ Universally)

On the punctured torus $E_\tau$ with primitive torsion twist $w = a\tau + b$ ($a, b \in \mathbb{Q}$) of any order $N = \mathrm{lcm}(\mathrm{denom}(a), \mathrm{denom}(b)) \ge 1$ and $\mathrm{SU}(5)$ hypercharge assignments $(q_Q, q_u) = (1, -4)$, $(q_Q, q_d) = (1, 2)$, $(q_L, q_e) = (-3, 6)$:

1. **Analytical Proof Across All Torsion Orders $N \ge 1$ in $\mathbb{Q}^2/\mathbb{Z}^2$:**
   The $e_1$ ($i$-channel) puncture residue is $R_i(x, y) \propto \vartheta_2((x+y)/2, \tau)\,\vartheta_2((x-y)/2, \tau)$. Since $x_s + y_s = \pm 3w$ in every sector ($3w$ in up/lep, $-3w$ in down), any zero of $\vartheta_2((x+y)/2, \tau)$ vanishes simultaneously in all three sectors (`R_i^(up) = R_i^(down) = R_i^(lep) = 0`), leaving the $D=9$ lock $Y_e = Y_d^T$ unbroken on $e_1$-dressed doublets.
   Requiring **Condition C1 (Asymmetric 2-Torsion $e_1$-Kernel)**:
   $$a \notin \left\{0, \frac{1}{2}\right\} \pmod 1, \qquad R_i^{(\mathrm{up})}(\tau, w) \equiv 0, \qquad R_i^{(\mathrm{down})}(\tau, w) \not\equiv 0, \qquad R_j^{(\mathrm{up})}(\tau, w) R_k^{(\mathrm{up})}(\tau, w) \not\equiv 0$$
   forces the zero to arise exclusively from the sector-difference argument $x_{\mathrm{up}} - y_{\mathrm{up}} = 5w$ and not from $x_{\mathrm{down}} - y_{\mathrm{down}} = -w$:
   $$5w \equiv \frac{1}{2} \pmod{\mathbb{Z}\tau + \mathbb{Z}} \quad \text{and} \quad w \not\equiv \frac{1}{2} \pmod{\mathbb{Z}\tau + \mathbb{Z}}.$$
   Writing $w = a\tau + b$ with $a \in (0, 1/2)$ and $b \in [0, 1)$, this is algebraically equivalent to:
   $$5a \in \mathbb{Z} \implies a \in \left\{\frac{1}{5}, \frac{2}{5}\right\}, \qquad 5b \in \mathbb{Z} + \frac{1}{2} \implies b \in \left\{\frac{1}{10}, \frac{3}{10}, \frac{1}{2}, \frac{7}{10}, \frac{9}{10}\right\},$$
   which **forces the primitive torsion order to be $N = \mathrm{lcm}(5, 10) = 10$ across the entire torsion lattice $\mathbb{Q}^2/\mathbb{Z}^2$ of all orders $N \ge 1$**. In particular, even at $N = 20 = 2 \times 10$, any line satisfying $5a \in \mathbb{Z}$ and $5b \in \mathbb{Z} + 1/2$ has $10a, 10b \in \mathbb{Z}$ and therefore reduces to primitive order $N = 10$.

2. **Exhaustive Verification Across All 662 Census Lines ($N \le 12$ and $N \in \{13, 14, 15, 20\}$):**
   Testing all $266$ lines of $N \le 12$ (`B1726`/`B1749`) and all $396$ lines of $N \in \{13, 14, 15, 20\}$ (`B1755`) confirms that **exclusively 10 lines out of 662** satisfy Condition C1:
   - **Orbit I (`lines 134..138` of `B1726`):** $a = 1/5, b \in \{1/10, 3/10, 1/2, 7/10, 9/10\}$ ($N = 10$).
   - **Orbit II (`lines 149..153` of `B1726`):** $a = 2/5, b \in \{1/10, 3/10, 1/2, 7/10, 9/10\}$ ($N = 10$).
   - **Zero lines** of $N \in \{13, 14, 15, 20\}$ satisfy Condition C1.

---

## 2. Theorem 2 (Attack 2 — Unique Selection of the $a = 2/5, 10b \text{ odd}$ $T$-Orbit via Up-Sector Isotropic Proximity)

Why do Orbit I ($a = 1/5$) and Orbit II ($a = 2/5$) behave identically in the down and lepton sectors (up to a permutation of $b \in \text{odd}/10$), yet diverge in the up sector?
- In the down sector $(q_Q, q_d) = (1, 2)$ and lepton sector $(q_L, q_e) = (-3, 6) \equiv (2, 1) \pmod 5$, both $a = 1/5$ and $a = 2/5$ assign the same unordered pair of $\tau$-slopes $\{1/5, 2/5\} \pmod 1$ to the left and right fermions.
- In the up sector $(q_Q, q_u) = (1, -4) \equiv (1, 1) \pmod 5$, both fermions receive the same $\tau$-slope $a \pmod 1$, whose distance to the half-period $1/2$ is $\|a - 1/2\|_{\mathbb{Z}} = 3/10$ at $a = 1/5$ versus the unique minimum $\|a - 1/2\|_{\mathbb{Z}} = 1/10$ at $a = 2/5$.
- Consequently, at $\tau = 0.3145 + 3.0345i$:
  - On **Orbit I ($a = 1/5$, `lines 134..138`)**: the up-sector off-cone invariant is $I(u_{\mathrm{up}}) = |u_{\mathrm{up}} \cdot u_{\mathrm{up}}| / \|u_{\mathrm{up}}\|^2 \in [0.2905, 0.2910]$ and the doublet-to-scalar ratio is $\|R_{(j,k)}^{(\mathrm{up})}\| / |R_1^{(\mathrm{up})}| \approx 1.855$.
  - On **Orbit II ($a = 2/5$, `lines 149..153`)**: the up-sector off-cone invariant is **$I(u_{\mathrm{up}}) \in [0.00628, 0.00683] < 0.01$** (**$44.7\times$ closer to the isotropic null cone $u \cdot u = 0$**) and the doublet-to-scalar ratio is **$\|R_{(j,k)}^{(\mathrm{up})}\| / |R_1^{(\mathrm{up})}| \in [12.10, 12.62]$** (**$6.66\times$ stronger doublet dominance**).

Requiring **Condition C2 ($I(u_{\mathrm{up}}) < 0.05$, or $\|R_{(j,k)}^{(\mathrm{up})}\| / |R_1^{(\mathrm{up})}| > 2$)** uniquely selects the **single 5-line $T$-orbit $a = 2/5, b \in \{1/10, 3/10, 1/2, 7/10, 9/10\}$** across all 662 lines with **zero Standard Model data**.

---

## 3. Theorem 3 & Theorem 4 (Attack 1 — Yukawa Gram Matrices $\Sigma^{(s)}$ and Zero-Parameter Down-Higgs Dressing on the Strip)

On $(2/5, 1/10)$ across all 4 strip points of `B1757`, define the normalized $3 \times 3$ Hermitian Yukawa Gram matrices on the Higgs triplet space $\mathbb{C}^3$:
$$\Sigma^{(s)}_{cd}(\tau, w) \;=\; \frac{\mathrm{Tr}\!\left(Y^{(s)\dagger}_c Y^{(s)}_d\right)}{\sum_{a=0}^2 \mathrm{Tr}\!\left(Y^{(s)\dagger}_a Y^{(s)}_a\right)}, \qquad c, d \in \{0, 1, 2\} = \{e_1, e_2, e_3\}.$$

1. **Exact $1 \oplus 2$ Block-Diagonalization of $\Sigma^{(\mathrm{up})}$ and $e_1$-Parity of $\Sigma^{(\mathrm{down})}, \Sigma^{(\mathrm{lep})}$:**
   - Across all 4 strip points, $\Sigma^{(\mathrm{up})}$ is strictly block-diagonal between $e_1$ and $(e_2, e_3)$:
     $$\sqrt{|\Sigma^{(\mathrm{up})}_{0,1}|^2 + |\Sigma^{(\mathrm{up})}_{0,2}|^2} \;\le\; 1.2 \times 10^{-17}.$$
   - Across all 4 strip points, $\Sigma^{(\mathrm{lep})}$ and $\Sigma^{(\mathrm{down})}$ satisfy the exact $e_1$-parity conjugation identity:
     $$\left\|\Sigma^{(\mathrm{lep})}(\tau, w) - P_{e_1}\,\Sigma^{(\mathrm{down})}(\tau, w)\,P_{e_1}\right\|_F \;\le\; 2.5 \times 10^{-16}, \qquad P_{e_1} = \mathrm{diag}(-1, +1, +1).$$

2. **Zero-Parameter Inverse-Gram Down-Higgs Dressing:**
   - Applying the inverse of the complex-conjugated down-sector Yukawa Gram matrix $(\overline{\Sigma^{(\mathrm{down})}(\tau, w)})^{-1}$ to the isotropic $(e_2, e_3)$ core $v_{012} = (0, \overline{\mathrm{dr}}_1, \overline{\mathrm{dr}}_2)^T$ with **zero free parameters** yields at the primary census point $\tau = 0.3145 + 3.0345i$:
     $$H_{d,\mathrm{inv\_gram}} = \begin{pmatrix} -0.02871 + 0.05278i \\ 0.71358 \\ +0.00512 + 0.69797i \end{pmatrix} \quad \text{vs} \quad H_{d,\mathrm{opt}}^{(\mathrm{B1757})} = \begin{pmatrix} -0.02656 + 0.04882i \\ 0.71696 \\ -0.00170 + 0.69490i \end{pmatrix},$$
     achieving an overlap **$|\langle H_{d,\mathrm{opt}} \mid H_{d,\mathrm{inv\_gram}}\rangle| = 0.999961$** (an angle of **$0.506^\circ$ in $\mathbb{CP}^2$**).
   - Substituting the zero-parameter Schur complement $e_{1,\mathrm{schur}} = -0.02876 + 0.05120i$ into $h_{d,0}$ at $\tau = 0.3145 + 3.0345i$ keeps **$\chi^2_{\mathrm{nine}} = 19.59 < 21.67$** (passing the 9-observable bar), and replacing the entire 3-vector $H_d$ with the zero-parameter $H_{d,\mathrm{inv\_gram}}$ lowers $\chi^2_{\mathrm{nine}}$ from $821.16$ to **$32.01$**.
   - Pairing the zero-parameter $H_{d,\mathrm{inv\_gram}}$ with the 1-complex-parameter up-sector $e_1$-pencil $H_u(\zeta_u) = (\zeta_u, \overline{\mathrm{dr}}_1, \overline{\mathrm{dr}}_2)^T$ (**2 real DOFs total**, matching the DOF count of `B1743`'s pencils which had $\chi^2_{\mathrm{nine}} \ge 212.14$) lowers $\chi^2_{\mathrm{nine}}$ to **$29.38 - 41.76$** across all 4 strip points with a single stable branch $\zeta_u \approx 0.10\,e^{+i\,35.5^\circ}$ (and down to **$23.82 - 27.88$** with 3 real DOFs, beating `B1757`'s 8-DOF fit $29.17$ at $\tau = 0.3145 + 3.10i$).

## Seen first

`VERDICT topic-sweep /order-10|2\/5|1\/10|Schur|Gram|two doublets|B1757/ (full text): 48 of 1531 arcs on main match (NEGATIVE 7, OPEN 4, PROVED 37)`
— among them B1656, B1726, B1743, B1749, B1755, B1757, B1759. **The register:** P-349, P-357, P-366, P-373, P-377, P-384. **Literature:** arXiv:2209.07249, arXiv:2302.11183 (P-382).
