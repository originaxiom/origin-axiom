# PC04 -- Noncommutative Cancellation Residue

Status: paper candidate. No physics claim.

## Classification

```text
Type: THEOREM_NOTE / SPECULATIVE_MODEL
Readiness: EVIDENCE_EXISTS
Priority: second-tier, after PC02
Main risk: distinguishability-to-order step must be formalized
```

## One-Sentence Thesis

Commutative inverse cancellation leaves no residue, while distinguishable
ordered inverse operations can leave a nontrivial noncommutative residue.

## What Is Genuinely New

The latest campaign independently reinforced the same Origin-side survivor in
several languages:

```text
abelian content cancels to zero
ordered free-group word remains nontrivial
closed label loop can carry nonidentity holonomy
minimal L/R shear residue produces trace 3 and phi-spectrum data
```

The strongest candidate theorem is not "physics emerges." It is:

```text
operational cancellation requires distinguishable inverse acts
distinguishable inverse acts require an ordered protocol
ordered protocols can retain noncommutative residue
the L/R residue is the minimal surviving instance under the project filters
```

## What Is Not Claimed

```text
not a derivation of the Standard Model
not a derivation of gauge fields or particles
not a proof that all cancellation must be noncommutative
not a proof that trace 3 alone selects physics
not a claim that residue becomes observable without a dictionary
```

## Evidence Files

```text
docs/atlas/nodes/noncommutative_cancellation_residue.md
docs/atlas/FAILURE_ATLAS.md
docs/atlas/RESEARCH_TREE.md
docs/atlas/campaigns/quantum_selector_v1.md
```

Campaign evidence to summarize, not copy raw:

```text
CANCEL_DISTINGUISHABILITY_ORDER_GATE
CANCEL_NONCOMMUTATIVE_RESIDUE_SEARCH
COV2_FREE_GROUP_COMMUTATOR_RESIDUE
COV2_HOLONOMY_LOOP_RESIDUE
COV2_LR_COMMUTATOR_TRACE3_PHI
COV2_COMMUTATIVE_INVERSE_CONTROL
```

## Reproduction Commands

Canonical baseline:

```bash
python -m pytest -q
```

Before drafting PC04, migrate or rewrite the private staging residue probes into
a small public reproducer.

## Required Controls

```text
compare against the commutative quotient
show which residue remains and in which algebra
separate free-group, SL(2,Z), and holonomy formulations
show trace 3 is not sufficient as a physics selector
state the missing dictionary, units, and observable bridge
```

## Paper-Grade Missing Step

The phrase "distinguishability implies order" needs a formal statement. A good
draft must define:

```text
what counts as distinguishable inverse acts
what data structure records their order
which equivalence relation makes commutative cancellation lose residue
which noncommutative quotient retains residue
why the L/R instance is minimal under stated filters
```

## Target Audience

```text
algebra and dynamics readers
foundations readers interested in cancellation arguments
reviewers of the project's obstruction map
```

## Best Publication Form

```text
theorem note after PC02
atlas-backed technical report
possible appendix to the obstruction atlas if it stays too narrow
```

## Decision

```text
Keep. Build a public atlas node before drafting.
```
