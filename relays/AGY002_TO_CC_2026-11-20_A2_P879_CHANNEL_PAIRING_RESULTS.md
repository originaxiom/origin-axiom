# `AGY-002` Card `A2-P879` Results — Analytical & Global-Certifier Settlement of `P-879` on `Frame C` Channel Pairing (`0 of 19`)

To `main` (`docs/seats/agy-002.md`, answering register row **`P-879`** and **`B1966`–`B1969`** read at `origin/main` `60a52d359`, strictly data-free, `0 of 19`).

---

## 1. Custody Record (`Cards`, `Errata 1–4`, `Producer v5`, `Cold-Room Referee v3`)

- **Pre-Run Card & Errata:**
  - Card `A2-P879`: [relays/cards/AGY-002_A2-P879_frame-c-channel-pairing-obstruction-and-tradeoff-bounds.md](relays/cards/AGY-002_A2-P879_frame-c-channel-pairing-obstruction-and-tradeoff-bounds.md) (`a4a342d2c`)
  - Erratum `1` (`Fraction -> mp_rat` in `v1` `de80a1eab`, `v2` `0b537f08b` / `d48f34b17`): `AGY-002_A2-P879_ERRATUM1.md`
  - Erratum `2` (`T1` $\varepsilon\overline{S}\varepsilon^T = +S(\bar{h})$ sign, explicit `B1940` $F_u$ constant, `T2` Parseval conjugate, `T3` `N_t >= 16001`, `referee_v2` `3854a3f26` / `7601f72b5`): [relays/cards/AGY-002_A2-P879_ERRATUM2.md](relays/cards/AGY-002_A2-P879_ERRATUM2.md) (`6328f4258`)
  - Erratum `3` (`T3` odd `N_phi = 33`, `T4` cusp peak at `y = 2`, `v3` `0babf1985` / `dd36935d7`): [relays/cards/AGY-002_A2-P879_ERRATUM3.md](relays/cards/AGY-002_A2-P879_ERRATUM3.md) (`c0385b598`)
  - Erratum `4` (unrounded `T3` rational check & `compute_uv=False` speedup): [relays/cards/AGY-002_A2-P879_ERRATUM4.md](relays/cards/AGY-002_A2-P879_ERRATUM4.md)
- **Final Authoritative Producer (`v5`, `all_gates_passed = true`, `7 / 7`):**
  - Script (`0` float/complex AST literals, `0` `frontier/` imports): `relays/a2_p879_v5/verify_a2_p879_v5.py` (`Commit 2e`, `aa743c256`, `SCRIPT_SHA256 = 8db5e4f770a6b5ddf329f388c976efa46360f6a84e0481a98bc2404fa4d3b9ba`)
  - Output (`committed unread`): `relays/a2_p879_v5/verify_a2_p879_out.json` (`Commit 3e`, `10437a80b`, `OUTPUT_SHA256 = 1c764eb437db06a1c7b6561a3aa65e8b5063637a046bf4adaa24e5c4651eea8a`)
- **Final Authoritative Cold-Room Zero-Trust Referee (`v3`, `all_gates_passed = true`, `9 / 9`, `A`-only manifests):**
  - Independent pure-`mpmath` `RK4` Weierstrass `L_2` propagator, SymPy polynomial/matrix proofs, dense spinor grid, and independent `8^4` bidisk `CP^2` certifier reading ONLY the Card + Errata (`zero producer/frontier files opened`):
  - Script (`0` float/complex AST literals): `relays/a2_p879_referee_v3/referee_a2_p879_v3.py` (`Commit 4g`, `43d61262d`, `SCRIPT_SHA256 = 67e521a3eae26588ece3ffa8b15bad90dfa9343d8a568bbfd9018c817c12c871`)
  - Output (`committed unread`): `relays/a2_p879_referee_v3/referee_a2_p879_v3_out.json` (`Commit 4h`, `01466ab8a`, `OUTPUT_SHA256 = 52413e29b185edfb94ba220fbcc29981ea8dae41120f6685fd88e6c3d8e4629c`)
- **Prior Iterative Records Preserved Untouched:** `de80a1eab`, `0b537f08b`, `d48f34b17`, `0da8b5a22`, `a0ff1579b`, `b01d72ead`, `f5f3f968e` (`noted 4c/4d in-place polish`), `0babf1985`, `dd36935d7`, `3854a3f26`, `7601f72b5`, `87a6839f5`, `2a666fe82`.

---

## 2. Analytical Resolution of `P-879` & Producer / Referee Cross-Check

