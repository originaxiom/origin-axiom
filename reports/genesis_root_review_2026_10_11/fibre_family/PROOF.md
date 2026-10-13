# A smooth family of the finite distance puncture operators

Authored analytic argument. Independent analytic review remains owed. This extends the specified fixed-fibre realization in ../puncture_fredholm/PROOF.md, not a total-space operator at a degenerating cusp. W46's sheaf sequence and weights are prior results; the contribution here is their graph-domain realization and explicit finite-dimensional reduction.

## The base and coefficient are fixed inputs

Work first over a relatively compact coordinate chart U in the upper half plane. Let pi:E_U->U be the marked compact elliptic family, P its zero section, and X_U=E_U minus P. The coefficient W has the literal three parity-twisted quaternion doublets of the earlier proof, transported by the marking. It is unitary, has puncture monodromy -I6 and determinant-one generators. E0 is the canonical extension with local frame z^(1/2)e; Eall is its upper modification with frame z^(-1/2)e. Each fibre has degrees -3 and +3, respectively.

Use a smoothly varying flat fibre metric initially. The relative odd spin is Srel=pi*lambda^(1/2), after making the coherent square-root choice on the lifted base. This is the trivial odd spin on each fibre but is not to be called a globally constant line on the modular quotient. A smooth family of nondegenerate conformal factors extending across P is also permitted. Such factors and their inverses are locally uniformly bounded on the compact family; an infinite cusp factor is excluded.

All statements globalize on the smooth lifted base only with the coefficient and spin transition maps already specified. This argument does not manufacture a missing descent datum from a list of matrix orders. It uses W21's constant Hodge decomposition and the corrected lifted move action already in B1634. It does not infer constant Hodge type merely from finite coefficient holonomy.

## The critical spin trace transforms without a Hodge half weight

In a local holomorphic vertical coordinate z, the plus critical section has the form

    z^(-1/2) (dz)^(1/2) e u.

