# Card `X-ENDGAME-4` — Target-Free `(L, R)` Bundle $\mathrm{SL}(2, \mathbb{C})$ Holonomy, Two-Route Adjoint Reidemeister–Ray–Singer Torsion, Plebanski $\operatorname{Spin}^+(3, 1)$ Soldering, and Parameter-Free Scale Hierarchy (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-15`
- **Context:** Fourth sealed stage of Campaign `X-ENDGAME` (`five stages, twenty blind-sealed commits, 0 of 19`). Connects combinatorial `(L, R)` non-cancellation on `m004`'s punctured-torus bundle directly to $\mathrm{SL}(2, \mathbb{C}) \cong \operatorname{Spin}^+(3, 1)$ hyperbolic holonomy, adjoint Reidemeister–Ray–Singer torsion (`4 sqrt(3)` in longitudinal trace framing and `1 / sqrt(3)` in meridian framing, cross-checked against `7`-level Kashaev quantum-dilogarithm state-sum asymptotics), `3+1`D Lorentzian Plebanski $B \wedge F$ = Palatini–Holst gravity, and parameter-free exponential scale generation.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_endgame_4_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared.

---

## 1. The Package and the Questions

1. **Question `4A` (`Combinatorial (L, R) Bundle Holonomy, Wada Polynomial, Porti Adjoint Torsion & Kashaev 1-Loop State Sum`):** Starting strictly from the `(L, R)` punctured-torus bundle presentation $\pi_1(m004) = \langle a, b, t \mid t a t^{-1} = a b a,\; t b t^{-1} = b a \rangle$ (`whose fiber abelianization is M = L R`) with **zero** embedded target literals (`AST`-verified), does unbiased complex Newton root-finding force a unique irreducible parabolic $\mathrm{SL}(2, \mathbb{C})$ geometry whose fiber puncture commutator $K = [a, b]$ automatically has $\operatorname{Tr}(K) = -2$, commutes with $t$, and recovers cusp modulus $\tau_{\mathrm{cusp}} = 2\sqrt{3}\,i$? Furthermore, do (i) two-presentation Wada twisted adjoint Fox minors, (ii) the exact parabolic Fox-bundle cochain complex (`via the free-group torus identity [t, K] = R_1 * ^{aba}R_2 * ^{ab}R_1^{-1} * ^K R_2^{-1}`), and (iii) `7`-point asymptotic extraction of Kashaev's finite quantum-dilogarithm sum $\langle 4_1 \rangle_N$ mutually verify $\operatorname{Vol}(m004)$, meridian torsion $|\mathbb{T}_{\mathrm{Porti}}(m004; \mu)| = 1/\sqrt{3}$ (`1-loop prefactor 3^{-1/4}`), trace-differential ratio $|d\operatorname{Tr}\rho(\lambda)/d\operatorname{Tr}\rho(\mu)| = 12$, and longitudinal torsion $|\mathbb{T}_{\mathrm{Porti}}(m004; \lambda)| = 4\sqrt{3}$?
2. **Question `4B` (`SL(2, C) = Spin+(3, 1) Lorentzian Homomorphism & 3+1D Plebanski Self-Dual B ^ F Soldering`):** Does `m004`'s $\mathrm{SL}(2, \mathbb{C})$ bundle holonomy map homomorphically onto orthochronous proper Lorentz transformations $\mathrm{SO}^+(3, 1)$, and does the complexified $\mathfrak{sl}(2, \mathbb{C})_+$ self-dual Plebanski pairing on soldered tetrads $B_+ = P_+(e \wedge e)$ reproduce the exact `3+1`D Palatini–Holst gravitational action (`while enforcing simplicity Re(B_+ ^ B_+) = 0`)?
3. **Question `4C` (`Parameter-Free Exponential Scale Hierarchy — Strict Dimensionless Ratios`):** Combining Stage `2`'s dynamically stabilized cusp area $A^*$ (`near tree-level 6 pi`), Stage `1`'s unified gauge trace and `4`-fold cover determinant $N_4 = 45$, and Stage `4`'s hyperbolic volume and `1`-loop torsion prefactor, what pure dimensionless exponential hierarchy ratios $\Lambda_{\mathrm{IR}} / \Lambda_{\mathrm{UV}}$ emerge from gravitational instantons and `1`-loop non-abelian dimensional transmutation (`|b_3| = 7` for `3` families) with zero continuous knobs?

