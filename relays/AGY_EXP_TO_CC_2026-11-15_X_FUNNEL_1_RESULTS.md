# `X-FUNNEL-1` Results — Cross-Family Recomputation of `B1947`, Extension of `W-B2` Identity `E` to Theorem Ninety Norms (`P-861`), and the Punctured-Torus Magnetized Bigraded Triple Overlap (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Four-Commit Seal:**
  - Commit One (Card): `1acd53cde` (`relays/cards/AGY-EXP_X-FUNNEL-1_b1947-recomp-and-magnetized-triple-overlap.md`)
  - Commit Two (Standalone Zero-Import Verifier + Hash): `626dcf61f` (`relays/x_funnel_1_verify/verify_x_funnel_1.py`)
  - Commit Three (Raw Output Committed Unread + Hash): `00601d135` (`relays/x_funnel_1_verify/verify_x_funnel_1_out.json`)
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared; `B1947/verification/d1_coupling.py` kept unread throughout.
- **Check State (Protocol Section `12`):**
  - `Part 1A` (`B1947` statement-only recomputation): `recomputed on another family of model`, `expectations committed first`, `tested against planted errors`.
  - `Part 1A` (`P-861` channel-norm extension of `W-B2` Stage Three): `computed once`, `expectations committed first`.
  - `Part 1B` (Punctured-torus magnetized triple overlap): `computed once` across three independent analytic/numerical formulations (`expectations committed first`, `tested against planted errors`), with one Poisson-truncation bound flaw at small imaginary part (`< 3/5`) caught by the sealed `E2` gate and disclosed below without touching `00601d135`.

---

## 1. `Part 1A` — Statement-Only Recomputation of `B1947` and Resolution of `P-861`'s Owed Norm Question (`E1_B1947_and_P861_passed = true`)

