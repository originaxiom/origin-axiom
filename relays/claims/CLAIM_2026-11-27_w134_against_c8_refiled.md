# CLAIM CARD — W134 and C8 share object, unit and count; they part only on E₈'s determinant (= K2), so C8 is scoped

- card id: new
- seat code: fam1-v1-unset-04
- seat, branch, commit: fam1-v1-unset-04, sm/cards, 3372dd041787d8e874121937af041a1747bb9afa
- kind: computation
- touches: P-610, P-302, P-288
- effect: conditions — P-288 (C8; GENESIS FK10 [v1.59]): the reduction holds outside E₈'s family slot; inside it
  the whole unit is excluded and the least three-27 datum is 17/24 (W134); P-302: K2 re-derived on its own route
- scope: frame: the weave's surface (the τ-line, Mp2(ℤ)), the triplet placed in the family slot of
  E₈ ⊃ (E₆ × SU(3))/ℤ₃; object: the weight-3/2 forms of ρ ⊗ χ_η^(r+m) and the index of 27 ⊗ V under uniform
  dressings η^m, |m| ≤ 24; reach: class; hypotheses: uniform end data only (no per-line fractional data); no flat U(1)
  lines inside E₆; the four puncture conditions 0, V2, V4, L6 of W46 (V2, V4, L6 via B1641's float pieces); K2's
  anomaly read as B1674 defines it, n_G = w_G · c mod 24
- identifications: W134's dressing m = 24n is C8's O(nδ) (the unit's multiplier χ_η²⁴ is trivial); W134's ρ is C8's
  ρ_T (main's theta multiplier, B1730; equivalent to main's lift, B1641)
- definitions: ρ(S) = ζ₈P, ρ(T) = ζ₈L⁻¹ with P the swap of the first two coordinates and
  L⁻¹ = [[1,0,0],[0,0,1],[0,−1,0]]; χ_η^a(S) = e^(−πia/4), χ_η^a(T) = e^(2πia/24); ε_r = χ_η^r, with the allowed r
  those (0, 4, …, 20) for which weight 3/2 is allowed; χ_k(ρ) = d + dk/12 − α(e^(πik/2)ρ(S))
  − α((e^(πik/3)ρ(S)ρ(T))⁻¹) − α(ρ(T)), α the sum of eigenvalue turns in [0, 1) (B1632); W134's index
  I(r, cond, m) = −χ_(3/2+m/2)(ρ ⊗ ε_r ⊗ χ_η^m) + Σ_(p ∈ cond) χ_(1+m/2)(p ⊗ ε_r ⊗ χ_η^m); admissible (E₈'s
  determinant condition) iff det(ρ ⊗ χ_η^(r+m)) = χ_η^c with c ≡ 0 mod 24; C8's count is the dimension of
  weight-3/2 forms of ρ with n uniform units, which equals χ_(3/2+12n)(ρ); K2: n_G = w_G · c mod 24 with w = (Dynkin
  index under SU(3), under SU(2), dimension) of the 27 or the 16, the index computed from E₈'s roots
- imports: E₈ ⊃ (E₆ × SU(3))/ℤ₃ as the family frame (W134's placement of the triplet; B1736's frame on main); B1674's
  reading of the moves' anomaly as n_G = w_G · c
- premises on main: B1632 (χ), B1641 (W46's lifts and pieces), B1730 (the theta multiplier; the exact q-series
  space), B1736 (ρ′ = ρ ⊗ χ_η^k, k ∈ {5, 13, 21}), B1796 and B1797 (C8); register rows P-288, P-302, P-610
- decisive script: relays/claims/sm_refile/r610_decisive.py, SHA-256 ccf3e326fcafba74, depends on the standard library,
  numpy, sympy and mpmath, run as python3 relays/claims/sm_refile/r610_decisive.py, output SHA-256 981a2bdcccaaec60
- decisive lines: 21 lines marked "DECISIVE:", SHA-256 f085b1ca158511bd
- failing control: python3 relays/claims/sm_refile/r610_control.py
- second computation: none
- already on main?: grep -il -E "W134|17/24 of the cusp" frontier/*/FINDINGS.md on main at 9c8b0a531: B1736 only,
  whose FINDINGS say K2 was not re-derived; B1796, B1797 and GENESIS v1.59 never cite W134; the closest arc is B1796
- what would make it fail: a whole unit (m = 24n) admissible for some allowed twist; three chiral 27s at some
  admissible |m| < 17; C8's 3n failing at O(δ) or O(2δ); W134's m = 24n differing from C8's O(nδ); or the full 27's
  anomaly vanishing at a datum whose family part is not det-1
