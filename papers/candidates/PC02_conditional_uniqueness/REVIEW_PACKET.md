# PC02 Review Packet -- Conditional Uniqueness of the Origin Axiom Core

Status: external-review packet. This is a guide for auditing the conditional
theorem. It does not promote C1 and does not add claims.

## Review Target

The candidate statement is:

```text
minimal-record axioms A1-A7
  -> first mixed persistent sector A = LR, up to order
  -> trace 3, determinant 1, discriminant 5
  -> phi-spectrum and golden fixed-point polynomial for the based representative
  -> downstream governed core P1-P16
```

The result is conditional. The axioms are motivated by the project, not derived
from nothing.

## Files To Read

Primary:

```text
docs/UNIQUENESS_THEOREM.md
tests/test_uniqueness_theorem.py
CLAIMS.md
papers/candidates/PC02_conditional_uniqueness/PAPER_CARD.md
papers/candidates/PC02_conditional_uniqueness/MAPPING_TORUS_TORSION_LEMMA.md
papers/candidates/PC02_conditional_uniqueness/VALIDATION_BRIEF.md
```

Secondary:

```text
docs/SESSION3_SYNTHESIS.md
tests/test_mobius_vector_field.py
tests/test_derived_potential.py
docs/atlas/RESEARCH_TREE.md
docs/atlas/SUCCESS_ATLAS.md
```

## Reproduction Commands

Run from the repository root:

```bash
python -m pytest -q
python -m pytest -q tests/test_uniqueness_theorem.py
```

Expected current result:

```text
full suite: 66 passed, 1 skipped
uniqueness theorem tests: 9 passed
```

## The Algebra To Check

The theorem uses primitive shears:

```text
L_a = [[1,a],[0,1]]
R_b = [[1,0],[b,1]]
B(a,b) = L_a R_b = [[1+ab,a],[b,1]]
```

The locked identities are:

```text
det B(a,b) = 1
trace B(a,b) = 2 + ab
det(B(a,b) - I) = -ab
```

Over positive integers, the torsion-free filter or minimal hyperbolic trace
forces:

```text
ab = 1
a = b = 1
B(1,1) = A = LR = [[2,1],[1,1]]
```

The local grid check is:

```text
12 x 12 positive mixed closures = 144 hyperbolic candidates
torsion-free filter leaves exactly 1 candidate
```

## The Order Caveat

The result is only unique up to order. This is intentional and load-bearing:

```text
LR -> tau^2 - tau - 1
RL -> tau^2 + tau - 1
conjugate representative K -> tau^2 - 3 tau + 1
```

The golden fixed-point polynomial belongs to the based representative `A = LR`,
not to the whole conjugacy class. The audit must check that the paper never
silently turns this based fact into a class invariant.

## Paper-Grade Lemma

The paper-support topology lemma is now written in:

```text
papers/candidates/PC02_conditional_uniqueness/MAPPING_TORUS_TORSION_LEMMA.md
```

It proves:

```text
H1(mapping torus of B) = Z plus coker(B - I)
if det(B - I) != 0, the torsion order is |det(B - I)|
```

For `B(a,b)`, this gives torsion order `ab`. Torsion-free closure then forces
`ab = 1`.

Validation checks:

```text
confirm the lemma statement is standard and correctly applied
confirm no orientability, boundary, or puncture convention changes the use here
confirm whether the proof should use cellular chains, Wang sequence, or mapping-torus homology
```

## Non-Claims To Enforce

The validation process should reject any draft wording that implies:

```text
the substrate was derived from nothing
the LR order was forced from weaker data
the theorem derives physics
the theorem derives units, gauge groups, particles, or observables
the field-theory lift B6-B9 is proven
```

The correct wording is:

```text
given the minimal-record axioms, the core is conditionally forced up to order
```

## Draft Readiness Checklist

Before PC02 becomes `DRAFTABLE`, it needs:

```text
independent check of the mapping-torus homology lemma
one-page statement of axioms with motivation and limitations for the draft body
explicit LR/RL order section
table separating proven P-claims from conditional C1
reproduction appendix naming the exact tests
short related-work scan for primitive shears and once-punctured torus bundles
one independent mathematical validation pass
```

## Validation Questions

Check:

```text
Are A1-A7 stated with enough precision?
Is the torsion-free closure condition natural or too tailored?
Is the 144 -> 1 grid check useful evidence, or should it be removed from the paper body?
Is "up to order" the right mathematical phrasing?
Is the based-invariant distinction stated correctly?
Is the downstream P1-P16 corollary too broad for the theorem note?
What existing theorem or terminology should replace project-specific language?
```

## Outcome Labels

After review, assign exactly one:

```text
DRAFTABLE = theorem and caveats are sound enough to draft
NEEDS_REVISION = statement is sound but presentation or proof needs repair
NEEDS_RESCOPING = the theorem should be narrower
KILLED = a central lemma or implication fails
```

## Current Decision

```text
Prepare PC02 for external mathematical review.
Do not merge with physics-facing material.
```
