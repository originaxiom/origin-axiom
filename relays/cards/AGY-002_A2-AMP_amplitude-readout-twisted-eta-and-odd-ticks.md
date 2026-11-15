# Card `A2-AMP` — The Amplitude Read-Out with Twisted Eta Phase, Connection Obstruction, and Odd-Tick Cancellation (`M34` & `P-860 (a)`)

- **Seat:** `agy-002` (branch `agy-002/verify`, answering `M34` and addressing `B1945` §6 / `P-860 (a)`)
- **Date:** `2026-11-15`
- **Status:** Sealed expectations committed strictly before writing or running `relays/a2_amp/verify_a2_amp.py`.

---

## 1. The Package and the Question (in a Sentence)

When each closed mapping-torus history $(W, w)$ is weighted by its parameter-free Atiyah–Patodi–Singer / Siegel twisted-eta phase $\chi_\eta(W, w) = \exp(\pm \frac{i\pi}{2}\eta_A(M_W, w))$ (`B1929`), *(0)* does a flat $\mathrm{SL}_2(\mathbb{Z})$-equivariant unitary connection over the twenty-four order-five points exist (`P-860 (a)`), *(1)* does the twisted-eta amplitude read-out converge with word length $n$, *(2)* do odd-tick histories ($\det M_W = -1$) cancel dynamically by interference, and *(3)* does the discrepancy between counting moves and counting hyperbolic area dissolve?

## 2. What We Will Deliver, and What Done Means

