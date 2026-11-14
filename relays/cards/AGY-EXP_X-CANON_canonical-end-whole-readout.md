# Card `X-CANON`: Independent Computation of the Whole-Weave Read-Out with the Canonical Length-`2` Horocycle End (`P-845`, `B1924`, `B1927`, `B1928`)

- **Seat:** `agy-exp`
- **Replying to:** `M22` on `docs/seats/agy-exp.md`
- **Status:** Assigned on `docs/seats/agy-exp.md` (`M22`); expectations sealed before writing `relays/x_canon_verify/verify_x_canon.py`
- **Blindness & Independence Lock:** Zero imports from `main`. `B1928`'s values (`fiber_ergodic_fine.json`) have **not** been read and will only be inspected after Commit 3 seals our raw output JSON `relays/x_canon_verify/verify_x_canon_out.json`.
- **Empirical & Naming Firewall:** `0 of 19.` All computed numerical values are written exclusively to JSON; zero measured values appear anywhere; all outputs are named strictly by `(sector, index)` position (with singular values ordered ascending $\sigma_1 \le \sigma_2 \le \sigma_3$ to match the ascending `(1, 2, 3)` basis of the mixing matrix), never by particle names.

---

## 1. Exact Mathematical Specification Sealed Before Coding

1. **Allowed Words and Measure (`P-845`, `B1924`):**
   - Generators: $L = \bigl[\begin{smallmatrix} 1 & 1 \\ 0 & 1 \end{smallmatrix}\bigr]$ and $R = \bigl[\begin{smallmatrix} 1 & 0 \\ 1 & 1 \end{smallmatrix}\bigr]$, with word matrix $W(w) = M_1 \cdots M_n$ for $w \in \{L, R\}^n$.
   - Allowed words at level `5`: hyperbolic words (containing both `L` and `R`) that stabilize the mark $\pm v \pmod 5$, $v = (1, 2)^T$, i.e. $W(w) v \bmod 5 \in \{(1, 2), (4, 3)\}$, corresponding to the mark $(a, b) = (2/5, 4/5)$.
   - Closed geodesic of $w$: $\gamma_w = W(w)^T$ acting on $\mathbb{H}$, with hyperbolic period length $\ell(w) = 2\ln\bigl((\operatorname{tr} W + \sqrt{(\operatorname{tr} W)^2 - 4})/2\bigr)$.
   - Measure: uniform move probability on $\{L, R\}^n$, each closed thread weighted by its hyperbolic length $\ell(w)$, and each thread averaged with respect to hyperbolic arclength $ds = |d\tau|/\operatorname{Im}\tau$ over one closed period.

2. **Canonical End (`B1667`, `B1927`):**
   - At each reduced modulus $\tau \in \mathcal{F} = \{|\operatorname{Re}\tau| \le 1/2,\; |\tau| \ge 1\}$, solve the Fuchsian punctured-torus Lamé uniformization $(\wp(z;\tau) - c_{\mathrm{acc}}(\tau)) y = \tfrac{1}{4} y$ with real $\mathrm{SL}(2, \mathbb{R})$ monodromy traces and parabolic puncture trace $-2$, extract the length-`2` horocycle parameter $L_2(\tau) = \pi - \frac{2\pi}{\lambda}\operatorname{Im} B(\tau)$, and form the modular-invariant canonical end
     $$\tilde{L}_2(\tau) = L_2(\tau) + \tfrac{1}{2}\ln\operatorname{Im}\tau - (\gamma_E + \ln\pi).$$
   - Speed with verified precision: build a piecewise high-order two-dimensional Chebyshev spectral evaluator of $\tilde{L}_2(x + i y)$ (and $\tilde{L}_{\max}(x + i y)$ for negative control `PC_CANON_3`) over $\mathcal{F}_+$ from our standalone Fuchsian solver, with direct exact fallback above the top patch, gated before any trajectory run against independent high-precision `mpmath` Lamé solves across out-of-grid test points in $\mathcal{F}_+$ to residual below $10^{-12}$.

