# Phase 4 Overview — Diagnostic FRW-Facing Stub

**Status (2026-01-07):**  
Phase 4 currently hosts a *diagnostic stub* that takes the Phase 3 vacuum
mechanism and pushes it into a structured, FRW-facing setting. It is **not**
yet a corridor-building or data-calibrated phase; the focus is on wiring,
sanity, and honest logging of both positive and negative toy results.

---

## 1. What Phase 4 currently does

Phase 4 reuses the Phase 3 baseline-vacuum mechanism and diagnostics to define
a simple scalar \(E_{\mathrm{vac}}(	heta)\) and then builds three diagnostic
layers on top of it:

1. **F1 mapping family (vacuum scalar)**  
   - Implemented in `phase4/src/phase4/mappings_f1.py`.
   - Reads the Phase 3 baseline diagnostics from  
     `phase3/outputs/tables/mech_baseline_scan_diagnostics.json`.
   - Uses the quantile-based floor \(arepsilon_{\mathrm{floor}}\) to define a
     strictly positive amplitude \(A(	heta)\) and a toy scalar
     \(E_{\mathrm{vac}}(	heta) = lpha A(	heta)^eta\) on a uniform
     grid \(	heta \in [0, 2\pi)\).
   - The primary goal is *numerical sanity* and *structural continuity* with
     Phase 3, not physical calibration.

2. **F1 shape diagnostics and toy corridor**  
   - Implemented in `phase4/src/phase4/run_f1_shape_diagnostics.py`.
   - Consumes the F1 sanity curve and constructs descriptive statistics for
     \(E_{\mathrm{vac}}(	heta)\) (min / max / mean / std / support).
   - Defines a **toy-level corridor** via a simple inequality in
     \(E_{\mathrm{vac}}(	heta)\) and records:
     - a JSON summary  
       `phase4/outputs/tables/phase4_F1_shape_diagnostics.json`, and
     - a per-\(	heta\) mask  
       `phase4/outputs/tables/phase4_F1_shape_mask.csv`.
   - This corridor is **explicitly non-binding**: it is a shape probe, not a
     physical \(	heta\)-filter and not a candidate \(	heta_\star\).

3. **FRW-inspired toy diagnostics**  
   - Implemented in `phase4/src/phase4/run_f1_frw_toy_diagnostics.py`.
   - Rescales \(E_{\mathrm{vac}}(	heta)\) into a proxy
     \(\Omega_\Lambda(	heta)\), picks toy values for \(\Omega_m\) and
     \(\Omega_r\), and evaluates
     \[
       H^2(a; 	heta) = \Omega_r a^{-4} + \Omega_m a^{-3} + \Omega_\Lambda(	heta)
     \]
     on a **late-time scale-factor grid** \(a \in [0.5, 1]\).
   - For each \(	heta\), checks:
     - positivity of \(H^2(a; 	heta)\) on the grid, and
     - a bound on the variation ratio \(\max H^2 / \min H^2\).
   - Produces:
     - a JSON diagnostics file  
       `phase4/outputs/tables/phase4_F1_frw_toy_diagnostics.json`, and
     - a per-\(	heta\) FRW-sanity mask  
       `phase4/outputs/tables/phase4_F1_frw_toy_mask.csv`.
   - The FRW toy is a **structured sanity probe only**. It does *not* define a
     FRW model, does *not* select a preferred \(	heta_\star\), and remains
     strictly non-binding.

The design motivation and the evolution of the FRW toy (including the initial
empty-mask outcome and the later late-time tweak) are documented in  
`phase4/design/FRW_TOY_DESIGN.md`.

---

## 2. Paper and artifact

The Phase 4 paper lives in:

- `phase4/paper/main.tex` with sections under `phase4/paper/sections/`,
- appendices in `phase4/paper/appendix/`, and
- bibliography `phase4/paper/Reference.bib`.

The canonical Phase 4 artifact is:

- `phase4/artifacts/origin-axiom-phase4.pdf`

built via the Snakemake workflow.

Key claims and scope for Phase 4 are summarised in:

- `phase4/paper/sections/01_introduction.tex`
- `phase4/paper/sections/02_mappings_stub.tex`
- `phase4/paper/sections/03_diagnostics_stub.tex`
- `phase4/paper/sections/04_limitations_stub.tex`
- `phase4/paper/appendix/A_claims_table.tex`

The limitations section explicitly states that Phase 4 currently:

- introduces **one** toy mapping family (F1),
- relies on grid-based diagnostics tied to a specific Phase 3 baseline,
- makes **no** claim about a physically justified \(	heta\)-corridor or
  \(	heta_\star\), and
- treats all corridor-like and FRW-like constructs as **diagnostics**, not
  physical predictions.

---

## 3. How to rebuild Phase 4 locally

From the repo root, the convenience helper:

```bash
oa && bash scripts/phase4_gate.sh --level A
```

will:

- rebuild the Phase 4 paper (`phase4/outputs/paper/phase4_paper.pdf`),
- copy the artifact to `phase4/artifacts/origin-axiom-phase4.pdf`, and
- ensure the minimal diagnostics are up to date.

The individual diagnostic scripts can be run as:

```bash
# 1. F1 sanity curve
oa && python phase4/src/phase4/run_f1_sanity.py

# 2. F1 shape diagnostics and toy corridor
oa && python phase4/src/phase4/run_f1_shape_diagnostics.py

# 3. FRW-inspired toy diagnostics
oa && python phase4/src/phase4/run_f1_frw_toy_diagnostics.py
```

Each script logs its outputs and summary statistics to stdout and writes the
corresponding JSON/CSV files under `phase4/outputs/tables/`.

---

## 4. Scope and non-claims

To keep Phase 4 aligned with the Phase 0 philosophy (honest, auditable, and
non-overreaching), the current Phase 4 implementation **does not**:

- claim a unique or physically preferred \(	heta_\star\),
- claim that F1 is the correct or final mapping family,
- present a calibrated FRW cosmology, or
- use any diagnostic (shape corridor or FRW toy) as a hard \(	heta\)-filter.

Instead, Phase 4 at this stage should be read as:

> a diagnostic bridge between the Phase 3 vacuum mechanism and simple
> FRW-inspired sanity checks, designed to test wiring, logging, and
> corridor-handling logic in a controlled setting.

Any future step that proposes:

- a physically motivated corridor,
- a candidate \(	heta_\star\), or
- a data-calibrated cosmological model

must be added as a **new rung** or **new mapping family** with its own clearly
scoped assumptions, diagnostics, and claims table entries.

### FRW ΛCDM-like probe on F1

Building on the FRW viability mask, we add a deliberately broad
"ΛCDM-like" diagnostic layer. The script
`phase4/src/phase4/run_f1_frw_lcdm_probe.py`:

- reads the FRW viability mask
  `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`;
- restricts to FRW-viable grid points; and
- marks as `lcdm_like` those points for which
  - the toy vacuum fraction \(\Omega_\Lambda(\theta)\) lies within a
    tolerance window around a target \(\Omega_\Lambda^{\mathrm{target}}
    \approx 0.7\), and
  - the toy FRW age \(t_0(\theta)\) lies within a tolerance window
    around \(13.8\,\mathrm{Gyr}\),

using the same FRW toy parameters as the viability rung
(\(\Omega_m = 0.3\), \(\Omega_r = 0\), \(H_0 = 70\,\mathrm{km\,s^{-1}\,\mathrm{Mpc}^{-1}}\)).

The code writes:

- `phase4/outputs/tables/phase4_F1_frw_lcdm_probe.json`, a diagnostic
  summary recording the ΛCDM-like fraction, the θ-extent of the
  selected subset, and the corresponding Ω\(_\Lambda\) and age ranges;
