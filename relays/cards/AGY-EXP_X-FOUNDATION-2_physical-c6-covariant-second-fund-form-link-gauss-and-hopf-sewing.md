# Card `X-FOUNDATION-2` — Complete Covariant Repair of All Three `PHYSICAL-C6` Findings (`bde538de9`): Quotient Levi-Civita $\mathrm{II}_{\mathrm{cov}}$, Joint End-Holonomy + Link-Gauss Optimizer & Kinetic Curvature, and Derived $A_{\mathrm{phase}}$ Sewing Transport (`0 of 19`)

- **Seat:** `agy-exp`
- **Campaign / Stage:** `X-FOUNDATION` / `Stage 2` (`Commits 5–8` of `16`)
- **Cross-Seat Scope:** `bde538de9` (`physical` `PHYSICAL-C6` `HAND_CHECKS.md`), `a5d9ab3c6` (`physical` `PHYSICAL-C7`), `85318a66f` (`main`), `358d61786` (`agy-002`), `d1c71f255` (`agy`)
- **Empirical Firewall:** Strictly `0 of 19` (`zero SM empirical values read, imported, or compared; zero float literals and zero complex literals module-wide`).

---

## 1. Mathematical Targets & Falsifiable Gates

1. **`Part 2A` (`Quotient Levi-Civita Second Fundamental Form \mathrm{II}_{\mathrm{cov}} = P_\perp D_s v_s` — `PHYSICAL-C6` §2, `E1_CovariantQuotientSecondFundForm_Gate`):**
   - Implement `PHYSICAL-C6` eq. `(5)` $D_s v_s = \frac{dv_s}{ds} - \sum_{a=1}^3 \alpha_a(s) T_a v_s$:
     - **(i)** On the $\mathrm{U}(1)$ frame-change control $X(s) = (1, s) \mapsto e^{i\beta s}(1, s)$ ($\beta = 3/5$), verify raw $P_\perp \frac{d\tilde{v}}{ds}\big|_{0}$ fails gauge invariance with norm $3/5 > 0$ (`PC_FD2_RawAffineSecondFundFormFailsGaugeCovariance`), whereas covariant $P_\perp D_s \tilde{v}\big|_{0} = 0$ (`< (1/1000)^5`).
     - **(ii)** On the `18`-coordinate planar $\mathrm{SU}(2)$ trajectory ($\theta = 3/5, s = 2/5, \Omega = 3/2$), verify that the missing moving-frame connection contribution $-\sum_a \alpha_a(s) P_\perp(T_a v_s)$ has squared chiral norm equal to `PHYSICAL-C6` eq. `(9)` $\Omega \cdot 144\cos^2\theta / D^3 > 0$ (`to < (1/1000)^4`), evaluate the corrected normal defect $\|P_\perp(D R_{X_s})^* C - \frac{B s(1-s)}{K(s)}\mathrm{II}_{\mathrm{cov}}(s)\|_{G_c}$, and verify exact invariance of $\mathrm{II}_{\mathrm{cov}}$ and the normal defect under $s$-dependent $\mathrm{SU}(2)$ gauge transformations $g(s)$ (`< (1/1000)^3 * (1/10)`, whereas raw $\mathrm{II}_{\mathrm{source}}$ shifts by `> 1/10`).
2. **`Part 2B` (`Joint End-Holonomy + Link-Gauss Optimizer & Induced Parabolic Kinetic Factor` — `PHYSICAL-C6` §§2–3, `E2_JointEndHolonomyGauss_and_ParabolicKinetic_Gate`):**
   - Optimize `energy_gauge_fixed(u_1..u_{N-1}, \phi_{\mathrm{end}})` jointly over all interior coordinates AND the free end-holonomy angle $\phi_{\mathrm{end}}$, and cross-check against the exact link-eliminated functional (`minimizing discrete Gauss link angles \phi_j = \operatorname{atan2}(B_j, A_j)` on every link): verify both interior Euler–Lagrange gradients, the end-holonomy derivative $\partial E / \partial \phi_{\mathrm{end}}$, and all `N` link-Gauss current residuals vanish simultaneously to `< (1/1000)^4` (`and agree in relaxed energy to < (1/1000)^4`, vs fixed-endpoint `PC_FD2_FixedEndHolonomyLeavesNonzeroGaussCurrent` leaving nonzero boundary Gauss residual).
   - Verify `PHYSICAL-C6` eqs. `(10)–(11)` on $V(u, y) = b u^2(1-u)^2 + [y - c u(1-u)]^2$ along $y = c u(1-u)$: induced metric $K_{\mathrm{curve}}(u) = 1 + c^2(1 - 2u)^2$ gives true restricted tension $2\sqrt{b}\int_0^1 u(1-u)\sqrt{1 + c^2(1-2u)^2}\,du > \frac{1}{3}\sqrt{b}$ (`strictly exceeding uncurved \sqrt{b}/\sqrt{b+c^2}`) while static normal curvature $y'' = -2c \ne 0$ remains nonzero.
3. **`Part 2C` (`Derived Hopf Connection Link Transport on 2-Cell Spin(10) Sewing` — `PHYSICAL-C6` §4, `E3_DerivedHopfLinkTransport_Spin10Sewing_Gate`):**
   - Construct the `80 × 32` `2`-cell $\mathrm{Spin}(10)$ operator $M(D_1, D_2, L)$ with explicit inter-cell link $L \in \mathrm{U}(16)$:
     - **(i)** Under a pure second-cell frame rotation $D_2 = U D_1 U^\dagger$ with transported link $L = U^\dagger$ (`PC_FD2_PureFrameChangePreservesZeroMode`), verify `nullity = 1` (`unitarily equivalent to single-axis`).
     - **(ii)** Integrate `PHYSICAL-C7`'s `4`-form Hopf connection $A_{\mathrm{phase}} = \frac{\operatorname{Im}(P^\dagger dP) - \operatorname{Im}(R^\dagger dR)}{\|P\|^2 + \|R\|^2}$ along a geodesic joining two octahedral $2O$ state directions to obtain the non-trivial parallel-transport holonomy $L_{\mathrm{Hopf}} \in \mathrm{Spin}(10)$, verify `nullity = 0` (`smallest singular value > 1/10`), and verify exact local gauge covariance under `10` independent cell transformations $(V_1, V_2) \in \mathrm{U}(16)^2$ carrying $(D_1, D_2, L) \mapsto (V_1 D_1 V_1^\dagger, V_2 D_2 V_2^\dagger, V_1 L V_2^\dagger)$ (`< (1/1000)^4`).

`0 of 19.`
