# The theta root lives on the existing quaternion cover

October 19, 2026. Analytical source/proof checkpoint, pending independent
review and prospective experimental admission. No scientific producer,
test collection or numerical calculation was executed. This is not a
new numbered arc, physical-index result or publication certificate.

## Question, recovery sources and quantifier

For the specified quaternion coefficient rho(a)=i, rho(b)=j, determine
which global cover realizes the preceding theta doublet and whether its
actual branch transport removes the reduced-base stabilizer obstruction.
This concerns that coefficient system across the elliptic family, not
every allowed word architecture or a newly selected physical carrier.

The prior [theta repair](THETA_SEQUENCE_REPAIR_AND_MONODROMY_DUTY.md)
and [profile norm](EXPLICIT_MATTER_PROFILE_NORM_AND_END_SCOPE.md)
retain the local branch and warn that complete descent is not proved.
The existing [form-parent proof](../weave_form_parent_2026_10_08/PROOF.md)
already constructs the regular degree-eight quaternion cover, its four
ramification points and genus three. Those facts are recovery controls,
not discoveries of this checkpoint. The addition below is an explicit
theta-root presentation and its maps to that existing cover.

All configured remote references were fetched successfully on October 19
after retrying the restricted network failure. Main remains
`2e5716bd9bea013d69f3cd733f083b61a6f59dbd`; the SM branch remains
`11ec0144ef25e8848968b909735c205809567fdf`. The read-only already-banked
lookup used `quaternion theta branched monodromy`, returned existing hits,
and licenses no claim of repository-wide absence. The relevant current
ladder/framework/campaign passages retain the quaternion form positive
and the distinct ordinary-spin/domain obligations.

