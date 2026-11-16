# Card `X-UNIFY-1` — `CRT` Gauge × Family Tensor Unification ($\mathcal{W}_{15} \cong \mathcal{W}_5^{\mathrm{gauge}} \otimes \mathcal{W}_3^{\mathrm{family}}$), Anomaly Hypercharge Lock, and Zero-Import Verification of `physical`'s `12`-Method `P-C3` Package (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-16`
- **Context:** First sealed stage of Campaign `X-UNIFY` (`four stages, sixteen blind-sealed commits, 0 of 19`), resolving the repository-wide Color-`3` vs Family-`3` collision via `m004`'s `4`-fold punctured torsion $\mathbb{Z}/3\mathbb{Z} \oplus \mathbb{Z}/15\mathbb{Z}$, restoring `physical`'s exact $c_H = \kappa(H^2)$ classical trace-norm type distinction (`ca500dad6`), and executing the first-ever independent zero-import scientific run of all `12` exact mathematical methods in `physical`'s sealed `P-C3` package (`ca02b5d8d`).
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_unify_1_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured quantities read, imported, or compared.

---

## 1. The Package and the Questions

1. **Question `1A` (`CRT Tensor Factorization W_15 ~= W_5 (x) W_3, Anomaly Hypercharge Lock, Cusp Spin Registration, & c_H Type Restoration`):**
   - On `m004`'s `4`-fold punctured cover ($H^2(X^{(4),\circ}; \mathbb{Z}) \cong \mathbb{Z}/3\mathbb{Z} \oplus \mathbb{Z}/15\mathbb{Z}$, Smith invariants `(3, 15)`), does Chinese Remainder Theorem ($\gcd(3, 5) = 1$, $x \equiv 3 u + 5 v \pmod{15}$) factorize the `15`-dimensional finite Weil representation $(T_{15}, S_{15})$ to `< (1/1000)^15` into commuting tensor factors $(T_5^{(3)} \otimes T_3^{(2)},\, S_5^{(3)} \otimes S_3^{(2)})$ on $\mathcal{W}_5 \otimes \mathcal{W}_3$?
   - Under parity $C_5 = (S_5^{(3)})^2$, does $\mathcal{W}_5$ split canonically into $3_c \oplus 2_w$ whose even exterior algebra $\Lambda^{\mathrm{even}}(\mathcal{W}_5)$ has dimension `16` ($1 \oplus 10 \oplus \bar{5}$) commuting identically (`0` commutator norm) with the mod-`3` family algebra $\operatorname{End}(\mathcal{W}_3)$, and does vanishing of the `4` gauge/gravitational anomalies ($A_{\mathrm{SU(3)}^2\mathrm{U(1)}}, A_{\mathrm{SU(2)}^2\mathrm{U(1)}}, A_{\mathrm{grav}^2\mathrm{U(1)}}, A_{\mathrm{U(1)}^3}$) uniquely force $3a + 2b = 0 \implies 6Y = \operatorname{diag}(-2, -2, -2, 3, 3)$ and exact $k_2 / k_1 = 3/5$ with `0` free charge parameters?
   - Does restoring `physical`'s classical generator trace norm $c_H = \kappa(H^2)$ cleanly separate $\Gamma_{\mathrm{reg}}(\Phi) = \frac{c_H}{2 G A}\Phi^2$ from the seam-phase Robin stiffness $\kappa_{\mathrm{seam}}$, and how does half-integral antiperiodic spin registration $q \in \mathbb{Z} - \frac{1}{2}$ (`where 0 is absent`) compare with untwisted integer registration $m \in \mathbb{Z}$ (`where m = 0 minimizes m^2 unless excluded`)?
