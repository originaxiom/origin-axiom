# The four charged forms determine a quotient and a connection

2026-11-17. PHYSICAL-C7 author hand derivation, pending independent
review. No scientific producer, symbolic evaluator, test or numerical
integration ran. The supplied physical parent and the P-C3e kernel,
moment and inverse estimates are explicit hypotheses.

The coefficients below are the two actual positive-charge form modes
P=(P_1,P_2) and the two actual negative-charge form modes R=(R_1,R_2).
All four belong to the same fixed colour-preserving sector. Canonical
coordinates use their positive physical source Grams. Other fields,
their conjugates and continua retain their places in the full theory.

## 1. Retain the entire charged-form space

P-C3e's BALANCED_FORM_TANGENTS_AND_ACTUAL_MOMENT_CORRECTION.md gives
the literal unbroken moment on these coordinates

    D_Q^(2)=e_Q (||P||^2-||R||^2).                    (1)

Its raw pure-form fields are exactly F-flat. The orthogonal real gauge
response cancels the non-Q quadratic moment. Thus the leading zero-
moment coefficient space, after quotient by its effective Q circle, is

    C_0={||P||^2=||R||^2}/U(1),
    (P,R) -> (exp(i phi)P,exp(-i phi)R).               (2)

The circle in (2) is effective on these colour-singlet coefficients.
Its lift to all E8 fields requires the centre calculation in the
companion note. A source that fixes a phase reference needs its own
variables and transformation law carried through this quotient.

Set Z_ij=P_i R_j. Every invariant polynomial is a product of these
entries, since each invariant monomial has equal numbers of P and R
factors. Their relation is

    det Z=Z_11 Z_22-Z_12 Z_21=0.                       (3)

Every nonzero matrix of rank one has a factorization P R^t. Two such
factorizations differ by (P,R)->(lambda P,lambda^-1 R), lambda in C*.
Choosing |lambda|^4=||R||^2/||P||^2 gives a balanced representative,
unique up to (2). A balanced representative with Z=0 has P=R=0.
Equations (2)-(3) identify the coefficient quotient with the affine
conifold, including its singular vertex. Its smooth part has three
complex dimensions. This identifies a family of coefficient data.
The full physical vacuum space can contain additional branches.

The quotient construction is established mathematics. Klebanov and
Witten's section 2 and equations (11)-(16) exhibit this same invariant
matrix and the zero-level quotient. The programme-specific step here
uses the four already-derived form slots and their actual source moment.
[Primary paper](https://arxiv.org/pdf/hep-th/9807080)

## 2. Eliminate the longitudinal gauge field with the source metric

Write b=e_Q B for the canonically normalized Abelian gauge field B.
At this order its scalar kinetic term is

    ||dP-i b P||^2+||dR+i b R||^2.                    (4)

At a nonzero coefficient pair the real Gauss minimizer is

    b=A,
    A=[Im(P^dagger dP)-Im(R^dagger dR)]/N,
    N=||P||^2+||R||^2.                                (5)

Indeed the quadratic in b is N b^2-2b J plus its b-independent term,
with J the numerator of (5). This retains the original charge signs.
The induced metric is

    ds_quot^2=||dP||^2+||dR||^2-J^2/N.                (6)

Under a local change of coefficient representative by phi,
A -> A+d phi. The same-source rule for horizontal transport is
therefore chi'=-A(gamma') along a specified path gamma. Its phase
link is exp[-i integral_gamma A] in local endpoint frames. Endpoint
frame changes transform this link with the two endpoint phases.
The connection is fixed by (4). An independent phase link would change
the stated kinetic theory for that path.

Equation (5) is the leading effective-circle part of the full real
Gauss connection. The latter includes non-Abelian gauge directions and
the nonlinear stationary response. Those are treated in the companion
nonlinear note. For one external spatial coordinate there is no external
F_mu_nu, so its longitudinal elimination follows directly from the
kinetic variation. In several coordinates the Abelian gauge kinetic
term also contributes. Algebraic elimination describes the leading
derivative regime relative to the Higgsed vector mass.

## 3. The inherited metric and topology

On the balance locus put P=t u, R=t v, with t>0 and ||u||=||v||=1.
Define a_u=Im(u^dagger du), a_v=Im(v^dagger dv). Then

    A_0=(a_u-a_v)/2,
    ds_quot^2=2 dt^2+t^2[||du||^2+||dv||^2
                                           -(a_u-a_v)^2/2].         (7)

The angular manifold is

    Y=(S^3 x S^3)/U(1),
    (u,v)->(exp(i phi)u,exp(-i phi)v).                 (8)

