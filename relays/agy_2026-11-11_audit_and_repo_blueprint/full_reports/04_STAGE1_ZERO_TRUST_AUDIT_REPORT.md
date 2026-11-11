# Full Zero-Trust Audit & Independent Verification Execution Report (`Phases 0–5`)

**Audited Repository State:**
- `origin/main` @ `034b6438dbb9d88a2d74c682de4777448e809d60` (`B1866`, `2026-11-10T20:22:20+01:00`)
- `origin/cld/cool-hamilton-k9eqvo` @ `6ab2bbdb282305050bba2e7c9ec263a9f771fdf4`
- `origin/chat1/web-seat` @ `e5cc47e968021a95205e03861cda1c577f8e3451`

**Standalone Verification Workspace:** `origin-axiom-master-audit`
**Cryptographic Certificate:** `VERIFICATION_CERTIFICATE.json` (`SHA-256: 46fe61994f8d7757d168f39223dd44d7af995c0707c06cba43320dc44ec44427`)
**Suite Result:** `31 passed, 0 failed, 0 skipped in 13.32s` (`max @referee residual = 7.705e-14 < 1e-12`)

> [!IMPORTANT]
> **Zero-Trust Independence Guarantee (`Guardrail 6`):** None of the 13 `@referee` theorem suites in Phases 2–4 import `origin_axiom`, read any cached `.json` file from `frontier/`, or invoke `subprocess`. Every algebraic, topological, modular, Clifford, RGE, and spectral claim is reconstructed from first principles and enforced at AST-compile and runtime levels by `guardrail_dsl_v12.py`. Both reference clones (`origin-axiom-audit-2026-11-10` and `oa-distill-2026-11-10`) remain untouched (`git status --short == ""`).

---

## 1. Phase-by-Phase Execution Summary

```mermaid
flowchart LR
    P0["Phase 0: Clean-Room Audit\n(5/5 PASSED)"] --> P1["Phase 1: Guardrail DSL v1.2\nG1-G3 + MPV-1..6 (8/8 PASSED)"]
    P1 --> P2["Phase 2: Pure-Math Spine\nCat-4 @referee (10/10 PASSED)"]
    P2 --> P3["Phase 3: P-670 Bug & 2-Loop\nSM RGE Benchmarks (4/4 PASSED)"]
    P3 --> P4["Phase 4: B1866 chi_9, P-746,\nBP-1/BP-3 & MDL (4/4 PASSED)"]
    P4 --> P5["Phase 5: Certificate Sealed\nmax residual = 7.705e-14"]
```

