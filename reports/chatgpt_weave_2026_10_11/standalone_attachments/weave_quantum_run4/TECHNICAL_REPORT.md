# Quantum realization of the weave — Run 4
## Genuine operator products, complete automorphy bundles, and an unfixed quantum coupling

**Date:** 10 October 2026.  
**Source basis:** *A Weave of Two Records*, §§2–4 and §7; the supplied Run 2 and Run 3 technical reports.  
**Scope:** A continuation and scope audit of the specified two-dimensional Gaussian model, with new exact algebra, charged-current Ward calculations, and an explicitly identified nonchiral bulk control. No project-repository edits, no Standard Model data, no gravitational completion.

## Executive conclusion

The Run 3 identities and the fixed-multiplier mismatch are retained. The inference drawn from them must remain narrower than a physical anomaly or a failure of every local triplet realization.

1. The quadratic vector K used in Run 3 is a **product of separate amplitudes**. It is not the same-theory correlator of two fermions. A direct Berezin calculation with one zero mode proves the distinction. All unnormalized correlators in one Gaussian theory carry one common nonzero-mode determinant, whereas a product of two separately integrated amplitudes carries its square.
2. The same four real fermions have a genuine local Q8 parity triplet: three weight-one currents. Their operator products are the level-one su(2) algebra. The other three weight-one currents commute with them and are Q8 singlets. The full weight-one space is six-dimensional, not only the desired three-dimensional subspace. This is known free-fermion current algebra, independently reconstructed here in the weave's quaternion basis.
3. Keeping modular weights, not only finite coefficient matrices, changes the geometric comparison. Multiplication by eta^2 intertwines the **complete holomorphic automorphy bundles** of the geometric and Gaussian quadratic vectors on the open moduli space. Multiplication by eta^22 similarly relates K to Phi. These maps do NOT automatically preserve a physical metric, connection, quantum normalization, or cusp boundary prescription.
4. Genuine conditional current responses can be calculated in the same puncture background. Their common oscillator determinant cancels in ratios to the nonzero saturated reference amplitude. This is not division by the insertion-free partition function, which vanishes.
5. A constant basis change, an invariant local scalar factor, and an ordinary Q8 discrete-torsion correction do not furnish the required compensation in the stated fixed-multiplier comparison. The ordinary cohomology check is explicitly not a classification of the full fermionic symmetry or metaplectic anomaly.
6. The commuting current sector admits an exactly marginal deformation in a standard diagonal nonchiral bulk control. Thus the current algebra, Q8 action and bulk quantum consistency alone leave an actual continuous physical parameter. We have NOT shown that the complete puncture data or Phi survive this deformation. Determining whether those additional data eliminate the parameter is now a concrete selection test.

The local quantum role of the three parity components is clearer. There is still no derivation of the exact metaplectic matter triplet as local currents, of three gauge-chiral generations, or of a unique spacetime theory.

---

## 1. What is inherited from Run 3

Write

\[
v(\tau)=(\theta_2^2,\theta_3^2,\theta_4^2)^T,
\quad G=\frac{v}{\eta^3},\quad K=\frac{v}{\eta},
\quad \Phi=\eta^{21}v.
\]

Run 3 derived, in its declared chiral oscillator/OPE normalization,

\[
\mathcal A(z|\tau)=\eta(\tau)s(z|\tau),\qquad
s=\frac{(\theta_3(z|2\tau),\theta_2(z|2\tau))^T}
{\sqrt{\theta_1(z|\tau)}}.
\]

There is **one vector-valued zero mode**, not two. Its residue has two coordinate components. Run 3 then formed K by taking quadratic functions of those components. The report explicitly warned that these functions were not being declared a two-identical-fermion state space or a complete set of rational-CFT sectors.

The inherited coefficient multipliers are

\[
\rho_G=\rho_\Phi=\chi_{\eta^3}\otimes O,
\qquad \rho_K=\chi_{\eta^5}\otimes O,
\]

but the respective modular weights are -1/2, 23/2 and 1/2. In particular, an exact comparison of the finite matrices alone is a comparison of only part of the automorphy data.

This run does not silently replace any of these source formulas. It tests the physical interpretation of the products and the stronger geometric implications of the mismatch.

