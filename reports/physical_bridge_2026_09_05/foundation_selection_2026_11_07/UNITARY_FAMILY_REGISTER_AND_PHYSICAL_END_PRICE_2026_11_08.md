# A unitary family can retain word order: the boundary price stays visible

2026-11-08. Authored analytical successor, **UNREVIEWED**. No scientific
module has been imported, collected or run for this note. The seven
controls sealed at `7e0159033` are unchanged and do not verify this new
argument. This is a conditional construction, not a foundational input
payment or a physical SM result.

## 1. Reuse before extension

The [first-order law](FIRST_ORDER_REGISTER_LAW_AND_MATTER_PRICE_2026_11_08.md)
already derives the adjoint deformation module for varying matrices. It
also distinguishes a covariant family from one common Nielsen-fixed
character. The [joint first-order register](JOINT_FIRST_ORDER_REGISTER_AND_OLD_QUATERNION_COVER_2026_11_08.md)
already identifies the information lost by `F/[N,N]`, where
`F=F(a,b)` and `N=ker rho` at the quaternion point. The
[higher-response proof](LARGER_REGISTER_ARCHITECTURE_AND_SECOND_ORDER_LAW_2026_11_08.md)
recovers that order by noncommutative responses. None of those facts is
being rediscovered here.

Two old physical positives must also be retained. The
[full E8 lift](../word_architecture_audit_2026_10_17/FULL_E8_COMPENSATOR_LIFT_AND_REGISTER_TRANSPORT.md)
already detects `a^4` on its 128 coefficients through `K(a^4)=Zeta`.
The [geometric join](../word_architecture_audit_2026_10_17/GEOMETRIC_SPIN_JOIN_AND_FULL_CURVE_OPERATOR.md)
retains based data beyond a finite coefficient image. It would therefore
be false to say that every field of the existing model kills `a^4`.

The new question is narrower: can the lost ordered response occur in
positive-norm unitary holonomies without adding a separate affine
doublet, and can such holonomies be varied inside the same physical end?

## 2. Explicit unitary recovery of the first lost order

Use anti-Hermitian quaternion matrices

    A^2=B^2=C^2=-I,  AB=C=-BA.

The two independently variable generator assignments

    A_e=exp(e A) A,  B_d=exp(d B) B

give actual representations `K_(e,d):F->SU2`, since F has no relators.
They preserve the ordinary positive Hermitian metric exactly. Here e,d
are coordinates on an allowed candidate family, not derived constants or
physical couplings. In particular

    K_(e,d)(a^4)=exp(4e A),
    K_(e,d)(b^4)=exp(4d B).

For `w=[a^4,b^4]` with `[x,y]=xyx^-1y^-1`, multiplication to second
total degree gives

    K_(e,d)(w)=I+16 e d [A,B]+O_3
              =I+32 e d C+O_3.                         (1)

The mixed term follows from ordinary unitary matrix multiplication;
it is not an independent coefficient fitted to the ordered register.
Thus a word killed by every joint Q8 first-order cocycle is visible in
the second jet of a family of unitary two-dimensional representations.
This does not equate that jet with the entire nine-generator relative
augmentation algebra. A particular response can detect this witness
while missing other words or other response directions.

The gauge-invariant closed-loop trace has a different leading order.
For orthogonal quaternion axes direct multiplication gives

    tr K_(e,d)(w)=2-4 sin^2(4e) sin^2(4d)
                =2-1024 e^2 d^2+O_6.                 (2)

It detects noncommutativity by comparison with the identity, but not at
second order. Moreover `tr K(a^4 b^4)=tr K(b^4 a^4)` for EVERY K: the
two words are conjugate. Distinguishing those two based words requires
the reference/framing information retained in the larger register.
Confusing (1), (2), and two equal product traces would manufacture a
physical observable that has not been defined.

## 3. This can be a full unitary register, not just a finite jet

Conditionally choose the whole based representation space

    X=Hom(F,SU2)=SU2 x SU2.