2. **Question `1B` (`Zero-Import Independent Verification of All 12 Sealed P-C3 Methods, ca02b5d8d`):**
   - Built standalone from first principles with **zero imports** from `reports/` or `checks.py`, do all `12` exact mathematical claims of `physical`'s `P-C3` package (`quaternion SO(3) vs unsigned det = -1, full & traceless M_3(C) rank-9 span, SL_2(C) covariance + traceless-S unsigned counterexample, Q_8 deck/inverse-argument cancellation + vertical spin sheet, rank-17 constant stabilizer on full & 5-slot families, antisymmetric cubic polarization, SU(5) root mass-derivative identity 5i, normalized |y|^2 / e_H^2 = 2 A_omega A_g / I_omega^2 rescaling invariance, Cauchy–Schwarz shape inequality >= 2 on flat/periodic/hyperbolic-collar metrics, pure-slot rank <= 2 rule, full-complement second-order V_2 - b c / d response m_2 = 2/3, and complex-bilinear transpose S_L^{-T} Y S_R^{-1} + Hermitian current transport`) hold identically (`SAME` across `12 of 12` methods)?

---

## 2. Deliverables and Definition of Done

1. **`Part 1A`:** `55`-digit + exact symbolic verification of $\mathcal{W}_{15} \cong \mathcal{W}_5^{\mathrm{gauge}} \otimes \mathcal{W}_3^{\mathrm{family}}$, exact anomaly polynomial factorization $A_{\mathrm{U(1)}^3} = 4(3a + 2b)((3a + b)^2 + 4b^2)$, exact $k_2/k_1 = 3/5$ derivation, $c_H = \kappa(H^2)$ vs $\kappa_{\mathrm{seam}}$ independence check, and untwisted vs half-integral spin registration audit.
2. **`Part 1B`:** Complete zero-import `sympy` + `80`-digit `mpmath` countercheck of all `12` `P-C3` methods (`M01..M12`) plus hyperbolic cusp metric $\Omega(y) = 1/y$ strict inequality check.

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_CRT_GaugeFamily_and_Anomaly_Gate` (`Part 1A`):** $P_{\mathrm{CRT}} T_{15} P_{\mathrm{CRT}}^\dagger = T_5^{(3)} \otimes T_3^{(2)}$ and $P_{\mathrm{CRT}} S_{15} P_{\mathrm{CRT}}^\dagger = S_5^{(3)} \otimes S_3^{(2)}$ hold to `< (1/1000)^15`; $\dim \mathcal{W}_5^+ = 3$, $\dim \mathcal{W}_5^- = 2$, $\dim \Lambda^{\mathrm{even}}(\mathcal{W}_5) = 16$, and gauge-vs-family commutator norm equals `0`; $A_{\mathrm{U(1)}^3} = 0$ over $\mathbb{R} \setminus \{(0,0)\}$ uniquely forces $3a + 2b = 0$ and $k_2/k_1 = 3/5$; and $c_H = \kappa(H^2)$ is strictly independent of $\kappa_{\mathrm{seam}}$ in the stiff-seam limit.
2. **`E2_PC3_TwelveMethod_Independent_Gate` (`Part 1B`):** All `12` `P-C3` methods (`M01` through `M12`) pass in exact symbolic arithmetic (`with 80-digit mpmath numerical cross-checks < (1/1000)^20`), confirming `SAME` on every algebraic claim and hyperbolic collar bound $|y|^2 / e_H^2 > 2$.

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage1_Unify_Passed`:** `AST` check confirming zero disallowed imports (`zero imports from reports/ or main`) and zero float literals across the entire verifier.
2. **`PC_U1_NonCoprimeLevel9Failure`:** Replacing coprime $15 = 5 \times 3$ by non-coprime $9 = 3 \times 3$ breaks tensor factorization of $T_9$ by `> 1`.
3. **`PC_U1_UnbalancedHyperchargeAnomaly`:** Setting $(a, b) = (-1, 1)$ (`3a + 2b != 0`) produces nonzero gauge and cubic anomalies `(|A_cubic| >= 32)`.
4. **`PC_U1_UnsignedLiftAndWrongSideDeck`:** Unsigned $|O_g|$ fails quarter-turn $\det = +1$ (`giving -1`) and fails traceless-$S$ covariance, while right-multiplied deck argument $k h^{-1}$ fails $Q_8$ section equivariance.
5. **`PC_U1_WrongHermitianVsTransposeGramAndConnectionWeight`:** Using $S_L^{-H} Y S_R^{-1}$ instead of $S_L^{-T} Y S_R^{-1}$ breaks complex-bilinear transport, and setting `connection_weight = 1` instead of `1/2` halves $|y|^2 / e_H^2$ to `1` instead of `2`.

`0 of 19.`