## 2. One theory has one measure: a direct zero-mode calculation

At a finite-mode cutoff, write the fermion field as

\[
\psi_i=a s_i+\sum_{\alpha=1}^N b_\alpha v_{i\alpha},
\qquad S=\sum_{\alpha,\beta}\bar b_\alpha D_{\alpha\beta}b_\beta.
\]

Here a is the Grassmann coefficient of the single zero mode and D is invertible on the other modes. Choose the Berezin orientation so that

\[
\mathfrak I[a]=\det D,
\qquad \mathfrak I[X]=\int da\,d\bar b\,db\, X e^{-S}.
\]

Then

\[
\mathfrak I[1]=0,\qquad
\mathfrak I[\psi_i]=\det D\,s_i,\qquad
\boxed{\mathfrak I[\psi_i\psi_j]=0.}
\]

The last statement follows without approximation: any term with two a's vanishes, and a term with one a and one unpaired nonzero-mode b has zero Gaussian integral. In contrast,

\[
\mathfrak I[\psi_i]\mathfrak I[\psi_j]
=(\det D)^2s_i s_j
\]

can be nonzero. Products of separately evaluated amplitudes belong to a tensor product of amplitude lines. A same-theory operator insertion, or a properly sewn amplitude, needs contractions and the appropriate gluing maps.

With one conjugate insertion and the ordering psi_i psi_j barpsi^k, Wick's rule gives

\[
\mathfrak I[\psi_i\psi_j\bar\psi^k]
=\det D\,[s_i G_j{}^k-s_jG_i{}^k],
\]

where G is the inverse nonzero-mode kernel. There is still one determinant. This formula is valid at every finite cutoff. Its regularized determinant-line version is the standard Gaussian structure, not a new eigenvalue computation [F].

### Independent finite verification

The code implements a five-generator exterior algebra, with one zero variable and two paired modes, using

\[
D=\begin{pmatrix}2&1\\1&3\end{pmatrix},\qquad \det D=5.
\]

All nine two-psi integrals vanish; all eighteen psi-psi-barpsi combinations obey the alternating Wick formula. A product of two selected one-insertion integrals equals 75, while the corresponding two-insertion integral is zero. The sign of the integration orientation is declared in the output.

### Consequence

Run 3's multiplier mismatch for K is not corrected or erased. It remains a true statement about the specified quadratic vector. What is now ruled out is treating K, without a further sewing or operator construction, as the automatically required local triplet correlator of the same one-zero-mode Gaussian theory. The earlier report already flagged this distinction; the present calculation makes its consequence explicit.

## 3. The complete weight-one operator algebra

Let chi=(chi_0,chi_1,chi_2,chi_3)^T be four real chiral fermions, with

\[
\chi_a(z)\chi_b(w)\sim\frac{\delta_{ab}}{z-w}.
\]

Let L_a and R_a be the real 4x4 matrices of left and right multiplication by the three imaginary quaternions. They obey

\[
[L_a,L_b]=2\epsilon_{abc}L_c,\quad
[R_a,R_b]=-2\epsilon_{abc}R_c,\quad [L_a,R_b]=0.
\]

With one fixed orientation convention, define

\[
J_a=\frac{i}{4}:\chi^T L_a\chi:,
\qquad I_a=-\frac{i}{4}:\chi^T R_a\chi:.
\]

Direct Wick contraction gives

\[
\boxed{
J_a(z)J_b(w)\sim
\frac{\delta_{ab}}{2(z-w)^2}
+\frac{i\epsilon_{abc}J_c(w)}{z-w}.}
\]

The same formula holds for I. Every J-I operator product is regular. Both levels are one. Their Sugawara central charges are 1 and 1, exhausting the original c=2 theory:

\[
\mathfrak{so}(4)_1\cong\mathfrak{su}(2)_{1,A}\oplus
\mathfrak{su}(2)_{1,B}.
\]

This is known conformal embedding/current algebra. The quaternion left/right construction appears, for example, as n=1 of the more general embedding in [C]. Here the entire singular OPE is recomputed from the free fermions rather than assumed from a Lie-algebra label.

### Quaternion and normalizer action

