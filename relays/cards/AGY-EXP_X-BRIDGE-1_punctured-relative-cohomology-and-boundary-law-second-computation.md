# Card `X-BRIDGE-1` — Punctured vs Closed Mapping-Torus Cohomology Repair (`H^2(X, dX; Z) ~= Z`), Blind `80`-Digit Second Computation of the Relative-Register Boundary Law (`a00bcb88e`), and Rank-`3` Principal-Parts End-Unit Theorem (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Context:** First sealed stage of Campaign `X-BRIDGE` (`four stages, sixteen blind-sealed commits, 0 of 19`), directly executing the pure-math topological repair (`REVIEW.md` Section `1`) and delivering a blind, zero-import `80`-digit second computation of `physical`'s relative-register boundary-law packet (`a00bcb88e`, `STATUS_PHYSICAL.md` request `1`).
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_bridge_1_verify/` exists in the repository at this commit, and `physical`'s `check_boundary_law.py` and `run01/result.json` have not been opened prior to sealing this card, our standalone verifier, and our raw output.
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared.

---

## 1. The Package and the Questions

1. **Question `1A` (`Punctured vs Closed Mapping-Torus Cellular Complexes & Relative Cohomology Repair`):**
   - On the punctured-torus `m004` mapping torus $X = M_3^\circ$, does exact integer Smith normal form (`SNF`) of the cellular chain complex confirm $H_1(X; \mathbb{Z}) \cong \mathbb{Z}$, $H_2(X; \mathbb{Z}) = 0$, and ordinary $H^2(X; \mathbb{Z}) = 0$ (`whereas adding the invariant closed-fiber 2-cell recovers H^2(\overline{M}_3; Z) ~= Z`), while on the `4`-fold punctured cover $X^{(4)}$ `SNF` of $M^4 - I_2 = \begin{pmatrix}33 & 21\\21 & 12\end{pmatrix}$ yields invariant factors `(3, 15)` so $H^2(X^{(4)}; \mathbb{Z}) \cong \mathbb{Z}/3\mathbb{Z} \oplus \mathbb{Z}/15\mathbb{Z}$ (`preserving all 45 finite torsion classes`)?
   - Simultaneously, on the compact exterior pair $(X, \partial X)$, does the Seifert-surface boundary relation $[\lambda] = \partial[\Sigma_S] = 0 \in H_1(X; \mathbb{Z})$ force $i^*: H^1(X; \mathbb{Z}) \to H^1(\partial X; \mathbb{Z})$ to map $k \mapsto (k, 0)$ with longitude cokernel **`H^2(X, \partial X; Z) ~= Z`**, paired with the gauge-invariant relative invariant $N[A, \phi] = \frac{1}{2\pi}(\int_C F - \oint_{\partial C}\eta)$ (`\eta = A|_Y - d\phi`)?
2. **Question `1B` (`Blind 80-Digit Second Computation of the Relative-Register Boundary Law a00bcb88e`):**
   - Does an independently assembled non-uniform multi-cell quadratic Maxwell + boundary-phase KKT linear system reproduce to `< (1/1000)^20` (`< (1/1000)^23` at `85` digits) the conserved boundary current $d_Y *_Y \eta = 0$, Robin law $\frac{c_H}{G} i^*(*F) + \kappa *_Y \eta = 0$, exact Schur circulation $B_* = \frac{p}{r+p}\Phi$, screened curvature flux $\frac{p}{r+p}n$, and stiff/weak limits?
   - Does an independent finite-element variational BVP + `24`-node Gauss–Legendre radial quadrature on $D_R^2 \times S_L^1$ reproduce the smooth radial Maxwell solution $a(r) = B_0 r^2 / R^2$, $B_{0*} = \frac{\kappa G R}{2 + \kappa G R}n$ to `< (1/1000)^20`?
   - Across three distinct rational area cuts $A_C / A \in \{1/5, 3/8, 7/11\}$, does the same-action core/tail transition functional $\Gamma_{\mathrm{reg}}(\Phi) = \frac{c_H}{2 G A}\Phi^2$ exhibit exact cut-motion invariance (`0` drift) and uniform physical curvature $\Phi/A$, cleanly distinguishing it from an artificial localized seam-matter source (`whose total added flux cancels to 0 and whose effective stiffness varies across cuts`)?
3. **Question `1C` (`Rank-3 Principal-Parts End-Unit Theorem & Quadratic Sector Landscape`):**
   - Does direct numerical Wronskian/evaluation rank over level-$d$ Jacobi theta sections on $E_\tau$ confirm $\chi(V(m p)) - \chi(V) = 3m$ across $m \in \{-4..4\}$ for rank-`3` bundles, so that while the unrestricted quadratic minimum of $E_m = C m^2$ is $m = 0$, the unique nonzero sector minima $m \in \{-1, +1\}$ already carry $|\Delta\chi| = 3$ chiral modes (`with E_3 / E_1 = 9`)?

---

## 2. Deliverables and Definition of Done

1. **`Part 1A`:** Exact integer `SNF` chain/cochain homology and relative cohomology verifier + `80`-digit `2D` Gauss–Legendre Chern–Weil relative invariant verifier.
2. **`Part 1B`:** Non-uniform multi-cell KKT solver, smooth radial finite-element + Gauss–Legendre BVP solver, and `3`-cut same-action vs seam-source discriminator.
3. **`Part 1C`:** Rank-`3` Jacobi-theta section rank verifier across $m \in \{-4..4\}$ and quadratic sector minimum audit.

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_PuncturedAndRelativeCohomology_Gate` (`Part 1A`):** Punctured $H^2(X; \mathbb{Z}) = 0$, closed recovery $H^2(\overline{M}_3; \mathbb{Z}) \cong \mathbb{Z}$, `4`-fold punctured $H^2(X^{(4)}; \mathbb{Z}) \cong \mathbb{Z}/3\mathbb{Z} \oplus \mathbb{Z}/15\mathbb{Z}$, relative $H^2(X, \partial X; \mathbb{Z}) \cong \mathbb{Z}$, and `80`-digit Chern–Weil relative invariance `< (1/1000)^20` (`with reference-only curvature == 0`).
2. **`E2_BoundaryLaw_SecondComputation_Gate` (`Part 1B`):** Multi-cell KKT vs Schur error `< (1/1000)^20`, smooth radial BVP residual `< (1/1000)^20`, `3`-cut same-action drift `== 0`, and seam-source cut spread `> 5/100` with net added flux `== 0`.
3. **`E3_Rank3EndUnit_and_SectorMinimum_Gate` (`Part 1C`):** $\chi(V(m p)) - \chi(V) = 3m$ holds identically across $m \in \{-4..4\}$, unrestricted minimum is `{0}`, nonzero minima are `{-1, +1}` with $|\Delta\chi| = 3$, and $E_3 / E_1 = 9$.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage1_Bridge_Passed`:** `AST` check confirming zero disallowed imports and zero float literals inside all exact integer `SNF`/topology and rational Schur functions.
2. **`PC_BR1_DropBoundaryEta`:** Dropping $-\oint_{\partial C}\eta$ on a screened configuration violates integer relative quantization by `> 1/2`.
3. **`PC_BR1_OmitPhaseGaugeShift`:** Applying a bulk gauge shift $A \to A + d\alpha$ while omitting $\phi \to \phi + \alpha$ breaks local gauge invariance of $\eta$ by `> 5/100`.
4. **`PC_BR1_ReversedSourceSign`:** Flipping $\eta = A|_Y - d\phi \to A|_Y + d\phi$ reverses $B_*$, failing the Schur target by `> 1`.
5. **`PC_BR1_SeamSourceVsTransition`:** Placing an independent seam-matter phase on a trivially glued surface changes total added flux from $\Phi$ to `0` and shifts effective stiffness across cuts by `> 5/100`.

`0 of 19.`
