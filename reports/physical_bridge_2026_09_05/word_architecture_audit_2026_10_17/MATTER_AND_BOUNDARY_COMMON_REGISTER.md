# The matter and boundary actions on one registered system

October 18, 2026. Analytical continuation of
[the coherent coefficient action](COHERENT_WORD_LIFTS_AND_LOCAL_BOUNDARY.md)
and [its faithful finite refinements](FAITHFUL_LIFTED_REGISTER_TOWER.md).
This draft is not experimentally admitted or independently reviewed.
No scientific producer has been imported, collected or executed.

For the specified quaternion local system, the six-dimensional
cohomology action factors exactly into quaternion-axis transport and
the untwisted two-dimensional cohomology action. The latter splits into
two opposite characters on the entire four-wording lifted completion.
This gives a common registered action on the matter triplets and local
boundary module, without identifying the two modules. Their joint image
has order 192. That image is still only a finite quotient of the based
architecture; it supplies neither a physical field assignment nor a
boundary condition.

## Inputs and conventions

Use E={(phi,g):rho phi=Ad_g rho} and the natural inner lifts
J_h=(I_h,rho(h)) from the preceding note, with rho(a)=i, rho(b)=j,
and i,j,k represented by the existing SU(2) matrices. The admitted
operation set in this calculation is the four wordings and their
inverses. Its derivation from the founding principle remains open.

Let V_p=H^1(F2;chi_p rho), P={(1,0),(0,1),(1,1)}, and
M0=H^1(F2;rho). The cocycle convention is

    z(xy)=z(x)+rho(x)z(y),    delta(v)(x)=(rho(x)-1)v

on M0, and the corresponding parity-twisted formula on V_p. The
pullback D_e z=g^-1 z composed with phi is a right action:
D_f D_e=D_(ef). The left action is U_e=D_(e^-1).

Set Q_(1,0)=j, Q_(0,1)=i, Q_(1,1)=k. These are both a basis of
the complex imaginary quaternions and intertwiners

    chi_p(x)rho(x)=Q_p rho(x)Q_p^-1.

In this ordered basis, write O_g for Ad_g. Since g is in 2O, O_g
is a real signed permutation of determinant one. No choice of a sign
for a lift is suppressed in E.

## An exact tensor factorization

Define an isomorphism

    F: C^3 tensor M0 -> direct sum_p V_p,
       e_p tensor [z] -> [Q_p z] in V_p.

Multiplication by Q_p intertwines the representations, cocycles and
coboundaries, so F is well-defined. For e=(phi,g), q=p phi, there is
a sign s(e,p) such that

    g^-1 Q_p g=s(e,p)Q_q.

To identify q, conjugate rho(x) by the left side. The two intertwiners
for chi_(p phi)rho differ only by a scalar; because both lie among the
imaginary quaternion units that scalar is a sign. Hence

    D_e(Q_p z)(x)
      =g^-1 Q_p z(phi(x))
      =s(e,p) Q_q [g^-1 z(phi(x))].

This proves the exact intertwining identity

    F^-1 D_e^V F = O_(g^-1) tensor D_e^0,
    F^-1 U_e^V F = O_g tensor U_e^0.                 (1)

It is a statement about every element of E, not a numerical inference
from a few generators. It also specifies which frame identifies the
three coefficient copies: independent changes of those frames must
transport F with them.

## The two characters from the untwisted cocycles

Every class in M0 has a unique cocycle representative with z(a)=0,
because i-1 is invertible. Write v=z(b), so this realizes M0=C^2.
Let l=(L,(1+i)/sqrt(2)), r=(R,(1-j)/sqrt(2)), and

    t=(1+i)/sqrt(2).

For L the representative remains in this gauge and

    D_l^0 v=g_L^-1 i v=t v.

For R the pulled-back cocycle has values
u_a=g_R^-1 i v, u_b=g_R^-1 v. Restoring z(a)=0 subtracts the
coboundary with parameter (i-1)^-1 u_a. Thus

    D_r^0 v=[g_R^-1-(j-1)(i-1)^-1 g_R^-1 i]v
            =(1-i)v/sqrt(2)=t^-1 v.                 (2)

The middle equality follows from

    (i-1)^-1=(-1-i)/2,
    (j-1)(i-1)^-1(1+j)i=(i+j).

The natural inner identity in the preceding note gives D_(J_h)^0=1
for every h. The four chosen lifts satisfy

    lbar=J_a^-1 l,    rbar=J_b r.

They generate E, by the nonsplitting argument in the faithful-register
note. Equivalently l,r,J_a,J_b generate E. Equations (2) therefore
diagonalize the whole action on M0, not just its original two moves.
In the standard matrix realization i=diag(i,-i), put
zeta=exp(pi i/4) and name the two characters by

    mu_+(l)=zeta,       mu_+(r)=zeta^-1,
    mu_-(l)=zeta^-1,    mu_-(r)=zeta,
    mu_+(J_h)=mu_-(J_h)=1.

The plus line is the second coordinate of M0 in this gauge, the minus
line the first. Both characters send epsilon=(id,-1) to -1; mu_- is
the inverse of mu_+. From (1),

    V = T_+ direct sum T_-,
    U_e on T_+ = mu_+(e) O_g,
    U_e on T_- = mu_-(e) O_g.                       (3)