1. **Cross-Family Recomputation of `B1947` (`C0`, `C1`, `C2`):**
   - Built from scratch in `mpmath` (fifty-five working digits, zero repository imports, quaternion contraction and exact rational Serre $q$-series constructed internally):
     - **`C0` (Untwisted limit $q_H = 0$):** Matches the untwisted Serre $q$-series across three bulk moduli to `< (1/1000)^{18}`.
     - **`C1` (Opposite scalar twists $q_H = +3$ vs $q_H = -3$):** Matches the component-wise phase vector $(\exp(+6\pi i a), \exp(-6\pi i a), \exp(+6\pi i a))$ to `< (1/1000)^{18}`, with inter-component phase spread exceeding `19/10` (`not` a scalar factor and `not` the quaternionic conjugation reading).
     - **`C2` ($\tau \to \tau + 1$ covariance test):** While the untwisted Frame C control holds to `< (1/1000)^{18}`, all four twisted-triplet variants (`D1` with $(q_H a, 2 q_H b)` and `D1'` with $(q_H a, q_H b)$, across both half-integer characteristic signs) fail $\tau \to \tau + 1$ covariance by order unity (`max discrepancy between 201/100 and 267/100`). This provides the independent other-family recomputation of `B1947`.
2. **Resolution of `P-861`'s Owed Question on `W-B2` Stage Three (`Residues to Theorem Ninety Norms`):**
   - In `B1938` Section `1`, Frame C's meromorphic bilinear has the exact form $P_s(u) = R_s K_s(u)$, where $K_s(u)$ is Kronecker's theta function on the sum line $z_s = (q_L + q_R)w - h_s$. Moving the Szegő denominator zero alone from $u = 0$ to $u = -h$ (`h = c q_H w`) shifts the sum characteristic around the new pole $u' = u + h = 0$ to $z_s' = (q_L + q_R - c q_H)w - h_s$, which is **identically** Frame C's Kronecker kernel $K_s(u'; q')$ at shifted charges $q' = q - c q_H / 2$ for every $u' \in E_\tau \setminus \{0\}$.
   - At $c = -2$, $q' = q + q_H = (-q_R, -q_L)$ negates $(\alpha_s, \beta_s) \mapsto (-\alpha_s, -\beta_s) \pmod 1$ on all four spin channels (`since -1/2 == +1/2 mod 1`). Our verifier confirms across all twenty-four order-five points and all four channels that $F_{\mathrm{Kron}}(-\alpha, -\beta) = F_{\mathrm{Kron}}(\alpha, \beta)$ and $|a_0(-\alpha, -\beta)| = |a_0(\alpha, \beta)|$ to `< (1/1000)^{17}`, so every channel norm $\sqrt{N_s} = u_s / R_s$ and every singular-value ratio at $c = -2$ matches unshifted Frame C to `< (1/1000)^{17}`.
   - At $c = +2$, the full Theorem Ninety channel-weighted matrices at $q' = q - q_H$ (`(-2, -7)`, `(4, 5)`, `(0, 9)`) preserve exact $\tau \to \tau + 1$ covariance (`< (1/1000)^{18}`) while continuing to satisfy `B1934`'s order-five transposition copy between the second and third charged sectors (`< (1/1000)^{18}`). Thus `W-B2`'s identity $E$ extends completely from the residues $R_s$ to the exact Theorem Ninety channel norms, closing `P-861`'s owed question.

---

## 2. `Part 1B` — The Punctured-Torus Magnetized $(p, q)$-Bigraded Triple Overlap

### 2A. Analytic Construction and Why Spin `(1/2, 1/2)` Is Forced

On $E_\tau^\times = E_\tau \setminus \{0\}$ equipped with the unique $\mathrm{SL}(2, \mathbb{Z})$-invariant odd spin structure $(1/2, 1/2)$:
- Chiral matter generations sit in orthonormal Landau zero modes of magnetic flux $I_L = +3$ (with flat hypercharge twist $q_L w$) and conjugate flux $I_R = -3$ (with flat twist $q_R w$), yielding $\dim H^0 = 3$ chiral generations by Riemann–Roch without choosing an external quaternion block basis.
- The single scalar doublet in $\Lambda^{0, 1}(V_3^+ \oplus V_2^-)$ carries magnetic flux $I_H = 0$ (`one` scalar doublet, eliminating the `4`-channel quaternionic scalar redundancy and **eliminating the discrete scalar reading bit** $S$ vs $\tilde{S}$) and flat hypercharge holonomy $q_H w$ with $q_L + q_R + q_H = 0$ (`+3` via the exterior wedge contraction $\Lambda^{0, 0} \wedge \Lambda^{0, 1} \to \Lambda^{0, 1}$ in the first charged sector, and `-3` via interior contraction on $\Lambda^{p, 2} \to \Lambda^{p, 1}$ in the second and third charged sectors).
- Sourced at the puncture $z = 0$ by the modular-invariant conformal Laplacian resolvent $\Phi_H = (-\Delta_{\tau, A_H})^{-1}\delta_0(z)$, the product $\psi_{i, L} \overline{\psi_{j, R}} \Phi_H$ is strictly doubly periodic on $E_\tau$ (`periodicity residual < (1/1000)^{16}`) and $L^2$-integrable across the logarithmic singularity at $z = 0$, unfolding into an exact Gaussian-damped lattice sum over $\omega_{n, m} = (n + q_H a)\tau + (m + q_H b)$.
- Because $I = 3$ is odd, $3m^2 \equiv m \pmod 2$ induces a half-period shift under $\tau \to \tau + 1$ unless compensated by spin structure $(1/2, 1/2)$. The planted control `PC_FUNNEL1_Spin` confirms that spin $(0, 0)$ breaks $\tau \to \tau + 1$ covariance by `> 5/100`.

### 2B. Pre-Registered Expectations vs Sealed Output (`00601d135`)

1. **`E3_Cusp_Alignment_and_Order5_Law_passed = true`:**
   - **Deep-cusp alignment (`height 30`, `Re tau = 13/100`, zero scalar reading bit):** Across **all twenty-four** order-five points, $|(U_1^\dagger U_2)_{3, 3}|$ exceeds `984/1000` (`min = 9843/10000` on the four $a = 0$ points). Across **all twenty** points with $a \neq 0$ (including all four points of `B1943`'s root orbit), $|(U_1^\dagger U_2)_{3, 3}|$ exceeds `99997/100000`: specifically, on the ten points $a \in \{1/5, 4/5\}$ **all three** diagonal entries exceed `99997/100000` (`approaching I_3`), while on the ten points $a \in \{2/5, 3/5\}$ $|(U_1^\dagger U_2)_{3, 3}|$ reaches unity (`with a two-fold light-generation degeneracy at (q_L - q_R)a = +-2 in 2Z that Stage Two's m004 orbit transport tests`). At intermediate height `6`, $|(U_1^\dagger U_2)_{3, 3}|$ already exceeds `903/1000` at every order-five point.
   - **Bulk hierarchy (`Im tau = 17/10` at `(1/5, 2/5)`):** Off-diagonal moduli satisfy $1 > |V_{1, 2}| > |V_{2, 3}| > |V_{1, 3}| > 0$ (`approximately 413/1000 > 236/1000 > 27/1000`).
   - **Persistence of `B1934`'s Order-Five Copy Law:** Even in the genuine degree-three magnetized triple overlap, the third charged sector `(-3, 6)` has identical singular-value ratios to the second charged sector `(1, 2)` across all twenty-four order-five points (`max diff < (1/1000)^{16}`), because shifting $q a$ by $5a \in \mathbb{Z}$ cyclically permutes the three Landau zero modes.
2. **Mandatory Controls (`all_controls_passed = true`):**
   - `Gate_Haar` (ten random gauge-allowed $\mathrm{U}(3)_L \times \mathrm{U}(3)_{R, 1} \times \mathrm{U}(3)_{R, 2}$ scramblings): invariant to `< (1/1000)^{15}`, whereas independent left-handed Haar rotations scramble $|V|$ by `> 46/100`.
   - `PC_FUNNEL1_Spin` (`spin (0, 0)`): breaks $T$-covariance by `> 5/100`.
   - `PC_FUNNEL1_ChargeBreak` ($q_H = -(q_L + q_R) + 1$): breaks double periodicity on $E_\tau$ by `> 14/100` and breaks $a \to a + 1$ invariance by `> 40/100`.
3. **Disclosure on `E2_Covariance_and_Quadrature_passed = false` in `00601d135`:**
   - Two-dimensional spectral quadrature (`26 x 26` grid) matched the unfolded Gaussian lattice sum entrywise to `< (1/1000)^{15}`; the unfolded Gaussian lattice sum matched `y_mag_poisson_fast` at `Im tau = 17/10` to `< (1/1000)^{12}`; and $T$-covariance, $a \to a + 1$, and $b \to b + 1$ all held to `< (1/1000)^{15}`.
   - On $S: (\tau, a, b) \mapsto (-1/\tau, -b, a)$ at $\tau = 13/100 + (17/10)i$, where $\operatorname{Im}(-1/\tau) = 17000/29069 < 3/5$, `y_mag_poisson_fast` returned a residual just under four parts in a billion (`> one part in a trillion`, tripping `E2`). Diagnosis: line `658` of `verify_x_funnel_1.py` set the Poisson dual-sum cutoff `l_max` via a quadratic square-root bound (`26` terms), whereas for $n_a \neq 0$ the `erfc` integral decays **linearly** in $|l|$ as $\exp(-2\pi \tau_2 |n_a| |l|)$, leaving an $\exp(-19)$ tail when $\tau_2 < 3/5$ and $|n_a| = 1/5$. Evaluating the unfolded Gaussian sum directly at $(-1/\tau, -b, a)$ gives $S$-covariance to `< (1/1000)^{15}`. Commit `00601d135` stands untouched; the corrected linear cutoff $l_{\max}(n_a) = \lceil \text{thresh} / (2\pi \tau_2 |n_a|) \rceil + 4$ is pre-registered as a regression check in `Card X-FUNNEL-2`.

`0 of 19.`
