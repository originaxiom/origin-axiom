# B1632 — PREREGISTRATION: THE SM SEAT'S W45 VERIFIED ON MAIN — the triplet's Riemann–Roch number on the weave's own surface, by main's own route, now that the owner's tagging of the cusp's unit makes it load-bearing

cc (main), 2026-10-09, after S109. **Sealed before `w45_on_main.py` runs.** No data. 0 of 19.

**Why it matters.** The owner tagged the unit of end data at the weave's cusp as a working postulate (GENESIS v1.39).
Its payoff, "given Λ and the unit, the weave's surface carries a four-dimensional index ±3", rests on the SM seat's W45
and W46, which main registered without re-running. The owner's rule (verify load-bearing mathematics) and the audit
instruction of the same day both ask main to compute it. This arc computes W45's core from scratch by another route:
χ_{3/2}(ρ_T) = 0 at the weight the geometry forces, and one unit on every component adds dim T = 3. W46's puncture
conditions are not covered here.

## Seen first

`VERDICT topic-sweep /vector-valued modular|Borcherds|Skoruppa|Riemann-Roch|metaplectic|W45/: 4 of 1403 arcs on main match (NEGATIVE 2, PROVED 2)`
— B1627 and B1631 (W45, W46 registered; the unit tagged), B1630 (the S-lift R L⁻¹ R), and the SM seat's relay §47 and
§48 with W45's method (the same formula, calibrated on the trivial representation, η and W41's Weil representation).
**Literature:** the dimension formula for vector-valued modular forms (Borcherds, *Reflection groups of Lorentzian
lattices*, §7; Skoruppa), used as a Riemann–Roch number χ_k(ρ) = dim M_k(ρ) − dim S_{2−k}(ρ^∨).

## Disclosed

- **Not an independent method, an independent computation.** The formula is the one the seat used. Main writes its own
  code, builds ρ_T from its own lifts (B1611's construction), and tests every identification of S and T with them
  rather than assuming the seat's.
- The convention for the centre's consistency (ρ(S)² = e^{−πik}) is fixed by the η calibration in C0. If C0 fails, the
  instrument is wrong, and that will be said.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **C0** | the calibrations hold: trivial χ₀ = 1, χ₂ = 0, χ₄ = 1, χ₆ = 1, χ₁₂ = 2; η: allowed at ½, χ_{1/2} = 1 | 90% |
| **C1** | among (S̃^{±1}) × (L^{±1}, R^{±1}), the Mp2(Z) relations hold for (S̃, L⁻¹), the seat's ρ_T, and for at least one more | 70% |
| **C2** | for ρ_T: weight 3/2 allowed and χ_{3/2} = 0; its dual not allowed at 3/2; χ first reaches 3 at weight 23/2 | 65% |
| **C3** | given the unit, χ_{3/2} + 3n = 3 at n = 1: one unit gives the triplet's 3 | 95% (arithmetic given C2) |

**The reading, written before the run (the cells can only lower it).** If C0–C2 hold, W45's core is verified on main by
its own computation. In its canonical reading the weave's own surface carries no chiral count, and one unit at the cusp
gives exactly three. The postulate's payoff then rests on verified mathematics, with W46's puncture conditions still
registered rather than recomputed.

## Instruments

`verification/w45_on_main.py`; hashes in `ARTIFACT_HASHES.txt`.
