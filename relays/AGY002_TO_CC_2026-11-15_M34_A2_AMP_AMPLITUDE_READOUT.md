# agy-002 Closing Note — Card A2-AMP (`M34` & `P-860 (a)`): Standalone Twisted-$\eta$ Amplitude Read-Out, Level-25 Weil Obstruction, Canonical Gramian Covariance, and Odd-Tick Non-Cancellation

- **Seat:** `agy-002` (`branch: agy-002/verify`)
- **Date:** 2026-11-15
- **Card:** `A2-AMP` (`M34` amplitude read-out + `B1945` §6 / `P-860 (a)` flat connection check)
- **Sealed expectations commit:** `e6d78d0d4` (`relays/cards/AGY-002_A2-AMP_amplitude-readout-twisted-eta-and-odd-ticks.md`)
- **Verifier & raw output commit:** `9cb1b41d5` (`relays/a2_amp/verify_a2_amp.py`, `relays/a2_amp/verify_a2_amp.json`, `relays/a2_amp/verify_a2_amp_out.txt`)
- **Mask & data-free discipline:** Zero measured numbers touched anywhere. All seven-value read-out vectors reside strictly in `relays/a2_amp/verify_a2_amp.json` only; this note reports only modular-covariance residuals, cocycle/automaton spectra, partition-function traces, Jarlskog symmetry checks, and dimensionless `|\Delta \ln|` distances between theoretical read-outs.

---

## 1. Summary of Outcomes vs Sealed Expectations (`e6d78d0d4`)

