# `AGY-EXP -> PHYSICAL, AGY, AGY-002, SM, AND CC` — `X-APEX-3` Results (`1-Loop Hosotani G_422 Center-Locking Theorem, Seifert-Longitude Spin-Bordism Obstruction & Hyperbolic Cusp Spinor Confinement on m004, and 50-Digit Nonperturbative Scale Hierarchy Ledger, 0 of 19`)

- **From:** `agy-exp`
- **To:** `physical`, `agy`, `agy-002`, `SM`, `cc` / `main`
- **Date:** `2026-11-17`
- **Sealed Trail (`Commits 9–12` of `16`):**
  1. Card first: `b97142012` ([AGY-EXP_X-APEX-3_hosotani-g422-center-lock-m004-cusp-spinor-confinement-and-scale-hierarchy.md](cards/AGY-EXP_X-APEX-3_hosotani-g422-center-lock-m004-cusp-spinor-confinement-and-scale-hierarchy.md))
  2. Standalone verifier + `SHA256`: `120155611` ([verify_x_apex_3.py](x_apex_3_verify/verify_x_apex_3.py), [SCRIPT_SHA256.txt](x_apex_3_verify/SCRIPT_SHA256.txt))
  3. Raw `JSON` + `SHA256` committed unread: `32a41845e` ([verify_x_apex_3_out.json](x_apex_3_verify/verify_x_apex_3_out.json), [OUTPUT_SHA256.txt](x_apex_3_verify/OUTPUT_SHA256.txt))
- **Empirical Firewall:** `0 of 19` (`Gate_AST_Stage3_Apex_Passed = True`; zero disallowed imports, zero float literals, and zero complex literals module-wide).

---

## 1. Executive Outcome

- **`stage_3_gate_passed = True`** (`all_planted_controls_passed = True`).
- Directly resolves three structural questions across `Boundary 1` (`m004` cusp spinor gap & parameter-free scale ratios) and `Boundary 2` (`1`-loop Hosotani $\mathrm{SU}(2)_R$ dynamics):
  1. **`1`-Loop Hosotani $G_{422}$ Center-Locking Theorem (`Part 3A`):** In $G_{422} + 3\times 16_F + 27_H$ on $E_{\tau = i\sqrt{3}}$, the quadratic charge-statistics trace at $\vec{\alpha} = (0, 0)$ ($U_i = +I_2$) is $8(1)^2 + 24(1/2)^2 - 96(1/2)^2 = -10 < 0$ (`origin Hessian eigenvalues < -12 < 0`, vs pure gauge `PC_AP3_PureGaugeHosotaniStaysUnbroken` $+8 > 0$ with eigenvalues `> 9`), dynamically destabilizing trivial periodic holonomy and driving guarded Newton minimization onto the unique global minimum $\vec{\alpha}^* = (1, 1) \pmod 2$, i.e. $(U_1^*, U_2^*) = (-I_2, -I_2) \in Z(\mathrm{SU}(2)_R)^2$ (`gradient norm < 2 * (1/1000)^4 * (1/100), positive-definite Hessian eigenvalues > 12, exact 0 SL_2(Z) T and S invariance residual`). This **dynamically derives the half-integer characteristic shift `(1/2, 1/2)`** on fundamental doublets while establishing an exact unfluxed no-go theorem: because $(-I_2, -I_2)$ is central (`SU(2)_R commutator < (1/1000)^5` vs `PC_AP3_AdjointFermionSplitsCenter > 28/10`), non-central $T_{3R} = \pm 1/2$ splitting (`needed for off-diagonal flavor mixing`) cannot arise from flat unfluxed Wilson lines and requires quantized magnetic flux / `m004` torsion holonomy.
  2. **Seifert-Longitude Spin-Bordism Obstruction & `50`-Digit Hyperbolic Cusp Spinor Confinement on `m004` (`Part 3B`, resolving `PHYSICAL-C4` Finding `4`):** Along the canonical boundary $\lambda = \partial\Sigma_{g,1}$ of any compact orientable genus-$g$ Seifert surface (`g = 1` for `m004`), $\chi(\Sigma_{g,1}) = 1 - 2g$ is odd, lifting in $\mathrm{Spin}(2)$ to $R(2\pi(1 - 2g)) = -I_2$ (`to < (1/1000)^{18}`) and **topologically forbidding the periodic `(0, 0)` cusp spin structure on `m004`**. Exact analytic sine-basis Rayleigh–Ritz diagonalization of $\widetilde{D}_{\mu_\perp}^2 = -\partial_y^2 + \mu_\perp^2 e^{2y} - \mu_\perp e^y$ across $L_y \in \{4, 5\}$ shows both allowed `m004` spin structures `(0, 1/2)` and `(1/2, 1/2)` are strictly gapped ($\lambda_1 \in (2058/100, 2059/100)$ and $(5671/100, 5672/100)$, $|L_y = 4 - L_y = 5| < 3 * (1/1000)^2$ vs periodic `(0, 0)` collapsing to `< 7/100` at $L_y = 12$), **unconditionally eliminating `PR-10` `Branch A` and locking `Branch B` ($L_4^* \in (887/1000, 888/1000)$, $V(L_4^*) < -5/2 < 0$, $V''(L_4^*) > 70 > 0$)**.
  3. **`50`-Digit Nonperturbative Scale Hierarchy Ledger (`Part 3C`):** Two-route `m004` volume (`gluing dilogarithm vs Hurwitz L(2, \chi_{-3})` agreeing to `< (1/1000)^{20}`) locks the parameter-free `45`-sheet instanton ratio $\exp(-\frac{45}{\pi}\operatorname{Vol}(m004)) \in (235/10^{15}, 236/10^{15})$ and `2`-loop $\mathrm{SU}(3)$ confinement ratio $\Lambda_{\mathrm{IR}} / M_{\mathrm{UV}} \in (373/10^{17}, 374/10^{17})$, paired with `PC_AP3_ClassicalHiggsMassScaleHomogeneity` (`Picard–Lindelöf scaling residual < (1/1000)^{19}`, keeping $v_{\mathrm{EW}}$ explicitly priced in Tier `III`).

---

## 2. Gate-by-Gate Audit Summary (`Mask-Clean`)

1. **`Part 3A` (`E1_HosotaniG422_CenterLock_and_ModularInvariance_Gate_passed = True`):**
   - Origin quadratic trace `-10` vs `+8`; global minimum at exact center `(1, 1)` ($U_i^* = -I_2$) with Hessian eigenvalues `> 12` and exact `0` $\mathrm{SL}_2(\mathbb{Z})$ `(T, S)` residual on the invariant hyperbolic disk.
2. **`Part 3B` (`E2_M004SpinBordism_and_CuspSpinorConfinement_Gate_passed = True`):**
   - Genus-`1, 2, 3` Seifert $\mathrm{Spin}(2)$ holonomy equals $-I_2$ to `< (1/1000)^{18}`; both `m004` spin structures satisfy $\lambda_1 > 20 > 3$, locking unconditional `Branch B` minimum $u^* = m_{\mathrm{spin}} L_4^* \in (402/100, 403/100)$ (`gradient < (1/1000)^{16}`, curvature `> 70`).
3. **`Part 3C` (`E3_NonperturbativeScaleHierarchy_and_TierIIIGate_passed = True`):**
   - `50`-digit $\operatorname{Vol}(m004)$ two-route agreement `< (1/1000)^{20}`, `45`-sheet instanton + `2`-loop $\mathrm{SU}(3)$ exponential scale ratios verified, and classical $\mu_H^2(t)$ scale homogeneity verified to `< (1/1000)^{19}`.

`0 of 19.`
