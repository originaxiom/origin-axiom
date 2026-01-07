# Phase 4 – PROGRESS LOG

This log records significant steps in the development of Phase 4.
Timestamps are approximate and refer to local time for the primary
developer.

---

## 2026-01-07 – Rung 0: Phase 4 contract skeleton (draft)

- Created `phase4/SCOPE.md` describing the draft mission of Phase 4:
  vacuum→FRW consistency and scale sanity tests using the Phase 3
  mechanism vacuum as the canonical anchor.
- Added draft `phase4/CLAIMS.md`, `phase4/CLAIMS_TABLE.md`,
  `phase4/NON_CLAIMS.md`, and `phase4/REPRODUCIBILITY.md`, all explicitly
  marked as **DRAFT / non-binding**.
- Established that Phase 4 must either:
  - produce at least one explicit, structurally reasonable mapping from
    \(A(\theta)\) (or a residue) to FRW/vacuum-energy-like observables
    with a non-empty corridor; **or**
  - record a structured negative result that this particular
    implementation of the Phase 3 global-amplitude mechanism fails the
    tested FRW consistency checks.
- No code, workflow, or θ-filter artifacts are introduced at this rung;
  the focus is on articulating a narrow, honest design contract for
  Phase 4 consistent with the Phase 0 architecture and the canonical
  θ/A definitions.

## 2026-01-07 – Rung 1: Phase 4 skeleton paper and gate

- Created Phase 4 directory structure (`paper/`, `outputs/`, `artifacts/`,
  `src/`, `workflow/`) mirroring earlier phases.
- Added a minimal Phase 4 LaTeX paper skeleton (`phase4/paper/main.tex`)
  with introduction, mappings placeholder, diagnostics placeholder,
  limitations, and draft appendices for claims and reproducibility.
- Implemented a Snakemake workflow in `phase4/workflow/Snakefile` that
  builds the Phase 4 paper and exports the canonical artifact
  `phase4/artifacts/origin-axiom-phase4.pdf`.
- Added `scripts/phase4_gate.sh` so `bash scripts/phase4_gate.sh --level A`
  from the repo root regenerates the Phase 4 artifact in a clean repository.
- No mappings, diagnostics, or \theta-filters are defined at this rung;
  this step only prepares the structural scaffolding for later, more
  physically meaningful Phase 4 work.

## 2026-01-07 - Rung 2: mapping families design note

- Added `phase4/MAPPING_FAMILIES.md` as a draft, non-binding design
  note describing candidate mapping families (F1: amplitude-to-density,
  F2: residue-relative, F3: normalised amplitude corridors) for
  Phase 4.
- Rewrote `phase4/paper/sections/02_mappings_stub.tex` to summarise
  these mapping families in the paper, emphasising explicitness,
  corridor compatibility, and honest physical status.
- No concrete mapping code, FRW modules, or \(\theta\)-filters are
  implemented at this rung; the goal is to lock in a narrow design
  space for later Phase 4 rungs consistent with the Phase 0 contract
  and the Phase 3 mechanism interfaces.

## 2026-01-07 - Rung 3: F1 mapping + vacuum-curve sanity check

- Implemented the F1 mapping family in `phase4/src/phase4/mappings_f1.py`,
  which reuses the Phase 3 vacuum mechanism and quantile-based floor
  to define a toy vacuum-energy-like scalar
  \(E_{\mathrm{vac}}(\theta) = \alpha A(\theta)^{\beta}\).
- Added `phase4/src/phase4/run_f1_sanity.py` to compute a baseline
  \(E_{\mathrm{vac}}(\theta)\) curve using the Phase 3 baseline
  diagnostics from
  `phase3/outputs/tables/mech_baseline_scan_diagnostics.json`.
- Wrote the per-theta sanity curve to
  `phase4/outputs/tables/phase4_F1_sanity_curve.csv` and inspected the
  summary statistics (strictly positive, small \(E_{\mathrm{vac}}\),
  consistent with the floor-enforced amplitude scale).
- No \(\theta\)-corridor or \(\theta\)-filter is defined at this rung;
  the goal is only to verify that the F1 mapping is numerically sane
  and cleanly wired into the Phase 3 mechanism outputs.

## 2026-01-07 – Rung 4: F1 shape diagnostics and toy corridor

- Added `phase4/src/phase4/run_f1_shape_diagnostics.py`, which rebuilds
  the F1 vacuum-energy-like curve \(E_{\mathrm{vac}}(\theta)\) from the
  Phase~3 baseline and computes basic shape descriptors (global min/max,
  mean, standard deviation).
- Defined a \emph{toy, non-binding} \(\theta\)-corridor as the set of
  grid points satisfying
  \(E_{\mathrm{vac}}(\theta) \le E_{\mathrm{vac},\min} + \sigma_{E}\),
  writing summary diagnostics to
  `phase4/outputs/tables/phase4_F1_shape_diagnostics.json` and a
  per-theta mask to
  `phase4/outputs/tables/phase4_F1_shape_mask.csv`.
- Rewrote `phase4/paper/sections/03_diagnostics_stub.tex` to document
  these diagnostics explicitly, emphasising that they are exploratory
  and non-binding: they do not define a canonical \(\theta_\star\) and
  serve only as a structured starting point for later, more physically
  motivated corridor work.

## 2026-01-07 - Rung 5: FRW toy diagnostics design note

- Added `phase4/FRW_TOY_DESIGN.md` as a draft, non-binding design note
  for a minimal FRW-inspired toy module driven by the F1 scalar
  \(E_{\mathrm{vac}}(\theta)\).
- Rewrote `phase4/paper/sections/03_diagnostics_stub.tex` to
  summarise the F1 vacuum-curve sanity check, the F1 shape
  diagnostics and toy corridor, and to reference the FRW toy design
  note as future, explicitly non-claiming work.
- No FRW-like code or \(\theta\)-filters are introduced at this rung;
  the focus is on tightening the diagnostic story and constraining
  later Phase 4 work to auditable, modest FRW-like sanity tests.

## 2026-01-07 - Rung 6: Phase 3–4 interface and reproducibility update

- Added `phase4/PHASE3_INTERFACE.md` to document the dependency of
  Phase 4 on the Phase 3 vacuum mechanism, baseline scan, and
  binding-certificate artifacts, and to spell out the current pipeline
  from Phase 3 amplitudes to F1 diagnostics and toy corridors.
- Updated `phase4/paper/appendix/B_reproducibility.tex` so that it
  reflects the implemented F1 mapping, diagnostics, and the Phase 3
  prerequisites, and provides explicit commands for rebuilding the
  Phase 4 paper and associated CSV/JSON artifacts.
- No new mapping families, FRW-like modules, or \(\theta\)-filters are
  introduced at this rung; the focus is strictly on tightening the
  upstream/downstream contract and the reproducibility story for the
  existing Phase 4 work.