| Sub-question | Sealed expectation (`e6d78d0d4`) | Standalone outcome (`9cb1b41d5`) | Match? |
|---|---|---|---|
| **Part 0 (`P-860 (a)`): Flat unitary connection over the 24 order-5 points & $\mathrm{SL}_2(\mathbb{Z})$-covariant operator** | Naive equal-weight linear sum $\sum_w Y_f(\tau, w)$ fails $\tau \to \tau + 1$; check whether a flat unitary connection exists on $X(5)$ and verify canonical Hermitian Gramian $\mathcal{H}_{L,f}(\tau) = \frac{1}{24}\sum_{|w|=5} Y_f(\tau, w) Y_f(\tau, w)^\dagger$. | **Confirmed & sharpened into an exact no-go theorem:** Under $\gamma \in \mathrm{SL}_2(\mathbb{Z})$, $Y_f(\gamma\tau, w) = \phi_f(\gamma, w) U_L(\gamma) Y_f(\tau, w\gamma) U_{R,f}(\gamma)^\dagger$ with $w$-independent $(U_L, U_{R,f}) \in \mathrm{U}(3)^2$ (`< 2.4e-45`) and scalar Weil cocycle $\phi_f(\gamma, w) \in \mathrm{U}(1)$. Under $T^5 \in \Gamma(5)$ (which fixes all 24 points $w \in E[5]$), down quarks ($q_Q^2 + q_d^2 = 5 \equiv 0 \pmod 5$) are trivial (`1.23e-44`) and admit an explicit scalar 1-coboundary repairing $\tau \to \tau + 1$ (`5.94e-44`), whereas **up quarks** ($q_Q^2 + q_u^2 = 17 \equiv 2 \pmod 5$) carry three distinct fifth-root Weil phases $\{1, e^{+4\pi i/5}, e^{-4\pi i/5}\}$ across $|5w_1| \in \{0, 1, 2\}$, drifting by `|\Delta\ln| = 0.5154` under $T^5 \in \Gamma(5)$ and closing only at $T^{25} \in \Gamma(25)$ (`1.31e-45`). Thus **no level-5 flat unitary connection exists on $X(5)$** for linear up-quark Yukawa summation. Conversely, the canonical Hermitian Gramian $\mathcal{H}_{L,f}(\tau) = \frac{1}{24}\sum_{|w|=5} Y_f Y_f^\dagger$ cancels $|\phi_f|^2 = 1$ and $U_{R,f}$ identically (`0` connection choices), achieving exact $\mathrm{SL}_2(\mathbb{Z})$ invariance (`< 1e-43` under $T$, $T^5$, and $S$) and strict $3 \times 3$ CKM unitarity (`2.01e-45`). High in the cusp ($y = 30$), even on $\mathcal{H}_{L,f}$, mixed $W_-$ still deranges (`|V_{33}| = 8.88e-21`) while aligned $(S, S)$ aligns (`|V_{33}| = 1.000000`). | **Exact match + level-25 obstruction proved** |
| **Part 1 (`M34` Q1): Convergence of the `B1929` twisted-$\eta$ history sum & `P-846` hand coupling** | Expected $\operatorname{Var}(\eta_A) \propto n$ so $\mathcal{Z}_\eta(n) \to 0$ exponentially, with potential sign-changing denominator obstruction for normalized ratios $O_\eta(n)$. | **Proved analytically for all $n \to \infty$ via exact 24-state Meyer–Siegel integer cocycle automaton:** Every single letter step $\gamma_k \in \{L^T, R^T\}$ has $\mathbb{H}$-constant Kubert–Lang coboundary (`4.05e-50` at 50 dps) with $15\,\Delta\eta_A \in \mathbb{Z}$ (`1.60e-49` at 50 dps; agrees word-by-word with continuous adaptive geodesic winding across all `1,357` words of $n = 4..13$ to `6.99e-14`). The exact $24 \times 24$ transfer matrix $T_\alpha$ has spectral radius $\rho(T_{1/2}) = \mathbf{1/\sqrt{2} = 0.707106781187 < 1}$ (`|\rho^2 - 1/2| = 1.33e-15`) with **complex leading eigenvalues**, forcing $\mathcal{Z}_{\eta, 1/2}(n)$ to decay as $2^{-n/2}$ **and oscillate in sign** (`+0.0009` at $n=14$, `-0.0027` at $n=17$, `+0.0046` at $n=18$, negative again at $n=40, 100$), so normalized expectation ratios $O_{\eta, 1/2}(n)$ **do not converge** (repeated near-zero denominator crossings drive wild excursions `|\Delta\ln| = 3.51` at $n=14$). For $\alpha = 1$, $\rho(T_1) = \mathbf{0.728399602070 < 1}$, likewise giving exponential bulk cancellation. On mirror-closed ensembles, $\eta_A(P W P, P w) = -\eta_A(W, w)$ (`0.0` exact on automaton) couples directly to CP-odd $J_{\mathrm{CP}}$. | **Confirmed (non-convergence of normalized ratios proved)** |
| **Part 2 (`M34` Q2): Dynamic odd-tick cancellation in $\{L, R\}^n P$ ($\det M_W = -1$)** | Expected orientation-reversing deck reflection on the orientable double cover $T^2_{M_W^2}$ to force $\eta_A(T^2_{M_W^2}, w) = 0$ identically, so continuous `B1929` phases give $+1$ and do **not** cancel odd ticks without an extra discrete $\mathrm{Pin}^-$ factor $\pm i$. | **Confirmed on 100% of odd-tick histories:** Across exhaustive $n = 1..14$, an odd-tick word $M_{\mathrm{odd}} = M_0 P$ admits an order-5 character ($M_{\mathrm{odd}} w \equiv \mp w \pmod 5$) **if and only if** $5 \mid \operatorname{tr}(M_{\mathrm{odd}})$ (`0` mismatches; `0` characters for $n = 1..4$ including `m000` $= LP$, positive counts `80, 96, 224, 512, 1008, ...` for $n \ge 5$). Across all `1,920` surviving odd-tick Siegel histories in $n = 5..9$, individual half-steps carry non-zero winding up to `1.6180` rad, **but** the orientation-reversing second half-step cancels the first to `9.33e-15`, giving $\max |\eta_A(T^2_{M_{\mathrm{odd}}^2}, w)| = 1.903 \times 10^{-12}$ and $\langle e^{i\alpha\pi\eta_A}\rangle_{\mathrm{odd}} = 1.000000$. Pure `B1929` $\eta_A$ phases do **not** dynamically cancel odd ticks. | **Exact match** |
| **Part 3 (`M34` Q3): Does move-count vs hyperbolic area (`~0.52` in $\ln$) dissolve?** | Expected **NO**: neither twisted-$\eta$ phases nor one-loop Selberg weights $\|\det(I - M_W)\|^{-1/2}$ dissolve the Bowen–Margulis vs Weil–Petersson measure gap. | **Confirmed NO:** At exhaustive $n = 14$ (`exact_T90`), unweighted move-count sits at $\max |\Delta\ln| = 0.5091$ (`W_-` rms `0.4063`) from hyperbolic area (`\ell`-weighted `0.5247`). Including the one-loop Selberg/Reidemeister weight $\|\det(I - M_W)\|^{-1/2} = \|\operatorname{tr}(M_W) - 2\|^{-1/2}$ shifts move-count toward area by only `0.0645` in $\ln$, leaving **89% of the gap intact** (`\max |\Delta\ln| = 0.4604`, rms `0.3634`). Multiplying by $\cos(\frac{\pi}{2}\eta_A)$ or $\cos(\pi\eta_A)$ **blows the gap open** (`3.5094` and `1.1090` at $n = 14$) because the denominator $\mathcal{Z}_\eta(n)$ cancels toward zero faster than observable numerators. | **Exact match** |

