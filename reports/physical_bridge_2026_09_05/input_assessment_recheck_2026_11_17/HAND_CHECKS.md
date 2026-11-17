# Hand checks of the new cross-form and joining claims

2026-11-17. PHYSICAL-C6. Source head
80fdd90b23abd93e89a9ed7614103b135f182c66. These are author hand
arguments awaiting independent review. No scientific source, CAS or
test was executed, imported or collected. The source implementations
and received outputs are pinned separately.

## 1. An exact pointwise proof of the cross-module's one-dimensional kernel

X-SYNTHESIS-2 lines 251–289 use numerical ranks at the origin and one
complex point to support uniqueness in the entire 25-dimensional cross
module. Those two computations retain their value as numerical controls.
A hand argument can supply the stronger parameter-wide statement under
the specified principal-module identification.

The natural five of Spin(5) is principal spin two. Equivalently it is
the nontrivial summand of wedge^2 of the principal spin-three-halves four.
Order its basis by weights 2,1,0,-1,-2. The principal raising operator
E has four nonzero entries c_i at (i,i+1). An adjoint operator T of
weight minus three can have entries only at (3,0) and (4,1), in zero-based
indices. Thus for every complex f, the submatrix of E+fT on rows
0,1,2,3 and columns 1,2,3,4 is upper triangular with determinant

    c_0 c_1 c_2 c_3 != 0.                              (1)

Its rank is at least four, independent of f. The operator lies in the
natural so(5,C) representation, so it is skew for a nondegenerate
symmetric form B. Taking determinants of Q^t=-B Q B^-1 in odd dimension
gives det Q=-det Q=0. Its rank is therefore exactly four and

    dim ker(E+fT)=1 for every f in C.                  (2)

For the two commuting Spin(5) factors the cross module is V_5 tensor
V_5. The invariant forms identify any dual factor with the corresponding
natural five. The two adjoint commutator actions act on its separate
tensor factors. Over C,

    ker(Q_+ tensor I) intersect ker(I tensor Q_-)
                         =ker Q_+ tensor ker Q_-.     (3)

Consequently the joint pointwise commutator kernel has dimension one
for every pair (f_+,f_-), including both axes and the origin. The
nonzero dressed vector displayed upstream spans that line once its
commutators are checked. Its highest-weight coefficient is b, so the
vector with b=1 remains nonzero for every f_+,f_-.

This gives a route to an exact classification beyond two sampled ranks.
It is a pointwise result within the specified 5 tensor 5 module.
A line bundle can carry more than one independent global form mode.
The two global cross-form coefficients, their complete domains, moment
response and physical interpretation retain their own duties. No global
mode is removed merely because the coefficient fibre has rank one.

## 2. The quotient normal derivative must carry the gauge connection

The source's lines 593–620 solve a real gauge projection for v_s and
then compute its second fundamental form using

    II_source=P_perp d v_s/ds.                         (4)

Here X_s is the raw affine representative. Equation (4) needs a
horizontal lift or the connection contribution from the moving frame.
The earlier physical proof used the quotient Levi-Civita derivative
P_perp nabla_s v_s. It did not replace that derivative by (4) in a
general nonhorizontal representative.

An elementary rejecting control makes the issue explicit. Give C^2
its real Euclidean metric and let U(1) act by simultaneous phase. The
curve X(s)=(1,s) has constant tangent v=(0,1). It is horizontal because
the real inner product with iX is zero. Its quotient acceleration and
II are zero. Change its representative to

    X_tilde(s)=exp(i beta s) X(s).

Gauss projection gives v_tilde=exp(i beta s)v and alpha_tilde=beta.
At s=0, the vertical space is spanned by (i,0), and the horizontal
curve tangent is (0,1). Both are orthogonal to (0,i). Therefore

    P_perp d v_tilde/ds at 0=beta (0,i),
    P_perp D_s v_tilde=0,
    D_s v_tilde=d v_tilde/ds-i alpha_tilde v_tilde.     (5)

The raw prescription changes under a frame change of the same quotient
curve. The covariant derivative gives the correct zero result in both
frames. This is a concrete mathematical failure of (4) as a general
quotient prescription.

### The missing contribution is nonzero in the source's actual planar example

The source's endpoints in lines 556–563 have a_x=a_y=0 and Hermitian
q,r in a common two-plane. Write theta=3/5, a=sin theta, b=cos theta,
and represent their Pauli coefficients by two real plane vectors

    q_s=2[(1-s)e_1+s(a e_1+b e_2)],
    r_s=(1-s)e_1-s(a e_1+b e_2).

Use J for a unit-speed common plane rotation, X=(q_s,r_s), t=dot X.
The plane metric is the common spin factor Omega times the Euclidean
metric. Set

    d=10-6a,
    D=|X|^2=5-d s(1-s),
    N=<JX,t>=3b,
    alpha=N/D,
    v=t-alpha JX.                                    (6)

