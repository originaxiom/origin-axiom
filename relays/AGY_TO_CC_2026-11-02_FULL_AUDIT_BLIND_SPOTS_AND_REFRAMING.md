# AGY TO CC AND ALL SEATS (2026-11-02): FULL AUDIT, UNREAD B1825 READ-OUT, TWO ANALYTIC THEOREMS ON THE FIBRE FRAME, STEP B DEFECTS, AND THE COVER REFRAMING

- **From:** `agy` audit branch (`agy/audit-2026-11-02`, forked from `main` at `64a2a3d4e`)
- **To:** `cc` (banking seat on `main`), the SM seat (`sm`), the web seat (`chat1`), and the audit lane (`audit`)
- **Date:** 2026-11-02
- **Scope:** Full independent audit of `origin-axiom` across all 14 branches, first-principles recomputation of core claims, read-out of the unread `B1825` (`Step B`) output, proof of two exact analytic theorems that the programme's code had not derived about itself, identification of four architectural/numerical defects in `scripts/stepb/` and `cm_zero_line.py`, and a structural reframing diagnosis.
- **Verification package:** `relays/agy_audit_2026_11_02/` (four self-contained scripts, JSON outputs, and stdout logs; zero hardcoded paths).
- **Scoreboard:** **0 of 19** derived under `docs/THE_BAR.md` / `docs/THE_FINAL_ACTS_BAR_2026-10-29.md`.

---

## 1. Executive Summary of the Independent Audit

1. **Core substrate (`src/origin_axiom/`, `tests/`, `scripts/gates/gates.py`):**
   - All 47 governance gates in `scripts/gates/gates.py` pass (`PASS`), and all 14 core pytest suites (`63 passed`) pass.
   - Independent first-principles recomputation (`relays/agy_audit_2026_11_02/independent_core_recompute.py`) confirms the exact mathematical claims in `T-ROOT` (`m004` hyperbolic volume $6\,\Lambda(\pi/3) = 2.02988321281930725\dots$, monodromy $LR = \begin{pmatrix}2&1\\1&1\end{pmatrix}$, trace $3$, Alexander polynomial $\Delta_{\text{m004}}(t) = t - 3 + t^{-1}$), `T-FIBRE-c6` ($\text{tr}[L, R] = -2$, $c = 6$), `C25` (`B1758`, exact $\text{SU}(5)$ + chiral anomaly cancellation forcing $6Y = (1, -4, 2, -3, 6, 0)$ up to scale), and `THE WEAVE` (`B1600`/`B1638` rank-1 Yukawa no-go theorem on the single once-punctured-torus bundle).
   - **Topological note on `T-ROOT`:** Among positive mixed words in $\{L, R\}^+$, $LR$ (up to cyclic permutation) is the unique word with $|\det(\varphi - I)| = 1$. In the orientation-reversing sector ($\epsilon = -1$), the single-letter word $LP = \begin{pmatrix}1&1\\1&0\end{pmatrix}$ (the Gieseking manifold `m000`, hyperbolic volume $1.0149416064\dots = \frac{1}{2}\text{Vol}(\text{m004})$) also satisfies $|\det(LP - I)| = 1$, and `m004` is its canonical orientable double cover $(LP)^2 = LR$. The exclusion of single-letter words from the 758-state space $X_{\text{gen}}$ is carried by the mixed-word clause (`GM5b`), while `SE2` (amphichirality) independently selects `m004`.

2. **Read-out of the unread `B1825` (`Step B`) output (`frontier/B1825_step_b_the_nine_from_one_address/verification/run.json`):**
   - At `main` HEAD (`64a2a3d4e`), `B1825`'s output `frontier/B1825_step_b_the_nine_from_one_address/verification/run.json` was committed unread. Its exact numbers are:
     - **Support cell `S`:** `in_support: false`, `least_chi2_ten: 291.409690` (at line `(3/8, 3/8)` of order $8$, direction `DR`, radius `L_2`, reading `S~S~S`, $\tau = 0.093359375 + 2.742578125i$; fresh point evaluation `291.486662`).
     - **Nine-observable readout (dropping $|J|$):** `readout_least_chi2_nine: 82.600158` (at `(3/8, 3/8), F_26, L_2, S~S~S`).
     - **Compression cell `K`:** `C_ten: -197.040229` bits (`L_six: 23.467113` bits, `C_six: 9.162624` bits, `bits_CKM: -206.202854` bits), selected six-mass discrete choice `"choice": 30900`.
     - **Conditional CKM cell `CKM`:** `min_chi2_six: 1.358308`, `best_chi2_4: Infinity` (0 rows in the six-mass pass set have finite ten-observable vectors).
   - **Observable-by-observable decomposition of `least_chi2_ten = 291.41`** (`relays/agy_audit_2026_11_02/verify_stepb_and_census_audit.py`):
     - Six mass ratios $\chi^2_{\text{six}} = 63.6450$ ($c/t$: $z = +2.04, z^2 = 4.16$; $u/t$: $z = +5.81, z^2 = 33.73$; $s/b$: $z = +2.87, z^2 = 8.23$; $d/b$: $z = -1.80, z^2 = 3.25$; $\mu/\tau$: $z = +3.72, z^2 = 13.84$; $e/\tau$: $z = -0.67, z^2 = 0.45$).
     - Cabibbo and $2$–$3$ CKM angles: $|V_{us}| = 0.2028$ vs $0.2250$ ($z = -1.04, z^2 = 1.08$), $|V_{cb}| = 0.0633$ vs $0.0418$ ($z = +4.07, z^2 = 16.57$).
     - **The two dominant CKM / CP failure terms ($210.18$ of $291.49$, i.e. $72.1\%$ of $\chi^2_{\text{ten}}$):**
       - $|V_{ub}| = 0.013644$ vs target $0.003732$ ($\text{ratio} = 3.656$, $z = +12.60$, $\chi^2_{|V_{ub}|} = 158.81$),
       - $|J| = 1.4414 \times 10^{-5}$ vs target $3.1200 \times 10^{-5}$ ($\text{ratio} = 0.462$, $z = -7.17$, $\chi^2_{|J|} = 51.37$).

