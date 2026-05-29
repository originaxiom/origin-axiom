# Research Tree

Status: map, not claim. This page summarizes the current research structure and
links each branch back to governed files.

## Root Question

```text
Can nothing produce something?
```

The working answer is split:

- Exact zero does not move without a source, rule, boundary, measure, or
  selector.
- Once a minimal record substrate is granted, a surprisingly rigid exact
  structure follows.

## Main Tree

```text
Can nothing produce something?
  exact zero cannot move
    source-free birth killed
    noise/source/boundary required
  cancellation attempt
    commutative cancellation killed
    distinguishable operations imply order
    order permits noncommutativity
    noncommutativity leaves residue
  residue
    free-group commutator survives
    SL(2,Z) L/R residue survives
    trace 3 / discriminant 5 / phi survives
  topology host
    figure-eight / A-polynomial / state integral survives as math
    contour/thimble selector missing
  physics bridge
    units missing
    gauge dictionary missing
    particle dictionary missing
    3+1D bridge missing
    observable missing
```

## Surviving Exact Spine

The current strongest spine is:

```text
minimal record axioms
  -> primitive L/R updates
  -> first mixed closure A = LR, up to order
  -> trace 3 and discriminant 5
  -> phi-spectrum and golden fixed-point polynomial
  -> figure-eight / punctured-torus monodromy structure
  -> derived Mobius vector field and cubic potential
  -> half-step trace lift and Fibonacci spectral anchor (frontier)
```

Primary files:

- `CLAIMS.md`
- `docs/UNIQUENESS_THEOREM.md`
- `docs/SESSION3_SYNTHESIS.md`
- `tests/test_uniqueness_theorem.py`

## The Load-Bearing Caveat

The order choice is not cosmetic. `LR`, `RL`, and conjugate representatives can
share trace and eigenvalues while giving different Mobius fixed-point
polynomials. The golden polynomial belongs to the based representative `A = LR`
with its order convention.

This is the cleanest current statement of the remaining inserted structure:

```text
the core is forced up to order
the golden vacuum is selected by the order convention
```

## Open Physics Bridge

Several structures are mathematically exact but do not yet become physics:

- A potential can be derived from the Mobius flow, but the kinetic term and
  spacetime carrier are additional choices.
- Topological and state-integral objects are exact, but the contour or thimble
  selector is not derived.
- Candidate gauge or particle dictionaries remain unconstructed.
- No observable has passed the governed promotion gate.
- The Fibonacci Hamiltonian at dimensionless `lambda/h=1` is a strong
  finite-approximant anchor, but B38-B47 make its status conditional on T1: the
  primitive projective tangent return must inherit the original arithmetic
  persistence filters. T1 remains motivated rather than derived.

The atlas should keep this separation visible. Exact mathematics can be
valuable without being a physical theory.

## Research Node Template

Each mature branch should eventually have a node card:

```text
ID:
Question:
Original intuition:
Mathematical object:
What was tested:
Result:
Verdict:
Why it matters:
What failed:
What remains open:
Links to code/tests:
Links to sources:
Beginner explanation:
Formal explanation:
```

## First Vertical Slice To Complete

The first complete reviewer route should be:

```text
exact zero cannot move
  -> commutative cancellation dies
  -> noncommutative residue survives
  -> trace 3 / phi structure appears
  -> topology host appears
  -> physics bridge remains open
```

That slice should become the template for future atlas nodes.
