# The B family changes the vector operator and retains the charged kernel

2026-11-18. P-C3h analytical scope d5f40bff7. Author hand derivation,
**not independently checked**. No science imports, execution, CAS,
numerical evaluation or tests. This is the supplied fixed-metric
classical E8 construction, not a foundational derivation of it.

Fix the coherent h4 bundle, eta=O, chi=0 and the small stationary
family X(b) of P-C3g, with b in the two neutral D5 cross-form modes.
Its existence and the source complete-domain/Hodge proofs remain
conditional. Both conjugate LEFT sectors, original kinetic metrics,
massive fields and threshold continua are retained throughout.

## 1. First separate the previous results

The November 8 up-sector proof already gives three charged coefficients
in this coherent bundle, with a two-form plus one-spin decomposition.
That number is reused. The November 16 cyclic-family calculation uses
nonzero spin deformations and, with its retained order-three Wilson,
changes its charged counts. It is another family, not a contradiction.

P-C3g has instead a pure connection tangent on D5's highest (2,2) line.
It derives a nonzero first vector response on a proposed stationary
colour/EM-preserving family. The question here is the complete charged
fermion kernel on that SAME family. Its projected singlet cubic zero
does not decide the question; the full complex must be carried.

## 2. Transfer the actual connection perturbation exactly

Use the actual tensor complex and metrics of
PARALLEL_BACKGROUND_ORTHOGONAL_REDUCTION.md. Its bidegrees are

    C^(k,l)=A^(0,l)(E tensor wedge^k(S tensor F)),
    k=0,1,2; l=0,1; total degree k+l.

Write its reference differential as d0=bar(partial)+delta_signed.
The physical maps and degreewise isometries in that proof give
J_(n+1) D_n=sqrt(2) d_n J_n and the corresponding actual four-slot
fermion/Hodge map. These constants and adjoint target are not changed.

At the reference point delta is parallel. Let P be the global
orthogonal projection on ker Delta_delta, i its inclusion, p its
projection, and let h be the algebraic contraction

    h|_(k,l)=(-1)^l delta† (Delta_delta|_(1-P))^-1.

The inverse is zero on P. Parallelness, metric compatibility and the
actual flat gluing make these global bounded tensor maps. The pointwise
positive algebraic gap is fixed at this reference point. On the total
complex, including its signs,

    d0 h+h d0=1-i p,  h²=0, p h=h i=0.               (1)

The complete-domain version is the source's orthogonal reduction.
Here h preserves Dolbeault degree l and lowers Koszul degree k.

The raw family changes only its (0,1) connection. Let V_b be that
change in the tensor Dolbeault differential, with its actual factor
-i ad_b/2 and dbar(z) wedge. It preserves k and raises l by one.
Since [b,q0]=[b,r0]=0, the raw family is exactly F-flat, so

    (d0+V_b)²=0.

There is only one antiholomorphic form direction on this surface.
Consequently

    V_b h V_b=0, (h V_b)²=(V_b h)²=0.                (2)

These are form-degree identities, not a truncation based on a small
numerical coefficient. The perturbed contraction therefore terminates:

    i_b=i-h V_b i, p_b=p-p V_b h, h_b=h-h V_b h,
    d_ret=bar(partial)|_P+p V_b i.                   (3)

There are no higher transferred powers of b. One can check (3) from
(1)-(2), or use the homological perturbation lemma with its homotopy
sign reversed. It does NOT replace the fermion operator by a fibre
matrix: the retained differential is still the global Dolbeault
operator on its actual bundles.