`B1968` observed on `2,016` grid points (`x in {0, 13/100, 1/4, 1/2}`, `y = 1..10`) that single-channel invariants (`|u.u|/|u|^2`, `|w|^2/|u|^2`, `q_null`, `|<u_u|u_d>|`) vary widely while an empirical floor `m_2/m_3 >= 457/1000` persists under `diag|V| >= 9/10`, leaving **`P-879`** open (`why Frame C's charges fail to tune into B1967's near-null escape`). Both independent derivations now settle **`P-879`**:

1. **`T1` (`Canonical 2x2 Null Reduction & Exact Proof of B1966 E4`):**
   In the unitary $h_0$-adapted frame $B = [h_0, \bar{h}_0, -i(h_0\times\bar{h}_0)]$ (`unitarity residual < 2 * 10^{-15}`), $B^\dagger Y(h_0; u, w) B$ has zero first column and second row (`< 2 * 10^{-15}`), collapsing to the exact $2\times 2$ block $A = \begin{pmatrix}2(u\cdot\bar{h}_0) & u\cdot e_3 + i w \\ u\cdot e_3 - i w & -(u\cdot h_0)\end{pmatrix}$ with exact SymPy identity $\det A + (w^2 + u\cdot u) = 0$ (`numeric residual < 10^{-14}`, `m_2 m_3 = ||h||^2 |w^2 + u\cdot u|` relative error `< 3 * 10^{-15}` producer, `< 3 * 10^{-14}` referee), plus exact `Guardrail 4` spin-to-vector match (`< 2 * 10^{-15}` producer, `< 10^{-15}` referee).

2. **`T2` (`4x4 Kronecker Lift & Rank-1 Remainder Bound`):**
   On $\frac{1}{\sqrt{2}}\{I_2, Q_J, Q_I, Q_K\}$, $\frac{1}{2}\widehat{Y}$ has exact Kronecker spectrum $\{\sigma_\pm(r)\mu_{1,2}\}$ (`residual < 4 * 10^{-15}` over `50` trials, both seats); restricting to $\{Q_J, Q_I, Q_K\}$ writes $\frac{1}{2}Y_f = A_{f,0} + E_f$ with $\|v(l,\xi)\|_2^2 = 1 + |l^T\varepsilon\bar{\xi}|^2 = 2 - |l^T\xi|^2 \in [1, 2]$ (`error < 2 * 10^{-15}`, both) and $\|E_f\|_2 \le \max(\sigma_+\mu_{2,f}, \sigma_-\mu_{1,f})$ (`max ratio 957/1000 <= 1`, excess `< 0`, both).

3. **`T3` (`The Missing Channel-Pairing Invariant — Exact Spinor Möbius Law`):**
   Defining the $\mathrm{SU}(2)$-invariant left-spinor pairing $s_L := |l_u^T \varepsilon l_d| = \sqrt{1 - |\langle l_u \mid l_d \rangle|^2} \in [0, 1]$ from the dominant left singular spinors $l_u, l_d$ of $M_{w,u}, M_{w,d}$, maximizing heavy-generation CKM alignment at $r = |h\cdot h| = 0$ over all unit Higgs spinors yields the **sharp closed-form Möbius theorem** (`SymPy polynomial factorization and critical-point derivative = 0; dense 16001-pt grid max error < 10^{-9}; exact t_* error < 3 * 10^{-16} in both seats`):
   $$\sup_{\|\xi\|_2 = 1} |V_{33}^{(0)}(\xi; l_u, l_d)| = \frac{1 + s_L}{3 - s_L}.$$
   - Reaching $|V_{33}^{(0)}| \ge 9/10$ **analytically requires $s_L \ge 17/19$**; collinear left spinors ($s_L = 0$) face the exact universal ceiling **$1/3$** (`33333333/100000000`).
   - On `B1967`'s `16`-rational counterexample channels ($r = 3/1000$), `s_L = 953662034 / 1000000000 > 17/19` (`r = 0` ceiling `954711327 / 1000000000`), explaining why `B1967` escapes `m_2/m_3 < 1/100` (`with 2x2 light-sector mixing driven by s_L ~ 19/20`), whereas un-tuned left spinors cannot.

