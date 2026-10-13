# Quantum realization of the weave — run 2
## The faithful cover, theta-state doublet, spin structures and the remaining scalar phase

**Date:** 10 October 2026.  
**Basis:** *A Weave of Two Records* (October 2026), §§2–4, and the preceding *Weave Quantum Realization — Run 1*.  
**Scope:** Independent mathematics and conditional two-dimensional quantum constructions. No Standard Model input, no claim of four-dimensional chirality or gravity, and no edits to the user's repository or PDF.

## Executive result

The faithful quaternion cover is the known genus-three quaternion origami, also called the Eierlegende Wollmilchsau. It is not a newly discovered curve. Its explicit equation allows the geometric state spaces and ordinary compact spin structures to be determined rather than guessed.

1. Its holomorphic differentials decompose under the deck group as **one trivial line plus one quaternion doublet**, not three parity lines.
2. The doublet is naturally identifiable, fiberwise, with the two-dimensional space of sections of a degree-two line bundle on the elliptic quotient. Its quadratic products give the theta-squared triplet by classical duplication identities.
3. All **64 compact spin structures** were enumerated. There are 36 even and 28 odd. None is invariant under the entire deck group Q8. The particular based lifts of the specified L and R fix exactly one odd spin structure. This is a lift-dependent subgroup statement, not a deck-independent selection.
4. The compact spin Dirac problem has zero or one holomorphic spinor for each spin structure, never three. The minimal rank-two parabolic Dolbeault extensions downstairs have kernel/cokernel dimensions (0,1) or (1,0), respectively. These latter counts require explicitly stated extension domains.
5. The manuscript's full three-dimensional multiplier factors **exactly** as a scalar eta-cubed multiplier times the rotation representation of the quaternion normalizer. The scalar is precisely identified, but its emergence from a faithful quantum determinant has not been derived.

This run therefore constructs a more intrinsic theta-state candidate and narrows the quantum problem. It does **not** compute the full Q8-twisted puncture correlators, determinant/Pfaffian line, connection or sewing data. A known geometric quantization space is not yet the required local quantum theory.

---

## 1. Source boundaries and conventions

The source manuscript defines

\[
\bigoplus_{p\ne0} H^1(F_2;\chi_p\otimes\rho_Q)=T\oplus\bar T,
\qquad \dim T=3,
\]

with \(\rho_Q(a)=i,\rho_Q(b)=j\), and specifies the multiplier of

\[
\Phi(\tau)=\eta(\tau)^{21}(\theta_2(\tau)^2,\theta_3(\tau)^2,\theta_4(\tau)^2).
\]

This run compares against that specified multiplier. It does not independently reconstruct the original manuscript's Hodge-basis intertwiner.

The group elements in the code are ordered

\[
(1,i,j,k,-1,-i,-j,-k).
\]

The grammar is

\[
L:a\mapsto a,\ b\mapsto ab,\qquad
R:a\mapsto ab,\ b\mapsto b.
\]

Based lifts are fixed by making the induced graph map send the vertex labelled 1 to itself. Changing the lift by a deck transformation can change its action on spin structures. The spin computations below must not be reported without this qualification.

---

## 2. The cover is a known curve, not a new quantum theory

The kernel of \(F_2\twoheadrightarrow Q_8\) is exactly the defining subgroup of the quaternion origami studied by Herrlich and Schmithüsen [HS]. Their Proposition 5 gives the smooth plane-quartic family

\[
X_\lambda:\quad y^4=x(x-1)(x-\lambda),\qquad \lambda\ne0,1,\infty.
\]

Its central quotient is

\[
E_\lambda:\quad v^2=x(x-1)(x-\lambda),\qquad
f(x,y)=(x,y^2).
\]

The full degree-eight origami map is the degree-two quotient followed by the degree-four multiplication-by-two map on the elliptic curve. The four branch points of f are the four two-torsion points. This is the same cover as Run 1, not a newly selected thread.

The known kernel is characteristic in F2, stronger than merely being preserved by L,R. The calculation in this run uses only the stated L,R and deck transformations.

[HS] also prove the isogeny

