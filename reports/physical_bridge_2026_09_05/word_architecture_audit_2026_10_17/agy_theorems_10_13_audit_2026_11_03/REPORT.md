# AGY Theorems 10–13 source and hand-proof audit

November 3, 2026. Audited AGY commit `dcae538abd0a90cb3a024e793de10703fd971f8e`, on `agy/audit-2026-11-02`.

**Status — authored review-sharing checkpoint, UNREVIEWED.** This is a source audit and hand derivation. No AGY scientific function, test, import, collection, numerical integration or quadrature was executed by this lane. Received numerical outputs remain received evidence. The attached receipt pins the inspected source. No new result is banked and no foundational input is marked paid.

The question is whether these four functions repair the corresponding claims about global transport, strong CP, running masses and neutrino mixing. Their failure to complete those duties is restricted to their stated constructions. It supplies no programme-wide exclusion.

## Overall assessment

AGY explicitly accepts the earlier `395b27210` audit and records **0 of 19 first-principles SM parameters certified** in its response and scorecard. Preserve that correction. The new functions contain real methodological repairs and some exact algebra. Their advertised physical closure remains unsupported.

| Theorem | Preserved contribution | Remaining duty or error |
|---|---|---|
| 10 | Correct order-five anti-invariant character and two-element orbit. Its orbit admits an explicit rank-two unitary extension described below. | Rank-one extension remains obstructed. The reported mass-matrix phase identities do not establish the whole physical bundle, action or domain transport. |
| 11 | On a compatible conjugation patch, a conjugate doubled determinant is a squared modulus. The single-sheet phase is now exposed. | Added conjugate blocks and answer-dependent rephasings do not derive a strong-CP mechanism. A global scalar square-root branch also needs repair. |
| 12 | The factor-of-two running-rate error is fixed. Direct top/Higgs ratios can be posed without importing the measured tau mass. | Three quartic coefficients remain wrong and three mixed terms are absent. Matching, boundary selection and indirect empirical dependencies remain. |
| 13 | Symmetrization removes the scalar contribution exactly for identical left fields. The mixing construction is basis-covariant. | The charged-sector normalization is reused for a different total twist. Its present numerical spectrum cannot yet be certified for the stated LL operator. |

## 1. Theorem 10 and the actual transport question

Source locations below refer to `src/origin_axiom/toe_closure.py` at the pinned AGY commit. Theorem 10 occupies lines 884–1033.

Put

\[
A=\begin{pmatrix}2&-1\\-1&1\end{pmatrix},\quad
M=A^3=\begin{pmatrix}13&-8\\-8&5\end{pmatrix},\quad
w=\frac15\binom21.
\]

Direct hand multiplication gives

\[
\det(M-I)=-16,\quad \det(M+I)=20,\quad
(M+I)w=\binom4{-2}.
\]

Thus `Mw = -w` modulo the integer lattice. This preserves an unordered pair of characters, not either character separately. The matrix M has determinant 1 and trace 18. It is infinite order. Calling its finite-character orbit an amphichiral involution does not exhibit an orientation-reversing manifold involution or its physical lift.

### A sign correction that leaves the anti-invariant orbit intact

AGY's relay identifies

\[
B=(M-I)/4=\begin{pmatrix}3&-2\\-2&1\end{pmatrix}
\]

with the inverse modulo 5 of `U = [[1,2],[2,3]]`. In fact `UB = -I` exactly, so `B = -U^{-1}`. This is a genuine sign error in the relay. It does not remove the displayed orbit, which was independently checked above.

### An explicit positive extension after retaining both characters

Assume the mapping-torus automorphism has the stated pullback action `phi* chi_w = chi_w^{-1}` on this abelian character. On the fibre group set

