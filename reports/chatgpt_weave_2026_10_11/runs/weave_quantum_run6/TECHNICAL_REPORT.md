# Quantum realization of the weave — Run 6
## A cochain-level map to a line-valued protected current sector

**Date:** 10 October 2026.  
**Inputs:** *A Weave of Two Records*, especially §§2–4 and §7; the supplied Run 5 report and earlier reports for fixed definitions.  
**Scope:** Independent exact reconstruction of the cohomology representation, a complete local protected-subalgebra calculation in the already specified two-dimensional spin-CFT family, and an ordinary protected-module control. No Standard Model input, repository edits, four-dimensional matter claim, or gravitational completion.

## Executive result

The scalar factor previously recognized as the multiplier of eta cubed can be derived directly from the original **group cohomology**. No eta function is needed to obtain it.

The untwisted cohomology has dimension two and splits under the chosen lifts into conjugate one-dimensional representations. Call the one with generator values

\[
\ell(L)=\zeta_8,\qquad \ell(R)=\zeta_8^{-1},
\qquad \zeta_8=e^{\pi i/4}
\]

by the name \(\ell\). The nontrivial-parity direct sum then admits the exact factorization

\[
\bigoplus_{p\ne0}H^1(F_2;\chi_p\rho_Q)
\cong (\ell\otimes O)\oplus(\bar\ell\otimes O),
\]

where \(O\) is the three-dimensional quaternion-normalizer rotation representation. The first summand is exactly equivalent, by a printed monomial intertwiner, to the manuscript's specified multiplier. This independently reconstructs the representation from crossed homomorphisms and coboundaries. It does **not** independently recompute the Hodge–Riemann form selecting which conjugate is called holomorphic.

The interacting family retains a protected current triplet \(J\) carrying \(O\). Consequently there is an explicit equivariant map

\[
\boxed{T\ \cong\ \ell\otimes\operatorname{span}\{J_1,J_2,J_3\}.}
\]

This is a **geometric line-valued operator map**, not the identification of \(T\) with three ordinary local quantum currents. The line is supplied by the mathematics, but a quantum realization of its transport, metric, amplitude normalization, and sewing has not been constructed.

The distinction is substantive. The complete local holomorphic algebra that remains holomorphic across an open interval of the deformation is

\[
\boxed{\mathcal A_{\mathrm{prot}}
=V_{\sqrt2\mathbb Z}\otimes\mathcal H_0
\cong \mathfrak{su}(2)_1\otimes\mathcal H_0,}
\]

where \(\mathcal H_0\) is the zero-charge Heisenberg vacuum algebra. Its internal normalizer action factors through ordinary rotations at **every conformal weight**. The manuscript's genuine metaplectic center cannot act on it in the same way as it acts on \(T\). A scalar twist of the three local currents also fails their nonzero vacuum and Lie-bracket operator-product coefficients.

The ordinary \(\mathfrak{su}(2)_1\) spinor-module alternative is protected, but its affine fusion is the semion rule \(s\times s=1\). Its complete genus-one primary-puncture block spaces have dimension zero or two, not three. This is a restriction on ordinary affine blocks, **not** on unknown nonabelian quaternion-crossed spin defects.

**Outcome:** the original cohomology-to-current map is now explicit as a line-valued map; an ordinary local-current interpretation fails; the missing quantum object is the physical realization of the geometric coefficient line together with the genuinely quaternion-twisted puncture data. The protected sector itself does not fix the deformation parameter.

---

## 1. Source boundaries

The source manuscript specifies

\[
V=\bigoplus_{p\ne0}H^1(F_2;\chi_p\otimes\rho_Q)=T\oplus\bar T,
\qquad \rho_Q(a)=i,\quad\rho_Q(b)=j,
\]

and identifies the multiplier of \(T\) with that of

\[
\Phi(\tau)=\eta(\tau)^{21}
(\theta_2(\tau)^2,\theta_3(\tau)^2,\theta_4(\tau)^2)^T.
\]

