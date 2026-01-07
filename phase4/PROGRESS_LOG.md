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
