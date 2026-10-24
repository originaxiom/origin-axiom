# B1742 — TWO_HIGGS VERIFIED ON MAIN (P-351): THE WEB SEAT'S SEALED H5 REPRODUCES ON MAIN'S OWN INSTRUMENT — H_u = F₆, H_d = F₂₂, BOTH READ S, c = 3: χ²_six 1.188, ALL SIX WITHIN 10% — AND THE REASON ITS D IS 9: ON THE α = 2/5 LINES THE LEPTON SPECTRUM IS THE DOWN SPECTRUM, SO THE SIX ARE FOUR NUMBERS

**Verdict: PROVED (a verification on main of a seat's sealed result, and a mechanism).** cc (main), 2026-10-23, after
B1740's outputs were committed (B1740's preregistration pledged that main would not read the web seat's F₋₂-bearing
results before then; TWO_HIGGS's menu contains F₋₂). A READING: the pair is chosen by the data, c = 3 by hand, τ
fitted, and the mixing fails. **0 of 19.**

## 1. What was checked

The web seat's TWO_HIGGS (`relays/chat1_2026-10-23_two_higgs/` on its branch; rule 0b192e458, result 8040bebd2): H_u for
the up quarks and H_d for the down quarks and leptons, each a zero-free direction F_a = (εθ₂^a, εθ₄^a, iθ₃^a) (B1730; ε =
1 for a ∈ {6, −2, 22}), all read S, c = 3, on its 1 280 points (the ten (2/5, k/10) lines, Re τ 0.0625–0.9375, Im τ
2.0–3.5, both horocycles).

**Main's instrument:** B1740's sealed `census.py`, imported and not modified; `verification/repro.py` adds a per-sector
Higgs outside it (the sectors' twists, residues, channel weights and coupling are B1740's own). **Control:** with F₋₂ in
every sector it reproduces B1740's stored census row at (1/2, 1/3), 0.55 + 2.25i, to 0.0 in ln, on both horocycles and
three reading triples.

## 2. The result

| item | the seat | main |
|---|---|---|
| best six-row (F₆ ∣ F₂₂, 0.5625 + 2.6i, (2/5, 1/10), L₂): model over measured | 1.010, 0.910, 0.983, 0.938, 0.938, 1.052 | 1.0099, 0.9103, 0.9831, 0.9377, 0.9381, 1.0519 |
| χ²_six (σ² = rel² + 0.10², B1720's) | 1.19 | 1.1884 |
| ∣V_us∣, ∣V_cb∣, ∣V_ub∣ over measured; J; D | 0.19, 0.55, 0.39; about −10⁻⁶; 9.000 | 0.187, 0.554, 0.392; −1.08 × 10⁻⁶ (sign by orientation); 9.0000 |
| with c = 1 at that row | worst six 3.20 | 3.198 |
| F₆ ∣ F₆ there: m_d/m_b, m_e/m_τ over measured | 0.33, 0.37 | 0.328, 0.368 |
| the full grid (15 360 off-diagonal rows): min χ²_six; min χ²_nine | 1.19; 154.1 | 1.1884; 154.14 |
| rows below 16.75 | 14, all F₆ ∣ F₂₂, Im τ 2.6, L₂, lines 1/10, 1/2, 4/5, 1.19–12.4 | the same 14, 1.188–12.373 |
| per pair, min worst six | F₆ ∣ F₂₂ 1.099; F₂₂ ∣ F₆ 3.07; with F₋₂ 25–167 | 1.099; 3.072; 24.98–166.7 |
| rows with the six within 2.0 and the nine within 2.5 | 0 | 0 |
| max ∣ln(D/9)∣ with H_d = F₂₂ | 5.5 × 10⁻⁷ | 7.3 × 10⁻⁸ |

Two wording differences, neither touching a cell: the seat's 3.07 for F₂₂ ∣ F₆ is that pair's grid minimum (3.51 at the
best six-row); its 5.5 × 10⁻⁷ is from float32 storage (main computes in float64). Sensitivity at the best row: ±0.02 in
Re τ or Im τ gives χ²_six 1.04–3.43 (the seat's ±0.05: 1.04–10.3).

## 3. Why D = 9: the lepton–down identity of the α = 2/5 lines (`verification/scan.py`, part B)

- With c = 3, D = 9 · (the leptons' m₂/m₁)/(the down quarks' m₂/m₁), so D = 9 exactly when the two spectra coincide.
- On w = (2/5)τ + k/10 the lepton twists (−3w, 6w) equal, modulo the lattice, (2w − k/2, w + k/2): the down twists
  (w, 2w) swapped and shifted by half-periods. For k even the shifts are whole periods and the spectra coincide for
  every Higgs (random directions: 10⁻¹⁴). For k odd they coincide only for a Higgs with no QI component; the departure
  is linear in that component (10⁻⁸ → 2 × 10⁻⁸, 10⁻⁴ → 10⁻⁴, 10⁻² → 10⁻²). F₂₂'s QI component is θ₂²²/θ₃²² ≈ 10⁻¹³ at
  Im τ 2.6, so D = 9 to rounding; F₆'s is about 3 × 10⁻⁴; F₋₂ is led by it.
- Off α = 2/5 (1/7, 3/7) there is no such relation (ln(D/9) about 3); the line (0, 1/2) shows it for every Higgs tried.
- **Consequence:** on these lines, with c = 3, the lepton ratios are the down ratios times 3 and divided by 3
  (Georgi–Jarlskog's relations) by construction of the line family, and D = 9, which P-094 (10.58 ± 0.11) excludes at
  14σ. The six are four independent quark ratios fitted with τ and discrete choices — as the seat's own Q1–Q4 say. The
  web seat's lepton_channels (row 1346) found the same identity independently. P-355.

> *Corrected 2026-10-24 (Review 69, an E54 instance). The order-5 case above (k even: the lepton spectrum is the down
> spectrum for every Higgs) is not new: it is B1728's law at N = 5 (d = e, with Y_e = Y_dᵀ; derived) and B1698's
> observation, and §3 re-derived it without citing them. What §3 adds is the order-10 case (k odd), where the identity
> holds only for a Higgs with no QI component, departing linearly in that component — beyond B1728's Higgs-independent
> law (the web seat's lepton_channels has it as observed, not derived).*

## 4. The jtheta caution (W144, P-354)

The SM seat's W144 found that mpmath's jtheta takes the principal nome root, wrong off −1 < Re τ ≤ 1. Main's
instruments are immune: `b1656_funcs.th_mp` builds θ₂ and θ₁ from an explicit q^{1/4} = e^{iπτ/4} and calls jtheta
only for θ₃ and θ₄ (power series in q with integer exponents); B1740's census and this arc sum θ₂ directly; B1741's
T-covariance control at Re τ 3.4 held to 3.3 × 10⁻¹⁰.

## 5. What it means

- **Verified on main:** the seat's sealed H5 stands as it states it — the first sealed χ²_six cell on record to hold
  with one reading (S) in every sector. Main's verification is the third opinion's first leg (P-351).
- **A READING, not a derivation:** the pair is chosen by the data out of six (no principle assigns a = 6 to H_u and a = 22
  to H_d); c = 3 by hand; τ fitted on a grid; on these lines the six are four numbers; D = 9 is excluded by P-094; the
  nine fail (154) with the mixing aligned but too small (∣V_us∣ 0.19 of measured).
- **With B1739 and B1740, three regimes of the Higgs:** nearly null with the conjugate in one sector — hierarchy,
  misaligned light states; non-null — aligned, no hierarchy; two nearly null directions read S — hierarchy, aligned,
  mixing too small.

## Seen first

`VERDICT topic-sweep /two.higgs|H_u|H_d|two doublets|F_22|F₂₂|lepton.down identity|D = 9/ (full text): 34 of 1514 arcs on main match (NEGATIVE 3, OPEN 6, PROVED 24, no verdict file 1)`.
Bearing on it: B1730 (the family), B1731, B1732, B1736 (the closed form), B1739, B1740, B1726, B1735, P-094.
**Literature:** Georgi and Jarlskog (1979); two-Higgs-doublet models (standard).

## Disclosed

- The reproduction was first run in the audit room by a read-only fork of main (`audit/verify_two_higgs/`) and moved
  here with one change (the repository root's depth in the path); rerun here, `repro_run.txt` is byte-identical.
- The seat's TWO_HIGGS result note was read before the reproduction ran; the reproduction checks the seat's numbers, it
  makes no prediction. `scan.py` writes `scan.json` (every row, 4.4 MB), not committed; `scan_run.txt` carries its summary.

## Files

- `verification/repro.py` → `repro.json`, `repro_run.txt`; `verification/scan.py` → `scan_run.txt`.
- The lock: `tests/test_b1742_two_higgs_verified_on_main.py`.
