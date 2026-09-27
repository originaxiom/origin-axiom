# Three upstairs needs a specified deck distribution, not three copies by declaration

2026-09-27. Second seal `655017f18e24d1e8a215146be15a42f9dc113492`.
Exact native comparators passed, nine new tests passed, and the combined
**41-test suite** (17 boundary + 9 deck allocation + 15 parent) passed with
actual exit zero. All six sealed files/dependencies retained their hashes.
No failed run or source correction. This is focused verification, not
whole-project certification or an independent review of the general proofs.

## New constraint on the actual global search

Conditional on finding one irreducible rank-five E on M2 with the proposed
2+3 meridian, its pullback to M6 remains irreducible. Both E and its
exterior square, with any line twist, have zero global invariant vectors
and zero dual invariant vectors. The odd rank is relevant: an invariant
alternating bivector would have to define an invertible alternating 5x5
map, which is impossible. The argument is in DECK_PROOF.md.

Consequently the balanced bounds apply to the actual candidate, without
assuming that all nonsplit representations have balanced invariants.
Relative Shapiro gives

    I_up(E) = J0(E) + J1(E) + J2(E),
    Jk(E) = I_down(E tensor chi^k),

and the same formula for exterior-square E. The dual of the k-th summand
uses chi^-k. Boundary capacities are (2,1,1) and (3,2,2), respectively.
The complete possible E triples with sum +3 are therefore

    (1,1,1), (2,0,1), (2,1,0).

These are **necessary integer distributions, not discovered cohomology
classes**. Under the additional hypothesis of a coefficient-field
automorphism fixing E and inverting the cubic root of unity, J1=J2,
leaving only (1,1,1). A real coefficient model satisfies that hypothesis;
a general Q(omega) model need not. Negative target three has opposite signs.

For either nontrivial E deck twist to have J=+1, its simple meridian
eigenline must also survive the actual longitude, and the global
restriction-map ranks must be r1=0 and r1-dual=2. This is a concrete
cohomology target, not supplied by the boundary-only example.

## What the exact local comparator verifies

On E tensor the regular C3 representation, ordinary geometric deck D
has D^3=1, while the unipotent holonomy transport still does not cube to
one. The boundary transfer has dimension 4 on E and 7 on its exterior
square, equal to 2+1+1 and 3+2+2. The D-invariant portions have dimensions
2 and 3. These finite matrix identities reproduce the general transfer
mechanism for the declared boundary pair; they do not supply global
relators or the index itself.

A different exact commuting longitude removes both nontrivial E twist
invariant lines. Thus a meridian-only search that never checks the
longitude can miss precisely the two contributions needed for the
arithmetic (1,1,1) distribution.

## Physical consequence, carefully delimited

Ordinary geometric invariant projection retains J0, at most two for E.
It therefore cannot retain an upstairs target three in this model. This
does NOT exclude charged states of a finite gauge group, a compensating
fiber action, or extra twisted sectors: none is the same projection, and
each needs its own action/domain. Nor does using a representation on M2
force physical space to be M2; it can supply a compatible background on M6.

This is why choosing "cover" versus "quotient" cannot be postponed until
after a desirable count appears. The physical interpretation must be
declared before that count is claimed as generations.

## Status and next milestone

The principal-cusp false lead has been separated from the live cover
boundary class. The global irreducible search now has an explicit coupled
coefficient and deck-character target. It remains a mathematical search,
not a derived physical phase. The global representation, its joint
interior indices, harmonic/background existence, physical norm/operator
domain, mirror removal and observable predictions are all still open.

See NEXT_GLOBAL_SEARCH.md for the next input contract and stop rules.
