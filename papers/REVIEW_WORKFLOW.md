# External Review Workflow

Status: workflow document. This file adds no claims and does not change any
candidate readiness by itself.

## Purpose

External review is now a controlled research step. The goal is not encouragement,
visibility, or publication. The goal is to answer narrow mathematical questions
that the repository has isolated but cannot settle internally.

Current packets:

```text
PC02: conditional uniqueness of the core
PC11: half-step trace lift and conditional trace selector
```

## Review Sequence

1. Select one packet.
2. Send only the minimal files named by that packet.
3. Ask the packet's explicit review questions.
4. Record the response in `REVIEW_RESPONSE_LEDGER.md`.
5. Classify the response with one outcome label.
6. Decide a repository action.
7. Implement any accepted fix through a normal branch and PR.
8. Update candidate readiness only after the response is logged and triaged.

Do not mix PC02 and PC11 unless the reviewer explicitly has expertise in both.

## Reviewer Archetypes

PC02 is for reviewers with expertise in:

```text
low-dimensional topology
mapping-torus homology
SL(2,Z) / punctured-torus bundles
integer matrices and torsion calculations
```

PC11 is for reviewers with expertise in:

```text
character varieties
Fricke-Vogt trace maps
Fibonacci Hamiltonian / gap labeling
renormalization on trace surfaces
```

Physics review is not the first target. Physics-facing review becomes useful
only after a mathematical reviewer agrees that the relevant bridge statement is
well-posed.

## Packet Rules

For PC02, send:

```text
papers/candidates/PC02_conditional_uniqueness/EXTERNAL_REVIEW_BRIEF.md
papers/candidates/PC02_conditional_uniqueness/REVIEW_PACKET.md
docs/UNIQUENESS_THEOREM.md
papers/candidates/PC02_conditional_uniqueness/MAPPING_TORUS_TORSION_LEMMA.md
```

For PC11, send:

```text
papers/candidates/PC11_trace_map_spectrum_bridge/EXTERNAL_REVIEW_BRIEF.md
papers/candidates/PC11_trace_map_spectrum_bridge/REVIEW_PACKET.md
docs/TRACE_SELECTOR_THEOREM.md
```

Optional shared context:

```text
GOVERNANCE.md
CLAIMS.md
papers/EXTERNAL_REVIEW_INDEX.md
```

Do not send raw chats, private transcripts, or private staging archives.

## Response Decisions

Every logged review item must receive one decision:

```text
ACCEPT_FIX = reviewer found a real error; patch math/docs/tests
ACCEPT_CLARIFY = statement is sound but wording must be narrowed
NEEDS_REPRO = reproduce or verify before accepting
DISPUTE_WITH_REASON = keep current statement and write the reason
OUT_OF_SCOPE = useful comment, but outside the packet's question
KILL_OR_RESCOPE = central implication fails or must be narrowed
```

## Outcome Labels

Use the packet-specific labels where available. Otherwise use:

```text
DRAFTABLE = sound enough to begin paper draft
NEEDS_REVISION = sound, but proof or presentation needs repair
NEEDS_RESCOPING = claim should be narrower
KILLED = central lemma or implication fails
```

For PC11, prefer the packet labels:

```text
T1_NATURAL
T1_INSERTED
NEEDS_REVISION
NEEDS_RESCOPING
KILLED
```

## Non-Claims To Preserve

Reject or rewrite any response summary that implies:

```text
the substrate is derived from nothing
T1 is derived before review establishes it
lambda/h=1 is a physical prediction
gap labeling is new to this project
finite spectra prove an exact Hausdorff dimension
the framework derives matter, gauge, gravity, spacetime, or awareness
```

The review workflow is allowed to make the project smaller. That is a success if
it makes the result more correct.