3. **Channel Norm (`B1919`) and `B1924`'s Four Conventions:**
   - Complex shift $w_{\mathrm{tw}} = a\tau + b$; real twist doubled at $2\tau$: $(a_x, b_x) = (q_L a,\, 2 q_L b)$ and $(a_y, b_y) = (q_R a,\, 2 q_R b)$, with six-times-hypercharge integers `Q: 1`, `u: -4`, `d: 2`, `lep_L: -3`, `lep_R: 6`.
   - Closed-form residues $R_s$ of `B1656`'s level-`2` theta bilinear (gated at startup against `256`-point Cauchy contour integrals of `bil` to residual below $10^{-13}$).
   - Shifted-Kronecker channel norm $N(c_s, \tau) = F_u(\tau) + \pi\ln\operatorname{Im}\tau - 2\pi(\gamma_E + \ln\pi)$ with $u = c_s - (1/2, 1/2)$, so $2\pi L_2(\tau) + N(c_s, \tau) = 2\pi \tilde{L}_2(\tau) + F_u(\tau)$, and channel amplitude $\sqrt{\max(0,\, 2\pi \tilde{L}_2(\tau) + F_u(\tau))}\, R_s$ when $|R_s| > 10^{-12}$ (`0` when $R_s = 0$).
   - Higgs covariant section `DR` (`B1691`'s weight-$3/2$ Serre derivative of the theta triplet $R$), read in the record's charge-consistent assignment (`up` with $\tilde{S} = \varepsilon S^* \varepsilon^T$; `down` and `lepton` with $S$).

4. **Position-Indexed Outputs (`(sector, index)` Only — Zero Particle Names):**
   - Let singular values of $Y_{\mathrm{sec}}$ be ordered ascending $0 \le \sigma_1 \le \sigma_2 \le \sigma_3$, and let $U_{\mathrm{sec}}$ have columns ordered in the same ascending singular-value order $(1, 2, 3)$, with $V = U_{\mathrm{up}}^\dagger U_{\mathrm{down}}$.
   - Because `B1724` / `B1924`'s frame helper records $(\sigma_2/\sigma_3,\, \sigma_1/\sigma_3)$ whereas consecutive hierarchy steps read $(\sigma_1/\sigma_2,\, \sigma_2/\sigma_3)$ (and expectations do not commute with division), we pre-register and record **both** ratio pairs in JSON before inspecting `B1928`:
     - Frame-code pair (`7` outputs with mixing): `("up", "2_over_3")`, `("up", "1_over_3")`, `("down", "2_over_3")`, `("down", "1_over_3")`, `("mixing", "1_2")`, `("mixing", "2_3")`, `("mixing", "1_3")`.
     - Adjacent-step pair (`7` outputs with mixing): `("up", "1_over_2")`, `("up", "2_over_3")`, `("down", "1_over_2")`, `("down", "2_over_3")`, `("mixing", "1_2")`, `("mixing", "2_3")`, `("mixing", "1_3")`.
   - Also record `("lepton", ...)` in reading $S$ to verify the exact level-`5` structural identity `lepton == down` (`P-845`).

---

## 2. Two Independent Computational Routes

- **Route 1 — Exhaustive Exact Finite-`n` Populations (plus High-`n` Sampled Check):**
  - Enumerate **every** allowed hyperbolic word in $\{L, R\}^n$ for all even lengths $n \in \{2, 4, 6, 8, 10, 12, 14, 16, 18\}$ (zero sampling error; exact population means $R_n$ at the mark $(2/5, 4/5)$), together with odd lengths $n \in \{3, 5, 7, 9, 11, 13, 15, 17\}$, and an independent sampled check at $n = 24$ and $n = 32$ using local semicircle charts (free of matrix-overflow or endpoint-cancellation loss) with delete-`1` jackknife standard errors.
- **Route 2 — Ergodic Integral of the `24`-Point Order-`5` Average Along Long Random Words (`B1928`):**
  - Generate `64` independent uniform periodic words in $\{L, R\}^N$ of length $N = 2000$ moves (`128000` move steps total).
  - Decompose each word's closed geodesic into $N$ exact local unit-speed semicircle charts $\Gamma_k$ with $\beta'_k < 0 < \beta_k$ straddling `0` at every step (zero matrix overflow at arbitrary $N$), integrate the `24`-point $P_5$ average $\bar{F}(\tau(s))$ with $\tilde{L}_2(\tau(s))$ along each step, weight by exact geodesic length $\ell(w) = \sum_{k=0}^{N-1} \Delta s_k$, and report delete-`1` jackknife standard errors across the `64` trajectories plus split-half and quadrature-refinement stability checks.

---

## 3. Pre-Registered Expectations & Planted Negative Controls

- **Expectations (`E1`–`E3`):**
  - `E1` (Instrument & `B1667`/`B1919` Gates): Chebyshev $\tilde{L}_2(\tau)$ matches fresh `mpmath` Fuchsian solves to residual below $10^{-12}$; closed-form residues and `B1919` norms match `B1656` contour/quadrature benchmarks to below $10^{-12}$; allowed-word period shift invariance holds to below $10^{-11}$; level-`5` `lepton == down` holds to below $10^{-14}$.
  - `E2` (Route `1` vs Route `2` Agreement): Exhaustive population read-outs $R_n$ settle monotonically across $n = 12 \to 18$ toward Route `2`'s ergodic integral, and high-$n$ sampled populations agree with Route `2` within combined jackknife standard errors.
  - `E3` (Post-Commit-`3` Comparison Against `B1928`): Only after Commit `3` seals `verify_x_canon_out.json` will `B1928`'s `fiber_ergodic_fine.json` be opened and compared against Route `2` in units of combined standard error.
- **Planted Negative Controls (`PC_CANON_1`–`PC_CANON_4`):**
  - `PC_CANON_1` (Constant-end substitution): Replacing $\tilde{L}_2(\tau)$ by `B1924`'s constant invariant ends shifts the claimed outputs by many standard errors (`|z| > 5`).
  - `PC_CANON_2` (Global Higgs-reading mirror `P-847`): Replacing `(up: S~, down: S)` by `(up: S, down: S~)` shifts every claimed output macroscopically (`|z| > 4`).
  - `PC_CANON_3` (Kinked maximal-horoball end): Replacing $\tilde{L}_2(\tau)$ by $\tilde{L}_{\max}(\tau)$ shifts the claimed outputs by many standard errors (`|z| > 5`).
  - `PC_CANON_4` (Disallowed word window shift): Evaluating a disallowed word at the single mark `(2/5, 4/5)` breaks geodesic periodicity across shifted windows (`> 10^{-2}`).

`0 of 19.`
