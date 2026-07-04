# B408 (Phase 1b) — PRE-REGISTRATION: the seam-channel hierarchy test

**Committed before computation. THE question left standing by the Wall Campaign: the
singles channel contracts (A2) — does the SEAM channel contract too, or is the boundary
channel the object's one scale lever?**

## The registered comparison

- Level 15: the (1,2) pair table's √−15-envelope: max over cells of |s| (exact; the
  banked max is 1/48 — re-derived from step0 as the gate).
- Level 45: the banked E16 pair table (sweep45.json, 12-dim basis {1,c₁,c₂}⊗H): the
  √−15-sector of a cell is s_bare + s_c1·c₁ + s_c2·c₂; its envelope = max over cells AND
  over the three real embeddings of ζ₉⁺ (c₁ → the conjugates). Exact coefficients;
  numeric evaluation only for the envelope comparison (honest: the comparison is of real
  magnitudes).

## Registered outcomes (two-outcome, both bank)

- **CONTRACTION** (envelope₄₅ < envelope₁₅ = 1/48): the seam contracts like the singles —
  Wall 1 closes completely: THE OBJECT HAS NO SCALE LEVER in any tested channel; the
  masterplan's Phase 5 gates on the coupling-channel theory only (no hierarchy hope).
- **PERSISTENCE/EXPANSION** (envelope₄₅ ≥ 1/48): the boundary channel does NOT contract —
  the seam is a genuine scale-lever candidate; Phase 2 gains a quantitative target (the
  seam envelope's level-dependence law).

VACUITY GUARD: both outcomes are live (the singles contracted 1/4 → 1/12-scale, so
contraction is possible; the 45-table's c-dressing could push magnitudes either way).

## ADDENDUM (2026-07-04): the 135 NUMERICAL SCOUT (registered before running)

The exact 135 sweep (36-dim identification) is a Phase-2 job. The envelope question
admits a numerical scout: compute the Par-graded pair table at complex embeddings
(numpy, float64), extract the √−15-sector per cell by the 4-fold Galois combination
(s-part = [T(e) − T(e·a₅) − T(e·a₃) + T(e·a₅a₃)]/(4·√−15(e)) with a₅/a₃ the
√5-only/√−3-only flip exponents), and take the max magnitude over cells × ζ-embeddings.

**THE GATE (binding):** the identical pipeline must reproduce (i) env₁₅ = 1/48 and
(ii) env₄₅ ≈ 0.02535468 (the banked exact verdicts) to ≤ 1e−8 relative error. If the
gate fails, the scout is void.

**Registered outcomes at 135:** GROWTH (env₁₃₅ > env₄₅ — the lever strengthens; the
growth-law question opens), PLATEAU (≈ equal), CONTRACTION (the 45 excess was a blip).
Scout verdicts are labeled NUMERICAL-SCOUT; exact confirmation = the Phase-2 sweep.
