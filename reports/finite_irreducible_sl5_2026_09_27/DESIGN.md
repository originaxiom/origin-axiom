# A different global starting point: finite-image irreducible SL5 seeds

2026-09-27, local fork, after b92c2ab7. Seal inputs, proof, producer and
tests before execution. No shared bank number or external publication.

## Why this is not the old local search

The native nonsplit 2+3 seed has no nearby irreducible SL5 representation
at its fixed meridian. Seek genuinely different GLOBAL irreducible seeds
on M2, not necessarily extending to m004. Use the faithful five-dimensional
augmentation representation of even permutations on six letters.

This is a declared change of peripheral starting class: test semisimple
order-three meridians of cycle types (3,1,1,1) and (3,3), not the earlier
J2+1+omega+omega^-1 meridian. The first has the same eigenvalues as that
earlier class, but a different Jordan partition. Both cube to identity
on M6. No assertion of physical selection or of a filling being performed.

Finite-image seeds preserve a positive metric and are self-dual. Their
interior indices are FORCED ZERO. They are prospective starting points
for deformation, not claimed chiral candidates or failed chirality tests.

## Prior work checked

Targeted searches of this fork and pinned main/SM report bodies for the
alternating group, PSL(2,9), deleted/augmentation representations and S6
found no matching common-parent deformation calculation. B719 was read:
its S6/A5 example concerns a different filled manifold and warns against
inferring absence of degree-six covers from homology. Do not claim a
whole-repository or literature novelty certificate.

Primary-source abstract discovery: Boden--Friedl, arXiv:1208.1708,
describes deformation results for certain metabelian finite-image seeds;
arXiv:0803.4329 classifies irreducible metabelian representations.
ONLY abstracts have been read in this step. Those theorems are not applied
to the nonmetabelian permutation seeds here. Morifuji's 2001 publisher
abstract supplies another higher-rank lead, not a read/verified theorem.
The present search and its group/linear-algebra criteria are self-contained.

## Exact finite domain and completeness

Use the already diagram-certified M2 presentation, mu and lambda, with
generators (T,B,C). Fix T to each of the two literal permutations in
INPUTS.json. Enumerate EVERY ordered pair (B,C) in A6 x A6: 360^2 per T.
Evaluate both relators exactly as permutations. No random samples,
first-working-slope breaks, or adaptive stopping. Count the full marked
homomorphism domain, not all SL5 representations or all covers.

For each successful pair, compute its generated permutation group and
test double transitivity on six letters. This guarantees irreducibility
of the rank-five augmentation representation over C. Classify candidate
pairs only up to conjugation by the S6 centralizer of the fixed T. These
are permutation-conjugacy representatives, not a proof of inequivalence
under every complex change of basis. Retain their reproducible IDs.

Analyze the first at most TWELVE sorted such representatives per T by
the exact cohomology producer. This fixed diagnostics budget is declared
before the search. If more exist, print their count and a digest of the
entire representative list; do not call diagnostics exhaustive. If none
exist, close only this finite ansatz and report the zero honestly.

## Diagnostics on each selected actual global seed

- Construct the 5x5 matrices in basis e_i-e_5, determinant one, relators,
  invariant positive Gram form I+ones, and irreducibility criterion.
- Compute the ACTUAL E5 and exterior-square E10 cohomology/duals on M2
  and M6 using the previously sealed exact rational engine. Verify I=0
  as a control, not a non-vacuous physics result. Record interior n too.
- Record the actual longitude, common cusp fixed dimensions and whether
  the M6 E coefficient has capacity at least three. A capacity bound is
  not an index or normalizability result.
- Construct the 14-dimensional Q-self-adjoint trace-free endomorphisms
  of E. They are the deformation directions transverse to SO(Q) inside
  SL5. Compute H1 and restriction to the whole torus and each circle.
  A positive meridian-relative H1 is a FIRST-ORDER candidate only; it
  needs an integrability check. A zero is not silently promoted to a
  classification of distant components or all boundary conditions.

## Controls and reporting

The abelian choice (T,1,T) passes the relators but fails irreducibility.
A fixed triple of even permutations generating A6 passes the irreducibility
criterion; it is a comparator, not claimed to solve the M2 relators.
Check the permutation/matrix functor, the positive Gram form, the symmetric
module's rank and invariant action, and all cohomological chain identities.
Keep first failures; seal corrections separately; record actual exits and
unchanged hashes. No source edits during runs. No physical chirality or
completed TOE claim follows from this search.