This compact target/category is still an input; it is not forced by
the act-and-register premise. The word assignments on X retain every
nonidentity free word. An external theorem supplies a stronger fact:
almost every pair in a compact semisimple group freely generates a free
subgroup, in both the Baire and Haar senses. For SU2 this gives faithful
pairs arbitrarily close to the quaternion pair. This is an application
of Breuillard--Green--Guralnick--Tao, Theorem 5.1, not a new OA theorem:
[primary paper](https://www.imo.universite-paris-saclay.fr/~emmanuel.breuillard/densepaper.pdf).
I personally read the introductory statements and Section 5's theorem
and proof; I do not claim to have independently reproved the entire paper.

One explicit positive-norm representation of the existing full joint
group can use these same two-dimensional fibres. Retain the previously
defined group

    E={(phi,g): rho composed phi=Ad_g rho},
    S=F semidirect E,

where the existing rho is the quaternion anchor and g is its specified
SU2 intertwiner. Define the left action on X by

    t_e(K)=g (K composed phi^-1) g^-1.                 (3)

It fixes the anchor rho. The use of g in both the base and fibre is
essential. Let m be product normalized Haar measure on X and put

    H=L2(X,m;C2),
    (M_h f)(K)=K(h) f(K),
    (U_e f)(K)=g f(g^-1 (K composed phi) g).           (4)

Nielsen generator changes preserve product Haar: for instance
`(A,B)->(A,AB)` is a Haar-preserving translation of the second factor
at each fixed A. Swaps and inverses preserve it too; these generate
the free-group automorphisms. Constant conjugation by g also preserves
it. Thus (4) is unitary, with

    U_e U_f=U_(ef),
    U_e M_h U_e^-1=M_(phi(h)).

Consequently `(h,e)->M_h U_e` is a representation of S with its actual
semidirect product law. Its fibres have dimension two; H is nevertheless
infinite-dimensional. No finite particle roster follows from this.

Here is a faithfulness check, including the lift sign. If `M_h U_e=I`,
commuting it with multiplication by every continuous scalar function
forces `t_e=identity` almost everywhere, hence everywhere by continuity
and full support of m. Therefore

    K(phi(w))=g K(w) g^-1       for every K,w.          (5)

Linearize (5) at the trivial representation, first allowing only a to
vary as `exp(tX)` and then only b. If the abelianization of phi is
`[[p,q],[r,s]]`, the equations force q=r=0 and
`Ad_g X=pX=sX` for every `X in su2`. An adjoint rotation in SO3 can be
a scalar only with scalar +1; hence p=s=1 and g is central. Equation
(5), together with the separating unitary word assignments, then gives
phi=id. The remaining equation is `K(h)g=I` for all K. At the trivial
representation it gives g=I, and separation gives h=1. The nontrivial
lift epsilon=(id,-I) acts as `-I` on H and is retained.

This is a second constructive completion of the full group, alongside
the earlier regular representation. It establishes compatibility of
faithful word registration, lift retention and a positive unitary norm.
It neither identifies H with a physical Hilbert space nor derives a
Hamiltonian, measuring apparatus or probabilities for physical events.

## 4. Kinematic covariance leaves a real state-selection duty

Write `kappa(K)=tr K([a,b])`. It is unchanged by oriented marking moves
and simultaneous conjugation. This is the familiar peripheral trace of
the punctured-torus character variety, not a new invariant. See
Forni--Goldman--Lawton--Matheus, Section 2.2 and the discussion of its
level sets in Section 4:
[primary paper](https://www.math.umd.edu/~wmg/AHL_2024__7__1099_0.pdf).
My use is of these character-variety statements, not their full KAM
analysis or its computational certificates.

Haar supplies one natural normalized kinematic norm after SU2 and the
full product family have been chosen. It is NOT selected by E covariance
alone. For every bounded strictly positive nonconstant function f on
[-2,2], the probability measure

    dm_f = f(kappa) dm / integral_X f(kappa) dm          (6)

is E-invariant as well. These weights can change the distribution of
peripheral trace while keeping the same allowed family, word transport
and positive norm. There are also invariant anchor atoms, since (3)
fixes rho. Even full support plus covariance does not exclude mixtures
of Haar and an anchor atom.

This reuses Gate 11's distinction between a kinematic invariant measure
and a physical history law. It sharpens that distinction on the actual
SU2 coefficient family. The registering principle needs further earned
dynamics or state/end information to prefer (6), a relative trace leaf,
or an anchor. Calling all allowed pairs physically realized would not
fix their weights or their interactions.

## 5. Fixing the old quaternion cusp excludes this deformation

For general unit quaternions

    A'=cos(alpha) I+sin(alpha) u,
    B'=cos(beta) I+sin(beta) v,

with u,v unit imaginary quaternions, elementary quaternion multiplication
gives

    tr[A',B']=2-4 sin^2(alpha) sin^2(beta)
                      * (1-(u dot v)^2).              (7)

The minimum -2 requires both scalar parts to vanish and the axes to be
orthogonal. Such pairs are conjugate to the quaternion pair. Thus the
fixed peripheral trace -2 leaf is a single SU2 character; it does not
contain nearby faithful free representations. In SU2, trace -2 means
the peripheral holonomy itself is -I.

In the explicit family of Section 2 the actual peripheral trace is

    kappa(e,d)=2-4 cos^2(e) cos^2(d)
              =-2+4(e^2+d^2)+O_4.                   (8)

So the recovery in (1) changes the old cusp sector, even though (8)
has zero first derivative at the anchor. The actual peripheral MATRIX
has a linear change:

    [A_e,B_d]=-I-2e A+2d B+O_2.                      (9)

At d=0 this is exactly `-exp(2e A)`. Testing only the derivative of its
trace would miss that boundary change. This is a specific control
against calling an ambient unitary deformation an admitted variation
with fixed end data. The earlier common-fixed-character restriction
remains intact; the covariant family deliberately allows more states.

## 6. The existing positive action does not make every such change a mode

The old [curved-action proof](../weave_curved_action_2026_10_08/PROOF.md)
already admits flat connections with q=r=0 as stationary backgrounds
and explicitly leaves their moduli unresolved. With a chosen compact
gauge embedding, a free-group unitary holonomy pair can define such a
flat bundle. This reuses the supplied action and embedding. It does not
derive their choice, preserve a nonzero old condensate, or prove its
SM gauge symmetry and fermion roster persist.

There is a further end test even at that flat origin. On its fixed
complete cusp use x of period one, y>=Y and

    ds^2=ell^2 (dx^2+dy^2)/y^2.

The connection kinetic metric is conformally invariant in these two
internal dimensions. A variation of a constant peripheral logarithm,
`delta A=delta H dx`, has

    ||delta A||^2 = const * kappa_pos(delta H^2)
                          integral_Y^infinity dy.     (10)

It diverges if delta H is nonzero. For the path d=0 in (9), choose the
constant-axis cusp representative with logarithm `(pi+2e)` along that
axis. Its infinitesimal change is nonzero, so (10) applies.

This is not just a poor choice of gauge at the central anchor. Holonomy
variation satisfies the usual integral parallel-transport formula;
unitarity and Cauchy--Schwarz bound its squared norm by a constant times
`integral_0^1 |delta A_x|^2 dx` on each horocycle. For flat linearized
variations about peripheral -I, its norm is constant along the cusp.
Gauge variations change peripheral holonomy by a commutator with -I,
which vanishes. A nonzero first derivative as in (9) therefore gives a
positive lower bound on every horocycle, and the integral over y still
diverges. No finite-norm gauge compensation removes this obstruction.

The scope is infinitesimal flat unitary variations changing this
peripheral holonomy, at this central anchor, in this fixed complete-end
kinetic metric. It is not an exclusion of different finite-width or
dynamical end laws, source fields, compact carriers, nonflat solutions,
other peripheral sectors, or changes whose holonomy derivative is zero.
In particular the existing nonflat stationary construction has its own
full gauge/spin/flavour bundle and cannot be classified by (10) alone.

## 7. What has been gained and the next discriminator

The lost word order is not evidence that a positive unitary realization
is impossible or that the doublet fibre must be replaced by unipotent
physical fields. A whole unitary family can recover it and can retain
the full lifted group coherently. The elementary witness and the
infinite-dimensional construction exhibit that possibility explicitly.

The independent physical prices are now more specific: derive why the
compact representation family is physically relevant; distinguish
variation among boundary sectors from finite-norm fields in one sector;
and derive the common action, admissible end response and relational
observables that couple these sectors. A bare Haar integral or a second
jet is not that coupling law. The existing E8 lift and full based geometry
must stay in the comparison, rather than be replaced by a Q8-only test.

A future verification successor should compare (1), (2), (8) and (9)
with independent exact quaternion arithmetic; reject the false quadratic
trace signal and the zero-trace-derivative boundary test; and verify
(3)--(5) with the actual multiplication convention. It must be separately
designed, sealed, reviewed and admitted. It is outside the seven current
unrun controls. No claim of a physical input reduction is banked here.