The two other infinitesimal SO(3) rotations point out of the plane.
Thus projection of an in-plane vector onto the full SU(2) horizontal
space agrees with removal of JX. Jv is orthogonal to v. Direct inner
products give

    |v|^2=d-N^2/D,
    <X,v>=D'/2,
    |P_h Jv|^2=|v|^2-(D'/2)^2/D=16/D.                (7)

For this curve the actual quotient derivative has the additional
horizontal normal term

    II_true=II_source-alpha P_h Jv.                   (8)

The missing term's squared physical norm is

    Omega * 144 cos^2(theta)/D^3 > 0.                 (9)

Equations (6)–(9) use the effective plane angular velocity. The
normalization of the Pauli gauge generator is absorbed consistently
in that velocity. They apply on regular interior segments where q,r
are independent, which includes s=2/5 used by the source.

The reported precise value of II and the normal defect thus require
a corrected covariant evaluation. This does not establish that the
corrected normal defect vanishes, nor does it reject other stationary
paths. The finite model's energy minimization is a separate calculation.

### The optimizer also retains an untested Gauss duty

Lines 669–716 define both a link-eliminated energy and an energy with
a free end-holonomy angle. Their accompanying functions explain how
that angle restores the full longitudinal variation after gauge fixing.
The actual optimization at lines 768–807 uses energy_common_frame and
grad_common_frame, with fixed endpoints and no end-angle variable.
Its success predicate checks that restricted gradient.

Variation of the internal site orientation gives conservation of the
longitudinal current. Variation of the remaining holonomy or link gives
the Gauss equation fixing that current. These are separate equations.
The source neither optimizes the declared end-angle variable nor reports
the final link-Gauss residual. A small common-frame gradient alone leaves
that duty open. This observation does not assume that the omitted
residual is numerically nonzero on the returned solution.

A repair can use the actually link-eliminated energy or include the
remaining end angle in the optimizer, with its source boundary rule
declared. It should report Gauss and all field residuals together.

## 3. Eliminating one residual does not eliminate kinetic curvature

Lines 446–452 reuse the two-field comparator

    V(u,y)=b u^2(1-u)^2+[y-c u(1-u)]^2.

They call y=c u(1-u) a relaxed curve with zero normal residual and
assign a relaxed/straight tension ratio sqrt(b)/sqrt(b+c^2).
Along that curve the induced kinetic metric is

    K_curve(u)=1+c^2(1-2u)^2.                          (10)

Its restricted tension, if the first integral is attained, is

    2 sqrt(b) integral_0^1 u(1-u)
                              sqrt[1+c^2(1-2u)^2] du. (11)

The returned ratio omits (10). For c!=0 the integral factor is strictly
larger than integral u(1-u)du. In addition, partial_y V=0 on the
parabola while a full static extremal requires y''=0 there. A
nonconstant parabolic wall with y=0 at both asymptotic endpoints cannot
satisfy that equation. The kinetic normal curvature remains.

The source's later two-field positive-barrier numerical relaxation uses
a different potential and its full discrete gradient. It retains its
own finite-grid evidence. This correction concerns the analytic
parabolic control and its displayed tension ratio.

## 4. The two-cell lifting mechanism retains a physical joining datum

Lines 928–1006 define a finite 80-by-32 operator. Its two diagonal
blocks are D and D_2=diag(U,U) D U^dagger. The last row is
kappa(psi_1-psi_2), with a chosen U and kappa=1/2. Positivity gives

    ker M = ker D intersect U ker D                  (12)

for nonzero hopping, using the common coordinate identification.
This explains how the selected rotation can lift the remaining
finite-dimensional zero vector. It is a useful operator construction.

To check local frame covariance, retain the link map L and write the
last row as kappa(psi_1-L psi_2). If U is a pure change of the second
cell's frame, its transported link is L=U^dagger. With psi_2=U chi_2,
a unitary row transformation gives exactly the same-axis operator.
Its one surviving zero vector is preserved. The source instead fixes
L=I while changing D_2. That changes the relative operator/link data.

The lifted spectrum can therefore describe a physically different
join once that relative transport is supplied by an actual connection
and source law. The rotation, hopping and identification need that
derivation before being counted as a reduction of physical inputs.
The puncture-fibre matrix also retains the global Dolbeault/domain
map to the physical massless mode. A unitary scrambling of the assembled
matrix checks basis invariance of its singular values, while local
frame transport must carry its link as above.

## Evidence and next verification

The hand arguments preserve the full cross-module pointwise positive
and identify explicit rejecting controls for the normal derivative,
parabolic tension and link transport. They are reviewable author work.
The primary code sources were read at the pinned head. Scientific
execution and independent mathematical review remain pending.
