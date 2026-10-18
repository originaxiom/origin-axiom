# Proposed execution boundary and review inventory

October 18, 2026. Author's source inventory, not an independent
source-completeness attestation. SPECIFICATION.json carries exact byte
pins for pre-execution sealing; neither this inventory nor its presence
authorizes execution.

## Local scientific execution

The sole proposed entrypoint is run_checks.py. Before admission it imports
standard-library modules only and checks runtime metadata. After admission
it imports checks.py, which imports controls.py, extended_checks.py and
SymPy. The extension imports the same controls, SymPy and standard-library
arithmetic/test utilities; it loads no additional scientific producer.
The controls
load the retained joined_background.py by its explicit path; that producer
loads cross_branch_positives.py by its explicit path. Both retained sources
have an additional digest check inside the control path. The retained
producer constructs its exact field and matrices afresh. Its script main,
stored spectrum, receipts and historical verdict flags are not executed
or substituted for live arithmetic.

| Local source | Duty |
|---|---|
| run_checks.py | Admission, exact test population, immutable output capture and post-run custody |
| checks.py | Original seventeen controls, with a separate partition-refinement implementation, plus explicit imports of the extension classes |
| extended_checks.py | Eleven controls for fixed/independent lifts, retained registers, limits/weights and graph/cohomology scope |
| controls.py | Word maps, partial-future equivalence, relative-placement and actual-join helpers |
| [joined_background.py](../../joined_background.py) | Existing R85 representation producer, cases and exact field utilities |
| [cross_branch_positives.py](../../cross_branch_positives.py) | Existing R75 symbolic generators, transport and field matrix primitives |

The manifest carries the exact repository paths. There is no data-file
input to these scientific producers. Their chosen
matrices, words, characters and finite test populations live in the pinned
source. CPython, SymPy and mpmath are external runtime dependencies, with
versions and required environment recorded in ENVIRONMENT.json. This is
version pinning, not a reproducible-build hash of the installed packages.

## Existing governance preflight

The entrypoint invokes scripts/gates/prospective.py. Its local code closure
includes gates.py and provenance_policy.py; the ordinary gate aggregate
also uses these existing helpers:

- scripts/checks/check_path_references.py
- scripts/checks/check_test_vacuity.py
- scripts/checks/retraction_sweep.py
- scripts/checks/relay_debt.py
- scripts/checks/doc_currency.py
- scripts/checks/representation_sweep.py
- scripts/views/generate.py

Their local imports and subprocess calls were inspected statically; these
helpers import the standard library and invoke Git, not scientific code.
Their bytes are pinned in the candidate specification. Pinning them does
not assert a new audit of every governance rule's implementation.

The governance data context is intentionally broader than the scientific
input set: policy files, current tracked reports and tests, generated
views, ledgers and Git objects/references. Existing governance scans this
context at the execution HEAD, rather than freezing the repository forever
at the design commit. The prospective schema binds the later independent
review and main acceptance separately. The runner captures the accepted
report and execution HEAD. An independent reviewer must check that this
separation matches the policy and that no scientific dependency is hidden
among these governance inputs.

Although the prospective checker describes itself as read-only, its
existing generated-view gate can regenerate view files before reporting
staleness. Do not run it in the current dirty worktree. A clean dedicated
checkout is required; tracked-state changes must fail admission or the
runner's final custody check. No change to this existing gate is proposed.

## Analytical review, separate from execution

The source-pinned review inputs include TYPED_ARCHITECTURE.md,
JOINING_LAW_ANALYSIS.md, LIFT_SCOPE_NOTE.md, LIFT_FAMILY_AND_REGISTER.md,
INFINITE_HISTORIES_AND_WEIGHTS.md and GRAPH_JOINING_AND_HIGHER_COHOMOLOGY.md,
plus the retained AR and R85/R86 proofs. Their general statements are
not proven merely by a pass on twenty-eight tests. R87's full-parent detector and R88's kinetic transfer
are preserved as distinct prior results, not reverified by this package.

The B144 control proves a limitation of a literal boundary-matrix
inequality using extendable solid-torus reflections. It does not compute
the mapping-class groups of B144's hyperbolic pieces. The B1248 control
addresses a degenerate-locus overstatement; the nondegenerate primitive
commutator law and the homogeneous golden positive are retained.

The extended graph test checks the Mayer–Vietoris rank arithmetic after
the cohomology inputs have been specified. It does not reconstruct the
peripheral embedding, prove asphericity, compute a cellular cup product
or independently establish the B1043 target. The exterior-algebra test
uses small explicit tensors, not E6 matrices or B1043's ten classes.
These limits are deliberate: a general proof review and a genuine
twisted-product calculation must not be replaced by tests of their own
assumed inputs. The latter is a separately designed future experiment.

## Outstanding independent checks

1. Challenge the proof domains, particularly the partial-history quotient,
   integral versus complex equivalence, and which boundary maps extend.
2. Check the science import closure and the declared runtime against the
   sealed bytes, not this author's assertion alone.
3. Review the runner's refusal paths with non-scientific sentinels: missing
   or rejected admission, malformed report, changed source, wrong command,
   output collision, incomplete tests, skips/expected failures and changed
   tracked state must not be accepted as success. Fourteen author-run
   sentinel checks now pass; ENGINEERING_CHECKS.md preserves their initial
   harness failure and correction. This does not replace independent review.
4. Obtain actual non-authoring review and main acceptance as separate
   committed records. Identity and independence require checking; distinct
   labels or commits alone do not establish them.
5. Run only the admitted command in a clean checkout. A source change,
   failed attempt or revised control needs its own preserved successor;
   never overwrite old logs or turn an unrun control into a pass.

No review, acceptance, admission or result file is fabricated in this
draft. Scientific execution remains outstanding.
