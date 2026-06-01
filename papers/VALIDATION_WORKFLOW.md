# Reviewability And Falsifiability Workflow

Status: validation workflow. This file adds no claims and does not change any
candidate readiness by itself.

## Purpose

The paper-candidate layer exists to make the project reviewable and falsifiable.
It is not a logistics plan and does not track private coordination. The goal is
to reduce each candidate to:

```text
claim boundary
minimal reading path
reproduction path
known controls
failure conditions
repository action if a flaw is found
```

Current validation packets:

```text
PC02: conditional uniqueness of the core
PC11: half-step trace lift and conditional trace selector
PC12: metallic SL(3) trace-map arithmetic
```

## Validation Sequence

1. Select one packet.
2. Read only the minimal files named by that packet.
3. Run the stated reproduction commands.
4. Check the packet's explicit falsification questions.
5. Record any actionable finding in `VALIDATION_LEDGER.md`.
6. Classify the finding with one decision label.
7. Decide a repository action.
8. Implement accepted fixes through a normal branch and PR.
9. Update candidate readiness only after the finding is logged and triaged.

Do not mix PC02 and PC11 unless the finding really depends on both packets.

## Competence Map

PC02 is best checked by someone using:

```text
low-dimensional topology
mapping-torus homology
SL(2,Z) / punctured-torus bundles
integer matrices and torsion calculations
```

PC11 is best checked by someone using:

```text
character varieties
Fricke-Vogt trace maps
Fibonacci Hamiltonian / gap labeling
renormalization on trace surfaces
```

PC12 is best checked by someone using:

```text
SL(3,C) character varieties
trace identities and invariant theory
algebraic entropy / degree growth
computer-assisted arithmetic classification
```

Physics-facing validation is not first. It becomes useful only after the
mathematical bridge statement is well-posed and falsifiable.

## Packet Rules

Packets are repository artifacts, not correspondence. They should contain enough
context for an independent reader to reproduce the claim boundary without raw
chats, private transcripts, private staging archives, or private identity data.

For PC02, validate from:

```text
papers/candidates/PC02_conditional_uniqueness/REVIEWABILITY_CHECKLIST.md
papers/candidates/PC02_conditional_uniqueness/VALIDATION_BRIEF.md
papers/candidates/PC02_conditional_uniqueness/REVIEW_PACKET.md
docs/UNIQUENESS_THEOREM.md
papers/candidates/PC02_conditional_uniqueness/MAPPING_TORUS_TORSION_LEMMA.md
```

For PC11, validate from:

```text
papers/candidates/PC11_trace_map_spectrum_bridge/VALIDATION_BRIEF.md
papers/candidates/PC11_trace_map_spectrum_bridge/REVIEW_PACKET.md
docs/TRACE_SELECTOR_THEOREM.md
```

For PC12, validate from:

```text
papers/candidates/PC12_sl3_metallic_trace_maps/VALIDATION_BRIEF.md
papers/candidates/PC12_sl3_metallic_trace_maps/PAPER_CARD.md
papers/candidates/PC12_sl3_metallic_trace_maps/CERTIFICATE_APPENDIX.md
papers/candidates/PC12_sl3_metallic_trace_maps/LITERATURE_POSITIONING.md
frontier/B48_sl3_metallic_trace_maps/FINDINGS.md
frontier/B49_sl3_certificate_proof_hardening/FINDINGS.md
frontier/B51_sl3_symbolic_m_factorization/FINDINGS.md
frontier/B52_multichannel_fibonacci_bridge_control/FINDINGS.md
papers/candidates/PC12_sl3_metallic_trace_maps/DRAFT_NOTE_SKELETON.md
```

Optional shared context:

```text
GOVERNANCE.md
CLAIMS.md
papers/REVIEWABILITY_INDEX.md
```

## Decision Labels

Every logged validation item must receive one decision:

```text
ACCEPT_FIX = a real error was found; patch math/docs/tests
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

For PC12, prefer:

```text
DRAFTABLE
NEEDS_REVISION
NEEDS_RESCOPING
KILLED
```

## Non-Claims To Preserve

Reject or rewrite any summary that implies:

```text
the substrate is derived from nothing
T1 is derived before validation establishes it
lambda/h=1 is a physical prediction
gap labeling is new to this project
finite spectra prove an exact Hausdorff dimension
the framework derives matter, gauge, gravity, spacetime, or awareness
PC12 proves a physical SU(3) sector
the naive three-channel Fibonacci bridge solves the PC12 physics dictionary
```

The validation workflow is allowed to make the project smaller. That is a
success if it makes the result more correct.
