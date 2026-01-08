# FRW Corridor Promotion Gate v1

**Purpose:**  
Define the minimum conditions under which Stage 2 FRW corridor results
may be **promoted** into:

- Phase 5 (or later) papers, or
- a dedicated FRW-focused phase / standalone paper.

Until this gate is passed, all FRW corridor diagnostics remain **Stage 2
exploratory work** and must not be described as physical predictions.

---

## 1. Scope

This gate applies to:

- `stage2/frw_corridor_analysis` rungs and successors,
- any future Stage 2 FRW axes that consume Phase 3–4 artifacts and
  attempt to relate θ, mechanism outputs, and cosmological observables.

It does **not** retroactively constrain:

- Phase 3 mechanism definition,
- Phase 4 FRW pipeline as documented in the Phase 4 paper.

---

## 2. Preconditions for promotion

A FRW corridor result may be promoted only if **all** of the following
are satisfied.

### (A) Data-backed

1. A concrete external FRW dataset is used, e.g.:

   - binned distance–redshift measurements, or
   - equivalent cosmological probes.

2. The dataset is:

   - explicitly described in the text,
   - versioned and cited,
   - either bundled in a reproducible location (or clearly referenced).

3. The Phase 4 / Stage 2 pipeline produces a **non-trivial** data mask:

   - `data_ok = 1` for at least some θ-grid points,
   - sensitivity to data is demonstrated (e.g. perturbing data or model
     changes the mask in a visible way).

### (B) Robust under reasonable choices

1. The FRW corridors and any proposed promoted family must be robust
   under:

   - small variations in mechanism parameters,
   - reasonable alternative grid resolutions,
   - modest changes in smoothing / stride / threshold choices.

2. This robustness must be demonstrated with:

   - tables / plots, and
   - clear quantitative thresholds (e.g. Jaccard overlap ≥ X, fraction
     changes within Y%).

### (C) Clearly formulated claims

1. The text must distinguish between:

   - **structural statements** (“this region exists on the grid with
     these properties”), and
   - **physical statements** (“this region is compatible with data and
     corresponds to a family of universes with properties P”).

2. Any promoted claim must be:

   - precise,
   - falsifiable in principle,
   - explicitly tied to:

     - the data used,
     - the mechanism configuration,
     - the θ-grid definition.

3. The role of θ\* must be described **without hype**, e.g.:

   - “θ\* lies within a data-compatible corridor of type X,” vs.
   - “the universe prefers θ\*,” unless we can define and justify that
     preference statistically and conceptually.

### (D) Reproducibility

1. The full pipeline from repo checkout to promoted figure/table must be
   reproducible via:

   - a small number of documented commands,
   - with clear instructions on external data placement.

2. All scripts and configs used in the promoted results must live in
   the repo under:

   - `phase4/` and/or
   - `stage2/` (or a successor axis),

   and be covered by a reproducibility appendix.

---

## 3. Promotion paths

If the above preconditions are met, promotion may proceed in one of two
modes:

### Option A — Minimal integration into an existing phase

- A short subsection in Phase 5 (or later), e.g.:

  - “FRW corridor diagnostics and data compatibility”

- Content restricted to:

  - describing the existence of data-compatible corridors,
  - summarizing their robustness,
  - neutrally stating how θ\* is positioned relative to them.

### Option B — Dedicated FRW phase / paper

- A new phase (e.g. Phase 6) or standalone paper centered on:

  - construction and analysis of FRW corridors,
  - interaction with data,
  - implications for the non-cancellation program.

- May contain richer interpretation, but must remain within the
  constraints above.

---

## 4. Current status (as of 2026-01-09)

- Stage 2 rungs 1–9 have established that:

  - the families F1–F5 are structurally robust on the current θ-grid,
  - θ\* sits deep inside the FRW-viable family F1,
  - no real FRW dataset is currently used in Phase 4.

- Therefore:

  - **Condition (A)** (data-backed) is not satisfied,
  - promotion into any phase paper is **not permitted** yet.

Until this document is updated and the conditions are explicitly marked
as satisfied, all FRW corridor results must be treated as **Stage 2
exploratory diagnostics only**.