---

## 2. Deliverables and Definition of Done

1. **`Part 4A` — Target-Free Bundle $\mathrm{SL}(2, \mathbb{C})$ Solver, Wada Polynomial, Exact Fox-Bundle Torsion, and Kashaev `1`-Loop Check:**
   - `AST`-verified zero-target solver on $\langle a, b, t \mid t a t^{-1} = a b a,\; t b t^{-1} = b a \rangle$ from four rational seeds; verify convergence (`spread < (1/1000)^{12}`), relation residuals `< (1/1000)^{12}`, $|\operatorname{Tr}(K) + 2| < (1/1000)^{12}$, $\|[K, t]\|_F < (1/1000)^{12}$, and $|-K_{0,1}/K_{0,0} - 2\sqrt{3}\,i| < (1/1000)^{12}$.
   - Verify $W_{\mathrm{bundle}}(u) + u^3 W_{\mathrm{Wirtinger}}(u) = 0$ across generic complex $u$ to `< (1/1000)^{12}`, interpolate exact polynomial coefficients of $(u - 1)(u^2 - 5u + 1)$ (`error < (1/1000)^{12}`), and verify $|W'_{\mathrm{bundle}}(1)| = 3$.
   - Construct the exact `m = 1` parabolic Fox-bundle cochain complex $0 \to C^0(\mathbb{C}^3) \to C^1(\mathbb{C}^9) \to C^2(\mathbb{C}^6) \to 0$ across two distinct unimodular bases of $\mathfrak{sl}_2(\mathbb{C})$: verify free-group reduction of $[t, K]$, peripheral pullback cocycle closure `< (1/1000)^{12}`, $|\operatorname{Tor}_{\mathrm{cohom}}(m004; \mu)| = 2/\sqrt{3}$ (`error < (1/1000)^{10}`, plus deformed check at $m = 3/2$ matching $2/\sqrt{(x^2-1)(5-x^2)}$ to `< (1/1000)^{10}`), character-variety $A$-polynomial trace ratio $|d\operatorname{Tr}\rho(\lambda)/d\operatorname{Tr}\rho(\mu)| = 12$ (`to < (1/1000)^8`), and Porti longitudinal torsion $|\mathbb{T}_{\mathrm{Porti}}(m004; \lambda)| = 4\sqrt{3}$ (`vs meridian 1/\sqrt{3}`).
   - Evaluate Kashaev's state sum $\langle 4_1 \rangle_N$ at $N \in \{100, 150, 200, 250, 300, 350, 400\}$ and extract its `7`-parameter asymptotic fit in $[N, \ln N, 1, N^{-1}, N^{-2}, N^{-3}, N^{-4}]$, verifying simultaneously $|2\pi c_N - \operatorname{Vol}(m004)| < (1/1000)^3$, $|c_{\ln N} - 3/2| < (1/1000)^2$, and $|\exp(c_0) - 3^{-1/4}| < (1/1000)^2$.
2. **`Part 4B` — $\mathrm{SL}(2, \mathbb{C}) \cong \operatorname{Spin}^+(3, 1)$ Homomorphism and `3+1`D Plebanski $B \wedge F$ = Palatini–Holst Identity:**
   - Verify $\Lambda(G)^T \eta \Lambda(G) = \eta$, $\det\Lambda(G) = +1$, $\Lambda(G)^0{}_0 \ge 1$, and exact bundle homomorphism relations on $(A, B, T)$ plus `10` random $\mathrm{SL}(2, \mathbb{C})$ pairs to `< (1/1000)^4`.
   - Across `10` random non-degenerate tetrads and Lorentz connections at rational Immirzi parameter $\gamma = 3/7$, verify Lorentzian self-dual projector identities ($\star^2 = -I$, $P_+^2 = P_+$, $\star P_+ = i P_+$), exact agreement between $\operatorname{Re}((i + 1/\gamma) B_+ \wedge F_+)$ and $\mathcal{L}_{\mathrm{Pal}} + (1/\gamma)\mathcal{L}_{\mathrm{Holst}}$, $\mathcal{L}_{\mathrm{Pal}} = 2(\det e) e^\mu_I e^\nu_J F^{IJ}_{\mu\nu}$, and simplicity $\operatorname{Re}(W_{BB}) = 0$, $\operatorname{Im}(W_{BB}) = -24\det(e)$ to `< (1/1000)^4`.
