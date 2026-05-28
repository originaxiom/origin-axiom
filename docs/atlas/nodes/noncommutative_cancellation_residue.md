# Noncommutative Cancellation Residue

Status: atlas node for PC04. Frontier synthesis, not a physics claim.

## Question

Can the "opposite of perfect cancellation" be modeled as a residue left by
ordered, noncommuting inverse operations?

## Original Intuition

Perfect cancellation in a commutative setting leaves nothing:

```text
x + (-x) = 0
```

That cannot generate structure. The live version of the idea is different:

```text
if cancellation is operational, the inverse acts must be distinguishable
if distinguishable acts are applied in sequence, their order can matter
if order matters, noncommutative residue can remain
```

## Mathematical Object

The minimal tested object is the L/R shear system:

```text
L = [[1,1],[0,1]]
R = [[1,0],[1,1]]
```

Two residue certificates are used:

```text
additive commutator: LR - RL != 0
group commutator: L R L^-1 R^-1 != I
```

This gives a precise mathematical version of imperfect cancellation by order
asymmetry.

## What Was Tested

Primary frontier evidence:

```text
docs/atlas/campaigns/quantum_selector_v1.md
papers/candidates/PC04_noncommutative_residue/PAPER_CARD.md
```

The private staging probes behind this summary tested whether mixed inverse
order leaves a nonidentity residue.

They also tested whether trace 3 is the first hyperbolic sector once
nonnegative integer `SL(2,Z)` structure is assumed.

They then tested which physics hosts could receive the residue without
overclaiming.

The campaign tested the same pattern in free-group, holonomy, L/R, and
commutative-control language.

## Result

What survives:

```text
LR - RL != 0
L R L^-1 R^-1 != I
commutative quotient kills the residue
ordered nonabelian word retains residue
minimal trace-3 sector gives phi-spectrum data once the substrate/filter is supplied
```

What does not survive:

```text
the two operations are not derived from nothing
the order loop is not forced from nothing
trace 3 is not by itself a physics selector
the residue does not supply units, fields, action, source law, or observable
```

## Verdict

```text
STALLED
```

The residue exists as mathematics after distinguishable ordered operations are
available. The missing step is deriving or justifying the operational substrate
and building a physical dictionary.

## Why It Matters

This is the cleanest mathematical form of the non-cancellation intuition:

```text
commutative cancellation -> no residue
noncommutative cancellation -> possible residue
```

It converts a vague slogan into a checkable object. It also explains why the
conditional uniqueness theorem's order convention is not cosmetic: order is
where the surviving residue enters.

## What Failed

Every physics-facing host still imports missing structure:

```text
holonomy/curvature imports connection, base space, loop family, and scale
quantum commutator imports Hilbert space, observable algebra, and state
anomaly/CP imports QFT framework, chirality, gauge bundle, regulator, and sector choice
causal growth imports causet substrate, birth rule, measure, and time orientation
statistical transfer imports ensemble, weights, boundary condition, and observable map
```

No host passed the bridge gate:

```text
forced generator
units or scale
selection rule
observable
```

## What Remains Open

The PC04 theorem program must formalize:

```text
what counts as distinguishable inverse acts
what data structure records order
which quotient makes commutative cancellation lose residue
which noncommutative quotient retains residue
why the L/R instance is minimal under stated filters
```

The physics program, if pursued later, must construct:

```text
field dictionary
action or operator complex
unit scale
selection rule
observable
```

## Reproduction Commands

Canonical baseline:

```bash
python -m pytest -q
```

The private staging probes should be converted into a small public reproducer
before PC04 is drafted. Until then, this node is a summary of the campaign and
paper-card evidence, not a standalone proof artifact.

## Beginner Explanation

If two steps perfectly undo each other and their order does not matter, nothing
is left. But if the steps are different and order matters, doing them around a
loop can fail to return exactly to the start. That leftover is the residue.

The project found this residue clearly in the L/R system. It has not shown that
the universe, particles, or fields come from it.

## Formal Explanation

The noncommuting shears `L` and `R` generate both an additive commutator
`LR - RL` and a group commutator `L R L^-1 R^-1`. Both are nontrivial, while the
commutative quotient removes the residue. Under additional nonnegative
`SL(2,Z)` and minimal hyperbolic filters, the trace-3 sector appears and carries
the familiar phi-spectrum. Those filters are assumptions or conditional gates,
not derivations from no structure.
