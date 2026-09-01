# PC02 Outreach Kit

Status: outreach template. This file adds no claims and records no reviewer
identity or private correspondence.

## Purpose

Use this kit to ask for external mathematical review of PC02:

```text
minimal-record axioms A1-A7
  -> first mixed persistent sector A = LR, up to order
  -> trace 3, determinant 1, discriminant 5
  -> governed downstream core P1-P16
```

The ask is narrow: check whether the conditional theorem and topology lemma are
mathematically sound and scoped correctly. Do not frame the project as physics,
cosmology, or a derivation from nothing.

## Reviewer Fit Criteria

Good fit:

```text
low-dimensional topology
mapping-torus homology
SL(2,Z) / punctured-torus bundles
integer matrix torsion calculations
once-punctured torus bundle conventions
```

Acceptable fit:

```text
geometric topology
3-manifold topology
Teichmuller / mapping class group background
algebraic topology with mapping-torus experience
```

Poor first fit:

```text
general physics only
cosmology only
number theory without topology or SL(2,Z)
general philosophy of foundations
```

## What To Send

Send the smallest useful packet:

```text
papers/candidates/PC02_conditional_uniqueness/EXTERNAL_REVIEW_BRIEF.md
papers/candidates/PC02_conditional_uniqueness/REVIEW_PACKET.md
docs/UNIQUENESS_THEOREM.md
papers/candidates/PC02_conditional_uniqueness/MAPPING_TORUS_TORSION_LEMMA.md
```

Optional context only if requested:

```text
GOVERNANCE.md
CLAIMS.md
tests/test_uniqueness_theorem.py
```

Do not send:

```text
raw chats
private transcripts
private staging archives
physics-facing speculation
the whole repository unless requested
```

## Short First-Contact Template

```text
Subject: Request for a narrow math review: SL(2,Z) mapping-torus torsion lemma

Hello,

I am preparing a short conditional theorem note about a minimal integer
record-transfer system. The specific review question is narrow: whether the
mapping-torus homology/torsion step and the "unique up to order" formulation are
mathematically sound.

The core object is B(a,b)=L_a R_b in SL(2,Z), with
det(B(a,b)-I)=-ab. The note uses the standard mapping-torus relation
H_1(M_B;Z)=Z plus coker(B-I), so a torsion-free closure condition forces ab=1,
hence A=LR up to order.

Would you be willing to look at a compact review packet and say whether the
statement is draftable, needs revision, needs rescoping, or fails?

The work is not presented as a physics theory and not as a derivation from
nothing. It is only a conditional theorem candidate.
```

## Full Review Request Template

```text
Subject: External review request: conditional uniqueness theorem for an SL(2,Z) record-transfer core

Hello,

I am looking for a narrow mathematical review of a conditional theorem candidate.
The theorem starts from explicit minimal-record axioms and studies the first
mixed closure

  B(a,b)=L_a R_b = [[1+ab,a],[b,1]]

with L_a and R_b the primitive parabolic shears. The two central checks are:

1. Whether the mapping-torus homology lemma is stated and applied correctly:

   H_1(M_B;Z)=Z plus coker(B-I),
   and when det(B-I) != 0 the torsion order is |det(B-I)|.

2. Whether the conclusion should be stated as "A=LR is forced up to order" once
   the torsion-free/minimal-trace filter gives ab=1.

The review packet explicitly does not claim physics, units, particles, gauge
groups, observables, or a derivation from nothing. It is a conditional theorem
about an already-specified integer record-transfer substrate.

The main files are:

  papers/candidates/PC02_conditional_uniqueness/EXTERNAL_REVIEW_BRIEF.md
  papers/candidates/PC02_conditional_uniqueness/REVIEW_PACKET.md
  docs/UNIQUENESS_THEOREM.md
  papers/candidates/PC02_conditional_uniqueness/MAPPING_TORUS_TORSION_LEMMA.md

The requested outcome label is one of:

  DRAFTABLE
  NEEDS_REVISION
  NEEDS_RESCOPING
  KILLED

Specific questions:

  - Are A1-A7 precise enough for a theorem note?
  - Is the torsion-free closure condition natural or too tailored?
  - Is the mapping-torus homology lemma correct with the stated hypotheses?
  - Is the B versus B^T convention harmless for torsion order?
  - Is "unique up to order" the right formulation for LR/RL?
  - Is the based-invariant caveat stated correctly?
  - Should the downstream P1-P16 corollary be narrowed?

If you are willing to review it, a short answer identifying the first serious
mathematical objection, or saying that the note is draftable with caveats, would
already be very useful.
```

## Response Logging Instructions

After receiving a response:

1. Do not paste private correspondence into the repository.
2. Summarize the response in `papers/REVIEW_RESPONSE_LEDGER.md`.
3. Use a neutral reviewer label such as `reviewer-001`.
4. Assign one outcome label: `DRAFTABLE`, `NEEDS_REVISION`, `NEEDS_RESCOPING`,
   or `KILLED`.
5. Assign one response decision: `ACCEPT_FIX`, `ACCEPT_CLARIFY`, `NEEDS_REPRO`,
   `DISPUTE_WITH_REASON`, `OUT_OF_SCOPE`, or `KILL_OR_RESCOPE`.
6. Patch claims, proofs, tests, or paper cards only after the response is
   triaged.

## Non-Claims To Preserve

Do not write outreach text that implies:

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