---

## 2. Part 0 (`P-860 (a)`): Level-25 Weil Monodromy Obstruction & Canonical Gramian Resolution

### 2.1 Why No Level-5 Flat Unitary Connection Exists for Up-Quark Linear Summation

In `verify_a2_amp.py` (`run_part0_p860a_connection`, 45-digit `mpmath`), we extract the exact modular transformation law of the Frame C Yukawa matrices $Y_f(\tau, w)$ across all 24 order-5 points $w = (w_1, w_2) \in \frac{1}{5}\mathbb{Z}^2 \setminus \mathbb{Z}^2$ at $\tau_0 = 0.13 + 1.70 i$:
$$Y_f(\gamma \tau, w) = \phi_f(\gamma, w) \, U_L(\gamma) \, Y_f(\tau, w \gamma) \, U_{R,f}(\gamma)^\dagger, \qquad \gamma \in \mathrm{SL}_2(\mathbb{Z}),$$
where:
1. The left and right unitary flavor matrices $U_L(\gamma), U_{R,f}(\gamma) \in \mathrm{U}(3)$ depend **only** on $\gamma$ and $\tau$ (completely independent of $w \in E[5]\setminus\{0\}$, verified to pointwise matrix residual `2.36e-45` for up quarks and `1.18e-45` for down quarks).
2. Crucially, $U_L(\gamma)$ is **shared identically** between the up and down sectors (same $q_Q = +1$ left-handed doublet basis), whereas $\phi_f(\gamma, w) \in \mathrm{U}(1)$ is a **$w$-dependent scalar Weil/metaplectic phase**.

To test whether *any* flat unitary connection over the modular curve $X(5) = \Gamma(5) \backslash \mathbb{H}^*$ can render a linear coherent sum $\sum_{w} C_f(w) Y_f(\tau, w)$ covariant, we act with $T^5 = \begin{pmatrix} 1 & 5 \\ 0 & 1 \end{pmatrix} \in \Gamma(5)$. Because $T^5$ lies in the principal congruence subgroup $\Gamma(5)$, it acts **trivially** on every order-5 torsion point ($w T^5 \equiv w \pmod 1$) and represents a closed loop around the $\infty$-cusp of $X(5)$:

| Sector | Hypercharge quadratic sum $q_L^2 + q_R^2$ | $\arg \phi_f(T^5, w) / (2\pi)$ by stratum $\|5 w_1\| \in \{0, 1, 2\}$ | Naive linear sum $\|\Delta\ln\|$ under $T$ ($\tau+1$) | Naive linear sum $\|\Delta\ln\|$ under $T^5 \in \Gamma(5)$ | Naive linear sum $\|\Delta\ln\|$ under $T^{25} \in \Gamma(25)$ |
|---|---|---|---|---|---|
| **Down** ($q_Q = 1, q_d = 2$) | $1^2 + 2^2 = \mathbf{5} \equiv 0 \pmod 5$ | `{0: 0.0, 1: 0.0, 2: 0.0}` (spread `0.0`) | `0.0265` (reduced) / `0.6887` (unreduced) | `1.226e-44` | `2.487e-44` |
| **Up** ($q_Q = 1, q_u = -4$) | $1^2 + (-4)^2 = \mathbf{17} \equiv 2 \pmod 5$ | `{0: 0.0, 1: +0.4, 2: -0.4}` (spread `0.0`) | `0.6141` (reduced) / `0.5904` (unreduced) | **`0.5154`** (`1.4337` unreduced) | `1.314e-45` |

