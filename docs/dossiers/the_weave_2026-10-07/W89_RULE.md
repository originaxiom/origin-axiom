# W89 — the rule, recorded before the code

The SM-derivation seat, 2026-10-15. Committed before the code that reads it exists. What the seat read and explored
while drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **Main sealed B1656, "the electron's zero"** (27e7e7482): the per-sector twisted channels at τ = ω on W59's eighteen
  Higgs lines. Its central claims are three:
  - the four channel norms satisfy c_i = c_j = c_k on every line and in every sector;
  - so D_sector = (c₁ − c_⊥)R₁²;
  - the leptons' R₁ vanishes because 9w lies in the lattice, so the electron stays massless while the quarks are
    lifted.
- **Relay §116 said this seat would check main's twisted channels after main's seal.** Doing it now, before main's run
  lands, keeps the check independent of main's output, as W85 did for B1651.
- **The check is on this seat's own code.** It uses W87's polar quadrature with twisted kernels, and W85's 60-digit
  theta series for the residues. None of main's instrument is used.

## Weave or thread?

- **Weave-type, as B1656:** the fibre every thread shares at τ = ω, W59's lines, and the three sectors jointly. It is
  given Λ, the dictionary's hypercharges (6Y), B1654's premises with four channels, and B1653's twisted pairing.

## Seen before the rule (disclosed)

- **B1656's preregistration, read in full** (27e7e7482). It includes main's disclosed exploration:
  - c₁ = −3.575627 and c_⊥ = 2.231269 in the quark sectors;
  - lepton D ≤ 5.1 × 10⁻¹³;
  - quark |D|/|R|² ∈ {1.0312, 2.4629, 2.7416};
  - the non-fixed lines' lepton lift 2.92;
  - the fictitious pairs' values.
- **This seat's exploration, firewalled** (scratch, double precision, W87's polar quadrature). On the lines (1/9, 1/9),
  (4/9, 4/9) and (2/9, 2/9) it reproduced c₁ = −3.575627 and c_i = c_j = c_k = 2.231269 in every sector, lepton
  |R₁|/|R| ≈ 10⁻¹⁵, and the three quark values, cycling between up and down. One lepton case overflowed: the numpy
  theta series was evaluated at δ = −9w far outside the fundamental domain. The residues are therefore taken from W85's
  60-digit series here.
- **The seat's own record:** W87 (the untwisted closed form and the method), the reading of relay §115 (which lines
  split the sectors), the CP reading (relay §118), W59 (the lines) and W85 (the series).
- An attempt to extend W87's closed form to twisted kernels failed in scratch. A Kronecker-type guess misses by O(1),
  and for a general twist the Parseval sums are Lerch transcendents. No closed form is used or claimed here.

## The method (fixed here)

- **The lines.** W59's eighteen, (ψ₁, ψ₂) = (b + i/3, b + j/3) with b ∈ {1/9, 2/9} and i, j ∈ {0, 1, 2}, and
  w = ψ₁τ − ψ₂ at τ = ω = e^{2πi/3}.
- **The sectors** (q_L, q_R) are up (1, −4), down (1, 2) and leptons (−3, 6), with ū = (q_L + q_R)w and
  δ = (q_L − q_R)w.
- **The channels** are the units (1, i, j, k) ↔ thetas (1, 2, 4, 3), with c = (−i, −1, −1, i) (B1653).
- **The kernels:** K_s(z) = e^{2πiAz}θ_s(z + ū)θ₁′(0)/(θ_s(ū)θ₁(z)), with A = Im ū / Im τ, so the multipliers are
  unitary.
  - The norm is c_s = ∫ dθ [ln r_max + ∫₀^{r_max} (r|K_s|² − 1/r) dr] over B1654's P. Angles are split at P's corners,
    with 100 Gauss–Legendre nodes per piece and 60 radial nodes. The thetas are numpy series, 40 terms.
- **The residues:** R_s = c_s θ_s(ū)θ_s(δ)/θ₁′(0) from W85's series at 60 digits, any common factor dropped. The
  ratios |R₁|/|R|, D/|R|² and (Σ R_s²)/|R|² do not depend on it.
- **The arithmetic is exact,** in rationals. Coordinates are taken in the basis (ω, 1), and multiplication by ω maps
  (a, b) ↦ (b − a, −a).
- **The controls:**
  - the generic τ₀ = 0.13 + 1.07i on MIX3 = (1/9, 1/9), (4/9, 4/9), (2/9, 2/9);
  - the three non-fixed 9-torsion lines (1/9, 2/9), (1/9, 0) and (2/9, 1/9) at ω.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **V1, the arithmetic** (B1656's E0, exact) | on all 18 lines, 9w lies in the lattice, 3w does not, and 3w is fixed by z ↦ ωz modulo the lattice; on the three non-fixed lines, 9w lies in the lattice and 3w is not fixed | 99% |
| **V2, the equal norms** (B1656's E3) | at ω, on all 18 lines and in every sector, c_i = c_j = c_k to 10⁻⁹; the gap c₁ − c_⊥ is the same on every line and in every sector to 10⁻⁸, and \|gap\| > 1 | 97% |
| **V3, the electron's zero** (B1656's E4) | on all 18 lines, the leptons have \|R₁\|/\|R\| < 10⁻¹² and \|D\|/\|R\|² < 10⁻¹⁰; the quarks have \|R₁\|/\|R\| > 0.1 and \|D\|/\|R\|² > 0.5; the null quaternion \|Σ R_s²\|/\|R\|² < 10⁻⁴⁰ everywhere | 97% |
| **V4, the three values** | the quark \|D\|/\|R\|² take exactly three values over the 36 quark cases (to 10⁻⁸), which round to 1.0312, 2.4629 and 2.7416 | 95% |
| **V5, the controls** (B1656's E5(a, b)) | at τ₀ on MIX3, the leptons' \|D\|/\|R\|² > 0.1; on the three non-fixed lines at ω, the leptons' \|R₁\|/\|R\| < 10⁻¹² yet the c_⊥ spread exceeds 10⁻³ and \|D\|/\|R\|² > 0.1 | 93% |

**The read-outs (no prior).** c₁, c_⊥ and the gap; each sector's |R₁|/|R| and |D|/|R|² per line; the controls'
values.

## What a failure would say

- **V2** fails if the rotation argument fails on this seat's kernels.
- **V3** fails if the residue formula or the arithmetic does.
- **V4** fails if the classes are not three.
- **V5** fails if the controls do not bite on this seat's code.

A failure is recorded as failed, with its cause found post hoc and labelled.

## After the run

- Record in the weave dossier's NOTE (section W89, the table), the state page, relay §120 to main, CHANGELOG and
  PROGRESS_LOG.
- A test in `tests/test_b1552_the_chiral_triplets_count.py` reads the JSON and recomputes V1 exactly in process.

0 of 19.
