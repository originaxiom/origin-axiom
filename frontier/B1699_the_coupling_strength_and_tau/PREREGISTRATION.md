# B1699 — PREREGISTRATION: THE COUPLING'S STRENGTH AND τ (P-247) — does this frame's own coupling strength select a τ, and at the τ it selects, do the six charged-fermion ratios come out, specifically?

cc (main), 2026-10-21, after S170 (B1698). **Sealed before `verification/the_strength.py`,
`verification/the_selected_tau.py` and `verification/compare.py` run.** A test of a structure (B1637's checklist), not a
value derived. 0 of 19.

## Why

The scan for misses (B1697, item 4) found W51's remark on record and unused: the lowest cusp-form couplings' norms peak
at τ ≈ 1.551 i and ½ + 2.224 i in the SM seat's frame — "a principle that extremizes a coupling's strength would select
them. None is on record" (rows 1075–1076; registered, not recomputed). P-247 asks it of this frame's own coupling: B1645's
covariant Y(a) = a Rᵀ + R aᵀ − (a·R) 1 with the Higgs of B1694–B1698, a = ∂R (weight 3/2; Y of weight 1). Its
modular-invariant strength is y·s₁(Y)² (the top Yukawa's Petersson-normalised strength; the theta triplet's T and S
matrices are orthogonal up to a scalar, so the moduli of its dot products are covariant).

## The selection rule (fixed before the strength was computed; disclosed below)

The selected τ: the critical points of y·s₁² for ∂R in the fundamental domain other than the elliptic points i and ω
(which every invariant function has); the global maximum if it is one of them. If the only critical points are i and ω,
P-247 selects nothing beyond the principle's points. Reported, not used to select: the Frobenius strength y‖Y‖²_F and
the unit-free Higgs a₀ = ∂²R − E₄R/48 (weight 7/2; B1697).

## The model and the cells

At the selected τ (with Re τ > 0; the strength is reflection-invariant): every flat line w = α τ + b with
(α, b) = (j/24, k/24), j, k = 0…23 (576 lines, every line of order dividing 24); the section ∂R; B1667's canonical end
(both horocycles; L interpolated in Im τ from B1667's column at Re τ = 0.25); B1656's four-channel coupling; B1660's
three readings of the up sector. No continuous number: 576 lines × 6 discrete choices.

| cell | prediction | prior |
|---|---|---|
| **S0, the selection** | the strength's critical points other than i and ω lie on the arc ∣τ∣ = 1 only; y·s₁² for ∂R increases toward the cusp without a maximum | 85% |
| **H1** | some line and choice puts all six ratios within a factor of 3 | 3% |
| **H2, specific** | at most 1% of 4 000 random hierarchical target sets (B1695's prior) fit at least as well | 1% |
| **H3** | the minimum χ² is below 16.75 | 0.5% |

Read-outs: the selected τ and its kind; the best line and choice; the smallest model ratio in each of the six slots over
all rows.

**The reading, written before the run.** If H1 fails: the frame's own coupling strength does not select τ where the
masses are — its one non-elliptic critical point sits at the bottom of the fundamental domain and the strength has no
maximum (it grows toward the cusp: ∂R carries one unit of end data, B1697) — and P-247's lead closes for this frame;
W51's peaks belong to the seat's frame of cusp-form couplings, which this frame's Higgs is not. If H1 holds and H2
fails: a near miss, recorded as such. If H2 holds: the strongest structural result on the record, graded a READING (Λ,
H-cov with end data, the strength's definition and 3 456 discrete choices tagged, inside the calibration), to be attacked
first.

## Seen first

`VERDICT topic-sweep /coupling'?s strength|strength of (the|a) coupling|extremi[sz](es|ing|ed)? (a|the) coupling|Petersson.normali[sz]ed|Petersson norm|W51/ (full text): 8 of 1470 arcs on main match (NEGATIVE 1, PROVED 7)` —
B1684 and B1673 (the torus determinant log(y∣η∣⁴): critical only at i, a saddle, and ω, a minimum — W51 and W59's
potential, a different quantity), B1636 (the lowest symmetric coupling's golden spectrum on the tick's geodesic), B1634,
B1697. None computes this frame's Yukawa strength or tests a τ it selects. **Literature:** the Kähler-normalised Yukawa
(2 Im τ)^k ∣Y(τ)∣² of modular-flavour models (Feruglio 2017, arXiv:1706.08749), as context.

## Disclosed

- **The strength was computed before the seal** (data-free, in main's gitignored drafts; the rule written down first,
  2026-10-21 23:40): invariance under τ ↦ −1/τ, τ + 1 to 10⁻¹⁵; on Re τ = 0 and ½ no critical point, y·s₁² for ∂R
  rising to 2.3 × 10⁵ at y = 5; dS/dy > 0 on a 2 138-point grid (for a₀, ≤ 0 only at six points beside the arc, where the
  normal derivative vanishes by symmetry); on the arc one interior critical point for ∂R's top strength, θ ≈ 0.589 π
  (τ ≈ ±0.276 + 0.961 i), a saddle (a maximum along the arc, rising outward). The Frobenius strength's arc point is at
  θ ≈ 0.566 π, a₀'s at 0.615 π (not tested). The instrument recomputes all of it.
- **Known before the seal.** The six measured ratios; B1694's curve (m₂/m₃ ≈ 0.18 at Im τ = 1.5 without a line) and
  B1692's line factors (up to about four in m₂/m₃) — the priors are informed by them. No model value at the selected τ
  has been computed.
- The line grid is a grid (every line of order dividing 24, not the order-5 lines); B1698's d–e criterion (order dividing
  4 or 5 makes d and e coincide) is known.

## Instruments

`verification/the_strength.py` (no data) → `the_strength.json`; `verification/the_selected_tau.py` (no data; reads the
selected τ) → `the_selected_tau.json`; `verification/compare.py` (the comparison and the calibration) → `comparison.json`;
B1656's functions copied verbatim; hashes in `ARTIFACT_HASHES.txt`.
