# Act III Roadmap — From Toy Universe to Observable Universe

This document sketches the *Act III* program for the Origin Axiom project: how we go from the toy θ★ + microcavity + FRW scaffolding (Act II) to contact with the actual observed universe.

It is intentionally high-level and modular. Each block can become its own notebook, script, or paper subsection.

---

## 0. Inputs from Act II (What We Already Fixed)

We will treat the following as *frozen inputs* going into Act III:

- **Flavor prior on θ★**:  
  - Fiducial value: θ★₍fid₎ ≈ 3.63 rad  
  - 1σ-ish band: [2.18, 5.54] rad  
  - Provenance: combined posterior from `NO_theta_star_delta_only_N2000`, `NO_theta_star_v2_N2000`, `NO_theta_star_v2_N4000`, `NO_theta_star_v2_N8000` in `origin-axiom-theta-star`.
- **Microcavity ΔE(θ★) curve** in the 1D toy model:
  - Stored in `data/processed/theta_star_microcavity_scan_full_2pi.npz` (origin-axiom).
  - ΔE(θ★) has a broad negative minimum, with the fiducial θ★ sitting inside that trough.
- **Toy mapping from ΔE(θ★) → Ω_Λ**:
  - Implemented in `run_frw_from_microcavity.py` and documented in Act II LaTeX (microcavity + FRW + scaling sections).
  - A *single* scale factor S is chosen so that ΔE(θ★₍fid₎) maps to the observed ΛCDM vacuum density ρ_Λ,obs.
- **Scaling sanity check**:
  - `scripts/estimate_lambda_scaling.py` computes the required S in J/m³ per unit of dimensionless ΔE and shows that, over the θ★ band, ρ_vac(θ★) comfortably spans values around ρ_Λ,obs.

Act III assumes all of this is *given* and focuses on sharpening predictions and microstructure.

---

## 1. Microstructure Upgrade: From 1D Toy to Meaningful Vacuum Cells

**Goal:** replace the ultra-simple 1D chain toy with a more realistic notion of “vacuum cell” or “microcavity” that could plausibly tile a 3D universe.

### 1.1. Define a Minimal 3D Patch Model

- Start from the existing “nonlinear 3D toy universe” scripts and the two-field bump runs:
  - `run_toy_universe_compare_constraint_nonlinear.py`
  - `run_two_field_bump_1d.py` (+ its inspector)
- Design a **single 3D cell** (or a small block of cells) with:
  - scalar fields (φ, χ, …) obeying the non-cancelling rule,
  - a localized defect / cavity region,
  - boundary conditions comparable to a coarse-grained cosmological patch.
- Deliverable:
  - A new module `src/microstructure/cell_3d.py` plus a driver script `src/run_3d_cell_scan.py` that:
    - sweeps over constraint strength ε,
    - monitors vacuum energy density inside and outside the cavity,
    - saves results to `data/processed/3d_cell_scan_*.npz`.

### 1.2. “Einstein Limit” Check for the Cell

- For small field amplitudes and small curvature (i.e. weak deformations), the cell’s effective stress-energy should match a **perfect fluid** with some (ρ, p).
- Task:
  - Introduce a simple mapping from lattice energy to an effective equation of state parameter w = p/ρ.
  - Verify that, in the relevant regime, the non-cancelling constrained vacuum behaves like w ≈ –1 (or close enough) when viewed at large scales.
- Deliverable:
  - Notes in `docs/SCALING_NOTES.md` describing this mapping,
  - plus a short script `scripts/check_einstein_limit_cell.py` that prints effective (ρ, p, w) for a family of cell runs.

---

## 2. From Cells to a Coarse FRW Patch

**Goal:** combine many micro-cells into an effective homogeneous FRW description, maintaining the link to θ★.

### 2.1. Define an Effective “Vacuum Tiling” Model

- Assume a large volume filled with identical cells (or a small set of cell types).
- Each cell has:
  - a microscopic ΔE_cell(θ★),
  - an effective vacuum density contribution ρ_vac,cell(θ★).
- Task:
  - Write a small library `src/vacuum_effective.py` with helpers:
    - `rho_vac_from_cells(theta_star, cell_params)`
    - `Omega_lambda_from_cells(theta_star, H0, Omega_m)`
- Deliverable:
  - A script `src/run_frw_from_cells.py` that:
    - loads θ★ config,
    - chooses a tiling / cell configuration,
    - runs FRW histories as in `run_frw_from_microcavity.py`,
    - compares to the “pure microcavity ΔE” scaling.

### 2.2. Consistency with Act II θ★ Band