\[
\operatorname{Jac}(X_\lambda)\sim E_\lambda\times E_i\times E_i.
\]

This is cited background, not a new computation here. An isogeny is **not** an equality of principally polarized Jacobians and does not justify replacing the genus-three quantum determinant by three independent elliptic determinants. No such factorization is used.

### Independent topology calculation

The punctured cover retracts to a graph with eight vertices and sixteen edges. Thus its first homology has dimension nine. Four lifted peripheral loops are filled on compactification, with one relation among them, giving compact first-homology dimension six.

The code constructs the integer boundary map, a fundamental-cycle basis, all four cap cycles, and the L,R and deck chain maps. A separately constructed ribbon-graph intersection pairing has rank six and annihilates exactly the cap span.

The compact Q8 character is

| element | 1 | -1 | ±i | ±j | ±k |
|---|---:|---:|---:|---:|---:|
| trace on H1(X,C) | 6 | -2 | 2 | 2 | 2 |

Consequently

\[
H^1(X,\mathbb C)\cong\mathbf1^{\oplus2}\oplus\rho_2^{\oplus2}.
\]

No nontrivial one-dimensional parity character occurs in compact H1.

---

## 3. Actual holomorphic forms: a singlet and a doublet

An explicit basis is

\[
\omega_0=\frac{dx}{y^2},\qquad
\omega_1=\frac{dx}{y^3},\qquad
\omega_2=\frac{x\,dx}{y^3}.
\]

At a finite branch point, use y as local parameter: x-a has order four and dx has order three. At infinity, a local parameter t has

\[
\operatorname{ord}_\infty x=-4,\quad
\operatorname{ord}_\infty y=-3,\quad
\operatorname{ord}_\infty dx=-5.
\]

Thus a monomial \(x^j dx/y^k\) is holomorphic only if

\[
3-k\ge0,\qquad 3k-4j-5\ge0.
\]

For 1≤k≤3 these give exactly the three forms above. Smoothness of the plane quartic implies genus three, so they exhaust the space.

The central involution sends y to -y. It fixes omega0 and negates omega1,omega2. All noncentral nonidentity Q8 deck transformations are fixed-point-free. Holomorphic Lefschetz gives the character

\[
\chi_{H^0(K)}(1,-1,\pm i,\pm j,\pm k)=(3,-1,1,1,1).
\]

Therefore

\[
\boxed{H^0(X,K_X)=\mathbf1\oplus W,\qquad W\cong\rho_2.}
\]

This is a Q8-module statement. Holomorphic one-forms are not spin-1/2 zero modes.

### Explicit quaternion action

On the doublet (omega1,omega2), one can use

\[
A_W=\begin{pmatrix}0&-i\sqrt\lambda\\-i/\sqrt\lambda&0\end{pmatrix},\qquad
B_W=\frac1{\sqrt{\lambda-1}}
\begin{pmatrix}-1&-\lambda\\1&1\end{pmatrix}.
\]

These arise from the transformations

\[
(x,y)\mapsto(\lambda/x,\ i\sqrt\lambda\,y/x),
\]

\[
(x,y)\mapsto((x-\lambda)/(x-1),\ \sqrt{\lambda-1}\,y/(x-1)).
\]

Direct substitution verifies the curve equation and

\[
A_W^2=B_W^2=-I,\quad A_WB_W=-B_WA_W,\quad
\det A_W=\det B_W=1.
\]

Square-root branches choose the signs of the lifts; no physical selection is attributed to them.

---

## 4. The doublet comes from degree-two theta sections

The double cover f is specified by a line bundle \(\mathcal L\) with

\[
\mathcal L^2\cong\mathcal O_E(B),\qquad \deg\mathcal L=2,
\]

where B is the sum of the four branch points. In the displayed marked equation,

\[
\mathcal L\cong\mathcal O_E(2O).
\]

Indeed, the elliptic function v has divisor

\[
\operatorname{div}(v)=P_0+P_1+P_\lambda-3O=B-4O.
\]

The double-cover canonical formula gives

\[
f_*K_X\cong K_E\oplus(K_E\otimes\mathcal L).
\]

