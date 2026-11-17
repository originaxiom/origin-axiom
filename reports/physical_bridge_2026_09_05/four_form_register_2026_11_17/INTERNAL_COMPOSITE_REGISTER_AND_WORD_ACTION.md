# A lossless internal composite and the native word-action test

2026-11-17. PHYSICAL-C7 continuation under scope commits 0d1834b9c
and 9f07f3096. Author hand derivation, not independently checked.
No scientific script, symbolic evaluator or test ran. This uses the
same four physical form coefficients, source metric and declared
coefficient-to-SU2 frames as the preceding C7 proofs.

The failed direct pair map does not establish that a new physical
reference field is necessary for every dictionary. The following
composite retains the entire angular quotient without such a field.
Its native word action and its radial extension have further duties.

## 1. A global composite on the angular quotient

For P=t u, R=t v, with t>0 and unit u,v, set

    U=U(u), C=U(bar v), J=diag(i,-i),
    A=U J U^-1, W=U C^-1.                              (1)

The matrix convention U(.) is the one displayed in the preceding
reference proof. Complex conjugation is in the declared negative-form
frame. Multiplying U and C in one SU2 target uses that dictionary.
The Hermitian metrics alone do not derive the dictionary or its
preferred axes.

The physical phase action sends both U and C to their right products
with D_phi=diag(exp(i phi),exp(-i phi)). It therefore leaves A and W
unchanged. The matrix A is an anti-Hermitian unit quaternion with
A^2=-I and tr A=0. W is an unrestricted member of SU2.

In fact (1) gives a diffeomorphism

    Y=(S^3 x S^3)/U1 -> S^2 x SU2,
    [(u,v)] -> (A,W).                                  (2)

To construct its inverse, choose a local lift U with U J U^-1=A.
Define C=W^-1 U and take u and bar v as the first columns of U and C.
Changing the lift to U D_phi changes C to C D_phi, so the two vectors
change by exactly the original opposite-charge gauge action. Local
inverses therefore patch to a global smooth inverse on the quotient.
There is no discarded angular degree of freedom in (2).

This recovers the familiar S^2 x S^3 topology of this particular
angular space, now with an explicit map on its actual coefficients.
It is not a derivation of a new spacetime factor.

## 2. Carry the complete leading metric and connection

Use the positive su2 norm <X,Y>=-tr(XY)/2. Let

    k=dW W^-1, D A=dA-(1/2)[k,A].                       (3)

The source quotient metric of the first C7 note becomes exactly

    ds_quot^2=2 dt^2
               +(t^2/2)(||D A||^2+||k||^2).           (4)

Here is a direct derivation retaining the cross term. In a quaternion
orthonormal basis J_1,J_2,J_3=J, write

    U^-1 dU=sum_j alpha_j J_j,
    U^-1 k U=sum_j beta_j J_j.

Since C=W^-1 U, C^-1 dC has components alpha-beta. Consequently

    |du|^2=|alpha|^2, |dv|^2=|alpha-beta|^2,
    a_u=alpha_3, a_v=-alpha_3+beta_3.

Substitution into the actual metric gives its angular factor

    |alpha|^2+|alpha-beta|^2-(2alpha_3-beta_3)^2/2
          =2|alpha_perp-beta_perp/2|^2+|beta|^2/2.

The commutator in (3) has norm squared
4|alpha_perp-beta_perp/2|^2. This proves (4). Treating (2) as a
product of two independent round metrics would lose this coupling.
The transported metric remains positive for t>0.

In a local Hopf lift U of A, the original Gauss connection is

    A_phase=a_u-(1/2)<A,k>.                            (5)

Indeed <A,k>=beta_3. Its first term transforms by d phi under a
lift change and its second term is globally defined on Y. Thus

    F_phase=F_Hopf-(1/2)d<A,k>.                        (6)

On the explicit primitive sphere v=bar u, W=I, so (5) reduces to
the Hopf connection and (6) integrates to the existing unit. These
equations fix the same connection in different variables, with no
new hopping coefficient or reference kinetic weight.

The nonlinear family can be labelled by (A,W) through the same
parameter map when its C7 inverse hypotheses hold. Its exact source
metric and connection are the pushforwards of those already defined
by the nonlinear fields and real Gauss equation. Formulae (4)-(5)
are the leading terms. No exact nonlinear product metric or new
isometry is inferred from this leading coordinate calculation.

## 3. Word evaluation is available, with a visible relation

The composite pair gives a based representation of F(a,b) by

    a -> A, b -> W.                                    (7)

Every word can be evaluated in its original order. The representation
always kills a^4, since A^2=-I. Thus (7) is a restricted register
comparator; it is not faithful on the free group or the whole native
based representation family. This relation was not forced on the
foundational generator by the physical charges. It entered through
the chosen composite (1).

For a unit quaternion W=w_0+w, with imaginary vector w, let the unit
imaginary vector of A be n. Direct quaternion multiplication gives

    tr[A,W]=2-4(|w|^2-(n dot w)^2).                    (8)

