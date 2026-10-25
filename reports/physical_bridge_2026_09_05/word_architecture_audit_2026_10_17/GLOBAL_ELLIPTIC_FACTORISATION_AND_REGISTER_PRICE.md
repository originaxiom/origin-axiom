# A global elliptic factorisation and its retained boundary price

October 24, 2026. UNREVIEWED analytical source audit and elementary
group calculation. No scientific producer, test, collection or admission
gate was executed. This does not amend B1343, canonical GENESIS or any
frozen verification package. It requests a scope review, not banking.

## Question, quantifier and result

This concerns finite positive L/R words in the already specified
boundary-preserving braid subgroup, their closed-torus matrix images,
and their specified quaternion/matter lifts. It does not quantify over
all generated histories, all four-manifolds or all physical completions.

B1343 correctly excludes a hyperbolic return as the local monodromy of
one Kodaira singular fibre. That local exclusion does not exclude a
product of positive Dehn twists with the same closed-torus monodromy.
There is an explicit such product for LR and a conditional construction
for every positive L/R word. Crucially, it differs from the original
based word by a boundary twist. The existing matter representation
detects that difference, even when homology and the local coefficient
module do not. Thus this is neither a free completion nor a new SM
construction. It is a concrete compatibility duty for a possible end.

## Source recovery, not rediscovery

Sources were read without importing their executable modules:

- Main `da077b79713b12cf2fa9fad44c243ef00e419ccb`:
  `frontier/B1343_deriving_the_other_faces/FINDINGS.md` and its entire
  `verification/b1343_faces.py`. Q1--Q3 compare one local Kodaira
  monodromy with LR and its powers. The producer contains no product-of-
  local-monodromies test. Its broader printed inference is not an
  additional computed exclusion.
- Main's B1634 findings, read in full on October 25, already state
  the braid subgroup, its boundary kernel and the matter sign
  Delta^4=-I. That sign and the mapping-class interpretation are
  established prior work, not new outcomes of this note. The extension
  here to positive-twist products must not be described as discovering
  either fact. Restriction to the L/R subgroup does not require adopting
  the independently enlarged four-wording operation set.
- [Coherent word lifts](COHERENT_WORD_LIFTS_AND_LOCAL_BOUNDARY.md):
  the existing based identity Delta^4=I_c and its quaternion lift.
  SHA256 `000a8df7534b57bbbd62a5ff22a5b2d9a3817e52c8cd03e08ffb3428e3cf28ca`.
- [Common matter/boundary register](MATTER_AND_BOUNDARY_COMMON_REGISTER.md):
  the existing action of Delta^4 on both modules, not just its matrix
  image. SHA256
  `919d215b4f6f6d32095c8341d7bef2036b97ae41d74b2fd849881a32cd6551f6`.
