# Reviewability Index

Status: public-safe validation router. This file adds no claims.

## Purpose

The repository has two reviewable mathematical packets:

```text
PC02: conditional uniqueness of the core
PC11: half-step trace lift and conditional trace selector
PC12: metallic SL(3) trace-map arithmetic
```

They should be audited separately. PC02 asks whether the record-transfer theorem
is stated and proved cleanly. PC11 asks whether the T1 tangent-filter
inheritance assumption is natural, standard, derivable, or inserted. PC12 asks
whether the metallic `SL(3)` trace-map arithmetic is correct, proof-hardened,
and properly positioned in the character-variety literature.

## Recommended Audit Order

1. `GOVERNANCE.md`
2. `CLAIMS.md`
3. `papers/FALSIFIABILITY_MATRIX.md`
4. `papers/VALIDATION_WORKFLOW.md`
5. `papers/candidates/PC02_conditional_uniqueness/REVIEWABILITY_CHECKLIST.md`
6. `papers/candidates/PC02_conditional_uniqueness/VALIDATION_BRIEF.md`
7. `papers/candidates/PC02_conditional_uniqueness/REVIEW_PACKET.md`
8. `papers/candidates/PC11_trace_map_spectrum_bridge/VALIDATION_BRIEF.md`
9. `papers/candidates/PC11_trace_map_spectrum_bridge/REVIEW_PACKET.md`
10. `docs/TRACE_SELECTOR_THEOREM.md`
11. `papers/candidates/PC12_sl3_metallic_trace_maps/VALIDATION_BRIEF.md`
12. `papers/candidates/PC12_sl3_metallic_trace_maps/PAPER_CARD.md`
13. `frontier/B49_sl3_certificate_proof_hardening/FINDINGS.md`

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

For PC12:

```text
Is the metallic SL(3) trace-map formula correct under the stated trace convention?
Is the entropy computation a proof, not only observed degree growth?
Is the B49 proof-module decomposition sufficient to draft the classification proof?
Is the compact SU(3) slice stated as compact-unitary mathematics only?
What parts, if any, are already present in the existing literature?
```

## Non-Claims To Enforce

Reject any validation summary or paper draft that says:

```text
the project derives the substrate from nothing
the trace selector is proven without T1
lambda/h=1 is a physical prediction
the Fibonacci Hamiltonian results are new gap-labeling mathematics
the framework derives matter, gauge, gravity, spacetime, or awareness
the metallic SL(3) direct/inverse trace distinction is particle physics
```

The correct status is:

```text
PC02: conditional theorem candidate, ready for mathematical validation
PC11: computational/literature bridge, conditional on T1
PC12: standalone metallic SL(3) arithmetic candidate, proof-hardened but not yet independently validated
```