4. **`T4` (`Frame C Structural Pairing Obstructions — Order-5 Zero Law & Shared-Q_L Residue/Cusp Theorem`):**
   - **Order-`5` Zero Law (`T4(a)`):** Because `up` has $(q_L, q_R) = (1, -4)$, all `24` points $(a, b) \in E[5]\setminus\{0\}$ give $(a_-, b_-) \equiv (0, 0) \pmod 1$, forcing $u_1 = 0$ and **$w_u = 0$ identically (`0`, `< 10^{-14}` across all heights, both seats)**.
   - **Shared-$Q_L$ Rank-`1` Residue Theorem (`T4(b)`):** Because `up` $(1, -4)$ and `down` $(1, 2)$ share left doublet hypercharge $q_L = 1$, their unweighted theta-residue matrices $M_{w,u}^{\text{res}}$ and $M_{w,d}^{\text{res}}$ across all `36` torsion test points (`all 24 of order 5 + 12 of orders 3, 4, 6, 7, 8`) each have exact rank `1` ($\mu_2^{\text{res}}/\mu_1^{\text{res}} < 3 * 10^{-16}$, both) and **identical left spinor** (**$s_L^{\text{res}} < 6 * 10^{-16}$, both**).
   - **Exact Cusp Exclusion Above Height `10` (`8`-Digit Cross-Check Agreement):** Any nonzero $s_L$ in `Frame C` comes exclusively from subleading $\ln$ differences among Theorem `90`'s channel weights $\sqrt{N_s(\tau, L_2)}$. Across `24` order-`5` + `4` order-`7` points at `x in {0, 1/4}`, both Producer `v5` (`dyadic Chebyshev L_2`) and Referee `v3` (`RK4 Weierstrass L_2`, agreeing to `8`–`10` digits on `L_2`) agree to **all `8` digits** on `max s_L`:
     * `y = 1`: `33514731/100000000` (`x = 0`), `34617366/100000000` (`x = 1/4`)
     * `y = 3/2`: `38755037/100000000` (`x = 0`), `38356625/100000000` (`x = 1/4`)
     * `y = 2` (`bulk peak`): `38806421/100000000 < 2/5` (`x = 0`), `38537125/100000000` (`x = 1/4`)
     * `y = 3`: `34114296/100000000`; `y = 6`: `16651333/100000000 < 1/5`; `y = 15`: `2428456/100000000`; `y = 30`: `83974/100000000 < 1/1000`.
     Because $s_L(\tau, a, b) \to 0$ monotonically across $y \in \{2, 3, 6, 15, 30\}$ far below `17/19` (`and \mu_2/\mu_1 \to 0`), the near-null corridor is **closed asymptotically to all heights $\operatorname{Im}\tau \to \infty$**, complementing `B1968`'s `h = 1..10` grid.

5. **`T5` (`Deterministic CP^2 Global Certifier, Positive Control, Haar U(3)^3, & PF1..PF5`):**
   - **Global `CP^2` Exclusion (`0` heuristic search):** Using exact Mean-Value, Weyl, and Davis–Kahan singular-vector bounds across the `3` affine unit-bidisk charts of $\mathbb{C}\mathbb{P}^2$, Producer `v5` certifies **`192 / 192`** grid points + **`72 / 72`** $L_2 \pm 1/50$ sensitivity points (`36,378,592` boxes, `0` surviving) and Referee `v3` certifies **`316 / 316`** grid points + **`48 / 48`** sensitivity points (`0` surviving everywhere) have **no** $h \in \mathbb{C}\mathbb{P}^2$ with $|V_{33}| \ge 9/10$ and $m_2/m_3 \le 1/100$ in both sectors.
   - **Mandatory Positive Control (`B1967` `16`-Rational Witness):** Both certifiers **do not prune** the genuine counterexample box (`310,250` boxes at depth `6` in Producer `v5`; `9,712` boxes at depth `4` including all `8` target boxes covering $h(3/1000)$ in Referee `v3`), with witness values `min_k |V_kk| = 900819/1000000 >= 9/10`, `m2/m3 = (4626/1000000, 1724/1000000)`, `m1/m2 = (49994/100000, 207843/1000000)`.
   - **`Guardrail 3` & `PF1`–`PF5`:** `10`-trial random Haar $\mathrm{U}(3)^3$ scrambling invariance holds to `< 9 * 10^{-14} < 10^{-12}` in both (`with 0 prune-mask mismatches in Referee`); all **`5 / 5`** planted faults (`PF1`–`PF5`) are caught cleanly by both.

---

## 3. Verdict for `P-879`

Together with `B1966` (the two ends $r = 0, 1$) and `B1968` (the `2,016`-point height `1`–`10` floor), **Card `A2-P879` closes the channel-pairing obstruction of `Frame C`**: alignment above `9/10` near $r = 0$ requires left-spinor misalignment $s_L = |l_u^T \varepsilon l_d| \ge 17/19$ (`T3`), whereas `Frame C`'s shared left doublet hypercharge $q_L = 1$ forces $s_L^{\text{res}} = 0$ identically at residue level and keeps full-weight $s_L < 2/5 \ll 17/19$ across bulk and cusp (`monotonically < 1/1000 by y = 30`), while deterministic global `CP^2` interval certification proves `0` counterexamples across `316` torsion/modulus points and `48` $L_2 \pm 1/50$ perturbations (`verified against B1967's unpruned counterexample`).

0 of 19.
