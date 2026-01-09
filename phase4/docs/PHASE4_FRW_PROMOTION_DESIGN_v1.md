# Phase 4 FRW promotion design (v1)

**Date:** 2026-01-09  
**Scope:** Decide, at design level, which Stage 2 FRW and joint mech–FRW
artifacts are candidates for inclusion in Phase 4 (or Phase 5) text and figures,
without yet editing the LaTeX.

This document is *downstream-only*: it consumes Stage 2 outputs and Phase 4
artifacts, and produces a promotion plan (not new claims).

---

## 1. FRW corridor content

### 1.1 Objects available (from Stage 2)

From `stage2/frw_corridor_analysis` and the Stage 2 overview:

- Families on a 2048-point θ grid:
  - **F1_FRW_VIABLE** (`frw_viable`)
  - **F2_LCDM_LIKE** (`lcdm_like`)
  - **F3_TOY_CORRIDOR** (`in_toy_corridor`)
  - **F4_CORRIDOR_AND_VIABLE** (`in_toy_corridor ∧ frw_viable`)
  - **F5_CORRIDOR_AND_LCDM** (`in_toy_corridor ∧ lcdm_like`)
- Fractions of grid:
  - F1 ≈ 0.496, F2 ≈ 0.031, F3 ≈ 0.579,
  - F4 ≈ 0.075, F5 ≈ 0.020.
- Rung 5 figures (PDFs):
  - `stage2/frw_corridor_analysis/outputs/figures/stage2_frw_corridor_family_theta_hist_v1.pdf`
  - `stage2/frw_corridor_analysis/outputs/figures/stage2_frw_corridor_family_omega_lambda_scatter_v1.pdf`
- Contiguity + robustness:
  - F1: single contiguous band; F2–F5: 2 segments each.
  - Smoothing / stride invariance tests (Stage 2 rungs 6–8).

### 1.2 Proposed Phase 4 usage (Option A vs Option B)

- **Option A (lightweight in Phase 4 main text):**
  - One short subsection, e.g.
    > “Corridors in θ-space and FRW viability”
  - Content:
    - Definition of F1–F5.
    - One compact table with the fractions of the θ grid.
    - One figure:
      - either θ-histogram, or (ω_Λ, E_vac) scatter, not both in the main text.
    - A sentence saying:
      > “We verified that the main conclusions are stable under simple
      >  smoothing/stride variations of the θ grid (see Stage 2 diagnostics).”
- **Option B (heavier FRW-focused material):**
  - Keep Phase 4 corridor story minimal.
  - Reserve the full pair of figures and more detailed discussion for a later
    FRW-focused stage/phase.

**Initial stance (v1):**  
We tentatively lean toward **Option A**: one figure + one table + a short
narrative, with the rest of the diagnostics staying in Stage 2 / appendix.

---

## 2. Mech/measure shortlist

### 2.1 Objects available (from Stage 2)

From `stage2/mech_measure_analysis`:

- A shortlist of smooth, probability-like measure candidates from Phase 3
  (Rungs 3–6).
- θ-profiles showing they are nontrivial and reasonably behaved.

### 2.2 Proposed Phase 4 usage

- Phase 4 is primarily about FRW / cosmology; measure content is supportive.
- Proposed usage:
  - One or two sentences in a “future directions” or “methodology” subsection:
    > “Phase 3 contains several smooth, probability-like scalars that can
    >  serve as candidate measures on θ-space; Stage 2 identifies and audits
    >  them, but we defer choosing a single preferred measure to later work.”
  - No figures in Phase 4 for measure yet (kept in Stage 2).

---

## 3. Joint mech–FRW correlations

### 3.1 Objects available

From `stage2/joint_mech_frw_analysis`:

- Joint θ-grid:
  - `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
- Global and family-conditioned correlations between:
  - `{E_vac, omega_lambda, age_Gyr}` and
  - `{mech_baseline_A0, mech_baseline_A_floor, mech_baseline_bound,
     mech_binding_A0, mech_binding_A, mech_binding_bound}`.

### 3.2 Proposed usage in Phase 4/5

- Conservative textual statement:
  - A short paragraph noting the existence of strong correlations between
    cosmological scalars and mechanical amplitudes, without causal language.
- Optional figure candidates (for Phase 5 or a later stage, not necessarily
  Phase 4):
  - A correlation matrix (heatmap) or a small panel comparing representative
    pairs, e.g. `omega_lambda` vs `mech_baseline_A_floor`.

**Initial stance (v1):**  
Phase 4 may include only a **textual summary** and leave visualizations of
these correlations to a later phase, to avoid overloading the main FRW section.

---

## 4. FRW data probes and `frw_data_ok`

### 4.1 Objects available

From `stage2/frw_data_probe_analysis`:

- Column stats for `has_matter_era`, `has_late_accel`, `smooth_H2`,
  `frw_viable`, `data_ok`.
- Viability cross-tables:
  - In current snapshot:
    - `has_matter_era` and `smooth_H2` always true.
    - `has_late_accel` ≡ `frw_viable`.
    - `data_ok` always false.

### 4.2 Proposed usage

- Phase 4 text:
  - Clarify that in this implementation, `frw_viable` is equivalent to
    “late acceleration present,” under always-true sanity checks.
- Explicitly state:
  - `frw_data_ok` is **currently closed** (no θ passes it).
  - Data-conditioned corridor claims are **postponed** until a future
    update of the data gate.

---

## 5. Boundaries and non-claims (v1)

To avoid drift, the following are explicitly **not** claimed at this stage:

- No choice of a unique, physically privileged measure on θ.
- No statement that any joint correlation “explains” Λ or FRW geometry.
- No data-conditioned corridor (`frw_data_ok`) until the upstream gate passes.

This document is a **design artifact** and does not by itself change
Phase 4/5 claims. Actual promotion will be handled in dedicated rungs that
edit the LaTeX under explicit contracts.