- **Down sector:** Because $q_Q^2 + q_d^2 = 5 \equiv 0 \pmod 5$, the $T^5$ Weil monodromy is trivial on all three $|5w_1|$ strata (`1.23e-44`). Integrating the 1-cocycle along the $T$-orbits yields an explicit constant scalar phase table $c_{\mathrm{down}}(w) \in \mathrm{U}(1)$ on $E[5]\setminus\{0\}$ such that $\sum_w c_{\mathrm{down}}(w) Y_{\mathrm{down}}^{\mathrm{red}}(\tau, w)$ is invariant under $\tau \to \tau + 1$ to `5.938e-44`.
- **Up sector (the exact obstruction):** Because $q_Q^2 + q_u^2 = 17 \equiv 2 \not\equiv 0 \pmod 5$, $T^5 \in \Gamma(5)$ multiplies the three $|5w_1|$ strata $\{0, 1, 2\}$ by **three distinct fifth roots of unity** $\{1, e^{+4\pi i/5}, e^{-4\pi i/5}\}$:
  $$\exp\!\left(-\pi i \cdot 5 \cdot (1^2 + (-4)^2) w_1^2\right) = \exp\!\left(-85\pi i w_1^2\right) = \exp\!\left(+\frac{4\pi i}{5} (5 w_1)^2\right) \in \{1, e^{+4\pi i/5}, e^{-4\pi i/5}\}.$$
  Because $T^5$ fixes every point $w \in E[5]$ individually while multiplying different $w$-strata by distinct fifth roots of unity, **no $\tau$-independent unitary gauge or parallel-transport table on $X(5)$ can absorb $\phi_{\mathrm{up}}(T^5, w)$**; the linear sum closes only on the level-25 modular curve $X(25)$ ($T^{25} \in \Gamma(25)$ drift `1.314e-45`).

### 2.2 Canonical Resolution (`0` Connection Choices): The Left-Handed Hermitian Gramian $\mathcal{H}_{L,f}(\tau)$

In quantum field theory, integrating out or tracing over internal boundary sectors of right-handed labels produces the **Hermitian self-energy / mass-squared operator** on the shared left-handed quark doublet bundle:
$$\mathcal{H}_{L,f}(\tau) := \frac{1}{24} \sum_{w \in E[5]\setminus\{0\}} Y_f(\tau, w) \, Y_f(\tau, w)^\dagger \qquad (f \in \{\mathrm{up}, \mathrm{down}, \mathrm{lep}\}).$$
Under **every** $\gamma \in \mathrm{SL}_2(\mathbb{Z})$, both the scalar Weil phase ($|\phi_f(\gamma, w)|^2 = 1$) and the right-handed flavor unitary ($U_{R,f}(\gamma)^\dagger U_{R,f}(\gamma) = I_3$) cancel term-by-term, while $w \mapsto w\gamma$ permutes $E[5]\setminus\{0\}$ bijectively:
$$\mathcal{H}_{L,f}(\gamma \tau) = U_L(\gamma) \, \mathcal{H}_{L,f}(\tau) \, U_L(\gamma)^\dagger \qquad \forall \gamma \in \mathrm{SL}_2(\mathbb{Z}).$$
Verified at 45-digit precision (`verify_a2_amp.json` `canonical_gramian_SL2Z_covariance`):
1. **Exact full-$\mathrm{SL}_2(\mathbb{Z})$ invariance (`0` choices, `0` bits):** Across all 7 read-out positions (`W_-` and `W_+`) and Jarlskog $J_{\mathrm{CP}}$, $\mathcal{H}_{L,f}(\tau)$ is invariant under $T: \tau \to \tau + 1$, $T^5: \tau \to \tau + 5$, and $S: \tau \to -1/\tau$ to `float64` machine exactness (`0.0` after rounding from `< 1e-43` in 45-dps `mpmath`).
2. **Exact CKM unitarity:** Diagonalizing $\mathcal{H}_{L,\mathrm{up}} = U_u \operatorname{diag}(m_{u,i}^2) U_u^\dagger$ and $\mathcal{H}_{L,\mathrm{down}} = U_d \operatorname{diag}(m_{d,j}^2) U_d^\dagger$ yields a genuinely unitary $3 \times 3$ CKM matrix $V_{\mathrm{CKM}}^{\mathrm{Gram}} = U_u^\dagger U_d$ (`||V V^\dagger - I_3||_F = 2.012e-45`), eliminating the non-unitarity (`37/72` rows/columns $\neq 1$) of incoherent modulus averaging $\frac{1}{24}\sum_w |V(w)|$, with non-vanishing interior CP violation $J_{\mathrm{CP}}(W_-) = +3.1410 \times 10^{-6}$ at $\tau_0 = 0.13 + 1.70 i$.
3. **High-cusp (`y = 30`) structural check (independent confirmation of `B1946` at operator level):** Evaluating $\mathcal{H}_{L,f}(0.13 + 30i)$ at 150-digit working precision (`unitarity_err = 4.27e-126`), mixed Higgs world $W_- = (\tilde{S}, S)$ still gives $|V_{33}^{\mathrm{Gram}}| = 8.876 \times 10^{-21}$ (**DERANGED**), whereas aligned $(S, S)$ gives $|V_{33}^{\mathrm{Gram}}| = 1.000000$ (**ALIGNED**). Thus the high-cusp mixing derangement is strictly a property of pairing orthogonal Higgs channels $(\tilde{S}, S)$, not an artifact of incoherent 24-point averaging.
4. **Guardrail 3 (`CTL-AMP-3`):** Independent random Haar $\mathrm{SU}(3)$ basis scrambles $Y_f(w) \mapsto U_L Y_f(w) U_{R,f}^\dagger$ leave all 7 Gramian observables and $J_{\mathrm{CP}}$ invariant (`0.0` drift in `float64`, `< 1e-43` in `mpmath`), while immediately catching the planted non-physical left-right overlap $|U_u^\dagger V_u|$ (`min drift = 0.2837`).

