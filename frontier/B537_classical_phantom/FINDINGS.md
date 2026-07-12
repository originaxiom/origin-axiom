# B537 — The classical-surface phantom: (1,1,5) PROVED (and a level correction)

Chat-2's W1c-Q2 handoff found phantom CANDIDATES on the classical Markov-type
surface x²+y²+z²−xyz = c, reported "at c = 32": (1,1,5), (4,4,16), (4,16,60),
with an explicit warning that the trace-1 slot is elliptic (disc −3) and the
twisted-surface Pell argument does not port.

**Correction:** (1,1,5) lies at level c = 22 (1+1+25−5), not 32. The two
imprimitive candidates are at c = 32.

**THEOREM (proved).** (1,1,5) is not (tr A, tr B, tr AB) for any A,B ∈ SL(2,ℤ).

Proof legs (all exact, `phantom_proof.py`):
1. **GL2-invariance + Latimer–MacDuffee completeness:** realizability depends
   only on the GL(2,ℤ)-class of A; classes with irreducible charpoly f
   correspond to ideal classes of ℤ[t]/f. Trace 1: disc −3, h(ℚ(ζ₆)) = 1
   (sage-verified). Trace 5: disc 21 = field disc of ℚ(√21), h = 1
   (sage-verified). Companion matrices suffice in every slot.
2. **Elliptic slots (A of trace 1, order 6):** B-existence reduces exactly to
   4Q = (2a+b−r)² + 3(b−s)² − 24 with (r,s) = (1,3) and (5,−1) for the two
   assignments (derivations verified symbolically from det B = 1). The form
   U² + 3V² does not represent 24 (finite check: no integer points). NO B.
3. **Hyperbolic slot (A of trace 5):** the companion criterion discriminant is
   21a² − 6a − 3 = 3(7a² − 2a − 1) with 7a² − 2a − 1 ≢ 0 (mod 3) for all a,
   so v₃ = 1 exactly — never a perfect square. NO B.

All assignments exhausted ⟹ phantom. Sanity: Cohn/Markov triples (3,3,3),
(3,3,6), (3,6,15) all realizable ✓.

**Status of the other candidates:** (4,4,16), (4,16,60) at c = 32 remain
scan-level candidates (companion slots empty to |a| ≤ 3000); even traces need
their own slot analysis (disc 12 / 252 orders; not done here).

**Novelty gate (hard, inherited from the handoff):** Whang's nonlinear descent,
BGS lifting, and the commutator-variety literature may own this; no novelty
language until the lit gate runs. The result symmetrizes the twisted-surface
phantom phenomenon to the classical surface at proof level.

Locks: tests/test_b537.py.

## Status update (2026-07-12, B545): (4,4,16) discrepancy recorded

A chat-2 handoff asserts (4,4,16) is a known "false candidate" (realizable).
That claim is NOT in this record and is UNVERIFIED here: a direct witness
search (entries ≤ 20) plus this file's companion scans find no realization.
Status remains CANDIDATE pending chat-2's witness pair. Meanwhile c = 1 is
now a PROVED ghost by the same elliptic-lock mechanism (B545), making
(1,1,5)/c = 22 the second proved instance, not the first.

## (4,4,16) discrepancy CLOSED (B547)

The recorded (4,4,16) discrepancy is resolved: it is a PROVED all-hyperbolic
ghost (inert-prime obstruction u²−3v²=7, 7 inert in ℚ(√3); trace-4 slot disc
12, h=1, complete). chat-2's "realizable/false candidate" claim is refuted;
no witness exists. See B547.
