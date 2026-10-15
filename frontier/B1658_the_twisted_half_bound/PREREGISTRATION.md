# B1658 — THE TWISTED HALF BOUND: one Higgs cannot spread the sectors by more than a factor 4 (B1656's twisted frame, equal framed data): preregistration

cc (main), 2026-10-15. POINT_REGISTER P-163 (the Higgs's defect), sharpened by the SM seat's W90 (verified on main): one
Higgs defect shared by every sector fits no assignment under B1657's UNTWISTED laws. This arc asks the same in B1656's
twisted, quaternionic frame, where each sector's matter residue is a different null quaternion. The weave's fibre at
τ = ω on W59's lines, given Λ, the dictionary and B1654's premises with B1656's four channels: a frozen piece. The census
in T4 reads data that were seen (HZ2021 at M_Z): **a scoreboard, not a blind test.** Under equal framed data the first
generation is massless in every sector (B1653), which the data already refute (the SM seat's W88, Q1); this arc's census
adds the second generation. The Higgs is the complexified quaternion of B1656 (S ∈ M₂(ℂ)); no reality or Hermiticity
condition is imposed on it. 0 of 19.

## 0. Seen first

`VERDICT topic-sweep /twisted half bound|one higgs|quaternion.{0,20}(null|norm)|adj.{0,10}Y|half bound/: 16 of 1429 arcs on main match (NEGATIVE 3, OPEN 2, PROVED 11)`.
Of the matches, the precedents are B1645 (the half bound) and B1653 (the rank of a point coupling); the others match
"one Higgs", "half bound" or "adj" in other senses (B812, B918, B969, B987 on the Higgs's role; harvests and seams), all
read at their verdict lines; none bounds a twisted coupling. The precedents: B1645 (the half bound, untwisted: s₁s₂ = ∣R∣²∣a∣², rank one on the cone),
B1656 (the twisted channels; its coupling Y_ab(S, M) and the null residue quaternion), B1657 (the two laws, untwisted),
the SM seat's W90 (one shared Higgs defect refuted under the untwisted laws; verified on main), its relay §124 (the
Higgs's factor θ_s(ū)² is the same in every sector of B1656's frame), the web seat's two-weaves reading (a two-point
term between threads as a sector-dependent mechanism). **Literature:** SU(2) invariants of C²; adjugates of bilinear
maps.

## 0b. Disclosed

- **Everything the cells read was seen** in main's exploration (`audit/drafts/p163/`: quat_probe.py, k_closed_form.py,
  quat_tensor.py, quat_symbolic.py, range_fit.py, verify_w90.py; NOTES.md), and the draft instrument was run once from
  the drafts folder with every cell holding and the census as below. **No cell is blind.**
- **A read-only reviewing agent read v1 before the seal** (`review/`): no blocker for validity; it found that the range
  [1, 4] holds for EVERY complex Higgs S, not only rank-one ones (so the census is exact and "a Higgs far from null"
  is closed: now T2b, by the Gram spectrum {1, 2, 2, 4}); that A is q̃ p̃ᵀ, not p̃ q̃ᵀ (now asserted in T1); that T5
  could not fail meaningfully (now a synthetic one-Higgs world the census must not refute); and asked for "complexified",
  "against M_Z ratios", the one-sided pair order, and the first generation's known miss up front. v1 is kept beside the
  seal (`design_v1/`).
- **A second reading agent read v2** (`review2/`): no blocker; it confirmed T2b by the Rayleigh quotient and the exact
  census to 6 × 10⁻¹⁵; it found the census one-sided (a ratio below ¼ would pass unseen — now two-sided, max(r, 1/r)),
  T5(b) an identity rather than a test (now labelled so, with a control outside the bound that must refute and one at
  3.9 that must not), nullness asserted rather than checked on 17 lines (now checked in T3), the scale sentence too
  strong (softened), and the degenerate limit and the look-elsewhere factor to state (below).
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
- **The factorisation.** For null M and any S, adj Y(S, M) = det S · A(M) with A = q̃ p̃ᵀ, where p̃ = (p·p, 2ip₀p₁,
  −i(p₀² − p₁²)) and q̃ the same in q; ∣∣p̃∣∣² = 2∣p∣⁴, so ∣∣A∣∣ = 2∣p∣²∣q∣² = 2∣∣M∣∣².
- **The spectrum.** det Y = (det M)·l_S(M) = 0 (B1656), so rank Y ≤ 2; σ₁σ₂ = ∣∣adj Y∣∣ = 2∣det S∣∣∣M∣∣² and
  σ₁² + σ₂² = ∣∣Y∣∣². So every sector's spectrum is exactly (1, m₂/m₃, 0) with m₂/m₃ + m₃/m₂ = ∣∣Y∣∣²/(2∣det S∣∣∣M∣∣²).
- **The norm law.** For S = u vᵀ, M = p qᵀ: ∣∣Y∣∣² = (∣u∣²∣p∣² + ∣u†p∣²)(2∣v∣²∣q∣² − ∣vᵀq∣²), in [1, 4]·∣∣S∣∣²∣∣M∣∣².
- **For every S** (not only rank one): S ↦ Y(S, M) is linear, and for null M its Gram matrix has the spectrum
  {1, 2, 2, 4}·∣∣M∣∣², so ∣∣Y(S, M)∣∣² ∈ [1, 4]·∣∣S∣∣²∣∣M∣∣² for all S.
- **The exact census quantity.** t + 1/t = ∣∣Y(S, M_s)∣∣²/(2∣det S∣∣∣M_s∣∣²) with t = m₂/m₃ (exact, from σ₁σ₂ and
  σ₁² + σ₂²). One Higgs shares det S and ∣∣S∣∣, so **(t + 1/t)_a/(t + 1/t)_b ∈ [¼, 4] for any two sectors and any S** —
  no first-order expansion, and a Higgs far from null is included.
