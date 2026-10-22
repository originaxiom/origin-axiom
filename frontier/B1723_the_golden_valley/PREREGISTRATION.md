# B1723 — PREREGISTRATION: THE GOLDEN VALLEY (the completion map's C3; L254, P-069) — with τ anywhere on the valley of the weave's own modular-invariant F = Σ_p ∣θ_p/η∣⁴ at its golden value 8 (the discriminant-5 locus), and any line of order ≤ 12, do the six ratios and the quark mixing come out, specifically?

cc (main), 2026-10-22, after B1722. **Sealed before `verification/the_golden_valley.py` and `verification/compare.py`
run.** A test of a structure, not a value derived. 0 of 19.

## Why

The completion map's C3 (L254, P-069) asks for τ as a field: a modular-invariant functional of the weave's forms whose
valley is the golden locus.
- **The record already holds the functional's ingredient.** B1636's F = Σ_p ∣θ_p/η∣⁴, built from the three theta constants
  and η, is modular-invariant. Its golden value F = 8 holds on the discriminant-5 geodesics, by the golden identity proved
  from Ramanujan's quintic (B1638, B1639). So (F − 8)² is a modular-invariant functional whose zero set, its valley, is
  that locus.
- **The canonical functionals pick ω or the cusp** (W51; F itself is least at ω, 7.56). The golden valley is the record's
  one named non-symmetric locus.
- **A valley fixes τ only to a curve.** Whatever second term picks a point along it, the point lies on the valley. So if
  no point of the valley, with any line, reproduces the six ratios specifically, no functional with this valley can do so
  in this frame. That is the test.

## The model (no data)

- **The valley.** Modulo SL(2, ℤ) the discriminant-5 locus is one closed geodesic, the tick's (the axis of LR, through
  i, of length 4 log φ). In the fundamental domain it is the two mirror arcs ∣τ ∓ ½∣ = √5/2 from i to ±½ + (√5/2)i, each of
  hyperbolic length log φ, at heights 1 to 1.118.
  - **Checked (geometry, no data):** F = 8 at every sampled point. On 41 vertical lines of the fundamental domain up to
    Im τ = 4, F − 8 changes sign exactly once, on the arcs, to 4 × 10⁻¹⁵. So in that region the valley is the arcs and
    nothing else.
- **The points:** 25 per arc, equally spaced in arclength, with i counted once: **49 points**.
- **The lines:** every flat line w = ατ + b of exact order N, 2 ≤ N ≤ 12, up to sign: **265 lines**. The set is
  SL(2, ℤ)-invariant, so sampling the fundamental domain suffices; the tick's own lines (order 5, B1698) are among them.
