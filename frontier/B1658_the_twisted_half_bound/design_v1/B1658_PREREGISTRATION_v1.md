# B1658 — THE TWISTED HALF BOUND: one Higgs cannot spread the sectors (B1656's twisted frame, equal framed data): preregistration

cc (main), 2026-10-15. POINT_REGISTER P-163 (the Higgs's defect), sharpened by the SM seat's W90 (verified on main): one
Higgs defect shared by every sector fits no assignment under B1657's UNTWISTED laws. This arc asks the same in B1656's
twisted, quaternionic frame, where each sector's matter residue is a different null quaternion. The weave's fibre at
τ = ω on W59's lines, given Λ, the dictionary and B1654's premises with B1656's four channels: a frozen piece. The census
in T4 reads data that were seen (HZ2021 at M_Z): **a scoreboard, not a blind test.** 0 of 19.

## 0. Seen first

`VERDICT topic-sweep /twisted half bound|one higgs|quaternion.{0,20}(null|norm)|adj.{0,10}Y|half bound/` — to be run
at the seal and recorded here. The precedents: B1645 (the half bound, untwisted: s₁s₂ = ∣R∣²∣a∣², rank one on the cone),
B1656 (the twisted channels; its coupling Y_ab(S, M) and the null residue quaternion), B1657 (the two laws, untwisted),
the SM seat's W90 (one shared Higgs defect refuted under the untwisted laws; verified on main), its relay §124 (the
Higgs's factor θ_s(ū)² is the same in every sector of B1656's frame), the web seat's two-weaves reading (a two-point
term between threads as a sector-dependent mechanism). **Literature:** SU(2) invariants of C²; adjugates of bilinear
maps.

## 0b. Disclosed

- **Everything the cells read was seen** in main's exploration (`audit/drafts/p163/`: quat_probe.py, k_closed_form.py,
  quat_tensor.py, quat_symbolic.py, range_fit.py, verify_w90.py; NOTES.md), and the draft instrument was run once from
  the drafts folder with every cell holding and the census as below. **No cell is blind.**
- **What the exploration found, in order:** a shared null Higgs gives sector-dependent O(1) coefficients (random S₀);
  the factorisation adj Y = det S·A(M) for null M (numerically, then symbolically); ∣∣A∣∣ = 2∣∣M∣∣²; the range of
  ∣∣Y∣∣² by optimisation [1, 4]; its closed form (1 + ∣u†p∣²)(2 − ∣vᵀq∣²) by a least-squares fit, then symbolically. The
  test first planned for P-163 — the symmetric null Higgs at ω against the data's cross-sector ratios — was NOT run: the
  bound makes it moot, since no Higgs can spread the sectors by more than 4.
- **The data** (HZ2021 at M_Z, B1637's received file, the same bytes as the SM seat's): m₂/m₃ = 0.003685 (up), 0.01872
  (down), 0.05887 (leptons) — known to everyone; the census's outcome was computed in the draft run.

## 1. The setting, and what follows by hand