- **The twisted half bound.** For a nearly null Higgs (∣d_S∣ = ∣det S∣/∣∣S∣∣² ≪ 1), m₂/m₃ = k_s∣d_S∣ + O(d_S²) with
  k_s = 2/((1 + x_s)(2 − y_s)) ∈ [½, 2], x_s = ∣û†p̂_s∣², y_s = ∣v̂ᵀq̂_s∣². **One Higgs gives every sector the same
  ∣d_S∣, so the sectors' second generations lie within a factor 4 of each other.**

## 2. The cells (the instrument `verification/the_twisted_half_bound.py`; one run; JSON after every cell)

| cell | prediction | seen | identity or test |
|---|---|---|---|
| **T0**, plumbing (void) | B1656's definitions loaded unchanged reproduce its stored R₁/∣R∣ on (1/9, 1/9) in every sector < 10⁻⁹; the residues null < 10⁻¹³ | held | gate |
| **T1**, the factorisation | symbolically adj Y(S, pqᵀ)/det S free of S; the row-form identity ∣∣(p·p, 2ip₀p₁, −i(p₀² − p₁²))∣∣² = 2∣p∣⁴; numerically ∣∣A∣∣/(∣det S∣∣∣M∣∣²) = 2 to 10⁻¹⁰ at 20 draws | held | identity |
| **T2b**, every Higgs | for null M, the 4 × 4 Gram matrix of S ↦ Y(S, M) has the spectrum {1, 2, 2, 4}·∣∣M∣∣² at 200 random null M (< 10⁻¹²); a check that nullness is used: at 20 non-null M it departs (> 10⁻³) | held | identity; the non-null case a check |
| **T2**, the norm law | symbolically ∣∣Y∣∣² − (∣u∣²∣p∣² + ∣u†p∣²)(2∣v∣²∣q∣² − ∣vᵀq∣²) = 0; numerically < 10⁻¹² at 400 unit draws; the range [1, 4] attained (u ⟂ p with vᵀq = 1 gives 1; u = p with vᵀq = 0 gives 4) | held | identity; the attainment a check |
| **T3**, the exact spectrum on W59's lines | 18 lines × 3 sectors × 3 random S: every residue null (∣det M∣/∣∣M∣∣² < 10⁻¹³); m₁/m₃ < 10⁻¹²; σ₁σ₂ = 2∣det S∣∣∣M∣∣² and σ₁² + σ₂² = ∣∣Y∣∣² to 10⁻¹⁰; for a nearly null Higgs (ε = 10⁻⁵) m₂/m₃ = k_s∣d_S∣ within 10⁻³ (relative); every k_s in [½, 2] | held | the spectrum identities; the k law a test of first order |
| **T4**, the census (a scoreboard) | the exact quantity t + 1/t from the data's M_Z ratios m₂/m₃, for the pairs up/down, up/leptons, down/leptons, two-sided (max(r, 1/r)) against the bound 4: refuted if any pair sits more than 3σ above 4 (three pairs: a look-elsewhere factor 3 on the threshold, immaterial at 27σ) | held: up/down 5.08 (2.3σ above, not by itself a refutation), up/leptons 15.92 (27σ above — the refutation), down/leptons 3.13 (within) | scoreboard |
| **T5**, controls | (a) three sector-specific Higgs fields fit the three m₂/m₃ to 10⁻⁶ (the frame reaches them), and the census, given those values with 1% errors, refutes them as one Higgs; (b) a synthetic world with ONE random Higgs, 1% errors: not refuted, every two-sided ratio ≤ 4 (an implementation check — by the theorem it cannot be refuted); (c) the same world with one sector's t + 1/t multiplied by 6: the census must refute; (d) multiplied to bring the largest ratio to 3.9: it must not | held | (a), (c), (d) tests of the census; (b) an identity |

PROVED if T0 is not void and T1, T2, T2b, T3, T5 hold (T5's controls (c) and (d) show the census can both refute and pass); T4 is recorded as found, and its refutation (if it holds as seen) is
a refutation of "one Higgs, under equal framed data, in B1656's frame, against the M_Z ratios" — a scoreboard entry like W88's and
W90's, not a closed door (E89).

## 3. What it would mean

- **The twisted half bound** is B1645's half bound carried into the twisted frame: one Higgs gives the three sectors'
  second generations coefficients within a factor 4, whatever the Higgs's direction, τ or line, under equal framed
  data — exactly in t + 1/t, for every complex Higgs (in t itself, for a nearly null Higgs, to first order: the k_s law).
  The sectors' twists move the coefficient, but only within [½, 2]. The census applies to the second generation
  against the third; the first generation is massless under P4′, a known miss.
- **With W90:** one Higgs defect cannot spread the sectors under the untwisted laws (W90) nor in the twisted frame under
  equal framed data (this arc). The remaining escapes are named: the canonical end condition's joint law (the matter's
  own defect D_s/(2πL) as a second light mass, its law owed) and a
  sector-dependent Higgs (the web seat's two-point term between threads; the owner's ruling on such terms is pending,
  P-166).

## 4. What it does not show

The joint law under P4 (both defects small); the first generation (zero under P4′ by B1653, a known miss); other lines
or τ, beyond T1–T2b, which hold for any null M; the interacting weave; any value. The model fibre has no scale: the
census compares with M_Z running ratios. That a factor 16 against 4 survives running to other scales is assumed, not
computed here.

## 5. Files

`verification/the_twisted_half_bound.py` (sealed), its JSON and run text; the exploration scripts beside the seal at
banking.
