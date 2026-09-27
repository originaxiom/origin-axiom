# Meridian-only relaxation is real, but it does not connect the full nearby SL5 parent

2026-09-27. Seal `bbadd39326cdaa05bf4a23002b2c8d42cbabf95d`.
Native exact test passed. Seven new/post-result tests and the combined
**64-test** suite passed with actual exit zero. All seven sealed sources
and dependencies retained their hashes. No failed run or correction.
The unused GUI warning remains the same. Remote head check `539edb`
found all seven branches unchanged from the pinned comparison.

## Result

The previous audit correctly found a direction missed by fixing the
ENTIRE peripheral pair: the mixed meridian-relative H1 is one-dimensional,
despite zero torus-relative H1. This is not retracted.

However, the active direction connects only rho2 to the deck-trivial
family line. The exact test of ALL links to the other two family lines
has now passed a stronger local criterion:

    E0 = A3 + eta + eta^-1,  A3 = rho2 + 1;
    off-block coefficient rank over K = 14;
    H0 = H1 = 0 in the off-block system;
    fixed-meridian Fox Jacobian: 28 x 28 over K=Q(zeta5),
                                112 x 112 over Q, rank 112;
    exact rational determinant = 8750640431914714140510423543328014336.

The paired nontrivial-family doublet and line modules each have
(a0,a1,t0,t1,r1)=(0,0,0,0,0), also for their duals. Seven trace comparisons
against the actual parent support the explicit Hom-block decomposition.
The exact matrix, not a tolerance on a numerical singular value, supplies
the nonzero Jacobian.

## What this proves locally, with its analytic argument stated

After conjugating the fixed meridian to the seed matrix, its three
distinct generalized eigenspaces give the 3+1+1 decomposition. The
off-block entries of the two relators are a square analytic system in
the off-block entries of the other two generator matrices. Its derivative
is the checked invertible matrix. Setting all off-block entries to zero
solves these equations for EVERY nearby block-diagonal choice.

The implicit-function theorem makes that solution unique nearby.
Therefore every sufficiently nearby representation with this EXACT
meridian conjugacy class remains block diagonal 3+1+1, up to conjugation,
even when the longitude is free. **There is no nearby irreducible SL5
candidate under these hypotheses.** The neighborhood size is not computed;
the analytic argument is authored, not independently referee-certified.
No assertion about all relative components or distant points is made.

Central twists cancel in the parent adjoint action, verified explicitly
on all matrix-unit directions and three generators. The local conclusion
therefore applies to all five central-twist seeds already computed.

## The control preventing a false kill

The older rank-six mixed module has a TWO-dimensional raw fixed-meridian
Jacobian kernel over K. One dimension is residual conjugation preserving
the meridian; after quotienting it, one genuine cohomology direction
remains. The test does not erase it. That direction lives inside A3 and
does not connect A3 to eta or eta^-1.

This distinction repairs the reasoning without turning either conclusion
into a universal negative. "No full-torus-relative direction" was too
strong an input to a meridian-only search. The appropriate full-parent
Jacobian nevertheless rules out nearby irreducibility here for an
independently verified reason.

## A limited count consequence

The two line summands stay finite-order characters in this fixed-meridian
neighborhood and have zero interior index. The active A3 meridian, also
after cubing to M6, has partition (2,1), hence invariant bound two.
IF its global H0 and dual H0 are balanced, then |I(E5 on M6)|<=2.
Reductivity is sufficient for this balance, not assumed for all nonsplit
deformations. Whether any physical energy/domain condition requires it
must come from the chosen action.

## Mission consequence

Keep the exact (0,3) partial positive in the real parent coefficients.
Do not call it complete generations. A small fixed-meridian perturbation
of this seed does not produce the required irreducible common parent.
The next such search must leave this neighborhood, change the stated
peripheral class, or price a different mechanism. This is not evidence
that the whole generated framework fails or necessarily describes nature.

Before a large search, retain the coupled E/exterior-square requirement,
actual deck allocation, and the action-to-physical-spectrum gate. The
ordinary cohomological target is a specific route, not a definition that
every possible physical realization must obey.
