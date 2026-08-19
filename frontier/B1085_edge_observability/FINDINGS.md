# B1085 — EDGE OBSERVABILITY: the free half materializes at the cut, and the two hands of one cut differ 5-vs-6

**Date:** 2026-08-19 · **Verdict: PROVED (rule-level; 1d; no SM claim)**
**Provenance:** the outside bench's V.3. **Fully re-derived on this bench with own code**,
including one construction subtlety the re-derivation itself exposed (§3).

## 1. The claims, re-established here

Fibonacci Hamiltonian (hopping 1, on-site λ=1 on the 'b' letters) on the half-line with a
Dirichlet cut. The two hands = **the two sides of ONE cut** of the bi-infinite golden
Sturmian word at cut phase ρ = α = 2−φ: the right half read forward, the left half read
outward. Then, re-derived exactly here:

- **Bulk hand-blindness:** the integrated densities of states of the two hands differ by
  AT MOST ONE state at every energy, at every tested size (N = 987, 1597, 2584, 4181) —
  the hull theorems (phase-blindness, palindromy, amphichirality) made visible as a
  finite-size count.
- **The edge sees the hand:** boundary-localized states differ **5 (right hand) vs 6
  (left hand)**, with every energy reproducing the source bench's values to every printed
  digit (right: −1.5305, −0.9160, −0.5039, +0.4704, +2.0303; left: −1.6041, −1.1584,
  −0.3064, +0.4474, +2.2987, +2.4385), stable across N.
- **The phase-dependence IS the mechanism:** sweeping the cut phase ρ changes the edge
  content (ρ=0 and ρ=1−α give different counts and energies). What appears at the cut
  depends on exactly the torsor point the bulk withholds — the free data is not
  unobservable, it is edge-observable, and ONLY edge-observable.

## 2. Physics-standard register

Same shape as domain-wall fermions / bulk–boundary correspondence — the register in which
the SM's own chirality is standardly engineered. Composition with the blanket layer
(S072/B761, banked): everything forced is boundary-visible; everything free is
boundary-only; the boundary is the total interface. Scope: one-dimensional, rule-level,
numerics at machine precision; no SM spectrum claimed. Feeds the laboratory lead (L173's
prereg spec: photonic/polariton Fibonacci chains scan ρ directly — the honest prediction
is the FUNCTION ρ ↦ edge content, gap-labeled).

## 3. The sobriety catch (this bench's own, found during re-derivation)

**The ba-hand cannot be built by naive substitution iteration.** The a→ba, b→a iterates
do not nest as prefixes (the starting letter alternates with iteration parity), so "the
first N letters of the limit" is ill-defined and produces N-unstable edge counts — this
bench's first two constructions produced 4/6/4 and then 9 stably, neither matching, until
the source's actual construction (ONE cut, two sides) was implemented, at which point
every number reproduced exactly. Recorded as a construction hazard for every future use:
**the two hands exist only as the two sides of one cut, not as two independent words.**

**Locks:** tests/test_b1085_edge_observability.py (N=987 both hands: IDS diff ≤ 1;
edge counts 5 and 6; the five right-hand energies to 1e-3). Own-code scripts archived in
the arc dir.
