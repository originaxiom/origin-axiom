# Phase 3 Ansatz Contract — θ Fit (Lock Document)

## Purpose
Phase 3 requires a **single-parameter fit** for a phase θ extracted from CKM+PMNS targets **within a declared ansatz class**.
This file locks the fit semantics so we cannot silently drift.

This is explicitly:
- **Fit layer** (empirical constraint within an ansatz),
not a derivation from the axiom.

## Contract objects
1. **Targets file (machine-readable):** `phase3/fit/targets.yaml`
2. **Fit runner (deterministic):** `phase3/src/phase3/fit/run_fit.py`
3. **Artifacts used in paper bundle:**
   - `phase3/outputs/tables/theta_fit_summary.csv`
   - `phase3/outputs/tables/theta_fit_summary.meta.json`
   - `phase3/outputs/tables/theta_fit_diagnostics.json`
   - `phase3/outputs/figures/fig1_theta_fit_diagnostics.pdf`

## Drift rule (non-negotiable)
Any change to:
- the ansatz mapping θ → observables,
- the list of observables included in χ²,
- the target values/σ used,
- the θ-domain or grid strategy,
must be accompanied by:
1) bump `ansatz.version` in `targets.yaml`,
2) update `phase3/CLAIMS_TABLE.md`,
3) add an entry to `phase3/PROGRESS_LOG.md`,
4) if it changes scope meaningfully, add `phase3/SCOPE_ADDENDUM_XX.md`.

## Definitions (what exactly is being fit)
- Observables are defined as entries in `targets.yaml` under `observables:`.
- Each observable has:
  - `key`: unique string identifier used by code
  - `target`: numeric target value
  - `sigma`: uncertainty (must be >0)
  - `weight`: optional multiplicative weight (default 1.0)

The χ² objective is:

  χ²(θ) = Σ_i  weight_i * ((pred_i(θ) - target_i)/sigma_i)^2

where `pred_i(θ)` is the ansatz prediction for that observable.

## θ scan domain + interval reporting
- θ domain: [0, 2π]
- Grid scan: fixed N points (declared in `targets.yaml`)
- Best-fit θ = argmin χ²(θ)
- 68% interval:
  - For 1 fitted parameter, use Δχ² = 1.0 (convention)
  - interval defined as the contiguous set of θ where χ² ≤ χ²_min + 1.0
  - if multiple disjoint intervals exist, report the full min-to-max envelope and note in diagnostics

## Placeholder mode (bootstrap only)
Until targets+ansatz are replaced with the real CKM+PMNS mapping,
we allow placeholder observables (e.g. `ckm_proxy`, `pmns_proxy`) **only if**
`targets.yaml: meta.placeholder_mode: true`.

When you flip `placeholder_mode: false`, the runner will hard-fail if any placeholder keys remain.

## Success criteria (Phase 3 fit claim readiness)
Phase 3 C3.1 (“θ fit reproducible within ansatz”) is ready when:
- `placeholder_mode` is false,
- targets cite the chosen sources (e.g., PDG/NuFit) or an internal frozen data file,
- the ansatz mapping is explicitly documented (either in code docstring + paper section),
- the fit reproduces the same θ and diagnostics from a clean clone using Level B gate.