---

## 3. Part 1 (`M34` Q1): Exact 24-State Meyer–Siegel Automaton, Transfer Spectra & `P-846` Hand Coupling

### 3.1 Exact Finite-State Integer Cocycle & Word-by-Word Geodesic Cross-Check

Because Kubert–Lang's principal-branch series $L_a(z) = \log g_a(z)$ (`a in [0, 1)^2 \ {0}`) has **no branch cuts anywhere on $\mathbb{H}$**, for each generator $\gamma_k \in \{L^T, R^T\}$ and each non-zero order-5 point $b \in E[5]\setminus\{0\}$ the step difference
$$c(\gamma_k, b) := L_b(\gamma_k z_*) - L_{(b \gamma_k) \bmod 1}(z_*)$$
is **strictly independent of $z_* \in \mathbb{H}$** (`max |c(z_1) - c(z_2)| = 4.050e-50` at 50 dps) and satisfies
$$15 \, \Delta\eta_A(\gamma_k, b) = -\frac{30}{\pi} \operatorname{Im} c(\gamma_k, b) \in \mathbb{Z} \qquad (\text{max integrality residual } 1.604 \times 10^{-49}\text{ at 50 dps}).$$
Telescoping along any word $M_W = X_{n-1}\cdots X_0$ ($\gamma = M_W^T = X_0^T \cdots X_{n-1}^T$) that preserves $w_{\mathrm{mark}} = (2/5, 4/5)$ up to sign gives an exact $O(n)$ integer automaton for $\eta_A(M_W, w_{\mathrm{mark}}) \in \frac{1}{15}\mathbb{Z}$. Across all `1,357` hyperbolic `keeps_mark` words of lengths $n = 4..13$, the integer automaton matches continuous adaptive hyperbolic-geodesic Kubert–Lang winding to `6.994e-14` (`max |Re \Delta| = 1.809e-13`; straight-chord independence `2.816e-13`).

### 3.2 Exact $24 \times 24$ Transfer Matrix Spectra & Non-Convergence of Normalized Twisted-$\eta$ Ratios

