# B1941 — A fermion determinant prefers one Higgs world at every sampled point [title corrected 2026-11-17, Review 83: it read "at every point"; the sign reverses near τ = i], and a one-loop trace prefers the other: X-SURVIVAL's S4 picks the world only once its functional is chosen

**Verdict: PROVED** (as computed, on 28 points of the modular surface; that the sign holds at every point is not
proved). Main, 2026-11-14, before the big run's look, so that no Higgs world is preferred after its output is read (the
sweep's S17). The test is P-831's: name what the selection declares, change each declared move, and see whether the
selection survives. Register rows P-847, P-831, P-850. **No measured value enters.** 0 of 19.

## Seen first

- **Swept:** `VERDICT topic-sweep /Berezin|fermion determinant|ln det|log det|Higgs world|W\+|global bit|X-SURVIVAL/: 6 of 1680 arcs on main match (OPEN 2, PROVED 4); 2 register rows match (QUEUED 2)`.
  - B1932 and B1936 carry the two worlds, and P-847 the bit.
  - X-SURVIVAL is agy-exp's card, harvest row 1815, read through the mask.
- **The literature:** integrating out chiral fermions gives the determinant of their mass operator, and a one-loop
  effective potential carries its traces. Neither fixes how they weigh two branches with no symmetry between them.

## The claim tested
agy-exp's X-SURVIVAL S4 (its sealed output says it holds) weights each Higgs world by
F_ferm(W) = ⟨3 ln det Ĥ_u + 3 ln det Ĥ_d + ln det Ĥ_e⟩, with Ĥ_f = (Im τ) Y_f† Y_f, the weave average of the
fermions' Grassmann integral. Its expectation was that W₋ = (up S̃, down S, leptons S) dominates
W₊ = (up S, down S̃, leptons S̃). Beside it the card lists a one-loop term, −⟨3 Tr Ĥ_u² + 3 Tr Ĥ_d² + Tr Ĥ_e²⟩.

## What was computed (`s4_pointwise.py`, main's code)
- **The difference.** Δ(τ) = F(W₋) − F(W₊) is computed pointwise, before any average. The frame is computed in extended
  precision (B1940's frame), averaged over the 24 points of order 5.
- **The sectors.** At level 5 the leptons' coupling is the down coupling transposed (B1934), so their determinant is
  the down determinant, and the colour weights act as (3 on up, 4 on down).
- **The points.** 28 points were taken on the modular surface, from height 0.9 to 9 (seed 1939). *[CORRECTED 2026-11-17, Review 83, agy-002's R83-17: the four draws at height 0.9 fall below the unit circle and were rejected, so the 28 points span heights 1.2 to 9.]*
- **If Δ has one sign at every point,** every measure (the move count, the area, any other) gives that sign. Then the
  measure is not a declared move this selection depends on.

| the functional, and the declared moves | positive at | Δ from | to |
|---|---|---|---|
| ln det, colour weights (3, 3, 1), exact weight | **28 of 28** | +1.38 | +6.44 |
| ln det, colour weights (3, 3, 1), truncated weight | 28 of 28 | +1.38 | +6.39 |
| ln det, weights (1, 1, 1), exact weight | 28 of 28 | +0.61 | +2.98 |
| ln det, weights (1, 1, 1), truncated weight | 28 of 28 | +0.61 | +2.97 |
| −Tr Ĥ², colour weights (3, 3, 1), exact weight | **0 of 28** | −3.2e21 | −4.2e-2 |
| −Tr Ĥ², weights (1, 1, 1), exact weight | 0 of 28 | −3.0e21 | −2.2e-2 |

## What it means
- **With the determinant, the preference is robust.** The fermion determinant prefers W₋, the record's practice, at
  every sampled point. That holds with either colour weighting and either channel weight. So no measure can reverse it. *[CORRECTED 2026-11-17, Review 83, agy-002's R83-17, recomputed by main (B1950; the output is `verification/near_i_run.txt`, committed at Review 84): false. Near τ = i the sign reverses: at τ = 1.05i the difference is −0.39 with the colour weights (3, 3, 1) and −0.12 with (1, 1, 1), and it vanishes at i. The sample never went below height 1.2. So the determinant prefers W₋ at the 28 sampled points, not at every point, and a measure concentrated near i reverses it.]*
  This is a stronger form of the seat's S4, and it agrees with it.
- **With the trace term, it reverses.** The one-loop term the seat lists beside it prefers W₊ at every sampled point. Its
  size grows with the frame's overall coupling scale, which frame C does not fix (C08), whereas the determinant's
  difference is scale-free.
- **So the selection is not a derivation.** The determinant would fix the Higgs world; the trace would fix the other.
  The choice between them, or their relative weight, is the decisive declared input. By P-831's test, S4 is a candidate
  principle conditional on its functional: "the world is the one the chiral fermions' determinant favours."
- **What would settle it is an action.** One stated action whose fermion integration gives the determinant, and whose
  one-loop terms are fixed with it, would decide between the readings (the dictionary run's open item: one action, its
  induced kinetic terms and its potential).

## What the wall teaches
- **A preference that survives every change but one has found its real premise.** Here the premise is the functional.
- **The two candidate functionals here disagree at every point,** not on average. Averaging cannot hide the choice.

## Not claimed
- That W₋ is physical.
- That the sign holds everywhere off the 28 points.
- Anything about the run's options. The run reports all four, none preferred, and this arc is committed before the
  look so that nothing here is used after it.
- Any value.
