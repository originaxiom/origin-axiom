# B630 — THE MATRIX COMPARISON DESIGN (the interaction round's one authorized comparison)

**Sealed 2026-07-15, AFTER the framework values were sealed and banked
(B629, sha 0ec9ac39…) and BEFORE any distance is computed anywhere.
SHA-256 of this file goes into frontier/B598_l85_campaign/
ARTIFACT_HASHES.txt at banking. The run arc (B631) verifies BOTH hashes
mechanically before computing. This design implements the
interaction-round directive's steps 2–4; the directive's discipline is
binding: one comparison, all nine distances reported, no tolerance
adjustment after seeing distances, no combination with Branch-3
statistics, and a null here means the SM-comparison capability at this
level is EXHAUSTED (no "next layer" escape).**

## 0. The two sides (fixed before this document)

- **Framework side (sealed in B629 §1):** |B_ij|², the moduli-squared
  table of the E₆₂ 3×3 odd hearing form — exactly the doubly-stochastic
  circulant of (A₁², A₂², A₃²) = ((4/7)sin²(2π/7), (4/7)sin²(4π/7),
  (4/7)sin²(6π/7)), rows/cols in B629's sealed channel order
  (27, 351′, 351). The held-out content is the ARRANGEMENT (Latin-square
  structure), disclosed at sealing.
- **Measured side:** |U_PMNS,ij|², rows (e, μ, τ), columns (1, 2, 3).

## 1. The frozen measured source (step 2 — ONE source, no mixture)

**Source: PDG 2024 central values**, for continuity with the campaign's
existing freeze (B615 froze the three sin² values verbatim in
frontier/B615_comparison/b615_comparison.py; they are reused byte-for-
byte, eliminating refreezing drift):

    sin²θ₁₂ = 0.307      sin²θ₂₃ = 0.546      sin²θ₁₃ = 0.0220
    δ_CP = 1.19π rad (PDG 2024 central; the one number newly frozen
    here; recorded from the assistant seat's knowledge of the PDG
    review — seat 4 flags if the printed source differs)

The nine |U_ij|² are DERIVED mechanically in B631 from these four
numbers via the standard parametrization (c_ij = cosθ_ij, s_ij = sinθ_ij):

    |U_e1|² = c₁₂²c₁₃²        |U_e2|² = s₁₂²c₁₃²        |U_e3|² = s₁₃²
    |U_μ1|² = |−s₁₂c₂₃ − c₁₂s₂₃s₁₃e^{iδ}|²
    |U_μ2|² = |c₁₂c₂₃ − s₁₂s₂₃s₁₃e^{iδ}|²                |U_μ3|² = s₂₃²c₁₃²
    |U_τ1|² = |s₁₂s₂₃ − c₁₂c₂₃s₁₃e^{iδ}|²
    |U_τ2|² = |−c₁₂s₂₃ − s₁₂c₂₃s₁₃e^{iδ}|²               |U_τ3|² = c₂₃²c₁₃²

The directive's handoff quoted an approximate (NuFIT-flavored) table;
it is NOT the frozen source. It enters only as robustness row R-a below.

## 2. The alignment rule (declared: no canonical channel↔generation map exists)

There is no banked map between the pair-channels (27, 351′, 351) and
the flavors/mass states. The statistic therefore MINIMIZES over all
alignments: 6 row permutations × 6 column permutations × {identity,
transpose} = 72 alignment configurations (for a circulant some coincide;
the degeneracy is harmless and is reported). The null model performs the
IDENTICAL minimization, so the alignment freedom is corrected by
construction, not by a post-hoc factor.

## 3. The distance metric (step 3 — chosen before computing)

- **The verdict statistic:** D = min over the 72 alignments of
  RMS(|B|² − |U|²) = min_a sqrt((1/9)Σ_ij (|B|²_a(i,j) − |U_ij|²)²).