The PDF treats the identification with physical generations and holomorphic modes with physical left-handed matter as part of its stated link \(\Lambda\), and separately postulates cusp data. Those assumptions are not removed here.

The pinned B1634 record was read to verify the lift convention: the move-product maps compose contravariantly, and the source's representation is obtained by taking their inverses. No project verification code was imported or executed. The code below starts with two explicit 2-by-2 quaternion matrices and derives all cohomology matrices anew.

Run 5 supplies the interacting spin-CFT family and its original glued charge lattice. It established that the full free holomorphic fermion prescription persists only at the free point, while the quaternion current algebra survives. We retain that family without changing its field content, spin-charge gluing, or deformation coordinate.

This run does not assert that the cohomology is a space of quantum states merely because its dimension matches a space of currents.

## 2. Direct calculation of group cohomology

### 2.1 Cocycles and the quotient

Use

\[
A=\begin{pmatrix}i&0\\0&-i\end{pmatrix},\qquad
B=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad C=AB.
\]

For a sign pair \(p=(a_p,b_p)\), the local system has matrices
\(A_p=a_pA\), \(B_p=b_pB\).

A crossed homomorphism is determined by two arbitrary vectors

\[
u=f(a),\qquad v=f(b),\qquad
f(gh)=f(g)+\rho_p(g)f(h).
\]

There are no relations in \(F_2\), so the cocycle space is \(\mathbb C^4\). Coboundaries are

\[
\delta w=((A_p-I)w,(B_p-I)w).
\]

Because \(A_p-I\) is invertible for all four sign pairs, every class has a unique representative with \(u=0\). Its quotient coordinate is

\[
c=v-(B_p-I)(A_p-I)^{-1}u.
\]

Thus all four cohomology spaces have dimension two. The implementation also uses the opposite gauge, setting \(v=0\), and verifies the explicit coordinate changes for both moves and all four characters.

### 2.2 Chosen normalizer lifts and cochain maps

The grammar maps are

\[
L:(a,b)\mapsto(a,ab),\qquad
R:(a,b)\mapsto(ab,b).
\]

Use their determinant-one quaternion normalizer lifts

\[
n_L=\frac{I+A}{\sqrt2},\qquad
n_R=\frac{I-B}{\sqrt2}.
\]

They obey

\[
n_L A n_L^{-1}=A,\quad n_L B n_L^{-1}=AB,
\]

\[
n_R A n_R^{-1}=AB,\quad n_R B n_R^{-1}=B.
\]

Pulling back a cocycle and using \(n^{-1}\) to return the coefficient representation to the chosen frame gives

\[
L^*(u,v)=\bigl(n_L^{-1}u,\ n_L^{-1}(u+A_pv)\bigr),
\]

\[
R^*(u,v)=\bigl(n_R^{-1}(u+A_pv),\ n_R^{-1}v\bigr).
\]

The output parity labels are respectively

\[
p_L=(a_p,a_pb_p),\qquad p_R=(a_pb_p,b_p).
\]

The code verifies directly that these maps send coboundaries to the appropriate coboundaries. It also verifies the induced quotient maps without relying on the gauge choice.

### 2.3 The scalar line is already in the untwisted cohomology

For the trivial sign pair \((+,+)\), the quotient pullbacks are

\[
M_L=\begin{pmatrix}\zeta_8&0\\0&\zeta_8^{-1}\end{pmatrix},
\qquad
M_R=\begin{pmatrix}\zeta_8^{-1}&0\\0&\zeta_8\end{pmatrix}.
\]

Taking inverse move matrices in the source's representation convention, the second coordinate line carries

\[
\ell(L)=\zeta_8,\qquad \ell(R)=\zeta_8^{-1}.
\]

The first coordinate line carries its complex conjugate.

This is a derivation from the cocycle equations. The scalar character is not guessed from eta functions or appended to a quantum theory. The untwisted cohomology is used as a common reference for the three isomorphic twists; it is not declared to be a new physical field.

## 3. Exact reconstruction of the triplet

The intertwining matrices for the three nontrivial sign characters are

\[
Q_{(+,-)}=A,\qquad Q_{(-,-)}=C,\qquad Q_{(-,+)}=B,
\]

