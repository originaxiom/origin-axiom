# Phase 4 FRW-facing synthesis (F1 mapping)

This note summarises what the Phase 4 FRW-facing infrastructure
actually does in the current baseline, and what the numerical
diagnostics say about the F1 mapping. It is intended as a
reader-facing bridge between the Phase 3 mechanism, the Phase 4
paper, and possible future, harder-novelty directions.

## 1. Pipeline recap

The current Phase 4 FRW-facing pipeline consists of the following
layers, all built on top of the F1 scalar mapping and the Phase 3
baseline diagnostics:

1. **F1 sanity curve**  
   - Code: `phase4/src/phase4/run_f1_sanity.py`  
   - Output: `phase4/outputs/tables/phase4_F1_sanity_curve.csv`  
   - Role: evaluate a toy vacuum-like scalar
     \(E_{\mathrm{vac}}(\theta)\) on a fixed \(\theta\)-grid and
     export a machine- and human-readable curve with basic
     diagnostics (extrema, moments, etc.). This is the core scalar
     object that all subsequent FRW-facing layers reuse.

2. **F1 shape diagnostics + toy corridor**  
   - Code: `phase4/src/phase4/run_f1_shape_diagnostics.py`  
   - Outputs:
     - `phase4/outputs/tables/phase4_F1_shape_diagnostics.json`
     - `phase4/outputs/tables/phase4_F1_shape_mask.csv`  
   - Role: characterise the shape of \(E_{\mathrm{vac}}(\theta)\)
     and define a **toy, non-binding corridor** via a simple
     condition of the form
     \[
       E_{\mathrm{vac}}(\theta) \le E_{\mathrm{vac}}^{\min}
       + k_\sigma \sigma,
     \]
     recording the resulting fraction of the \(\theta\)-grid and
     its range. This is explicitly diagnostic and does *not*
     define a Phase 4 \(\theta\)-filter.

3. **FRW toy sanity check**  
   - Code: `phase4/src/phase4/run_f1_frw_toy_diagnostics.py`  
   - Outputs:
     - `phase4/outputs/tables/phase4_F1_frw_toy_diagnostics.json`
     - `phase4/outputs/tables/phase4_F1_frw_toy_mask.csv`  
   - Role: rescale \(E_{\mathrm{vac}}(\theta)\) into a toy
     \(\Omega_\Lambda(\theta)\), fix a simple FRW model with
     \(\Omega_m = 0.3\), \(\Omega_r = 0\), and \(H_0 =
     70\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\), and check that
     \(H^2(a; \theta)\) remains positive and not wildly varying
     over a **late-time scale-factor grid** \(a \in [0.5, 1]\).
     The outcome is a non-binding FRW-sanity mask and associated
     diagnostics.

4. **FRW viability scan**  
   - Code: `phase4/src/phase4/run_f1_frw_viability.py`  
   - Outputs:
     - `phase4/outputs/tables/phase4_F1_frw_viability_diagnostics.json`
     - `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`  
   - Role: promote the FRW toy into a more structured
     **viability** test by imposing:
     - positivity and smoothness of \(H^2(a; \theta)\),
     - existence of a matter-dominated era,
     - late-time acceleration,
     - a broad age window \(t_0 \in [10, 20]\,\mathrm{Gyr}\).  
     The mask file carries, per \(\theta\), \(E_{\mathrm{vac}}\),
     \(\Omega_\Lambda(\theta)\), age in Gyr, individual flags, and
     an overall `frw_viable` Boolean.

5. **FRW viability corridors**  
   - Code: `phase4/src/phase4/run_f1_frw_corridors.py`  
   - Outputs:
     - `phase4/outputs/tables/phase4_F1_frw_corridors.json`
     - `phase4/outputs/tables/phase4_F1_frw_corridors.csv`  
   - Role: given the FRW-viability mask, find contiguous
     \(\theta\)-intervals (“corridors”) where `frw_viable = 1` on
     the fixed grid. The diagnostics JSON records the number of
     corridors, their ranges, and summary quantities such as
     mean \(\Omega_\Lambda\) within each.

