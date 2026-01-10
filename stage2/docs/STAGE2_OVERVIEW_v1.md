# Stage 2 Overview and Verdict (v1)

**Scope:** High-level overview of Stage 2 diagnostic rungs built on top of
Phase 3 (mechanism) and Phase 4 (FRW) outputs. This document summarizes what
we actually did, what nontrivial structure we found, what we did *not* find,
and how Stage 2 sits in the overall 5-phase program.

**Status:** Descriptive / diagnostic. No new claims, no promotions into
Phase 3/4/5 are enacted here.

---

## 1. Position of Stage 2 in the program

Stage 2 is a **diagnostic belt** that sits *downstream* of:

- Phase 3: the mechanism scan and measure-like summaries,
- Phase 4: the FRW grid, viability bands, and toy corridor definitions.

Stage 2 does **not** change the mechanism or FRW runs; instead it:

1. Reads the Phase 3 and Phase 4 outputs (tables),
2. Builds a consistent θ-grid view of those outputs,
3. Probes structure:

   - in the FRW families and corridors,
   - in the mechanism-derived “measure” candidates,
   - in their joint correlations,
   - and in the current data probes,

4. Provides internal diagnostics for possible future promotions into Phase 4/5
   (via Option A/B as defined in `stage2/docs/STAGE2_PROMOTION_DESIGN_v1.md`).

All Stage 2 artifacts are therefore **non-canonical** until explicitly promoted.

---

## 2. FRW corridor belt (rungs 1–9)

### 2.1. What we did

Using the Phase 4 FRW tables:

- `phase4_F1_frw_viability_mask.csv`
- `phase4_F1_frw_lcdm_probe_mask.csv`
- `phase4_F1_frw_shape_probe_mask.csv`
- `phase4_F1_frw_data_probe_mask.csv`

Stage 2 built a series of FRW “family” and “corridor” diagnostics:

1. **Rung 1–2: Sources and boolean census**

   - Inventory & boolean-column census over the Phase 4 FRW masks.

2. **Rung 3: FRW families on the θ grid**

   Defined the main families on a 2048-point θ grid:

   - F1_FRW_VIABLE
   - F2_LCDM_LIKE
   - F3_TOY_CORRIDOR
   - F4_CORRIDOR_AND_VIABLE
   - F5_CORRIDOR_AND_LCDM
   - F6_DATA_OK (currently empty)

   and counted how much of the θ grid each occupies.

3. **Rung 4: Family overlaps**

   - Quantified pairwise overlaps between the families, especially:
     - intersections of corridor with viable and LCDM-like sets.

4. **Rung 5: θ histograms and ω_Λ scatter**

   - Produced structural plots:
     - θ histograms of the main families,
     - ω_Λ vs θ scatter highlighting family membership.

5. **Rung 6: Contiguity**

   - Measured how many **contiguous segments** each family breaks into
     along the θ grid.

6. **Rung 7: Stride robustness**

   - Re-sampled the grid with strides (1, 2, 4, 8) and checked:

     - whether the **fraction of true points** remained stable,
     - whether contiguity structure survived sub-sampling.

7. **Rung 8: Smoothing robustness**

   - Applied small-window boolean smoothing and checked:

     - true fractions before/after,
     - change in segments,
     - Jaccard similarity of masks.

8. **Rung 9: θ★ alignment diagnostic**

   - For each FRW family, found:

     - the θ inside that family closest to θ★ ≈ φ^φ,
     - the absolute distance |θ – θ★|,

   as an *internal* sanity check, not as a discovery engine.

### 2.2. What we found (nontrivial structure)

- The FRW-viable set occupies **about half** of the θ grid.
- The toy corridor occupies **more than half** the grid, and its intersections
  with viability and LCDM-like subsets are non-empty and structured.
- Families like FRW_VIABLE and TOY_CORRIDOR are:

  - **contiguous or nearly contiguous** in θ,
  - **robust** under stride sub-sampling,
  - **robust** under small-window smoothing.

