# agy-002 Pre-Run Expectations Card — Card A2-B1947 (`M40`): Standalone Second Computation of `B1947`'s `C2` ($\tau \to \tau + 1$ Covariance) Negative

- **Seat:** `agy-002` (`branch: agy-002/verify`)
- **Date:** 2026-11-15
- **Card:** `A2-B1947` (`M40` — after `A2-R83` pushed at `8603eca3c`, reproduce `B1947`'s negative from its card and amendment `A1` on standalone code, sealing expectations first and computing **no mixing**)
- **Repository files opened prior to sealing this card (complete blindness log):**
  1. `docs/seats/agy-002.md` (`M40`)
  2. `frontier/B1947_frame_d1s_coupling/CARD.md` (including `Amendment A1`)
  3. `relays/a2_smc13/verify_smc13_order5.py` (`agy-002`'s own standalone 55-digit Frame C coupling & Jacobi-theta engine)
  - **Not opened:** `frontier/B1947_frame_d1s_coupling/FINDINGS.md`, its JSON outcome summary, `verification/d1_coupling.py`, `verification/higgs_transport.py`, `d1_outputs.json`, `d1v2_outputs.json`, and all other seat branches.
- **Strict execution rules (`M40`):**
  1. **Compute no mixing** (`V = U_u^\dagger U_d` and `|V|` are strictly omitted everywhere in code and output).
  2. **Zero measured numbers touched**; physical ratio values stay strictly in `.json` only (`_out.txt` and `.md` report only dimensionless covariance drifts, analytical component-phase residuals, and control checks).

---

## 1. Exact Definitions Under Test (From `B1947/CARD.md` and `Amendment A1` Alone)

In Frame C (`exact_T90` channel weight, canonical end $L_2$, 24 non-zero points $w = (a, b) \in \frac{1}{5}\mathbb{Z}^2 \setminus \mathbb{Z}^2$), replace the untwisted Higgs $q$-series $S$ / $\tilde{S}$ by the Serre derivative of the charge-twisted weight-$(-1/2)$ triplet:
$$R(\tau; \delta\alpha, \delta\beta) = \left(-\frac{\theta_2}{\theta_3 \theta_4},\; -\frac{\theta_4}{\theta_2 \theta_3},\; i \frac{\theta_3}{\theta_2 \theta_4}\right), \qquad D R = q \frac{dR}{dq} + \frac{1}{24} E_2(\tau) R, \qquad S_{D1} = \sum_{k=0}^{2} (D R)_k Q_k,$$
with sector Higgs hypercharge $q_H = -(q_L + q_R)$ in $6Y$ units (`up`: $q_H = -(1 - 4) = +3$; `down`: $q_H = -(1 + 2) = -3$; `leptons`: $q_H = -(-3 + 6) = -3$), tested across **both shift conventions** and **both $\theta_4$ characteristic representatives**:

1. **Two shift conventions:**
   - **Convention `D1` (original card):** $(\delta\alpha, \delta\beta) = (q_H a,\; 2 q_H b)$.
   - **Convention `D1'` (`Amendment A1`):** $(\delta\alpha, \delta\beta) = (q_H a,\; q_H b)$.
2. **Two $\theta_4$ characteristic representatives:**
   - **Representative `+` (declared):** $\theta_2 = \theta[\frac{1}{2} + \delta\alpha,\; \delta\beta]$, $\theta_3 = \theta[\delta\alpha,\; \delta\beta]$, $\theta_4 = \theta[\delta\alpha,\; +\frac{1}{2} + \delta\beta]$.
   - **Representative `-` (other):** $\theta_2 = \theta[\frac{1}{2} + \delta\alpha,\; \delta\beta]$, $\theta_3 = \theta[\delta\alpha,\; \delta\beta]$, $\theta_4 = \theta[\delta\alpha,\; -\frac{1}{2} + \delta\beta]$.

---

## 2. Sealed Algebraic & Numerical Expectations Committed Before Running

1. **Check `C0` (Untwisted limit $q_H = 0$):**
   - At $q_H = 0$ (`\delta\alpha = \delta\beta = 0`), by Jacobi's triple-product identity $\theta_2 \theta_3 \theta_4 = 2 \eta(\tau)^3$ and $q \frac{d}{dq}(\eta^3) = \frac{1}{8} E_2 \eta^3$, $D R = q \frac{d}{dq}\!\left(\frac{N}{2\eta^3}\right) + \frac{1}{24} E_2 \frac{N}{2\eta^3} = \frac{q \, dN/dq}{2\eta^3} - \frac{1}{12} E_2 \frac{N}{2\eta^3}$ matches Frame C's untwisted `B1691` $B[1]$ $q$-series (`S` reading) to `< 1e-45` at 55-digit working precision, and satisfies `C2` ($\tau \to \tau + 1$ with $w \mapsto T \cdot w = (a, b - a)$) on mass ratios $(\sigma_1/\sigma_3, \sigma_2/\sigma_3)$ to `< 1e-45`.

2. **Check `C1` (Sign-flip phase relation $q_H = -3$ vs $q_H = +3$):**
   - Using $\theta[-\alpha, -\beta](\tau) = \theta[\alpha, \beta](\tau)$, $\theta_2$ and $\theta_3$ are strictly even under $(\delta\alpha, \delta\beta) \mapsto (-\delta\alpha, -\delta\beta)$, whereas $\theta_4$ shifts $\beta$ by $\mp 1$:
     $$\theta[\delta\alpha, \mp \tfrac{1}{2} + \delta\beta]\big|_{-\delta\alpha, -\delta\beta} = \theta[\delta\alpha, \pm \tfrac{1}{2} + \delta\beta] = e^{\pm 2\pi i \delta\alpha} \, \theta[\delta\alpha, \mp \tfrac{1}{2} + \delta\beta].$$
   - Hence for **both** `D1` and `D1'`, with $\phi = 2\pi \cdot 3 a$:
     - Under **Rep `+`**: $D R(-3) = \big(e^{+i\phi} D R_0(+3),\; e^{-i\phi} D R_1(+3),\; e^{+i\phi} D R_2(+3)\big)$ to `< 1e-45`.
     - Under **Rep `-`**: $D R(-3) = \big(e^{-i\phi} D R_0(+3),\; e^{+i\phi} D R_1(+3),\; e^{-i\phi} D R_2(+3)\big)$ to `< 1e-45`.

3. **Check `C2` ($\tau \to \tau + 1$ Covariance at $(\tau + 1, T \cdot w)$ vs $(\tau, w)$, $T \cdot w = (a, b - a)$):**
   - **Expected outcome: `NEGATIVE` (`FAILS C2`) for BOTH conventions (`D1` and `D1'`) and BOTH representatives (`Rep +` and `Rep -`)** on all 20 order-5 points with $a \not\equiv 0 \pmod 1$ ($a \in \{1/5, 2/5, 3/5, 4/5\} \implies q_H a = \pm 3a \notin \mathbb{Z}$), while holding accidentally on the 4 $a = 0$ points $(0, b)$ in `D1'` (and even on $a = 0$ in `D1` since $\delta\alpha = 0$):
     - **Why `D1` (`(q_H a, 2 q_H b)`) fails:** Under $\tau \to \tau + 1$, $\theta[\alpha, \beta](\tau + 1) = e^{-\pi i \alpha(\alpha + 1)} \theta[\alpha, \beta + \alpha + \frac{1}{2}](\tau)$. At $T \cdot w = (a, b - a)$, the second argument becomes $2 q_H (b - a) + q_H a + \frac{1}{2} = 2 q_H b - q_H a + \frac{1}{2} \neq 2 q_H b + \frac{1}{2}$ whenever $q_H a \notin \mathbb{Z}$. Thus `D1` does not even return to the same characteristic lattice point (`O(1)` failure on mass ratios / log-ratios for both `Rep +` and `Rep -`).
     - **Why `D1'` (`(q_H a, q_H b)`, `Amendment A1`) ALSO fails:** Although $q_H(b - a) + q_H a = q_H b$ repairs the characteristic coordinates modulo $\mathbb{Z}$, wrapping $\beta + \alpha + \frac{1}{2}$ back into the standard $(\theta_2, \theta_3, \theta_4)$ representatives shifts $\beta$ by $+1$ on $\theta_2$ ($\alpha_2 = \frac{1}{2} + \delta\alpha$, giving multiplier $-e^{2\pi i \delta\alpha}$) and on $\theta_4$ in `Rep +` ($\alpha_4 = \delta\alpha$, giving multiplier $+e^{2\pi i \delta\alpha}$). Because $q \frac{d}{dq}$ and $E_2(\tau)$ are $\tau \to \tau + 1$ invariant, $(D R_0, D R_1, D R_2)$ transforms at $(\tau + 1, T \cdot w)$ with **unabsorbed component-dependent fifth-root phases** ($\delta\alpha = q_H a$):
       $$\text{Rep } +:\quad D R(\tau + 1, T \cdot w) = e^{\frac{\pi i}{4} + \pi i \delta\alpha^2}\!\left(D R_0,\; e^{+2\pi i q_H a} D R_2,\; -e^{-2\pi i q_H a} D R_1\right),$$
       $$\text{Rep } -:\quad D R(\tau + 1, T \cdot w) = e^{\frac{\pi i}{4} + \pi i \delta\alpha^2}\!\left(e^{+2\pi i q_H a} D R_0,\; D R_2,\; -D R_1\right).$$
       Frame C's untwisted quaternion contraction `COUP["S"]` only intertwines the $q_H = 0$ permutation $(D R_0, D R_2, -D R_1)$ with matter's $T$-transformation; whenever $q_H a \notin \mathbb{Z}$ ($20/24$ order-5 points), the relative component phases $e^{\pm 2\pi i q_H a} \neq 1$ distort the singular values of $Y_f(\tau + 1, T \cdot w)$ relative to $Y_f(\tau, w)$ by $O(10^{-1}\text{--}10^1)$ in $|\Delta \ln(\sigma_i/\sigma_3)|$ across both `Rep +` and `Rep -`!

---

## 3. Falsification Criteria & Planted Controls

- **What would falsify our expectation (`DIFFERENT` vs `B1947`):** If *any* of the 4 combinations `(D1, Rep +)`, `(D1, Rep -)`, `(D1', Rep +)`, `(D1', Rep -)` achieves $\max_{w \in E[5]\setminus\{0\}} |\Delta \ln(\sigma_i / \sigma_3)| < 10^{-10}$ across all 24 order-5 points at 3 bulk moduli $\tau \in \mathbb{H}$.
- **Mandatory controls (`Guardrails 2, 3, 6`):**
  1. `CTL-B1947-UNTWISTED` ($q_H = 0$): must pass `C0` and `C2` across all 24 points and 3 bulk moduli to `< 1e-45`.
  2. `CTL-B1947-A0-STRATUM` ($a = 0$, 4 points $(0, b)$): verify analytically and numerically that $\delta\alpha = q_H \cdot 0 = 0$ makes `C2` hold to `< 1e-45` on the 4 $a = 0$ points while failing at `O(1)` on all 20 $a \neq 0$ points (proving a test restricted to $a = 0$ would falsely pass!).
  3. `CTL-B1947-HAAR` (`Guardrail 3`): verify random Haar $\mathrm{SU}(3)_L \times \mathrm{SU}(3)_R$ basis-scrambling invariance of $\sigma_i/\sigma_3$ to `< 1e-45` and catch planted non-invariant extraction.

0 of 19.
