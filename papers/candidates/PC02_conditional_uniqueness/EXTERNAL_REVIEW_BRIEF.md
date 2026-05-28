# PC02 External Review Brief

Status: review brief. This is a compact handoff for a mathematical reviewer.
It does not add claims.

## What To Review

PC02 claims a conditional theorem:

```text
minimal-record axioms A1-A7
  -> first mixed persistent sector A = LR, up to order
  -> trace 3, determinant 1, discriminant 5
  -> phi-spectrum and golden based fixed-point polynomial
  -> governed downstream core P1-P16
```

The review target is not a physics theory and not a derivation from nothing. It
is a conditional uniqueness statement in a small integer record-transfer system.

## Minimal Reading Set

Read in this order:

```text
papers/candidates/PC02_conditional_uniqueness/PAPER_CARD.md
docs/UNIQUENESS_THEOREM.md
papers/candidates/PC02_conditional_uniqueness/MAPPING_TORUS_TORSION_LEMMA.md
tests/test_uniqueness_theorem.py
papers/candidates/PC02_conditional_uniqueness/REVIEW_PACKET.md
```

## Main Checks Requested

Please check:

```text
Are A1-A7 precise enough for a theorem note?
Is the torsion-free closure condition natural, or too tailored?
Is the mapping-torus homology lemma stated and applied correctly?
Is the B versus B^T convention harmless for the torsion-order conclusion?
Is "unique up to order" the right wording for LR/RL?
Is the based-invariant caveat stated correctly?
Should the P1-P16 corollary be narrowed in a paper draft?
```

## Core Lemma To Audit

The topology step is:

```text
H1(M_B; Z) = Z plus coker(B - I)
|torsion H1(M_B; Z)| = |det(B - I)|, when det(B - I) != 0
```

For:

```text
B(a,b) = L_a R_b = [[1+ab,a],[b,1]],
```

this gives:

```text
det(B(a,b) - I) = -ab
```

so the torsion-free filter forces `ab = 1`, hence `a = b = 1` over positive
integers.

## Non-Claims

Reject wording that implies:

```text
the substrate is derived from nothing
the LR order is forced from weaker data
the theorem derives physics
the theorem derives units, particles, gauge groups, or observables
the frontier field-theory lift is proven
```

Correct status:

```text
conditional mathematical theorem candidate, ready for external review
```

## Suggested Outcome Labels

```text
DRAFTABLE = theorem and caveats are sound enough to draft
NEEDS_REVISION = proof or presentation needs repair
NEEDS_RESCOPING = statement should be narrower
KILLED = a central lemma or implication fails
```
