# Stage 2 → Phase 4/5 Promotion Design (v1)

**Scope:** Design-only document for *possible* promotion of Stage 2 artifacts  
into Phase 4/5 (or a later dedicated phase). No promotions are enacted here.

**Status:** Planning / contract rung. All Stage 2 artifacts remain internal diagnostics.

---

## 1. Motivation

Stage 2 has produced a dense belt of diagnostics:

- FRW corridor analysis (rungs 1–9),
- Mech/measure analysis (rungs 1–6),
- Joint mech–FRW analysis (rungs 1–4),
- FRW data probes (rungs 1–2),
- θ★–FRW alignment diagnostic.

These rungs reveal **nontrivial structure** (robust FRW bands, strong mech–FRW correlations,  
negative results for current data probes, and a clean θ★ sanity check), but all of them are  
currently gated as **internal**.

This document answers:

> If we ever promote some of this into the main Phase 4/5 narrative, *what exactly* would we promote, under *what conditions*, and in *which minimal form*?

---

## 2. Promotion modes: Option A vs Option B

We distinguish two kinds of promotion:

### 2.1. Option A — Minimal “supporting material” promotion

Characteristics:

- **Few artifacts** (e.g. 1–3 tables/figures),
- Clearly labeled as **diagnostic / structural**, not as “new physics”,
- Integrated as **short subsections** or appendices in existing phase papers,
- Requires **strong robustness and interpretability**, but can live as “supporting evidence”.

Option A is meant to:

- help readers see the structure of the θ landscape,
- show that the mechanism and FRW pieces are not random,
- document negative results (like the current “data_ok” flag) in a controlled way.

### 2.2. Option B — Dedicated follow-up phase / paper

Characteristics:

- Larger set of artifacts, potentially including:
  - refined data probes,
  - richer mech–FRW joint measures,
  - more sophisticated corridor constructions,
- Likely requires **new runs** and possibly **new θ grids**,
- Framed as a separate Phase (e.g. “Phase 6: FRW corridors and measure”) or separate paper.

Option B is where genuinely new *claims* about FRW corridors, data selection, or measure  
would live, once the diagnostics are mature enough.

**This document primarily designs Option A.**  
Option B is sketched as a roadmap target, not something we commit to now.

---

## 3. Candidate artifacts from Stage 2 belts

This section lists **what could** be promoted (not what *will* be).

### 3.1. FRW corridor belt (rungs 1–9)

**Representative inputs:**

- Tables:
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung3_families_v1.csv`
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung4_family_overlap_v1.csv`
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung6_contiguity_v1.csv`
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung7_stride_robustness_v1.csv`
  - `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung8_smoothing_v1.csv`
- Figures:
  - `stage2/frw_corridor_analysis/outputs/figures/stage2_frw_corridor_family_theta_hist_v1.pdf`
  - `stage2/frw_corridor_analysis/outputs/figures/stage2_frw_corridor_family_omega_lambda_scatter_v1.pdf`

**Option A candidates:**

1. **FRW viability fraction table**  
   - Very small, Phase-4-friendly table summarizing (for current run):
     - total grid size (2048),
     - counts/fractions for:
       - FRW_VIABLE,
       - LCDM_LIKE,
       - TOY_CORRIDOR,
       - CORRIDOR_AND_VIABLE,
       - CORRIDOR_AND_LCDM,
       - DATA_OK (empty in this run).
   - Could become an appendix table in Phase 4.

2. **FRW family θ histogram figure**  
   - A single multi-panel or color-coded θ histogram showing:
     - FRW_VIABLE band,
     - TOY_CORRIDOR,
     - their intersections (F4/F5).
   - Framed as “structure of the θ grid in our FRW scan”, nothing about θ★ selection.

3. **FRW ω_Λ vs θ scatter figure**  
   - A compact plot showing ω_Λ vs θ for the main families.
   - Purely structural: “what the current θ-grid scan looks like”.

**Non-candidates for Option A (for now):**

- Detailed contiguity / stride / smoothing diagnostics:  
  useful internally, but too technical for Phase 4 unless they become critical to a claim.
- The θ★ alignment table itself:  
  kept internal as a **sanity diagnostic** to avoid over-reading significance.

### 3.2. Mech/measure belt (rungs 1–6)

**Representative inputs:**

- `stage2/mech_measure_analysis/outputs/tables/stage2_mech_rung6_phase3_preferred_measure_candidates_v1.csv`
- Plus upstream inventory/stats/profiles tables.

**Option A candidates:**

4. **Short table of preferred measure candidates (Phase 3)**  
   - A trimmed, human-readable version of the preferred measures:
     - name,
     - basic range / behavior,
     - qualitative monotonicity / smoothness description.
   - Could be cited in Phase 3/5 discussion as:  
     “Post-hoc diagnostics suggest the following mechanism-derived scalars are the most structured and well-behaved; we keep them as candidates for future measure work.”

**Non-candidates for Option A (for now):**

- Full θ profiles and detailed heuristics for candidate selection:  
  these are Phase-0/Stage-2-ish and likely belong in a more technical follow-up.

### 3.3. Joint mech–FRW belt (rungs 1–4)

**Representative inputs:**

- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_theta_grid_v1.csv`
- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_rung3_correlations_v1.csv`
- `stage2/joint_mech_frw_analysis/outputs/tables/stage2_joint_mech_frw_rung4_family_correlations_v1.csv`
- `stage2/joint_mech_frw_analysis/docs/STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md`

**Option A candidates:**