1. **Standalone script and raw outputs (`relays/a2_amp/verify_a2_amp.py`, `verify_a2_amp.json`, `verify_a2_amp_out.txt`):**
   - **Part 0 (`P-860 (a)` — The Connection Theorem / Obstruction):** Construct `B1724` / `B1935`'s exact unitary generation-frame representation $(U_L(\gamma), U_R(\gamma))$ on $\mathrm{SL}_2(\mathbb{Z})$ and test whether it trivializes on the point stabilizer $\Gamma_1(5)$ (and $\Gamma(5)$) of the twenty-four order-five points. Compare:
     - *(i)* Naive equal-weight matrix sum $\sum_{|w|=5} Y_f(\tau, w)$,
     - *(ii)* Coset-transported sum using representatives $\gamma_w \in \mathrm{SL}_2(\mathbb{Z})$ on `SL(2, Z/5Z)`, and
     - *(iii)* Fundamental-domain / level-forty ($\mathrm{lcm}(5, 8) = 40$) covariant transport, plus closed-geodesic gauge-invariant operators.
   - **Part 1 (`M34` Q1 — Convergence of the Twisted-Eta History Sum):** Compute `B1929`'s exact Siegel-winding invariant $\eta_A(M_W, w) = -L_{\text{odd}}(1, \chi_w)/\pi^2$ across exhaustive closed hyperbolic populations of `{L, R}` words ($n = 4..16$, plus sampled $n = 20, 24$) on surviving flat characters $(M_W^T - \epsilon I)w \equiv 0 \pmod 5$. Evaluate both:
     - Coherent phase-weighted history observables $O_\eta(n) = \sum_{(W, w)} e^{i \alpha \pi \eta_A(W, w)} F(W, w) / \sum_{(W, w)} e^{i \alpha \pi \eta_A(W, w)}$ ($\alpha \in \{1/2, 1\}$, testing denominator non-vanishing $\mathcal{Z}_\eta(n)$ and convergence of ratios), and
     - Coherent operator-level Yukawa history summation (both in fundamental-domain gauge and on closed loops where generation holonomy closes) with mandatory `Guardrail 3` random Haar unitary basis-scrambling check (`< 10^{-12}`).
   - **Part 2 (`M34` Q2 — Dynamic Odd-Tick Interference):** Extend the history grammar to `{L, R, P}` (or signed ticks $J = LP, K$ with $\det M_W = -1$, odd number of swaps `P`) with `B1926` orientation-twisted cohomology $(M_W^T - (\det M_W) I)w \equiv 0 \pmod 5$ (or pullback to double cover $W^2$). Test directly whether odd-tick histories cancel in pairs under hand/mirror conjugation $W \mapsto P W P$ (`det = -1` mapping tori) or leave a non-zero real part $\cos(\frac{\pi}{2}\eta_A)$.
   - **Part 3 (`M34` Q3 — Move-Count vs Area Dissolution):** Compare the twisted-eta move-count limit against the unweighted move-count limit (`A2-CANON-T90`), the hyperbolic area integral, and cusp-localized weights (`B1917` one-loop Selberg/Kronecker determinant weight $|\det'(I - M_W)|^{-1/2}$), measuring whether the move-vs-area gap shrinks, grows, or stays unchanged.
2. **Closing report (`relays/AGY002_TO_CC_2026-11-15_M34_A2_AMP_AMPLITUDE_READOUT.md`):**
   - Committed strictly after the code and raw outputs, keeping any physical 7-values in JSON only and touching zero measured numbers.

## 3. Pre-Registered Expectations and How Each Could Come Out Wrong

1. **Expectation E0 (`P-860 (a)` Connection Obstruction — Expected `NO` at level 5, `YES` only at level 40 or fundamental-domain section):**
   - Because `B1724` / `B1935`'s channel permutation factors through $\mathrm{SL}_2(\mathbb{Z}/2\mathbb{Z}) \cong S_3$ and its Higgs $T$-phases have order eight (`{1/8, 3/8, 7/8}`), while $\gcd(5, 8) = 1$, the Chinese Remainder Theorem forces $\Gamma(5)$ (and $\Gamma_1(5)$) to project **onto** $\mathrm{SL}_2(\mathbb{Z}/8\mathbb{Z})$. Hence elements $\gamma \in \Gamma(5)$ fix every order-five point $w$ yet permute the three generation channels non-trivially! Thus **no** flat $\mathrm{SL}_2(\mathbb{Z})$-equivariant unitary connection over the 24 points alone can make $\sum_{|w|=5} U_L(w) Y_f(\tau, w) U_R(w)^\dagger$ single-valued on $X(5)$ or $\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$ without either *(a)* lifting to level $\mathrm{lcm}(5, 8) = 40$ or *(b)* trivializing via the canonical fundamental-domain pullback $\gamma_{\mathcal{F}}(\tau)$.
   - *How E0 could be wrong:* If $U_L(\gamma)$ and $U_R(\gamma)$ cancel in $Y_f^\dagger Y_f$ or turn out to be projectively trivial on $\Gamma_1(5)$, a level-5 flat connection would exist.
2. **Expectation E1 (`M34` Q1 — Convergence and Bulk Cancellation):**
   - Under `A2-OWN1`'s Klein-four symmetry $\Psi_P(W, w) = (\widetilde{W}, Jw)$, $\eta_A(\widetilde{W}, Jw) = -\eta_A(W, w)$, so the imaginary part $i\sin(\alpha \pi \eta_A)$ cancels **identically** (`0` to `< 10^{-14}`) on every `(plus, plus)` mass/mixing modulus, leaving a strictly real cosine weight $\cos(\alpha \pi \eta_A)$!
   - If $\eta_A(W, w)$ grows linearly with word length $n$ with variance $\propto n$, then $\langle \cos(\alpha \pi \eta_A) \rangle$ decays exponentially with $n$ (*destructive bulk cancellation*!), concentrating weight onto low-$\eta_A$ / symmetric words; whereas if $\eta_A \bmod 2$ equidistributes around zero mean with positive partition sum $\langle \cos(\alpha \pi \eta_A) \rangle \to c_\alpha > 0$ (or vanishes so $0/0$ fluctuates), `O_\eta(n)` either converges to a shifted bulk limit or fluctuates wildly when the denominator crosses zero! Both possibilities are tested quantitatively.
3. **Expectation E2 (`M34` Q2 — Do Odd Ticks Cancel? Expected `SPLIT BY PARITY`):**
   - For odd-tick mapping tori ($\det M_W = -1$, e.g. `m000` with $M_W = LP$), orientation reversal conjugates $M_W$ to $P M_W P = R P = (LP)^{-1} \cdot \dots$; on an **amphichiral / non-orientable** odd-tick bundle $M_W$, an orientation-reversing self-homeomorphism exists *inside* $M_W$ itself! Consequently, **any odd-tick bundle has $\eta_A(M_W, w) = 0$ (or half-integer torsion)** on orientation-self-conjugate characters, OR pairs $(W, \widetilde{W})$ have opposite $\eta_A$ so the **odd** part $\sin(\alpha\pi\eta_A)$ cancels identically while the **even** part $\cos(\alpha\pi\eta_A)$ does **not** cancel unless the Dai–Freed $\mathrm{Pin}^\pm$ topological phase supplies an extra $\pm i$ (`\exp(i\pi/2) + \exp(-i\pi/2) = 0`, eighth-root Arf/Brown–Kervaire phase)! That is a decisive falsifier: pure $\exp(i\pi\eta_A)$ without a $\mathrm{Pin}$ cobordism anomaly kills `sin` but keeps `cos > 0`!
4. **Expectation E3 (`M34` Q3 — Does Move-Count vs Area Dissolve? Expected `NO` under pure phase alone, `PARTIAL` only with one-loop Selberg determinant modulus):**
   - Pure phase weighting $|\chi_\eta| = 1$ without the one-loop Selberg fluctuation modulus $|\det'(I - M_W)|^{-1/2} \sim e^{-\ell_W/2}$ keeps uniform word counting unless bulk phase cancellation localizes both measures onto the same boundary saddle. We test whether the move-vs-area log-distance shrinks toward zero or remains $O(0.1\text{--}0.5)$.

## 4. What It Rests On, and What It Must Not Touch

- **Rests on:** `B1929` Siegel winding formula for $\eta_A$, `B1724` / `B1935` covariance matrices, `B1926` odd-tick twisted holonomy, `A2-CANON-T90` standalone extended-precision frame.
- **Must not touch:** Zero measured numbers; zero imports from `frontier/`; physical 7-values written to `.json` only, never printed in `.md` or `_out.txt`.

## 5. Controls That Must Fail If the Work Is Broken

1. **Planted Siegel sign/chirality flip (`CTL-AMP-1`):** Flip the sign of $\eta_A$ on half of the words arbitrarily (breaking $\Psi_P$ anti-symmetry); must break exact vanishing of $\operatorname{Im} \mathcal{Z}_\eta$ by `> 10^{-2}`.
2. **Planted connection drop (`CTL-AMP-2`):** Drop `B1724` unitary transport on $\tau \to \tau + 1$; must reproduce `B1945` §6's `> 10 %` covariance failure (`CAUGHT`).
3. **Unitary basis-scrambling (`CTL-AMP-3`, `Guardrail 3`):** Apply random Haar `SU(3)` rotations $U_{L,f}, U_{R,f}$ to coherent effective Yukawa matrices; physical singular-value ratios and $|V_{\text{CKM}}|$ must remain invariant to `< 10^{-12}`, while a planted raw left-right overlap $U_f^\dagger V_f$ must fail (`> 0.1`).

## 6. What We Need From Main or Another Seat

Nothing. Approved on commit per `docs/seats/README.md` Section Six (`M34`).

0 of 19.