- **The coupling** is B1656's, Y_ab(S, M) = Σ (C_aᵀ ε S C_b) ∘ M, bilinear in the Higgs quaternion S ∈ span{1, i, j, k}
  and the matter's weighted residue M. det S = s₀² + s·s. Under equal framed data (P4′) M is the residue quaternion,
  null in every sector (B1653's null quaternion), so M = p qᵀ.
- **The factorisation.** For null M and any S, adj Y(S, M) = det S · A(M), with A's rows (p·p, 2ip₀p₁, −i(p₀² − p₁²))
  times q's same quadratic forms, so ∣∣A∣∣ = 2∣p∣²∣q∣² = 2∣∣M∣∣².
- **The spectrum.** det Y = (det M)·l_S(M) = 0 (B1656), so rank Y ≤ 2; σ₁σ₂ = ∣∣adj Y∣∣ = 2∣det S∣∣∣M∣∣² and
  σ₁² + σ₂² = ∣∣Y∣∣². So every sector's spectrum is exactly (1, m₂/m₃, 0) with m₂/m₃ + m₃/m₂ = ∣∣Y∣∣²/(2∣det S∣∣∣M∣∣²).
- **The norm law.** For S = u vᵀ, M = p qᵀ: ∣∣Y∣∣² = (∣u∣²∣p∣² + ∣u†p∣²)(2∣v∣²∣q∣² − ∣vᵀq∣²), in [1, 4]·∣∣S∣∣²∣∣M∣∣².
- **The twisted half bound.** For a nearly null Higgs (∣d_S∣ = ∣det S∣/∣∣S∣∣² ≪ 1), m₂/m₃ = k_s∣d_S∣ + O(d_S²) with
  k_s = 2/((1 + x_s)(2 − y_s)) ∈ [½, 2], x_s = ∣û†p̂_s∣², y_s = ∣v̂ᵀq̂_s∣². **One Higgs gives every sector the same
  ∣d_S∣, so the sectors' second generations lie within a factor 4 of each other.**

## 2. The cells (the instrument `verification/the_twisted_half_bound.py`; one run; JSON after every cell)

| cell | prediction | seen | identity or test |
|---|---|---|---|
| **T0**, plumbing (void) | B1656's definitions loaded unchanged reproduce its stored R₁/∣R∣ on (1/9, 1/9) in every sector < 10⁻⁹; the residues null < 10⁻¹³ | held | gate |
| **T1**, the factorisation | symbolically adj Y(S, pqᵀ)/det S free of S; the row-form identity ∣∣(p·p, 2ip₀p₁, −i(p₀² − p₁²))∣∣² = 2∣p∣⁴; numerically ∣∣A∣∣/(∣det S∣∣∣M∣∣²) = 2 to 10⁻¹⁰ at 20 draws | held | identity |
| **T2**, the norm law | symbolically ∣∣Y∣∣² − (∣u∣²∣p∣² + ∣u†p∣²)(2∣v∣²∣q∣² − ∣vᵀq∣²) = 0; numerically < 10⁻¹² at 400 unit draws; the range [1, 4] attained (u ⟂ p with vᵀq = 1 gives 1; u = p with vᵀq = 0 gives 4) | held | identity; the attainment a check |
| **T3**, the exact spectrum on W59's lines | 18 lines × 3 sectors × 3 random S: m₁/m₃ < 10⁻¹²; σ₁σ₂ = 2∣det S∣∣∣M∣∣² and σ₁² + σ₂² = ∣∣Y∣∣² to 10⁻¹⁰; for a nearly null Higgs (ε = 10⁻⁵) m₂/m₃ = k_s∣d_S∣ within 10⁻³ (relative); every k_s in [½, 2] | held | the spectrum identities; the k law a test of first order |
| **T4**, the census (a scoreboard) | the data's ratios of m₂/m₃ between sectors against the bound 4: refuted if any pair sits more than 3σ above 4 | held: down/up 5.08 (2.3σ above 4), leptons/up 15.98 (27σ above), leptons/down 3.14 (within) | scoreboard |
| **T5**, control | three sector-specific Higgs fields (each near null, along that sector's p) fit the three m₂/m₃ to 10⁻⁶: the census can pass when the Higgs is not one | held | test |

PROVED if T0 is not void and T1, T2, T3, T5 hold; T4 is recorded as found, and its refutation (if it holds as seen) is
a refutation of "one nearly null Higgs, under equal framed data, in B1656's frame" — a scoreboard entry like W88's and
W90's, not a closed door (E89).

## 3. What it would mean

- **The twisted half bound** is B1645's half bound carried into the twisted frame: one Higgs gives the three sectors'
  second generations coefficients within a factor 4, whatever the Higgs's direction, τ or line, under equal framed
  data. The sectors' twists move the coefficient, but only within [½, 2].
- **With W90:** one Higgs defect cannot spread the sectors under the untwisted laws (W90) nor in the twisted frame under
  equal framed data (this arc). The remaining escapes are named: the canonical end condition's joint law (the matter's
  own defect D_s/(2πL) as a second light mass, its law owed), a Higgs far from null (beyond first order), and a
  sector-dependent Higgs (the web seat's two-point term between threads; the owner's ruling on such terms is pending,
  P-166).

## 4. What it does not show

The joint law under P4 (both defects small); anything at a Higgs far from null; the first generation (zero under P4′
by B1653, a known miss); other lines or τ; the interacting weave; any value.

## 5. Files

`verification/the_twisted_half_bound.py` (sealed), its JSON and run text; the exploration scripts beside the seal at
banking.
