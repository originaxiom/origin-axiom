# Card `X-FOUNDATION-3` — First Zero-Import Execution of `PHYSICAL-C7` (`a5d9ab3c6`): Conifold Quotient & Symplectic Scale Neutrality, Lossless $S^2 \times \mathrm{SU}(2)$ Composite Register & Constrained Sewing, and Fibered `4`-Fold Cover Word Lift (`0 of 19`)

- **Seat:** `agy-exp`
- **Campaign / Stage:** `X-FOUNDATION` / `Stage 3` (`Commits 9–12` of `16`)
- **Cross-Seat Scope:** `a5d9ab3c6` (`physical` `PHYSICAL-C7` Discriminators `1, 2, 3, 8, 9, 10, 11, 12`), `85318a66f` (`main`), `358d61786` (`agy-002`), `d1c71f255` (`agy`)
- **Empirical Firewall:** Strictly `0 of 19` (`zero SM empirical values read, imported, or compared; zero float literals and zero complex literals module-wide`).

---

## 1. Mathematical Targets & Falsifiable Gates

1. **`Part 3A` (`Conifold Quotient Z_ij = P_i R_j, 50-Digit Hopf Period 1, & Symplectic Scale Neutrality` — `PHYSICAL-C7` Discriminators `1, 2, 3, 8`, `E1_ConifoldQuotient_HopfPeriod_and_ScaleNeutrality_Gate`):**
   - Verify the `4`-mode charge `(+1, +1, -1, -1)` invariant matrix $Z_{ij} = P_i R_j$ satisfies $\det Z = 0$ identically (`rank 1 away from vertex`) with unique balanced representative $\|P\| = \|R\| = t$ modulo $\mathrm{U}(1)$.
   - Verify real Gauss connection $A_{\mathrm{phase}} = \frac{\operatorname{Im}(P^\dagger dP) - \operatorname{Im}(R^\dagger dR)}{\|P\|^2 + \|R\|^2}$ (`rejecting wrong + sign in PC_FD3_WrongPlusSignConnectionFailsGauge`), integrate $\frac{1}{2\pi}\int_{S^2} F_{\mathrm{phase}} = 1$ to `50` digits on the primitive sphere $v = \bar{u}$ (`rejecting half-unit 1/2 when dropping R`), and verify `Discriminator 8`: common positive action scaling $\kappa > 0$ leaves $A_{\mathrm{phase}}$ and its Chern number `1` invariant while the exact reduced symplectic `2`-form $\omega_{\mathrm{red}} = d(t^2 A_{\mathrm{phase}})$ has **exact integral `0`** over $S^2$ (`proving the topological period does not falsely fix the overall action scale`).
2. **`Part 3B` (`Lossless S^2 x SU(2) Composite Register (A, W), Cross-Term Metric, Radial Chart, & Constrained Sewing` — `PHYSICAL-C7` Discriminators `9, 11, 12`, `E2_CompositeRegister_CrossTermMetric_and_PhaseSewing_Gate`):**
   - Construct $(u, v)/\mathrm{U}(1) \leftrightarrow (A = U J U^{-1}, W = U C^{-1}) \in S^2 \times \mathrm{SU}(2)$ and verify global invertibility independent of the local Hopf lift $U \mapsto U D_\phi$ (`< (1/1000)^5`).
   - Verify `C7` eqs. `(3)–(5)`: $ds_{\mathrm{quot}}^2 = 2\,dt^2 + \frac{t^2}{2}(\|dA - \frac{1}{2}[dW W^{-1}, A]\|^2 + \|dW W^{-1}\|^2)$ matches the `4`-form horizontal kinetic metric to `< (1/1000)^3` (`rejecting product metric without cross term in PC_FD3_DroppedCrossTermMetricError > 1/10`), $A_{\mathrm{phase}} = a_u - \frac{1}{2}\langle A, dW W^{-1}\rangle$, radial dictionary $v \mapsto e^{i\theta(t)}v$ produces `C7` eq. `(13)` extra kinetic term $\frac{t^2}{2}\theta'(t)^2 dt^2 > 0$ (`and distinct W limits at t -> 0`), and constrained fixed-holonomy energy `C7` eqs. `(4)–(5)` $\Delta^2 / R_\gamma$ composes across two intervals as $(\beta - I_1 - I_2)^2 / (R_1 + R_2)$ with exact seam current matching.
3. **`Part 3C` (`Static T^4 = I Word Obstruction & Fibered m004 4-Fold Cover Word Lift` — `PHYSICAL-C7` Discriminator `10`, `E3_NativeWordObstruction_and_4FoldFiberedLift_Gate`):**
   - Verify `C7` eqs. `(8)–(10)`: $\operatorname{tr}[A, W] = 2 - 4(|w|^2 - (n\cdot w)^2)$ (`equal to +2 across the entire primitive sphere W = I`), shear $v \mapsto i v$ realizes $T(A, W) = (A, A W)$ preserving the leading metric and $A_{\mathrm{phase}}$ with **exact order `4`** ($T^4 = \mathrm{id}$), while at $W = -A$ the complementary move sends $A \mapsto A W = +I_2$ (`leaving the traceless-A subfamily, PC_FD3_StaticSubfamilyExitsOnSecondMove`).
   - Prove and verify on the fibered register-modulus space $\mathbb{H}_\tau \times (S^2 \times \mathrm{SU}(2))$ that coupling $(L, R)$ to `m004`'s Möbius shears $M = LR = \begin{psmallmatrix} 2 & 1 \\ 1 & 1 \end{psmallmatrix}$ yields infinite hyperbolic order ($\operatorname{tr}(M^n) \to \infty$) while the minimal power trivializing `C7`'s order-`4` register shear $T^4 = \mathrm{id}$ is **$M^4$ (`|\det(M^4 - I_2)| = 45`, Smith invariants `(3, 15)`), structurally linking `C7`'s $A^4 = I$ relation to `m004`'s `4`-fold cyclic cover $X^{(4)}$**.

`0 of 19.`