since \(Q_p\rho_QQ_p^{-1}=\chi_p\rho_Q\).

Write every cohomology class in the common untwisted coordinates using \(Q_p^{-1}\). In the ordered parity basis

\[
((+,-),(-,-),(-,+)),
\]

the selected three-dimensional summand has matrices

\[
T_L=\zeta_8 O_L,\qquad T_R=\zeta_8^{-1}O_R,
\]

where

\[
O_L=\begin{pmatrix}1&0&0\\0&0&1\\0&-1&0\end{pmatrix},
\qquad
O_R=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&1\end{pmatrix}.
\]

These are the adjoint actions of \(n_L,n_R\) on \((A,C,B)\). They are related to previous runs' axis choices by fixed signed permutations; the coordinate change is not a new physical choice.

The other three-dimensional summand has the complex-conjugate matrices. All raw six-dimensional matrices and all frame changes are printed in `results/exact_results.json`.

Let

\[
T_S=T_RT_L^{-1}T_R,\qquad
D=\operatorname{diag}(-i,1,i),
\]

and

\[
P=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix},\qquad
M=\begin{pmatrix}i&0&0\\0&0&1\\0&1&0\end{pmatrix}.
\]

The exact intertwiner is

\[
\boxed{DT_LD^{-1}=\zeta_8^{-1}M,\qquad
DT_SD^{-1}=\zeta_8 P.}
\]

These are the manuscript's two target coefficient matrices. They obey

\[
T_S^2=(T_ST_L)^3,\qquad T_S^8=I,\qquad T_S^4=-I.
\]

The complete image has order 96; the rotation image has order 24; the scalar center is \(\{1,i,-1,-i\}\). Both summands are irreducible by an exact finite-character calculation.

Consequently

\[
\boxed{T\cong\ell\otimes O.}
\]

Since \(S=RL^{-1}R\), the line satisfies

\[
\ell(S)=\zeta_8^{-3},\qquad \ell(S)^4=-1,\qquad\ell^8=1.
\]

These are precisely the **coefficient** multipliers of eta cubed. This does not assign modular weight 3/2 to an ordinary local field and does not make \(\eta^3\) a flat section of a weight-zero local system. Indeed

\[
\frac{1}{2\pi i}\partial_\tau\log\eta^3=\frac18E_2(\tau),
\]

which is nonzero. Full automorphy weights, connections and amplitudes remain distinct data, as in Run 4.

### What has been independently reconstructed

The two conjugate invariant triples and their exact lifts have been reconstructed from the group-cohomology quotient. The chosen triple is identified by its exact agreement with the source's stated target, rather than by an independent recomputation of the source's Hodge–Riemann positivity. No such positivity calculation is silently claimed.

Because the full generator intertwining and defining relations hold, the representation comparison holds for every word in the allowed generators. It is not a finite census on selected threads.

## 4. The complete protected local algebra in the interacting family

Retain Run 5's integer local NS charge lattice

\[
(q_{L1},q_{L2};q_{R1},q_{R2})\in\mathbb Z^4.
\]

Write

\[
a_L=(q_{L1}-q_{L2})/\sqrt2,\quad b_L=(q_{L1}+q_{L2})/\sqrt2,
\]

and similarly on the right. The deformation changes the B charges by the real boost

\[
(b_L,b_R)\mapsto(\cosh t\,b_L+\sinh t\,b_R,
\sinh t\,b_L+\cosh t\,b_R).
\]

For a state with nonnegative right oscillator level \(N_R\),

\[
\bar h(t)=\frac12\left[a_R^2+(\sinh t\,b_L+\cosh t\,b_R)^2\right]+N_R.
\]

Suppose a continuously tracked local field is holomorphic throughout an open interval of real \(t\). Nonnegativity and analyticity force

\[
a_R=0,\quad b_L=b_R=0,\quad N_R=0.
\]

The charge lattice then gives exactly

\[
\boxed{(q_L;q_R)=(n,-n;0,0),\qquad n\in\mathbb Z.}
\]