\[
\rho(\gamma)=\operatorname{diag}\bigl(\chi_w(\gamma),\chi_w(\gamma)^{-1}\bigr),
\qquad
\rho(t)=J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

Both matrices are unitary and have determinant 1. Direct multiplication gives

\[
J\rho(\gamma)J^{-1}
=\operatorname{diag}(\chi_w^{-1},\chi_w)
=\rho(\phi\gamma).
\]

This satisfies the mapping-torus relation and constructs a rank-two unitary local system on that carrier. `J^2 = -I` causes no contradiction because the stable letter t has infinite order. A U(2) exchange matrix with square I is another lift with a different central choice. Neither choice has been selected physically here.

The rank-one obstruction therefore does not exclude an orbit-pair extension. The resulting rank-two representation factors through the abelian fibre characters and sends the fibre commutator to I. It alone does not reproduce the physical puncture's Q8 central holonomy, the full matter complex, its norms or its end condition. Those structures must be joined compatibly before interpreting multiplicities or generations. This construction is an authored hand-proof candidate, with no independent review or executed controls in this checkpoint.

For comparison, the same character is fixed by `A^6`, so it also extends as a rank-one character to the corresponding sixfold mapping torus. Choosing that carrier would incur its own geometry and field-content duties.

### Why scalar phases and H invariance are insufficient

A rank-one stable-letter phase cancels from `chi(t gamma t^{-1})`. It cannot change a non-invariant character into its inverse. Thus the longitudinal phase mentioned in the theorem does not itself repair the rank-one relation.

The source tests eight sampled moduli for the displayed Yukawa identities. Their reported numerical agreement is preserved as such. It does not prove all-moduli covariance of a complete operator and domain.

There is also a strong-CP qualification to the claimed T8 physical gauge equivalence. Using AGY's stated phases, the quark determinant product transforms by

\[
3(\phi_u+\phi_d)
=3(2\pi/25-4\pi/5)
\equiv-4\pi/25\pmod{2\pi}.
\]

Under its inversion phase the corresponding shift is `-2pi/5` modulo `2pi`. Hermitian mass squares and the ten flavour invariants can remain unchanged while this phase changes. A full physical equivalence requires the anomalous/bare-theta matching as well. The effective strong angle is defined after quark-mass diagonalization. [PDG axion review, section 89.2.1](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-axions.pdf)

## 2. Theorem 11 and strong CP

Theorem 11 is at lines 1036–1146. Its fixed-matrix conjugation identity, when valid on a specified patch, implies

\[
\det\operatorname{diag}(Y,P\overline YP)=|\det Y|^2
\]

because `det(P)^2 = 1`. This is correct conditional algebra. A physical use must derive the added conjugate sector, its spectrum and its thresholds and must account for the bare strong angle. A real doubled determinant alone supplies none of those identifications.

Lines 1094–1099 choose two independent phases from the answers already computed,

\[
\theta_u=-\arg\det Y_u/3,\qquad
\theta_d=-\arg\det Y_d/3.
\]

The determinant cancellation is then an algebraic identity. No action, potential, stationary equation or physical coupling selecting those phases is computed there. If these are field redefinitions, the anomalous theta shift must accompany them. If they are physical Wilson moduli, their dynamics and allowed independent couplings must be derived. A dynamical cancellation requires that extra structure. [PDG axion review, section 89.2.1](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-axions.pdf)

The statement `H^1(M_3,U(1)) = Z` is also incorrectly typed. For this once-punctured-torus mapping torus, abelianization gives

\[
H_1(M_3,\mathbb Z)=\mathbb Z\oplus\operatorname{coker}(M-I)
=\mathbb Z\oplus\mathbb Z_4\oplus\mathbb Z_4.
\]

The Smith invariants are 4 and 4, from the entry gcd and determinant. Hence its flat U(1) character group is `U(1) x Z4 x Z4`. An integer winding group and the group of flat phases must be distinguished. The existence of a continuous phase still does not select its vacuum value.

### The global square-root issue

The helper `_f10_st_and_scalar`, `sm_19_gate.py` lines 350–362, uses the conjugate of a principal square root of

\[
F=\theta_4^{20}+\theta_2^{20}-\theta_3^{20}.
\]

There is a useful exact factorization. Set `X = theta2^4`, `Y = theta4^4`. The theta identity gives `theta3^4 = X+Y`, so

\[
F=X^5+Y^5-(X+Y)^5
=-5XY(X+Y)(X^2+XY+Y^2)
=-80\eta^{12}E_4.
\]

The theta/Eisenstein identities and valence formula used here are standard. E4 has a simple zero at the order-three elliptic point and eta has no zero in the upper half-plane. Consequently F has a simple zero there. A global holomorphic square root on that half-plane is impossible. A scalar lift on a branched double cover or compatible transition data is required. This is a duty for the scalar construction, not an exclusion of that larger construction. [Schultz, sections 3.2–3.4](https://people.maths.ox.ac.uk/beem/papers/modular_forms_notes.pdf)

The all-upper-half-plane fixed-P claim also encounters its principal-root cut. In the exact theta limit at `tau = iy`, theta constants are positive real and F is negative real. With the conventional principal value `sqrt(F)=+i sqrt(-F)`, `b_st=-i sqrt(-F)`, so `b_st(-bar(tau))=-conj(b_st(tau))` on this fixed locus. The scalar sign is different from the one used by the displayed fixed-P formula away from the cut.

An explicit hand check uses the up pair `(1,-4)` at `(alpha,b)=(2/5,0)`. Their characteristics differ by the integer 2, so the two spinor columns agree. Thus `m1=0`. At `tau=iy`, the residue vector and h satisfy `m=P bar(m)` and `h=P bar(h)`, while m is nonzero. Here `c_u=-i sqrt(2)` and `a0=c_u b_st` is nonzero real. Writing

\[
Y=S+a_0T,\quad S=hm^T+mh^T-(h\cdot m)I,\quad T=-[m]_\times,
\]

gives `P bar(Y) P = S-a0 T`, whereas the reflected data are the same data. The proposed fixed-P equality therefore fails on this cut in the exact principal-value convention. This is a hand-derived limiting countercheck, not a fresh floating-point run. Signed rounding at the cut can choose either side and cannot replace a specified transition law. AGY's sampled conjugation tests keep positive real part between 0.15 and 0.55 and do not exercise this locus or continuation around the simple zero.

## 3. Theorem 12 and its beta functions

Theorem 12 occupies lines 1149–1363. Its time convention is now consistent,

\[
t=\log(\mu/\mu_0)/(2\pi),\qquad
f_1=1/(4\pi),\quad f_2=1/(64\pi^3).
\]

Credit the rate correction. Its gauge and top-Yukawa polynomials agree with the cited equations in the declared approximation `yb = ytau = 0`. Calling that approximation the complete SM evolution needs qualification.

The quartic polynomial still disagrees with the cited equation. In the table, g1 and g2 denote the ordinary GUT-normalized couplings. The code's variables of the same names are their squares.

| Monomial in the two-loop polynomial | AGY coefficient after its 0.6 conversions | Published coefficient |
|---|---|---|
| `lambda g1^4` | `629/400` | `1887/400` |
| `g2^2 g1^4` | `-559/800` | `-1677/800` |
| `g1^6` | `-1137/4000` | `-3411/4000` |
| `yt^2 g2^4` | absent | `-9/8` |
| `yt^2 g1^4` | absent | `-171/200` |
| `yt^2 g2^2 g1^2` | absent | `63/20` |

These are direct source comparisons at lines 1213–1230. The same defects occur in the earlier repair function at lines 731–748. The relevant reference is Appendix B, equation 99, in version 4. [Buttazzo et al.](https://arxiv.org/html/1307.3536v4)

The claimed Table 1 published benchmark is not established by the given citation. Table 1 in the inspected version summarizes calculation orders. Its inputs and matching formulas occur elsewhere. The code's threshold agreement with 9.68 can coexist with the coefficient errors above. A correct benchmark must name its exact input scale, matching, approximation and reference trajectory. The code's tolerance of 0.02 in log scale is also looser than a three-significant-figure check.

### What input reduction is real and what remains supplied

The direct `MZ/v`, `yt` and Higgs boundary-value path does remove a direct numerical tau-mass anchor. Its measured MZ is used for comparison in that ratio path. Preserve this conditional improvement. The gauge boundary formulas remain supplied hypotheses, as AGY's accepted-audit response already acknowledges. The new UV conditions `yt^2(M12)=1/5` and `lambda(M12)=0` are also hypotheses awaiting a derivation. A post-inspection algebraic value does not earn a zero-choice declaration.

The bottom and tau ratios still inherit `theorem8` dependencies. `sm_19_gate.py` lines 740–759 contain empirical `alpha_EM^-1=127.951`, `sin^2(thetaW)=0.23122`, an assigned `I_top=0.1462`, and `exp(-0.0170)`. Their dependence does not disappear because Theorem 12's returned `imported_MZ_count` and `imported_mtau_count` are literal zeros. `eta_abs` there is reconstructed from the F10 scalar, so the earlier F10/DR distinction must remain explicit.

### Mass matching and verification

The displayed Higgs value is obtained from `sqrt(2 lambda(MZ)) v` without the cited loop-level pole matching. The top conversion uses an MZ-scale running mass with the scale-specialized one-loop factor and omits the necessary scale treatment. Pole-level precision claims require consistent thresholds and running. [Buttazzo et al., section 2 and Appendix A](https://arxiv.org/html/1307.3536v4)

The boundary solver uses 2000 steps for the baseline and 1000 for finite-difference perturbations divided by `1e-6`. This mixes discretization error into its Jacobian. It also takes a fixed twelve Newton updates without an explicit convergence failure condition. Reported final residuals remain useful, but round-trip agreement checks inversion of the implemented flow, including any erroneous coefficients. It cannot establish that the implemented flow is the SM flow.

The AGY referee's purported independent Theorem 12 and 13 outputs at lines 1086–1121 are taken from the producer scorecard. The Theorem 11 route through B1656 is a genuinely distinct numerical construction at its sampled point. Preserve that distinction.

## 4. Theorem 13 and the LL norm

Theorem 13 occupies lines 1366–1463. Equal spinor arguments make the Pauli-singlet bilinear vanish by antisymmetry, so `m1=0`. Taking the symmetric part of the quaternionic Yukawa formula then gives

\[
M_W=hm^T+mh^T-(h\cdot m)I
\]

for every complex scalar a0. Its skew contribution cancels exactly. This is a genuine conditional removal of a0 from this particular flavour tensor.

The revised mixing calculation has a correct covariance argument. Under

\[
Y_e\mapsto L Y_eR^\dagger,\qquad
M_W\mapsto L M_WL^T,
\]

both `Ye Ye†` and `MW MW†` conjugate by L. With distinct singular values, their ordered left eigenspaces transform together. PMNS moduli and the Dirac Jarlskog invariant are unchanged. Majorana phases would need additional Takagi phase information. This repairs the old charged-lepton-only left/right-overlap diagnostic.

### The normalization is outside the charged-sector theorem's scope

Line 1390 computes `closed_form_cA(tau, "2/5", "0")` once and lines 1398–1400 reuse it for `(-3,-3)` residues. That function explicitly hardwires the total charged-sector twist magnitude 3. Its sector-independence theorem covers `(1,-4)`, `(1,2)` and `(-3,6)`, whose total charges are -3, 3 and 3. The LL total is -6.

For `alpha=2/5`, the charged-sector fractional strip parameters are `1/5` for channels 1/i and `7/10` for j/k. Using total charge -6 instead gives `3/5` and `1/10`, respectively. Even identifying `nu` with `1-nu` leaves different pairs. The generic cusp norm contains `psi(nu)+psi(1-nu)`, which is strictly increasing on `(0,1/2)`, so these generic norms cannot be identical.

The positive repair is to reuse the addition/kernel derivation with actual total twist `ubar=-6w`, and then compare with the existing B1656 `cA(x,y,t,R)` on those same LL arguments. A doubled torsion address is a candidate implementation of that change, subject to the inversion and spin conventions. No fresh quadrature or corrected PMNS number is claimed here.

Basis scrambling cannot detect this mistake. Any assigned symmetric matrix has the stated covariance, including one constructed with an incorrect diagonal normalization. The algebraic symmetrization and covariance remain valid independently of the numerical normalization issue.

AGY transparently reports a very small atmospheric angle for its present assigned tensor. Keep that as a received output of that prescription. Recompute after correcting or independently deriving its LL norm before banking a physical neutrino exclusion. Adding an MR rotation is another model ingredient until it is derived from the admitted action. The gauge-invariant LLHH operator, its physical normalization and its parent identification also need explicit treatment before this flavour tensor is called a physical Weinberg prediction.

The Theorem 13 docstring still quotes the earlier incorrect modular scales. The executable return and relay distinguish F10 and DR with approximately 0.021434 and 0.004092. Update the docstring while preserving their distinction.

## 5. Cross-check against the newly fetched independent seat

During the final fetch, `audit/independent-2026-11-03` appeared at `2dbfe96dc`. Its Theorems 10–13 report and 208-line check were read. Its reported reruns are outside this lane's execution and are not adopted as new numerical certificates here.

Several findings agree, including the conditional conjugate determinant, the answer-dependent rephasing, the revised mixing covariance, empirical inter-sector dependencies and missing mass matching. Its explicit beta polynomial at lines 117–122 includes the corrected coefficients and mixed terms listed above. Its claim that nearby integrations confirm AGY's RGE is therefore too strong. The vector fields visibly differ. Numerical agreement of selected endpoints does not erase that source difference.

Its approximate matching exercise reports substantially different pole masses. This is useful corroboration of the matching duty. Those exact values and sigma labels were not independently rerun here and require their own scale, theory-error and fit-domain accounting before certification. Its unqualified confirmation of the all-moduli conjugation identity does not address the square-root cut, and its proposed PMNS negative still needs the LL normalization audit above.

The reported T8 orbit equivalence of all five addresses is also compatible with the relabelling rule `p2 -> p2-k p1`. Such equivalence must carry the modulus, field lifts, phases, reference data and selected-state rule together. It cannot alone select one address or prove equivalence of fully interacting vacua.

Reading this seat's broader report exposed additional quoted B1825 values. The raw B1825 run artifact remains unopened in this audit, but no blindness to the reported values is claimed.

## 6. Next bounded repair work

1. Implement and verify the entire order-five orbit transport on the physical registered bundle, retaining its puncture holonomy, all fields, interactions, norms and end domain. Use the explicit rank-two construction as an abelian subproblem.
2. Specify the F10 square-root cover and all conjugation/translation transition laws. Include the imaginary-axis cut and continuation around an E4 zero in a separately sealed test design.
3. Replace both quartic polynomial copies from the cited equation and certify their coefficients independently. Then use consistent threshold matching and a source-complete, convergent boundary solver. Retain the UV and gauge hypotheses in the input ledger.
4. Derive the actual LL channel norms and then recompute the symmetric-tensor spectrum. Preserve the a0 cancellation and mixing covariance. Derive any additional Majorana structure from the same physical action before granting input-reduction credit.

These tasks are compatible with the lane's reductions-first mission and its full register/field/end-law work. No full SM, three-generation, strong-CP or gravity derivation is certified by this checkpoint.
