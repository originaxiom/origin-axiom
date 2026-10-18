# Separate review intake: changes required, not admission

October 18, 2026. Source-review and verification-infrastructure record.
No scientific execution, canonical amendment or numbered result.

## Scope and custody

The owner authorized separate non-authoring review and coordination with
main. Two separate review lanes, whole_word_proof_review and
whole_word_code_review, returned independently authored reports on the
proposal sealed at `4b0ad6d541133c5ddc39aa07142c1e4bb99032c4`.
The specification digest is
`1b2ba7de9c89c40bc8c4518d75b5dec2263bc636e80b9c1ab27057b3bb2fb304`.
This intake is the author's account of those reports and follow-up
checks. It is not an approval attestation authored by either reviewer.

Both lanes were read-only and ran no scientific imports, collection or
tests. The proof lane read the six requested analytical notes, design
and relevant scope material, then selected original sources and producers.
The code lane read the complete proposed verification sources and the
two transitive scientific producers. Neither claimed to rerun historical
spectra or exhaustively certify the repository. Main must still establish
review independence and accept an exact reviewed successor before
prospective execution. The owner reports main unavailable until
Tuesday, October 20.

The code lane found all 34 design/artifact pins consistent with the seal
and current bytes; it found no undeclared scientific data-file dependency
in the reachable closure it inspected. Both reserved result paths were
absent. The author separately confirmed the verification directory is
unchanged from the seal. The original scientific proposal remains unrun.

## Findings requiring a successor

### 1. Chronological and algebraic register orders were conflated

TYPED_ARCHITECTURE defines a history uv as first u, then v, with action
rho(v) rho(u). LIFT_FAMILY_AND_REGISTER prints

    h(uv) = h(u) rho(u)(h(v)).

That is the correct law for composition-preserving algebraic actions,
rho(uv)=rho(u)rho(v), and likewise for rho'. Equal homology for separately
assigned histories alone does not establish either action property.
Under the declared chronological convention the corresponding law is

    h(uv) = h(v) rho(v)(h(u)).

The proof reviewer supplied a concrete comparator, which the author
checked directly against the displayed definitions. Compare fixed pairs
(L,R) and (L,Rbar), so h(L)=1 and h(R)=b. Chronological LR has
rho'(LR)=Rbar L=I_b R L and therefore register b. Inserting that same
chronological string into the printed algebraic formula instead gives
L(b)=ab. The problem is the undeclared convention change, not a failure
of the cocycle identity under its proper hypotheses. The frozen test
composes Lbar after Rbar and does not resolve this interpretation.

Required successor: declare both action hypotheses and the word-order
convention; retain an explicit translation and a discriminating control.
Do not silently correct the sealed note or its test.

### 2. The clean-state predicate misses a dirty index

scripts/gates/prospective.py:95 and verification/run_checks.py:141 use
`git diff --name-only HEAD --` to support a tree/index cleanliness claim.
The code reviewer identified that this compares the working tree to
HEAD without separately checking the index.

The author independently reproduced the predicate defect in a disposable
Git repository, without executing repository science:

1. Commit a sentinel containing A.
2. Change it to B and stage B.
3. Restore the working file to A while leaving B staged.

The HEAD-to-working-file diff was empty. The cached diff against HEAD
and working-tree diff against the index both named the sentinel; status
was MM. Thus the current predicate can claim a clean tree/index when
the index differs. This reproduction tests the Git predicate, not a full
prospective-admission run.

Required successor: independently check index versus HEAD and worktree
versus index before scientific import and after execution, with a real
Git fixture rather than only mocked dirty-state output.

### 3. Exceptional exits omit final custody verification

The author confirmed the code review's source finding: post-run pin,
HEAD and tracked-state checks occur only after the test runner returns.
The BaseException branch records a traceback and halted event but no
final custody assessment. This does not produce a false pass; it loses
promised evidence for import/collection failures or interruption.

Required successor: best-effort final custody recording on every exit
that can be handled, preserving the original exception and recording any
custody-check failure. Add import-failure and interruption sentinels.

### 4. Reused instrument controls are not reached by this entrypoint

ActualJoinChecks invokes R85 case() for three characters. The existing
singular-intertwiner, proper-algebra, reducible-flag and determinant
controls live in historical fixture/control entrypoints not called here.
The repository does contain those controls; this is not a missing-test
claim. Both author source inspection and the code lane confirm the scope.

Required successor: include the relevant opposite instrument controls,
or obtain explicit evidence-backed acceptance of their reuse. This does
not require claiming that a fresh full spectrum was computed.

### 5. Complementary projective coordinate undeclared in the seal

The proofs use beta=y/(x+y), while the proposed finite controls use
gamma=x/(x+y). Both reviews confirm gamma=1-beta gives equivalent interval
length/nesting, transformed golden polynomial and exchanged chronological
bounds. This is convention debt, not an algebraic contradiction.

Required successor: declare and test the conversion, or use a single
coordinate throughout. The later assessment does not retroactively amend
the frozen declaration.

## Preserved positives and limits

The proof review supports, within their declared conditional domains,
the lift/kernel arguments, infinite positive-direction coverage, pairwise
algebra, B1248 and B144 scope repairs, and the graph-of-spaces H3 argument.
It supports the cubic's sign, not its unevaluated twisted value. These
are source-review conclusions, not fresh numerical certificates or main's
accepted verdict. The review does not invalidate the retained conditional
physical constructions or promote them into a fully derived theory.

A minor terminology correction is also needed: the homogeneous LRL
counterexample has eigenvalues 2 plus/minus sqrt(3). The assessment's
word silver was inappropriate; the updated assessment calls it LRL.

The code lane supports source completeness for the inspected scientific
closure, exact command/output membership, exclusive result creation,
test-population enforcement and skip/expected-failure rejection. Its
ordinary shell did not resolve the declared research environment. The
author separately checked the intended interpreter's metadata: CPython
3.12.1, SymPy 1.14.0 and mpmath 1.3.0. No scientific package was imported;
this metadata check is not an environment execution certificate.

## What the owner's clarification changes

The finite graph theorem starts with specified vertices, edges and
interfaces. It does not derive the allowed graph/interface architecture
from the foundation. This limitation must not be restated as a demand
to select one privileged global carrier. The owner's target is the whole
allowed interacting architecture, with non-cancellation as its proposed
reason for emergence; see GOAL_CONTRACT's owner-clarification section.

The earlier selected-assembly wording in the assessment was corrected
in `fcf3303fe`. The sealed JOINING_LAW_ANALYSIS retains historical wording
about a selected joining arrangement; that wording is scoped by the
clarification, not silently edited. Conditional composition and joining
are infrastructure for the stronger question, neither its completion
nor a no-go theorem about it. The act and its registering relation remain
part of the intended object of study.

## Disposition

Changes are required before recommending execution of this exact
proposal. Preserve the original seal, failed assumptions and unrun
status. Prepare a separately sealed successor addressing these findings,
obtain its separate review and main acceptance, then seek prospective
admission. No reviewer approval, receiver acceptance or admission record
has been manufactured. This intake and the owner clarification are local
checkpoints, not a publication or full-suite certificate.