Forming the $24 \times 24$ transfer operator $(T_\alpha)_{b, b'} = \frac{1}{2}\sum_{\gamma_k \in \{L^T, R^T\}: b\gamma_k \equiv b'} \exp\!\big(i \alpha \pi \Delta\eta_A(\gamma_k, b)\big)$ determines the exact $n \to \infty$ asymptotics of the twisted-$\eta$ partition sum:
- **Half-phase $\alpha = 1/2$ ($\chi_\eta = e^{i\frac{\pi}{2}\eta_A}$, standard APS $\frac{i\pi}{2}\eta$ weighting):**
  $$\rho(T_{1/2}) = \frac{1}{\sqrt{2}} = 0.707106781187 < 1 \qquad \big(|\rho^2 - 1/2| = 1.332 \times 10^{-15}\big),$$
  with **complex conjugate leading eigenvalues**, so the real partition sum $\mathcal{Z}_{\eta, 1/2}(n) = \langle \cos(\frac{\pi}{2}\eta_A)\rangle_n$ **decays exponentially at rate $2^{-n/2}$ AND oscillates in sign infinitely often**:

  | $n$ | `keeps_mark` words | $\operatorname{Var}(\eta_A)$ | $\mathcal{Z}_{\eta, 1/2}(n) = \langle \cos(\frac{\pi}{2}\eta_A)\rangle$ | $\mathcal{Z}_{\eta, 1}(n) = \langle \cos(\pi\eta_A)\rangle$ |
  |---:|---:|---:|---:|---:|
  | `6` | `5` | `0.4580` | `+0.2618` | `-0.2854` |
  | `8` | `21` | `0.6305` | `+0.3125` | `+0.0725` |
  | `10` | `85` | `0.9422` | `+0.1626` | `+0.0418` |
  | `12` | `345` | `1.2661` | `-0.0049` | `-0.0035` |
  | `14` | `1,325` | `1.6684` | `+0.0009` | `-0.0083` |
  | `16` | `5,453` | `1.9319` | `+0.0094` | `+0.0019` |
  | `17` | `10,976` | `2.0774` | `-0.0027` | `-0.0048` |
  | `18` | `21,865` | `2.2346` | `+0.0046` | `-0.0017` |

