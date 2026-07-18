# B678 — THE D4 ANNEX BANKED: THE FULL 8x12 LADDER TABLE (main seat,
# 2026-07-18; cc2's annex as-received sha-prefix 54d64048, privacy-
# patched; their FINDINGS_CC2.md alongside)

## Verify-on-receipt (this seat, from the MERGED json directly)

- NO GROWTH ANYWHERE: any_growth_any_level = False; zero failed gates
  across all 12 levels, 96 cells. CONVERGENT with B669's independent
  route (the exact certificate ladders, Artin periodicity ⇒ bounded):
  two methods, same Track-H refutation — chat1's amphichiral-
  suppression mechanism has no empirical support at any level κ = 4..15
  on any metallic word n = 3..10.
- THE OWN-CHANNEL SIGNATURE verified exactly: golden |Z| = 1/φ at
  κ = 5, 10, 15 (diff ~1e-16 all three).
- THE CROSS-CAMPAIGN NUMBER verified exactly: (n = 4, κ = 12) cell
  = √3 − 1 (diff ~1e-16) — reproduces this seat's banked B4-landscape
  value. Two campaigns, one number, now three independent computations.
- The ceiling map recomputed from the raw 96 rows on this seat matches
  cc2's stated map: {3:1, 4:1, 5:2, 6:1, 7:2, 8:√3, 9:2, 10:1.785…}.
  The ceiling is resonance-structured, NOT disc-monotone (golden = 1
  is the minimum, tied with n = 4, 6) — the monotone-in-conductor
  hypothesis is REFINED as cc2 states.
- The (10, κ=8) value 1.7849887… stays UNIDENTIFIED: this seat's
  independent identification attempt over ℚ(√2,√3,√5,φ) found nothing
  clean (nsimplify returns junk). Honestly open; HINT_LEDGER row.

## The engineering bank (adopted)

cc2's diagnosis: the shared engine_v7.gate_report() recomputes a full
O(N³) product inside every (i,j) scan — O(N⁵) total; their local
fast_gate_report (compute-once, O(N²) scan) took every level from
hours to < 15 s, making the level-10 cap moot — the FULL prereg table
including the κ = 14, 15 resonances is banked. Their upstream
recommendation is REGISTERED as a priced door: patch engine_v7
in-place with behavioral equivalence proven against the existing
locks before merge (any cell importing gate_report at N ≥ 40 pays
the same tax until then).

Locks: tests/test_b678_d4_annex.py.
