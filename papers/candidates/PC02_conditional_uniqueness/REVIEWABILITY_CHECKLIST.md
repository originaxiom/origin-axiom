# PC02 Reviewability Checklist

Status: reviewability checklist. This file adds no claims and records no private
correspondence or identity data.

## Purpose

Use this checklist to validate PC02:

```text
minimal-record axioms A1-A7
  -> first mixed persistent sector A = LR, up to order
  -> trace 3, determinant 1, discriminant 5
  -> governed downstream core P1-P16
```

The target is narrow: check whether the conditional theorem and topology lemma
are mathematically sound and scoped correctly. Do not frame the project as
physics, cosmology, or a derivation from nothing.

## Competence Areas

Useful background:

```text
low-dimensional topology
mapping-torus homology
SL(2,Z) / punctured-torus bundles
integer matrix torsion calculations
once-punctured torus bundle conventions
geometric topology
Teichmuller / mapping class group background
algebraic topology with mapping-torus experience
```

Poor first validation target:

```text
general physics only
cosmology only
number theory without topology or SL(2,Z)
general philosophy of foundations
```

## Minimal Packet

Validate from the smallest useful packet:

```text
papers/candidates/PC02_conditional_uniqueness/VALIDATION_BRIEF.md
papers/candidates/PC02_conditional_uniqueness/REVIEW_PACKET.md
docs/UNIQUENESS_THEOREM.md
papers/candidates/PC02_conditional_uniqueness/MAPPING_TORUS_TORSION_LEMMA.md
```

Optional context only if needed:

```text
GOVERNANCE.md
CLAIMS.md
tests/test_uniqueness_theorem.py
```

Do not use:

```text
raw chats
private transcripts
private staging archives
physics-facing speculation
the whole repository as the first reading path
```

## Core Validation Questions

```text
Are A1-A7 precise enough for a theorem note?
Is the torsion-free closure condition natural, or too tailored?
Is the mapping-torus homology lemma stated and applied correctly?
Is the B versus B^T convention harmless for the torsion-order conclusion?
Is "unique up to order" the right wording for LR/RL?
Is the based-invariant caveat stated correctly?
Should the P1-P16 corollary be narrowed in a paper draft?
What concrete flaw would kill or rescope PC02?
```

## Triage Instructions

After a finding:

1. Do not paste private correspondence into the repository.
2. Summarize the technical finding in `papers/VALIDATION_LEDGER.md`.
3. Assign one outcome label: `DRAFTABLE`, `NEEDS_REVISION`,
   `NEEDS_RESCOPING`, or `KILLED`.
4. Assign one decision: `ACCEPT_FIX`, `ACCEPT_CLARIFY`, `NEEDS_REPRO`,
   `DISPUTE_WITH_REASON`, `OUT_OF_SCOPE`, or `KILL_OR_RESCOPE`.
5. Patch claims, proofs, tests, or paper cards only after the finding is
   triaged.

## Non-Claims To Preserve

Do not write validation text that implies:

```text
the substrate is derived from nothing
the LR order is forced from weaker data
the theorem derives physics
the theorem derives units, particles, gauge groups, or observables
the frontier field-theory lift is proven
```

Correct framing:

```text
given the minimal-record axioms, the core is conditionally forced up to order
```