Left oscillators of both bosons remain available. Thus the complete common local chiral algebra is

\[
\mathcal A_{\rm prot}=V_{\sqrt2\mathbb Z}\otimes\mathcal H_0
\cong\mathfrak{su}(2)_1\otimes\mathcal H_0.
\]

This is the intersection over an open deformation interval. It is not a classification of extra chiral fields at isolated enhanced points. The lattice labels are tracked continuously; switching to a newly selected orbifold or new charge lattice would change the question.

The \(\mathfrak{su}(2)_1\) identification is the standard self-dual-boson current algebra. The Heisenberg factor here is its **zero-charge vacuum algebra**, not a claim that the full compact charge sector has only one state or one representation. Bulk theories still differ through their charged spectra.

### Complete graded count

Its vacuum character is

\[
\boxed{\operatorname{ch}\mathcal A_{\rm prot}(\tau)
=\frac{\theta_3(2\tau)}{\eta(\tau)^2}
=q^{-1/12}(1+4q+9q^2+20q^3+42q^4+80q^5+147q^6+\cdots).}
\]

This is a chiral vacuum-module character, not a complete modular-invariant torus partition function. In particular the Heisenberg vacuum alone is not a rational modular completion.

Let \(p_2(N)\) be the coefficient of \(q^N\) in \(\prod_{m\ge1}(1-q^m)^{-2}\), and set it to zero for negative N. At grade h the multiplicity of ordinary integer spin j is

\[
 m_j(h)=p_2(h-j^2)-p_2(h-(j+1)^2).
\]

This follows by subtracting adjacent Cartan-weight multiplicities. It is independently checked against the direct lattice-oscillator dimension. The first grades are

| h | total dimension | integer-spin multiplicities, starting at j=0 |
|---|---:|---|
| 0 | 1 | 1 |
| 1 | 4 | 1, 1 |
| 2 | 9 | 3, 2 |
| 3 | 20 | 5, 5 |
| 4 | 42 | 10, 9, 1 |
| 5 | 80 | 16, 18, 2 |
| 6 | 147 | 29, 31, 5 |

Every representation is an integer-spin representation of the flavour rotation group; B oscillators are singlets. Hence the internal normalizer action on the entire common protected local algebra factors through ordinary rotations. This is an all-weight conclusion; exact coefficients through grade 18 provide checks rather than the proof.

## 5. Why the full target is not an ordinary protected current multiplet

The actual current triplet has OPE

\[
J_a(z)J_b(w)\sim\frac{\delta_{ab}}{2(z-w)^2}
+\frac{i\epsilon_{abc}J_c(w)}{z-w},
\]

up to a fixed orientation convention on its axes. Its local normalizer matrices are \(O_L,O_R\).

The central word satisfies

\[
O_S^4=+I,
\qquad T_S^4=-I.
\]

Therefore an intertwiner from \(T\) into any common protected local weight space, with **this internal normalizer implementation of the generators**, must vanish:

\[
\boxed{\operatorname{Hom}_{G}(T,\mathcal A_{\rm prot}[h])=0
\quad\hbox{for every }h.}
\]

The exact finite-group character computation verifies this through grade 18, using all 96 group elements.

This comparison must not conflate an internal transformation of local operators with transport of conformal blocks over moduli space. Quantum conformal-block transport may carry determinant or framing phases even when local operators do not. The theorem excludes the direct local-operator identification for the specified action; it does not exclude every quantum realization of \(T\).

### A scalar current twist is not an OPE-preserving repair

Multiplying every current by the geometric phase does not preserve its algebra. For example, a central element of the target acts by \(iI\). It changes the double-pole coefficient by \(i^2=-1\), while the vacuum identity must remain fixed. The simple-pole coefficient is incompatible as well.

More generally a scalar \(\alpha\) multiplying a genuine rotation changes the vacuum term by \(\alpha^2\) and the current term by \(\alpha^2\), whereas transforming the current on the right-hand side gives \(\alpha\). With a nonzero level and nonzero bracket, both requirements force \(\alpha=1\).

