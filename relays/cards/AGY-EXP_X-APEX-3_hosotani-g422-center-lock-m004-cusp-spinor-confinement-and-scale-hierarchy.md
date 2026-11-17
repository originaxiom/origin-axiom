# Card `X-APEX-3` — `1`-Loop Hosotani $G_{422}$ Center-Locking Theorem, Seifert-Longitude Spin-Bordism Obstruction & Hyperbolic Cusp Spinor Confinement on `m004`, and `50`-Digit Nonperturbative Scale Hierarchy Ledger (`0 of 19`)

- **Seat:** `agy-exp`
- **Campaign / Stage:** `X-APEX` / `Stage 3` (`Commits 9–12` of `16`)
- **Cross-Seat Scope:** `M40`, `407583a8c` (`physical` `PHYSICAL-C4` Finding `4` `PR-10` cusp spinor gap), `f877e0481` (`agy-002` `SU(2)_R` holonomy duty), `d1c71f255` (`agy` `stage1 v17`)
- **Empirical Firewall:** Strictly `0 of 19` (`zero SM empirical values read, imported, or compared; zero float literals and zero complex literals module-wide`).

---

## 1. Mathematical Targets & Falsifiable Gates

1. **`Part 3A` (`1`-Loop Hosotani $G_{422}$ Wilson-Line Potential & Unfluxed Center-Locking Theorem — `E1_HosotaniG422_CenterLock_and_ModularInvariance_Gate`):**
   - Formulate the exact `6D -> 4D` `1`-loop Hosotani winding potential $V_{\mathrm{Hos}}(\alpha_1, \alpha_2; \tau)$ along $T_{3R} \in \mathfrak{su}(2)_R$ on $E_{\tau = i\sqrt{3}}$ for `Pati–Salam` $G_{422}$ gauge vectors (`8` real on-shell dof at $|q| = 1$), `27_H` scalars (`24` real dof at $|q| = 1/2$), and `3` chiral `16_F` families (`96` real Weyl dof at $|q| = 1/2$).
   - Verify: (i) at the trivial origin $\vec{\alpha} = (0, 0)$ ($U_i = +I_2$), pure gauge (`PC_AP3_PureGaugeHosotaniStaysUnbroken`) has strictly positive-definite Hessian (`+8` weight), whereas $G_{422} + 3\times 16_F + 27_H$ has strictly **negative-definite** Hessian (`8 + 6 - 24 = -10 < 0`), dynamically destabilizing $(+I_2, +I_2)$; (ii) guarded Newton + global grid minimization converges to the unique global minimum $\vec{\alpha}^* = (1, 1) \pmod 2$, i.e. $(U_1^*, U_2^*) = (-I_2, -I_2) \in Z(\mathrm{SU}(2)_R)^2$ (`dynamically enforcing the half-integer characteristic shift (1/2, 1/2) on doublets with positive-definite Hessian > 0 and exact SL_2(Z) modular invariance < (1/1000)^4`); and (iii) because $(-I_2, -I_2)$ is central in $\mathrm{SU}(2)_R$, unfluxed flat Hosotani dynamics preserves $|V_{33}| = 1$ (`proving non-central T_{3R} = \pm 1/2 holonomy splitting requires quantized magnetic flux / m004 torsion holonomy or adjoint fermions as in PC_AP3_AdjointFermionSplitsCenter`).
2. **`Part 3B` (`Seifert-Longitude Spin-Bordism Obstruction & 45-Digit Hyperbolic Cusp Spinor Confinement on m004 — `E2_M004SpinBordism_and_CuspSpinorConfinement_Gate`):**
   - Prove algebraically in $\mathrm{Spin}(2)$ that along the canonical boundary $\lambda = \partial\Sigma_{g,1}$ of any compact orientable genus-$g$ Seifert surface (`g = 1` for `m004`), the tangent winding number $\chi(\Sigma_{g,1}) = 1 - 2g$ is odd, lifting in $\mathrm{Spin}(2)$ to $R(2\pi(1 - 2g)) = -I_2$ and topologically forbidding the periodic `(0, 0)` cusp spin structure (`restricting both spin structures of m004 to (\epsilon_\mu, \epsilon_\lambda) \in {(0, 1/2), (1/2, 1/2)}`).
   - Compute in `50`-digit precision via exact analytic sine-basis Rayleigh–Ritz matrices on $L^2([0, L_y], dy)$ for the volume-flattened hyperbolic cusp squared Dirac operator $\widetilde{D}_{\mu_\perp}^2 = -\partial_y^2 + \mu_\perp^2 e^{2y} - \mu_\perp e^y$ across $L_y \in \{4, 5\}$ that all `3` non-periodic spin structures satisfy $\lambda_1 > 20 > 3$ with $|L_y = 4 - L_y = 5| < 3 * (1/1000)^2$ (`unconditionally selecting PR-10 Branch B L_4^* > 0 with V(L_4^*) < 0 and V''(L_4^*) > 0`), whereas `PC_AP3_PeriodicCuspSpinorZeroGap` `(0, 0)` collapses as $\pi^2 / L_y^2 \to 0$.
3. **`Part 3C` (`50-Digit Nonperturbative Instanton & Confinement Scale Hierarchy Ledger — `E3_NonperturbativeScaleHierarchy_and_TierIIIGate`):**
   - Compute to `50` digits across two independent target-free routes (`gluing dilogarithm vs joint 3D+2D Newton saddle`) the `45`-sheet instanton suppression $\exp(-\frac{45}{\pi}\operatorname{Vol}(m004))$ and `2`-loop $\mathrm{SU}(3)$ confinement ratio $\Lambda_{\mathrm{IR}} / M_{\mathrm{UV}}$ from $\alpha_{\mathrm{UV}}^{-1} = \operatorname{Vol}(m004) A_{\mathrm{Cas}}^*$, paired with `PC_AP3_ClassicalHiggsMassScaleHomogeneity` verifying homogeneous Picard–Lindelöf scaling of $\mu_H^2(t)$ (`pricing v_EW in Tier III`).

`0 of 19.`
