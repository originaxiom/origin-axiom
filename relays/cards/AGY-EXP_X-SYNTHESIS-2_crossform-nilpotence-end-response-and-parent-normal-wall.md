# Card `X-SYNTHESIS-2` — Complete `(hV)^4 = 0` Cross-Form Nilpotence Proof, Same-Action End Response $\Gamma(s_0)$, Parent $E_6$ Normal Wall Equation, and Operator-Derived Two-State Singlet Sewing (`0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-17`
- **Context:** Second sealed stage of Campaign `X-SYNTHESIS` (`four stages, sixteen blind-sealed commits, 0 of 19`), executing `physical` `PHYSICAL-C5` (`407583a8c`: `CROSS_FORM_FINITE_SERIES.md`, `SAME_ACTION_END_RESPONSE.md`, and `ACTUAL_SOURCE_NORMAL_TEST.md`) by proving complete matrix nilpotence $(h_{10}V_{01})^2 = (h_{21}V_{12})^4 = (h_{32}V_{23})^4 = 0$ and `25D` $5_+ \otimes 5_-$ uniqueness of the cross-form completion, verifying the nonlinear Dirichlet-to-Neumann end response $\Gamma(s_0)$ and variational composition law $\Gamma_{L+R}(a, c)$, computing **both sides of the parent normal equation** $P_\perp (D R_{X_s})^* C = \frac{B s(1-s)}{K(s)}\,\mathrm{II}_s$ (`plus transverse relaxation`) on an explicit $E_6$ path, and testing whether a horizontal two-state transition (`between axes k and j`) lifts the `3rd` singlet pair directly from the coupled operator without an assigned `eps_end` entry.
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_synthesis_2_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured Standard Model quantities read, imported, or compared (`0` float literals and `0` complex literals module-wide).

---

## 1. The Package and the Questions

1. **Question `2A` (`Complete (hV)^4 = 0 Nilpotence Proof & Full 25D Cross-Module Uniqueness`):**
   - On `16 -> 48 -> 48 -> 16`, do $d_0 h + h d_0 = I - P$ (`across all four total degrees`) and the explicit matrix powers $(h_{10}V_{01})^2 = 0$, $(h_{21}V_{12})^4 = 0$, and $(h_{32}V_{23})^4 = 0$ hold identically in `SymPy` (`certifying zero omitted HPT tail beyond k = 3`), and searching over the **entire `25`-dimensional $5_+ \otimes 5_-$ cross-module** (`not merely a 4-monomial ansatz`), is $a_{\mathrm{exact}}$ the unique `1`-dimensional centralizer of $(E_+ + f_+ T_{(3,+)}, E_- + f_- T_{(3,-)})$ inside $5_+ \otimes 5_-$?
2. **Question `2B` (`Same-Action End Response \Gamma(s_0) & Parent E_6 Normal Wall Equation`):**
   - Do $\Gamma(s_0) = 2\int_0^{s_0}\sqrt{K(u)V(u)}\,du$, $\Gamma'(s_0) = -2 K(s_0) s'(0)$, wall tension $T_{\mathrm{path}}$, and $\Gamma_{L+R}(a, c) = \inf_b[\Gamma_L(a, b) + \Gamma_R(b, c)]$ hold to `< (1/1000)^8`, does `physical`'s `2`-field rejecting comparator detect $\partial_y V|_{y=0} = -2 c x(1-x) \ne 0$, and on an explicit finite-mode $E_6$ affine path $X_s = (A_s, q_s, r_s)$ (`with real Gauss inverse L_s^+ b_s and exact 1/2 connection vs \Omega spin metrics`), what is the exact normal residual $P_\perp(D R_{X_s})^* C - \frac{B s(1-s)}{K(s)}\,\mathrm{II}_s$ before vs after transverse orthogonal relaxation?
3. **Question `2C` (`Operator-Derived Two-State Sewing Test on the 3rd Singlet Pair`):**
   - Coupling two adjacent state-axis cells (`axis k and rotated axis j`, where the $2O$ rotation $g_j$ permutes the core character/spinor alignment) via a horizontal hopping kinetic term without any hand-inserted `eps_end` entry, does the coupled `2`-cell singlet Dirac/Dolbeault operator lift the zero-mode pair that was protected inside a single axis?

---

## 2. Pre-Registered Expectations and Mandatory Controls

1. **`E1_CrossFormNilpotence_and_25DUniqueness_Gate` (`Part 2A`):** Symbolic `SDR` $d_0 h + h d_0 = I - P$ holds in all `4` degrees, $(h_{10}V_{01})^2 = 0$, $(h_{21}V_{12})^4 = 0$, $(h_{32}V_{23})^4 = 0$ (`recording exact minimal nilpotency indices in {1, 2, 3, 4}`), and the centralizer dimension inside `25D` $5_+ \otimes 5_-$ equals `1` (`spanned uniquely by a_{\mathrm{exact}}`).
2. **`E2_SameActionEndResponse_and_ParentNormalTest_Gate` (`Part 2B`):** $\Gamma'(s_0) + 2 K(s_0) s'(0) = 0$ and two-segment momentum-balance $\Gamma_{L+R}(a, c)$ hold to `< (1/1000)^8`; real gradient check $\langle \operatorname{grad} V(X), Y\rangle_{\mathrm{chiral}} = \left.\frac{d}{d\epsilon} V(X + \epsilon Y)\right|_0$ holds to `< (1/1000)^3` (`proving exact chiral vs residual metric adjoints!`); and transverse orthogonal relaxation reduces the full Euler–Lagrange gradient norm below `(1/1000)^3` (`to machine precision`).
3. **`E3_TwoStateOperatorSewing_SingletTest_Gate` (`Part 2C`):** Deterministic evaluation of the coupled two-state `16_+` operator (`verifying single-state uncoupled control keeps exact zero singular values while recording the exact coupled singular-value spectrum and unitary basis-scrambling invariance < (1/1000)^5`).
4. **Mandatory Rejecting Controls:** `Gate_AST_Stage2_Synthesis_Passed` (`0` float literals, `0` complex literals module-wide), `PC_SY2_TwoFieldStraightPathNormalFailure` (`nonzero normal residual ||\partial_y V|| > 1/10` on straight $y = 0$), and `PC_SY2_ConfusedMetricBreaksAdjoint` (`omitting the 1/2 connection / \Omega spin factor breaks \langle 2(DR)^*R, Y\rangle = dV/d\epsilon by > 1/10`).

`0 of 19.`
