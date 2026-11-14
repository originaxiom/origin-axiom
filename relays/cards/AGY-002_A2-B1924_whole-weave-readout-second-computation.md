# Card A2-B1924: Independent Second Computation of `B1924` Whole-Weave Read-Out (`M23` + `M25`)

- **Seat:** `agy-002` (`origin/agy-002/verify`)
- **Messages:** `M23`, `M24` (queue item two, priority blocker for the read-out), `M25` (three fixed coordinate-end constants)
- **Point Register:** `P-845` (whole-weave read-out condition; second independent computation before `B1924` leaves `CANDIDATE`)
- **Code & Output Blindness:** Strictly enforced. Neither `frontier/B1924*/*.py` nor `frontier/B1924*/*.json` has been read prior to committing this card and running our standalone code. Zero shared code with `main`.

---

## 1. Mathematical Specification (Locked Before Running)

1. **Allowed Words and Stabiliser Condition (`P-845`, `M23`):**
   - Alphabet: positive move matrices $L = \begin{pmatrix}1 & 1\\ 0 & 1\end{pmatrix}$ and $R = \begin{pmatrix}1 & 0\\ 1 & 1\end{pmatrix}$ in $\operatorname{SL}_2(\mathbb{Z})$.
   - Under $\gamma \in \operatorname{SL}_2(\mathbb{Z})$ acting on the upper half-plane via $\tau \mapsto \frac{p\tau + q}{r\tau + s}$, the flat torsion line $w = a\tau + b$ transforms covariantly by $(a', b')\gamma \equiv (a, b) \pmod 1$.
   - A word $W \in \{L, R\}^n$ is **allowed** if and only if its matrix $\gamma_W$ stabilises the canonical eigenline modulo sign:
     $$(2, 4)\,\gamma_W \equiv \pm(2, 4) \pmod 5 \quad \Longleftrightarrow \quad (1, 2)\,\gamma_W \equiv \pm(1, 2) \pmod 5.$$
     Because $\operatorname{SL}_2(\mathbb{Z})$ acts transitively on the $24$ non-zero elements of $(\mathbb{Z}/5\mathbb{Z})^2$ and modulo sign there are $12$ cosets, the stabiliser $\Gamma_{\pm} \subset \operatorname{SL}_2(\mathbb{Z})$ has index **twelve**, so asymptotically one twelfth of all $2^n$ words in $\{L, R\}^n$ are allowed.
   - Note on parabolic words $L^{5k}, R^{5k}$: at $n = 16$ and $n = 22$, $5 \nmid n$, so neither $L^n$ nor $R^n$ is allowed; at $n = 10$, $L^{10}$ and $R^{10}$ have $\operatorname{tr} = 2$ and hyperbolic axis length $\ell = 0$, so under hyperbolic length-weighting $\ell(\gamma_W)$ they carry weight **zero** automatically (we record both the exact count of parabolic vs hyperbolic allowed words and exclude $\operatorname{tr} \le 2$ from closed-axis averages).

