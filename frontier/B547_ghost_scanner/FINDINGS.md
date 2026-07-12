# B547 — The ghost scanner: (4,4,16) is the first ALL-HYPERBOLIC ghost

The prereg'd ghost scanner, built. It decides realizability of trace triples
(x,y,z) on x²+y²+z²−xyz=c EXACTLY: (x,y,z) = (tr A, tr B, tr AB) for some
A,B ∈ SL(2,ℤ) iff, for A = companion of a trace t with class number
h(t²−4)=1, the binary quadratic Δ = (t²−4)q² + (4z−2ty)q + (y²−4) is a
perfect square for some integer q (decided by sympy.diophantine). Completeness
is guaranteed by h=1 (companion is the only GL(2,ℤ) class); the S₃ symmetry of
the trace triple lets A be taken as any coordinate, so ONE complete failing
trace proves non-realizability.

## The headline: (4,4,16) resolved — and it answers the open question

**(4,4,16) at c=32 is a PROVED GHOST — and the FIRST ALL-HYPERBOLIC one.**
- Every coordinate is ≥4, so every slot is hyperbolic (t²−4 > 0): B545's
  elliptic-lock does NOT apply. This is the case the open question asked for.
- The trace-4 slot reduces exactly to **u² − 3v² = 7** (u = 3q+4). Since
  (3/7) = −1, **7 is INERT in ℚ(√3)**, so it is not a norm from ℤ[√3] and the
  equation has NO integer solution (confirmed three ways: the inert-prime
  argument, sympy.diophantine returning ∅, and brute force |u|,|v|≤200). The
  trace-4 order has disc 12, h=1 ⟹ complete ⟹ **(4,4,16) is not realizable.**

**This is a SECOND ghost mechanism, distinct from B545's elliptic-lock:** an
**inert-prime norm obstruction** on the Pell conic. Small ghosts (c=1,
(1,1,5)) are elliptic-locked (a coordinate too rigid to compose); (4,4,16) is
all-hyperbolic and ghostly for a purely arithmetic reason (7 inert). So:

> **Ghostliness is not merely an elliptic shadow.** All-hyperbolic ghosts
> exist; the obstruction can be inert-prime rather than elliptic-rigidity.

## Discrepancy RESOLVED (chat-2 refuted)

chat-2's bravery-cycle corrections log called (4,4,16) a "false candidate
already in CC's record" (i.e. realizable, wrongly flagged). **Refuted.**
(4,4,16) is a genuine, proved ghost — no witness exists (there cannot be one).
The B537/B545 "status stays candidate, witness requested" flag now closes:
GHOST, proved. (4,16,60) at c=32 is likewise a proved all-hyperbolic ghost via
the same complete trace-4 slot.

## Census (sanity + verdicts)
Markov triples (3,3,3),(3,3,6),(3,6,15) all REALIZE (as Cohn's theorem
requires) ✓. c=1 (B545) and (1,1,5)/c=22 (B537) confirmed GHOST(proved) by
the unified scanner (elliptic slots, h(−3)=1).

## Gate (hard, unchanged)
The two mechanisms (elliptic-lock, inert-prime) and the all-hyperbolic-ghost
existence are firewall-safe pure number theory, but NOVELTY is gated:
Whang (nonlinear descent), BGS lifting, and Fricke/free-product trace theory
may own the realizability criterion and/or the ghost phenomenon. No novelty
language until that lit-gate runs. Value even if owned: the (4,4,16) resolution
closes the recorded discrepancy and answers the sharpened open question.

Locks: tests/test_b547.py.
