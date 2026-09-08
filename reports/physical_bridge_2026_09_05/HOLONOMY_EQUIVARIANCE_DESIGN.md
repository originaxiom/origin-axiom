# R20: source symmetry and the global form of the flat connection

2026-09-08. Pre-execution design; path-local R20, no global B number.

BANKED IDENTITY: R15's m202 order-three cusp maps and three proper
fixed-source arcs; the physics seat's R72b explicit automorphism
a->B, b->aB, pinned at 659487bb, are prior work. R19 at 5952328d
already proves the full rank-one character spectrum and E6 cocharacter
period. B960 already distinguishes the fundamental 27 from adjoint
representations of E6/Z3. Reuse those results at their actual scope.

PRIOR ART: SnapPy 3.3.2 primary documentation, read 2026-09-08:
https://snappy.computop.org/manifold.html#snappy.Manifold.canonical_retriangulation
and https://snappy.computop.org/triangulation.html#snappy.Triangulation.isomorphisms_to.
Verified canonical retriangulation plus complete combinatorial
automorphisms certifies the isometry enumeration. Cusp matrices act
on columns. These tools do not certify source dynamics or a physical
gauge lift. Root/coroot lattice membership is tested using R19's actual
Cartan matrix, not a group name or an adjoint phase alone.

P0: the SAME prescribed m202 three-proper-source, strong maximal
complex, with commuting scalar holonomy in exp(2*pi*i*R*u),
u=omega_1^vee. Test invariance under the source's order-three isometry,
and separately the complete isometry group when the source densities
are invariant. Compare simply connected compact E6 and E6/Z3 explicitly.
Not a statement over the whole relational object, all flat E6
connections, all gauge lifts, or all source theories.

P1: PB-BOUNDARY / X33, the next R19 duty. This tests a hole within our
candidate construction before widening it. No original failure is
deleted, no physical absence is inferred from a lexical miss.
P2/P3/P4: HOLONOMY_EQUIVARIANCE_PRIOR.md records the all-head fetch,
atlas/bank checks, actual R72/R72b body/source/run and B960 body read.
B955's rank preservation is retained; its nonabelian hatch stays open.
The 27-specific B960 restriction is not generalized to all matter in
the adjoint-origin construction. R19's anomaly and neutral-cusp duties
remain regardless of this result.

P6: expect a MIXED result. The C3 action on H1 should leave precisely
three adjoint characters: trivial and a conjugate pair of order three.
Expect the pair to be off R19's exceptional locus and hence three/zero.
But in the simply connected parent the scalar circle has period THREE
in u units. Expect its C3-invariant points to be central and therefore
adjoint-trivial: the pair-free adjoint characters should have a central
equivariance obstruction for all nine scalar parent lifts. In E6/Z3
the period is one and the pair should be permitted. Expect the full
sixfold symmetry (and hence full D6) to fix only the trivial scalar
character. These are constraints on symmetry-preserving vacua, NOT a
no-go for symmetry breaking, noncentral transport or other completions.

## Geometry and exact action

1. Build the VERIFIED canonical retriangulation in Sage. Enumerate its
   combinatorial self-isomorphisms. Transfer cusp maps back to the
   original m202 peripheral basis through an EXPLICIT combinatorial
   isomorphism Q->K; never assume a canonicalization preserved labels.
   If no such map is available, fail this instrument and retain the
   failure rather than guess a basis or assert nonexistence.
2. For each original cusp let B_c have columns equal to the meridian
   and longitude exponent vectors in the original a,b presentation.
   Derive A B_c = B_sigma(c) M_c. B_0 is rationally invertible here;
   require A integral/unimodular and the second cusp equation exactly.
   Enumerate all twelve A's, their group closure, element orders,
   orientations, cusp permutations, and C3 normality. Count uniqueness
   explicitly; if H1 is not faithful do not use its orders as isometry
   orders. The source C3 should have two nonidentity elements.
3. Independently verify the R72b free-word substitution a->B,b->aB:
   its third power is identity on both generators; its relator image
   is freely conjugate to the original relator or its inverse.
   Compare its exponent matrix to the certified geometric action.
   This reuses an earlier explicit map, not an invented isometry.
4. m004 is a geometric comparator: its verified canonical
   self-isomorphism count should be eight, excluding order three by
   Lagrange. Do not infer any general chirality theorem from that.
5. Use two canonical-certification precision requests, 100 and 212
   bits, and compare the entire action sets, not just the group orders.

## Characters, parent lifts and two-sided controls

Write h=(h_a,h_b)^t and rho(g)=exp(2*pi*i*u*(n(g).h)).
The pullback is A^t h. In a circle of period p, invariance is
(A^t-I)h in p Z^2. For det(A-I) nonzero, every fixed point has
coordinates in p/d Z mod p, d=abs(det(A-I)); finite enumeration
therefore exhausts ALL continuous characters, not a sampled grid.
Verify count d, and intersect with every group action for full invariance.
Controls: inversion gives four two-torsion points; identity is rejected
as a finite enumeration (its fixed locus is continuous).

Compute R19's exact relative cohomology at each C3-fixed ADJOINT
character, not an Euler shortcut. Check all group actions preserve the
normalized Alexander polynomial. Record the stabilizer and orbit of
each fixed character and the order-two example used in R19.
These are bundle symmetry groups; NO orbifold quotient/projection is
performed, and an equivariant bundle's full kernel is not identified
with its invariant subspace.

For p=3 compute every C3-fixed scalar simply connected parent
holonomy and its adjoint phases. For each p=1 fixed character enumerate
all nine lifts h+(i,j), i,j in {0,1,2}, modulo three. Keep the exact
central defects (A^t-I)h mod 3. Cross-check with all E6 roots and
fundamental-27 weights: a defect can vanish in the adjoint and fail
on the 27. A false period-one parent control must be caught.
Verify 3u is a coroot-lattice vector, u is not, and u is integral
against all roots. Thus p=3 versus p=1 is earned from the actual
lattices. The sourced adjoint spinor sectors descend in the adjoint
parent because the entire 78 does; a fundamental 27 does not.

## Analytic and physical interpretation owed

The fixed arcs are pointwise fixed by C3. Averaging the scalar solution
over C3 preserves their specified densities, strong asymptotics and
field equation. The average therefore allows a C3-invariant dF.
A gauge lift preserving phi=u dF must centralize u wherever dF is
nonzero; it then commutes with EVERY exp(t*u), so cannot remove a
central holonomy mismatch by conjugation. This obstruction is scoped
to the scalar transport ansatz and this fixed signed Higgs field.
An outer action or sign reversal changes the declared problem, and a
noncentral connection is not tested here.

Since C3 has fixed points on the undrilled Q and A extends across the
sources, invariant rank-one characters have an equivariant lift via the
based semidirect product; the fibre action still has three possible
C3 phases. Invariance is compatibility, NOT physical selection.
Requiring invariance is itself an extra condition unless dynamics
demands it. A symmetry may instead permute vacua.

Preserve R19's anomaly (48,48,6), non-normalizable holonomy variations,
and R17's neutral cusp channel. Do not invent anomaly cancellation,
a physical mass or a selected global gauge form. The next investigation
must construct consistent transport/defect dynamics, not label these
conditional kernels a complete physical theory.

Seal design, summarized prior receipt, source and tests, and verify
provenance/digests BEFORE execution. Keep the tree read-only throughout
scientific/certifying runs. Preserve failures in new artifacts; repairs
require a separate sealed control, not edits to original assertions.