2. **Closed-Geodesic Axis Parametrisation and Period Quadrature:**
   - Every hyperbolic word $\gamma = \begin{pmatrix}p & q\\ r & s\end{pmatrix}$ with $t = p + s > 2$ has hyperbolic translation length:
     $$\ell(\gamma) = 2\operatorname{arccosh}\!\left(\frac{p + s}{2}\right) = 2\ln\!\left(\frac{t + \sqrt{t^2 - 4}}{2}\right) > 0,$$
     and real fixed points $x_\pm = \frac{(p - s) \pm \sqrt{t^2 - 4}}{2 r}$ on $\partial\mathbb{H}$ ($r \ge 1$ for every mixed word in $\{L, R\}^n$).
   - Its unit-speed hyperbolic geodesic axis is the semicircle:
     $$\tau(u) = \frac{x_+ + x_-}{2} + \frac{x_+ - x_-}{2}\,\tanh(u) + i\,\frac{|x_+ - x_-|}{2\,\cosh(u)}, \qquad u \in [0, \ell(\gamma)],$$
     where $ds = |d\tau| / \operatorname{Im}\tau = du$ identically!
   - **Critical Periodicity Note ($\gamma$ with $-1 \pmod 5$ sign flip):**
     - When $(a, b)\gamma \equiv +(a, b) \pmod 5$, all gauge-invariant Yukawa ratios and CKM moduli satisfy $O(\tau(u + \ell); a, b) = O(\tau(u); a, b)$ with period $\ell(\gamma)$ (since $O$ is invariant under $(a, b) \mapsto (-a, -b)$ as well! Let us verify directly in code that $(a, b) \mapsto (-a, -b)$ leaves all singular-value ratios and CKM moduli invariant to $< 10^{-13}$, so **both** $+(a, b)$ and $-(a, b)$ stabilizer words are strictly periodic with period $\ell(\gamma)$!).
   - **Numerical Quadrature Precision:**
     - Periodic midpoint / trapezoid rule on $u \in [0, \ell(\gamma))$ with $N_{\text{quad}} = \max(64, \lceil 24\,\ell(\gamma)\rceil)$ nodes (with a convergence check doubling $N_{\text{quad}}$ on sample words to assert quadrature error $< 10^{-8}$).
     - At every quadrature node $\tau(u)$, we pull $(\tau(u), a, b)$ back into the standard $\operatorname{SL}_2(\mathbb{Z})$ fundamental domain ($\operatorname{Im}\tau_{\text{red}} \ge \sqrt{3}/2$) via exact $\operatorname{SL}_2(\mathbb{Z})$ co-transformation (justified to $< 10^{-13}$ by `P-720` weight-zero invariance of all ratios and CKM moduli at fixed $L_{\text{coord}}$!), guaranteeing machine-precision $q$-series convergence even when a geodesic makes a deep cusp excursion.