Exact representation checks also give

\[
\operatorname{Hom}_G(\mathbf1,T\otimes T)=0,
\qquad \operatorname{Hom}_G(T,T\otimes T)=0,
\]

while

\[
\dim\operatorname{Hom}_G(\mathbf1,T\otimes\bar T)=1.
\]

This is not a prohibition on complex matter multiplets with conjugate partners. Such fields need not close under the current OPE above. It is a restriction on reading \(T\) as these three self-contained local currents.

## 6. The exact line-valued map — and its physical limit

Let \(e\) be a local frame of the geometric line \(\ell\). In the common parity frame the map is

\[
\boxed{(x_1,x_2,x_3)\longmapsto
e\otimes(x_1J_1+x_2J_2+x_3J_3).}
\]

In the manuscript's theta frame, first apply \(D^{-1}\). This gives an explicit \(T\to\ell\otimes J\) intertwiner for both generators and every word they generate.

Among the eight tensor powers \(\ell^r\otimes J\), exact character calculations give

\[
\dim\operatorname{Hom}_G(T,\ell^r\otimes J)
=\begin{cases}1,&r=1\pmod8,\\0,&\text{otherwise}.\end{cases}
\]

So the needed line is specified, not an arbitrary scalar choice once this map and action are fixed.

At the level of associated flat local systems on the metaplectic modular orbifold, the tensor-product connection provides a flat geometric map: the line has the stated finite unitary holonomies and the rotation factor has its finite transport. This construction is mathematical. It does **not** compute the physical Berry, determinant, Quillen or conformal-block connection of the interacting theory and does not assert equality to that connection.

Turning \(e\) into a physical field, puncture amplitude, or defect state is an additional operation. Its operator products and sewing would have to be specified. For instance, two factors of \(e\otimes J\) live naturally in \(\ell^2\) before a contraction is supplied; it is not legitimate simply to identify that coefficient line with either the vacuum line or \(\ell\). The source does not currently supply a quantum rule doing so.

### Neutral operators lose the line exactly

For any unitary geometric line,

\[
\operatorname{End}(\ell\otimes J)\cong\operatorname{End}(J).
\]

Explicitly,

\[
(\ell(g)O_g)X(\ell(g)O_g)^{-1}=O_gXO_g^{-1}.
\]

This was checked on the complete finite group and numerically on generic matrices. Neutral endomorphism/projector comparisons cannot by themselves determine the extra scalar character. A phase-sensitive amplitude or appropriate transport observable is needed.

The protected current algebra and this external geometric tensor construction exist throughout the marginal family. Matching them does not select the parameter t or any source modulus tau. In this limited sense, protection preserves structure while making it insensitive to the very coupling one hoped to determine.

## 7. The ordinary protected spinor alternative

Run 5 found the chiral flavour spinor components

\[
S_\pm=e^{\pm iH_A/\sqrt2},\qquad h=\tfrac14,
\]

which remain unchanged by the B-current deformation. These are not local NS fields of the original glued integer lattice: their original charges are \((\pm\tfrac12,\mp\tfrac12;0,0)\). They belong to a module/disorder-sector comparison and must not replace the original puncture without explanation.

Their OPEs show

\[
S_+(z)S_+(0)\sim z^{1/2}J_+(0),
\]

\[
S_+(z)S_-(0)\sim z^{-1/2}\bigl[1+zJ_3(0)+\cdots\bigr].
\]

The precise phase conventions of intertwiners do not change the fusion channel statement. The current states are descendants of the affine vacuum module. At level one there is no additional integrable spin-one primary sector.

The protected \(\mathfrak{su}(2)_1\) theory has two simple affine modules, \(1\) and \(s\), with

\[
s\times s=1,\qquad d_s=1,\qquad\vartheta_s=i,
\]

and

\[
S_{\rm aff}=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]

These are the standard semion data, not a new category. A complete pointed presentation uses

\[
\omega(a,b,c)=(-1)^{abc},\qquad R(a,b)=i^{ab},\quad a,b,c\in\mathbb F_2.
\]