This means the FRW scan is not a random sprinkling of good/bad points; it has
coherent bands in θ-space.

### 2.3. What we did *not* find

- No data-driven corridor yet: the current `data_ok` flag is **empty** in this run,
  so there is no observationally selected corridor.
- No promotion of any specific corridor to “truth”: Stage 2 only reports structure
  in the scan; it does not declare any corridor as physical.

---

## 3. Mechanism / measure belt (rungs 1–6)

### 3.1. What we did

Using Phase 3 tables:

- `mech_baseline_scan.csv`
- `mech_binding_certificate.csv`
- `phase3_measure_v1_hist.csv`
- `phase3_measure_v1_stats.json`
- plus their diagnostic JSONs,

Stage 2:

1. **Inventoried** Phase 3 tables and columns.
2. **Flagged “probability-like” columns** based on ranges, monotonicity hints,
   and basic statistics.
3. **Separated** candidates into:
   - potential “measure-like” scalars,
   - potential “flag-like” booleans.
4. Built **θ profiles** for the candidate measures.
5. Selected a small set of **preferred measure candidates** based on:

   - smoothness,
   - boundedness,
   - lack of pathological spikes,
   - plausibility as something one might integrate or threshold.

All of this remains diagnostic: no single measure is declared “the” measure.

### 3.2. What we found

- Several mechanism-derived scalars behave smoothly over θ and are well-behaved
  enough to be **kept as future measure candidates**.
- The Phase 3 outputs are internally consistent enough that Stage 2 can:

  - re-interpret them as candidate measures,
  - align them with FRW quantities on a common θ grid.

### 3.3. What we did *not* find

- No unique or canonical measure function yet.
- No final choice of weighting scheme or probability measure on θ; Stage 2 only
  curates **candidates**.

---

## 4. Joint mech–FRW belt (rungs 1–4)

### 4.1. What we did

1. **Built a joint θ grid** combining:

   - FRW columns: `E_vac`, `omega_lambda`, `age_Gyr`, family flags,
   - Mechanism columns: selected amplitudes / bounds from Phase 3,

   all on the same 2048-point θ grid.

2. **Family summaries**

   - Re-expressed the FRW families (viable, LCDM-like, corridor, intersections)
     in this joint space.

3. **Joint correlations**

   - Computed correlations between:

     - FRW vacuum/age quantities `(E_vac, omega_lambda, age_Gyr)` and
     - mechanism-derived amplitudes/bounds.

4. **Family-restricted correlations**

   - Looked at correlations within specific FRW families rather than
     on the full grid, as a diagnostic of how tightly the mechanism and
     FRW structures are entangled.

### 4.2. What we found (nontrivial structure)

- Strong correlations between:

  - `E_vac` / `omega_lambda` and certain mechanism amplitudes,
  - `age_Gyr` and those same amplitudes, with opposite sign.

- This means: within this model and this scan, the mechanism’s effective
  “strength” is **not independent** of the FRW background; they co-vary in a
  simple, structured way over θ.

We interpret this as **internal structural consistency**, not yet as an
observational claim.

### 4.3. What we did *not* find

- No evidence that the joint structure singles out a unique θ or a narrow
  corridor that would be compelling on its own.
- No observational selection: all results are entirely internal to the model
  and the chosen scan.

---

## 5. FRW data probes (rungs 1–2)

### 5.1. What we did

Using `phase4_F1_frw_data_probe_mask.csv`, Stage 2:

- Cross-tabulated the “probe” flags (`has_matter_era`, `has_late_accel`,
  `smooth_H2`, `frw_viable`, `data_ok`) against the main FRW viability flag.

### 5.2. What we found

- `has_matter_era` and `smooth_H2` are essentially **always true** in this grid.
- `has_late_accel` and `frw_viable` are tightly aligned (same fraction of grid).
- `data_ok` is **false everywhere** in this run.

