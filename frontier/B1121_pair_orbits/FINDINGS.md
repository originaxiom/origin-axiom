# B1121 — L176: F₄(ℤ) on idempotent PAIRS — the machinery is validated, the pair question is inconclusive at the bound

**Status: banked (frontier). Verdict OPEN (an honest INCONCLUSIVE-AT-BOUND; the
validated machinery + the stated bound are the contribution). L176's cell (the
outside session's C-P3-adjacent pair lane, pointed at Route A). Gate 5 untouched.
Lock `tests/test_b1121_pairs.py`.**

## The question (L176)

Route A's rank-6 → rank-4 needs a PAIR (B1094: "the pair is the object"). Does F₄(ℤ)
(integral Jordan automorphisms) act TRANSITIVELY on orthogonal pairs of rank-1
idempotents in the split integral exceptional Jordan algebra J₃, or does the orbit
SPLIT (a computable separating invariant)?

## What was established (this bench, own reimplementation)

**The machinery is built and VALIDATED** — reimplemented from the outside session's
description (the scripts were not shipped):
- automorphy on the Jordan product: 500/500 exact (the load-bearing check — a map
  connecting two idempotents must be a genuine automorphism);
- the norm/trace/cubic invariants preserved: 500/500 + 60/60 across every control
  (Leibniz derivation, Jordan identity, Freudenthal identity, N-vs-Newton,
  N-vs-closed-form);
- the SINGLE-idempotent positive control CONNECTS (the outside session's transitivity
  on rank-1 idempotents reproduced — the isotropy⟺nilpotency mechanism, the split
  lattice's isotropic supply);
- the division-form control collapses (zero isotropics — the rigid picture).

## The honest verdict: INCONCLUSIVE-AT-BOUND

Neither outcome was reached within the search bound:
- **NOT proven PAIR-TRANSITIVE**: the BFS did not connect the hand-built orthogonal
  pair seed D to the automorphism-derived seed orbit {A,B,C} within the depth/pool/
  cap/time bound — all runs capped before exhausting the group. (The A-derived seeds
  B,C DID connect back to A — a sanity check the pair-BFS machinery works.)
- **NOT proven ORBIT-SPLIT**: no separating pair-invariant was found among the
  natural candidates (det(E+F), joint-kernel theta, the cross cubic-form coefficients).

So **L176 remains OPEN**, now with validated tooling and a stated bound. The
contribution is the machinery (reusable, controls green) + the honest boundary: a
larger search (bigger pool/depth/cap) or a cleverer invariant would decide it. Route
A's pair-orbit lane is neither advanced nor closed — it is instrumented.

## Fences

No claim of transitivity or split — the search was bounded and did not settle it. The
validated machinery is the real result; the bound is stated, not hidden. No SM value;
Gate 5 untouched.
