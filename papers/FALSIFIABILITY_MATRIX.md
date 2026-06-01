# Falsifiability Matrix

Status: validation matrix. This file adds no claims and does not change any
candidate readiness.

## Purpose

Each active candidate must state what would make it smaller, stronger, or dead.
This matrix is the first stop after the governed ledgers:

```text
CLAIMS.md -> REVIEWABILITY_INDEX.md -> FALSIFIABILITY_MATRIX.md
```

The goal is not to prove the candidates. The goal is to make the next validation
step and the failure condition explicit.

## Active Candidate Matrix

| Candidate | Current status | Claim boundary | Missing object | Reproduction / proof path | Validation question | Kill or rescope condition |
|---|---:|---|---|---|---|---|
| PC02 -- Conditional uniqueness core | NEEDS_VALIDATION | Given A1-A7, the first mixed persistent sector is `A=LR` up to order; downstream P1-P16 are exact consequences of `A`. | Independent check that the mapping-torus torsion lemma and torsion-free closure condition are stated and applied correctly. | `docs/UNIQUENESS_THEOREM.md`; `papers/candidates/PC02_conditional_uniqueness/MAPPING_TORUS_TORSION_LEMMA.md`; `tests/test_uniqueness_theorem.py`. | Are A1-A7 precise enough, is the torsion lemma correct, and is "unique up to order" the right formulation? | Kill or rescope if the homology/torsion step is wrong, if the filter does not follow from the stated axioms, or if the LR/RL based-invariant caveat is invalid. |
| PC04 -- Noncommutative cancellation residue | EVIDENCE_EXISTS | Ordered noncommutative protocols can retain residue where commutative cancellation loses it. | A formal statement of "distinguishability implies order" and a public reproducer for the residue controls. | `docs/atlas/nodes/noncommutative_cancellation_residue.md`; `docs/atlas/FAILURE_ATLAS.md`; future public residue probe. | Does the residue survive under the exact equivalence relation needed for the cancellation argument? | Kill or rescope if distinguishable inverse acts do not require ordered data, or if the residue collapses under the required quotient. |
| PC06 -- Quantum selector bridge problem | NEEDS_VALIDATION | The figure-eight state-integral route is a serious host, but the nonzero contour/thimble/relative-homology selector is not forced. | A source-level theorem forcing a nonzero selected class without inserting the desired branch. | `docs/atlas/nodes/state_integral_selector_gap.md`; `docs/atlas/campaigns/quantum_selector_v1.md`; future source-level literature/proof audit. | Is the selector supplied by existing quantum-topology theory, derivable from the setup, or inserted? | Kill or rescope if the contour is merely chosen, if the selected class is nonunique, or if the A-polynomial branch is used as a hidden target. |
| PC07 -- Mobius-flow potential and kink toy model | NEEDS_VALIDATION | P15/P16 derive an exact vector field and cubic potential from `A`; field-theory, kink, particle, and unit language remain frontier. | A canonical kinetic/carrier/dimension/unit choice, or a proof that no such canonical lift is available. | `docs/SESSION3_SYNTHESIS.md`; `tests/test_mobius_vector_field.py`; `tests/test_derived_potential.py`; `frontier/B6_field_equation/` through `frontier/B9_fusion_scattering/`. | Which parts are exact algebra about `A`, and which parts require inserted field-theory structure? | Kill or rescope any physical reading if the kinetic term, carrier, units, or observable dictionary is inserted rather than derived. |
| PC11 -- Trace-map spectrum bridge | NEEDS_VALIDATION | The half-step trace lift is canonical and C5 gives `T1 -> S1 -> I=1/4 -> lambda/h=1`; T1 is not derived. | The status of T1: theorem, standard naturality principle, useful conditional axiom, or inserted selector. | `docs/TRACE_SELECTOR_THEOREM.md`; `frontier/B18_trace_lift_functoriality/`; `frontier/B25_fibonacci_spectrum_anchor/`; `frontier/B38_tangent_return_arithmetic_filter/` through `frontier/B47_s1_verdict_ledger/`. | Does the primitive projective tangent return legitimately inherit the original arithmetic persistence filters? | Kill or rescope if T1 is not derivable or natural; then `lambda/h=1` remains only conditional/motivated, not a prediction. |
| PC12 -- Metallic SL(3) trace-map arithmetic | NEEDS_VALIDATION | The metallic substitutions `a -> a^m b, b -> a` induce a reproducible `SL(3,C)` trace-map family with commutator trace-pair invariant, entropy, fixed-line arithmetic, and compact-unitary controls. | Polished human proof text for the fixed-line integer splitting classification, plus literature priority validation. | `frontier/B48_sl3_metallic_trace_maps/`; `frontier/B49_sl3_certificate_proof_hardening/`; `tests/test_sl3_metallic_trace_maps.py`; `tests/test_sl3_certificate_proof_hardening.py`; `papers/candidates/PC12_sl3_metallic_trace_maps/`. | Are the trace convention, entropy argument, proof-hardened classification, and compact `SU(3)` slice stated correctly as standalone mathematics? | Kill or rescope if the trace-map formula is wrong, the entropy no-cancellation proof fails, the splitting classification has counterexamples, or the result is already standard in the cited literature. |

## Status-Change Rule

Do not advance a candidate readiness label unless a validation finding is logged
in `papers/VALIDATION_LEDGER.md` and linked to a commit or PR.

Do not mark a candidate `KILLED` without recording the exact failed implication.
When possible, prefer `NEEDS_RESCOPING` for results whose algebra survives but
whose interpretation was too broad.