3. **`Part 4C` — Parameter-Free Dimensionless Scale Hierarchy Ledger:**
   - Compute Stage `2` stabilized area $A^*$ directly inside the standalone verifier (`confirming |A^* - 6\pi| < 2/1000`), evaluate semi-classical instanton hierarchy factors $(4\sqrt{3})^{-1/2}\exp(-k\operatorname{Vol}(m004)/(2\pi))$ for $k \in \{1, 4, 45, 180\}$, and evaluate `1`-loop non-abelian dimensional transmutation ratios $\exp(-2\pi \alpha_{\mathrm{UV}}^{-1}/7)$ under both pure-`2`D horotorus ($\alpha_{\mathrm{UV}}^{-1} = A^*$) and `3`D-bulk-weighted ($\alpha_{\mathrm{UV}}^{-1} = \operatorname{Vol}(m004) A^*$) Kaluza–Klein measures (`explicitly pricing the 2D vs 3D KK measure choice at 1 discrete bit`).

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_Bundle_Holonomy_Torsion_and_StateSum` (`Part 4A`):**
   - Four-seed bundle Newton spread, relation residuals, commutator errors, Wada identity residuals, and Fox-bundle cochain torsion errors against $2/\sqrt{3}$ (`meridian`) and $4\sqrt{3}$ (`Porti longitudinal`) are all `< (1/1000)^8`; `7`-point Kashaev state-sum extraction matches $\operatorname{Vol}(m004)$ to `< (1/1000)^3` and $3^{-1/4}$ to `< (1/1000)^2`.
2. **`E2_Spin31_and_Plebanski_Soldering` (`Part 4B`):**
   - All Lorentzian homomorphism, projector, Palatini–Holst Lagrangian, and simplicity identities across `m004` holonomy and `10` random tetrad/connection configurations hold to `< (1/1000)^4`.
3. **`E3_ParameterFree_Exponential_Hierarchy` (`Part 4C`):**
   - $|A^* - 6\pi| < 2/1000$, and both `1`-loop dimensional transmutation scale ratios (`2`D horotorus and `3`D-bulk-weighted) plus the `45`-sheeted `4`-fold cover instanton factor generate dimensionless infrared-to-ultraviolet hierarchies strictly `< (1/1000)^2` with zero continuous parameters.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage4_ZeroTargetLiterals`:** AST scan verifying zero disallowed imports and zero float literals or `sqrt(3)` calls inside the target-free bundle holonomy solver.
2. **`PC_ENDGAME4_AbelianLocusCohomologyFailure`:** Evaluating $d^0$ on the reducible abelian representation ($A = B = I_2$, $T = \begin{pmatrix}1&1\\0&1\end{pmatrix}$) drops $\operatorname{rk}(d^0)$ from `3` to `2` (`\dim H^0 = 1 \neq 0`), confirming non-acyclicity of $H^0$ when `(L, R)` non-cancellation is turned off.
3. **`PC_ENDGAME4_BrokenSimplicityConstraint`:** Replacing $B_+ = P_+(e \wedge e)$ by `10` generic self-dual `2`-forms violates $|\operatorname{Re}(W_{BB})| = 0$ (`minimum violation > 1/100`).
4. **`PC_ENDGAME4_EuclideanSignatureSelfDualMismatch`:** Replacing Minkowski $\eta$ by Euclidean $\operatorname{diag}(1, 1, 1, 1)$ flips $\star^2$ from $-I$ to $+I$ and breaks $P_+ = \frac{1}{2}(I - i\star)$ idempotency (`\|P_+^2 - P_+\|_F > 1/2`).

`0 of 19.`