Since \(K_E\cong\mathcal O_E\),

\[
\boxed{W\cong H^0(E,\mathcal L),\qquad h^0(E,\mathcal L)=2.}
\]

The dimension follows from elliptic Riemann–Roch, not a desired particle count.

In a theta trivialization, use

\[
\Theta_r(z;\tau)=
\sum_{n\in\mathbb Z}
\exp\left(2\pi i\tau(n+r/2)^2+4\pi i(n+r/2)z\right),
\quad r=0,1.
\]

These are degree-two theta sections. Normalized translations by half periods act by

\[
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad XZ=-ZX.
\]

Thus iZ and iX generate a faithful Q8 action. Explicitly,

\[
\Theta_r(z+1/2)=(-1)^r\Theta_r(z),
\]

\[
e^{\pi i\tau/2+2\pi iz}\Theta_r(z+\tau/2)=\Theta_{1-r}(z).
\]

This is the familiar finite Heisenberg/theta construction [Y], now reached through the specified cover. Interpreting these sections as a geometric-quantization Hilbert space is a **candidate quantum reading**, not a derivation of a Hamiltonian or four-dimensional fields. Magnetic translations on this positive-degree line bundle are not automatically identical to parallel transport in the original flat rank-two punctured bundle.

### Quadratic products recover the three functions exactly

At z=0 put u=Theta0=theta3(2tau), v=Theta1=theta2(2tau). Classical duplication gives

\[
\boxed{
\theta_2(\tau)^2=2uv,\quad
\theta_3(\tau)^2=u^2+v^2,\quad
\theta_4(\tau)^2=u^2-v^2.
}
\]

These identities are not new; see [DLMF]. Their use here identifies the three functions with the quadratic sector of the degree-two section space supplied by the cover.

Under iZ and iX, the ordered quadratics (2uv,u²+v²,u²-v²) transform by

\[
\operatorname{diag}(1,-1,-1),\qquad
\operatorname{diag}(-1,-1,1).
\]

They are exactly the three nontrivial parity characters; the middle component is negative on both generators, matching the manuscript's clock-line assignment.

Numerical checks used direct series in tau, avoiding fractional-nome branch ambiguity. Five generic/sample moduli were used, with 55 comparisons covering duplication, S,T and both normalized translations. At 100 decimal digits the largest residual was approximately 5.73e-101. These are high-precision corroborations, not interval bounds; the identities have analytic proofs.

### Statistics warning

Sym²W is a three-dimensional space of quadratic **holomorphic sections**. It is not automatically a three-state fermion Fock sector. For two identical fermionic zero modes,

\[
\Lambda^*W=\mathbf1\oplus W\oplus\Lambda^2W
\]

has dimensions 1+2+1; the two-particle sector has dimension one. A traceless operator space End0(W) is three-dimensional, but those operators are not thereby three fermionic generations. Any physical use of the quadratic triplet must state its statistics and operator meaning.

---

## 5. All compact spin structures, not just a chosen favorable example

Spin structures on a genus-three compact surface are the 64 quadratic refinements of its mod-two intersection form. Their parity agrees with h0(S) mod 2 for the corresponding theta characteristic \(S^2=K_X\) [A].

The code constructs the ribbon graph from the eight-sheeted cover, contracts a spanning tree to a chord diagram, and obtains an exact 9×9 alternating intersection matrix of rank six. Every quadratic refinement on graph homology is enumerated; those vanishing on the three independent cap classes descend to the compact surface. Exactly 64 do so.

The complete calculation was repeated with a different spanning tree. Spin labels change with basis, but counts, fixed-point counts and orbit sizes agree.

### Results

- 36 even theta characteristics and 28 odd.
- No theta characteristic fixed by both deck generators i,j.
- The particular based L,R lifts fix exactly one theta characteristic, and it is odd.
- That theta characteristic belongs to a four-element orbit under Q8.
- Each of these L,R fixes eight spin structures separately; each deck i,j,k fixes four; the central deck involution fixes sixteen. Individual fixed-point existence does not imply a common fixed point for a group.

