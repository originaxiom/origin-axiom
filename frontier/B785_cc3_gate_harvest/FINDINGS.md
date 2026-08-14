# B785 — the cc3 gate harvest (cc, 2026-07-25)

Owner directive: "process and verify them all" → the five cc3 audit-seat branches were
gated (each load-bearing claim reproduced in-sandbox). This arc banks the deliverables
that PASSED, re-derived independently in `compute.py`. cc3's branches are NOT merged; cc
is the sole gate. Gate 5-Q; nothing to CLAIMS.

## Harvested (independently reproduced, exact)

| id | claim | source branch | status |
|---|---|---|---|
| H1 | B768 correspondence: T=[[1/φ²,1/φ],[1,0]] row-stochastic, eigenvalues {1,−1/φ}; (1−φ)²=φ⁻² | audit/b768-correspondence | CONFIRMED |
| H2 | B489: torsion = \|L(2n)−2\| = (φⁿ−φ⁻ⁿ)² ≥ 5 for n≥2 (n=1..16) | hunt/r28-10-stabilizations | STABILIZED |
| H3 | TOMB-L255: Sym^d(diag(φ,−1/φ)) spectrum = {(−1)ʲφ^{d−2j}} (d=1..12) | hunt/r28-10-stabilizations | STABILIZED |

These corroborate/close the corresponding main arcs (B768_correspondence_crosstest,
B489_self_interaction_tower, B767_stabilizations). H2/H3 are structural closures (all n /
all d, by Binet and by the Sym^d polynomial-functor spectrum).

## Cited, NOT re-run (honest provenance)

- **P1 WALL-7** (hunt/wall7-twisted-extension): cc3 sampled 18 weld points of the twisted
  f3 system, all dim=0. This is a **sample**, not a generic proof (which needs many more
  points — the entry-degree and minor-degree bounds disagree, 53 vs 865, worth reconciling).
  Inspected cc3's `wall7_output.txt`; **not** independently re-run here (requires the B575
  infrastructure and ~36 s/point). Recorded as evidence, not as a cc computation.

## Explicitly EXCLUDED at the gate

- The **b769 / C21 "tangent frames align → chord = c⊕θ"** mechanism did NOT pass: it is the
  c-odd/θ-odd conflation (on Sym²(SL(2)) traces θ is trivial, so `d/du[tr Sym²(AB)]|_ω =
  −5+i√3` has θ-odd part exactly 0 and its Im part is c-odd). cc3's b769 audit re-confirmed
  C21 without catching this. C21's *mechanism* was corrected in main (2026-07-25); the
  theorem (discrete T1, no invariant continuous modulus) is unchanged. Same class as the
  retracted B780 gate and cc3's B784.

## Forks (F1–F4)

Firewall-side (Gate 5-Q, priced C18, no CLAIMS): received, not gated. The F1 Ferroni
softening is the one actionable hygiene item; K.C. remains the honest residual.

Lock: `tests/test_b785_gate_harvest.py`.