So the current “data probe” layer acts more like a structured consistency check
than a real observational filter.

### 5.3. Negative result

- There is *no* θ region currently satisfying `data_ok` = true.  
  This is an important negative result and is why Stage 2 does **not** attempt
  to define a “data corridor” yet.

---

## 6. θ★ diagnostic rung

### 6.1. What we did

- For each FRW family, Stage 2 located the grid point in that family closest
  to θ★ ≈ φ^φ on the θ grid and recorded:

  - the nearest θ,
  - the grid index,
  - the absolute distance |θ – θ★|.

This is a **sanity check** meant to detect any obvious pathologies, not a
search for a special coincidence.

### 6.2. What we found

- For at least one FRW-viable family, θ★ lies fairly close to a viable point,
  but:

  - θ★ is **not** at a singular or isolated spike of viability,
  - other families have nearest points noticeably farther away.

In other words:

- θ★ behaves like an ordinary point in the viable belt of this scan,
- there is **no dramatic “θ★ is uniquely picked out” signal** in these FRW
  diagnostics.

This is exactly what we want at this stage: θ★ is neither excluded nor
artificially privileged by our current FRW setup.

---

## 7. Global verdict on Stage 2

### 7.1. What Stage 2 gives us

Stage 2 delivers:

1. **Evidence of structure** in the θ landscape:

   - FRW viability and corridor bands are coherent and robust.
   - Mechanism-derived scalars are smooth and well-correlated with FRW quantities.

2. **A curated shortlist of measure candidates**, but no final measure.

3. **Joint mech–FRW correlations** that show the mechanism and FRW pieces are
   meaningfully coupled in this model.

4. **A clean negative result** for the current data probe (`data_ok` empty),
   which prevents premature data-driven claims.

5. **A θ★ sanity check** that shows θ★ is compatible with the present FRW
   structure but not obviously singled out by it.

### 7.2. What Stage 2 does *not* yet provide

- No observational corridor or constraint on θ (data layer is not active).
- No canonical measure or probability distribution on θ.
- No promotion of Stage 2 artifacts into the main phase papers (this is gated
  by `STAGE2_PROMOTION_DESIGN_v1.md`).

---

## 8. Relation to Option A / Option B promotions

The separate doc `stage2/docs/STAGE2_PROMOTION_DESIGN_v1.md` specifies how
Stage 2 artifacts *could* be promoted into Phase 4/5 under:

- **Option A:** minimal, diagnostic/supporting inclusions (a few tables/figures,
  clearly labeled as structural, not as new physics), and
- **Option B:** a future dedicated FRW/measure phase or paper with more ambitious
  claims.

This overview is meant to be read *before* that design doc, to understand
what Stage 2 actually did and which structural features any promotion would
be talking about.

---

## 9. Next steps (conceptual, not enacted here)

Possible future directions, all gated by additional rungs:

1. **Option A enactment:**
   - Freeze specific Stage 2 artifacts,
   - Export a small set of Phase-4-/Phase-5-compatible tables/figures
     (FRW fractions, one joint correlation plot, preferred measure candidate
     list, data_ok negative result),
   - Integrate them as clearly labeled supporting material.

2. **Data layer refinement:**
   - Redefine or refine `data_ok` using more realistic observational proxies,
   - Re-run FRW and Stage 2 belts to see if a genuine “data corridor” appears.

3. **Measure follow-up:**
   - Explore how the preferred measure candidates behave under model variants,
   - Test whether any candidate yields a stable, interpretable weighting on θ.

None of these are enacted in this document; they are targets for future rungs.


## Status and promotion

Stage 2 lives strictly downstream of Phase 3 and Phase 4 artifacts and is non-canonical. No Stage 2 result is currently promoted into any Phase paper or the global claims ledger. For the up-to-date gate and status table, see `docs/GATES_AND_STATUS.md`.
