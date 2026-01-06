# Phase 3 (Mechanism) — Progress Log

## 2026-01-06 — Rung 0: Mechanism contract + flavor-v1 archival

- Created `phase3/MECHANISM_CONTRACT.md` defining the role of Phase 3 (Mechanism),
  required artifacts, theta-filter schema, run-id layout, reproducibility levels,
  and claims / non-claims, in a way that is compatible with the Phase 0 contract.
- Archived the previous flavor-sector exploratory Phase 3 under
  `experiments/phase3_flavor_v1/`, including its paper, claims, code, and gate scripts,
  so its negative result remains fully reproducible but no longer part of the
  canonical corridor.
- Removed the old Phase 3 theta filter from `phase0/phase_outputs/`, so the Phase 0
  corridor now aggregates only Phases 0–2 until a new mechanism-based
  `phase_03_theta_filter.json` is implemented.

## 2026-01-06 — Rung 1: Phase 3 mechanism skeleton + gate

- Created a fresh Phase 3 mechanism namespace under `phase3/` (paper,
  src, outputs, artifacts, workflow) distinct from the archived
  `experiments/phase3_flavor_v1/` flavor-calibration experiment.
- Added a Rung-1 skeleton paper (`phase3/paper/main.tex`) with
  introduction, mechanism-design placeholder, baseline-experiments
  placeholder, limitations, and reproducibility appendices, aligned
  with the Phase 0 contract and Phase 3 mechanism contract.
- Implemented a minimal Snakemake workflow in
  `phase3/workflow/Snakefile` that builds the Phase 3 paper and exports
  the canonical artifact `phase3/artifacts/origin-axiom-phase3.pdf`.
- Added `scripts/phase3_gate.sh` so that `bash scripts/phase3_gate.sh
  --level A|B` from repo root regenerates the Phase 3 artifact in a
  clean repository.
- No physical mechanism, numerical experiments, or theta-filter
  artifacts are defined at this rung; the skeleton only prepares the
  structure for later rungs.

## 2026-01-06 — Rung 2: toy vacuum mechanism + unconstrained amplitude

- Implemented a toy vacuum mechanism in `phase3/src/phase3_mech/vacuum_model.py`
  with a deterministic ensemble of complex modes and a global amplitude
  observable \(A_0(\theta)\).
- Exposed `VacuumConfig`, `make_vacuum_config`, `amplitude_unconstrained`,
  and `scan_amplitude_unconstrained` via `phase3/src/phase3_mech/__init__.py`
  so that future rungs and scripts can reuse the same baseline configuration.
- Rewrote `phase3/paper/sections/02_mechanism_design.tex` to describe the toy
  vacuum ensemble, define \(A_0(\theta)\), and clarify the structural role
  of the phase parameter \(\theta\) without yet enforcing the non-cancellation
  floor.
- No floor-enforced amplitude, binding certificate, or theta-filter artifact
  is defined at this rung; those are deferred to later rungs in accordance
  with the Phase 0 contract.

## 2026-01-06 — Rung 3: non-cancellation floor + binding diagnostics (definition level)

- Extended `phase3/src/phase3_mech/vacuum_model.py` with a floor-enforced
  amplitude \(A(\theta) = \max(A_0(\theta), \epsfloor)\) and a grid scanner
  `scan_amplitude_with_floor` that returns both unconstrained and
  floor-enforced amplitudes, plus a boolean mask where the floor is active.
- Exposed `amplitude_with_floor` and `scan_amplitude_with_floor` via
  `phase3/src/phase3_mech/__init__.py` so that future rungs and scripts
  can reuse the same mechanism.
- Rewrote `phase3/paper/sections/02_mechanism_design.tex` to describe the
  toy vacuum ensemble, the unconstrained observable \(A_0(\theta)\), the
  floor-enforced amplitude \(A(\theta)\), and the binding diagnostics
  needed for a Phase 0–style binding certificate.
- No specific choice of \(\epsfloor\), no numerical binding certificate,
  and no \(\theta\)-filter artifact are fixed at this rung; those are
  deferred to later rungs in accordance with the Phase 3 mechanism contract.

## 2026-01-06 - Rung 4: baseline binding experiment

- Added `phase3/src/phase3_mech/run_baseline_scan.py` to construct the
  baseline vacuum configuration, scan the unconstrained amplitude
  \(A_0(\theta)\), choose \(\epsfloor\) as the 25th percentile of the
  sampled \(A_0(\theta)\) values, and rescan with the non-cancellation
  floor enforced.