The relevant standard lemma was personally read in Crainic's v1,
sections 2 and 3.1-3.6, including its proof. Its homotopy convention
is ip=1+dh+hd; ours is (1). The bounded physical-domain application
is the argument here, not a theorem attributed to that paper.
[Primary paper](https://arxiv.org/pdf/math/0403266)

## 3. No physical domain or adjoint is discarded

The source B profile satisfies |b|_gauge/Omega=O(rho log(1/rho)^3)
at its largest allowed puncture pole, with the same decay after a
fixed number of physical derivatives up to logarithmic powers.
Thus V_b, h V_b and V_b h are bounded between the actual tensor
Hilbert slots. Their smooth coefficients preserve compact-support
cores. The chain identities give graph bounds directly: for example
d_b i_b=i_b d_ret and d_b h_b=1-i_b p_b-h_b d_b.
Approximating in those cores extends (1)-(3) to the same complete
closed differential domains. No inverse of a decaying mode is used.

The source charged half-root sector has a confining tail. The up
sector's retained powers are -2,3,-1,4, away from its critical power
one. Their actual endpoint estimates and physical Hodge identification
remain the source review premises. A bounded decaying b is graph-
compact on these charged Dirac blocks: compact-core ellipticity gives
Rellich compactness and its tail supremum tends to zero. Their
Fredholm/Hodge interpretation persists, with no invented cap.

The stationary representative is the bounded Hermitian complex-gauge
response g(b)=exp[-psi(b)] of P-C3g. It and its inverse and first
derivatives are bounded; it intertwines the raw holomorphic complex
and its responded one, on the stated complete domains. The physical
adjoint is then taken in the ORIGINAL positive metric, and includes
b† and all spin-response terms. This transports cohomology dimensions,
not massive singular values, unchanged wavefunctions or unitary norms.
Physical harmonic representatives and current overlaps must be solved
and normalized at the responded background.

## 4. The entire 128 block has zero transferred B action

On each actual Spin10 half-spinor the two principal spinors are
V_(3/2) tensor V_(3/2). The highest D5 cross generator acts as a
fixed nonzero multiple of X tensor X, with X=e13+e24 in the ordered
four. Equivalently X is proportional to the square of its principal
raising matrix. The two equal entries are required by its highest-
weight equation, as in P-C3g.

The reference fibre harmonic representatives are

    k=0: |j,j>,
    k=1: e_+|-j,j>, e_-|j,-j>,
    k=2: e_+ wedge e_-|-j,-j>, j=3/2.

X tensor X annihilates the first three representatives. It sends
the last gauge vector to |1/2,1/2>, orthogonal to the retained
lowest vector at k=2. Thus, in every complementary coefficient,

    p V_b i=0.                                      (4)

Equations (2)-(4) give exactly the OLD retained Dolbeault complex,
not just a first-order zero in its finite cohomology. This holds in
both half-spinors, on all colour and charge coefficients. The old
two form modes and the spin mode allowed by its actual compact flat
character persist as physical kernel dimensions. No extra field is
hidden in the contractible complement. The four-slot adjoint kernel
is retained by the same Hodge argument.

At the present chi=0, eta=O point the old coherent formula gives
three per coefficient in 1_(+1)+3_(-1/3) and its conjugate: 24
independent left Weyl coefficients in the whole 128 block. The old
18 at nontrivial order-three Wilson is not copied to chi=0. The
new result is persistence along the B family, not a new origin count.

## 5. The vector-ten middle coupling needs the actual bilinear form

For (10,6) the D5 gauge vector splits as V2 plus V2. Write its
normalized highest/lowest vectors x_+,x_- and y_+,y_- in the two
five-spaces. The positive Hermitian form is the source one.

The COMPLEX SYMMETRIC bilinear form is also needed. In the original
B plus B-dual ten-frame it is [[0,I5],[I5,0]]. The source unitary
frame change diag(I5,J5), followed by the real Hadamard change of
the two five-spaces, takes that form to

    diag(J5,-J5), J5=anti-diag(1,-1,1,-1,1).          (5)

It follows directly by transforming the form with the inverse
transpose; it is not permissible to replace it by diag(J5,J5).
In particular the two highest/lowest pairings have opposite signs.
The source reflection has phase i when exchanging either highest
five-vector, and phase i on the two lowest as well. It preserves
(5). A same-sign replacement would already fail that control.

The cross generator Z_B=x_+ wedge y_+, with an inherited fixed
normalization, therefore sends x_- to -y_+ and y_- to -x_+, up
to a common nonzero scalar. Its two relevant entries have the SAME
sign. An antisymmetric two-entry shortcut would have the wrong
core character for this source frame.

Use the reference middle planes in the up proof:

    L=S^3 V3:  e_+ x_-, e_- y_-,
    H=S^-1 V_-1: e_- x_+, e_+ y_+.

The retained p V_b i maps L to (0,1) forms valued in H, with
coefficient proportional to b times sigma_x in these frames.
It annihilates H. Its action on the retained extreme k=0 and k=2
planes is zero after projection. Hence the sole new reduced
operator is a TRIANGULAR Dolbeault extension from L to H.

The literal flat matrices check its typing: A_L=A_H=i A0,
D_L=diag(-i,+i), D_H=diag(+i,-i), with A0 exchanging the two
coordinates. sigma_x intertwines A and reverses those D signs,
as required for the highest B line of core character +1.

## 6. The global up-mass map cancels, not just its gauge coefficient

The up charges are +2/3 and -2/3, with independent LEFT fields.
In the SAME source weight frames the h4 electromagnetic phase is
+i and -i respectively. The bare D5 matrix is the same. Thus

    A0,-=-A0,+,  D3,-=D3,+.

T=diag(1,-1) anticommutes with their off-diagonal A0 and commutes
with D3. It is a global linear unitary intertwiner of the two
S^3 V3 bundles, including their half-power extensions, spin factor
and complete norms. Their actual H0 spaces each have dimension one.
After one common normalization and constant phase, if the positive
charge spin section is (f,g), the negative one is (f,-g).
This is not a reality identification of their independent fields.

Take the polarized source cubic W3=(i/G) integral kappa(b,[u,v]).
For one conjugate colour pair the relevant components are

    u_+=f x_- tensor c_+, v_+=g y_- tensor c_+,
    u_-=f x_- tensor c_-, v_-=-g y_- tensor c_-.

The actual (10,6) bracket contracts c_+,c_- with the symmetric
orthogonal-six pairing. Its D5 coefficient for [x_- c_+,y_- c_-]
is therefore the SAME as for [x_- c_-,y_- c_+]. Both are nonzero
fixed multiples of x_- wedge y_-. Polarization gives

    kappa(Z_B,[u_+,v_-]+[u_-,v_+])
                     =C(-f g+f g)=0                 (6)

pointwise, with the actual invariant trace and flavour epsilon.
Colour pairs with unequal components have zero colour contraction.
No global integral is presumed generically nonzero or zero.

This is the one-dimensional connecting map from H0(L) to H1(H).
The actual complete dual pairing identifies H1(H) with the dual of
the opposite-charge H0(L); these noncritical endpoint spaces both
have dimension one by the up proof. Equation (6) therefore proves
that entire connecting map is zero for EVERY allowed B profile.

There is an explicit retained spin solution as well. Let phi be the
old low-plane holomorphic section, and let bar(partial)_H^+ be the
actual bounded inverse onto the range of the high-plane Dolbeault
operator. H has no H0 kernel and a one-dimensional H1 cokernel.
Equation (6) puts V_b phi in its range. Then

    (phi, -bar(partial)_H^+ V_b phi)                 (6a)

is an exact zero-degree cocycle of the triangular middle system.
There is no further return term. Its inverse and norms are the
source's noncritical complete ones, not division by a vanishing
section or a chosen boundary value. The moment response and physical
Hodge normalization are still carried as in section 3.

Using the same (f,g) for the two charges would instead give 2C f g
and a false prospective mass. It violates the literal core phases.
The T sign, the symmetric gauge pairing and the antisymmetric flavour
pairing have to travel together. This resolves the specific cancellation
question left open in the November 8 native-field notes.

## 7. Why this is an all-orders kernel statement on the pure B family

In the reduced k=1 system the diagonal operators are the old
Dolbeault maps on L and H, and the only off-diagonal map is t B
from L to (0,1)H along a real ray. There is no reverse arrow and no
second Dolbeault degree. The exact sequence of this triangular
extension has connecting map t times (6), identically zero.
It therefore retains both its degree-zero and degree-one cohomology
dimensions. In particular its middle H0 contribution stays one;
the extreme k=0 Dolbeault H1 still supplies two. H0 and H3 of the
whole up complex stay zero, and H2 stays three. Thus

    (dim H0,dim H1,dim H2,dim H3)=(0,3,3,0)          (7)

in each conjugate up representation, throughout the small stationary
B family. This does not infer all-orders persistence merely from a
vanishing first-order mass. It uses the EXACT reduction (2)-(3) and
the one-way extension; there is no higher return path to discard.

The long-exact-sequence argument is for the inherited complete
complexes. The endpoints have the source closed-range estimates;
the off-diagonal bounded decaying map preserves their domains and
their compact-extension resolutions. The bounded contractions and
Hermitian response then transfer (7) to the physical Hodge map as
in section 3. These analytic premises require independent checking.

## 8. Complete charged result and its remaining physical price

For every sufficiently small stationary B for which the source
construction holds, the reused origin roster therefore persists:

| Surviving colour/EM representation | Left multiplicity |
|---|---:|
| 3_(+2/3), conjugate3_(-2/3) | 3 each |
| 3_(-1/3), conjugate3_(+1/3) | 3 each |
| 1_(+1), 1_(-1) | 3 each |

There are 42 independent left Weyl coefficients in these rows,
including every conjugate and colour dimension. The A3 directions
of charge +/-4/3 commute with D5. Their WHOLE physical operator is
unchanged by b and by its D5 Hermitian response. Their existing
zero-kernel proof is retained with the actual h4 core character,
not replaced by a Fredholm argument at their threshold.

Those extra charged directions retain their spin threshold continuum,
as do the unbroken centralizer directions. It would be wrong to call
42 the complete low-energy spectrum or to say the only surviving
continua are neutral. Massive partners, scalar/gaugino fields and
interactions remain in the supplied supersymmetric parent as well.
The neutral D5 kernel and its critical channels have not been counted
on this nonparallel family by the present charged calculation.

Together with P-C3g, this supplies a proposed SAME-CONSTRUCTION join:
a stationary colour/EM-preserving deformation can split the old
vector pole while retaining the charged three-coefficient roster.
The normalized left/right current analysis near the origin still
keeps both currents. Physical weak closure, three chiral families,
a viable complete spectrum and vacuum selection are not obtained.

The family has zero classical internal residual potential; its
availability or the unique first-response coupling direction does
not select a nonzero amplitude. The fundamental parent, carrier,
metric, spin/flavour map, lift, reference and states remain priced.
No foundational input reduction, observed parameter or gravity result
is claimed. The new proofs and complete-domain steps remain authored
and need non-authoring scrutiny before any admission or banking.