Theta arguments below have periods 1,tau. Scalar i is distinguished
from the quaternion matrix i by its context. The primary formula inputs
were reread in [DLMF 20.2.6--9 and 20.2.11--14](https://dlmf.nist.gov/20.2)
and [20.7.26--33](https://dlmf.nist.gov/20.7). These are classical theta
identities; this note's covering and compatibility arguments are authored
deductions, not theorems claimed from those formula tables.

## A local square root is not a double cover of the original torus

Let Lambda=Z+tau Z and E_tau=C/Lambda. No connected two-sheeted cover
of E_tau minus its one puncture can have nontrivial local puncture
monodromy. Its sheet action lands in S2, an abelian group, while the
puncture loop is a commutator in pi1(E_tau minus {0})=F2. Hence its
sheet action is the identity. Equivalently a compact double cover with
exactly one simple ramification point would violate Riemann--Hurwitz:
2g-2=1 is impossible.

This does NOT forbid the local coordinate z=u^2, a double cover of the
lattice plane, or the existing degree-eight cover. It forbids identifying
any of those with a two-sheeted cover of the original once-punctured
torus. A theta-root branch on the plane needs its period gluing too.

## Explicit root surface and period gluing

On the lattice plane take the connected smooth root surface

    Z_tau={(z,w): w^2=theta_1(z|tau)}.

Include the simple zeros for its smooth completion over C; delete them
when discussing unramified punctured covers. Simplicity is the standard
theta zero property, also used by the preceding profile proof. Put
t(z)=exp(-pi i tau/2-pi i z) and define, rightmost map acting first,

    C(z,w)=(z,-w),
    A(z,w)=(z+1, i w),
    B(z,w)=(z+tau, i t(z) w),
    K1(z,w)=(z+2,w),
    K2(z,w)=(z+2tau,exp(-2pi i tau-2pi i z) w).

The theta quasi-period laws verify that all maps preserve the equation.
Direct substitution, using t(z+1)=-t(z), gives

    C^2=1,  C central,
    A B=C B A,  A^2=C K1,  B^2=C K2.             (1)

K1 and K2 commute and are central in the group generated here. Their
base translations are linearly independent, so they generate Z^2 and
their nonidentity elements have no fixed point. Form

    Y_tau=Z_tau/<K1,K2>.

It is a double cover of C/(2Lambda), branched over its four distinct
points Lambda/(2Lambda). The map C/(2Lambda)->C/Lambda has degree four.
Thus Y_tau has degree eight over E_tau, four simple ramification points,
and 2g(Y_tau)-2=4, giving genus three.

On Y_tau, (1) becomes

    A^2=B^2=C,  AB=CBA,  C^2=1.                 (2)

The eight resulting maps are distinct: the four base translations in
Lambda/(2Lambda), each with two root signs. They give its full regular
deck group Q8 over E_tau, with A->i, B->j, C->-1. This identifies the
literal monodromy of the earlier eight-square cover, not just its genus.
The double cover and eightfold cover describe different stages of this
factorization, not competing carriers.

For trivializing the ENTIRE specified faithful rho coefficient by an
ordinary connected cover, eight is minimal: its covering subgroup must
lie in ker rho, whose index is eight. This is not a minimality theorem
for every representation, a single projective observable or a physical
universe. Starting with rho already supplies this finite quotient.

## The actual field descends and extends as a form

Write N=(i theta_2(z|2tau),theta_3(z|2tau))^T and F=N/w.
Full-period formulas at modulus 2tau give

    N(z+2)=N(z),
    N(z+2tau)=exp(-2pi i tau-2pi i z) N(z).

Thus F is invariant under K1,K2 and is a meromorphic doublet on Y_tau.
The half-period formulas already read in the theta repair give

    F(Ax)=i_matrix F(x),
    F(Bx)=j_matrix F(x),
    F(Cx)=-F(x).                                (3)

These are noncommuting deck maps on Y_tau, not commuting translations
of a single-valued doublet on the original torus. The lost puncture
commutator now acts on a real geometric argument by C.

Near each ramification point use z-z0=u^2. F has a simple pole in u,
but alpha=F dz has a regular nonzero leading coefficient proportional
to du. It extends as a doublet of global holomorphic one-forms on Y_tau.
This recovers, rather than replaces, the earlier quaternion Hodge proof.
It does not make F itself a globally holomorphic function on a compact
curve, nor turn the form into an ordinary spinor.

There are no common zeros of the two components away from ramification:
the theta_2 zeros at modulus 2tau are 1/2+Z+2tau Z, whereas theta_3 zeros
are 1/2+tau+Z+2tau Z. These sets are disjoint for Im tau>0. The regular
branch coefficients above exclude common zeros at ramification too.
Consequently alpha is nowhere zero as a SECTION of K_Y tensor C^2,
not as a scalar one-form. Individual components may have zeros.

For example this gives the ordinary holomorphic Koszul sequence

    0 -> O_Y --alpha--> K_Y tensor C^2
       --(alpha^T epsilon)--> K_Y^2 -> 0,         (4)

where epsilon=[[0,1],[-1,0]]. Its exactness follows locally by solving
with either nonzero component. Tensoring by a declared rank-three bundle
retains exactness. This is a real global geometric control; it is NOT
already the paper's puncture evaluation sequence, an identification of
T_plus/T_minus on full E, or a four-dimensional fermion index. The
canonical-bundle powers, deck actions and ramification must accompany
any such comparison. Forgetting them would repeat the earlier error.

## Modular root maps and a central-relation control

Take principal tau^(1/4) on the upper half-plane and set
alpha0=exp(pi i/8), beta0=exp(-3pi i/8). The primary theta laws give

    L:(tau,z,w)->(tau+1,z,alpha0 w),
    S:(tau,z,w)->(-1/tau,z/tau,
                 beta0 tau^(1/4) exp(pi i z^2/(2tau)) w). (5)

Squaring the w factors reproduces exactly theta_1's transformation,
including its odd-characteristic -i under inversion. In (5) denote
the target period maps by primes. Substitution gives

    L K1=K1' L,       L K2=(K2' K1'^-1) L,
    S K1=K2'^-1 S,    S K2=K1' S.               (6)

These checks show (5) really descends to the Y family. On its Q8 deck
group L sends (A,B) to (A',B'A'^-1), and S sends them to (B',A').
On the plane before the quotient the first S image is C B'^-1;
replacing it by B' is licensed only after (2). The plus-period B here
is not silently identified with the earlier affine convention's J_b,
whose base translation was -tau. Path and marking comparison is owed.

Composition now supplies root phases rather than resetting them. Since
arg(tau)+arg(-1/tau)=pi, (5) gives

    S^2:(tau,z,w)->(tau,-z,-i w),
    S^4=C,  S^8=1.                              (7)

There is also a nontrivial mixed control: (S L)^3=S^2. To check its
root factor set u0=tau+1, u1=tau/(tau+1), u2=-1/tau. They lie in the
upper half-plane, their arguments sum to pi, and their product is -1.
The three fourth-root factors therefore multiply to exp(pi i/4).
Together with (beta0 alpha0)^3=exp(-3pi i/4), this gives -i. The
Gaussian exponent cancels because

    1/(tau+1)+1/[tau(tau+1)]-1/tau=0.

The net coordinate map is z->-z, proving the stated relation. Equations
(5)-(7) define concrete coherent lifted modular maps. They do not prove
that their entire combined group with deck maps is the previously
specified E with all of its based relations and coefficient factors.

Indeed this remaining check has teeth: in E the existing proof has
s^4=epsilon J_c^-1 with J_c acting trivially on the reduced base. Here
the concrete S^4 is C. Identifying J_c with C would consequently force
epsilon to act trivially on this GEOMETRIC base, not as another C.
Both assignments and the source's minus-period convention must be
tested together on all relations. A new independent square-root sign
per word would not be a proof of descent.

October 19 own-error correction: commit `94613bc41` omitted the inverse
on J_c in that paragraph. Since s=Delta^-1, its fourth power is the
inverse of epsilon J_c. Q8 hides this based-word distinction. The
[joint-action successor](JOINT_ROOT_ACTION_AND_AUTOMORPHY.md) discloses
the correction and constructs the actual based root action; the original
mistake remains visible in that commit's historical text.

## What this pays, and what it does not

The specified matter profile needs no invented global twofold carrier
or dummy sign register: its actual root geometry is realized inside the
existing Q8 cover. Its period and modular branch maps can be written
explicitly, with central and mixed composition controls. This replaces
an unspecified geometric lift in this bounded model with a candidate
derived from its actual theta field. It does not derive rho itself.

The reduced-base obstruction no longer applies verbatim once the
commutator moves the root sheet. That does NOT establish the desired
full-E bundle map, its actual physical bulk transitions or a selected
boundary projector. The finite Q8 cover also does not retain the whole
faithful F2 register: words in ker rho can still differ in that register.

Next compare the joint deck/modular group and its field automorphy with
the source-complete E presentation, then compare the actual geometric
sequence and chosen extension/domain with the same physical parent.
The distinction between holomorphic form, finite-distance spinor and
complete-cusp spinor remains exactly as in the profile-norm checkpoint.
No physical kinetic/action input, Higgs end response, generation count,
SM field assignment, gravity, observer or qualia row is marked paid.

This note is an authored analytical successor, not an independently
verified breakthrough. The frozen v2/v3 scientific controls remain
unmodified and unrun; separate review, main acceptance and the applicable
execution/publication gates remain required. Historical noncompliance
and the old staged phase10 work are preserved, not retrospectively cured.
