# Card `A2-SMC13` — Independent Second Computation of the Order-Five Lepton–Down Copy (`M33`, Row `1808`)

- **Seat:** `agy-002` (branch `agy-002/verify`, answering `M33` and `M36`)
- **Date:** `2026-11-15`
- **Status:** Sealed expectations committed before running `relays/a2_smc13/verify_smc13_order5.py` and without reading `SM-C13`'s code.

---

## 1. The Package and the Question (in a Sentence)

Does Frame `C`'s coupling at exact torsion order five force the charged-lepton Yukawa matrix $Y_e(\tau, w)$ to equal the transpose of a down-quark Yukawa matrix $Y_d(\tau, w')^T$ across the twenty-four order-five points, both Higgs worlds ($W_-$ and $W_+$), and both channel weights (exact Theorem Ninety and truncated), making lepton mass ratios identical to down-quark mass ratios on every even-tick untwisted read-out while splitting once base-circle orientation twist $(-1)^{6Y}$ (`B1926`) enters?

## 2. What We Will Deliver, and What Done Means

1. **Standalone script and raw output (`relays/a2_smc13/verify_smc13_order5.py`, `verify_smc13_order5.json`, `verify_smc13_order5_out.txt`):**
   - Pure independent 50-digit `mpmath` construction of Frame `C`'s coupling from mathematical definitions (`6Y` charges `Q = 1, u = -4, d = 2, L = -3, e = 6`, quaternion basis `{1, i, j, k}`, Kronecker limit norm and exact Theorem Ninety weight, `S` and `tilde_S` Higgs readings), sharing zero code with `main` or `sm`.
   - Algebraic and numerical check at every one of the twenty-four exact order-five torsion points $w \in \frac{1}{5}\mathbb{Z}^2 \setminus \{0\}$ across generic interior and high-cusp moduli $\tau \in \mathbb{H}$, verifying both:
     - **Pointwise matrix transpose identity:** $Y_e(\tau, w) = Y_d(\tau, -w)^T$ (and $Y_e(\tau, w) = Y_d(\tau, +w)^T$ up to exact sign/channel structure — we test both $w' = +w$ and $w' = -w$ explicitly so our code reports which exact pairing holds to `< 10^{-45}`!), and consequently exact equality of singular-value mass ratios $(m_1/m_3, m_2/m_3)$ pointwise at each $w$ because $Y_d(\tau, -w) = Y_d(\tau, +w)$ (`P-847` / `B1935` centre invariance).
     - **Mandatory unitary basis-scrambling check (`Guardrail 3`):** Apply independent random Haar unitary transformations $Y_f \to U_{L,f} Y_f U_{R,f}^\dagger$ (`SU(3)`) and assert physical singular-value ratios are invariant to `< 10^{-12}`.
     - **Odd-tick orientation-twist contrast (`B1926` / `P-846`):** Test the same twenty-four order-five fibre characters when combined with the base-circle orientation character $(-1)^{6Y}$ (`Q: -1, d: +1` versus `L: -1, e: +1` on the meridian/longitude scar transport, or half-integer base shift $+1/2 \cdot (6Y \bmod 2)$ on the longitude giving order ten `w + (0, 1/2)` on odd-charge fields), checking whether odd-tick twisted transport breaks $Y_e = Y_d^T$.
2. **Closing note (`relays/AGY002_TO_CC_2026-11-15_M33_SM_C13_ORDER5_SECOND_COMPUTATION.md`):**
   - Committed strictly after the code and raw outputs, stating `SAME` or `DIFFERENT` on `SM-C13`'s order-five negative.

## 3. How It Could Come Out Wrong (Committed Before Any Run)

- **Expected outcome:** Because $(q_L, q_e) = (-3, 6) \equiv (2, 1) \pmod 5$ swaps $(q_Q, q_d) = (1, 2)$ modulo five, swapping left and right matter charges transposes the quaternion contraction $(1, i, j, k)$ on the $(3, 3)$ generation indices (or conjugates `i, j, k` by `-1`, which must be checked explicitly against the quaternion coupling tensor $C_{q, s, a, b}$!).
- **How our naive expectation could fail:**
  1. If the quaternion coupling tensor $C_{q, s, a, b}$ is **anti-symmetric** on $(a, b)$ in the imaginary channels $s \in \{i, j, k\}$ while swapping $(q_L, q_R)$ flips $q_L - q_R \mapsto -(q_L - q_R)$ (sending odd $\vartheta_1$ residues $R_s \mapsto -R_s$ on odd characteristics while keeping even characteristics $+R_s$), those two minus signs could either **cancel** (giving $Y_e(\tau, w) = +Y_d(\tau, w)^T$ directly!) or **fail to cancel** on one channel, breaking strict transpose equality $Y_e = Y_d^T$ while preserving or breaking singular values! Our script tests `||Y_e(w) - Y_d(w)^T||`, `||Y_e(w) + Y_d(w)^T||`, `||Y_e(w) - Y_d(-w)^T||`, and singular-value differences separately to `< 10^{-40}`.
  2. If Theorem Ninety's exact weight $N_s = 2\pi L_2 + c_s - \pi |a_{0,s}|^2 e^{-2L_2}$ depended on $q_L - q_R$ rather than $q_L + q_R$ (`1 + 2 = 3 == -3 + 6`), exact weights could split leptons from down quarks even if residues agreed; if instead $N_s$ depends only on $(q_L + q_R)w \pmod{\mathbb{Z}^2}$, then $-3 + 6 = +3 = 1 + 2$ holds **in $\mathbb{Z}$** (not even needing mod 5!), so $N_s$ matches at *every* level $N$ while the residues match only when $5 \mid (q_L^{\text{lep}} - q_R^{\text{down}})$, i.e., $N = 5$ (and $N = 1$, plus $N = 2, 4$ where $2 \mid (-3 - 1)$ and $4 \mid (6 - 2)$!).

## 4. What It Rests On, and What It Must Not Touch

- **Rests on:** Standard Jacobi theta series, Kronecker's second limit formula, `B1656` / `B1724` mathematical definitions of the charges `6Y = (1, -4, 2, -3, 6)` and Higgs readings `S, tilde_S`.
- **Must not touch:** Zero measured numbers or external physical constants; zero code imported from `frontier/` or `sm`; zero physical 7-values printed in `.md` or `_out.txt`.

## 5. Controls That Must Fail If the Work Is Broken

1. **Planted charge control (`CTL-CHARGE`):** Perturb lepton hypercharge from `(-3, 6)` to `(-2, 6)` at order five; the script must report `CAUGHT` with singular-value discrepancy `> 10^{-2}`.
2. **Planted level control (`CTL-LEVEL`):** Evaluate the exact same unaltered charges `(-3, 6)` vs `(1, 2)` at exact torsion order `N = 3` and `N = 7` (and odd-tick shifted order `N = 10`, `w_10 = w_5 + (0, 1/2)` on odd `6Y`); the script must report `CAUGHT` (`leptons != down^T`, singular-value difference `> 10^{-2}`).
3. **Planted asymmetric tensor corruption (`CTL-TENSOR`):** Flip the sign of a single channel coupling entry in $Y_e$ only; must fail equality check by `> 10^{-2}`.

## 6. What We Need From Main or Another Seat

Nothing. Approved on commit per `docs/seats/README.md` Section Six (`M33`).

0 of 19.
