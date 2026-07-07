# B458 — PREREGISTRATION: Ethogram E5 — the per-component CS test (the handoffs' decisive computation)

**Committed before computation. Firewalled. Merges the 2026-07-07 handoffs' Tests 1+3
(SL(3) component internal content + CP on V₁/V₂) under the campaign's discipline.**

## The question (blind)

The complex volume (Vol + i·CS) of EACH irreducible SL(3) boundary-unipotent component of the
figure-eight — V₀ (geometric line, ℚ(√−3)) and the V₁/V₂ pair (the ℚ(√−7) conic) — their mutual
relations (ΔCS), and the ℤ/3-center behavior; the identical pipeline on 5₂ (control).

## GATE #1 (runs FIRST, binding on the reading): the amphichirality pairing

If the mirror involution swaps V₁ ↔ V₂, then CS(V₁) = −CS(V₂) is FORCED — Chat-1's outcome (b)
("CP violation exists on each component but cancels") is then the *expected generic* outcome,
not a discovered SM mechanism. **The finding, if any, is the VALUE of CS(V₁) (a new exact
number), never the cancellation pattern.** Pre-registered readings:
- (a) CS(V₁) = CS(V₂) = 0: the symmetry holds all the way down (dead-flat, consistent).
- (b) CS(V₁) = −CS(V₂) ≠ 0 **with the pairing confirmed**: FORCED pattern; bank the value as
  ℚ(√−7)-component arithmetic; adjudicate the value itself (whitelist F or escalate).
- (c) any other pattern (equal nonzero; unpaired): contradicts the pairing — anomaly, adversarial
  recompute before anything else.
- Control comparison: 5₂'s per-component CS through the same pipeline; forced/laundered
  adjudication only (knot channel, no p-values).

## BLOCKING lit-gate

The handoff's "nobody has computed component-level CS of SL(3) knot components" is presumed
FALSE: the Ptolemy database (Goerner; Garoufalidis–Goerner–Zickert, exact computations of
boundary-unipotent SL(N) reps and their complex volumes) publishes precisely these numbers;
`retrieve_solutions()` fetches them. Our delta = the CP-pairing question + the fig-8-vs-5₂
comparison + the ℤ/3-center action — NOT the CS values. Any novelty claim beyond that is barred.

## Machinery & fallbacks

SnapPy `ptolemy_variety(3,'all')` → `retrieve_solutions()` (database; requires network) →
`complex_volume()` per solution; component ID by number field (B444's eliminations: ℚ(√−3) line
vs ℚ(√−7) conic). Fallback if retrieval fails: exact solutions by back-substitution from B444's
Groebner bases + the named boundary for the CS evaluation (the extended-Bloch computation is out
of sandbox scope without the database). ℤ/3-center: the action of the center on the Ptolemy/
obstruction data (how the obstruction classes and solutions permute).

## MB-guards
The value-of-CS(V₁), if nonzero, is HELD(value-matching) against any physical constant by
default (S055/S054 rules); the Jarlskog framing is a NAME, not an identification (the handoff's
own firewall note). Escape hatches (networks/4d-lift/categories) remain set aside.
