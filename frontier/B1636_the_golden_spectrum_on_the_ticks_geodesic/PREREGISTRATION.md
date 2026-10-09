# B1636 — PREREGISTRATION: THE GOLDEN SPECTRUM ON THE TICK'S GEODESIC

cc (main), 2026-10-09, after B1635's run. **Sealed before `golden_on_the_ticks_geodesic.py` runs.** No data. 0 of 19.

**Why it matters.** B1635's post-seal read-out (unpredicted) found the weave's lowest symmetric coupling on the ruled
branch (O⁺ at k = 1, one-dimensional, so canonical up to scale) giving normalized masses (1, 0.618033989, 0.381966011) at
13 of 13 points of the tick's closed geodesic (the axis of LR, |τ − ½| = √5/2, through i), and (1, 1/φ, 1/φ²) at i to
10⁻¹⁶; at generic τ it does not. If the spectrum is constant on the tick's whole geodesic, then a sector at that weight
has its mass ratios fixed by the principle's tick, with no free number for them — a direct bearing on the owner's question
of how many free numbers the principle leaves. This arc tests the read-out with controls before anything is built on it.

## Seen first

`VERDICT topic-sweep /golden mass|mass ratio.*phi|phi.*mass ratio|1 : 1/phi|geometric hierarch/: 1 of 1407 arcs on main match (PROVED 1)`
(B963, a word match: its sentence is about values in general); the broad sweep `/golden|tick's geodesic|closed
geodesic|mass spectrum|sum rule/` matches 168 arcs, the golden ratio being everywhere in this record; `already_banked`
returns no golden mass spectrum. B1629 (the tick LR the unique lowest closed geodesic of the weave, √5/2), B1630 (the
tick's point i), B1635 and its post-seal Q1–Q4 (read before this seal). **Literature:** none located for a golden
spectrum of a vector-valued modular form on a closed geodesic; the sum rule below is elementary linear algebra.

## Disclosed

- **Not blind.** The golden spectrum on 13 points of the tick's geodesic, and its exactness at i, were seen before this
  seal (B1635's post-seal Q1, Q4). G1 tests it on 66 points; G4 and G5 are the controls, not yet computed.
- **G2 is a theorem, checked as a control.** A zero-diagonal complex symmetric 3 × 3 matrix can be rephased (Y → D Y D,
  D diagonal unitary) to positive real off-diagonal entries; its eigenvalues then sum to zero with one positive and two
  negative, so its singular values satisfy m₁ = m₂ + m₃. So every O⁺ coupling, at every τ, obeys that sum rule, and on
  the golden locus the characteristic polynomial is λ³ − 2λ − 1 = (λ + 1)(λ² − λ − 1).
- Sample points keep Im τ ≥ 0.27 (the series and the division by η¹⁸ keep full precision there).
- **No data.** Whether a golden spectrum resembles any observed mass ratios is not looked at here; any comparison is a
  separate, sealed arc under the value-contact checklist.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **G1** | O⁺ at k = 1 has normalized masses (1, 1/φ, 1/φ²) within 10⁻¹⁰ at all 66 points of the tick's geodesic and its LR-images | 90% |
| **G2** | every O⁺ coupling (k = 1, 3, 5, 7; generic members) at 12 random τ obeys m₁ = m₂ + m₃ within 10⁻¹² | 97% |
| **G3** | read-out only (the entries' moduli and the theta ratios along the geodesic); no prediction | — |
| **G4** | O⁺ at k = 1 is not constant (spread > 10⁻³) along any of the five other closed geodesics (L²R, LR², L²R², L³R, LRLR²) nor along any of the three reflection lines | 60% |
| **G5** | O⁺ k = 3, D k = 5, D k = 7 and generic members of O⁺ k = 5, D ⊕ O⁺ k = 5 and O⁺ k = 9 are not constant (spread > 10⁻³) along the tick's geodesic | 65% |

**The reading, written before the run (the cells can only lower it).**
- **If G1, G4 and G5 hold,** the golden spectrum belongs to the tick and the lowest coupling together. On the principle's
  own closed geodesic, the weave's lowest symmetric coupling has the τ-independent masses 1 : φ⁻¹ : φ⁻² (m₁ = m₂ + m₃
  with m₁/m₂ = m₂/m₃ = φ). A sector at that weight on that locus would leave no free number for its mass ratios.
- **If G4 fails,** constancy is a property of the coupling on a wider class of curves, and the tick is not singled out.
- **If G5 fails,** constancy on the tick holds for more couplings, which is a wider law.
- In every case, whether the principle puts τ on its tick's geodesic is not decided here.

## Instruments

`verification/golden_on_the_ticks_geodesic.py` (imports B1635's sealed instrument); hashes in `ARTIFACT_HASHES.txt`.