The action is free. The homotopy exact sequence, with S^3 x S^3
simply connected and with zero pi_2, gives pi_1(Y)=0 and pi_2(Y)=Z.
Hurewicz then gives H_2(Y,Z)=Z. Formula (8) is the standard topology
of T^(1,1). The source kinetic metric on it is specified by (7).

In invariant complex coordinates the same quotient metric has Kahler
potential, in the source scalar kinetic convention,

    K_quot=2 sqrt[tr(Z Z^dagger)].                    (9)

This differs from the Ricci-flat conifold potential discussed in the
primary paper. No Ricci-flat internal space, spacetime compactification
or extra spacetime dimension is inferred from (3) or (8).

The vertex t=0 is at finite distance in (7). Its Q gauge symmetry is
restored and the circle action ceases to be free there. All topology
statements about the bundle below refer to t>0. A deformation through
the vertex requires the unreduced fields and their gauge dynamics.

## 4. A primitive curvature period follows without choosing a flux value

Consider the explicit sphere in Y represented by v=bar u. Changing
u by exp(i phi) changes v by exp(-i phi), so it gives a well-defined
map CP^1->Y. Equivalently Z=t^2 u u^dagger on this sphere. An
orthonormal basis was used to display the sphere. The primitive
period does not depend on that coordinate choice.

The total circle bundle restricted to this sphere is the Hopf bundle.
Because a_(bar u)=-a_u, its connection is A_0=a_u. In a north chart
choose

    u=(cos(theta/2),exp(i varphi)sin(theta/2)).

The connection and curvature are

    A_N=sin^2(theta/2) d varphi,
    F=dA_N=(1/2)sin(theta) d theta wedge d varphi,
    (1/(2pi)) integral_(S^2) F=1.                     (10)

In a south chart A_S=A_N-d varphi. Their transition winds once.
The corresponding sphere is primitive in pi_2(Y), since the boundary
map to pi_1(U(1)) sends it to that single winding. Its orientation
reversal changes the sign. A half-unit from keeping only one of the
two Hopf terms would be an incorrect cycle or an incorrect connection.

The period in (10) is a property of the gauge-orbit bundle over the
space of stationary coefficient directions. It provides a concrete
candidate for a registered curvature unit. A map from the physical
carrier or its end data into this family is still needed to use it as
physical flux or an index contribution.

## 5. The transport retains its path duty

For the latitude theta=theta_0 on the displayed sphere,

    holonomy=exp[-i pi(1-cos(theta_0))].                (11)

The connection has a fixed primitive period while its loop holonomies
can vary continuously with the loop. The two endpoint configurations
alone therefore leave a path duty. A field equation, an actual history
law or a specified source must determine which path contributes.

As a scalar closed-loop holonomy, (11) is Abelian. Applied alone to
based closed words it kills their commutator. The larger based register,
its non-Abelian gauge transport and its measuring relation remain
essential for retaining the full ordered architecture.

The non-Abelian source connection, operator domains and full E8 centre
are kept in the companion notes. No fundamental action coefficient,
state amplitude, history weight or physical three-family assignment
is fixed by the coefficient geometry established here.

## 6. The resulting restricted joining response

Take an external interval of physical length L and restrict the field
to the admitted stationary family. Eliminate its real longitudinal
gauge component with the full version of (5). The restricted energy is

    E[gamma]=integral_0^L g_family(gamma',gamma') dx.   (12)

Its internal residual potential is zero at every point of the family.
For fixed endpoints a,b in a regular region, Cauchy–Schwarz gives
E>=length(gamma)^2/L. Taking the infimum over the allowed family paths
therefore yields

    Gamma_L(a,b)=d_family(a,b)^2/L.                   (13)

An attaining path is a minimizing geodesic at constant speed. A singular
vertex, excluded state or source restriction can alter attainment or
the allowed path distance and must be retained. The leading metric
in (7) specifies the first approximation to (13). The nonlinear
metric is determined by the response in the companion note.

Where the endpoint branch is smooth, variation of (12) gives the
momenta -2 g_family(gamma'(0),.) and
+2 g_family(gamma'(L),.) at the two ends. The usual variational sewing
over an intermediate state follows by minimizing the sum of the two
interval energies. Its coefficient comes from the original mode norm
and physical length. It is fixed once those data are fixed.

The full field equations normal to the stationary family remain.
A geodesic of the family can source normal fields through its second
fundamental form. Equations (12)-(13) give a restricted source response
whose actual completion can be tested with the C5/C6 covariant normal
equation. They do not establish a full spacetime interface by themselves.