- **The frame, as B1712, B1713 and B1720:** the section ∂R (one unit on v₊; B1700); B1667's canonical end at both
  horocycles, with L read at Im τ from its Re τ = ¼ column; B1656's coupling; B1660's three up readings. V = U_u^H U_d.
  - The instrument asserts its own domain: every point has 1 ≤ Im τ ≤ 4 (B1667's tabulated range), so no end radius is
    clamped.
- **No continuous number is free but the position along the valley.** The discrete choices are the line, the horocycle
  and the reading. **77 910 mass rows.**

## Cells

| cell | prediction | prior |
|---|---|---|
| **T1** | some (point, line, horocycle, reading) puts all six ratios within a factor 3 | 10% |
| **T2, specific** | at most 1% of 4 000 random hierarchical target sets (B1695's prior) fit at least as well with the same rows | 2% |
| **T3** | the minimum χ² is below 16.75 | 2% |
| **K1** | some row puts PDG's ∣V_us∣, ∣V_cb∣, ∣V_ub∣ within a factor 3 | 40% |
| **K2, specific** | at most 1% of 4 000 random hierarchical mixings (B1713's prior) fit as well | 3% |
| **K3** | some row puts all nine within a factor 3 | 5% |
| **K4, specific** | at most 1% of random nine-target sets fit as well | 2% |
| **C1, control** | the same configuration in another basis gives the same six ratios, on the first 12 lines of order neither 4 nor 12, ratios below 10⁻¹⁰ not compared: (i) the apexes −½ + (√5/2)i and ½ + (√5/2)i are one point, τ → τ + 1 with (α, b) → (α, b − α), ∣log∣ < 10⁻⁶; (ii) at i, the fixed point of S, τ → −1/τ = i with (α, b) → (−b, α) and the end unchanged (L′ = L + log∣τ∣ = L), ∣log∣ < 10⁻⁶ | 95% |

The calibration seed is 1723. Read-outs:
- the best row's point (arc and arclength), line, order, horocycle and reading;
- the best per line order;
- ∣J∣ at the best mixing row.

**The reading, written before the run.**
- **If T2 holds,** the golden valley holds a point that reproduces the data specifically. The functional's second term,
  which must pick that point along the valley, becomes the question. It is graded a READING with its tags (Λ, the unit,
  H-cov, the canonical end, the functional's choice of the golden value 8).
- **If T1 fails,** the valley sits too low (Im τ ≤ 1.118) for the frame's hierarchy. No functional whose valley is the
  golden locus produces the six ratios in this frame, and C3 is closed in it. The golden spectrum stays B1636's, in the
  older coupling.
- **If T1 holds and T2 fails,** the valley comes near but not specifically, as B1720's threads did.
- **C1 failing** would mean the construction depends on the basis. The read-out would then be the representative's, and
  stated so.

## Seen first

`VERDICT topic-sweep /golden valley|discriminant-5|discriminant 5 (locus|geodesic)|F ?= ?8|tau as a field|τ as a field|modular-invariant (potential|functional)|valley/ (full text): 48 of 1494 arcs on main match (NEGATIVE 4, OPEN 2, PROVED 41, RETRACTED 1)`.
Most matches use "valley" in other senses. Bearing on it:
- B1636 (the golden spectrum on the tick's geodesic; F = 8 there);
- B1638 and B1639 (the golden identity, proved from Ramanujan's quintic);
- B1657 (D vanishes on ω's orbit; W87);
- B1712, B1713, B1720 (the frame's line census, τ free at Im τ 1.5–3.5, and at the threads' apexes).

None puts τ on the golden valley in B1656's frame at the canonical end. **Literature:** modular-invariant potentials for
the modulus and their minima at or near the fixed points (the modular-flavour vacuum-stabilisation literature); standard.

## Disclosed

- **Known before the seal:**
  - the six measured ratios and PDG's moduli;
  - B1712, B1713: the τ-free best fits cluster at Im τ ≈ 3.1, and no line of order ≤ 12 fits specifically;
  - B1720: the valley's top, ½ + (√5/2)i, is the LR thread's apex. There, with its own fixed lines (order 5), the best
    worst factor was 4 506;
  - B1722 and its after-read check.
- **Expected direction, stated before the run:** the valley is low (Im τ ≤ 1.118) and B1720's LR apex was far off, so T1
  is expected to fail. The test is run because the other 263 lines and the rest of the valley have not been seen.
- **Model values seen before the seal:**
  - the geometry only (the arcs, F = 8 on them, the level-set check, the line count);
  - **the covariance pre-check,** run with the instrument's own `control` on its 12 lines. It read ratios but compared
    them only across bases: T ≤ 1.5 × 10⁻¹³ and S ≤ 6.2 × 10⁻¹⁴.
- **Redundancy, disclosed:**
  - at i, lines related by S give identical ratios;
  - mirror points on the two arcs, with mirror lines, give identical ratios;
  - i has Re τ = 0, where B1713's family applies: the up and down quarks vanish on order-12 lines with 12α odd (P-292);
  - lines of order 4 (all sectors) and of order 12 (the leptons) carry an exact first-generation zero (B1716) and fail
    by construction. They are kept.
- **L is read from B1667's Re τ = ¼ column at the point's Im τ, as B1712 did.** The end varies with Re τ by a few per cent
  on B1667's grid (L_max 0.64–0.69 over the whole grid).
- The instruments were import-tested before the seal; importing them computes no ratio.

## Instruments

- `verification/the_golden_valley.py` (no data) → `the_golden_valley.json`.
- `verification/compare.py` → `comparison.json`.
- B1656's functions copied verbatim (`verification/b1656_funcs.py`, identical to B1712's and B1720's). The hashes are in
  `ARTIFACT_HASHES.txt`.
