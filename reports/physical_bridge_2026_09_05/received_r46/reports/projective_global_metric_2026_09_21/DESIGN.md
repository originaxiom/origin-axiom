# F12: global completion at the exceptional projective parameters

September 21, 2026. Starting checkpoint 08ff88e0, local fork
audit/fork-2026-09-20. No shared B number or remote publication.
Draft resumed September 25 before sealing or execution. Manual pre-run
review corrected the expanded upper-bound polynomial (4c^2+26cw+18w^2)
and kept the real-root counter over Q, distinct from the Q(i)
irreducibility check. These are pre-execution draft corrections.

## Quantifier, prior and two outcomes

This computes the two exact quadratic loci q^2-14q+1=0 and
q^2-34q+1=0 of F10's actual SL4 representation on the figure-eight
member, including both positive embeddings and central fourth-root
characters. The analytic extension statement is scoped to irreducible
flat bundles with these explicit cusp models on the complete fixed
hyperbolic base. Finite-cover consequences are by pullback of an earned
base solution, not by assuming every restriction remains irreducible.
This is not every representation in the arithmetic class, a derivation
of the base or parent action, a chiral index or a full TOE.

Prior: the generated matrix algebra should be all Mat4 at both loci,
and the reference cusp's energy above a sharp universal floor should
be integrable. Neither H0=0 nor scalar commutant alone certifies
irreducibility. If the exact algebra is proper, do not invoke the
irreducible existence argument at that locus; retain the failure and
investigate the invariant structure. If the energy or compactness
argument fails, retain the normalizable-mode result as conditional on
a smooth metric completion, not as an established stationary vacuum.

## Mathematical experiment and conventions

Use the already sealed F10 matrices, q=2t>0, and F11's exact arithmetic
in Q(i)[q]/p. The discriminants 192 and 1152 are not squares in Q(i),
so a nonzero field certificate holds in BOTH real embeddings. Scalar
unitary twists multiply each word by a nonzero scalar and do not alter
the generated algebra. Duality preserves irreducibility; it is not a
flat isomorphism with the original coefficient.

Compute associative-algebra span closure by left multiplication by
both generators, retaining actual word witnesses and a nonzero 16x16
determinant when full. A generic rational-function rank or a modular
sample alone is not the intended certificate. Reconstruct the witness
words directly as a second check. Known full Mat4, scalar, and upper
triangular examples control the instrument in both directions. The
triangular example also has scalar commutant, exposing that shortcut.

H is a positive determinant-one Hermitian metric. The symmetric-space
metric is (1/4) tr(H^-1 dH H^-1 dH), making |dh|^2=|Psi|^2 in a flat
frame; multiplying the energy by an overall constant does not change
the harmonic equation. Use E=integral |Psi|^2, not a residual-square
potential or a claimed finite background norm. On the unit-period
cusp g=z^-2(dx^2+L^2dy^2+dz^2), L>0, k=log q,
c=4 beta^2/L^2, beta=6/(q-q^-1), choose Z>sqrt(c).

Sharp floor: for a unit parallel longitudinal eigenvector with
eigenvalue q^-3, project away the scalar direction. The projector
P-I/4 has squared norm 3/4, and trace Psi=0. Cauchy-Schwarz along
the loop gives integral |Psi_y|^2 >= 12 k^2. This should reproduce
the leading coefficient of the actual F10 norm, not the weaker 9k^2
single-vector estimate. Controls recover the trace-free diagonal
equality and demonstrate the nonintegrable error left by the weaker
floor. Check the exact remaining density, primitive, positivity and
large-Z limits against F10's independently computed matrix norm.

The analytic proof must earn: compact-domain Dirichlet solutions for
the flat symmetric-space bundle; local energy bounds after subtracting
the floor; no target-space escape via the full word algebra; smooth
subsequential convergence; and a uniform bound on target distance to
the exact harmonic cusp reference. Only then transfer F11's L2 result.
Finite symbolic tests are NOT a numerical global PDE solve or peer
review of this analytic argument.

## Prior-art navigation and reading

Queries: already_banked.py 'harmonic metric exhaustion' (121 broad
hits, 2 settled multi-term hits) and 'Ballas irreducible' (34 broad
hits, no settled multi-term hit). Read the full flagged B1220 and
B896 FINDINGS: their exhaustion/harmonics meanings are different.
Read B149 classify_fp.py and the SL4 paper's completeness discussion:
algebra span closure is an existing instrument, not a new discovery.
Reuse F11's field arithmetic, adapting that closure method to exact
quadratic fields. Inspected the campaign, compute protocol, relevant
ladder/framework/lead/law/kill entries and atlas context card. Large
truncated navigation outputs are not complete reading or absence
certificates. No new all-head fetch, population-absence or novelty claim.

Personally read primary HTML: Sagman 1911.06937v3 sections 3.2 and
5.1, especially Proposition 5.1's energy-exhaustion argument; and
Riestenberg--Smillie 2511.11469v3 section 2.3, with Theorem 17's
mean-value statement. The former's main existence theorem is for
SURFACES and is not applied to our three-dimensional domain by name.
The latter records the general CAT(0) Dirichlet/compactness tools;
its new coarse-stability theorem is not invoked here. Proof below
adapts the standard local tools explicitly to the flat bundle and
derives the actual end and representation estimates. No full-paper
read or independent proof acceptance is claimed. No subagents.

Seal this design, proof, code and tests before execution. Preserve
first failures, if any, and separately seal any required correction.
