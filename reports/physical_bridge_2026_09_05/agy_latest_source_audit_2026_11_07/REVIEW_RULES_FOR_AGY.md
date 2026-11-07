# Preventing these errors: evidence rules with concrete countercontrols

2026-11-07. Proposed review contract, derived from the accompanying audit.
This is guidance for AGY and receiving reviewers. It does not silently
amend repository policy, certify existing code, or admit a scientific run.
Implementation belongs in a separately sealed and reviewed change.

The objective is to stop a generated claim being promoted when its evidence
does not support it. No prompt, model or test suite guarantees mathematical
truth. A gate must inspect evidence that the claim's author cannot replace
with a reassuring Boolean.

## 1. Preserve the mathematical object and every joining map

For each claim declare: carrier; marking; coefficient representation;
spin/lift; fields and action; operator and domain; normalization; and
physical measurement map. Use "not applicable" where appropriate, with a
reason. Every change of object needs its actual intertwiner or construction.
An equal number is not that map.

Required failure examples:

- Substitute ordinary `A-I` homology for the mirror-twisted `A+I` carrier.
- Keep the correct orbit count but replace its eigenvectors by `(1,0)`.
- Transport a torsion point but leave the modulus/operator/spin unchanged.
- Reuse a compact-domain or periodic-end kernel result on a different end.

The checker must reject these joins. This does not reject either component's
standalone mathematics. Claim dependencies should say which joins remain
supplied, so the same missing map is not hidden in several later theorems.

## 2. Verify the witness, not just its dimension or determinant

Counting a four-point kernel is insufficient if later code computes on
specific representatives. Require the claimed points themselves to satisfy
`Av=-v mod N`, and require the actual function to consume those same points.
For a marking move, compare the full transported observables, including
the measuring fields. Do not test only an invariant that discards the datum
under dispute.

Mutation: an incorrect point with the right order and the same count must
fail. Acceptance of that mutation means the control is not discriminating.

## 3. One-factor comparisons must change one factor

List the independent inputs and the permitted changes before an ablation.
Have an external comparison record the actual changed values. For the phase
question use separate geometric-phase and Weil-phase switches and a 2-by-2
table. Turning both off must be labelled a joint removal.

Mutation: a helper that silently sets `zeta5=1` while purporting to change
only Re(tau) must be rejected. A zero output from two identical real matrices
does not establish a causal mechanism.

## 4. A texture, an overlap and a physical coupling are different objects

Every alleged Yukawa matrix must have a traceable producer. If the claim is
physical, require the declared action, normalized field modes, common
left-handed transport and the interaction integral. A hand-built matrix
can be a useful control when explicitly labelled as such.

Mutation: replace a physical producer by a matrix with convenient powers
of q. Its singular values and unitary invariance may still be correct; the
physical-derivation gate must nevertheless reject the identification.

For a negative, remove one assumption in thought before claiming a no-go.
`Yd=conj(Yu)` forces symmetric mixing magnitudes under its common-frame
hypothesis; it does not eliminate every two-flank sewing. Conversely an
arbitrary new sewing matrix must be priced, not called a derived escape.

## 5. Give evidence a type; do not let names certify it

Use distinct statuses for: definition; supplied input; hand proof; imported
result at an exact pin; new recomputation; numerical consistency check;
interval certificate; non-authoring review; and admitted execution.
An internal alternate-precision check is not a non-authoring reviewer.
An imported high-precision decimal is not a certified interval.

The record of a pass should be emitted by the external runner from actual
assertions and logs. Reject author-assigned `independent=True`,
`source_complete=True`, `no_data_looks=True` or `all_guardrails_passed=True`
as evidence by themselves. Preserve useful internal checks under honest
names. Do not confuse verification of schema with verification of truth.

Mutation: replace a computation by a literal equal to its old output. A
fresh-recomputation claim must fail even if the resulting number agrees.

## 6. Every universal claim needs its quantifier and completeness argument

State the sampled population and the all-object theorem separately. Finite
tests may support a proof; they do not replace its induction, bound, exact
classification or exhaustive certificate. Record degeneracies and exceptions.

For sums declare the ensemble, multiplicity, equivalences, measure and
convergence. A single-run partition sum plus two example clusters is not
the entire weave. A least individual action is not its normalized probability.

Mutation: add an allowed gapped history outside the sampled range. The
framework must suspend the universal promotion unless its proof covers it.
Retain the corrected lcm>=12 counterexamples; never generalize a finite
minimum back into their refuted depth law.

## 7. Charge every selection to its actual premise

List supplied inputs before and after the argument. Imported SM hypercharges
cannot then count as a derived SM field assignment. A selected level-five
register, a field dictionary, a readout state and a measure are independent
until the relevant maps/equations identify them.

Where multiple choices are permitted, retain the family or distribution.
Do not force uniqueness to make a parameter-free headline. Symmetrization
removes a choice only after checking the full observables and interactions.

Mutation: change the carrier to another allowed word, or change a physical
field norm while retaining the same representation name. A root-specific or
unnormalized conclusion must not survive as an architecture-wide prediction.

## 8. Regression tests must follow the corrected science

Keep historical wrong computations as labelled known-error controls. They
must not remain the condition for a successful physical prediction. The old
Higgs test still checks a good agreement from a rate explicitly acknowledged
as buggy; that agreement is history, not a surviving accuracy claim.

Use separate expected outcomes for the corrected calculation, the preserved
legacy bug and the physical claim. A correction can invalidate a prediction
without invalidating every structural theorem in the same file.

## 9. Review a small packet independently before aggregation

Replace a monolithic "complete TOE" certification with bounded units that
declare one question, exact dependencies, nontrivial countercontrols,
expected outputs and open physical identifications. Seal source-complete
designs before execution. Keep failures; correct at a new version.

A non-authoring reviewer must reproduce the reasoning independently enough
to challenge the shared premise. Reusing the same helper at higher precision
is numerical checking, not independence. Cross-seat agreement that copies
one input is not two derivations.

The author cannot grant itself banking, execution acceptance or main review.
Main being unavailable leaves that status pending. Already authorized
source/hand review and reversible repairs can continue without repeatedly
asking the owner for routine permission.

## Immediate repair order

1. Correct Theorem 141's carrier and Theorem 145's actual point/marking join.
2. Separate Theorem 155's two phase controls; label its texture honestly.
3. Pin imported geometry and distinguish its numerical and exact components.
4. Carry forward current main/explore rulings, with their unverified parts
   visible; retain useful positives and localize every negative.
5. Build the discriminating checks above under the existing scientific
   verification process. Add them to enforcement only after showing that
   each deliberately wrong version is rejected for the intended reason.

This is how the model learns a practice: the same mistake repeatedly fails
an external check, and the repair changes its reasoning and evidence.
Adding another page saying "be rigorous" is not the enforcement mechanism.
