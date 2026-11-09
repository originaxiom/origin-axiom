# Exploration audit, preserved positives and required corrections

2026-11-09. Personal source and hand review, with no scientific imports,
test collection or execution. Numerical values below are received saved
outputs. They were not independently reproduced by this seat. Original
source line numbers refer to the .txt-preserved files in received/.

## Verdict and custody

This is useful supplementary evidence for specific finite identities.
The headline that a DSL has certified all theorems exceeds its coverage
and enforcement. Neither that headline nor the source findings below
replace the existing analytical proofs, invalidate all the mathematics,
or establish a physical Standard Model.

All five owner-supplied hashes match. The named standalone commit ad6f2f5
contains seven matching files. The archive head 2f45580 adds four Golden
Spikes files. All eleven match that tree byte for byte. CUSTODY.json pins
the archive, original file names and actual hashes. The three hashes in
the Golden Spikes report's table do not match the delivered script, tests
or JSON. That report says v2 and 4/4 tests, while the delivered suite has
five test methods and the JSON says v3. Preserve both versions' evidence
and regenerate a correctly bound report. This establishes a version
mismatch, not misconduct or evidence of a failed numerical run.

The package supplies saved JSON and reproduction commands. It does not
supply an environment/version lock and successful command/exit/stdout
record bound to these exact bytes, or a complete first-failure chronology.
A Git commit and matching hashes establish custody, not execution order.

## Finite mathematical positives

The main verifier builds sixteen Jordan-Wigner Clifford generators on
256 dimensions, selects the positive half-spinor, and forms 120 exterior-
square plus 128 half-spinor matrices. It reconstructs A, D, H, C and the
compensators instead of importing the OA producer. Its selected group
equalities have a meaningful full-248 target, including signs invisible
in the 120 block alone.

| Claim | What the received source actually checks | Preserved scope |
|---|---|---|
| h1 versus h3 | Full-248 coherent squares, commutator, and the h3 wrong-sign failure | Concrete witnesses within the supplied embedding |
| W f1 | Wrong negative-omega6 expression rejected and corrected positive-omega6 expression compared | Genuine sign repair already independently proved by hand in the prior intake |
| Four phase representatives | Four coherent squares, fixed A3 dimensions 9,9,10,10 and cross-block trace signs | Representative tests supplement the continuous classification proof |
| Repaired k0 and g1 | k_bad retained as a failure, k0=f3 f5 and g1=(f1 f2)s intertwine both named holonomies | Explicit gauge-pair equivalences, with their references transported |
| Register finite image | Generated 2O order 48, parity orbit and stabilizer counts 16 and 8 | Finite quotient controls, not a count of the infinite group E |
| Coherent word control | Four named normal relators evaluated on 248, coherent square relations and XY=D | All-word inference still uses the normal-generation proof |
| Fourth-root bridge | Sixteen character assignments, four restriction fibres and squaring labels | Finite character control supplements the earlier exact proof |
| Weil-5 | Finite base group, projective collisions, parity blocks and selected traces | Projective representation checks and the stated parity-sector comparison |
| Charge-law defect | One gapped S={4,5} counterexample, integer defect products and 80-digit evaluation | This witness, not the complete original defect census |

The saved h1 square residual is about 3.36e-14. The deliberately wrong h3
square has Frobenius norm 16 sqrt(2), about 22.63. If the difference is
twice a unitary on 128 and zero on 120, that norm follows exactly by hand.
The largest saved coherent normal-relator aggregate is about 1.315e-13.
Thus the earlier statement that all central residuals are below 3.4e-14
needs narrowing. These received finite residuals remain below 1e-12.

The lift helper at main-verifier lines356-379 accepts its spin matrix and
16-dimensional vector image independently. It assumes, without checking,
their Clifford conjugation compatibility, evenness and chirality leakage.
The displayed formulas can be checked by hand, but the helper must reject
a mismatched pair before serving as a reusable certificate. An overall
sign change of the vector representative can be a legitimate semispin
ambiguity because its exterior square is unchanged. Do not reject that
case mechanically. No full E8 cross-sector bracket or physical fermion
operator is built by this helper. Neither is needed for these subgroup
word identities, but neither is certified by them.

## Important coverage corrections

1. Main-verifier line964 announces h1 fixing all 48 registered scalar
   states. The following code reconstructs A, D and coherent relators.
   It never constructs Phi0, its 48 flavour transforms, X_z, or their h1
   stabilizer residuals. The original scalar-family hand argument may
   stand. This package does not implement that advertised finite control.

2. The 2O stabilizer enumeration deduplicates solely by its SU2 matrix at
   lines942-945. It should check that a repeated matrix has the same mod2
   action. Otherwise the routine assumes that the paired action descends.
   The two displayed mod2 matrices and row-action comments also use
   transposed conventions. Name and test one convention consistently.

3. Weil-5 collisions remove an arbitrary scalar at lines1150-1151.
   This tests projective consistency. A claim of an exact linear lift
   needs its phase normalization and exact collision control as well.
   The code's scalar-block comparison should also check parity leakage.

4. B1857 is sampled only on the class (m,n)=(1,0), with t=2s and centre
   zero, at 61 points. It checks f(t)=cosh(t)/r. It does not verify the
   general shifted charge-class formula, the complete state/readout
   theorem or all ground-state transitions.

5. The scan ledger prices six supplied candidate run lists. Its cost is
   log2(6), as the JSON correctly reports. It does not price the advertised
   643-candidate search, earlier model choices or choices made outside the
   instrumented call. The 80-digit calculation does not by itself certify
   precision adequacy or implement a precision-escalation comparison.

## Source-proved guardrail gaps