This proves a simultaneous normal form for the actual cohomology
action on the enlarged lifted system. The two triplets are irreducible:
the natural inner lifts give the three distinct parity axes, while
l and r permute them transitively. They are inequivalent: their
l eigenvalue multisets are (1,3,7)/8 and (1,5,7)/8 turns. This names
the hands by their matrices; it does not reprove the Hodge identification
or identify either hand with physical chirality.

The paper's inverse-pullback convention lists (1,3,7)/8 for its triplet,
which matches T_+ at this generator. The SM seat's W38 normal-form
source instead lists the opposite scalar on L. That hand/convention
difference must be retained when comparing couplings; a shared abstract
group does not identify two concrete multipliers.

## The joint finite image

Let pi(g) be the permutation of the three unsigned quaternion axes,
and use mu=mu_+. Every generator satisfies

    mu(e)^4=sign(pi(g)).

Both sides are characters, so the identity holds on E. The joint map
e->(g,mu(e)) therefore lands in the finite group

    K={(g,z) in 2O times mu_8 : z^4=sign(pi(g))}.    (4)

Its projection onto 2O is onto. Its kernel under that projection is
the entire mu_4, not just {+1,-1}. Indeed, with
Delta=l r^-1 l and c=a b^-1 a^-1 b,

    g_(Delta^2)=-1,   mu(Delta^2)=zeta^6=-i,
    g_(J_c)=-1,       mu(J_c)=1.

Consequently Delta^2 J_c^-1 maps to (1,-i). This generates all four
allowed phases over g=1. Surjectivity onto 2O and this kernel prove
that the image equals K and has 48 times 4 = 192 elements.

The local boundary representation A detects g faithfully, as proved
in the preceding note, but forgets z. The matter triplet detects zO_g
and identifies (1,1) with (-1,1). No other pair lies in that kernel:
a scalar real orthogonal 3-by-3 matrix of determinant one can only
be +I. Hence the matter image has order 96 and the local image order
48, whereas their direct sum detects all 192 elements of K.

| Registered element | Pair (g,z) | Local boundary | Matter |
|---|---|---|---|
| epsilon | (-1,-1) | -I | -I |
| J_c | (-1,1) | -I | +I |
| Delta^4 | (1,-1) | +I | -I |

This order 192 is not B1606's group obtained by appending bare parity
grading to the local module, nor B1600's enlargement by the orientation
reversing swap. No swap or new boundary grading was used. The local
module's existing 2+4 splitting is unchanged. Agreement of orders
cannot transfer those other constructions' irreducibility or index.

K is a common finite quotient for these modules, not the whole based
operation group. For example J_(a^4) is a nonidentity based inner
operation with g=1 and mu=1, and is invisible to both modules. The
faithful finite refinement tower remains necessary for the full E.

## What a modulus only field omits

Natural J_a and J_b act trivially on the homology matrix and hence on
tau. On either matter triplet they act respectively as

    diag(-1,+1,-1),    diag(+1,-1,-1).

Their common fixed space is zero. A T-valued field f(tau) that depends
only on tau and is required to obey f(e tau)=U_e f(tau), with no extra
inner automorphy factor, must therefore vanish. The same is true if
the field includes modular weight factors pulled back from homology
that are trivial on these two natural inner lifts.

This is not an obstruction to the paper's ruled-branch modular forms:
those two inner maps are not moves on that restricted branch. Nor is
it an obstruction to fields depending on the registered state. For
example take the deliberately unreduced state space X=H_upper times E
with e acting by (tau,r)->(h(e)tau,e r), where h is the homology
matrix. For any holomorphic f on H_upper, the field

    F(tau,r)=U_r f(h(r)^-1 tau)

is nonzero if f is and satisfies F(e(tau,r))=U_e F(tau,r). This is a
kinematic witness, not a proposed minimal state space or the paper's
fully weighted theta-field construction. It shows precisely why a
failure on tau alone cannot eliminate every retained-register field.

## Source reconciliation and remaining duties

Sources were read at fetched main
2e5716bd9bea013d69f3cd733f083b61a6f59dbd and the SM branch
11ec0144ef25e8848968b909735c205809567fdf. Main was unchanged by the
October 18 fetch. Read bodies include main B1600's w10_check.py,
B1617's weave_at_omega.py, B1641's findings and scope addendum,
B1640's frame_audit.py, the paper's s04_modular.tex and
s05_couplings.tex, and the SM seat's complete the_couplings_exact.py,
W21_RULE.md and W42_RULE.md. Preregistration predictions are not
treated as their execution results.

W9/W10/W21/W38 already record the scalar-times-octahedral normal form
on the ruled branch and its two triplets. B1641 already identifies
parity-dependent point-push action and a fibre-blindness obstruction.
The new argument is the explicit cochain intertwiner (1), its exact
extension through the coherent E, the shared quotient (4), and the
registered-state scope of that obstruction. It is not a new discovery
of a triplet, theta correspondence, or a replacement root.

The paper's holomorphic fields, their automorphy line, puncture,
regulator and physical matter assignments still need a simultaneous
specification. The
[coupling transport analysis](REGISTERED_COUPLING_TRANSPORT.md)
addresses the algebraic tensor and distinguishes transport from joining.
No complete physical-input row is paid. Exact finite controls, separate
review, main acceptance and the applicable admission/publication checks
remain required; this proof does not amend the frozen v2/v3 packages.