- Korkmaz and Ozbagci, *On sections of elliptic fibrations*, arXiv
  math/0604516v1, Introduction and section 3.1, read personally in
  [the primary text](https://arxiv.org/html/math/0604516v1), October 24.
  Their conventions compose rightmost first. Positive twist products
  construct Lefschetz fibrations over a disk with closed regular fibres;
  their one-holed torus relation identifies (UV)^6 with the boundary
  twist for intersecting positive twists U,V. This is a topological
  construction theorem, not a physical action or a holomorphic model
  with specified gauge singularities. The preprint is from 2006; the
  HTML conversion's displayed 2026 date is not its publication date.

Searches of main, the SM branch `293ab0e1a` and chat1 `252fddf28`
used positive factorization/factorisation, chain relation, boundary
twist, Lefschetz fibration and one-holed torus. They recover existing
boundary/register and character-variety work; they do not certify
absence under every spelling, on every branch or in deleted history.
No claim of repository-wide novelty is made. Before extending this
into a new producer, ask the receiving seats for any existing exact
factorisation/completion under another name. The classical relation
and the previously proved registered sign are explicitly reused here.

## Conventions and algebra

Keep the old based maps on F2=<a,b>, rightmost map first:

    L(a)=a,     L(b)=ab,
    R(a)=ab,    R(b)=b,
    c=a b^-1 a^-1 b.

Both preserve c. Put U=L and V=R^-1. With the oriented torus
convention in which U is a positive twist, V is the positive twist
about the intersecting curve; R itself is its inverse. Their matrices
are

    U = [[1,1],[0,1]],       V = [[1,0],[-1,1]],
    UV = [[0,1],[-1,1]],     LR = [[2,1],[1,1]].

The already used exact braid relation is UVU=VUV. Write

    Delta=UVU,          B=(UV)^6=Delta^4.

For completeness, Delta^2=(UVU)(VUV)=(UV)^3. The braid relation
also gives Delta U=V Delta and Delta V=U Delta, so Delta^2, hence
B, commutes with U and V. The existing free-word calculation gives
B=I_c in the based automorphism group; on closed-torus homology B=1.
Under the one-boundary mapping-class interpretation B is a boundary
twist. A puncture, a fixed boundary circle and a closed torus are not
being silently identified: these are the respective retained/forgotten
boundary data in this construction.

Now take the positive word

    W = U (UV)^5 U.

It has twelve positive factors. Multiplication by V gives

    W V = U (UV)^6 = U B,
    W   = U B V^-1 = U V^-1 B = LR B.             (1)

Thus W and LR have exactly the same closed-torus matrix, of trace 3.
The cited construction theorem produces a genus-one Lefschetz
fibration over a disk whose closed regular fibre has that boundary
return and whose twelve vanishing cycles are the displayed factors.
This is not a single Kodaira degeneration and does not contradict the
monodromy theorem. No claim is made that the resulting smooth fibration
has the desired complex, metric, spin, E8 or physical structures.

Nor is this an extension of the same based return without extra data:
equation (1) retains B. In particular, it does not prove an unchanged
boundary-framed filling of the original punctured-torus mapping torus.
No classification of the unmarked three-dimensional boundaries, no
minimality of twelve factors, and no uniqueness of this completion
has been established here.

## The price seen by the existing register

Use precisely the old lifts, not newly chosen intertwiners:

    g_U=(1+i)/sqrt(2),       g_V=(1+j)/sqrt(2),
    g_Delta=(i+j)/sqrt(2),   g_B=+1,
    rho(c)=-1.

Consequently the lifted B is (I_c,+1)=epsilon J_c, not J_c.
The common-register proof already computes its pair (g,mu)=(1,-1).
On the local coefficient module its action is +I; on EACH of the
two matter triplets it is -I. Since this element commutes with the
chosen word lifts, equation (1) implies

    matrix(W) = matrix(LR),
    A_local(W) = A_local(LR),
    U_matter(W) = - U_matter(LR).                  (2)

The last statement holds for both triplets and survives conversion
between left and right action conventions because the scalar is -1.
It is a statement about the specified cohomology modules, not about
an already identified physical fermion spectrum. The based map itself
also changes by I_c. Calling W merely the same LR on the strength of
its matrix or local action would discard observables the joint
register was expressly constructed to retain.

A sign in a representation is not automatically a measurable physical
difference. Whether it can be compensated by an admitted gauge/spin
operation must be checked on the complete fields and observables,
rather than assumed either impossible or harmless.

Repeated B^2 is invisible even to this finite joint representation,
but not to the full based word I_(c^2). This reuses the earlier
finite-quotient warning: invisibility in selected modules is not
physical equivalence without a specified full observable algebra.

## Family extension, with its actual bound

For a finite positive L/R word X with n_L copies of L and n_R copies
of R, replace each R by

    (UV)^5 U = V^-1 B = R B.

Centrality moves the inserted boundary twists to the end. The result
is a positive U/V word W_X of length n_L+11 n_R satisfying

    W_X = X B^(n_R),
    matrix(W_X)=matrix(X),
    A_local(W_X)=A_local(X),
    U_matter(W_X)=(-1)^(n_R) U_matter(X).          (3)

This gives a construction over that entire declared finite-word
family, not a census of admissible infinite histories or a claim that
this boundary cost is minimal. Changing each constituent this way
must also transport its joins, lifts and relations; equation (3)
does not supply those interactions. Even when n_R is even, its based
boundary word must not be dropped merely because these modules agree.

## Consequence for physics and remaining input duties

The valid old local exclusion remains unchanged. Its extrapolation
to every global elliptic dynamical construction is not licensed by
the Q1--Q3 computation: a product is a different quantifier, and (1)
exhibits why the distinction matters. This does NOT by itself repair
the specific IV* / E6 proposal or refute its other requirements.

Nothing here derives positivity of the twists from non-cancellation,
selects a four-dimensional physical spacetime, supplies a gauge
bundle, derives a stationary metric/end action, or produces a chiral
operator or three generations. Those are not paid inputs. A chosen
positive Lefschetz completion is an additional construction criterion
until its physical role and necessity are earned.

The useful next question is narrower and constructive: can a permitted
physical completion of the SAME parent absorb the required boundary
twist while preserving the full registered matter transport and the
joining law? An extra spin/gauge factor might compensate its sign,
but must be exhibited globally with all fields, kinetic terms and
the operator domain. The earlier compensations that change the weak
factor or the coefficient system retain those costs; they are not
borrowed as a solution. Until such a map is built, this is a scoped
geometric opening with a derived register constraint, not physical
chirality, an accepted theorem arc or a completed input reduction.

## October 25 reuse check: a conditional compensation already exists

The preceding last paragraph must NOT be read as saying that no
geometric spin compensation has been constructed. Before proposing
one, I reread the existing
[joint root action](JOINT_ROOT_ACTION_AND_AUTOMORPHY.md) and
[principal-parts/Green transport](REGISTERED_PRINCIPAL_PARTS_AND_GREEN_TRANSPORT.md)
in full. They already supply one for a DECLARED vertical ordinary-spin
family, without adding a new arbitrary sign. This is recovered prior
work; the substitution below is not a new physical mechanism.

For the same lifted B=epsilon J_c, those sources give

    P_B=C (the root sheet flip),    g_B=1,    mu(B)=-1,
    k_B=-1,                        r_B=-1.

Here F(P_e x)=k_e g_e F(x), r_e is the actual derivative of the root
normal frame, and k_e^2=j_e mu(e). Consequently j_B=-1. The value
of j is the previously DECLARED metaplectic/vertical spin lift, not
a new derivation of the higher-dimensional physical spin structure.

The old actual scalar-section sequence has transport

    A_e=k_e^-1 O_e,   M_e=r_e(O_e tensor g_e),
    C_e=k_e j_e^-2 O_e.

At B these are (-I3,-I6,-I3). In the declared vertical spin sequence,
the SAME sources instead give

    A_e^spin=(j_e/k_e)O_e,
    M_e^spin=j_e r_e(O_e tensor g_e),
    C_e^spin=(k_e/j_e)O_e.

All three are +I at B. The previous proof also retains the normal
derivative in the actual Green pairing; it is not only cancellation
of labels. Thus a raw matter sign cannot establish an obstruction
for this dressed vertical spin sequence. It is precisely the field
type and its transported lines that decide which action is relevant.

The root sheet action and full based word still differ. Identity on
these spin sequence maps is not identity on the entire relational
architecture. Moreover these conditional maps do not yet identify
the spin sequence with all fields of the E8 parent, or prove that it
extends through the twelve vanishing cycles of the proposed fibration.
No stationary completion, full spectrum, anomaly cancellation or
physical end selection follows. The revised next duty is therefore
to TEST THE EXISTING compensation against that common parent and
global extension, not to construct it again or bank the undressed
minus sign as a new no-go. The sign comparison (2)--(3) keeps its
explicit raw-module scope.