All 16 pentagon and all 16 hexagon equations were verified. Replacing the associator by 1 while keeping the braiding fails a negative control. Verlinde multiplication independently gives the same fusion rule.

### Ordinary puncture-block dimensions

For a genus-g surface with N semion-labelled primary punctures and any number of vacuum labels, the ordinary Verlinde formula gives

\[
\begin{aligned}
\dim\mathcal V_{g,N}
&=\sum_{x=1,s}S_{0x}^{\,2-2g}
\left(\frac{S_{sx}}{S_{0x}}\right)^N\\
&=2^{g-1}(1+(-1)^N).
\end{aligned}
\]

Hence the complete ordinary block space has dimension

\[
\boxed{2^g\text{ for even }N,\qquad0\text{ for odd }N.}
\]

At genus one this is two or zero, never three. In particular a single ordinary spinor insertion has no torus one-point block. Local descendant insertions do not add a new integrable fusion channel.

**Boundary:** This calculates ordinary integrable affine-primary punctures of the protected flavour sector. It does not calculate noncommuting Q8 symmetry twists, their central flux, fermionic junction data, sums over additional defect labels, or the physical spin-charge gluing of an asserted standalone semion theory. The Heisenberg vacuum factor likewise does not constitute a complete rational theory whose every defect has been classified. The calculation rules out that simple ordinary-block identification, not all protected defect routes.

## 8. What the map does and does not achieve for physics

The original geometric triplet is now reconstructed exactly, not inferred from a similarity to theta functions. Its extra scalar phase has a precise cohomological origin. The protected quantum operator factor is also explicit.

But they inhabit different kinds of object:

- \(T\): the supplied geometric lifted cohomology representation;
- \(J\): genuine protected local currents with a unital operator algebra;
- \(\ell\otimes J\): currents with values in a geometric coefficient line;
- quantum puncture/conformal blocks: amplitudes with physical sewing and transport data, not yet identified with that line-valued object.

This separation prevents two opposite mistakes: declaring failure merely because local currents do not have a global block phase, and declaring success merely because a geometric line can be tensored onto them.

The exact conditions for promoting the result are now more specific. A faithful construction must produce the geometric line's transport from its actual quaternion puncture/defect states and must provide compatible gluing maps and quantum connections. It must keep the original equal-half-pole prescription or explicitly state and justify a changed physical dictionary. Ordinary semion blocks alone do not accomplish this.

Even a successful protected-sector identification would not automatically select bulk couplings. The current-current family is an explicit example in which the protected local algebra remains unchanged while charged dimensions vary. Couplings between protected and unprotected sectors, or another independent physical selection principle, would still need to be addressed.

No gauge-chiral Standard Model spectrum, physical source modulus, gravitational dynamics or observed constant has been obtained.

## 9. Verification and reproducibility

Run:

```text
python verify_exact.py
python verify_numerical.py --dps 60
python verify_numerical.py --dps 90
```

The exact script has **140 named checks**. Many are deliberately repetitive: 38 graded checks and 45 sampled genus/puncture-rank checks corroborate all-weight and all-genus formulas already proved analytically. This count is an inventory, not a confidence score or 140 independent discoveries.

The exact work includes:

- all four cochain quotients and both move maps;
- invariance under changing from the a-zero to b-zero quotient gauge;
- the six-dimensional reconstruction and printed exact intertwiner;
- all 96 finite group elements and all eight geometric line powers;
- current OPE covariance and the nontrivial-center negative test;
- independent oscillator counts and the protected graded algebra through grade 18;
- the ordinary semion associator, braiding and Verlinde control.

The numerical script contains **80 checks at each precision**, all direct formula comparisons. It uses direct theta sums in tau (not principal fractional powers of the nome), eta products, an independently constructed 150-term character expansion, both modular generators, eta logarithmic differentiation, neutral endomorphism transport, and protected weights at nonzero deformations.

At 60 digits the largest normalized residual was approximately **7.00e-61**. At 90 digits it was approximately **1.69e-90**. These are numerical corroborations with finite truncations and conservative working cutoffs, not certified interval/tail bounds. The mathematical identities and obstruction claims have the analytic arguments above.