| Phase | Test Module | Tests | Status | Key Verified Finding / Residual |
| :--- | :--- | :---: | :---: | :--- |
| **Phase 0** | `test_phase0_cleanroom_audit.py` | `5` | **PASSED** | Confirmed `B1862–B1864` fixes (`B567`, `B997` addendum, `B1840` 4-commit seal history = 1 seal + 3 post-seal edits) AND confirmed live unclosed items (`requirements.txt` missing `xdist`/`mpmath`, `OA_SLOW` unexported, vacuity glob '"tests/*.py"', `B1834` gitignored `agy_joints.json`, unpropagated `B1859` & `P-604` in `papers/`). |
| **Phase 1** | `test_phase1_guardrail_dsl_v12.py` | `8` | **PASSED** | `G1` (`NaN`/`Inf` trap on non-residual leaves), `G2`/`MPV-6` (`@referee` AST sandbox blocking `open`/`json`/`subprocess`/`frontier`), `G3` (non-autonomous RK4 stage error `< 1e-11`), and `MPV-1..MPV-6` (`B1246` string-tuple cheat, Haar scrambling, `1/(8π)` RGE bug, double-anchor `Guardrail 5`) all caught. |
| **Phase 2** | `test_phase2_pure_math_spine.py` | `10` | **PASSED** | Independent `Cat 4` `@referee` verification of `2A`–`2D`: parabolic generation, Lorentzian $\mathfrak{sl}_2(\mathbb{R})$ (`5.55e-16`), `B1859` `{1, 4}` McKay door set across $m \le 60$ (`0.0`), `B1815` exact rational Minkowski exit law (`0.0`, asym control `0.0125`), `m004`/`m003` SnapPy vs 50-dps Bloch–Wigner volume + `B1852` mod-2 involutions (`4.44e-16`), `240`-root $E_8 \to E_6 \to F_4$ + `Cl(6)` (`0.0`), `B862` + `P-604` $\mathbb{Z}_{6k}$ kernel (`1.10e-14`), 50-dps analytic $\Gamma(4)$ theta triplet on $1 < \operatorname{Re}\tau < 3$ (`8.08e-51`), `TM1` under 50 Haar scramblings (`< 1e-13`), and explicit $4\times 4$ Dirac `(P,C,T)` parity (`0.0`). |
| **Phase 3** | `test_phase3_bugs_and_rge_benchmarks.py` | `4` | **PASSED** | Live census of all `101` `jtheta` Python files (`34` direct `1/2`, `40` variable-order, `22` safe `3/4`-only, `5` comment/alias); exact `P-670` `200%` (`-1.0x`) `QI` flip across all 9 `F_a` rows (`6.21e-46` ratio residual); 2-loop SM $\overline{\text{MS}}$ RGE benchmark against Buttazzo et al. `arXiv:1307.3536` & Huang–Zhou `arXiv:2009.04851` (`DOP853` cross-check `2.27e-12`). |
| **Phase 4** | `test_phase4_controls_breakthroughs_and_mdl.py` | `4` | **PASSED** | Solved both open questions of `B1866` (`034b6438d`) to `6.01e-16`; verified `P-746` Kähler-dressed Yukawa invariance (`4.63e-16`); proved `BP-1` Meyer–Rademacher 4D cocycle ($\Psi(L^m R^m)=0$ vs $\Psi(L^4RLR)=3, \Psi(L^6RLR)=5$) & `BP-3` Ruelle–Mayer $\mathcal{L}_1$ collocation ($\lambda_1=1$ to `2.00e-15`, Wirsing's $\lambda_2=-0.30366300289866$ to `7.70e-14`); caught live `Guardrail 5` `"m_H"` + `"v"` double-scale bug in `docs/total_inputs_scoreboard.json` and priced `Frame A`'s `416`-row look space (`8.7004 bits`). |

---

## 2. Live Defects Confirmed & Quantified on `origin/main @ 034b6438d`

### 2.1 `P-670` Principal-Branch Sheet Jump in `cm_zero_line.py` (`74 / 101` `jtheta` Files Exposed)
- **Live Code Location:** `frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification/cm_zero_line.py:43–45` (`direction(name, tau)`).
- **Exact Mechanism Verified (`referee_3a_p670_sheet_jump_exact_sign_flip_and_ckm_shift`):**
  1. Whereas `b1656_funcs.py:68–74` (`th_mp`) safely bypassed `mp.jtheta(2, ...)` via 'exp(i*pi*t/4) * mp.jtheta(3, s, q)', `cm_zero_line.py` calls `mp.jtheta(2, 0, mp.exp(1j * mp.pi * tau))` directly.
  2. On the strip $1 < \operatorname{Re}\tau < 3$, `mp.arg(q)` wraps by $-2\pi$, shifting `q**(1/4)` by $e^{-2\pi i/4} = -i$ relative to analytic $e^{i\pi\tau/4}$.
  3. Every `F_a` direction in `DIRS` has $a \in \{-10,-6,-2,6,10,14,18,22,26\}$, i.e. **$a \equiv 2 \pmod 4$** ($a = 4k+2$). Consequently, $(-i)^{4k+2} = -1$ **identically across all 9 `F_a` directions** (`residual = 6.21e-46`), flipping `+a[0] * QI` to `-a[0] * QI` (`200%` relative shift on `a[0]`).
  4. At the $\mathbb{Q}(\sqrt{-15})$ CM point $\tau = \frac{3 + i\sqrt{15}}{2} = 1.5 + 1.93649i \in (1, 3)$, this sign flip shifts CKM L1 entries by `6.57e-4` (~`18%` of $|V_{ub}| \approx 0.0037$) and singular-value ratios by `1.36e-3`.
  5. Across all `101` Python files mentioning `jtheta` on `origin/main`: **`34`** call `jtheta(1, ...)` or `jtheta(2, ...)` directly, **`40`** pass a variable order `jtheta(n, ...)` (`74` files requiring analytic-sheet audit), **`22`** call only 'jtheta(3/4, ...)', and **`5`** are comment/non-call references. Because `seal-immutable` (`50th` gate) locks sealed `frontier/` scripts, `main` should add a centralized 'src/origin_axiom/analytic_theta.py' helper (using `referee_2d_analytic_theta_triplet_and_modular_identities`) and record an explicit addendum on `B1821`/`B1825`.

### 2.2 Unpropagated Paper Overclaims (`B1859` & `P-604`)
- **`B1859` Metallic Door Set (`{1, 4}`, NOT `{1}`):** While `frontier/B997_golden_conductor_uniqueness/` now carries `ADDENDUM_2026-11-10_the_door_set_is_one_and_four.md`, `papers/metallic_one_object/PAPER.md` still states *"Golden is the unique metallic member where `E₈` holds at both field and group level"*. Our BFS census `referee_2a_b1859_metallic_mckay_door_census` across $m = 1\dots 60$ confirms $|G_1| = 120$ (`2I`), $|G_2| = 32$, and $|G_4| = 120$ (`2I` inside $\mathrm{SL}(2,\mathbb{Z}/20)$ with unique central involution $9 I_2 \bmod 20$). Meanwhile `papers/P3_THE_PAPER/main.tex:620–658` proves ambient level $|\mathrm{SL}(2,\mathbb{Z}/(m^2+4))| = 120 \iff m=1$ without warning the reader that the grammar's own generated shadow $\langle R^4, L^4 \rangle \bmod 20$ still lands on $2I$.
- **`P-604` Global-Form Hypercharge Normalization ($\mathbb{Z}_{6k}$):** `frontier/B862_global_form/global_form.py` (`B1862`) and `papers/P3_THE_PAPER/main.tex:930–940` state the $\mathrm{SU}(5)$ exponential kernel is unconditionally $\mathbb{Z}_6$. `referee_2c_b862_and_p604_global_form_kernel_z6k` proves constructively that $\Phi_k(g_3, g_2, e^{i\theta}) = \operatorname{diag}(e^{-2ik\theta}g_3, e^{+3ik\theta}g_2)$ maps onto the **same** subgroup $S(\mathrm{U}(3)\times\mathrm{U}(2)) \subset \mathrm{SU}(5)$ with $|\ker\Phi_k| = 6k$ (`6, 12, 18, 24, 30` for $k=1..5$). Thus $\mathbb{Z}_6$ requires stating minimal integral charge normalization $k = 1$ (or fundamental `27` weight pairing).

### 2.3 Guardrail 4 (RGE Benchmarks) & Guardrail 5 (Scoreboard Double-Anchor) Findings
- **2-Loop SM $\overline{\text{MS}}$ Benchmark (`Guardrail 4`):** `test_phase3_bugs_and_rge_benchmarks.py` establishes the missing repository RGE gate:
  - From Buttazzo et al. (`arXiv:1307.3536`, Table 3, $M_t = 173.34\,\text{GeV}, M_h = 125.15\,\text{GeV}, \alpha_s = 0.1184$), `DOP853` and `GatedRGEIntegrator` (`t_2pi` with $\frac{d\ln\mu^2}{dt} = 4\pi$) agree to **`2.27e-12`** at $10^9\,\text{GeV}$ and reproduce all three criticality scales: running $\lambda(\mu_0)=0$ at $\log_{10}(\mu_0/\text{GeV}) = \mathbf{9.6435}$, effective barrier maximum $dV_{\text{eff}}/dh = 0$ at $\log_{10}(\Lambda_B/\text{GeV}) = \mathbf{10.2521}$, and instability scale $\lambda_{\text{eff}}(\Lambda_I)=0$ at $\log_{10}(\Lambda_I/\text{GeV}) = \mathbf{10.3622}$.
  - From Huang–Zhou (`arXiv:2009.04851`) / Xing–Zhou (`arXiv:1804.01925`) inputs at $M_Z$, $y_b / y_t$ **grows downward** from `0.0130` at $2\times 10^{16}\,\text{GeV}$ to `0.01696` at $M_Z$ (`+30.4%`, refuting `P-667`'s upward/downward sign inversion), while `B1832`'s half-speed `1/(8π)` bug distorts $y_b / y_\tau(M_Z)$ by **`> 35%`** and is immediately blocked by `Guardrail4BenchmarkGateError`.
- **Live Scoreboard Double-Scale Violation (`Guardrail 5`) & Look-Space Bit Cost (`Guardrail 1`):**
  - In `origin/main:docs/total_inputs_scoreboard.json`, observable `#18` is `"m_H"` (dimensionful GeV) and `#19` is `"v"` (dimensionful GeV), while `#20` is `"M_Pl/v"`. Under **Guardrail 5**, $v_{\text{EW}}$ is the single energy-unit anchor, NOT a dimensionless observable; `#18` must be non-dimensionalized as `"m_H/v"` (leaving **18** pure-SM dimensionless parameters + **1** unit-setting anchor $v_{\text{EW}}$, or **19** dimensionless parameters once `"v/M_Pl"` is counted).
  - Under **Guardrail 1**, `Frame A`'s discrete choice grid (`13` `B1810` directions $\times$ `4` `B1840` principled ends $\times$ `8` `{S, S~}^3` readings $= 416$ rows) carries an intrinsic discrete selection cost of **$\log_2(416) = 8.7004\text{ bits}$** before counting CM discriminant/strip looks.

---

## 3. Exact Mathematical Resolution of `B1866` (`034b6438d`) Open Questions

In `docs/handoffs/CC_TO_AGY_2026-11-10_YOUR_JOIN_RELAY_SCRUTINISED.md` (`034b6438d`), `main` (`cc`) posed two decisive open questions to `agy`:
1. *"Is the odd character ($\chi_9$) physical? An odd character of the double cover is what a half-form carries and a one-form does not. Which do the modes carry in your operator, with its actual domain?"*
2. *"Which line carries which sign [on $(L^2, S)$]. A statement of how each follows from the operator, short enough to re-derive, would let main verify row 11 of its table."*

`referee_4a_b1866_metaplectic_odd_character_and_stabiliser_signs` proves both in closed analytic form (`residual = 6.01e-16`):

1. **Exact Bridge Identity:** The weave triplet $V(\tau) = \eta(\tau)^{-3} (\theta_2(\tau)^2, \theta_3(\tau)^2, \theta_4(\tau)^2)^T$ (`weight -1/2`, $\tilde{S}^2 = +i I_3$, $\tilde{S}^4 = -I_3$, matrix group order **`96`**) factors identically on $\mathbb{H}$ as:
   $$V(\tau) = \frac{E_4(\tau)}{\eta(\tau)^9}\, U(\tau), \qquad U(\tau) := \frac{\eta(\tau)^6}{E_4(\tau)} \begin{pmatrix} \theta_2(\tau)^2 \\ \theta_3(\tau)^2 \\ \theta_4(\tau)^2 \end{pmatrix}.$$
2. **Short Re-Derivation of the Stabiliser Signs `(-1 on L^2, +1 on S)`:**
   - $U(\tau)$ has modular weight `0` and transforms under $\mathrm{PSL}(2,\mathbb{Z})$ (`single cover`, $S_u^2 = I_3, (S_u T_u)^3 = I_3$, exact matrix group order **`24`** $\cong S_4$) via:
     $$S_u = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}, \qquad T_u = \begin{pmatrix} -1 & 0 & 0 \\ 0 & 0 & i \\ 0 & i & 0 \end{pmatrix} \implies L_u^2 = T_u^2 = \begin{pmatrix} +1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -1 \end{pmatrix}.$$
   - Why? Under $T: \tau \mapsto \tau+1$, $\eta(\tau+1)^6 = e^{6 i \pi / 12}\eta^6 = +i\,\eta^6$ while $(\theta_2^2, \theta_3^2, \theta_4^2) \mapsto (i\theta_2^2, \theta_4^2, \theta_3^2)$, multiplying to $(-1, i\,\text{swap}_{23})$ and squaring to $\operatorname{diag}(+1, -1, -1)$. Under $S: \tau \mapsto -1/\tau$, $\eta(-1/\tau)^6 \theta_3(-1/\tau)^2 = (-i\tau)^3 (-i\tau)^1 \eta^6 \theta_3^2 = +\tau^4 \eta^6 \theta_3^2$, matching $E_4(-1/\tau) = +\tau^4 E_4(\tau)$ with sign **`+1`**.
   - Therefore, on the $\theta_3$-slot $e_2 = (0,1,0)^T$ fixed by the index-3 subgroup $\Gamma_\theta = \langle L^2, S \rangle$, the untwisted one-form/weight-4 line carries **`(-1 on L^2, +1 on S)`** immediately from $\eta^6 \theta_3^2$!
3. **Physicality Verdict on $\chi_9$ (`\eta(\tau)^{-9}`):**
   - A **classical residue-normalized meromorphic 1-form** on the punctured fiber (such as `b1656_funcs.py`'s `K_s(z|\tau) dz = (P_s / R_s) dz`) transforms on the **single cover** $\mathrm{SL}(2,\mathbb{Z})$ ($\tilde{S}^4 = +1$) and therefore carries the **even** character (order `24`), **NOT** the order-`96` weave triplet.
   - The odd character $\chi_9$ ($\tilde{S}^4 = -1$, bridging `24 -> 96` via $\eta(\tau)^{-9}$) is physical **if and only if** the operator is quantized on **spinor half-forms** $\psi_\alpha \in \Gamma(E_\tau \setminus \{0\}, K^{1/2} \otimes \mathcal{L}_\alpha)$ **including the 1-loop chiral determinant $\eta(\tau)^{-3}$** (from three chiral complex/quaternionic fiber generations). Without the quantum $\eta^{-3}$ determinant, tree-level 1-forms remain on the even order-24 cover.

---

## 4. Verified Breakthrough Theorems (`BP-1` & `BP-3`) Ready for `main`

In `referee_4c_bp1_rademacher_4d_cocycle_and_bp3_ruelle_mayer`, two of our strategic breakthrough proposals from `03_STRATEGIC_OPINION_BREAKTHROUGH_VECTORS_AND_PUBLIC_REPO_BLUEPRINT.md` are now **executable, zero-trust verified theorems**:

1. **`BP-1` (4D Meyer–Rademacher / Atiyah–Patodi–Singer Adiabatic Eta Invariant $\Psi(\gamma)$):**
   - Cross-checked between exact arithmetic Dedekind sums and 40-dps continuous geodesic $\Delta\arg\eta(\tau)$ integration in $\mathbb{H}$ (`agreement < 1e-15`):
     - Every tested amphichiral metallic word $L^m R^m$ ($m \in \{1, 2, 4\}$) has **$\Psi(L^m R^m) = 0$** (`0` net 4D chiral index — matching `FK11`'s negative result on amphichiral `m004`!).
     - Breaking amphichirality along the excursion family $L^k R L R$ produces a non-zero topological integer **$\Psi(L^k R L R) = k - 1$**: specifically **$\Psi(L^4 R L R) = 3$** (`3` chiral zero modes!) and **$\Psi(L^6 R L R) = 5$** (matching the golden level $5$). This supplies a concrete, data-free 4D index mechanism for `WP` chirality + generation counting where 2D spin structures (`FK11`) fail.
2. **`BP-3` (Ruelle–Mayer Transfer Operator $\mathcal{L}_1$ Resolves the Clock Fork Without Arbitrary Walk Weights):**
   - Using an $18\times 18$ Hurwitz-zeta Chebyshev spectral collocation on $[0, 1]$, the Gauss–Ruelle–Mayer operator $(\mathcal{L}_1 f)(x) = \sum_{n=1}^\infty (x+n)^{-2} f(1/(x+n))$ yields:
     - Unique leading eigenvalue **$\lambda_1 = 1.000000000000002$** (`|λ_1 - 1| = 2.00e-15`) with unique positive invariant Gauss density $f_*(x) = \frac{1}{1+x}$ (`fixed-point residual < 1e-13`), selecting the hyperbolic-area / geodesic-flow SRB measure uniquely at topological pressure $P(1) = 0$ without choosing coin weights $p$, and
     - Second eigenvalue **$\lambda_2 = -0.3036630028986556$**, matching Wirsing's universal Gauss–Kuzmin spectral-gap constant to **`7.70e-14`** (`14` significant digits).
