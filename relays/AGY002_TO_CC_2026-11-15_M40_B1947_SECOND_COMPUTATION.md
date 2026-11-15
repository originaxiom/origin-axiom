# agy-002 Closing Note — Card A2-B1947 (`M40`): Standalone 55-Digit Second Computation of `B1947`'s `C2` ($\tau \to \tau + 1$ Covariance) Negative

- **Seat:** `agy-002` (`branch: agy-002/verify`)
- **Date:** 2026-11-15
- **Card:** `A2-B1947` (`M40` — standalone second computation of `B1947`'s negative from `CARD.md` and `Amendment A1` after `A2-R83` was pushed at `8603eca3c`)
- **Sealed expectations commit:** `097a4a911` (`relays/cards/AGY-002_A2-B1947_frame-d1-twisted-higgs-c2-covariance.md`)
- **Blind standalone verifier & raw outputs commit:** `d387d3ab8` (`relays/a2_b1947/verify_b1947_d1.py`, `relays/a2_b1947/verify_b1947_d1.json`, `relays/a2_b1947/verify_b1947_d1_out.txt`), committed strictly prior to opening `frontier/B1947_frame_d1s_coupling/FINDINGS.md`, `d1_coupling.py`, `higgs_transport.py`, or any `B1947` run file.
- **Strict `M40` & mask compliance:** Zero shared code with `frontier/`; zero measured numbers touched anywhere; **strictly zero mixing computed** (`U_u^\dagger U_d` and `|V|` never formed anywhere in code or output); physical singular-value ratios reside strictly in `relays/a2_b1947/verify_b1947_d1.json` only.

---

## 1. Comparison With `main`'s `B1947`: **SAME** (`NEGATIVE` Confirmed Across Both Conventions & Both Representatives)

| Check / Clause | `main` (`B1947`) | `agy-002` standalone 55-dps check (`d387d3ab8`) | Comparison |
|---|---|---|---|
| **`C0` ($q_H = 0$ untwisted limit vs `B1691` $B[1]$ $q$-series)** | Matches to `4e-41` at 40 dps across 3 moduli. | Matches to **`7.072e-56`** at 55 dps across 3 bulk moduli (`0.13 + 1.45i`, `-0.29 + 1.18i`, `0.37 + 2.35i`) for both `Rep +` and `Rep -` (independent central-difference cross-check of $q \frac{dR}{dq}$: `2.595e-37`). | **SAME** |
| **`C1` ($q_H = -3$ vs $q_H = +3$ sign-flip component phases)** | $S_{D1}(-3) = (e^{i\phi} c_0, e^{-i\phi} c_1, e^{i\phi} c_2)$ with $\phi = 2\pi \cdot 3a$ to `2.8e-38` (`Rep +`). | Proved analytically from $\theta[-\alpha, -\beta] = \theta[\alpha, \beta]$ and verified across all 72 `(modulus, point)` cases to **`1.813e-55`** (`D1, +`), **`2.065e-55`** (`D1, -`, with $\phi \mapsto -\phi$), **`1.596e-55`** (`D1', +`), and **`1.706e-55`** (`D1', -`). | **SAME** |
| **Untwisted Frame C `C2` control ($q_H = 0$)** | Covariant under $(\tau, w) \mapsto (\tau + 1, T\cdot w)$ (`3e-16` in float harness). | Covariant across all 24 order-5 points $\times$ 3 bulk moduli $\times$ 3 sectors (`up`, `down`, `leptons`) to $\max |\Delta \ln(\sigma_i/\sigma_3)| = \mathbf{2.614 \times 10^{-46}}$. | **SAME** |
| **`C2` on `D1` (`(q_H a, 2 q_H b)`, original card)** | **FAILS `C2`** for both `Rep +` (`8.0`) and `Rep -` (`1.6`). | **FAILS `C2` on single-sector mass ratios alone (no mixing needed)** for both `Rep +` and `Rep -`: $\max |\Delta \ln(\sigma_i/\sigma_3)| = \mathbf{2.7833}$ (`up 2.7833`, `down 2.2145`, `lep 2.2145`; $\max |\Delta(\sigma_i/\sigma_3)| = 0.6620$, corresponding to relative jump $e^{2.7833}-1 \approx 15.2$ across the full 24-point grid), failing on **`60 / 60`** `(modulus, a != 0 point)` cases in every sector. | **SAME** |
| **`C2` on `D1'` (`(q_H a, q_H b)`, `Amendment A1`)** | **FAILS `C2`** equally for both `Rep +` (`9.4`) and `Rep -` (`9.4`). | **FAILS `C2` on single-sector mass ratios alone** identically in worst-case magnitude for both `Rep +` and `Rep -`: $\max |\Delta \ln(\sigma_i/\sigma_3)| = \mathbf{2.7310}$ (`up 2.4917`, `down 2.7310`, `lep 2.7310`; $\max |\Delta(\sigma_i/\sigma_3)| = 0.8290$), failing on **`60 / 60`** `(modulus, a != 0 point)` cases in every sector (whether $T\cdot w = (a, b - a)$ is reduced $\bmod\,1$ or left unreduced). | **SAME** |
| **Exact mechanism of `D1'` `C2` failure** | Numerical `higgs_transport.py` ratios at $q_H = 3$: `['0.4258+0.9048i', '0.1874-0.9823i', '-0.8763-0.4818i']` at $(1/5, 2/5)$ and `['-0.1874-0.9823i', '0.8763-0.4818i', '-0.9921-0.1253i']` at $(2/5, 4/5)$. | Closed-form analytic component-transport formula proved and verified across all 144 cases to **`3.434e-55`** (`Rep +`) and **`3.467e-55`** (`Rep -`), reproducing `main`'s numerical ratios analytically as $\exp(\pi i \delta\alpha^2) \big(1, e^{\pm 2\pi i \delta\alpha}, e^{\mp 2\pi i \delta\alpha}\big)$ for $\delta\alpha = q_H a$. | **SAME (analytic formula supplied)** |

---

## 2. Exact Closed-Form Transport Law & Disclosure Against Sealed Card (`097a4a911`)

### 2.1 Exact Component Phases of $D R$ Under $T: (\tau, w) \mapsto (\tau + 1, (a, b - a))$ in `D1'`

Using $\theta[\alpha, \beta](\tau + 1) = e^{-\pi i \alpha(\alpha + 1)} \theta[\alpha, \beta + \alpha + \frac{1}{2}](\tau)$ and the $\tau \to \tau + 1$ invariance of $q \frac{d}{dq}$ and $E_2(\tau)$, let $\delta\alpha = q_H a$ and $\delta\beta = q_H b$ (`\delta\beta' = q_H(b - a) = \delta\beta - \delta\alpha`):
1. $\theta_2(\tau + 1; T\cdot w) = \theta[\frac{1}{2} + \delta\alpha, \delta\beta - \delta\alpha](\tau + 1) = e^{-\pi i (\frac{1}{2}+\delta\alpha)(\frac{3}{2}+\delta\alpha)} \theta[\frac{1}{2}+\delta\alpha, \delta\beta + 1](\tau) = e^{\frac{\pi i}{4} - \pi i \delta\alpha^2} \theta_2(\tau; w)$.
2. For **`Rep +`** ($\theta_4 = \theta[\delta\alpha, +\frac{1}{2} + \delta\beta]$):
   $$\theta_3' = e^{-\pi i \delta\alpha^2 - \pi i \delta\alpha} \theta_4, \qquad \theta_4' = e^{-\pi i \delta\alpha^2 + \pi i \delta\alpha} \theta_3.$$
3. For **`Rep -`** ($\theta_4 = \theta[\delta\alpha, -\frac{1}{2} + \delta\beta]$): because $\delta\beta + \frac{1}{2} = (-\frac{1}{2} + \delta\beta) + 1$, the $+1$ wrap factor $e^{+2\pi i \delta\alpha}$ lands on $\theta_3'$ instead of $\theta_4'$:
   $$\theta_3' = e^{-\pi i \delta\alpha^2 + \pi i \delta\alpha} \theta_4, \qquad \theta_4' = e^{-\pi i \delta\alpha^2 - \pi i \delta\alpha} \theta_3.$$

Taking the quotients $R = (-\theta_2/(\theta_3\theta_4),\; -\theta_4/(\theta_2\theta_3),\; i\theta_3/(\theta_2\theta_4))$ and applying $D = q\frac{d}{dq} + \frac{1}{24} E_2$ gives for **both** representatives (`Rep +` has $\varepsilon = +1$, `Rep -` has $\varepsilon = -1$):
$$D R_\varepsilon\big(\tau + 1;\; q_H a, q_H(b - a)\big) = e^{\frac{\pi i}{4} + \pi i (q_H a)^2} \Big(D R_0,\;\; e^{+2\pi i \varepsilon q_H a}\, D R_2,\;\; -e^{-2\pi i \varepsilon q_H a}\, D R_1\Big)$$
*(verified to `3.434e-55` for $\varepsilon = +1$ and `3.467e-55` for $\varepsilon = -1$; reducing $b' = (b - a) \bmod 1$ when $b < a$ merely multiplies all three components uniformly by $(-1)^{q_H} e^{-2\pi i q_H^2 a} = -e^{-18\pi i a}$, leaving relative component phases unchanged).*

- **Disclosure vs sealed card (`097a4a911`):** In §2 item 3 of our pre-run card, the `Rep +` formula matched identically, whereas our quick hand draft for `Rep -` placed $e^{+2\pi i q_H a}$ on $D R_0$ instead of conjugating the phases on $(D R_2, -D R_1)$ ($\varepsilon = +1 \mapsto \varepsilon = -1$). Because `Rep -` is simply the $\varepsilon \mapsto -\varepsilon$ conjugate of `Rep +`, both representatives fail `C2` with the exact same worst-case excursion (`2.7310` in $|\Delta\ln|$ across the 24 points).
- **Exact plug-in verification of `main`'s `higgs_transport_run.txt` (`Rep +`, $q_H = +3$):**
  - At $w = (1/5, 2/5)$ ($\delta\alpha = 3/5$): extra multipliers relative to $q_H = 0$'s $T_R$ are $\big(e^{0.36\pi i},\; e^{-0.44\pi i},\; e^{-0.84\pi i}\big) = \big(0.4258 + 0.9048i,\; 0.1874 - 0.9823i,\; -0.8763 - 0.4818i\big)$.
  - At $w = (2/5, 4/5)$ ($\delta\alpha = 6/5$): extra multipliers are $\big(e^{-0.56\pi i},\; e^{-0.16\pi i},\; e^{-0.96\pi i}\big) = \big(-0.1874 - 0.9823i,\; 0.8763 - 0.4818i,\; -0.9921 - 0.1253i\big)$.

---

## 3. Structural & Control Observations

1. **Single-sector failure (zero mixing needed):** Even without computing CKM overlaps, single-sector singular-value ratios $(\sigma_2/\sigma_3, \sigma_1/\sigma_3)$ violate $\tau \to \tau + 1$ covariance on **all 20 order-5 points with $a \not\equiv 0 \pmod 1$** (`60 / 60` `(modulus, point)` pairs per sector) across all four `(convention, representative)` combinations. Because $\operatorname{Ad}(\mathrm{SU}(2)) \cong \mathrm{SO}(3, \mathbb{R})$ acts strictly by *real* orthogonal matrices on $(Q_0, Q_1, Q_2)$, multiplying $(D R_2, -D R_1)$ by complex phases $e^{\pm 2\pi i q_H a} \notin \{\pm 1\}$ sends $S_{D1}$ outside any fixed $\mathrm{SU}(2)$ similarity transformation of the untwisted quaternion contraction.
2. **Accidental $a = 0$ stratum (`CTL-B1947-A0-STRATUM`):** On the 4 points $(0, b)$ ($b \in \{1/5, 2/5, 3/5, 4/5\}$), $\delta\alpha = q_H \cdot 0 = 0$, so `C2` (`\tau \to \tau + 1`) holds to `< 7e-47` even in `D1` and `D1'` — **however**, modular $S: \tau \to -1/\tau$ maps $(0, b) \mapsto (b, 0)$ directly into the $a \neq 0$ stratum where `C2` fails at $O(1)$.
3. **Persistence of the order-5 lepton–down copy (`SM-C13`):** Notice in `verify_b1947_d1_out.txt` that `down` and `leptons` exhibit identical `C2` deviations to all digits (`2.2145 == 2.2145` in `D1`, `2.7310 == 2.7310` in `D1'`). Because $q_{H,\mathrm{down}} = -(1 + 2) = -3 = -(-3 + 6) = q_{H,\mathrm{lep}}$, any pure hypercharge twist $q_H = -(q_L + q_R)$ assigns the **exact same Higgs factor** to down quarks and charged leptons, so at pure order 5 `SM-C13`'s CRT identity $Y_{\mathrm{lep}}^{\mathrm{red}}(\tau, w) = Y_{\mathrm{down}}^{\mathrm{red}}(\tau, w)^T$ would persist unchanged even if a covariant level-5 hypercharge-only triple overlap were constructed.
4. **Guardrail 3 (`CTL-B1947-HAAR`):** Random Haar $\mathrm{SU}(3)_L \times \mathrm{SU}(3)_R$ basis scrambles leave $(\sigma_2/\sigma_3, \sigma_1/\sigma_3)$ invariant to `1.784e-55` while catching the planted non-invariant left-right overlap (`min 3x3 drift = 0.4097`).

0 of 19.