Orbit sizes under Q8:

- even: six orbits of size 2 and three of size 8;
- odd: one orbit of size 4 and three of size 8.

Under the subgroup generated by the specified based L,R lifts:

- even: 12 and 24;
- odd: 1, 3 and 24.

Under deck Q8 together with those L,R lifts:

- even: 12 and 24;
- odd: 4 and 24.

The 3-element orbit is not a three-dimensional conformal-block calculation. Orbit size alone supplies neither amplitudes nor a metaplectic scalar multiplier.

### Why the selected odd spin has one section

The curve is a smooth plane quartic, hence nonhyperelliptic. A degree-two line bundle with at least two independent sections would yield a degree-two map to P1, contradicting nonhyperellipticity. Therefore every theta characteristic has h0≤1. Parity then gives

\[
h^0(S)=\begin{cases}0&\text{even},\\1&\text{odd}.\end{cases}
\]

This standard plane-quartic fact is also stated explicitly in [O]. The ordinary compact chiral Dirac kernel is accordingly zero or one, not three. By Serre duality h1(S)=h0(S), so its ordinary complex index is zero.

Four explicit odd theta characteristics are \(\mathcal O_X(2P_a)\), where Pa are the four branch points. Their unique spinor sections square to the hyperflex differentials

\[
\frac{dx}{y^3},\quad
\frac{x\,dx}{y^3},\quad
\frac{(x-1)dx}{y^3},\quad
\frac{(x-\lambda)dx}{y^3},
\]

each of which has a single zero of order four. Q8 permutes these four spin structures. The chosen based L,R lifts preserve one peripheral point and hence its hyperflex spin class; the exact 64-element enumeration shows there is no additional common fixed spin class.

### Independent analytic obstruction to a Q8-invariant spin structure

Suppose a compact theta characteristic were invariant under Q8. Lifts preserving its square-isomorphism to K would form a central extension of Q8 by fermion parity epsilon of order two.

Let I,J,Z lift i,j,z=-1. For signs a,b,c,

\[
I^2=Z\epsilon^a,\quad J^2=Z\epsilon^b,\quad
[I,J]=Z\epsilon^c.
\]

The first two equations force Z to commute with I and J. Thus the commutator is central. Since I² is central,

\[
1=[I^2,J]=[I,J]^2=Z^2.
\]

But z fixes a branch point and acts there on its tangent/cotangent line as -1. Its lift to a square root of K must have eigenvalue ±i, hence Z²=epsilon, not 1. Contradiction.

A separate calculation enumerates **all normalized Q8 2-cocycles over F2 by linear algebra**. There are 49 variables, cocycle rank 42, and dimension 7. Every cocycle forces f(z,z)=0. An eight-equation XOR certificate is included in the results. C2 provides a positive control: its order-four spin lift is allowed.

Scope: this forbids a single ordinary compact spin structure invariant under the deck Q8. It does not forbid the original rank-two gauge-twisted theory on the base, a theory summing spin structures, or a correctly defined combined spin-and-gauge construction. It is not an established four-dimensional anomaly.

---

## 6. A direct punctured rank-two Dolbeault calculation

The compact spin problem is not the same as the original gauge-twisted punctured problem. We therefore also calculate two explicitly specified algebraic extensions downstairs.

Let E-minus be the parabolic extension of the irreducible unitary quaternion representation on the punctured elliptic curve, with both puncture weights 1/2. The unitary/parabolic correspondence [MS] gives parabolic degree zero:

\[
0=\operatorname{pardeg}(E_-)=\deg(E_-)+\frac12+\frac12,
\quad \deg(E_-)=-1.
\]

Because the two weights are equal, parabolic stability implies ordinary stability here. Indeed a line subbundle has parabolic degree deg(line)+1/2<0, so its integer degree is at most -1, strictly less than the slope -1/2.

Define \(E_+=E_-(p)\). It is stable of rank two and degree +1. Tensoring either with any of the four degree-zero base spin line bundles preserves stability and degree.

