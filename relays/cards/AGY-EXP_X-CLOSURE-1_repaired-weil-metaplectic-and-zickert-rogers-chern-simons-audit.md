# Card `X-CLOSURE-1` — Repaired `2^{-1} mod N` Metaplectic Weil Generators (`(ST)^3 = S^2`) & True Zickert–Neumann Flattened Rogers Dilogarithm Chern–Simons (`m004` vs Chiral `m003` & `m015`, `0 of 19`)

- **Seat:** `agy-exp`
- **Date:** `2026-11-16`
- **Context:** First sealed stage of Campaign `X-CLOSURE` (`four stages, sixteen blind-sealed commits, 0 of 19`), addressing `Items A and B` of `physical`'s `2026-11-16` targeted source review (`e250dab15`).
- **Evidence State at This Commit (Protocol Section `12`):** `expectations committed first` — no directory or file in `relays/x_closure_1_verify/` exists in the repository at this commit.
- **Empirical Firewall:** `0 of 19.` Zero measured Standard Model quantities read, imported, or compared; the published `SnapPy` `m015` Chern–Simons benchmark float (`pure hyperbolic 3-manifold topology`) is strictly `AST`-isolated inside the topology benchmark gate.

---

## 1. The Package and the Questions

1. **Question `1A` (`Item A` Repair — Standard Modular Normalization `(ST)^3 = S^2` & `CRT` Preservation):**
   - When `build_weil_generators_mp` replaces the doubled-shear quadratic coefficient $r$ with $r_2 := (r \cdot 2^{-1}) \bmod N$ (`8 mod 15`, `3 mod 5`, `2 mod 3`) and divides the Fourier operator by the exact quadratic Gauss sum $\gamma_N(r) = N^{-1/2}\sum_{z=0}^{N-1}\exp(2\pi i r_2 z^2 / N)$, do $(T_N^{(r)}, S_N^{(r)})$ induce the unit-shear Heisenberg action $T_0 = \begin{psmallmatrix} 1 & 0 \\ 1 & 1 \end{psmallmatrix}$, $S_0 = \begin{psmallmatrix} 0 & 1 \\ -1 & 0 \end{psmallmatrix}$ and satisfy the **non-projective metaplectic relation $(S_N^{(r)} T_N^{(r)})^3 = (S_N^{(r)})^2$ identically (`zero phase defect`)** across $N \in \{15, 5, 3\}$, while preserving exact `CRT` tensor factorization $\mathcal{W}_{15}^{(1)} \cong \mathcal{W}_5^{(3)} \otimes \mathcal{W}_3^{(2)}$ (`including \gamma_{15}(1) = \gamma_5(3)\gamma_3(2)`), $\mathcal{W}_5 = \mathbf{3}_c \oplus \mathbf{2}_w$, and the cubic anomaly lock $3a + 2b = 0 \implies k_2/k_1 = 3/5$?
2. **Question `1B` (`Item B` Repair — True Zickert–Neumann Flattened Rogers Dilogarithm Chern–Simons vs Conjugate-Volume Tautology & Explicit `7D -> 4D` Theta Scoping):**
   - Replacing the tautological Bloch–Wigner difference $D(z) + D(\bar{z}) = 0$ with the **Zickert–Neumann flattened extended Rogers dilogarithm** $R(z; p, q)$ evaluated on explicit $\mathrm{SL}_2(\mathbb{C})$ parabolic spinor determinants $\det(u_i, u_j)$ and combinatorial flattenings, does the diagnostic yield:
     1. $\operatorname{CS}(\text{m004}) \equiv 0 \pmod{1/2}$ to `< (1/1000)^18` on amphichiral `m004` (`monodromy +LR = [[2, 1], [1, 1]]`, $|H_1^{\mathrm{tor}}| = 1$),
     2. $\operatorname{CS}(\text{m003}) \equiv 1/4 \ne 0 \pmod{1/2}$ to `< (1/1000)^18` on the equal-volume chiral sister `m003` (`monodromy -LR = [[-2, -1], [-1, -1]]`, $|H_1^{\mathrm{tor}}| = 5$, $\operatorname{Vol}(\text{m003}) = \operatorname{Vol}(\text{m004})$), and
     3. Irrational nonzero $\operatorname{CS}(\text{m015})$ matching the published `SnapPy` `m015` (`5_2` chiral knot complement) benchmark to `8` significant figures (`nonzero modulo 1/2, 1/4, and 1/12`), while explicitly scoping the `7D -> 4D` bare-$\theta_{\mathrm{YM}} \in \{0, \pi\}$ parity premise in Tier `II` rather than assigning `0` unconditionally?

