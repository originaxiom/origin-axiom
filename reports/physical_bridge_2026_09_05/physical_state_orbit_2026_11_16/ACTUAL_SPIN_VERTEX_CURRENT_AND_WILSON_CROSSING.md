# An interacting spin zero line in the same physical action

2026-11-16. P-C3b continuation. Author hand derivation, independent review
pending. No scientific producer, CAS, collection, integration or test ran.
The field/action/domain inputs and the kernel premises keep their stated
status. This note joins the preceding physical spin-mode inclusion to an
actual vertex and charge current. It does not compose its three different
background sectors into simultaneous local families.

## 1. Retain the parent and both opposite-charge left fields

The curved parent fixes the positive chiral kinetic densities
(1/2,Omega,Omega) for (a,u,v), the vector density Omega^2, and a common
overall coefficient 1/G, where G=g6^2>0. Its cubic is

    W3=(i/G) integral dxdy kappa(a,[u,v]).                 (1)

Use the coherent two-triple background and the two colour-singlet
half-root coefficients of Q_em charge +1 and -1. Put Q=Q_em and q=1.
Q commutes with the background and its core holonomy. Its unbroken
vector and connection harmonic mode are both retained. The coefficient
Wilson datum from the earlier construction acts trivially in this block.

In the balanced raising-field coordinates, write the gauge weight
vectors at the two algebraic middle extremes as X_+,Y_+ in charge +q,
and X_-,Y_- in charge -q. They have two-triple weights (-j,j),(j,-j),
respectively, with j=3/2. Choose the dual compact phases by

    Y_-=X_+^dagger, X_-=Y_+^dagger,
    kappa(X_+,Y_-)=kappa(Y_+,X_-)=k>0.                    (2)

The two weight vectors in a fixed charge have equal positive Hermitian
norm k. The equality follows either from the unitary Weyl element
interchanging the extremes or from the product of the two invariant
spin-j pairings. It uses their actual trace-dual opposite-charge spaces.

The direct zero-mode proof gives actual highest-vector phases
alpha_+=-1, alpha_-=+1 for the first coherent correction. For an extending
spin with equal a,b signs, the unique spin line in each charge has

    delta_+=eta(a) alpha_+, delta_-=eta(a) alpha_-.

Thus delta_-=-delta_+. In the aligned seed these are (+1,-1), and in
the odd seed they are (-1,+1). Reversing the coherent correction reverses
both deltas. Misaligned spin/state seeds have no such spin zero line.
These alternatives are kept throughout.

The two modes have both physical spin slots populated,

    u_+=s_+ X_+/sqrt(2), v_+=s_+ delta_+ Y_+/sqrt(2),
    u_-=s_- X_-/sqrt(2), v_-=s_- delta_- Y_-/sqrt(2).       (3)

s_+,s_- denote the actual scalar factors in the trivial compact
combined spin/gauge eigenlines. Their invariant product can be framed
as s_+s_-=omega, a nonzero holomorphic one-form on the compact elliptic
curve. In a translation coordinate omega=dz these factors are constant.
Globally this is the pairing through S^2=K, the flavour epsilon and the
gauge trace. It does not assert triviality of the original untwisted
spin line. The opposite-charge left fields in (3) remain independent.

## 2. Compute the actual polarized vertex, including its sign

Take the neutral connection mode a0=bar(omega) Q. The full field family
in (1) is a=A a0, (u,v)=t_+(u_+,v_+)+t_-(u_-,v_-). Invariance of kappa
and [Q,X_+]=q X_+, [Q,X_-]=-q X_- give

    kappa(Q,[u_+,v_-]+[u_-,v_+])
      = q k (delta_--delta_+) s_+s_-/2
      = -q k delta_+ s_+s_-.                            (4)

Both terms are needed. Keeping only one would miss a factor two. Adding
them with the same charge sign would incorrectly annihilate this vertex.
Equation (4) is nonzero because the actual two polarizations are opposite.

In coordinates omega=f(z)dz, define

    A_omega=integral |f|^2 dxdy,
    A_g=integral Omega^2 dxdy,
    I_omega=integral Omega |f| dxdy.

The coefficient of A t_+ t_- is therefore

    Y_raw=-i q k delta_+ A_omega/G.                      (5)

These are three distinct chiral coefficients. The usual one-half in
the Weyl Hessian pairs its two off-diagonal entries and introduces no
additional factor in (5). The determinant sign of the balanced flavour
coordinate change is a common phase of W and is carried consistently;
it does not change the magnitude or nonvanishing of (5).

Each charged profile in (3) has physical magnitude O(Omega^-1/2)
near the end. The neutral connection profile has magnitude O(Omega^-1).
They are bounded and decay in the complete cusp frame. Their graph
domain and nonlinear-product admission are the direct kernel proof's
ones. The cubic is absolutely integrable. No boundary vertex is supplied
to restore it. The source boundary primitive is quadratic in q,r and
has no a-dependent contribution to (1).

## 3. Normalize the vertex and its actual gauge current together

Set h_Q=kappa(Q,Q)>0. Choose the scalar frame constants by

    |s_+|^2=c_+ |f|, |s_-|^2=c_- |f|,
    c_+,c_->0, c_+ c_-=1.

The full mixed-slot norm of each mode, including its two factors
1/sqrt(2), gives

    Z_+=k c_+ I_omega/G, Z_-=k c_- I_omega/G,
    Z_a=h_Q A_omega/(2G), Z_Q=h_Q A_g/G.                 (6)

