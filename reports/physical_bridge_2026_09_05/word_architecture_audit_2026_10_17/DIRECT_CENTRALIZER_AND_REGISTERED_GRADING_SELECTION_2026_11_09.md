# The full centralizer, equal classical minima and a global grading duty

2026-11-09. Author hand derivation, UNREVIEWED and UNRUN. Sources are
the supplied curved action, actual two-triple E8 embedding, full lift,
connected Pin2 construction and the repaired h1 witness. AGY's component
proof at6e9683ab93f438971a0da5b10107acc3cacafc31 is a separate authored
source. This note supplies a direct argument for its global group
reduction and derives the associated action and registering duties.

Use compact centre-free E8 and the actual integer/half-root decomposition
g=e8=d8 plus S+, of dimensions120 and128. Zeta acts as+1 and-1 on those
two parts. Let C denote the source order-four D5 centre element and let
G_c denote the full centralizer of the two ordered compact principal
SU2 triples. C and G_c have different roles in the notation below.

## 1. A direct proof of Z_E8(Zeta)=Ss16

The connected Spin16 image Ss16 fixes Zeta. Conversely let g commute
with Zeta. Its adjoint action preserves d8 and S+ separately and induces
an automorphism of compact d8. Modulo inner automorphisms, type D8 has
its one diagram involution, represented on the root system by an odd
sign reversal of the eight Cartan coordinates. That involution exchanges
the even and odd half-spin weights. Hence it sends the irreducible
module S+ to the inequivalent S-.

But Ad_g supplies an invertible intertwiner on the actual S+ subspace
of e8. It cannot implement that inequivalent twist. Thus its restriction
to d8 is inner. Choose k in Ss16 with the same inner action on d8 and
put u=k^-1 g. Ad_u is identity on d8 and, by complex Schur's lemma,
a scalar c on its irreducible S+ module.

The bracket of two elements of S+ is nonzero in d8. An explicit root
witness uses

    alpha=(1,1,1,1,1,1,1,1)/2,
    beta =(1,1,-1,-1,-1,-1,-1,-1)/2.

Both are even half-roots, their inner product is-1, and their sum is
the integer root(1,1,0,0,0,0,0,0). Their Chevalley bracket is nonzero.
Preserving this bracket forces c^2=1. The resulting adjoint action
is that of1 or Zeta on the full248. Centre-freeness of E8 then gives
u=1 or Zeta, both in Ss16. Consequently

    Z_E8(Zeta)=Ss16=Spin16/{1,omega16}.                 (1)

This uses the source D8/half-spin structure and the standard root
automorphism classification. It supplies the precise group equality
without relying on the unchecked numbering of AGY's Steinberg citation.
It remains an authored proof requiring formal independent scrutiny.

## 2. The two-component conclusion and the relevant group image

The source identity exp(i pi H_+)=Zeta follows on every integer and
half-integer root. Any element of G_c fixes H_+, hence lies in(1).
Lifting to Spin16, commutation with each connected SU2 image is exact.
Any possible lift commutator lies in a discrete central kernel and is
identity at the connected group's identity, so it is identity throughout.

On the real vector16 the ordered SU2 factors act on
(5,1) plus(1,5) plus six trivial lines. Each real5 is the irreducible
spin-two representation. Its nonzero raising string connects its five
weights, so the real intertwining algebra is the scalars. The full
orthogonal commutant in SO16 is therefore

    diag(eps_+ I5,eps_- I5,M6),
    eps_+,eps_-=+/-1, M6 in O6, det M6=eps_+ eps_-.     (2)

This also centralizes the full two Spin5 factors. Lifting and quotienting
by omega16 merges the two equal-sign components and the two opposite-
sign components. The connected Spin6 in the six-space has no intersection
with that quotient kernel. The resulting group has exactly

    G_c,0=Spin6~=SU4,
    G_c,1=h1 G_c,0,    pi0(G_c)=Z2,
    h1^2=Zeta, h1 u h1^-1=tau(u),                     (3)

with tau the six-space reflection automorphism from the witnessed h1.
Its odd-odd product is Zeta tau(u)v. These formulas describe the group
extension explicitly. Identification with a named Pin group needs the
specified square and Clifford convention.

