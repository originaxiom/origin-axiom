# Reviewability Index

Status: public-safe validation router. This file adds no claims.

## Purpose

The repository has two reviewable mathematical packets:

```text
PC02: conditional uniqueness of the core
PC11: half-step trace lift and conditional trace selector
```

They should be audited separately. PC02 asks whether the record-transfer theorem
is stated and proved cleanly. PC11 asks whether the T1 tangent-filter
inheritance assumption is natural, standard, derivable, or inserted.

## Recommended Audit Order

1. `GOVERNANCE.md`
2. `CLAIMS.md`
3. `papers/VALIDATION_WORKFLOW.md`
4. `papers/candidates/PC02_conditional_uniqueness/REVIEWABILITY_CHECKLIST.md`
5. `papers/candidates/PC02_conditional_uniqueness/VALIDATION_BRIEF.md`
6. `papers/candidates/PC02_conditional_uniqueness/REVIEW_PACKET.md`
7. `papers/candidates/PC11_trace_map_spectrum_bridge/VALIDATION_BRIEF.md`
8. `papers/candidates/PC11_trace_map_spectrum_bridge/REVIEW_PACKET.md`
9. `docs/TRACE_SELECTOR_THEOREM.md`

Record any actionable finding in:

```text
papers/VALIDATION_LEDGER.md
```

## Validation Questions

For PC02:

```text
Are A1-A7 precise enough for a conditional theorem note?
Is the mapping-torus torsion lemma correct and applied with the right hypotheses?
Is "unique up to order" the right formulation?
What concrete statement would falsify or rescope the theorem candidate?
```

For PC11:

```text
Is the half-step trace lift standard character-variety material?
Is the projective quotient being used legitimately?
Is T1 a theorem, a standard naturality principle, or an inserted axiom?
Does C5 correctly stop at conditional lambda/h=1?
What concrete statement would falsify or rescope the selector bridge?
```

## Non-Claims To Enforce

Reject any validation summary or paper draft that says:

```text
the project derives the substrate from nothing
the trace selector is proven without T1
lambda/h=1 is a physical prediction
the Fibonacci Hamiltonian results are new gap-labeling mathematics
the framework derives matter, gauge, gravity, spacetime, or awareness
```

The correct status is:

```text
PC02: conditional theorem candidate, ready for mathematical validation
PC11: computational/literature bridge, conditional on T1
```
