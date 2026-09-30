# What a global common-parent candidate would have to do

## Hypotheses, not a candidate

Let H=pi1(M6) be a normal subgroup of G=pi1(M2) with G/H=C3, and take
the finite cover of pairs (M6,T6)->(M2,T2). The peripheral map sends mu
to a generator of C3 and lambda to zero; there is one cusp upstairs.
Let E be an irreducible complex rank-five G module with meridian
diag(J2(1/3),P3). Let chi be the corresponding cubic deck character.
No such irreducible global E is supplied by the boundary model.

The notation fixes the same topological cover relation as the handoff,
not a proof that a newly proposed representation satisfies its relators.
As everywhere in this gate, I denotes ordinary interior cohomology.

## 1. Irreducibility and global H0

Restrict a finite-dimensional irreducible G module to normal finite-index
H. Choose a minimal nonzero H submodule. Its G conjugates span the whole
module by G irreducibility, and their sum is semisimple as an H module.
G acts transitively on its H-isotypic components. Here their number is
one or three, since G/H is C3. Three is impossible in dimension five.
Thus restriction is W tensor C^e, for irreducible H module W.

A lift t of the cyclic generator preserves this isotype and acts as
S tensor A: S intertwines W with its t-conjugate, and the remaining
factor acts on the multiplicity space. Over C, A has an eigenline; W
tensored with that line is stable under H and t, hence under G. G
irreducibility forces e=1. Therefore restriction to H is irreducible.

E tensor any line is also irreducible, nontrivial rank five, so its H0
and its dual H0 vanish, both downstairs and upstairs. Moreover a nonzero
invariant element of exterior-square E tensor a line would give a
nonzero equivariant alternating map E* -> E tensor that line. The two
rank-five modules are irreducible, so such a map must be an isomorphism.
But an odd-dimensional alternating matrix has determinant zero. This is
impossible. Apply the same reasoning to the dual. Thus the exterior-square
twists also have balanced (indeed zero) H0, without assuming they are
themselves irreducible.

## 2. The full relative complex splits, not just its dimension

Finite-cover transfer and the projection formula identify the relative
and absolute cochain complexes upstairs with downstairs coefficients

    E tensor C[C3] = direct sum (E tensor chi^k), k=0,1,2.

These identifications commute with the relative-to-absolute and boundary
maps. Therefore they also identify their images, yielding

    I(M6; E restricted to H) = sum_k J_k(E),
    J_k(E) = I(M2; E tensor chi^k).

The dual of the k-th coefficient is E* tensor chi^{-k}; summing all k
also gives the corresponding upstairs dual count. This explains the
inverse-character convention, rather than silently pairing equal labels.
Everything here applies as well to exterior-square E. Exterior square
is taken BEFORE the regular-representation decomposition; one must not
replace it by the exterior square of the rank-fifteen pushforward.

## 3. Necessary allocation for a target three

By balanced H0 and the verified meridian fixed-space bounds,

    |J0(E)|<=2, |J1(E)|<=1, |J2(E)|<=1;
    |J0(wedge^2 E)|<=3, |J1(wedge^2 E)|<=2, |J2(wedge^2 E)|<=2.

If the upstairs E index is +3, the only possible triples are

    (1,1,1), (2,0,1), (2,1,0).

For -3 their negatives are necessary. These are integer capacity
constraints, not a sufficiency statement or an actual class count.
No physical significance is assigned to the number of allowed triples.

The two nontrivial E twists see a simple meridian eigenline. A commuting
longitude acts on it by a scalar; for it and its dual the common fixed
space is simultaneously dimension one or zero. If J_k=+1 in either of
these sectors, both have t0=1 and the full identity forces r1=0, r1*=2.
This is a sharp target for the global boundary restriction calculation.
The toy longitude satisfies the invariant condition, not the global
cohomology/rank condition. A different commuting longitude can remove it.

## 4. Conditional arithmetic simplification

If E is defined over a coefficient field K and K(omega) has an automorphism
fixing K and taking omega to omega^-1, applying it to the finite cochain
matrices and boundary maps preserves all ranks, and sends k=1 to k=2,
including the dual coefficients. Hence J1=J2. Under this EXTRA hypothesis,
the +3 distribution must be (1,1,1), and the -3 distribution (-1,-1,-1).

In particular a real coefficient model satisfies the conjugation version.
A general complex or Q(omega) model need not. This is Galois rank
invariance already used in B1297; it does not make E self-dual and does
not force J to vanish without that further condition.

## 5. Descent is not a harmless relabeling of three generations

Ordinary geometric C3-invariant cochains pick the k=0 summand. Their
interior index is J0, with absolute value at most two for E. Thus the
target-three candidate on M6 would lose that target under THIS invariant
projection. At least one nontrivial deck-character contribution is needed;
under the arithmetic hypothesis both are needed with the same sign.

This does not forbid charged representations of a finite gauge group,
compensating fiber actions, or additional twisted-sector fields. Those
are different models/domains and must be specified in the action. Nor
does a representation on M2 imply that physical space must be its quotient:
it can furnish a deck-compatible background on M6.

## What remains physically decisive

A certified global representation must first realize the coupled E and
exterior-square targets, not just the inequalities. Then the same parent
action must determine a background metric/fields, norm and operator domain,
the interpretation of deck transformations, and the actual chiral spectrum.
This application of elementary finite-cover algebra supplies search
constraints, not those missing ingredients. Proofs are authored, not an
independent specialist review; tests below check only finite comparators.