A negative-degree stable bundle on an elliptic curve has no nonzero holomorphic sections. A positive-degree stable bundle has h1=0 by duality. Riemann–Roch has chi=degree. Consequently, for every base spin choice,

| specified extension | degree | h0 | h1 | Dolbeault index |
|---|---:|---:|---:|---:|
| E-minus | -1 | 0 | 1 | -1 |
| E-plus | +1 | 1 | 0 | +1 |

These are analytic kernel/cokernel counts for the specified Dolbeault extensions, not numerical Dirac eigenvalues. Which singular-Dirac self-adjoint/domain prescription is physical is not selected here.

All parity twists remain isomorphic, as proved in Run 1. Thus one selected E-plus problem supplies **one** holomorphic mode. Taking the three already labelled copies gives three modes, but that is the manuscript's direct sum, not a new derivation of why nature includes exactly those three copies.

More generally, E-minus(np) has degree 2n-1 and the corresponding algebraic h0/h1 counts follow immediately. This is not a classification of physically admissible puncture domains. In particular, selecting n=2 to obtain three sections is an additional end-data choice. It also retains the canonical subspace H0(E-minus(p)) of dimension one, so its unmodified pole-order-filtered family should not be equated to an irreducible three-dimensional target simply by counting sections.

---

## 7. Exact reduction of the metaplectic phase gap

The quaternion normalizer acts on imaginary quaternion axes by the rotations

\[
O_L=\begin{pmatrix}1&0&0\\0&0&-1\\0&1&0\end{pmatrix},\qquad
O_R=\begin{pmatrix}0&0&-1\\0&1&0\\1&0&0\end{pmatrix}.
\]

Their group has order 24. These are the adjoint rotations induced by \((1+i)/\sqrt2\) and \((1-j)/\sqrt2\). This three-dimensional representation is equivalent to Sym² of the determinant-one quaternion doublet.

Put

\[
O_S=O_RO_L^{-1}O_R,
\quad \zeta=e^{\pi i/4},
\quad D=\begin{pmatrix}-1&0&0\\0&0&-i\\0&1&0\end{pmatrix}.
\]

For the target multiplier in the ordered theta basis (2,3,4), direct matrix calculation gives

\[
\rho_{\Phi}(T)=\zeta\,D O_LD^{-1},
\qquad
\rho_{\Phi}(S)=\zeta^{-3}\,D O_SD^{-1}.
\]

But eta³ has precisely the scalar multiplier

\[
\chi_{\eta^3}(T)=\zeta,\qquad
\chi_{\eta^3}(S)=\zeta^{-3},
\]

with its weight-3/2 automorphy factor treated consistently. Therefore

\[
\boxed{\rho_\Phi=\chi_{\eta^3}\otimes O.}
\]

This is an exact representation factorization on the chosen metaplectic lifts. Both generators were checked, not merely their eigenvalues. The rotation image has order 24, whereas the scalar-twisted target has order 96 with scalar center {1,i,-1,-i}. Untwisted O(S)^4=+I; the target has rho(S)^4=-I. The scalar factor is indispensable.

Equivalently, as functions,

\[
\Phi/\eta^3=\eta^{18}(\theta_2^2,\theta_3^2,\theta_4^2)
\]

has weight ten and rotation multiplier O after the displayed basis change.

**What is and is not explained:** the cover supplies a natural doublet and quadratic parity sector, and the entire desired finite multiplier differs from its adjoint rotation action by a specifically identified one-dimensional character. This does not derive that character as the anomaly/holonomy of the actual puncture determinant. Nor does it derive the scalar functional amplitude eta18 in the last equation. Multiplying by eta³ or importing additional fields would reproduce the target by construction, not answer the quantum-origin question.

---

## 8. Next decisive calculation

The next calculation should be a determinant/Pfaffian-line and puncture-insertion calculation **for a specified faithful theory**, not another search for a matching finite group.

One concrete candidate is the family of parabolic Dolbeault operators just defined, with a fully stated physical boundary domain, metric and field content. Compute its determinant-line curvature, its central and S,T holonomies, and the zero-mode-saturating insertion maps. Separately track the degree-two theta-state bundle through the chosen correspondence; a fiberwise identification alone does not identify its connection.

