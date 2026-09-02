# Addendum (2026-09-02) — the join skipped a step; the step, computed, is a positive datum (B1235)

**Codex R036, correct:** "A6 ⇒ amphichiral ⇒ k-blind wall" needs CS = 0, but amphichirality forces only
CS ∈ {0, ¼} (B1224). The arc's chain proved the first arrow and assumed the second.

**The step computed** (`frontier/B1235_two_seat_harvest/verification/a6_cover_cs.py`): all **40** orientation double
covers of the arc's slice (`NonorientableCuspedCensus[:40]` — named here; the arc's text did not name it) have CS = 0
(0 at ¼), against a **36 %** quarter-rate (16/44) among amphichiral manifolds in general (13/38 in the 112-family,
3/6 in the 200-census slice). P(40/40 by amphichirality alone) ≈ 0.64⁴⁰ ≈ 2 × 10⁻⁸. A6's free deck selects the CS = 0
stratum. **Data, not theorem** → L194.

**Also:** `a6_built_the_walls.py:71` records `same_trace_field` as a literal string, not a computed boolean; the arc's
verdict does not rest on it, but it must not be read as a check. The chirality test the arc used
(`symmetry_group().is_amphicheiral()`) is the correct one — it is why B1234 stands while B1181 falls.