G1. Numerical validation depends on dictionary key names. In
guardrail_dsl.py lines471-498, only keys containing residual, error, diff
or violation receive finite-value and tolerance checks. Bare numbers and
ordinary-key numeric fields have no such checks. The static scanner
does not reject a call to float with a string argument. Consequently
the following source-level counterexample traverses both checks without
a rejection under the delivered logic.

```python
@theorem()
def unvalidated_claim():
    return {"claim": float("nan")}
```

This is an inspected control-flow deduction, not an executed test.
Renaming a checked residual to norm also changes enforcement. Require a
typed claim schema with declared diagnostic fields, numeric domains and
expected relations. Reject missing, unexpected, empty and nonfinite
claim data. Finite output alone still does not prove the right identity
was checked.

G2. The referee decorator does not establish independent reconstruction.
Its AST scan at lines341-392 bans certain names, registered producers and
reflection. Despite its cached-file claim, it does not inspect file reads
or their dataflow. Its runtime checks only top-level ProducerOutputDict
arguments/results. A function returning
json.loads(pathlib.Path("result.json").read_text()) passes the shown
name-based scan and returns an ordinary dictionary. A cached producer
result can therefore be echoed without the special taint type. Identity,
separate authorship and source-complete review need actual provenance
and review receipts. They cannot be assigned by a decorator name.

G3. The RGE wrapper's nonautonomous time conversion is incomplete. It
integrates in tau=Delta ln(mu), multiplies the RHS by s=dv/dln(mu), but
calls that RHS at tau and its RK stages rather than v0+s*tau
(lines1227-1238). For v=2tau and dy/dv=v, with v0=0 and tau from0 to1,
the correct answer is2. The implemented change of variables integrates
dy/dtau=2tau and gives1. This hand counterexample does not affect the
E8 group identities. Autonomous benchmark equations can miss it. The
initial absolute/relative-time convention and all stage arguments must
be specified and tested. The benchmark tolerance also needs an explicit
finite positive range check, since NaN is not rejected by rtol>1e-3.

These findings limit the guardrails' guarantees. Their existing tests
can still catch the eight particular attacks supplied. Do not replace
that scoped positive with either universal robustness or a universal
failure verdict.

## Golden Spikes source findings

The added packet reconstructs useful finite Lie/Koszul matrices, source
phase actions, theta-series samples, affine word products, the 45-D D5
potential, four-cycle matrices and the 20+25 generator split. Preserve
those controls and their saved outputs. Its report's broader certification
claims need the following qualifications.

S1. Lines125-129 assign h0=0 from negative total degree. Lines373-380
similarly return cohomology numbers using degree sign, with a comment
appealing to a maximum principle. These are conditional analytical
inputs, not an independent computation of global holomorphic sections.
Negative degree alone does not force h0=0 for a rank-two bundle.
O(p) plus O(-2p) on an elliptic curve has degree-1 and a nonzero section.
This example is not the specified irreducible unitary parabolic bundle
and does not refute its vanishing theorem. It shows why that theorem's
unitarity, extension, boundary and duality hypotheses must remain explicit.
The formula deg=trace(commutator)//2 is a shortcut for the specified
rank-two peripheral -I case, not a general degree algorithm.

S2. Lines1226-1237 use the wrong area element after defining T=log(1/r).
The cusp measure is dT/T^2 up to the fixed scale/angular factor, not
dT/(T log T)^2. The resulting norm integral has an extraneous
1/(log T)^2. HAND_CHECKS.md derives the corrected expression exactly.
The simple-pole/double-pole convergence verdict survives. The quoted
quadrature values do not verify the physical norm and must be replaced.
The earlier radial quadrature in lines171-192 uses the correct metric
expression and should be retained as a recovery control.

S3. The coupled middle transport at lines1212-1218 supplies a_low and
a_middle directly. It does not derive the six lowering steps from a full
source adjoint action. Calling that a verified transport derivation is
too broad. Keep the supplied phase convention visible or add the actual
operator construction.

S4. The rank-two pole-residue test constructs C from selected finite
brackets and grade tests, then rotates C unitarily. That tests the stated
finite Gram covariance. It does not evaluate global normalized profile
integrals, complete same-pole eigenspaces, Green operators, or all fermion
modes. The source's physical current/domain obligations remain open.

S5. Four-cycle parity is an exact hand matrix identity. The random forty
examples are useful controls. The 20-D subalgebra/25-D coset tests verify
local bilinear intertwining signs. They do not prove that every possible
Spin5 deformation preserves the whole global physical operator, or that
a mixed coset connection is the only possible way to split a spectrum.
Actual flat gluing, antiunitarity, reducing subbundles, derivatives and
domains matter. The physical seat's existing CARTAN_CYCLIC_VECTOR_PAIRING
report gives a stronger but explicitly conditional complete-operator
argument for the particular Cartan-closed cyclic family. Preserve that
positive and its pending review. Do not extend it to arbitrary fields.

S6. The 90 affine words provide finite controls. The all-word characteristic
kernel conclusion also requires that the stated nine generators generate
N, that the crossed homomorphism restricts to an additive map there, and
that the automorphism identities extend through products and inverses.
Those can be analytical deductions. The script alone does not present
the complete proof. A histogram of traces is also not a character table
or, alone, a group-isomorphism certificate.

## Consequence for the physical mission

Keep the corrected coherent alternatives, the fourth-root character
bridge, the scoped parabolic counts and the conditional stationary cyclic
family. The package strengthens selected consistency checks and exposes
a real sign error. It removes no canonical physical input by itself.
It derives neither three complete chiral Standard Model families nor
nineteen measured parameters or gravity.

Use REPAIR_REQUIREMENTS.md for a bounded follow-up. AGY-04a remains the
current author hand task. Source review, scientific execution, formal
independent review, main acceptance and banking retain distinct records.
