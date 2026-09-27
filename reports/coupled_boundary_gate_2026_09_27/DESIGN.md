# Coupled boundary admission for the actual parent coefficients

2026-09-27. Local fork only; no shared bank number. This design, proof,
literal inputs, producer and tests must be committed before execution.

## Question and scope

Can the proposed peripheral classes support algebraic interior index of
absolute value three in BOTH E and exterior-square E, the rank-five and
rank-ten charged coefficients of the verified adjoint E8 parent?
This is a necessary-condition screen, not a construction of a global
representation, physical background, zero-mode spectrum or TOE.

The ordinary relative-cohomology index is used. No identification with L2
cohomology or physical chirality is assumed. A boundary upper bound passing
does not establish that its value can be attained. The global H0 terms are
retained, including for nonsplit modules.

## Prior record, read personally

- Main 987c0c8f, B1297 FINDINGS section 2 gives the full index identity;
  its September 16 addendum retains nonsplit positive examples. The phrase
  "interior = L2" in the original is NOT imported without analytic hypotheses.
- SM branch 9f9a0751, B1377 gives a different rank-two extension bound;
  it is not a bound on every rank-five parent.
- The September 27 corrective handoff's parabolic-cusp report and NEXT_TEST
  distinguish a principal Sym4 control from a desired 2+3 meridian whose cube
  is J2 plus three trivial directions. They do not give the full longitude
  of a global representation. Its suggested relative search is not a result.
- September 25 m6_physical_gate REPORT section 6 already computed the
  nilpotent partition kernel counts and warned that they are not generation
  counts. The partition table here is an independent comparator, not a new
  discovery or a demand that both local kernels equal three.
- This fork's parent-admission result 9cb1fd6b fixes E, exterior-square E
  and the hypercharge exponents. Its rank-six obstruction is not a bound
  on the number of cohomology classes in E.

A targeted body search of B findings/reports on the pinned main and SM
heads found no explicit version of the coupled bound below. This is not a
whole-literature absence or novelty claim. Remote heads were rechecked over
HTTPS with per-command global/system URL rewrites disabled; all seven
advertised heads match the prior assessment. No persistent config changed.

## Pre-execution discriminators

1. Re-derive the identity with unequal a0 and a0-dual. Distinguish a
   balanced-H0 bound from an unconditional bound. For one principal J5
   meridian predict |I(E)| <= 2 even without H0 balance (<= 1 with balance).
   Thus this peripheral class cannot support the algebraic target three.
2. Independently calculate exact fixed-space dimensions for E and its wedge
   square, their duals, and Hom(3,2). On the 2+3 meridian predict quotient
   dimensions (2,3,1) and cubed-cover dimensions (4,7,3). These are meridian
   bounds, with equality only on an explicitly declared compatible toy
   longitude. They are not a global M2/M6 representation.
3. For the quotient, balanced-H0 rank-five bound two excludes target three;
   WITHOUT balance the bound is four and does not exclude it. On the cover,
   bound four with balance leaves the target open. Neither is existence.
4. Reproduce all seven unipotent rank-five partitions, with wedge dimensions
   independently predicted by an sl2/Jordan formula. This must reproduce
   the known fact that no pair of local kernel dimensions is (3,3).
5. Test cubic scalar meridian twists exactly over Q(omega) represented as
   two-dimensional rational linear algebra. Prove separately that any
   nontrivial scalar twist of a unipotent meridian kills its invariants.
   The condition on an upstairs character is not a condition that its
   downstairs character be trivial: a cubic downstairs phase can pull back
   to one. Hypercharge exponents refer to one common line, not five free lines.
6. Countercontrols: a commuting longitude must sometimes reduce the
   meridian fixed space; two commuting unipotents must sometimes have
   unequal fixed dimensions in V and V-dual. The test must catch silently
   setting these equal or importing the mixed rank-six count into E.

## Exactness and stop conditions

Use rational matrices and exact SymPy rank, never floating rank. Wedge
matrices use explicit 2x2 minors. A separate Jordan-block count checks the
seven unipotent cases. All inputs are literal in INPUTS.json. Assert the
cover cube, commuting pairs, determinant one, dual consistency and induced
wedge functoriality. Keep first failures and seal corrections separately.
Only actual terminal exit zero constitutes a completed run. Save commands,
outputs, hashes and exit status; focused tests do not certify the whole repo.

No global relative-character search or physical PDE is authorized by a
passing dimension screen alone. The next design must specify E and wedge E
together, actual longitude, global H0, cover/quotient, and action/domain.