The two quaternion generators act on the J currents as

\[
i:(J_1,J_2,J_3)\mapsto(J_1,-J_2,-J_3),
\]

\[
j:(J_1,J_2,J_3)\mapsto(-J_1,J_2,-J_3).
\]

These are precisely the three nontrivial parity characters, up to ordering. All three I currents are Q8 singlets.

The two prescribed normalizer lifts produce

\[
O_L=\begin{pmatrix}1&0&0\\0&0&-1\\0&1&0\end{pmatrix},\qquad
O_R=\begin{pmatrix}0&0&-1\\0&1&0\\1&0&0\end{pmatrix}.
\]

Their exact image has order 24. These are the rotation matrices used in Run 2. Thus the local currents naturally realize O, **not** its extra scalar twist chi_eta3. Normal ordering does not create that scalar twist in the field transformation law. A torus block containing a current can have additional determinant/sector multipliers; these are separate from the local operator action.

The first six currents are complete: at conformal weight one, the free NS vacuum Fock space is exterior^2(C^4), of dimension six. Its Q8 decomposition is

\[
\boxed{\mathcal H_{h=1}=\mathbf1^{\oplus3}\oplus\chi_1\oplus\chi_2\oplus\chi_3.}
\]

The script also enumerates the graded Q8 characters through h=6. Initial rows are:

| h | total dimension | trivial multiplicity | each parity multiplicity | quaternion doublet multiplicity |
|---|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 | 0 |
| 1/2 | 4 | 0 | 0 | 2 |
| 1 | 6 | 3 | 1 | 0 |
| 3/2 | 8 | 0 | 0 | 4 |
| 2 | 17 | 5 | 4 | 0 |

This is the untwisted local NS operator algebra, not the twisted torus-block spectrum. Its J currents are bosonic composite operators. They are not three elementary fermions, three zero modes, or four-dimensional gauge bosons. Their OPE is a genuine quantum composition law, but does not make the free model an interacting spacetime theory.

## 4. Actual conditional current responses in the puncture background

To retain the Run 3 background rather than only calculating a local flat-plane algebra, use its abelianized cover, with modulus T=2tau. The positions and charges are

\[
(z_r,a_r)= (z,+1),(0,-1/2),(\tau,-1/2),\qquad
Z=\sum_r a_r z_r=z-\tau/2.
\]

Let

\[
\Theta(Z)=\theta[1/4,0](Z|T),\quad
E_T(w)=\theta_1(w|T)/\theta_1'(0|T).
\]

The saturated reference amplitude is nonzero at the tested generic points. Define a conditional current response as the ratio of a current-inserted block to that reference block. It is NOT an expectation normalized by the zero insertion-free partition function.

For the bosonized Abelian current j=i partial phi, differentiating the charged trace gives

