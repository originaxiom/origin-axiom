# B20 -- Findings

> Logged observation, not a claim.

## Result

The trace map preserves `I`, so it has invariant-memory in the narrow
operational sense.

It also has feedback: the update `z -> 2xz-y` is state-dependent.

However, the map does not explicitly read `I`. The same polynomial rule applies
on `I=0`, `I=1/4`, `I=1/2`, and all other surfaces. Numerical sample orbits show
surface-dependent quantitative behavior, but that follows from initial
conditions and invariant separation, not from a separate read-and-respond
mechanism.

## Verdict

**`STALLED`**

The trace map supports invariant-memory and recursive-sector language. It does
not yet satisfy the stricter operational self-model criterion.