Z_Q is the coefficient of -F_Q^2/4 in the same vector convention as
the source parent and earlier normalized Wilson-crossing calculation.
The covariant derivative gives charge insertion +q Z_+ and -q Z_-
on the two modes. After rescaling both the matter fields and the vector,

    e_Q=|q|/sqrt(Z_Q),
    |y|=|Y_raw|/sqrt(Z_a Z_+ Z_-),
    |y|^2/e_Q^2=2 A_omega A_g/I_omega^2.                 (7)

The mode phases, root pairing, trace normalization, frame constants and
common G cancel in the last ratio. Its shape dependence belongs to the
retained metric. Cauchy-Schwarz gives I_omega^2<=A_omega A_g and hence
|y|/e_Q>=sqrt(2). Equality would require Omega proportional to |f|
almost everywhere. The complete hyperbolic cusp violates that condition,
so the inequality is strict here. This reuses the earlier normalization
law on newly constructed, actual two-triple spin modes. It is a tree-level
relation in the supplied parent, with no comparison to a measured SM value.

The odd seed and both coherent signs give the same magnitude. The
interaction therefore does not select the aligned state over the odd
alternative. Its holomorphic sign alone can be changed by a mode phase.

## 4. Recover (5) from the same operator and retain the form partners

For a connection variation a0, the two physical spin rows of M vary by

    delta M_u=-i[a0,v]/Omega,
    delta M_v=+i[a0,u]/Omega.                            (8)

Pairing (8) with the trace-dual opposite-charge left mode carries the
target kinetic density Omega. The resulting bilinear is

    integral {-i kappa(u_-,[a0,v_+])
                   +i kappa(v_-,[a0,u_+])}
      =i integral kappa(a0,[u_-,v_+]+[u_+,v_-]).          (9)

Equations (4)-(5) follow, including the common factor 1/G. The gaugino
row has no additional a0-dependent term on a pure-spin input. This
compares the physical operator derivative with the actual superpotential.

Each charge also has two pure-form zero modes and no pure gaugino
mode. They are retained. Equation (1) with a0 and two pure-form inputs
vanishes. The first-order neutral connection deformation consequently
has rank one between the spin lines and zero on their form partners.
The full charged reduced mass still needs the actual complementary
inverse at higher orders. The companion parallel-background proof
provides its fixed-surface existence and domain on this charged block,
subject to that proof's pending review. It supplies no inverse on the
entire parent neutral continuum.

There is an exact count control near this crossing. Adding the flat
Q connection a0 preserves [Q,q0]=[Q,r0]=0, the vacuum equations, the
parallel algebraic differential and the peripheral holonomy. It twists
the two compact middle eigenlines by the actual unitary Q character.
At the seed one eigenline is trivial and the other has signs (-1,-1).
A sufficiently small nontrivial Q character makes both nontrivial in
each charge. Their compact degree-zero holomorphic sections disappear.
The form line still has its degree-two puncture allowance, hence its
two sections in either charge. Thus in this specified nearby family
the spin pair lifts and the two form modes per charge remain. This is
consistent with (9) and preserves the vector-like net index.

## 5. Transport the coupled observable over the state orbit

For every aligned state-axis representative, flavour SU2 preserves
epsilon and the gauge coefficient Q. Transporting (2)-(3) with the
actual field maps gives the same cellwise tensor and metric. In coherent
representative frames the finite spin-line action in both charges is
R_e=sigma(g_e) O_(g_e). It is real orthogonal. Their bilinear contraction
is therefore invariant, while the full raw maps remain

    t_+ -> j_e R_e t_+, t_- -> j_e R_e t_-,
    A -> bar(d_e) A, d_e=j_e^2.

These are maps of the three different background sectors. The formal
cellwise tensor is proportional to A sum_p t_(+,p) t_(-,p). This states
the comparison of the three vertices. It introduces no inter-sector
local interaction or simultaneous-generation matter content.

With the marked elliptic coordinate and its omega=dz basis,
A_omega transforms by |d_e|^-2, I_omega by |d_e|^-1, and A_g is
invariant. The product of the three raw coefficient factors is
bar(d_e) j_e^2=|d_e|^2. It cancels the transformation of (5). The
finite R_e factors cancel by its bilinear transpose. In canonically
normalized variables the scalar phases multiply to

    (bar(d_e)/|d_e|) (j_e/|j_e|)^2=1.

The full interaction and current transport therefore retain the
previous proof's scalar line and central sheet. Replacing either
spin module by the native triplet alone would lose these factors.

## 6. What is earned at author-proof level

The invariant physical spin line now has an explicit nonzero same-action
coupling, a normalized charge current and a controlled Wilson-crossing
mass rank. The interaction was obtained by projecting existing fields
and brackets. No independent Yukawa tensor was assigned.

The construction retains both charges, the two form partners per charge,
the other gauge sectors and the neutral continuum. The complete parent
has the earlier U3 phase here. A charged colour-singlet interacting pair
and a three-state operator orbit do not establish three chiral SM families.
The odd state gives the same coupling magnitude. The composition of
background sectors and their physical selection keep their own duties.

The supplied parent, embedding, spin/flavour and holonomy data, internal
geometry, registering lift and action normalization remain explicit.
No foundational input reduction or gravity result is counted. Independent
review must check (2), both terms in (4), the global product line, every
normalization in (6), the trace-dual variation (9), the complete-domain
perturbation and the full-E scalar cancellation. No earlier finite package
or received numerical result verifies this successor.