6. **FRW \(\Lambda\)CDM-like probe**  
   - Code: `phase4/src/phase4/run_f1_frw_lcdm_probe.py`  
   - Outputs:
     - `phase4/outputs/tables/phase4_F1_frw_lcdm_probe.json`
     - `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`  
   - Role: refine the FRW-viable subset by selecting those grid
     points for which
     \(\Omega_\Lambda(\theta) \approx 0.7 \pm 0.1\) and
     \(t_0 \approx 13.8 \pm 1.0\,\mathrm{Gyr}\), under the same
     toy FRW parameters. The mask augments the FRW-viability
     columns with a `lcdm_like` Boolean flag.

7. **Shape + FRW overlap probe**  
   - Code: `phase4/src/phase4/run_f1_frw_shape_probe.py`  
   - Outputs:
     - `phase4/outputs/tables/phase4_F1_frw_shape_probe.json`
     - `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv`  
   - Role: join the F1 shape mask, FRW-viability mask, and
     \(\Lambda\)CDM-like mask on the common grid to quantify:
     - how much of the F1 toy corridor is FRW viable,
     - how much of it is simultaneously FRW viable and
       \(\Lambda\)CDM-like.

8. **FRW data probe scaffold (optional)**  
   - Code: `phase4/src/phase4/run_f1_frw_data_probe.py`  
   - Outputs:
     - `phase4/outputs/tables/phase4_F1_frw_data_probe.json`
     - `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`  
   - Role: provide a single, explicit hook to compare FRW
     histories to an external binned distance–redshift dataset at
     `phase4/data/external/frw_distance_binned.csv`. In the
     current repository no such data file is bundled, so the
     diagnostics record `data_available = false` and set
     `data_ok = 0` for all grid points.

## 2. Numerical summary of the current baseline

The key numerical outcomes from the current runs (with
\(\Omega_m = 0.3\), \(\Omega_r = 0\), \(H_0 = 70\) and the late-time
scale-factor window) are:

- **F1 shape corridor (toy)**  
  - grid size: \(N_\theta = 2048\);
  - toy corridor fraction:
    \[
      \text{corridor\_fraction} \approx 0.5791;
    \]
  - toy corridor spans essentially the full \([0, 2\pi)\) grid.

- **FRW viability**  
  - FRW-viable fraction:
    \[
      \text{frac\_viable} \approx 0.4961;
    \]
  - FRW-viable \(\theta\)-range:
    \[
      \theta \in [0.4264,\, 3.5404]\ \text{(principal corridor)}.
    \]

- **\(\Lambda\)CDM-like subset (within FRW-viable)**  
  - \(\Lambda\)CDM-like fraction:
    \[
      \text{lcdm\_like\_fraction} \approx 0.0308;
    \]
  - selected \(\theta\)-range:
    \[
      \theta \in [0.5983,\, 3.3625];
    \]
  - selected \(\Omega_\Lambda(\theta)\)-range:
    \[
      \Omega_\Lambda \in [0.603,\, 0.798];
    \]
  - selected age range:
    \[
      t_0 \in [13.19,\, 13.77]\,\mathrm{Gyr}.
    \]

- **Shape–FRW overlaps (from the shape probe)**  
  - fraction in both F1 toy corridor and FRW-viable:
    \[
      \text{frac\_shape\_and\_viable} \approx 0.0752;
    \]
  - fraction in F1 toy corridor *and* \(\Lambda\)CDM-like:
    \[
      \text{frac\_shape\_and\_lcdm} \approx 0.0195.
    \]

In other words:

- The F1 toy corridor is broad in \(\theta\).  
- The FRW-viable subset is narrower but still a **contiguous**
  corridor covering roughly half of the grid.  
- Within that, a small but non-zero fraction is simultaneously
  FRW-viable and broadly \(\Lambda\)CDM-like in age and
  \(\Omega_\Lambda\).  