Here e is a multivalued flat coefficient frame and u is its critical coefficient. Change coordinates by w=f(z), f(0)=0, f'(0)!=0, with the already fixed compatible square roots. The scalar ratio of the two displayed critical spin frames is

    R(z) = sqrt(z f'(z)/f(z)) = 1 + O(z).

The constant half-weight from the pole cancels that of the vertical spin. The O(z) change contributes only a minimal-domain section: after the radial normalization used in the fixed-fibre proof it is O(r), hence belongs to r^(1/2) H_b^1. The same conclusion holds after a smooth flat-gauge change whose value at P is prescribed. Its constant value is the coefficient transition, not another Hodge power. Compatible square-root signs remain part of the lifted transition data; they cannot be dropped by choosing R independently on overlaps.

Consequently the positive critical quotient for the VERTICAL spin operator is the local coefficient bundle L6 itself. Without the vertical spin factor it would be lambda^(-1/2)L6, the quotient in W46 before its spin twist. This is precisely why adding a trace subbundle Lambda contributes [Lambda], not [lambda^(-1/2)Lambda], to the vertical family index. It does not say that L6 or its transition representation is trivial.

## Local graph trivializations and smooth dependence

Blow up P fibrewise. Choose smooth identifications of the resulting compact surfaces over a smaller U, holomorphic near P, and flat unitary coefficient frames on its angular double cover. The combined spin/gauge frame is periodic. In the normalized dr dtheta density the local operator is the fixed model

    -i [[0,partial_r-i/r partial_theta],
        [partial_r+i/r partial_theta,0]],

up to smooth positive scale factors from the fibre metric. The indicial roots remain sigma=+/- i n, n integer. Thus none hits Im sigma=+/-1/2, and the only critical term is n=0 in each slot. The fixed-fibre cone hypotheses continue to hold; no estimate at a nodal fibre is implied.

Gil--Krainer--Mendoza Proposition3.5 identifies the minimal domain with r^(1/2)H_b^1, and Theorem3.6 gives the finite critical quotient and Fredholm extensions. The weighted Sobolev norm and graph norm are equivalent: the operator is bounded in the first norm, and the closed graph theorem gives the converse. Local coefficient smoothness therefore gives smooth maps from this common Banach domain into L2. Indeed r^-1 Diff_b^1 maps r^(1/2)H_b^1 boundedly into r^(-1/2)L2_b, and the coefficients vary smoothly in the corresponding bounded-map norm. This also explains why pointwise Fredholmness alone is not the argument for family continuity. [Primary source, Section3](https://arxiv.org/html/math/0410176).

Choose smooth orthonormal frames of a fixed-rank Lambda subbundle locally. Cutoff critical sections in Lambda and Lambda_perp vary smoothly. Their sums with the minimal domain give fixed abstract Banach-domain charts, and applying the operator to these sections varies smoothly in L2. For a varying conformal factor use the exact two-dimensional conformal spin transformation from the fixed-fibre proof; both multiplications and inverses are locally bounded and smooth in these charts. Thus the full graded operator and its chiral block form smooth families of Fredholm maps. The full operator is selfadjoint with compact resolvent on each fibre by the earlier Green and compact-embedding argument. No claim of a single spectral gap as Im(tau) tends to infinity is made.

Changing a cutoff alters a section only by an element of the minimal domain. Coherent lifted moves preserve the flat coefficient metric and the Green form, and send Lambda to the prescribed transported subbundle. These facts give graph transition maps; they do not permit transporting Lambda while forgetting its complementary negative domain. For a move-invariant choice the constructions descend on the stated lifted smooth base. On compact subsets a finite chart cover supplies uniform local bounds. The cusp is outside those subsets.

## A finite complex gives the actual index bundle

Write D0^+ for the canonical plus domain, with no critical plus coefficients. Its kernel is zero and its cokernel C has rank three on every smooth fibre by the earlier norm and Serre-duality proof. Smooth Fredholm dependence and constant kernel/cokernel ranks give a smooth cokernel bundle, for example by local spectral projections of the selfadjoint full canonical operator around its isolated zero eigenspace. No global cusp gap is needed for those local projections.

For a smooth critical section u of Lambda, let s(u) be a cutoff lift. Define

    delta(u) = [D^+ s(u)] in C = L2_minus / ran(D0^+).

This is independent of the cutoff and lift modulo the minimal domain. It is an actual operator map, not an identification of bundles by their ranks. It is smooth in the graph charts. Closed range and the bounded inverse of D0^+ onto its range identify

    ker D_Lambda^+ = ker(delta:Lambda->C),
    coker D_Lambda^+ = coker(delta:Lambda->C).

For example, if delta(u)=0, the unique correction v in the canonical plus domain solving D0^+v=-D^+s(u) makes v+s(u) a zero mode. Conversely every zero mode has that critical trace. The cokernel equality follows by quotienting the same target by the enlarged range. Therefore the family index is represented by the finite two-term complex

    Lambda --delta--> C,
    Ind(D_Lambda^+) = [Lambda] - [C].

This remains valid where delta changes rank. It does NOT assert separate kernel and cokernel vector bundles across such a jump. For the all-allowed domain its cokernel is identically zero, so delta:L6->C is surjective and its kernel is a rank-three bundle. For intermediate smooth subbundles one must compute delta to claim separate dimensions.

## The Hodge factors and W46 agree

Denote by T01 the Hodge (0,1) flat triplet in W45's left-action convention, and by T10 its Hodge (1,0) dual/conjugate triplet. These names remove the ambiguity between W21's holomorphic T and W45's canonical H1 T. Their constancy under the supplied move action is the earlier W21 theorem, not newly inferred here.

For the canonical extension, the fibrewise Dolbeault map identifies H1(E,E0) with T01. For the all-allowed extension, multiplication by the relative differential identifies H0(E,Eall) with lambda^-1 T10. These are the parabolic Hodge identifications used in W46. They are compatible over U: in the finite branched cover realizing the finite unitary coefficient they are the usual harmonic/Dolbeault identifications in a fixed isotypic summand. Holomorphic relative one-forms supply the explicit lambda factor. The constant extreme dimensions and the smooth harmonic projections identify the resulting smooth bundles. No intermediate-rank assertion is needed.

Tensoring by Srel gives

    C = lambda^(1/2) T01,
    ker D_all^+ = lambda^(-1/2) T10,
    0 -> lambda^(-1/2) T10 -> L6 --delta--> lambda^(1/2) T01 -> 0,
    Ind(D_Lambda^+) = [Lambda] - [lambda^(1/2) T01].

At the sheaf level the same delta is the connecting map of the puncture modification: applying Dbar to a cutoff polar holomorphic section is the standard Cech-to-Dolbeault representative. Thus the operator reduction agrees with the stated sheaf sequence by a map, not by counting its terms. The sequence is not claimed to split as a flat representation or holomorphic bundle.

The base spin lambda on the open/logarithmic base changes this vertical class to

    [lambda Lambda] - [lambda^(3/2) T01].

For all-allowed Lambda, the same class is [lambda^(1/2) T10]. These are exactly W46's weights, including its overall minus sign for the canonical condition. With the ordinary compact base spin lambda^-5 the formal weights become -5, -9/2 and -11/2, respectively. The cusp_spin_extension packet already describes the extra leading-coefficient conditions when comparing these modular extensions. Nothing in the present smooth-family argument chooses one of them.

## What this earns and what remains

The conditional family-domain step over the smooth base now has an authored graph argument and an explicit finite complex. W46's bundle expression is realized by the vertical Fredholm family, not merely a numerical fibre index. This removes an intermediate analytic assumption within the existing model. It is not a new three-generation result, a solution of Lambda or a derivation of the supplied metric and kinetic field from genesis.

Turning the class into a total-space index still needs a specified horizontal operator, coefficient and spin extensions at the base cusp, and a closed total domain controlling the simultaneous degeneration of the elliptic fibre and the deleted section. Merely applying modular Riemann--Roch to this class is not that proof. A physical use further needs the same-field parent/end/source map and observable interpretation, consistently in the charged slots. Neither the compact silver-cover stationary result nor the complete positive-cusp count is transported into this family by a common occurrence of three.