The alternate quotient gauge is a coordinate-robustness test of the cochain construction, not an independent research team. The numerical theta comparison provides a separate functional check of the cochain-derived matrices. No earlier run's verification functions were imported.

The working plan was written after source reading and exploratory cohomology calculations, then hashed before the formal scripts. It is not blind or externally timestamped. Exploratory SymPy characteristic-polynomial/solver diagnostics are disclosed in `CHANGELOG.md`; no final claim depends on those solver calls. Formal exact and numerical runs completed successfully. No source PDF, earlier report, or user repository was modified.

## 10. Claim grades and next step

| Claim | Grade |
|---|---|
| Six-dimensional source cohomology splits as two conjugate line-times-rotation triples | **COMPUTED EXACTLY; proved by cochain formulas** |
| Printed intertwiner matches the manuscript's exact S,T coefficient matrices | **EXACT** |
| Independent Hodge–Riemann sign determination | **NOT PERFORMED** |
| Complete common local holomorphic algebra across the deformation interval | **PROVED for the specified spin-charge family** |
| Direct local protected-current realization of full T | **EXCLUDED for the specified internal normalizer action** |
| Geometric line-valued map from T to protected currents | **CONSTRUCTED EXACTLY; not promoted to a quantum block** |
| Ordinary protected affine-spinor torus blocks yield a triplet | **EXCLUDED in that ordinary primary-block problem** |
| Full Q8-crossed puncture amplitudes, physical determinant connection and sewing | **NOT CALCULATED** |
| Selection of interactions, 4d chiral matter or gravity | **NOT DERIVED** |

The next well-specified quantum object is the **Q8-twisted puncture block with its actual geometric coefficient-line transport**, not another scalar eta prefactor or another internal three-dimensional representation. A proposed realization must compute the original central loop and both modular generators as physical block transport, and supply nonzero compatible puncture sewing maps. A local current basis change cannot answer that question.

## References and roles

1. Dritëro M., *A Weave of Two Records* (supplied PDF, October 2026), §§2–4 and §7. Source of the target and of the declared physical assumptions.
2. Supplied *Weave Quantum Realization — Run 5* report. Source of the interacting spin-charge family and the distinction between preserved symmetry and preserved free puncture prescription.
3. Pinned repository B1634 findings, commit `6c148ddd495d133213140995976ff08849793d5d`: https://github.com/originaxiom/origin-axiom/blob/6c148ddd495d133213140995976ff08849793d5d/frontier/B1634_w50_on_main/FINDINGS.md . Consulted for the source's contravariant lift convention, not imported as executable verification code.
4. S. Förste and D. Roggenkamp, *Current-Current Deformations of Conformal Field Theories, and WZW Models*, arXiv:hep-th/0304234, especially §2 and Appendix A. Established charge-lattice deformation and parallel operator-structure framework. https://arxiv.org/abs/hep-th/0304234
5. E. Rowell, R. Stong and Z. Wang, *On classification of modular tensor categories*, arXiv:0712.1377, especially §5.3.1. Standard semion data and distinction between fusion categories and mere group representations. https://arxiv.org/abs/0712.1377
6. M. R. Gaberdiel and S. Lang, *Modular differential equations for torus one-point functions*, arXiv:0810.0106, §2. Torus one-point amplitudes require an allowed return channel in fusion. https://arxiv.org/abs/0810.0106
7. C.-M. Chang, J. Chen and F. Xu, *Topological Defect Lines in Two Dimensional Fermionic CFTs*, arXiv:2208.02757. Fermionic endpoint/junction data are additional to ordinary primary fusion. https://arxiv.org/abs/2208.02757
8. NIST DLMF §§20.7 and 23.18. Theta and eta transformation identities. https://dlmf.nist.gov/20.7 ; https://dlmf.nist.gov/23.18

No novelty claim is made for group cohomology, the lattice chiral algebra, the semion category, or theta transformations. The work in this packet is their explicit, scoped reconstruction and comparison for the supplied weave.