The same identity follows from the SU2 Fricke formula with
tr A=0, tr W=2w_0 and tr(AW)=-2 n dot w. The trace ranges between
-2 and 2 on this family; the physical quotient has not forced one
value. In particular W=I on the entire primitive sphere, so the
composite commutator is I there. Its curvature unit coexists with
commuting composite generators. Identifying that unit with a native
noncommutativity invariant would therefore require another argument.
No knot-meridian trace is being used in (8).

## 4. One Nielsen shear is an actual leading isometry

The native operation (a,b)->(a,ab) acts on (7) as

    T:(A,W)->(A,AW).                                   (9)

It is realized on the original form directions by

    (u,v)->(u,i v).                                   (10)

Indeed C changes to C(-J), and U[C(-J)]^-1=A W.
Equation (10) preserves all terms of the leading source metric and
the Gauss connection. It commutes with the physical gauge circle.
Thus the angular dictionary has one explicitly compatible native
move; the negative conclusion about the earlier direct map cannot
be transferred to this different map.

The action of this move has order four here: T^4=identity. The
infinite word shear is represented by a finite action because of
the relation a^4=1. Compatibility of one move therefore does not
establish a faithful native action.

The second elementary operation (a,b)->(ab,b) generally leaves this
angular subfamily. For example W=-A is allowed, while AW=I has
trace 2 and cannot be the first composite of (1). A swap of the
generators likewise leaves the subfamily for a general W. The full
native architecture is not obtained by closing only (9).

## 5. The radial degree of freedom gives a larger chart

The physical family also retains its amplitude t. Given any specified
smooth invertible angle function theta(t) from t>0 to 0<theta<pi,
define

    G=cos(theta) I+sin(theta) A, B=W.                  (11)

This is a diffeomorphism from the punctured six-dimensional parameter
cone to (SU2 minus {I,-I}) x SU2. Its inverse reads theta from
tr G=2cos(theta), then obtains A=(G-cos(theta)I)/sin(theta), t from
the chosen function, and W=B. For the admitted small-amplitude source
family only its corresponding open angular range is earned.

This local register chart needs no seventh physical field. It does
need theta(t). For example theta=2 arctan(t/t_0) carries a positive
reference scale t_0 in the units of t. A dimensionless amplitude still
leaves the function as a dictionary choice. A coordinate convention
alone can be changed freely if all data are transported; requiring
native group multiplication to be the physical operation makes its
dictionary consequential and requires that operation to be derived.

The transported leading metric is

    2 (dt/dtheta)^2 dtheta^2
           +(t(theta)^2/2)(||D A||^2+||dB B^-1||^2).   (12)

An identification with an independently supplied native Haar or
product metric cannot discard these factors and the cross term.
Neither the source charges nor the conifold topology selects theta.

## 6. The radial chart retains its action and vertex duties

For (11), the native shear (G,B)->(G,G B) acts on the form variables
as v->exp(i theta(t))v, with t and u fixed. At each fixed t it is
a constant phase rotation. On a varying-amplitude path it introduces
additional terms. Evaluating the leading metric on any tangent Y,
its exact change is

    Delta g(Y,Y)=t^2 theta'(t) dt(Y)(a_u(Y)+a_v(Y))
                       +(t^2/2)theta'(t)^2 dt(Y)^2.   (13)

The sum a_u+a_v is basic under the original gauge action. For a
pure radial tangent with fixed u,v, the last term is positive when
theta' is nonzero. Thus the full leading source metric is not
invariant under this fixed-geometry radial word dictionary. A
transported geometry, field map or source might restore covariance;
the existing moving-Hodge metric is a relevant recovery control.
The nonlinear source correction retains its own computation and
could affect these terms. Equation (13) is not a universal obstruction
to the full registering architecture.

The second native move can send G B to I or -I and leave the chart.
These values are not a pair of harmless coordinate points of the
physical cone. At t=0 every angular coefficient tends to the same
background X_0. For fixed W, however, (11) tends to a native pair
whose second component is W. Distinct W therefore give distinct
limits of the dictionary at the same physical cone vertex. No
continuous extension of this particular chart can retain W there.
The projection to W already has this defect, whatever theta is.

A larger joint state that retains the registering record at the
restored-symmetry point can avoid this loss. Its source variables,
transitions and dynamics would then be part of the physical theory.
This test makes that obligation explicit; it does not exclude such
an extension or select its implementation.

## 7. What is reduced and what is still supplied

The four existing fields suffice for an explicit, lossless angular
composite and, with a radial dictionary, a six-dimensional native
pair chart. An additional charged reference is consequently one
possible completion, not a necessary deduction from dimension or
from the failed direct pair map.

The inherited connection and kinetic cross term have now been
transported into the composite variables. They introduce no free
link for a specified physical path. The declared SU2 coefficient
category, frames, angle dictionary, native-operation identification,
full E8 centre, source law and global extension remain earning duties.
All topology here belongs to the parameter family. A physical end
map and the complete fermionic construction are still required.

No foundational input is counted removed by these alternative maps.
Their value is an explicit positive construction and two distinct
controls: preserving every physical coordinate is achievable, and
preserving the full physical and native composition laws requires
more than a matching manifold or dimension.