- The F1 shape corridor and the FRW-viable corridor intersect in a
  modest but non-negligible fraction of the grid.

All of these statements are versioned in the JSON/CSV outputs and can
be regenerated by re-running the corresponding scripts.

## 3. Interpretation at the current claim level

At the present Phase 4 scope, the FRW-facing infrastructure is
deliberately modest. The **only** formal claims it supports are:

1. Given the Phase 3 mechanism and the F1 mapping, we can construct a
   family of toy FRW histories parameterised by \(\theta\) and
   derived from a single scalar \(E_{\mathrm{vac}}(\theta)\).

2. For a specific, fixed choice of FRW background parameters
   \((\Omega_m, \Omega_r, H_0)\) and broad viability criteria
   (matter era, late acceleration, age window), a **non-zero,
   contiguous corridor** of \(\theta\) values yields FRW histories
   that are structurally viable in this toy sense.

3. Within that FRW-viable corridor, a small but non-zero fraction of
   grid points also yields \(\Omega_\Lambda \approx 0.7\) and
   \(t_0 \approx 13.8\,\mathrm{Gyr}\) to within broad tolerances,
   again with all definitions and thresholds spelled out in code and
   logs.

4. The overlaps between F1 shape-based toy corridors and FRW-based
   corridors are explicitly quantified and versioned, rather than
   hand-waved.

These are **structural** claims about the mapping and its FRW-facing
corridors, not evidence that the F1 mapping is realised in Nature.
There is no data fitting, no parameter estimation, and no model
selection at this stage.

## 4. Limitations and sources of arbitrariness

The main limitations of the current FRW-facing setup are:

- The FRW background parameters \(\Omega_m\), \(\Omega_r\), and
  \(H_0\) are fixed by hand, not inferred from data.

- The age and \(\Omega_\Lambda\) windows are broad, box-shaped cuts
  rather than likelihood contours from real datasets.

- The viability criteria (positivity and smoothness of \(H^2\),
  presence of a matter era, late-time acceleration) are necessary but
  far from sufficient as realistic cosmological tests.

- The FRW data probe exists only as a scaffold: no external dataset is
  bundled, and the current baseline records `data_available = false`.

- The F1 mapping itself remains a phenomenological choice at this
  stage; it is not derived from a fundamental field theory or
  variational principle.

These limitations are by design: Phase 4 is currently scoped as an
infrastructure and corridor-mapping phase, not as a full cosmological
analysis.

## 5. Possible directions for harder novelty

The FRW-facing machinery now in place suggests several natural
directions for more physically substantial work:

1. **From box cuts to likelihoods.**  
   Replace the broad age / \(\Omega_\Lambda\) windows with a simple
   \(\chi^2\) or likelihood construction based on a public
   distance–redshift dataset (e.g. SNe Ia or BAO), using the existing
   FRW data probe as the starting point.

2. **Systematic scans over background parameters.**  
   Instead of fixing \((\Omega_m, \Omega_r, H_0)\) once and for all,
   treat them as hyperparameters and study how the FRW-viable and
   \(\Lambda\)CDM-like fractions move as these are varied within
   observationally plausible ranges.

3. **Sharper structural questions about F1.**  
   Use the FRW viability and shape probes to ask whether the F1
   mapping exhibits any robust features (e.g. stable corridors,
   clustering, forbidden regions) that survive changes in resolution
   and FRW parameter choices.

4. **Bridging back to the axiom.**  
   Make explicit which aspects of the FRW-facing behaviour are truly
   inherited from the origin-axiom machinery (Phase 1–3), and which
   are artefacts of ad hoc choices in Phase 4. This would help
   identify which quantities, if any, might qualify as
   axiom-driven predictions rather than post-hoc tunings.

All of these directions can be pursued without breaking the current
Phase 0 claim discipline: each step can be added as a new rung with
explicit code, logs, and clearly scoped claims.