\[
\boxed{
\mathcal J(w)=\frac{\Theta'(Z)}{\Theta(Z)}
+\sum_r a_r\,\partial_w\log E_T(w-z_r).}
\]

Its residues are exactly +1,-1/2,-1/2 at the three marked points. The connected two-current response is

\[
\boxed{
\mathcal C(w,v)=
-\partial_u^2\log E_T(u)\big|_{u=w-v}
+\partial_Z^2\log\Theta(Z).}
\]

In particular,

\[
\mathcal C(w,v)\sim\frac1{(w-v)^2}.
\]

These follow by introducing infinitesimal neutral charge pairs into the same trace. The source differentiation is an algebraic generating technique, not the addition of arbitrary continuously charged physical operators. The oscillator/prime-form machinery is standard [MT]; the formulas above specialize it to the declared Run 3 charge data.

A factor depending only on tau, including the common nonzero-mode determinant, cancels from these conditional responses. It does not need to be deleted from the underlying unnormalized theory. This gives actual observables for which the common eta factor does not enter, instead of trying to manufacture a compensating sector.

### Verification and limits

The code checks a direct finite neutral-source derivative, independent position differentiation of its linear coefficient, the connected log derivatives, the charge residues, and the level-one current pole. It uses direct theta sums and no Run 3 verification functions.

This is an Abelian Ward calculation on the unfolded cover. It is **not** a construction of every nonabelian Q8 puncture junction or an all-genus defect sewing theorem. The local J-current triplet in §3 and the global Abelian responses here are distinct, compatible partial calculations; no uncomputed global triplet correlator is claimed.

## 5. The full automorphy comparison

A vector-valued modular object is specified by both weight k and coefficient multiplier rho:

\[
f(\gamma\tau)=(c\tau+d)^k\rho(\gamma)f(\tau).
\]

The finite rho alone is not the full transformation law.

### 5.1 An exact holomorphic bundle isomorphism on the open moduli space

Let h=eta^2. Since eta has no zeros on the upper half-plane [D], h is invertible there, and

\[
K=hG.
\]

Moreover,

\[
h(\tau+1)=e^{\pi i/6}h(\tau),\qquad
h(-1/\tau)=(-i\tau)h(\tau).
\]

These are exactly the relative **full** automorphy factors between weights -1/2 and +1/2 and their coefficient multipliers. Therefore multiplication by h is an equivariant holomorphic isomorphism of these two automorphy bundles over the smooth/open modular orbifold (with the declared metaplectic lifts). Similarly, eta^22 maps the bundle of K to the bundle of Phi.

This includes stabilizers. At tau=i,

\[
\chi_{\eta^2}(S)(c\tau+d)=(-i)i=1.
\]

At the ST fixed point omega, the factors are exp(-pi i/3) and exp(pi i/3), again multiplying to one. At -I, both factors are -1. Looking only at finite coefficient matrices would miss these cancellations.

There is no conflict with the known order-twelve Hodge line on the open moduli stack; character and weight factors must be treated together. The general Picard-group background is given in [FO]. The specific bundle maps here are proved directly from the eta identities, not inferred from a Picard-group slogan.

### 5.2 Why this is not automatically a physical equivalence

The map changes the oscillator-normalized section. It also changes the cusp behavior:

\[
\eta^2=q^{1/12}(1+O(q)),\qquad
\eta^{22}=q^{11/12}(1+O(q)).
\]

An invertible map on the open moduli space need not remain invertible at the cusp with a prescribed asymptotic extension. No vacuum-energy or boundary condition is thereby preserved.

Given a connection nabla_G=d+A_G and a Hermitian metric H_G, the isomorphism f_K=h f_G can be made connection-compatible and isometric by **transporting** the data:

\[
A_K=A_G-d\log h,\qquad H_K=|h|^{-2}H_G.
\]

Indeed, nabla_K(h f)=h nabla_G(f). This is a mathematical change of frame/data, not evidence that independently specified physical metrics equal these transported choices.

A concrete control uses the usual modular norm

\[
\|f\|_k^2=y^k f^\dagger f,\quad y=\operatorname{Im}\tau.
\]

Then

\[
\frac{\|K\|_{1/2}^2}{\|G\|_{-1/2}^2}=y|\eta|^4,
\qquad
\frac{\|\Phi\|_{23/2}^2}{\|K\|_{1/2}^2}
=(y|\eta|^4)^{11}.
\]

These positive factors are nonconstant. Since log|eta| is harmonic on H,

\[
\partial_\tau\partial_{\bar\tau}\log(y|\eta|^4)
=-\frac1{4y^2}.
\]

Thus these particular standard metrics are not isometric under the holomorphic map and have a nonzero relative Chern curvature. The corresponding coefficient for Phi/K is eleven times larger. No orbifold degree is inferred here by integrating over an effective fundamental domain; stack stabilizer conventions would have to be retained.

The projectors ff^dagger/(f^dagger f) of G,K,Phi coincide exactly in the common coordinate trivialization. This proves equality of their projective directions, not equality of independently specified determinant-line holonomies.

**Boundary:** None of these modular-norm calculations is the Quillen metric of the singular punctured operator. A physical/global anomaly requires the relevant metric/connection and its allowed counterterms; [F] makes that distinction explicit. Run 3 did not compute those data, and this run does not re-label a Petersson-norm calculation as Quillen theory.

## 6. Restricted repair tests

### Constant basis changes and invariant scalar factors

The different T eigenvalues retained from Run 3 still exclude a constant intertwiner between the finite coefficient representations. An invariant scalar counterterm f has f(tau+1)=f(tau). It cannot supply the nontrivial factor exp(-pi i/6). The simple wrong-character test has residual 2 sin(pi/12), approximately 0.517638.

This is a restriction on **invariant scalar** counterterms with the stated background and frame data, not a classification of all anomalous counterterms, bulk inflow theories or additional fields.

### Ordinary Q8 discrete torsion has no order-three component

The needed inverse character chi_eta^(-2) has order twelve and a nontrivial order-three component. For ordinary finite-group cohomology with trivial F3 coefficients, averaging over Q8 is allowed because 8 is invertible modulo 3. Hence H^n(Q8,F3)=0 for n>0. More generally, transfer implies that positive-degree ordinary Q8 cohomology classes with U(1) coefficients have orders dividing a power of two (indeed they are killed by |Q8|). There is no nontrivial ordinary discrete-torsion class of order three.

The script constructs the full normalized cochain matrices through degree four. Over F3 the differential ranks are

\[
7,\quad42,\quad301,
\]

on cochain dimensions 7,49,343,2401. Thus H^2 and H^3 both vanish. As a positive control, the same implementation gives dimensions one for both H^2(C3,F3) and H^3(C3,F3).

This rules out an order-three compensation from a **nontrivial ordinary Q8 discrete-torsion class**. It does not prohibit gauge-dependent cube roots in a coboundary convention, which do not supply a new invariant. Nor does it classify the full metaplectic group, normalizer, or Spin-Q8 symmetry, where the central quaternion element can be tied to fermion parity. Those are different problems.

Similarly, a bare Arf spin phase has only a sign and cannot supply the required cubic component. The Arf/Arf-Brown framework is reviewed in [AB]. No general spin-symmetry anomaly classification is claimed here.

## 7. A continuous parameter survives bulk symmetry and consistency

The other three currents were not added; they were already present in the four real fermions. In the standard diagonal nonchiral current-algebra control, select I_3 and its antichiral partner. The local perturbation

\[
\delta S=g\int d^2z\,I_3(z)\bar I_3(\bar z)
\]

is Q8 invariant because every I current is a Q8 singlet. It also commutes with the quaternion normalizer action on the J triplet.

This is an exactly marginal current-current deformation. The needed commutativity criterion is established in [FRg]; its elementary realization here is a compact free boson whose kinetic coefficient, equivalently radius R, varies. The triplet su(2) sector is unchanged. This is an established CFT deformation, not a newly discovered interaction or a proposed TOE.

For a convention with p_L=m/R+nR/2 and p_R=m/R-nR/2,

\[
h+\bar h=\frac{m^2}{R^2}+\frac{n^2R^2}{4},\qquad
h-\bar h=mn.
\]

The scaling dimensions change while conformal spin remains integral. The central charge stays two in each chiral half of this diagonal bulk control. Thus this is not just a change of notation or normalization: it changes spectral data.

**What is preserved:** the displayed local J-current algebra, its Q8/parity and normalizer action, unitary bulk CFT consistency, and the central charge.

**What has NOT been shown to be preserved:** the original fermionic spin completion with every global choice, the precise E_+ puncture state and its boundary domain, all Q8 defect-junction amplitudes, the exact theta functions Phi, or the original cohomology-to-physics link. Radius R is a coupling of this two-dimensional CFT, not automatically a spacetime radius or the original torus modulus tau.

Therefore this is a counterexample to uniqueness from the **reduced bulk data**, not from every piece of the weave. The complete puncture/connection/sewing data might still select one point. Establishing that would be a genuine dynamical selection result.

## 8. What changed and the next justified calculation

The main change is not a new eta prefactor. It is a more faithful separation of three different objects:

- geometric cohomology/theta data;
- genuine local operators and their quantum products;
- quantum amplitude lines with metrics, connections and cusp behavior.

The triplet now has a concrete local realization as currents, but only at the rotation-representation level. The scalar mismatch remains exact for the original quadratic-amplitude comparison, yet it is not by itself a holomorphic bundle obstruction or a proven physical anomaly. The existing fields also leave a nontrivial bulk deformation.

The next narrowly justified test is whether the **complete quaternion puncture and its sewing/transport data** remain consistent along the commuting-current deformation, and whether those conditions select a coupling without matching observed numbers or imposing the target eta factor. A surviving continuous family would demonstrate a remaining input. A unique point would be a meaningful selection result. A failure to transport the defect would reject that deformation as a full completion, not invalidate the bulk theorem.

The independent target of a full singular-operator Quillen connection remains open; it should not be conflated with the just-computed modular norm. No result here supplies a Standard Model gauge group, gauge chirality, gravity or measured parameters.

## 9. Reproducibility and integrity

Run:

```
python verify_exact.py
python verify_cocycles.py
python verify_ward_and_bundles.py --dps 60
python verify_ward_and_bundles.py --dps 90
```

- 46 exact algebraic checks, including all OPE pairs, finite-mode Wick checks, full weight-one completeness, and NS graded character decompositions through h=6.
- Five cochain checks, including the nontrivial C3 positive control. Rank computations use modular integer arithmetic, not floating-point rank thresholds.
- 55 numerical comparisons at each precision: 40 strict formula checks and 15 explicitly finite-distance/source limits.
- At 90 digits the largest strict normalized residual is about 6.14e-91. The largest finite-distance/source residual is about 3.36e-30. At 60 digits the corresponding values are about 4.67e-61 and 3.36e-20.

These are arithmetic checks and high-precision corroborations, not an interval proof, independent research teams, a Dirac eigensolver or 106 separate physics discoveries. The infinite identities and coherence claims are limited to those analytically derived above or attributed to the cited CFT frameworks.

The working plan was written after source reading and exploratory reasoning and before formal scripts. It is not blind or independently timestamped. Two exact-code convention/assertion fixes and an inefficient numerical differentiation implementation are recorded in CHANGELOG.md; initial script snapshots are retained as .txt for inspection. The final scripts were rerun. No prior project verification code was imported.

## References and source boundaries

[F] D. S. Freed, *On Determinant Line Bundles* (1987), especially §§1 and 4. Determinant lines, metrics, connections and anomaly holonomy; not a computed solution of this punctured operator. https://web.ma.utexas.edu/users/dafr/detsur.pdf

[C] M. Cheng, *Microscopic Theory of Surface Topological Order for Topological Crystalline Superconductors*, arXiv:1707.02079, supplement equations S17–S24. The n=1 quaternion left/right conformal embedding specializes to su(2)_1 x su(2)_1 in so(4)_1. The broader condensed-matter application is not imported here. https://arxiv.org/abs/1707.02079

[MT] G. Mason and M. P. Tuite, *Torus Chiral n-Point Functions for Free Boson and Lattice Vertex Operator Algebras*, arXiv:math/0204323. Oscillator and prime-form machinery. Fractional-source specialization is derived as a formal current-generating derivative of the Run 3 twisted amplitude, not claimed verbatim from an even-lattice theorem. https://arxiv.org/abs/math/0204323

[D] NIST DLMF §§20.7 and 23.18. Theta/eta modular transformations. https://dlmf.nist.gov/20.7 ; https://dlmf.nist.gov/23.18

[FO] W. Fulton and M. Olsson, *The Picard group of M_{1,1}*, Algebra & Number Theory 4 (2010), 87–104. Weight/Hodge bundle and open-versus-compactified moduli background; the specific eta maps here are checked directly. https://msp.org/ant/2010/4-1/ant-v4-n1-p04-s.pdf

[FRg] S. Forste and D. Roggenkamp, *Current-Current Deformations of Conformal Field Theories, and WZW Models*, arXiv:hep-th/0304234, §2. The Abelian current-current marginality criterion and continuous deformation spaces. https://arxiv.org/abs/hep-th/0304234

[AB] A. Debray and S. Gunningham, *The Arf-Brown TQFT of Pin-minus Surfaces*, arXiv:1803.11183, including its restriction to spin surfaces. Used only for the sign/topological-phase control. https://arxiv.org/abs/1803.11183

No literature-novelty claim is made for the Gaussian integral, current algebra, group-cohomology vanishing, modular identities, or marginal deformation. The new work in this packet is their explicit implementation and appropriately scoped application to the fixed weave comparison.
