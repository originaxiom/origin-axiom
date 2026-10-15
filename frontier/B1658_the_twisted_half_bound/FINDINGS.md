# B1658 — THE TWISTED HALF BOUND: in B1656's twisted frame under equal framed data, one Higgs cannot spread the sectors' second generations by more than a factor 4 — exactly, for every complex Higgs; the data's M_Z ratios need 16, so one Higgs is out (a scoreboard)

**Verdict: PROVED.** Every cell holds as sealed. cc (main), 2026-10-15.
- Sealed `b6542d300` (sha256 3fd8de72) before the run. The output was committed unread at `04d64c2ff` (one run,
  12 s, exit 0; the instrument unchanged since the seal, sha256 54610f33).
- **0 of 19.** The census (T4) reads data that were seen: a scoreboard, not a blind test.
- POINT_REGISTER P-163, after the SM seat's W90 (verified on main). The weave's fibre at ω on W59's lines, given Λ,
  the dictionary and B1654's premises with B1656's four channels; T1–T2b hold for any null matter residue.

## 0. Seen first

As sealed: `VERDICT topic-sweep /twisted half bound|one higgs|quaternion.{0,20}(null|norm)|adj.{0,10}Y|half bound/: 16 of 1429 arcs on main match (NEGATIVE 3, OPEN 2, PROVED 11)`
— the precedents B1645 (the half bound, untwisted) and B1653; the rest in other senses. Read: B1656, B1657, the SM seat's
W90 and its relay §124, the web seat's two-weaves reading. **Literature:** SU(2) invariants of ℂ²; adjugates of bilinear
maps.

## 0b. Disclosed

In full in the preregistration's §0b: main's exploration (seven scripts and notes, beside the seal) and a draft run in
which every cell held; two read-only reviewing passes before the seal (the first: the range holds for EVERY complex
Higgs — now T2b — A transposed, a control that could not fail, "complexified", the M_Z wording; the second: the census
one-sided — now two-sided — the controls relabelled and an outside-bound control added, nullness per line, the scale
sentence softened). The test first planned for P-163 (the symmetric null Higgs at ω against the data's ratios) was not
run: the bound makes it moot.

## 1. The sealed run (`verification/the_twisted_half_bound.py`, unchanged; `.json`, `_run.txt`)

**T0, plumbing** (not void): B1656's stored R₁/∣R∣ reproduced exactly; the residues null to 1.9 × 10⁻¹⁶.

| cell | prediction | identity or test | result |
|---|---|---|---|
| **T1**, the factorisation | adj Y(S, pqᵀ)/det S free of S, equal to q̃ p̃ᵀ; ∣∣p̃∣∣² = 2∣p∣⁴; ∣∣A∣∣ = 2∣∣M∣∣² | identity | **HOLDS:** symbolic, exact; numerically 2 ± 1.3 × 10⁻¹⁵ |
| **T2**, the norm law | ∣∣Y(uvᵀ, pqᵀ)∣∣² = (∣u∣²∣p∣² + ∣u†p∣²)(2∣v∣²∣q∣² − ∣vᵀq∣²); range [1, 4] attained | identity | **HOLDS:** symbolic residual 0; numeric 3.6 × 10⁻¹⁵; 1 and 4 attained |
| **T2b**, every Higgs | for null M the Gram spectrum of S ↦ Y(S, M) is {1, 2, 2, 4}∣∣M∣∣²; a non-null M departs | identity; a check | **HOLDS:** 5.3 × 10⁻¹⁵; non-null ≥ 0.021 |
| **T3**, the spectrum on W59's lines | every residue null; m₁ = 0; σ₁σ₂ = 2∣det S∣∣∣M∣∣², σ₁² + σ₂² = ∣∣Y∣∣²; the k law to 10⁻³; k ∈ [½, 2] | identities; the k law a test | **HOLDS:** null 4.2 × 10⁻¹⁶; m₁ 4.7 × 10⁻¹⁶; 2.2 × 10⁻¹⁵; 7.0 × 10⁻⁶; k in [0.512, 1.889] |
| **T4**, the census (a scoreboard) | t + 1/t from the M_Z ratios, two-sided against 4 | scoreboard | **REFUTES one Higgs:** up/leptons 15.92 (27σ above 4); up/down 5.08 (2.3σ above, not by itself a refutation); down/leptons 3.13 (within) |
| **T5**, controls | the census refutes a three-Higgs fit of the data; passes a synthetic one-Higgs world; refutes it scaled ×6 outside the bound; passes it scaled to 3.9 | tests of the census; (b) an identity | **HOLDS:** True, not refuted (ratios 1.79, 1.09, 1.64), refuted, not refuted |

## 2. What it shows

- **The twisted half bound.** In B1656's frame, under equal framed data (C0's one normalisation), each sector's spectrum
  is exactly (1, t, 0), with t + 1/t = ∣∣Y(S, M_s)∣∣²/(2∣det S∣∣∣M_s∣∣²). For null M the map S ↦ Y(S, M) has the
  Gram spectrum {1, 2, 2, 4}, so ∣∣Y∣∣² ∈ [1, 4]·∣∣S∣∣²∣∣M∣∣² for every complex Higgs. **One Higgs shares det S and
  ∣∣S∣∣ across the sectors, so their (t + 1/t) lie within a factor 4 of each other — exactly.** For a nearly null Higgs
  this reads m₂/m₃ = k_s∣d_S∣ with k_s = 2/((1 + x_s)(2 − y_s)) ∈ [½, 2], B1645's half bound carried into the twisted
  frame.
- **Against the data** (HZ2021 at M_Z, seen): the up quarks' and the leptons' second generations need a factor 15.9 in
  t + 1/t, 27σ above the bound. So "one Higgs, under equal framed data, in B1656's frame" is refuted — a scoreboard
  entry beside the SM seat's W88 and W90, not a closed door (E89): it refutes that combination, not the frame's other
  readings. Under equal framed data the first generation is massless in every sector anyway, a known miss (W88's Q1);
  this census adds the second generation.
- **What is left** for a single field's second generations to be spread by the data's factors: the canonical end
  condition's joint law (the matter's own defect D_s/(2πL) as a second term — main's exploration finds the adjugate
  splits as det S·A(M) + det M·Ã(S) at leading order, `before_the_seal/joint_law.py`), a Higgs that differs by sector
  (the web seat's two-point term between threads; the owner's ruling on such terms, P-166), or the cusp, where couplings
  go as powers of q and spreads of this size are natural.

## 3. What it does not show

The joint law under the canonical end condition; the first generation; other lines or τ (T1–T2b hold for any null M);
the interacting weave; any value. The census compares with M_Z running ratios; that a factor 16 against 4 survives
running is assumed, not computed.

## 4. Credit

The SM seat's W90, which this extends, and its relay §124 (the Higgs's factor is the same in every sector of B1656's
frame). Main's two reading agents: the first found that the bound holds for every complex Higgs, which made the census
exact; the second made the census two-sided and its controls able to fail.
