# PC02 -- Conditional Uniqueness of the Origin Axiom Core

Status: paper candidate. No claims beyond governed repository artifacts.

## Classification

```text
Type: CONDITIONAL_THEOREM
Readiness: NEEDS_VALIDATION
Priority: first ship target
Main risk: substrate and order are inserted, not derived
```

## One-Sentence Thesis

Given the minimal-record axioms A1-A7, the first mixed persistent sector is
forced to `A = LR` up to order; from `A`, the governed core P1-P16 follows.

## What Is Genuinely New

The canonical repository has a formal, tested statement:

```text
minimal-record axioms
  -> A = LR, up to order
  -> trace 3, determinant 1, discriminant 5
  -> phi-spectrum and golden fixed-point polynomial for the based representative
  -> downstream P1-P16
```

The strongest feature is not an unconditional emergence claim. It is the
compression of the exact core into a finite conditional theorem with explicit
remaining assumptions.

## What Is Not Claimed

```text
not a derivation from absolute nothing
not a derivation of physics
not a derivation of units, particles, gauge groups, or observables
not proof that reality must use this substrate
not proof that the LR order is forced from weaker data
```

## Evidence Files

```text
CLAIMS.md
docs/UNIQUENESS_THEOREM.md
docs/SESSION3_SYNTHESIS.md
papers/candidates/PC02_conditional_uniqueness/MAPPING_TORUS_TORSION_LEMMA.md
papers/candidates/PC02_conditional_uniqueness/VALIDATION_BRIEF.md
tests/test_uniqueness_theorem.py
tests/test_mobius_vector_field.py
tests/test_derived_potential.py
```

## Reproduction Commands

```bash
python -m pytest -q
python -m pytest -q tests/test_uniqueness_theorem.py
```

## Required Controls

```text
show the candidate set before filtering
state the inserted substrate explicitly
state LR/RL order dependence explicitly
separate exact P15/P16 from frontier B6-B9
separate proven claims from conditional assumptions
keep the physics bridge open unless an observable is produced
```

## Paper-Grade Topology Lemma

The supporting lemma is now written in:

```text
papers/candidates/PC02_conditional_uniqueness/MAPPING_TORUS_TORSION_LEMMA.md
```

It proves the standard mapping-torus homology step:

```text
H1(mapping torus of B) = Z plus coker(B - I)
torsion order = |det(B - I)| when det(B - I) != 0
```

The repository tests check the algebraic consequences; the lemma note supplies
the paper-facing topology proof for independent validation.

## Target Audience

```text
low-dimensional topology readers
dynamical systems readers
mathematicians interested in rigidity and generators
auditors of the project core
```

## Best Publication Form

```text
narrow theorem note
reproducible technical report
validation packet before public draft
```

## Decision

```text
Keep. Ready for mathematical validation.
```