Success at the representation stage requires the naturally computed scalar character to be chi_eta3 relative to the adjoint sector, without tensoring it in merely because it fits. Success for amplitudes additionally requires nonzero inserted blocks with consistent composition/sewing. A different character, remaining arbitrary flat-line twist, or unfixed boundary choice is a branch-specific failure or underdetermination.

The all-spin calculation shows why the covering method cannot simply assume an arbitrary compact spin structure descends equivariantly. The downstairs rank-two formulation supplies a way to state a consistent alternative rather than mistaking that obstruction for the failure of every quantum realization.

No gravitational completion has been attempted in this run. No gauge-chiral Standard Model spectrum or empirical parameter is claimed.

---

## 9. Reproduction, controls and integrity

Run:

```
python verify_cover_states.py
python verify_cover_states.py --reverse-tree
python verify_quantum_reduction.py --dps 80
python verify_quantum_reduction.py --dps 100
```

There are 30 named topology/spin checks and 22 named algebra/phase/numerical checks. This count is an inventory, not a confidence score. A test can pass by certifying a proposed interpretation fails.

Exact data include all chain matrices, intersection forms, spin permutations, orbit decompositions, and the central-extension certificate. Positive controls include the allowed C2 spin lift and the known theta translation/duplication identities. The untwisted normalizer's wrong central phase is an explicit negative control.

The alternate spanning tree is a basis-robustness check using the same algorithm, not a second independent implementation. Independence instead comes from the analytic local spin-lift proof and separate cocycle calculation, and from the algebraic curve/differential calculation versus graph topology. The parabolic h0/h1 counts are proved from stability, duality and Riemann–Roch; the code does not pretend to solve an infinite-dimensional Dirac spectral problem.

The working plan was locally hashed after initial source reading and exploratory reasoning and before executing these checks. It is not an externally timestamped preregistration. The theta-doublet identification and explicit phase factorization were developed during this run and should not be described as blind predictions. No code or result was silently imported from the project repository. A narrow GitHub search for 'Wollmilchsau' returned no indexed match; that is not proof the repository has never studied related geometry.

## References

[HS] F. Herrlich and G. Schmithüsen, *An extraordinary origami curve*, arXiv:math/0509195, especially Propositions 2, 3, 5 and 7. https://arxiv.org/abs/math/0509195

[MY] C. Matheus and J.-C. Yoccoz, *The action of the affine diffeomorphisms on the relative homology group of certain exceptionally symmetric origamis*, arXiv:0912.1425, Theorem 1.15 and §2. Known finite homology action; used as literature cross-check, not as an input matrix implementation. https://arxiv.org/abs/0912.1425

[A] M. F. Atiyah, *Riemann surfaces and spin structures*, Ann. Sci. ENS 4 (1971), 47–62. Quadratic refinements, parity and invariant-spin framework. https://www.numdam.org/item/10.24033/asens.1205.pdf

[O] G. Ottaviani, *Effective methods for plane quartics, their theta characteristics and the Scorza map*, arXiv:2403.19599. Plane quartic theta-characteristic section counts. https://arxiv.org/abs/2403.19599

[MS] V. B. Mehta and C. S. Seshadri, *Moduli of vector bundles on curves with parabolic structures*, Math. Ann. 248 (1980), 205–239. https://doi.org/10.1007/BF01420526  
For a research-paper restatement of the unitary/degree-zero stable-parabolic correspondence: C. Arusha and S. K. Singh, arXiv:2012.13543. https://arxiv.org/abs/2012.13543

[Y] J.-H. Yang, *Heisenberg Groups, Theta Functions and the Weil Representation*, arXiv:0905.1865. Background to the theta-state realization, not a uniqueness theorem for the physical interpretation. https://arxiv.org/abs/0905.1865

[DLMF] NIST Digital Library of Mathematical Functions, Chapter 20, especially §20.7. https://dlmf.nist.gov/20.7

No literature-novelty claim is made for the curve, theta identities or general quantum framework. The value of this run is the explicit reconstruction and scoped comparison with the stated weave target.