5. **Single joint correlation figure**  
   - e.g. scatter of E_vac vs a representative mech amplitude (baseline_A or binding_A),
   - with correlation coefficient quoted.
   - Framed as:  
     “In this run, the Phase 3 mechanism-derived scalar tracks the FRW vacuum sector in a structured way; this is evidence that the mechanism and FRW scans are not independent knobs.”

6. **Short correlation table (condensed)**  
   - A compact table listing:
     - (E_vac, ω_Λ, age_Gyr) vs (one or two mech scalars),
     - correlation coefficients,
   - With a clear warning that this is **grid-internal structure**, not an observation-based constraint.

**Non-candidates for Option A (for now):**

- Family-restricted correlation matrices:
  - These are informative but could overcomplicate Phase 4/5 without clearer narrative pay-off.

### 3.4. FRW data probes belt (rungs 1–2)

**Representative inputs:**

- `stage2/frw_data_probe_analysis/outputs/tables/stage2_frw_data_probe_rung2_viability_cross_v1.csv`

**Option A candidates:**

7. **Negative-result note about current “data_ok”**  
   - A single sentence or brief footnote in Phase 4:
     - “Our current placeholder ‘data_ok’ flag is empty in this run, so we do not yet use it to define a data-informed corridor.”
   - This helps avoid confusion or over-interpretation.

### 3.5. θ★ diagnostic rung

**Representative inputs:**

- `stage2/frw_corridor_analysis/outputs/tables/stage2_frw_corridor_rung9_theta_star_alignment_v1.csv`
- `stage2/theta_star_analysis/docs/STAGE2_THETA_STAR_ALIGNMENT_v1.md`

**Option A stance:**

- **No direct promotion** of θ★ alignment tables/plots into Phase 4/5 at this stage.
- Instead, we keep θ★ diagnostics as an **internal guardrail**:
  - future promotions must not cherry-pick corridors that only “work” by retrospectively clustering around θ★.

---

## 4. Promotion criteria and gates

For any Option A artifact to be promoted, all of the following must hold:

1. **Reproducibility**
   - Artifact must be generated by a **documented script** in `stage2/.../src/`.
   - Inputs (Phase 3/4 tables) must be:
     - version-controlled,
     - stable under at least one rerun, and
     - logged in Phase 3/4/Stage 2 progress logs.

2. **Robustness**
   - For FRW families:
     - contiguity, stride robustness, and smoothing diagnostics show stable structure.
   - For mech–FRW correlations:
     - correlations do not disappear under small changes in the grid or filters.
   - For measure candidates:
     - no pathological spikes or sign flips that would mislead readers.

3. **Interpretability**
   - The artifact can be explained in **≤ 1–2 concise paragraphs** in a phase paper.
   - Axes, units, and semantics are unambiguous.

4. **Narrative alignment**
   - The artifact supports the **core narrative**:
     - non-cancellation principle,
     - structure of the θ landscape,
     - interaction between mechanism and FRW background,
   - without prematurely implying claims about observational cosmology or final measures.

5. **θ★ neutrality**
   - The artifact must not be constructed or cherry-picked to “favor” θ★.
   - θ★ diagnostics must be checked:
     - if a promoted artifact happens to highlight θ★, it must be *explicitly* justified and described as such.
   - Current design prefers artifacts where θ★ is **just one ordinary viable point**.

6. **Labeling discipline**
   - Any Option A artifact must be labeled as:
     - “diagnostic”, “structural”, or “internal correlation” — not as “evidence for φ^φ”.
   - Negative results (like empty `data_ok`) are labeled as such.

---

## 5. Concrete Option A set (proposal, not enactment)

Given the above, a **minimal Option A package** (for future consideration) could be:

1. **FRW viability fraction table** (Phase 4 appendix).
2. **FRW θ histogram figure** showing the main families.
3. **One joint correlation figure** (E_vac vs a representative mech amplitude).
4. **Short note about `data_ok` being empty** in this run.
5. **Short table of preferred Phase 3 measure candidates** (Phase 3/5 appendix).

This package:

- is small enough to not distort the main narrative,
- shows that the θ scan + mechanism has **structure**,
- transparently documents the current limitations (no data corridor yet),
- keeps θ★ diagnostics internal as a sanity check.

---

## 6. Roadmap and future rungs

To actually enact Option A, we would need **dedicated promotion rungs**, e.g.:

1. **Rung P1 — Freeze Stage 2 inputs**
   - Confirm versions of Phase 3/4 tables and Stage 2 scripts.
   - Rerun all required Stage 2 scripts and log seeds / hashes.

2. **Rung P2 — Export canonical Option A artifacts**
   - Copy or regenerate selected tables/figures into Phase 3/4/5 `artifacts/` paths.
   - Add minimal LaTeX/Markdown hooks in the relevant phase papers.

3. **Rung P3 — θ★ promotion audit**
   - Explicitly check Stage 2 θ★ diagnostic doc against the chosen artifacts.
   - Confirm no hidden θ★ tuning.

4. **Rung P4 — Final promotion commit**
   - Update PROGRESS_LOG with a “Promotion enacted” entry,
   - Tag or branch the repo for this publication-ready configuration.

**This document (v1)** does not perform P1–P4; it only defines the intended shape of such rungs.

---

## 7. Status

- Stage 2 remains a **diagnostic belt**.
- This promotion design doc provides:
  - a shortlist of candidate artifacts,
  - strict criteria and θ★ guardrails,
  - a clear path for Option A promotions,
  - and a placeholder vision for a future Option B / dedicated FRW–measure phase.

