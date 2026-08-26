# Closure-ledger schema

Each canonical item is represented by these fields:

| field | meaning |
|---|---|
| `campaign_id` | stable `OA-C####` identifier assigned only after deduplication |
| `canonical_key` | semantic tuple `(object, requested operation/morphism, yes/no criterion)` used for deduplication |
| `aliases` | every branch-qualified source occurrence: repo, ref, commit, blob/path/line, declared ID, and role |
| `question` | one mathematically typed proposition or construction request |
| `domain` | `genesis`, `carrier`, `arithmetic`, `lie`, `geometry`, `qft`, `spectrum`, `vacuum`, `flavor`, `values`, `process` |
| `kind` | theorem, existence, uniqueness, computation, literature, empirical, repair |
| `sources` | exact repository/branch/path/line anchors |
| `deepest_artifacts` | scripts, data, proofs, primary papers—not generated navigation |
| `dependencies` | canonical parent IDs or unresolved source aliases |
| `children` | questions generated while adjudicating this item |
| `closure_criterion` | observation/proof that would pass the node |
| `falsifier` | observation/counterexample that would refute it |
| `source_verdict` | verbatim assertion-level verdict from each source, possibly contradictory |
| `claim_truth_grade` | independent audit grade of the proposition actually established |
| `obligation_effect` | `creates`, `narrows`, `closes`, `retracts`, or `none`; a `PROVED` arc may create an open obligation |
| `adjudicated_status` | one operational state from `README.md`; `OPEN` is admissible but nonterminal |
| `evidence_mode` | `proof`, `exact-compute`, `bounded-numeric`, `literature`, `postulate`, or `unrun` |
| `review_state` | author-bank status and independent-review status, kept separate |
| `evidence` | concise proof/result and reproducibility record |
| `scope` | exact quantified domain; no silent universalization |
| `stale_or_conflict_reason` | why a navigation/status assertion was superseded, contradicted, or held |
| `owner_track` | campaign workstream |

## Gate rules

- A value match cannot repair a missing type-changing functor.
- An isomorphic Lie subalgebra is not a spacetime/gauge field theory.
- A representation dimension is not a zero-mode multiplicity.
- A nonzero internal central character is not spacetime fermion parity.
- A standard branching is an existence result, not an object-specific selector.
- A lock that checks stored outputs is weaker than a clean recomputation.
- A source-labelled theorem is not accepted until its hypotheses and proof domain are audited.
- `source_verdict` is about an arc's assertion, not the state of every residue it mentions.
- A later disappearance from navigation never counts as closure; an explicit proof, refutation,
  supersession, or scope ruling is required.
- Namespace collisions are split before semantic merging (`B58` is already two different arcs;
  q/paper/main identifiers are branch-qualified).
- “No hit” is exhaustive only after the search space and completeness certificate are proved.
- A feasible computation that has not run is `OPEN`, not `EXTERNAL_BLOCKER`; campaign exhaustion
  requires the `OPEN` count to be zero.