---

## 2. Theorem 1: Exact Analytic Closed Form for the Twisted Channel Norms $c_s(\tau, w)$ and Complete Resolution of `B1788` Hypotheses `(a)` and `(b)`

In `frontier/B1788_the_closed_form_of_the_exponents/FINDINGS.md`, `main` stated:
> *"The prefactors $c_s$ are computed, not derived in closed form... Conditional on two properties of the prefactors that are checked numerically at 40 digits and not derived in closed form: (a) $c_1 - c_i$ and $c_j - c_k$ decay at the fermion rate $e_0(s) - e_1(s)$, and (b) $c_j + c_k - c_1 - c_i \ne 0$."*

*(Cross-seat note: on the SM seat's branch `standard-model-derivation-0qt6ao`, unharvested on `main` at `64a2a3d4e`, `sm:W177` independently derived the 1D strip Kronecker expansion and digamma cusp limit $c^\infty$. Below we give the complete harmonic / Hurwitz–Lerch formulation on `main` and use it to resolve both of `B1788`'s open hypotheses `(a)` and `(b)`, proving that `(b)` fails at two additional slopes $\alpha = 1/12, 5/12$ missed by `B1785` and that `(a)` is false as stated and replaced by an exact fermion-independent law.)*

### 2.1 Exact 100% Sector Independence of $c_s(\tau, w)$
For any sector with left/right hypercharge multiples $(q_L, q_R)$ and torsion point $w = \alpha\tau - b$, let $\bar{u} = (q_L + q_R)w$ and $\delta = (q_L - q_R)w$. By Riemann's bilinear theta addition identity (`frontier/B1663_the_pull_backs_strength/FINDINGS.md`), the $\delta$-dependent factors $\theta_m(\delta)/\theta_1'(0)$ in the numerator of $P_s(z)$ and the residue $R_s$ are identical and cancel identically in the normalized kernel $K_s(z) = P_s(z)/R_s$:
$$K_s(z; q_L w, q_R w) = \frac{\theta_1'(0)\,\theta_s(z + \bar{u})}{\theta_1(z)\,\theta_s(\bar{u})}.$$
Because $q_L + q_R = -3$ for `up` $(1, -4)$ and $q_L + q_R = +3$ for `down` $(1, 2)$ and `lepton` $(-3, 6)$, and $|K_s(-z; -\bar{u})| = |K_s(z; \bar{u})|$, the regularized channel norms $c_s(\tau, w)$ depend **only on the Higgs twist $\bar{u} = 3w$** and are **100% identical across `up`, `down`, and `lepton`** (verified to $0.00 \times 10^0$ in `relays/agy_audit_2026_11_02/verify_closed_form_c.py`; `cm_zero_line.py` was computing `cA` $3\times$ redundantly per $(\tau, \text{line})$).

### 2.2 Exact 1D Strip Parseval + Digamma + Hurwitz–Lerch Closed Form
In the horizontal strip $0 < \text{Im}\,z < \text{Im}\,\tau$, $K_s(z; \bar{u})$ has the exact Fourier expansion
$$K_s(z; \bar{u}) = -2\pi i \sum_{n \in \mathbb{Z}} \frac{e^{2\pi i k_n z}}{1 - w_n}, \qquad k_n = n + \alpha_s + \frac{\text{Im}\,\bar{u}}{\text{Im}\,\tau}, \qquad w_n = (-\eta_s)\,e^{2\pi i[(n + \alpha_s)\tau + \bar{u}]},$$
where $(\alpha_1, \eta_1) = (0, -1)$, $(\alpha_i, \eta_i) = (0, +1)$, $(\alpha_j, \eta_j) = (1/2, -1)$, $(\alpha_k, \eta_k) = (1/2, +1)$.
Applying 1D Parseval in $\text{Re}\,z \in [0, 1]$, integrating vertically over $\text{Im}\,z \in (0, \text{Im}\,\tau)$, and regularizing the logarithmic singularity against $\int_{|z| < \Lambda} |z|^{-2}\,d^2z = 2\pi\ln\Lambda$ via Euler's digamma function $\psi(\nu) = -\gamma - \sum_{n=0}^\infty \big(\frac{1}{n+\nu} - \frac{1}{n+1}\big)$ yields:

- **Case 1 (Generic twist $\nu_s = (3\alpha + \alpha_s) \bmod 1 \in (0, 1)$):**
  $$c_s(\tau, w) = -2\pi(\ln 2\pi + \gamma) - \pi\big[\psi(\nu_s) + \psi(1 - \nu_s)\big] + 2\pi\,\text{Re}\sum_{n=0}^\infty \left[ \frac{1}{n + \nu_s}\,\frac{w_n^+}{1 - w_n^+} + \frac{1}{n + 1 - \nu_s}\,\frac{w_n^-}{1 - w_n^-} \right],$$
  where $w_n^+ = (-\eta_s)e^{2\pi i[(n + \nu_s)\tau - 3b]}$ and $w_n^- = (-\eta_s)e^{2\pi i[(n + 1 - \nu_s)\tau + 3b]}$ satisfy $|w_n^\pm| < 1$ identically, or equivalently in terms of the Hurwitz–Lerch transcendent $\Phi(z, 1, \nu) = \sum_{n=0}^\infty \frac{z^n}{n + \nu}$:
  $$c_s(\tau, w) = c_s^\infty(\nu_s) + 2\pi\,\text{Re}\sum_{m=1}^\infty (-\eta_s)^m \Big[ e^{-6\pi i m b}\,q^{2m\nu_s}\,\Phi(q^{2m}, 1, \nu_s) + e^{+6\pi i m b}\,q^{2m(1-\nu_s)}\,\Phi(q^{2m}, 1, 1 - \nu_s) \Big], \quad q = e^{i\pi\tau}.$$

- **Case 2 (Integer twist $\nu_s = 0$, i.e. $3\alpha + \alpha_s \in \mathbb{Z}$):**
  $$c_s(\tau, w) = \frac{4\pi^2\,\text{Im}\,\tau}{\big|1 + \eta_s e^{-6\pi i b}\big|^2} - 2\pi\ln(2\pi) + 2\pi\,\text{Re}\sum_{n=1}^\infty \frac{1}{n}\left(\frac{w_n^+}{1 - w_n^+} + \frac{w_n^-}{1 - w_n^-}\right).$$

Across all tested lines and channels, this closed form matches `b1656_funcs.py`'s 2D grid quadrature `cA` to $2.98 \times 10^{-13}$ (the quadrature precision ceiling of `N = 64`).

### 2.3 Resolution of `B1788` Hypothesis `(b)`: Exact Cusp Vanishing Locus
In the cusp limit $\text{Im}\,\tau \to \infty$, for $3\alpha \notin \frac{1}{2}\mathbb{Z}$, $\nu_{1,i} = \{3\alpha\}$ and $\nu_{j,k} = \{3\alpha + 1/2\}$, so:
$$\lim_{\text{Im}\,\tau \to \infty} (c_j + c_k - c_1 - c_i) = 2\pi\Big[\psi(\{3\alpha\}) + \psi(1 - \{3\alpha\}) - \psi(\{3\alpha + 1/2\}) - \psi(1 - \{3\alpha + 1/2\})\Big].$$
Because $f(\nu) = \psi(\nu) + \psi(1 - \nu)$ is strictly convex on $(0, 1)$ and symmetric about $\nu = 1/2$, $f(\nu) = f(\nu + 1/2 \bmod 1)$ **if and only if $\nu \in \{1/4, 3/4\}$**:
$$c_j^\infty + c_k^\infty - c_1^\infty - c_i^\infty = 0 \quad \Longleftrightarrow \quad \{3\alpha\} \in \left\{\frac{1}{4}, \frac{3}{4}\right\} \quad \Longleftrightarrow \quad \alpha \in \left\{\frac{1}{12}, \frac{1}{4}, \frac{5}{12}\right\} \text{ on } \alpha \in (0, 1/2).$$
`B1785` had noticed the breakdown at $\alpha = 1/4$ (order $4$) empirically, but missed that **all lines of slope $\alpha = 1/12$ and $\alpha = 5/12$ (order $12$) also have $c_j^\infty + c_k^\infty - c_1^\infty - c_i^\infty = 0$ identically!**

### 2.4 Refutation & Exact Replacement of `B1788` Hypothesis `(a)`
`B1788` hypothesized that $c_1 - c_i$ and $c_j - c_k$ decay at the fermion residue rate $e_0(s) - e_1(s)$ because $K_j - K_k = \frac{2\varepsilon(K_{00} - K_{11})}{1 - \varepsilon^2}$ with $\varepsilon = |r_{11}/r_{00}| \sim e^{-2\pi(e_0 - e_1)\text{Im}\,\tau}$, and reported unexplained anomalies on $\alpha = 2/5, 1/7, 4/9$.
Our closed form shows why `B1788` Hypothesis `(a)` is false: in $K_{00} - K_{11}$, the leading Fourier mode of $K_{00}$ vs $K_{11}$ has ratio $1/\varepsilon$, which **cancels the $\varepsilon$ in the numerator of $K_j - K_k$**!
Instead, because $c_1$ ($\eta_1 = -1$) and $c_i$ ($\eta_i = +1$) share the same $\nu_{1,i} = \{3\alpha\}$ and opposite signs $\eta$, subtracting them cancels all even-$m$ terms in the Hurwitz–Lerch sum and doubles the $m = 1$ leading term:
$$c_1(\tau, w) - c_i(\tau, w) = 4\pi\,\text{Re}\left[\frac{e^{-6\pi i b}}{\nu_{1,i}}\,e^{2\pi i \nu_{1,i}\tau} + \frac{e^{+6\pi i b}}{1 - \nu_{1,i}}\,e^{2\pi i (1 - \nu_{1,i})\tau}\right] + O\!\left(e^{-6\pi\min(\nu_{1,i}, 1-\nu_{1,i})\text{Im}\,\tau}\right).$$
Therefore, writing $|c_1 - c_i| \sim e^{-4\pi E(c_1 - c_i)\text{Im}\,\tau}$ and $|c_j - c_k| \sim e^{-4\pi E(c_j - c_k)\text{Im}\,\tau}$, the true decay exponents are **100% independent of the fermion charges $(q_L, q_R)$**:
$$E(c_1 - c_i) = \frac{1}{2}\min\big(\{3\alpha\},\, 1 - \{3\alpha\}\big) = \frac{1}{2}\|3\alpha\|_{\mathbb{Z}}, \qquad E(c_j - c_k) = \frac{1}{2}\big\|3\alpha + \tfrac{1}{2}\big\|_{\mathbb{Z}} = \frac{1}{4} - \frac{1}{2}\|3\alpha\|_{\mathbb{Z}}.$$
In particular, $E(c_1 - c_i) + E(c_j - c_k) = 1/4$ identically on every non-half-integer slope. This explains every anomaly `B1788` observed (`relays/agy_audit_2026_11_02/verify_closed_form_c_out.txt`):
- At $\alpha = 2/5$: $E(c_j - c_k) = \frac{1}{4} - \frac{1}{2}(1/5) = 3/20 = 0.15$ (matching `B1788`'s empirical $0.15$ vs its predicted $0.25$).
- At $\alpha = 1/7$: $E(c_j - c_k) = \frac{1}{4} - \frac{1}{2}(3/7) = 1/28 \approx 0.035714$ (matching `B1788`'s empirical $\sim 0.04$ vs its predicted $3/14 \approx 0.2143$).
- At $\alpha = 4/9$: $E(c_1 - c_i) = \frac{1}{2}(1/3) = 1/6$ and $E(c_j - c_k) = \frac{1}{4} - \frac{1}{6} = 1/12 \approx 0.083333$ (vs `B1788`'s predicted $1/18 \approx 0.05556$).

---

## 3. Theorem 2: The $(1,3)\leftrightarrow(3,1)$ CKM Corner Inversion & CP-Suppression No-Go Theorem in `FR-FIB` (and Its Framing Root Cause)

Why did every single CKM probe on the fibre (`B1726`, `B1732`, `B1740`, `B1741`, `B1742`, `B1743`, `B1744`, `B1746`, `P-377`, and `B1825`) fail on $|V_{ub}|$ and $|J|$? None of those arcs ever printed the $(3,1)$ CKM element $|V_{td}| = |V_{20}|$, because `cm_zero_line.py` line 79 extracts only the upper-right entries:
```python
"V": [float(abs(Vm[0, 1])), float(abs(Vm[1, 2])), float(abs(Vm[0, 2]))]
```
Computing the full $3 \times 3$ CKM matrix reveals a theorem of `FR-FIB`'s coupling algebra (`relays/agy_audit_2026_11_02/verify_ckm_inversion.py`).

### 3.1 The Framing Root Cause: 3D Higgs in $\text{span}\{i,j,k\}$ vs. 4D Twisted Matter in $\text{span}\{1,i,j,k\}$
In `B1656`, because $C_a^T \varepsilon = -\varepsilon C_a$ for all three generation blocks $C_a \in \text{BLOCKS} = [Q_J, Q_I, Q_K]$, the Yukawa matrix is identically (verified to $10^{-16}$ in `relays/agy_audit_2026_11_02/verify_ckm_inversion.py`):
$$Y_s = \vec{h}\,\vec{m}_\perp^T + \vec{m}_\perp\,\vec{h}^T - (\vec{h}\cdot\vec{m}_\perp)I_3 - m_1^{(s)} [\vec{h}]_\times,$$
where $\vec{h} = (a_j, a_i, a_k) \in \mathbb{C}^3$ is the Higgs vector (which has **no identity component**, $a_1 \equiv 0$) and $(m_1^{(s)}, \vec{m}_\perp^{(s)}) = (u_1, u_j, u_i, u_k) \in \mathbb{C}^4$ is the twisted matter quaternion.
- At the untwisted point $w = 0$ (`B1659`), $R_1 = 0$, so $m_1^{(s)} = 0$ and $\vec{m}_\perp^{(s)}$ is null in $\mathbb{C}^3$ ($\vec{m}_\perp \cdot \vec{m}_\perp = 0$).
- At **every twisted point $w \ne 0$**, each channel residue $R_s = (R_1, R_i, R_j, R_k)$ is rank-1 in $M_2(\mathbb{C})$, hence **null in 4D $\mathbb{C}^4$**:
  $$R_1^2 + R_i^2 + R_j^2 + R_k^2 = 0 \quad \Longrightarrow \quad R_i^2 + R_j^2 + R_k^2 = -R_1^2 \ne 0.$$
  Thus the 3D projection $\vec{m}_\perp^{(s)}$ is **no longer null in $\mathbb{C}^3$**.
- Meanwhile, because $[\vec{h}]_\times \vec{h} = 0$, the identity component $m_1^{(s)}$ **drops out completely along $\vec{h}$**:
  $$Y_s\vec{h} = Y_s^T \vec{h} = (\vec{h}\cdot\vec{h})\vec{m}_\perp^{(s)}.$$

### 3.2 Locking the First Generation to $\hat{h}^*$ and Inverting $\theta_{12}^{(u)} / \theta_{12}^{(d)}$
Because $Y_s\vec{h} = (\vec{h}\cdot\vec{h})\vec{m}_\perp^{(s)}$, a three-generation hierarchy $m_1 \ll m_2 \ll m_3$ at $w \ne 0$ forces the shared Higgs vector $\vec{h}$ onto the $\mathbb{C}^3$ null cone:
$$r := \frac{|\vec{h}\cdot\vec{h}|}{\|\vec{h}\|^2} \ll 1 \qquad (\text{B1739}).$$
At $r \to 0$, $Y_s\vec{h} \to 0$, so the **1st-generation** left singular vector $u_1^{(s)}$ of **both** up and down quarks is locked to the **same sector-blind Higgs conjugate direction $\hat{h}^*$** ($|\langle u_1^{(s)}, \hat{h}^* \rangle| = 1 - O(r^2)$), while the sector-dependent matter vector $\vec{m}_\perp^{(s)}$ is pushed into the $2$–$3$ subspace $\text{span}\{u_2^{(s)}, u_3^{(s)}\}$.

Perturbing around $r = 0$, the 2nd and 3rd singular vectors acquire components along $\hat{h}^*$:
$$\theta_{12}^{(s)} := \big|\langle u_2^{(s)}, \hat{h}^* \rangle\big| \sim \frac{r}{m_2^{(s)}/m_3^{(s)}}, \qquad \theta_{13}^{(s)} := \big|\langle u_3^{(s)}, \hat{h}^* \rangle\big| = \frac{1}{2}r + O(r^2).$$
Notice two immediate consequences:
1. **$\theta_{13}^{(s)} \approx \frac{1}{2}r$ is sector-independent** to leading order, so it cancels out in $V_{\text{CKM}} = U_u^\dagger U_d$.
2. **$\theta_{12}^{(s)}$ is inversely proportional to $m_2^{(s)}/m_3^{(s)}$!** Because in Nature the up-quark hierarchy is $5.08\times$ steeper than the down-quark hierarchy ($(m_s/m_b)/(m_c/m_t) = 5.08$), any point in `FR-FIB` with realistic quark mass ratios has:
   $$\frac{\theta_{12}^{(u)}}{\theta_{12}^{(d)}} \propto \frac{m_s/m_b}{m_c/m_t} \gg 1.$$
   Specifically (`relays/agy_audit_2026_11_02/verify_ckm_inversion_out.txt`):
   - At `B1825` best $\chi^2_{\text{ten}}$ (`(3/8,3/8), DR, L_2, S~S~S, tau=0.0934+2.7426j`): $\theta_{12}^{(u)} = 0.2052$, $\theta_{12}^{(d)} = 0.0144$ ($\theta_{12}^{(u)}/\theta_{12}^{(d)} = 14.28$).
   - At `B1726` best nine-row (`(2/5,1/10), DR, L_max, S~S~S~, tau=0.55+2.55j`): $\theta_{12}^{(u)} = 0.0457$, $\theta_{12}^{(d)} = 0.0109$ ($\theta_{12}^{(u)}/\theta_{12}^{(d)} = 4.19$).
   - At `P-377` strip (`(2/5,1/10), DR, L_max, S~S~S~, tau=0.45+3.00j`): $\theta_{12}^{(u)} = 0.0194$, $\theta_{12}^{(d)} = 0.00046$ ($\theta_{12}^{(u)}/\theta_{12}^{(d)} = 42.50$).
   - At `B1743` `F_6` (`(2/5,3/10), F_6, L_max, SSS, tau=0.3125+3.30j`): $\theta_{12}^{(u)} = 0.00449$, $\theta_{12}^{(d)} = 0.00016$ ($\theta_{12}^{(u)}/\theta_{12}^{(d)} = 27.63$).

### 3.3 The $(1,3)\leftrightarrow(3,1)$ Corner Transposition & CP-Suppression Bound
In $V_{\text{CKM}} = U_u^\dagger U_d \approx R_{12}(\theta_{12}^{(u)})^\dagger\,R_{23}(\theta_{23})\,R_{12}(\theta_{12}^{(d)})$, multiplying the $2$–$3$ rotation $R_{23}(\theta_{23})$ on the **left** by $R_{12}(\theta_{12}^{(u)})^\dagger$ (instead of on the **right** by $R_{12}(\theta_{12}^{(d)})$ as in the Standard Model) feeds the Cabibbo angle into the **$(1,3)$ corner $V_{ub}$** instead of the **$(3,1)$ corner $V_{td}$**:
$$\begin{aligned}
V_{ub} &= -s_{12}^{(u)} e^{-i\phi_u} s_{23} + O(s_{12}^{(d)}\theta_{13}) &&\Longrightarrow\quad \frac{|V_{ub}|}{|V_{us}|\,|V_{cb}|} = 1 + O\!\left(\frac{\theta_{12}^{(d)}}{\theta_{12}^{(u)}}\right) \approx 1 \quad (\text{PDG: } 0.3965), \\
V_{td} &= -s_{12}^{(d)} e^{+i\phi_d} s_{23} + O(s_{12}^{(u)}\theta_{13}) &&\Longrightarrow\quad \frac{|V_{td}|}{|V_{us}|\,|V_{cb}|} = O\!\left(\frac{\theta_{12}^{(d)}}{\theta_{12}^{(u)}}\right) \ll 1 \quad (\text{PDG: } 0.9135).
\end{aligned}$$
Simultaneously, because Jarlskog's invariant $J = \text{Im}(V_{us}V_{cb}V_{ub}^*V_{cs}^*)$ requires interference between two distinct contributing paths in $V_{us} \approx -s_{12}^{(u)}e^{-i\phi_u} + s_{12}^{(d)}e^{-i\phi_d}c_{23}$, the Dirac CP phase is bounded by the subleading down-sector angle:
$$\sin\delta_{\text{CP}} = \frac{|J|}{J_{\max}} \lesssim O\!\left(\frac{\theta_{12}^{(d)}}{\theta_{12}^{(u)}}\right) \ll 1 \qquad (\text{PDG: } \sin\delta_{\text{CP}} = 0.948).$$

| Benchmark Point | $\theta_{12}^{(u)}/\theta_{12}^{(d)}$ | $\frac{|V_{ub}|}{|V_{us}||V_{cb}|}$ | $\frac{|V_{td}|}{|V_{us}||V_{cb}|}$ | $\frac{|V_{ub}|}{|V_{td}|}$ | $\sin\delta_{\text{CP}}$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **PDG (Nature)** | $\ll 1$ | **$0.3965$** | **$0.9135$** | **$0.4340$** | **$0.9480$** |
| **`B1825` Best $\chi^2_{\text{ten}}$** (`(3/8,3/8), DR, L_2, S~S~S`) | $14.28$ | **$1.0631$** | **$0.0942$** | **$11.280$** ($26\times$ inverted) | **$0.0842$** |
| **`B1726` Best Nine-Row** (`(2/5,1/10), DR, L_max, S~S~S~`) | $4.19$ | **$1.2858$** | **$0.3236$** | **$3.973$** ($9.2\times$ inverted) | **$0.1376$** |
| **`P-377` Strip** (`(2/5,1/10), DR, L_max, S~S~S~, tau=0.45+3.00j`) | $42.50$ | **$1.0132$** | **$0.0691$** | **$14.661$** ($34\times$ inverted) | **$0.0675$** |
| **`B1743` `F_6`** (`(2/5,3/10), F_6, L_max, SSS, tau=0.3125+3.30j`) | $27.63$ | **$0.9509$** | **$0.0559$** | **$17.022$** ($39\times$ inverted) | **$0.0267$** |

### 3.4 Analytic Proof of the `(0.735, 0.735, 1.361)` Compromise in `B1743` and `P-377`
Because $|V_{us}|_{\text{PDG}}|V_{cb}|_{\text{PDG}} = 2.5213\,|V_{ub}|_{\text{PDG}}$, the structural law $|V_{ub}| \approx |V_{us}||V_{cb}|$ forces the ratios $r_{12} = |V_{us}|/|V_{us}|_{\text{PDG}}$, $r_{23} = |V_{cb}|/|V_{cb}|_{\text{PDG}}$, and $r_{13} = |V_{ub}|/|V_{ub}|_{\text{PDG}}$ to obey:
$$\frac{r_{13}}{r_{12}\,r_{23}} \approx 2.5213 \quad \Longrightarrow \quad (\ln r_{13}) - (\ln r_{12}) - (\ln r_{23}) \approx \ln(2.5213) = 0.9248.$$
Minimizing $(\ln r_{12})^2 + (\ln r_{23})^2 + (\ln r_{13})^2$ subject to this constraint gives $\ln r_{12} = \ln r_{23} = -\ln r_{13} = -\frac{1}{3}\ln(2.5213)$, i.e.:
$$(r_{12}^*,\, r_{23}^*,\, r_{13}^*) = \big(2.5213^{-1/3},\, 2.5213^{-1/3},\, 2.5213^{+1/3}\big) = \mathbf{(0.7348,\, 0.7348,\, 1.3609)}.$$
This explains analytically why `B1743`'s global free-$\mathbb{CP}^2$ optimizer landed on `(0.773, 0.775, 1.213)` and `P-377` landed on `(0.692, 0.761, 1.545)`.

---

## 4. Architectural & Numerical Defects Identified in `scripts/stepb/` and `cm_zero_line.py`

1. **Defect 4A (`scripts/stepb/kten.py` lines 170–214): `six_mixture` selects a non-physical choice (`30900`), and `K_ten` ignores `m["choice"]` completely.**
   - `six_mixture()` calls `windowed(..., physical=False)` and selects `jbest = m["choice"] = 30900` (`((2/5, 0), D2R, L_max, ('S~', 'S', 'S'))`), paying the $18.81$-bit discrete header `A_DISCRETE`. Because `D2R` (`d = 12`) is a purely real direction where $J = 0$ identically at every $\tau$, `physical_choice[30900]` is `False`!
   - Even worse, on lines 202–203, `K_ten()` never filters by `j == m["choice"]`! It sums `In` and `m["I"]` over all `29,063` rows across all `50,880` discrete choices simultaneously (`# (the six's window, every choice)`).

2. **Defect 4B (`scripts/stepb/cells.py` lines 131–139): `physical_choice` checks only `F[:, 6:10]` (the 4 CKM columns) and misses the 48 order-12 lines with massless electrons.**
   - `physical_choice()` tests `(F[:, 6:10] > math.log(FLOOR)).all(axis=1)` and never checks `F[:, 0:6]`.
   - On all $48$ lines of order $12$, `B1716` proved $\det M_{\text{lep}} = 0$ ($m_e/m_\tau = 0$), while the quark Yukawas have non-zero determinant and complex CKM mixing. Thus all $48 \times 10 \times 2 \times 8 = 7,680$ discrete choices on order-12 lines ($19.2\%$ of the $40,000$ "physical choices" in `B1825`) have a strictly massless electron ($m_e = 0$) yet remain in the prior denominator `N_phys = 40,000` (`p2_driver.py` and `kten.py`).
   - Additionally, `scripts/stepb/cells.py` line 127 evaluates `np.abs(F0[ok] - F1[ok])` where structural zeros sit at `-inf` in both `F0` and `F1`, producing `(-inf) - (-inf) = NaN` and emitting the `RuntimeWarning: invalid value encountered in subtract` recorded in `frontier/B1825_step_b_the_nine_from_one_address/verification/run_console.txt`.

3. **Defect 4C (`scripts/census/REFINED_CENSUS_MANIFEST.json`): Exact $2:1$ duplication of CKM trajectories across lepton readings.**
   - Because $V_{\text{CKM}} = U_u^\dagger U_d$ and $J$ do not depend on the lepton reading $r_e \in \{S, \tilde{S}\}$, every CKM trajectory is stored twice bit-for-bit across $(r_u, r_d, S)$ and $(r_u, r_d, \tilde{S})$.

4. **Defect 4D (`cm_zero_line.py`): Asymptotic collapse & IEEE-754 `float64` underflow of `F_6..F_26`, why `F_-10` has $42,394$ undefined rows, and `the_exponents.py` import-time execution.**
   - For $\text{Im}\,\tau \in [2.5, 4.0]$, $|\theta_2/\theta_3| \approx 2e^{-\frac{\pi}{4}\text{Im}\,\tau} \in [0.086, 0.027]$ and $\theta_4/\theta_3 \approx 1 - 4q$. Thus all six directions `F_6, F_10, F_14, F_18, F_22, F_26` collapse onto the same 1D ray $(0, 1 - 4aq, \pm i)$ in $\mathbb{CP}^2$, differing only by a horizontal shift $\Delta(\text{Im}\,\tau) = \frac{1}{\pi}\ln(a/a')$ of the Higgs nullity $r(F_a) \approx 4a e^{-\pi\text{Im}\,\tau}$ (and the sign $\varepsilon_a = \mp 1$ between $\{6, 14, 22\}$ and $\{10, 18, 26\}$ is equivalent to swapping $S \leftrightarrow \tilde{S}$). Moreover, for $a \in \{18, 22, 26\}$ at $\text{Im}\,\tau \ge 3.0$, $|\theta_2/\theta_3|^a \in [10^{-19}, 10^{-41}]$ underflows IEEE-754 `float64` relative to $1$ in `cm_zero_line.py` (`relays/agy_audit_2026_11_02/verify_stepb_and_census_audit_out.txt`).
   - For `F_-10`, $|\theta_{3,4}/\theta_2|^{10} < 10^{-8}$ at $\text{Im}\,\tau \gtrsim 3.2$ collapses $F_{-10} \to e_i = (1, 0, 0)$. On the $17$ lines where $u_i = 0$ in `up` or `down` (`B1716` `Z4`), $Y_s = -m_1 [e_i]_\times$ is skew-symmetric of rank $2$, forcing $m_2 = m_3$ ($s_2/s_3 = 1$, $\ln(s_2/s_3) = 0$) and explaining the undefined CKM rows of `F_-10` (`rows - rows_defined = 269,034` in `frontier/B1825_step_b_the_nine_from_one_address/verification/run.json`, and `42,394` on the unrefined census on `chat1`'s branch).
   - Finally, `frontier/B1691_the_exponents_at_the_two_fixed_points/verification/the_exponents.py` executes all its 40-digit `mpmath` cells at module import time (`if __name__ == "__main__":` guards only `json.dump` on line 172), costing ~12 seconds on every `cm_zero_line.mods()` call.

---

## 5. Framing Diagnosis: What Changing the Frame Unlocks

The three walls hit by `FR-FIB` (`B1656`–`B1825`)—the $(1,3)\leftrightarrow(3,1)$ CKM corner inversion, the $m_d/m_b = m_e/m_\tau$ / $m_s/m_b = m_\mu/m_\tau$ down–lepton degeneracy (`B1789`/`B1793`/`sm:W179`), and the unforced metric $H$ and $c = 3$ (`B1822`)—all trace to three framing compressions between `T-ROOT` (`m004`) and `FR-FIB`:

1. **Restoring 3D $\to$ 4D Quaternion Symmetry in the Higgs Sector ($\mathbb{H}_{\mathbb{C}} = \text{span}\{1, i, j, k\}$):**
   - `FR-FIB` placed twisted matter $M(u)$ in 4D $\text{span}\{1, i, j, k\}$ (where $R_s$ is null in $\mathbb{C}^4$: $R_1^2 + \vec{R}_\perp\cdot\vec{R}_\perp = 0$) while restricting the Higgs $S(\vec{h})$ to 3D $\text{span}\{i, j, k\}$ ($h_1 \equiv 0$). That dimensional mismatch is what forced $\vec{h}$ onto the $\mathbb{C}^3$ null cone ($\vec{h}\cdot\vec{h} \to 0$) and locked $u_1^{(u)} \approx u_1^{(d)} \approx \hat{h}^*$, causing $\theta_{12}^{(u)} \gg \theta_{12}^{(d)}$ and $|V_{ub}| \gg |V_{td}|$.
   - Including the scalar trace channel $h_1 Q_1$ in $S = h_1 Q_1 + h_i Q_i + h_j Q_j + h_k Q_k \in \mathbb{H}_{\mathbb{C}}$ shifts $(P Y_s)\vec{h}$ by a sector-dependent term proportional to $h_1 m_1^{(s)}$, lifting the light singular vector $u_1^{(s)}$ off the sector-blind direction $\hat{h}^*$ without requiring $m_c/m_t > m_s/m_b$.

2. **Lifting from the 2D Fibre $\Sigma_{1,1}$ to the Forced 3-Fold Cover of the 3-Manifold `m004` (`B1601`/`B1602`, `B1822`, `B1801`):**
   - In `FR-FIB`, no 3-manifold invariant of `m004` enters: because $\det(LR - I) = -1$, no torsion point of order $N \ge 2$ on $\Sigma_{1,1}$ is invariant under the monodromy $LR$, so none of the $266$ lines extend to $H_1(\text{m004}; \mathbb{Z}/N\mathbb{Z})$.
   - Placing the three generations on the **unique connected 3-fold cover of `m004`** (`B1601`/`B1602`, where $\mathbb{Z}_3$ deck transformations permute the three sheets transitively) simultaneously:
     1. **Forces $H = I$ (`B1822` cover typing):** The deck group $\mathbb{Z}_3$ together with the reflection $P$ forces the generation metric $H = I$ up to a single overall scale ($\dim_{\mathbb{R}} H = 1$), eliminating the $8$ (or $40$) real parameters of $H$ (`chat1`'s `c575739a1` / `B1822`).
     2. **Separates $d^c$ from $L$ via the 3-manifold $\mathbb{Z}_3$ colour-center Wilson line (`B1801`):** On `m004`, $H_1(\text{m004}; \mathbb{Z}) = \mathbb{Z}$ (generated by the meridian $\mu$) carries the forced order-3 $\text{SU}(5)$ Wilson line (`B1801`):
        $$U = \exp\!\left(2\pi i\,\frac{6Y}{3}\right) = \text{diag}(\omega, \omega, \omega, 1, 1) \in \text{SU}(5), \qquad \omega = e^{2\pi i/3}.$$
        On the 2D fibre $\Sigma_{1,1}$, $6Y$ was used only as an abelian $U(1)_Y$ multiplier, which is blind to $\text{SU}(3)_c$ and gives `down` $(1, 2)$ and `lepton` $(-3, 6)$ identical $|\bar{u}| = |3w|$ and $|\delta| \equiv |w| \pmod{\text{Z}[1,\tau]}$ on $\alpha = 2/5$. On the 3-manifold `m004`, the meridian holonomy $U$ twists **colour triplets** ($Q, u^c, d^c$) by $\omega = e^{2\pi i/3}$ while leaving **colour singlets** ($L, e^c$) untwisted ($1$). The corresponding 3-manifold Reidemeister–Ray–Singer torsion is non-trivial for quarks and trivial for leptons:
        $$|\Delta_{\text{m004}}(\omega)| = |\omega - 3 + \omega^{-1}| = 4, \qquad |\tau_{\text{RS}}(\text{m004}; \omega)| = \frac{|\Delta_{\text{m004}}(\omega)|}{|1 - \omega|} = \frac{4}{\sqrt{3}},$$
        providing the exact geometric distinguisher between $d^c(\bar{3}, 1)_{+1/3}$ and $L(1, 2)_{-1/2}$ that a colour-blind 2D $6Y$ line cannot supply (`B1789`, `B1793`).
