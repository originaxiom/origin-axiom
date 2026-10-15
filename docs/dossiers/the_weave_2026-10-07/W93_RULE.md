# W93 — the rule, recorded before the code

The SM-derivation seat, 2026-10-15. Committed before the code that reads it exists. Nothing here is a result.

## Why this arc

- **The owner ruled P-163 first** (relay §133). Main sealed and ran it as B1658, the twisted half bound (b6542d300,
  output 04d64c2ff).
  - In B1656's twisted fibre frame under equal framed data, each sector's residue is a null quaternion M = p qᵀ.
  - For any Higgs S, the sectors' (t + 1/t), with t = m₂/m₃, then lie within a factor 4 of each other.
  - The data need 15.9 (up against leptons), so one Higgs is refuted at 3σ.
- **This seat checks it on its own code, as W89 checked B1656.** The residues come from analytic theta sums: W92's
  post hoc found mpmath's jtheta unsafe off the principal strip.
- **Not blind.** B1658's preregistration and its output were read before this rule.

## Weave or thread?

- **A fibre-frame result at one τ (τ = ω), on W59's eighteen lines: a frozen piece, as B1658 is.** It is not a weave
  result.

## The objects (fixed here, from B1658's text)

- **Units.** QI = diag(i, −i), QJ = [[0, 1], [−1, 0]], QK = QI·QJ, with ε = QJ and C = (1, QI, QJ, QK).
- **The generations' blocks** are (QJ, QI, QK).
- **The pairing** is ⟨A, B⟩ = Σ_mn A_mn B_mn. The dual basis E^s satisfies ⟨ε C_t, E^s⟩ = δ_st.
- **The weighted residue** is M = Σ_s R_s E^s.
- **The coupling** is Y_ab(S, M) = ⟨C_aᵀ ε S C_b, M⟩.
- **The residues.** R_s = c_s θ_s(ū)θ_s(δ), with c = (−i, −1, −1, i) on (1, i, j, k) ↔ θ (1, 2, 4, 3).
  - ū = (q_L + q_R)w and δ = (q_L − q_R)w, with w = p₁τ − p₂ on W59's lines (b + i/3, b + j/3), b ∈ {1/9, 2/9}.
  - The 6Y charges are the dictionary's.
  - The thetas are evaluated by analytic sums at 40 digits, at τ = ω.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **K1, the factorisation** | for 200 random null M = p qᵀ and two random complex S each: ∥adj Y∥ = 2∣det S∣∥M∥² to 10⁻¹⁰; adj Y/det S the same for both S to 10⁻¹⁰; σ₃/σ₁ ≤ 10⁻¹² | 97% |
| **K2, the Gram spectrum** | for 200 random null M, the Gram matrix of S ↦ Y(S, M) has spectrum {1, 2, 2, 4}∥M∥² to 10⁻¹²; for 20 random non-null M it misses by more than 10⁻³ | 97% |
| **K3, the null residues** | on the 18 lines and three sectors, ∣det M∣/∥M∥² ≤ 10⁻²⁵; the leptons' R₁ = 0 on every line (B1656's electron's zero) | 95% |
| **K4, the exact spectrum and the bound on the actual residues** | for 20 random S per line and sector: σ₁σ₂ = 2∣det S∣∥M∥² and σ₁² + σ₂² = ∥Y∥² to 10⁻²⁰, σ₃/σ₁ ≤ 10⁻²⁰; and for 1 000 random S per line, every two sectors' (t + 1/t) lie within a factor 4 | 95% |
| **K5, the census** | on this seat's `received/HZ2021_running_masses_MZ.json`: (t + 1/t) ratios up/down 5.08, up/leptons 15.92, down/leptons 3.13 (two decimals), with up/leptons above 4 at more than 3σ | 99% (seen) |

**The read-out (no prior).** Which pairs the bound constrains if the up sector's Higgs is not the down quarks' and the
leptons' (two Higgs fields, one for up and one for down and leptons): only down/leptons, with its ratio and z against 4.

## After the run

- Record in the weave dossier's NOTE (section W93, the table) and the state page.
- A relay to main says whether B1658 holds on a second instrument, and carries the read-out.
- CHANGELOG and PROGRESS_LOG are updated.
- A test reads the JSON and recomputes the census ratios in process.

0 of 19.