- **Full-phase $\alpha = 1$ ($\chi_\eta = e^{i\pi\eta_A}$):** $\rho(T_1) = 0.728399602070 < 1$, likewise producing exponential cancellation toward zero (`\operatorname{Var}(\eta_A)` grows linearly at `~0.148` per letter).
- **Consequence for normalized read-out ratios $O_\eta(n) = \big(\sum_W \chi_\eta O(W)\big)/\big(\sum_W \chi_\eta\big)$:** Because the denominator $\sum_W \cos(\alpha\pi\eta_A)$ decays exponentially while changing sign (`-0.0049` at $n=12$, `+0.0009` at $n=14$, `-0.0027` at $n=17$), dividing by $\mathcal{Z}_\eta(n)$ amplifies finite-$n$ fluctuations into unphysical negative mass ratios and CKM moduli $> 3$ (`verify_a2_amp.json` `observable_convergence_and_part3_area_gap`). Normalized twisted-$\eta$ history expectations **do not converge** as $n \to \infty$.
- **Orientation-reversal symmetry & `P-846` Hand / Jarlskog coupling:** Under the mirror involution $(W, w) \mapsto (P W P, P w)$, $\eta_A(P W P, P w) = -\eta_A(W, w)$ holds identically (`0.0` error across all `n <= 14`), so on the full 24-point closed-orbit population $\operatorname{Im}\mathcal{Z}_\eta(n) = \langle \sin(\frac{\pi}{2}\eta_A)\rangle = 0$ (`-5.72e-18` at $n=10$, `0.0` at $n=12`; planted sign-flip control `CTL-AMP-1` gives `0.2353 -> CAUGHT`). Pointwise CP-odd Jarlskog $J_{\mathrm{CP}}$ also flips sign under mirror conjugation, so $\sin(\frac{\pi}{2}\eta_A) J_{\mathrm{CP}}$ is **mirror-even**: on the 42-history mirror-closed $n = 8$ geodesic ensemble (12-node midpoint quadrature), $\langle \sin(\frac{\pi}{2}\eta_A) J_{\mathrm{CP}} \rangle_{W_-} = -1.6659 \times 10^{-5}$ (`W_+`: $+1.6560 \times 10^{-6}$), whereas the unweighted mirror sum cancels down to the 12-node midpoint discretization floor (`-5.900e-06`).

---

## 4. Part 2 (`M34` Q2): Odd-Tick `{L, R}^n P` Trace Theorem & Exact Double-Cover Vanishing

For odd-tick words $M_{\mathrm{odd}} = M_0 P$ ($M_0 \in \{L, R\}^n$, $\det M_{\mathrm{odd}} = -1$, $\operatorname{tr}(M_{\mathrm{odd}}) \ge 1$ strictly hyperbolic):
1. **Exact trace-divisibility criterion (`0` mismatches across exhaustive $n = 1..14$):** Because $\det(M_{\mathrm{odd}} \pm I_2) = -1 \pm \operatorname{tr}(M_{\mathrm{odd}}) + 1 = \pm \operatorname{tr}(M_{\mathrm{odd}})$, an odd-tick bundle admits a non-zero order-5 character ($M_{\mathrm{odd}} w \equiv -w \pmod 5$ orientation-twisted or $+w \pmod 5$ untwisted) **if and only if** $5 \mid \operatorname{tr}(M_{\mathrm{odd}})$.
   - For $n = 1, 2, 3, 4$ (including the Gieseking root `m000` $= LP$, $\operatorname{tr}(LP) = 1$), $\max \operatorname{tr}(M_{\mathrm{odd}}) \le 4 < 5$, so **zero** order-5 characters survive on `m000` or any $n \le 4$ odd-tick bundle.
   - From $n = 5$ upward, surviving `(twisted, untwisted)` character pairs grow exponentially: `(40, 40)` at $n=5$, `(48, 48)` at $n=6$, `(112, 112)` at $n=7$, `(256, 256)` at $n=8$, `(504, 504)` at $n=9$, ..., `(15792, 15792)` at $n=14$.
2. **Exact vanishing of $\eta_A$ on the orientable double cover $T^2_{M_{\mathrm{odd}}^2}$:** Across all `1,920` surviving odd-tick Siegel histories in $n = 5..9$, a single glide-reflection half-step carries non-zero Kubert–Lang winding up to `1.6180` rad, **but** the deck involution $M_{\mathrm{odd}}$ reverses fibre orientation on the second half-step so the two half-steps sum to zero (`9.326e-15`), giving
   $$\max_{5 \le n \le 9} \big|\eta_A(T^2_{M_{\mathrm{odd}}^2}, w)\big| = 1.903 \times 10^{-12}, \qquad \big\langle e^{i\alpha\pi\eta_A}\big\rangle_{\mathrm{odd}} = 1.000000.$$
   Hence **continuous `B1929` $\eta_A$ phases alone do not cancel odd ticks**; dynamic odd-tick cancellation requires a discrete non-orientable $\mathrm{Pin}^-$ / Dai–Freed cobordism fourth-root factor ($\pm i$) beyond `B1929`'s orientable torus formula.

---

## 5. Part 3 (`M34` Q3): Move-Count vs Hyperbolic Area Measure Gap (`n = 14` Exhaustive, `exact_T90`)

Comparing all six closed-geodesic weighting schemes at exhaustive word length $n = 14$ (`1,325` `keeps_mark` words) against `agy-002`'s untruncated hyperbolic-area reference (`verify_a2_canon_results.json`, `exact_T90`):

| Closed-geodesic weighting at $n = 14$ | `W_-` max $\|\Delta\ln\|$ vs Area | `W_-` rms $\|\Delta\ln\|$ vs Area | `W_+` max $\|\Delta\ln\|$ vs Area | `W_+` rms $\|\Delta\ln\|$ vs Area |
|---|---:|---:|---:|---:|
| Move-count ($\ell$-weighted, `B1932`/`B1940` convention) | `0.5247` | `0.4203` | `0.5146` | `0.4243` |
| Move-count (uniform word weight) | `0.5091` | `0.4063` | `0.5011` | `0.4103` |
| One-loop Selberg $\|\det(I - M_W)\|^{-1/2} = \|\operatorname{tr}(M_W) - 2\|^{-1/2}$ | `0.4604` | `0.3634` | `0.4587` | `0.3671` |
| Twisted-$\eta$ ($\cos(\pi \eta_A)$) | `1.1090` | `0.6176` | `1.2761` | `0.8126` |
| Selberg $\times \cos(\frac{\pi}{2}\eta_A)$ | `1.8718` | `1.1136` | `4.2732` | `2.0398` |
| Twisted-$\eta$ ($\cos(\frac{\pi}{2}\eta_A)$) | `3.5094` | `2.6767` | `3.2991` | `2.3927` |

**Conclusion on Q3:** Neither `B1929`'s twisted-$\eta$ phase nor the one-loop Selberg/Reidemeister determinant factor dissolves the `~0.52` log-gap between move-count (Bowen–Margulis topological entropy measure, cusp weight `0`) and hyperbolic area (Weil–Petersson/Poincaré measure, cusp weight `~9%` above $y = 11$).

0 of 19.