- Wrote per-grid results to
  `phase3/outputs/tables/mech_baseline_scan.csv` and summary diagnostics
  (including \(\epsfloor\), \(\min A_0\), \(\max A_0\), binding fraction,
  and quantiles) to
  `phase3/outputs/tables/mech_baseline_scan_diagnostics.json`.
- Rewrote `phase3/paper/sections/03_results_stub.tex` as a baseline
  binding experiment section that documents the scan procedure, the
  quantile-based floor selection, and the diagnostic quantities used to
  certify a genuine binding regime.
- No \(\theta\)-filter artifact or contact with external observables is
  introduced at this rung; the goal is to demonstrate that the toy
  vacuum admits a non-trivial binding regime suitable for later
  certificates and corridor work.

## 2026-01-06 - Rung 5: binding certificate diagnostics

- Added `phase3/src/phase3_mech/run_binding_certificate.py`, which reuses
  the baseline toy vacuum configuration and the quantile-based floor
  from the baseline scan to compare \(A_0(\theta)\) and the
  floor-enforced amplitude \(A(\theta)\).
- Wrote per-grid binding-certificate data to
  `phase3/outputs/tables/mech_binding_certificate.csv` and summary
  diagnostics (mean shift, \(L^2\) distance, binding fraction, and basic
  moments) to
  `phase3/outputs/tables/mech_binding_certificate_diagnostics.json`.
- Rewrote `phase3/paper/sections/03_results_stub.tex` to describe both
  the baseline binding experiment and the binding-certificate
  diagnostics, showing that the non-cancellation floor has a
  quantitatively non-trivial effect on the observable while remaining
  in a genuine binding regime.
- No \(\theta\)-filter artifact or external observables are introduced
  at this rung; the focus is on establishing a Phase~0-style binding
  regime for the toy vacuum mechanism.

## 2026-01-06 - Rung 6: mechanism-focused introduction and limitations

- Rewrote `phase3/paper/sections/01_introduction.tex` to give Phase 3 a
  mechanism-focused introduction that explains the role of the toy vacuum,
  the global amplitude \(A_0(\theta)\), the floor-enforced amplitude
  \(A(\theta)\), and the binding-regime diagnostics, while clarifying the
  relationship to the archived flavor experiment.
- Rewrote `phase3/paper/sections/04_limitations_stub.tex` as a structured
  ``Limitations and outlook'' section, explicitly stating the toy nature of
  the vacuum ensemble, the single-parameter structure, the lack of a
  selection mechanism for \(\theta\) and \(\epsfloor\), and the absence of
  direct empirical contact at this phase.
- No changes to the numerical mechanism, baseline scan, or
  binding-certificate diagnostics; this rung improves the scientific
  narrative around the existing Phase 3 mechanism while keeping the gate
  workflow and artifacts unchanged.

## 2026-01-06 - Rung 7: binding profile figure and results consolidation

- Added `phase3/src/phase3_mech/make_mech_figures.py` to generate a
  baseline binding-profile figure showing \(A_0(\theta)\), the
  floor-enforced amplitude \(A(\theta)\), and the floor level
  \(\epsfloor\), writing the PDF to
  `phase3/outputs/figures/fig1_mech_binding_profile.pdf`.
- Rewrote `phase3/paper/sections/03_results_stub.tex` as a structured
  Results section covering the baseline scan, quantile-based floor
  selection, binding-certificate scan, and the binding-profile
  figure and diagnostics.
- No changes to the underlying toy vacuum mechanism, baseline scan
  parameters, or binding-certificate diagnostics; this rung improves
  the presentation and adds a visual diagnostic while keeping the
  Phase 3 gate workflow unchanged.

## 2026-01-06 - Rung 8: discussion and limitations for the Phase 3 mechanism

- Replaced the stub `phase3/paper/sections/04_limitations_stub.tex` with
  a structured Discussion and Limitations section that:
  - clarifies the toy nature of the vacuum ensemble and global
    amplitude observable \(A_0(\theta)\);
  - explains the design-choice status of the \(\theta\) grid and
    quantile-based floor \(\epsfloor\); and
  - situates the current mechanism-only rung with respect to the
    Phase~0 contract, explicitly noting that no \(\theta\)-filter
    artifact or external data contact is claimed at this stage.
- Left the toy mechanism, baseline scan, binding-certificate
  diagnostics, and gate workflow unchanged; this rung is editorial,
  improving the scientific narrative without altering any numerical
  results or code paths.
