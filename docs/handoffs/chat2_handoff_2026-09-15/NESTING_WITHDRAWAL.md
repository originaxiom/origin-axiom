# WITHDRAWAL: the nesting theorem is WRONG

## The claim (withdrawn)
"Drilling the shortest geodesic from M(A₁) = m004 gives M(A₂) — the silver
bundle lives inside the golden bundle as the complement of its shortest
closed geodesic."

## The error
The drilled manifold has **two cusps** (it is the Whitehead link complement,
m129 in the census). The silver bundle M(A₂) = m136 has **one cusp**. A
two-cusped manifold cannot be homeomorphic to a one-cusped manifold.

The volume match (3.6639 to 10⁻¹⁰) is real and is exactly the trap: two
non-homeomorphic hyperbolic 3-manifolds with the same volume. I matched
volumes and declared a topological identification without checking
`num_cusps()` — one function call that would have killed the claim.

## What I actually computed
```python
M = snappy.Manifold('b++RL')  # m004
D = M.drill(0)                 # drill shortest geodesic
D_filled = D.filled_triangulation()
vol = float(D_filled.volume())  # = 3.6639 = Vol(m136) = Vol(m129)
```
I never ran `D.num_cusps()` or `D_filled.num_cusps()`.

## CC's independent verification
CC confirmed: the drilled manifold is isometric to m129 (Whitehead link
complement, two cusps), not m136 (silver bundle, one cusp).

## The pattern
This is the fifth error caught in this session, and it has the same shape
as the others: right computation, wrong conclusion. The volume computation
is correct; the topological inference from it is not. Specifically:
"equal volume → homeomorphic" is FALSE for hyperbolic 3-manifolds.

## Status
WITHDRAWN. The "nested metallic bundles" claim is deleted from the
fresh-eyes handoff. The structural findings section (§3a) is replaced with
this withdrawal notice. The minimum-compression finding (§3b) is unaffected
(it uses mapping torus volumes, not drilled manifolds).
