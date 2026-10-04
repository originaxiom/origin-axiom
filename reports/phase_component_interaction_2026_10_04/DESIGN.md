# First order matter continuation in the new phase families

2026-10-04. Local branch audit/fork-2026-09-20. Pre-execution design.
The preceding exact three-point calculation found one paired interior E
mode at t=-1 in each of four new families. Test whether that actual mode
continues to first order along t=-exp(z). An isolated rank jump alone
does not decide its first derivative. Prior: uncertain for the new families;
the previously proved zero cubic at the old real t=1 point is a comparator.

## Exact question

Use BOTH seeds, BOTH nontrivial phase components and BOTH actual dual
choices. Work over Q(zeta3), with no numerical differentiation. At z=0
differentiate generator transport as dot A=diag(v) A. Differentiate the
Fox matrices by the product rule, including dot Ainv=-Ainv dot A Ainv.
Independently evaluate Fox derivatives with a dual-number representation.

Let B=d0, J=d1, R=peripheral restriction, and N=ker(J stacked with R).
N represents strict zero-period cocycles. Quotient its boundary-exact
subspace B ker(boundary d0); verify its dimension is t0-a0. The quotient
has dimension n(E), not ordinary H1 and not relative H1 before the
boundary connecting classes are removed.

The ordinary obstruction rank is rank[J, dot J N]-rank J. Also compute
the fixed-peripheral continuation rank with J stacked with R. Keep these
two answers separate. A nonzero latter answer with zero ordinary answer
does not establish the bulk cup product or a physical Yukawa. A literal
nonzero cycle/cokernel pairing must certify any positive ordinary answer.
Raw pairings are basis-dependent and are not normalized couplings.

## Transfer and controls

Check the finite unitary background at t=-1, its unchanged real diagonal
adjoint bundle, nonzero interior exponent class and full-parent projection.
PROOF.md gives the conditional analytic transfer and a compact-support
duality argument. It deliberately does NOT import a charged degree-one gap
or closed range from the other seat's canonical geometry.

Check the complex-linear commutant directly. Together with the already
checked H0 of E, Lambda2 E and their duals this determines the full E8
gauge Lie algebra at these unitary points through the verified regular
branching. This is not a global gauge-group classification.

Controls include all boundary connecting classes, constant transport,
nonzero toy ordinary obstruction, a toy relative-only obstruction and a
quadratic rank jump with zero first derivative. At the new t=1 points
there is no interior E mode; at t=-1 Lambda2 E has none. Recover the old
t=1 zero-cubic comparator separately and retain any disagreement.

## Prior art and evidence grades

R54's complete NEUTRAL_MATTER report and proof at aff8a569 were personally
read on October 4, not rerun or adopted as premises. They use the prior F15
continuation obstruction on a different rank-four canonical background.
The derivative-to-vertex method is credited, not claimed as a new discovery.
This packet tests new rank-five phase data on the supplied hyperbolic model.
R46's report/proof were also inspected; one combined display was truncated,
so no full reading of that proof is claimed. The underlying action was
checked directly in Braun et al. (2.13), (6.2)-(6.5). No Morse source,
associative instanton or compact G2 completion is supplied by that reading.

## Custody

Seal this design, literal inputs, proof, producer, tests and dependencies
in a local commit BEFORE the first scientific import/run. The run tree is
read-only. Preserve first outputs, failures and original sources; separately
seal any repair. Run focused and inherited regression tests, then verify
unchanged hashes and commit receipts. No push, shared B number or main merge.