---

## 2. Deliverables and Definition of Done

1. **`Part 1A`:** `60`-digit `mpmath` + exact `SymPy` verification of repaired `2^{-1} mod N` Weil generators (`unit Heisenberg shear, exact (ST)^3 = S^2, Gauss-sum CRT identity \gamma_{15}(1) = \gamma_5(3)\gamma_3(2), W_5 = 3_c (+) 2_w, and 3a + 2b = 0`).
2. **`Part 1B`:** `60`-digit Zickert–Neumann flattened extended Rogers dilogarithm engine verified across amphichiral `m004`, equal-volume chiral sister `m003`, and `3`-tetrahedron chiral knot complement `m015` (`with explicit separation between geometric \Delta\theta_{\mathrm{CS}} = 0 and conditional bare \theta_{\mathrm{YM}} \in \{0, \pi\} exclusion`).

---

## 3. Pre-Registered Expectations and Falsification Criteria

1. **`E1_RepairedWeilMetaplectic_and_CRT_Gate` (`Part 1A`):** Unit-shear Heisenberg conjugation holds to `< (1/1000)^18`; non-projective $(S_N^{(r)} T_N^{(r)})^3 - (S_N^{(r)})^2$ Frobenius norm `< (1/1000)^18` across $N \in \{15, 5, 3\}$; $|\gamma_{15}(1) - \gamma_5(3)\gamma_3(2)| < (1/1000)^18$; `CRT` Weil tensor errors `< (1/1000)^18`; and $A_{\mathrm{U(1)}^3} = 4(3a + 2b)((3a + b)^2 + 4b^2)$ uniquely forces $k_2/k_1 = 3/5$.
2. **`E2_ZickertRogersCS_and_ThetaScoping_Gate` (`Part 1B`):** $|\operatorname{Vol}(\text{m004}) - \operatorname{Vol}(\text{m003})| < (1/1000)^18$; $|\operatorname{CS}(\text{m004}) \bmod (1/2)| < (1/1000)^18$; $|\operatorname{CS}(\text{m003}) - 1/4| < (1/1000)^18$; `m015` reproduces the published `SnapPy` `CS` benchmark to `< (1/1000)^2 * (1/100)` (`8` figures) with irrational residual `> 1/100` modulo `1/12`; and bare parity-$\pi$ branch remains explicitly flagged in Tier `II` (`producing \bar{\theta}_{\mathrm{phys}} = \pi > 3` rad when planted).

---

## 4. Mandatory Controls That Must Fail When Broken

1. **`Gate_AST_Stage1_Closure_Passed`:** `AST` check confirming zero disallowed imports and zero float literals inside all target-free algebra and `3`-manifold geometry functions (`benchmark float strictly isolated in check_m015_published_benchmark`).
2. **`PC_CL1_DoubledShearHeisenbergDefect`:** Un-halved quadratic phase $T_{\mathrm{old}}[x,x] = \exp(2\pi i r x^2 / N)$ yields $(S_0 T_0^{\mathrm{old}})^3 = \begin{psmallmatrix} 4 & 3 \\ -3 & -2 \end{psmallmatrix} \not\equiv S_0^2 \pmod 5$ (`non-scalar matrix defect > 1`).
3. **`PC_CL1_BlochWignerConjugateTautologyControl`:** Confirm that $D(z) + D(\bar{z}) = 0$ vanishes identically (`< (1/1000)^18`) even on chiral `m003` and chiral `m015`, proving it cannot discriminate amphichirality, whereas Zickert–Rogers `CS` detects both chiral manifolds (`|CS(m003)| = 1/4 > 1/5` and `|CS(m015)| > 1/10`).
4. **`PC_CL1_BareParityPiBranchUnselectedWithoutParentMap`:** Setting bare `4D` $\theta_{\mathrm{bare}} = \pi$ while $\Delta\theta_{\mathrm{CS}}(\text{m004}) = 0$ yields $|\bar{\theta}_{\mathrm{phys}}| = \pi > 3$ rad.

`0 of 19.`
