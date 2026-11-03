# THE RECHECK (S291; main, 2026-11-03, night)

The owner: "approved, continue, just make sure sure sure all your claims and conclusions are right". Every claim of S289 and
S290 (B1827 § 2 and its dated note; docs/FRAMING_LEDGER.md § D; P-566) re-derived from the frame's code. Data-free.

| script | what it checks | result |
|---|---|---|
| identities_and_order5.py (V1, V2) | adj(S) = εSᵀεᵀ = det(S)·S⁻¹ = a₀ − h·Q; S̃ = εS*εᵀ = a₀* + h*·Q; det S = a₀² + h·h; coupling(−S) = −coupling(S); Y(S, M) = −Y(adj S, Mᵀ)ᵀ | 500 random (S, M): 7.4 × 10⁻¹⁵. HOLDS. So the adjugate reading IS the opposite-sign family (an overall sign changes no mixing) |
| identities_and_order5.py (V3) | all 24 order-5 lines × 3 τ × 2 radii × 4 directions × 2 readings (1 152): M_u symmetric, R₁(up) = 0, Y_u(h·Q) symmetric, the singlet's Y_u part antisymmetric, the down and lepton spectra equal; M_e = M_dᵀ | the first five HOLD (≤ 3 × 10⁻⁹); **M_e = M_dᵀ FAILS in general** (see the next row) |
| down_lepton_relation.py | M_e = λ M_dᵀ per line; the lepton singlet coefficient k for which the spectra stay equal | **M_e = λ M_dᵀ with λ a fifth root of unity on every line** (residual ≤ 2.4 × 10⁻¹⁵; λ = 1 on the 8 lines with a = 0 or b = 0); the spectra stay equal only at **k = −1** (≤ 1.6 × 10⁻¹²) |
| lepton_reads_adjugate.py | Y_e(S) = −λ Y_d(adj S)ᵀ, matrix level, 4D Higgs | 1 152 cases: 9.3 × 10⁻¹⁵. HOLDS: **the leptons read the down sector's adjugate** |
| identities_and_order5.py (V4) | why two of twelve phases had no points | at c = ±i, a₀ = c√(h·h) gives det S = 0 (a null Higgs) and m₁/m₃ ≈ 10⁻¹⁷ in every sector (B1659's J4: m₁ = 0 for null S); the hierarchy filter drops them |
| gj45_corrected.py | the 45 probe with the correct labels: the singlet's Clebsch relative to the triplet's SU(5) relation is κ = −k | κ = +1 (the 5): exactly 1 (a check). κ = −1 (the frame's own singlet, equal coefficients): medians 1.0 and 1.0. **κ = −3 (the 45): (μ/τ)/(s/b) median 2.02 [1.27, 3.28], (e/τ)/(d/b) median 3.29 [1.47, 6.04]; Georgi–Jarlskog's pattern (about 3 and 1/3) at 1.1%.** κ = +3 (S290's "45"): 2.10, 3.08, 0.5% |

**Verdicts on S289/S290's claims.**
- HOLD: the identities; every scan number quoted (they match the output files); the SM reading's failure; on order-5 lines
  Y_u symmetric, R₁(up) = 0, equal spectra; the singlet's up part antisymmetric (the 45's 10·10 form); c = 3 is the
  Georgi–Jarlskog factor (stepb_core.c_shift: × c on μ/τ, ÷ c on e/τ); B1724 and B1790 considered S, S* and S̃ only (B1659
  has the adjugate inside its law for adj Y with a general S, never as a reading).
- DISCLOSURE OWED: "at every phase" = the ten non-null phases of twelve; the SM reading's over-flip and scrambled ∣V_ud∣ are
  the reading's own (identical at c = 0: 73%, 14%, 1.2%), not the singlet's.
- CORRECTED: "Y_e = Y_dᵀ" holds on 8 of the 24 order-5 lines; in general Y_e = λY_dᵀ (λ⁵ = 1).
- RETRACTED: S290 (c), "the 45-like singlet splits the second generation by about 3": gj45_probe.py's k = −3 was κ = +3 and
  its "5-like control" was κ = −1. With the true 45 the first generation goes the wrong way. The 45 half of P-566 is dead.
- SHARPENED: "about nine of the 19 have no frame" — nine lie outside the ten; six have no frame (g₁, g₂, g₃, m_H, v, y_t);
  three are frame outputs never examined (θ̄; y_b/y_t, y_τ/y_t).

**Reading the output files.** identities_and_order5_out.txt prints three FAIL labels; each is read here:
- `MeMdT FAIL` is the finding (M_e ≠ M_dᵀ in general; M_e = λM_dᵀ, down_lepton_relation_out.txt).
- `Ye_adj FAIL` tested Y_e = −Y_d(adj S)ᵀ without the phase λ; with it the identity holds to 9.3 × 10⁻¹⁵
  (lepton_reads_adjugate_out.txt).
- `spec FAIL` is 2.8 × 10⁻⁹ against the script's 10⁻⁹ threshold: equal spectra to the channel norms' quadrature precision
  (the 4D check at k = −1 in down_lepton_relation_out.txt agrees to 1.6 × 10⁻¹²).
The first seven lines of down_lepton_relation_out.txt repeat V3's summary: the module was imported before its checks were
guarded by `__main__` (they now are; importing no longer re-runs them).

**Seen first, paid late (S294).** M_e = λM_dᵀ and the order-5 SU(5) relations are B1728's derived law (and B1698, B1703); c = 3 as Georgi–Jarlskog's factor is B1742's P-355. New here: the singlet's sign under the swap (the adjugate form) and the retraction of the 45-like split.