- For θ★ in [2.18, 5.54] rad, check:
  - how much Ω_Λ and ρ_vac vary across the prior band, 
  - whether some sub-interval is particularly natural (e.g. stability, cell spectrum nice, etc.).
- Deliverable:
  - Plots: Ω_Λ(θ★) vs θ★, w_eff(θ★) vs θ★.
  - Short LaTeX subsection: “Act III: effective vacuum fluid from microstructure cells”.

---

## 3. First Observational Touchpoints

**Goal:** identify low-hanging observational handles where this framework could, in principle, deviate from vanilla ΛCDM or at least be mapped onto it.

### 3.1. Background Expansion (H(z))

- With a range of Ω_Λ(θ★) and w_eff(θ★), we can generate families of H(z) curves:
  - Use standard FRW equations with the effective fluid.
  - Compare qualitatively to:
    - SNe Ia Hubble diagrams,
    - BAO distance measures,
    - Cosmic chronometer data (H(z)).
- This will remain **conceptual** in Act III (no serious data fitting yet), but we can still check:
  - Are there θ★ values in the band that are obviously ruled out at background level?
- Deliverable:
  - A script `scripts/plot_Hz_family_from_theta_star.py` that:
    - samples θ★ in the prior band,
    - plots the corresponding H(z) curves,
    - overlays a rough ΛCDM reference.

### 3.2. Order-of-Magnitude Check vs. ΛCDM Parameters

- Map the microstructure-based ρ_vac (for θ★ near the fiducial) onto:
  - an effective Ω_Λ,
  - a possible small deviation in w (if present),
  - and check if those are within current observational error bars (Planck, SNe, etc.).
- Deliverable:
  - Short note in `docs/SCALING_NOTES.md` or a new `docs/OBSERVABLES_NOTES.md` summarizing which ranges of Ω_Λ and w are observationally allowed and how our model sits inside that space.

---

## 4. What Would Count as a Real Prediction?

**Goal:** make explicit what kind of future calculation would *falsify* or strongly support the Origin Axiom picture.

### 4.1. Sharp Predictions

Candidates for “sharp” predictions (even if we cannot compute them fully yet):

- A constrained relation between:
  - θ★ and Ω_Λ,
  - or θ★ and some other cosmological parameter (e.g. σ₈, n_s) via vacuum microstructure.
- A specific pattern of how vacuum energy responds to defects / cavities at different scales (e.g. scaling with cavity size or curvature).
- A requirement that certain θ★ values are unstable or forbidden once we include more realistic geometry or gauge fields.

These are targets for *future* heavy computations, but Act III should list them clearly.

### 4.2. “No-Go” / Consistency Checks

- Ensure that the non-cancelling rule does **not** lead to obvious paradoxes:
  - Energy conditions grossly violated everywhere,
  - Catastrophic instabilities at small scales,
  - Incompatibility with standard GR in weak-field tests.
- Deliverable:
  - A checklist in `docs/CONSISTENCY_CHECKS.md` with items to verify as the model grows.

---

## 5. Act III Paper Skeleton

Finally, outline a potential *Act III* paper that sits after the current Act II LaTeX:

1. **Introduction & Motivation**
   - Recap: Origin Axiom, θ★ from flavor, non-cancelling principle.
   - Why microstructure + cosmology is the next frontier.
2. **Microstructure Cell Model**
   - Construction of 3D cells, constraints, vacuum energy definition.
   - Einstein-limit mapping to an effective fluid.
3. **From Cells to FRW**
   - Coarse-graining procedure.
   - θ★-dependent vacuum density and equation of state.
4. **Comparison with ΛCDM Background**
   - H(z) families, Ω_Λ and w ranges.
   - Scaling assumptions and how to falsify them.
5. **Predictions, Open Problems, and Future Work**
   - Concrete numerical targets,
   - Needed upgrades (gauge fields, spinor matter, full curvature coupling).

This skeleton can eventually become `docs/paper/act3_microstructure_and_cosmology.tex`.

---

## 6. Immediate Next Steps (Concrete)

If we want to *keep momentum* with small, clear steps, a practical order could be:

1. **Create** a stub file `docs/ACTIII_ROADMAP.md` (this file) in the repo.  
2. **Add** a short section to `SCALING_NOTES.md` linking to this roadmap (so future you knows where to look).  
3. **Next code task:** implement `src/vacuum_effective.py` with *dummy* cell inputs that just wrap the existing microcavity ΔE(θ★).  
4. **Then:** write `src/run_frw_from_cells.py` as a thin wrapper over `run_frw_from_microcavity.py` but using the new interface.

From there we can gradually swap in more realistic microstructure without breaking the higher-level pipeline.