- **The transparency table (the directive's step 6):** at the D-optimal
  alignment, ALL NINE absolute deviations |Δ_ij| are reported — match
  and miss, no selection — with match tiers |Δ| ≤ 0.01 and |Δ| ≤ 0.001
  (absolute, since the entries are probabilities in [0, 1]). The tier
  counts carry NO verdict weight (the verdict is D's p-value, which
  already includes the alignment look-elsewhere); they are the
  directive's required per-entry accounting, calibrated by the null's
  expected counts.

## 4. The null model (step 4)

**Ensemble:** Haar-random U(3), N = 10⁶ samples (complex Ginibre → QR
with the standard phase correction; fixed seed 20260715). For each
sample, |U_rand,ij|² is compared to the SAME frozen |U_PMNS|² table by
the SAME min-over-72-alignments RMS statistic D_rand.

- **The p-value:** p_D = (#{D_rand ≤ D_obs} + 1)/(N + 1).
- **The per-entry calibration:** from the same ensemble, the expected
  number of entries (out of 9, at each sample's optimal alignment)
  within 0.01 and within 0.001 of the measured table — the directive's
  "expected match count" computed exactly, not estimated.

Rationale: |U|² of ANY unitary matrix is doubly stochastic, so the Haar
ensemble is exactly the right reference class for "is the object's
doubly-stochastic table unusually close to the measured one." The
framework matrix's circulant constraint (2 free parameters) is a
property of the OBJECT, not of the null — restricting the null to
circulants would answer a different (weaker) question.

## 5. The verdict table (locked)

- **p_D < 0.01 — MATCH-CANDIDATE:** goes to seat 4 with the full raw
  output before ANY claim; no escalation without seat-4 review; even
  then, per the directive, no "the SM is derived" language.
- **0.01 ≤ p_D < 0.1 — AMBIGUOUS:** banked as suggestive-only; NO
  escalation; per the directive, no further SM comparison at this level
  without a new owner-level directive and a principled preregistration.
- **p_D ≥ 0.1 — STRUCTURED-NULL:** the stopping rule fires; the
  program's SM-comparison capability at this level is exhausted; the
  mathematics publishes as mathematics.

The deliverable sentence (verbatim template from the directive): "The
3×3 odd hearing form at E₆ level 2 [matches / does not match] the PMNS
matrix at the [X]% tier, with null-model p-value [Y]." Plus the raw
9-entry table. Nothing else.

## 6. Robustness rows (declared now; reported after the primary; NO verdict weight)

- **R-a:** D and the per-entry table recomputed against the directive
  handoff's quoted approximate table [[0.681, 0.297, 0.0222], [0.109,
  0.370, 0.521], [0.210, 0.333, 0.457]] (NuFIT-proxy sensitivity; the
  literature lesson that matches must be source-robust).
- **R-b:** D recomputed at δ_CP ∈ {0, π/2, π, 3π/2} with the frozen
  angles (CP-phase sensitivity; the e-row and column 3 are
  δ-independent, so only the μ/τ interior entries move).

## 7. MB12 triple-check (computed at sealing)

- **Non-trivial:** no matrix-level comparison has ever been computed in
  this program; D_obs is genuinely unknown at sealing (no distance has
  been evaluated; the seat has approximate knowledge of PMNS magnitudes
  from memory — the blindness lives in this mechanical protocol, not in
  the seat's ignorance, exactly as B614 §0 stated for Branch 3).
- **Can fail:** generic doubly-stochastic tables sit far from the
  measured one; the Haar median D is O(0.1–0.3); p_D ~ O(0.5) is a live
  outcome.
- **Can pass:** a circulant pinned near the measured table's bulk
  values would land in the Haar lower tail; p_D < 0.01 is a live
  outcome (the ensemble has positive density at small D).
- **The known structural limitation, recorded now:** the measured table
  contains one small entry (s₁₃² = 0.0220) while the circulant's
  smallest modulus² is A₃² ≈ 0.1076 — these two numbers were already
  publicly paired in B615's G2 grid (no match at either tier), so ANY
  alignment leaves ≥ 0.085 absolute deviation on that one entry. This
  bounds the per-entry match count at ≤ 8/9 a priori and puts a floor
  D_obs ≥ 0.0285 (= 0.0855/√9, if all other eight entries were exact).
  Whether that floor region is null-typical or null-rare is EXACTLY
  what the Monte Carlo decides — the directive's "why this could fail"
  clause anticipated this; it is a limitation of the object's matrix,
  not of the test.
- **Both hashes gate the run:** B631 verifies B629's sealed-values hash
  and this design's hash before computing anything; one run, no reruns.