3. **Paired Observables, Readings, Word Lengths, and Three Fixed Coordinate Ends (`M23` + `M25`):**
   - **Observables (averaged as direct ratios / moduli, NOT log-ratios):**
     - Six intra-sector mass ratios: $m_u/m_t, m_c/m_t, m_d/m_b, m_s/m_b, m_e/m_\tau, m_\mu/m_\tau \in [0, 1]$;
     - Nine CKM moduli $|V_{ij}| \in [0, 1]$ ($i \in \{u, c, t\}, j \in \{d, s, b\}$), evaluated in both `SEAT` Higgs-reading patterns `(S~, S, S)` and `(S~, S~, S~)` (so $6 \times 2 + 9 \times 2$ or $6$ per sector reading `S` and `S~` plus $9$ CKM in `(S~, S, S)` and `(S~, S~, S~)` — all reported explicitly).
   - **Paired Mark vs Twin Comparison:**
     - Mark: $(a, b) = (2/5, 4/5)$; Twin: $(a, b) = (1/5, 2/5)$, evaluated on the **exact same** allowed words $\gamma_W$, weighted by geodesic length $\ell(\gamma_W)$:
       $$\widehat{R}_{\text{mark}} = \frac{\sum_j \ell(\gamma_j)\,\overline{O}_{\text{mark}}(\gamma_j)}{\sum_j \ell(\gamma_j)}, \qquad \widehat{\Delta}_{\text{mark}-\text{twin}} = \frac{\sum_j \ell(\gamma_j)\,\big(\overline{O}_{\text{mark}}(\gamma_j) - \overline{O}_{\text{twin}}(\gamma_j)\big)}{\sum_j \ell(\gamma_j)},$$
       with delete-one-word **paired ratio jackknife** standard errors on both $\widehat{R}$ and $\widehat{\Delta}_{\text{mark}-\text{twin}}$.
   - **Word Lengths (`M23`):**
     - $n = 10$: **exact exhaustive census** of all $2^{10} = 1{,}024$ words (zero sampling error at $n = 10$!), testing short-history twin separation;
     - $n = 16$: **exact exhaustive census** of all $2^{16} = 65{,}536$ words to identify all allowed words, plus deterministic stratified / uniform draw of $M_{16} = 200$ allowed hyperbolic words (and check against a second disjoint seed);
     - $n = 22$: uniform draw of allowed hyperbolic words from $\{L, R\}^{22}$ with $M_{22} = 200$ allowed hyperbolic words (testing $n$-settling between $n = 16$ and $n = 22$ and twin fading at larger $n$).
   - **Three Coordinate-End Constants (`M25`):**
     - $L_{\text{coord}} = L + \frac{1}{2}\log\operatorname{Im}\tau = \widetilde{L} + \gamma + \log\pi$ held fixed at:
       1. **`1.30`** (`main`'s first `B1924` constant),
       2. **`0.90`** (`main`'s second `B1924` constant),
       3. **`2.20`** (`agy-002`'s independent third constant inside the canonical cusp's `0.69`–`2.99` band, well separated from `0.90` and `1.30`, corresponding to $\widetilde{L} = 2.20 - \gamma - \log\pi \approx +0.4781$).

---

## 2. Locked Expectations & Falsifiable Hypotheses

1. **Exact Allowed-Word Fraction & Periodicity (`H1`):**
   - At $n = 10$ and $n = 16$ (exhaustive), the fraction of words stabilising $\pm(2, 4) \pmod 5$ approaches $1/12 \approx 0.08333$.
   - Every allowed hyperbolic word has strictly periodic ratios/CKM moduli over $[0, \ell(\gamma)]$ (`|O(tau(ell)) - O(tau(0))| < 1e-12`), and doubling quadrature nodes shifts thread averages by `< 1e-8`.
2. **Short-History Twin Asymmetry at $n = 10$ vs Asymptotic Twin Fading at $n = 16, 22$ (`H2`):**
   - At $n = 10$ (exhaustive), mark $(2/5, 4/5)$ and twin $(1/5, 2/5)$ differ by multiple standard errors (because positive $\{L, R\}^{10}$ words are not invariant under the outer $\det = -1$ tick involution $J$ exchanging mark and twin);
   - As $n$ grows to $16$ and $22$, the paired difference $|\widehat{\Delta}_{\text{mark}-\text{twin}}|$ shrinks systematically toward zero across **all three** ends `0.90`, `1.30`, and `2.20` (provided both readings `S` and `S~` or their self-conjugate sector are compared — **AND we explicitly test whether in a single chiral reading `S` vs `S~` the twin converges to the SAME reading `S` OR to the conjugate reading `S~`!**).
3. **$n$-Settling vs End-Dependence (`H3`):**
   - Between $n = 16$ and $n = 22$, the length-weighted weave read-out settles within Monte Carlo jackknife uncertainty at each fixed $L_{\text{coord}}$, whereas varying $L_{\text{coord}}$ across `0.90 -> 1.30 -> 2.20` moves the read-out ratios monotonically and substantially (confirming `P-845`'s open status of the invariant end $\widetilde{L}$).
4. **Adversarial Planted Controls (`CTL-B1924-1..3`):**
   - `CTL-B1924-1`: Unpaired standard-error inflation vs paired jackknife SE on strongly correlated mark/twin observables;
   - `CTL-B1924-2`: Non-stabilised word (`RL`, which maps $(2, 4) \mapsto (1, 0) \pmod 5$) fails periodicity along its geodesic axis (`|O(tau(ell)) - O(tau(0))| >> 1e-3`);
   - `CTL-B1924-3`: Holding bare $L$ constant instead of $L_{\text{coord}} = L + \frac{1}{2}\log\operatorname{Im}\tau$ breaks $\operatorname{SL}_2(\mathbb{Z})$ pullback invariance along a geodesic period.

0 of 19.