The two principal SU2 images share their centre Zeta. Their joint
image in E8 is(SU2 times SU2)/diagonal Z2. Using that image in the
centralizer is equivalent to using the abstract product acting through
it. It is the joint image which subsequent physical transport must use.

## 3. Every admitted correction gives the same local classical minimum

For h in G_c satisfying the full coherent relation(Ah)^2=K_pi, set
A_h=Ah and B_h=D A_h as in the source. Since h centralizes the ordered
triples, it fixes E,G,H. The same balanced scalar pair

    Phi0=(E,G)/(2 sqrt(2) ell)

therefore glues with the stipulated quaternion flavour holonomies and
these corrected gauge holonomies. It retains the same spin-induced
connection and complete metric in contractible frames. All residuals
in the actual source potential vanish,

    g6^2 V = integral dxdy kappa(
       Omega^-1(|Dbar q|^2+|Dbar r|^2)+2|[q,r]|^2
       +(1/(2 Omega^2))|F+Omega([q,q†]+[r,r†])|^2)=0.   (4)

This is the internal potential per four-dimensional volume in the
specified action. The full unitary transition and complete-domain
conditions are those of the source stationary construction. They retain
their analytical review duties. There is no extra interface or added
background energy in this comparison.

In particular h4 and h1 are two such corrections with V=0. The source
gauge zero-parameter equation restricts parallel unbroken generators to
the pointwise A3 centralizer and then to the flat holonomy fixed algebra.
Its connected algebras here are u3 and so5, of dimensions9 and10.
A gauge equivalence of the full background would conjugate these
algebras and preserve their dimension. The two backgrounds are therefore
distinct, despite their equal classical minimum and local scalar data.

Equation(4) leaves selection among these minima open. Matter backreaction,
the actual full operator, quantum response and registering/source dynamics
can depend on the global holonomies and require their own derivation.
No claim about those contributions follows from the vacuum energy alone.

## 4. A local stabilizer test for a proposed derived orientation

Consider a point-local gauge-covariant construction F from the existing
background fields, their covariant derivatives, metric, adjoints, trace
and flavour epsilon. Include no further oriented internal reference.
In a contractible stationary frame all these input tensors are fixed
by h1. Naturality then requires the output to be fixed by h1 too,

    F(X0)=Ad_h1 F(X0).                                (5)

This holds for a group-valued output with conjugation as well. The
particular oriented element C fails this test, because
h1 C h1^-1=C^-1 and C^-1 differs from C. Thus that oriented element
cannot be recovered from these fixed local inputs by such a covariant
construction. The unordered pair{C,C^-1} is preserved. An additional
reference or actual global relational datum changes the hypotheses
of this local test and carries its own earning duty.

This is a stabilizer/naturality argument applied to this state. It
concerns the local construction just specified. The full generated
register and allowed nonlocal observables retain their wider scope.

## 5. A precise way a registering relation could settle the component

In the faithful adjoint bundle put T=Ad_C. It has the declared order-four
grading on the complete120+128 roster. The bare A and D commute with C.
Equation(3) then gives for the corrected holonomies

    h in G_c,0:  A_h C A_h^-1=C,       B_h C B_h^-1=C,
    h in G_c,1:  A_h C A_h^-1=C^-1,    B_h C B_h^-1=C^-1. (6)

The local spin-induced connection also commutes with C. Consequently a
parallel ORDERED grading T of this stated kind extends over the full
marked carrier exactly in the identity-component case. In the other
case the core loops interchange T and T^-1. The unordered pair still
extends. Its orientation character sends each of the surface generators
a,b to the same nontrivial Z2 element, while their commutator maps to0.

Both cases have the same peripheral Zeta. A cusp-only holonomy test
therefore loses this distinction. The full core transport retains it.
Here a,b are the physical surface generators. Their identification
with native registering operations remains the original priced map.

If the existing registering architecture were to derive such a physical
ordered grading together with its parallel transport and observable
role, equation(6) would discharge this component-selection duty. Merely
postulating T as a preferred reference supplies that duty as an input.
The object-to-register map, reference dynamics, norms and relevant
interactions must earn the stronger premise. Observer and qualia
questions retain their separate mathematical and empirical conditions.

The next task is to identify a source-derived global measuring/reference
map with this property, or retain the allowed alternatives with their
complete physical operators. The two components and equal classical
minima by themselves determine neither a vacuum distribution nor SM3.