- `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`, a
  per-grid CSV with an added `lcdm_like` Boolean flag.

In the current baseline configuration this selects a small but
non-zero fraction of the θ-grid. This layer is still explicitly
non-binding: it is used as an illustrative, FRW-facing probe of the F1
mapping rather than a data-driven constraint or a mechanism for
picking a unique \(\theta_\star\).

### Rung 12 – F1/FRW shape probe

- Implemented `phase4/src/phase4/run_f1_frw_shape_probe.py`, which joins:
  - the toy F1 shape mask (`phase4_F1_shape_mask.csv`),
  - the FRW-viability mask (`phase4_F1_frw_viability_mask.csv`), and
  - the \(\Lambda\)CDM-like probe mask (`phase4_F1_frw_lcdm_probe_mask.csv`)
  on the common \(\theta\)-grid.
- Wrote a joined per-\(\theta\) mask
  `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv` with Boolean
  flags for `in_toy_corridor`, `frw_viable`, `lcdm_like`, and the
  intersections `shape_and_viable`, `shape_and_lcdm`.
- Recorded summary diagnostics in
  `phase4/outputs/tables/phase4_F1_frw_shape_probe.json`. In the current
  baseline run (2048-point grid) roughly 58\% of points lie in the toy F1
  shape corridor, about 50\% are FRW-viable, and a few percent are both
  FRW-viable and \(\Lambda\)CDM-like; the intersection with the toy
  corridor is explicitly logged but not promoted to a \(\theta\)-filter.

## Rung 12: FRW data-probe scaffolding

- Implemented `phase4/src/phase4/run_f1_frw_data_probe.py`, which builds on the
  FRW viability mask and optionally compares model distance moduli to a
  binned distance–redshift dataset located at
  `phase4/data/external/frw_distance_binned.csv` (not bundled).
- In the current repository state no external data file is present, so the rung
  reports `data_available = false`, `n_data_points = 0`, and sets `data_ok = 0`
  for all FRW-viable grid points. This keeps Phase 4 fully reproducible while
  exposing a single, explicit hook for future data work.
- The data probe is explicitly non-binding and does not introduce a new
  `theta`-filter; it is a structured, optional diagnostic in the spirit of
  Phase 0.

---

## Companion docs: Phase 4 contract and design bundle

For readers who arrive here first and want to see the full Phase 4 contract and
design surface, the following documents are relevant:

- `SCOPE.md` — Phase 4 scope definition (draft, non-binding at this stage).
- `CLAIMS.md` and `NON_CLAIMS.md` — draft Phase 4 claims and guardrails.
- `REPRODUCIBILITY.md` — draft reproducibility plan and gate criteria.
- `CLAIMS_TABLE.md` — draft claims→artifacts map for Phase 4.
- `PHASE3_INTERFACE.md` — design note for the Phase 3↔Phase 4 interface (how
  the mechanism module feeds FRW-facing diagnostics).
- `MAPPING_FAMILIES.md` — design note describing candidate mapping families
  from Phase 3 amplitudes into FRW-like quantities.

These Phase 4-local documents are complemented by the FRW design and promotion
docs:

- `FRW_TOY_DESIGN.md`, `FRW_DATA_DESIGN.md`, and `FRW_SYNTHESIS.md` for the
  FRW toy background, data-probe layer, and synthesis.
- `docs/FRW_CORRIDOR_PROMOTION_GATE_v1.md` and
  `phase4/docs/PHASE4_FRW_PROMOTION_DESIGN_v1.md` for the promotion gate and
  design-level plan governing how Stage 2 FRW/mech/joint/data diagnostics may
  eventually feed into Phase 4/5 text.

All of these are subject to the Phase 0 contracts and the Stage 2 promotion
design; until the relevant gates are passed and claims are locked, they should
be read as internal Phase 4 contract and design material, not as binding
predictions.
