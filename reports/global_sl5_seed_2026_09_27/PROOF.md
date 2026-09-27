# Algebra and verification scope of the native global seed

## Words and boundary marking

For transversal 1,a,...,a^(n-1), Schreier generators are z=a^n and
y_k=a^k b a^-((k+1) mod n). Every positive edge from coset k to k+1
is named by a^k g a^-((k+1) mod n); negative edges use the inverse of
the preceding positive edge. Thus the rewrite identity a^start w =
rewrite(w) a^finish is an equality in the FREE group, not just in a
numerical holonomy. The n rewritten relators present the cyclic subgroup.

Write W=b a^-1 b^-1 a, WS=a b^-1 a^-1 b, R=a W b^-1 W^-1,
and L=W WS. The relation b WS a^-1 WS^-1 is a cyclic conjugate of
R^-1. Multiplying R by its W-conjugate gives [a,L]. The exact words
in the producer certify this, and the diagram/Tietze check tests that
L is the preferred diagram longitude up to reversal, not merely a
commuting power. All emitted word replacements are identities modulo
one conjugate of R or R^-1. A failed search yields no nonidentity proof.

The quotient G2/G6 is C3 with weights (1,0,1) on the three G2 generators.
Meridian a^2 maps to its generator and L maps to zero, so the peripheral
subgroup surjects onto the deck group and the cusp remains connected.
This concerns the cusped M2/M6, not their Dehn-filled closed counterparts.

## Coefficient field, cocycle and SL5 determinant

The companion matrix Z of 1+x+x^2+x^3+x^4 gives the faithful regular
representation of K=Q(zeta5) on Q^4. A K-linear map of rank r therefore
has rational rank 4r. Exact rational nullspaces and ranks suffice; no
floating or finite-field rank is used. The rational dual representation
is isomorphic to the restriction of the K-dual by the nondegenerate
field-trace pairing, so its divided cohomological dimensions are correct.

For chi=(1,zeta5,zeta5^-1), take c a non-coboundary 1-cocycle with
coefficients chi^2. Then

    rho(g) = [[chi(g), c(g)/chi(g)], [0, chi(g)^-1]]

is a determinant-one representation. The producer constructs c from the
Fox kernel and explicitly checks that it is outside the coboundary image;
it is not read from the source's saved answer. Scalar normalization does
not change its nonzero cohomology class. All global relators are checked.

B is the determinant-one regular representation of the quotient C3.
For E_q=(rho+B) tensor chi^q, det E_q=det rho det B chi^(5q)=1.
On each generator this is an identity over K, not just a norm-one test
on the 20x20 rational lift. The minor construction of exterior-square E
uses its FIVE field coordinates; exterior-square of the rational lift
would instead have dimension 190 and be the wrong coefficient system.

## Global cohomology and duality checks

Fox cocycles satisfy d1 d0=0. Restriction to mu,lambda is the Fox word
derivative and maps coboundaries into boundary coboundaries. The torus
differentials are [(U-1);(W-1)] and [-(W-1),U-1]. The script verifies
these chain identities, computes all kernels and images, and retains

    I = (a1-r1)-(a1*-r1*) = (a0-a0*)+t0*-r1.

It checks r1+r1*=t1 and the full identity independently of the direct
index subtraction. H1 of a presentation complex is H1 of the group;
no assertion about higher cells is needed to compute H0,H1 and the
marked peripheral map. The index's topological interpretation uses
the actual knot complement and peripheral marking, hence Phase A.

For restriction to just the meridian, the target H1 is V/(U-1)V.
Its restriction rank is computed separately. A class trivial on the
whole torus is trivial on each circle, but the converse need not hold:
separate circle coboundaries can require different correcting vectors.
The next relative search must state which peripheral condition it fixes.

## Two independent decompositions on the cover

B restricts to three trivial lines on G6. Hence, as actual G6 modules,

    E_q|G6 = rho_q|G6 + 3 chi^q|G6,
    (wedge^2 E_q)|G6 = 3 rho_(2q)|G6 + 4 chi^(2q)|G6.

The second formula is wedge^2 rho + rho tensor C3 + wedge^2 C3,
then twisted by chi^(2q). It is a DIRECT-SUM statement only for this
native split 2+3 construction. Interior cohomology respects direct sums,
not arbitrary extensions; do not apply this formula to a mixed nonsplit E.
The script compares all five cohomological numbers and their duals, not
only I, against a direct calculation on the seven-generator G6 group.

Separately, relative Shapiro for pullback splits into the three quotient
characters. The paired nontrivial characters are represented over K by
the rational block [[0,-1],[1,-1]]. Since K=Q(zeta5) and the cubic
field are disjoint, conjugation fixing K exchanges them and preserves
each cohomological rank. Half the paired dimensions gives either one.
The direct M6 answer must equal the M2 trivial-character answer plus
this paired answer. No geometric deck projection is imposed physically.

## What a result would and would not establish

All E_q are reducible controls. A nonzero index is ordinary interior
cohomology, not yet a normalizable chiral particle. The irreducible E5
search, a common physical action and its global background, operator
domain, interactions and gravity remain separate obligations. A failed
joint target rules out only the five declared central twists of this
native seed, not all SL5 representations or all sources/end mechanisms.
