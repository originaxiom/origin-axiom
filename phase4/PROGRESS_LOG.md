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

## 2026-01-07 - Rung 7: FRW-inspired toy diagnostics on F1

- Added `phase4/src/phase4/run_f1_frw_toy_diagnostics.py`, which reads
  the F1 sanity curve `phase4_F1_sanity_curve.csv`, rescales
  \(E_{\mathrm{vac}}(\theta)\) into a toy \(\Omega_\Lambda(\theta)\),
  evaluates a simple FRW-like quantity
  \(H^2(a; \theta) = \Omega_r a^{-4} + \Omega_m a^{-3} +
  \Omega_\Lambda(\theta)\) on a fixed scale-factor grid, and constructs
  a Boolean per-\(\theta\) "FRW-sane" mask.
- Wrote the resulting diagnostics and mask to
  `phase4/outputs/tables/phase4_F1_frw_toy_diagnostics.json` and
  `phase4/outputs/tables/phase4_F1_frw_toy_mask.csv`, respectively.
- Rewrote `phase4/paper/sections/03_diagnostics_stub.tex` to document
  the three diagnostic layers now in place: F1 sanity curve, F1 shape
  diagnostics with a toy corridor, and the FRW-inspired toy
  diagnostics, all explicitly marked as non-binding.
- No \(\theta\)-filter or physically calibrated FRW model is introduced
  at this rung; the FRW-inspired module is used strictly as a
  structural sanity probe for the F1 mapping.

## 2026-01-07 - Rung 8: FRW toy baseline outcome and documentation

- Inspected the FRW-inspired toy diagnostics output, noting that with
  the current toy parameters and variation bound the FRW-sanity mask
  is empty (`frac_sane ≈ 0`).
- Updated `phase4/paper/sections/03_diagnostics_stub.tex` so the Phase 4
  paper explicitly records this baseline outcome as a toy-level
  negative result, emphasising that it is non-binding and does not
  define a θ-filter.
- Appended a "Baseline Rung-7 outcome" section to
  `phase4/FRW_TOY_DESIGN.md` to document the current FRW toy behaviour
  and to frame it as a local test of the F1 mapping and normalisation,
  not a global verdict on Phase 4.
- No changes were made to the mapping implementation or sanity
  criteria at this rung; the focus is on honest reporting and
  alignment with the Phase 0 philosophy about structured negative
  results.

## 2026-01-07 - Rung 9: FRW toy late-time tweak

- Rewrote `phase4/src/phase4/run_f1_frw_toy_diagnostics.py` to use a
  late-time scale-factor window a ∈ [0.5, 1] instead of [0.1, 1],
  keeping the same basic FRW sanity structure (positivity of H^2 and a
  bound on max(H^2)/min(H^2) per θ).
- Updated `phase4/paper/sections/03_diagnostics_stub.tex` so the Phase 4
  paper reflects the late-time FRW toy configuration without hard-coding
  any particular value of the FRW-sanity fraction.
- Appended a design note to `phase4/FRW_TOY_DESIGN.md` documenting this
  late-time tweak as a non-binding change motivated by the earlier
  empty-mask outcome.
- Re-ran the Phase 4 gate to regenerate the artifact and refreshed the
  diagnostics files for the FRW toy. The resulting `frac_sane` remains a
  logged diagnostic only and is not promoted to a θ-filter.

## 2026-01-07 - Rung 10: Limitations and scope section

- Replaced `phase4/paper/sections/04_limitations_stub.tex` with a structured
  limitations/scope section for the Phase 4 artifact.
- Made explicit that the current Phase 4 content is:
  - structurally focused (wiring Phase 3 amplitudes into scalar diagnostics),
  - based on a single toy mapping family (F1) and simple thresholds, and
  - not calibrated to observational data or a concrete field-theoretic model.
- Clarified the status of \(\theta\)-corridors and \(\theta_\star\): the F1
  corridor is a diagnostic shape summary only, not a physically justified
  corridor and not used to select a preferred \(\theta_\star\).
- Recorded the FRW-inspired module as a toy sanity device that:
  - treats \(E_{\mathrm{vac}}(\theta)\) as a proxy for \(\Omega_\Lambda(\theta)\),
  - checks simple positivity and bounded-variation conditions for \(H^2(a;\theta)\),
  - and does not perform parameter inference or cosmological fitting.
- Stated the numerical limitations (finite \(\theta\)- and \(a\)-grids, single
  baseline configuration) and positioned Phase 4 as one concrete, reproducible
  instance of the mapping/diagnostic workflow rather than a survey of design
  space.
- Emphasised that any future tightening of the corridor notion, introduction of
  a candidate \(\theta_\star\), or calibration to data must live in rungs beyond
  the present Phase 4 artifact and carry their own explicit assumptions.

## 2026-01-07 - Rung 10: FRW viability corridor on F1

- Implemented and ran `phase4/src/phase4/run_f1_frw_viability.py`, which
  reads the F1 sanity curve, rescales it into a toy \(\Omega_\Lambda(\theta)\),
  and evaluates a minimal FRW viability diagnostic on each grid point.
- The viability mask requires (i) a coarse age window
  \(t_0 \in [10, 20]~\mathrm{Gyr}\) for a background with
  \(\Omega_m = 0.3\), \(\Omega_r = 0\), \(H_0 = 70~\mathrm{km\,s^{-1}\,Mpc^{-1}}\),
  (ii) a matter-dominated era, (iii) a late-time accelerating regime,
  and (iv) bounded variation of \(H^2(a; \theta)\) over a fixed
  late-time scale-factor grid.
- Wrote the resulting diagnostics to
  `phase4/outputs/tables/phase4_F1_frw_viability_diagnostics.json` and
  the per-theta viability mask to
  `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`. For the
  current baseline parameters, roughly half of the F1 grid passes all
  checks (non-zero `frac_viable`).
- Updated `phase4/paper/sections/03_diagnostics_stub.tex` and
  `phase4/FRW_TOY_DESIGN.md` so that the Phase 4 paper and design note
  record this FRW-inspired viability corridor as a toy, physics-facing
  constraint, without yet promoting it to the final \(\theta\)-filter.

## 2026-01-07 – Rung 10: FRW viability scan and corridor extraction

- Implemented `phase4/src/phase4/run_f1_frw_viability.py`, which maps
  the F1 vacuum curve into a toy FRW background with
  \(\Omega_m = 0.3\), \(\Omega_r = 0\),
  \(\langle \Omega_\Lambda \rangle \approx 0.7\), and
  \(H_0 = 70\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\). For each theta-grid
  point it computes a cosmic age \(t_0(\theta)\) in Gyr, checks for a
  matter era, late-time acceleration, and smooth positive \(H^2(a)\),
  and applies a broad age window \(10\text{–}20\) Gyr.
- Wrote the resulting diagnostics and per-theta viability mask to
  `phase4/outputs/tables/phase4_F1_frw_viability_diagnostics.json`
  and `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`.
- Added `phase4/src/phase4/run_f1_frw_corridors.py` to compress the
  FRW viability mask into contiguous theta-corridors, producing
  `phase4/outputs/tables/phase4_F1_frw_corridors.json` and
  `phase4/outputs/tables/phase4_F1_frw_corridors.csv` and highlighting
  a principal corridor (largest number of viable grid points).
- Updated `phase4/paper/sections/03_diagnostics_stub.tex` and
  `phase4/FRW_TOY_DESIGN.md` so the Phase 4 paper and design note
  describe the FRW viability and corridor layers explicitly, with all
  FRW-facing modules clearly marked as toy-level and non-binding.
- Re-ran the Phase 4 gate to regenerate the canonical artifact. The
  FRW viability and corridor results are treated as structured
  diagnostics of the F1 mapping and not as a claim of a physically
  calibrated theta-filter.

## 2026-01-07 – FRW ΛCDM-like probe on F1

- Implemented `phase4/src/phase4/run_f1_frw_lcdm_probe.py`, which
  reads the FRW viability mask
  (`phase4_F1_frw_viability_mask.csv`) and defines a broad
  "ΛCDM-like" window on top of the FRW-viable grid points.
- Used toy targets \(\Omega_\Lambda^{\mathrm{target}} \approx 0.7\)
  (tolerance ±0.1) and \(t_0^{\mathrm{target}} \approx 13.8\,\mathrm{Gyr}\)
  (tolerance ±1 Gyr) with \(\Omega_m = 0.3\), \(\Omega_r = 0\),
  \(H_0 = 70\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\), matching the FRW
  viability rung.
- Recorded the resulting diagnostics in
  `phase4/outputs/tables/phase4_F1_frw_lcdm_probe.json`, including
  the ΛCDM-like fraction (`lcdm_like_fraction ≈ 0.03`) and the
  θ-range and age/Ω\(_\Lambda\) ranges of the selected subset.
- Wrote a per-θ ΛCDM-like mask to
  `phase4/outputs/tables/phase4_F1_frw_lcdm_probe_mask.csv`, adding a
  `lcdm_like` Boolean column on top of the FRW-viability mask.
- Updated `phase4/paper/sections/03_diagnostics_stub.tex` and
  `phase4/OVERVIEW.md` to document this ΛCDM-facing probe as a
  non-binding, illustrative diagnostic rather than a data-driven
  constraint or a mechanism for selecting a unique \(\theta_\star\).

## 2026-01-07 - Rung 12: F1/FRW shape probe

- Added `phase4/src/phase4/run_f1_frw_shape_probe.py` to join the toy F1
  shape mask, the FRW-viability mask, and the \(\Lambda\)CDM-like probe
  mask on the common Phase 4 \(\theta\)-grid.
- Generated a joined per-\(\theta\) mask
  `phase4/outputs/tables/phase4_F1_frw_shape_probe_mask.csv` with Boolean
  flags for `in_toy_corridor`, `frw_viable`, `lcdm_like`, and the
  composite intersections `shape_and_viable`, `shape_and_lcdm`.
- Wrote a diagnostics summary to
  `phase4/outputs/tables/phase4_F1_frw_shape_probe.json`, which records
  the fractions and \(\theta\)-ranges of these sets; in the current
  baseline run this reveals a small but non-zero overlap region where
  the toy F1 corridor, FRW-viable histories, and \(\Lambda\)CDM-like
  windows coexist.
- Updated `phase4/paper/sections/03_diagnostics_stub.tex` and
  `phase4/OVERVIEW.md` so that the Phase 4 paper and overview document
  fully reflect this joined shape-probe layer as a non-binding,
  FRW-facing diagnostic.

## 2026-01-07 - Rung 13: F1/FRW shape-probe summary figure

- Added `phase4/src/phase4/plot_f1_frw_shape_probe.py` to visualise the
  joined F1/FRW/LCDM shape probe on the common Phase 4 \(\theta\)-grid.
- Generated `phase4/outputs/figures/phase4_F1_frw_shape_probe_omega_lambda_vs_theta.png`,
  a scatter plot of \(\Omega_\Lambda(\theta)\) highlighting FRW-viable
  points, \(\Lambda\)CDM-like points, and their intersection with the toy
  F1 corridor.
- Updated `phase4/paper/sections/03_diagnostics_stub.tex` to reference
  this figure and explain its role as a compact summary of the Phase 4
  FRW-facing diagnostics.

## 2026-01-07 - Rung 12: FRW data-probe scaffolding (no bundled data)

- Added `phase4/FRW_DATA_DESIGN.md` to describe a data-facing FRW probe
  that builds on the existing F1 mapping and FRW viability layer.
- Implemented and ran `phase4/src/phase4/run_f1_frw_data_probe.py`, which:
  - reads `phase4/outputs/tables/phase4_F1_frw_viability_mask.csv`;
  - optionally consumes an external binned distance–redshift dataset
    from `phase4/data/external/frw_distance_binned.csv` with columns
    (`z`, `mu`, `sigma_mu`);
  - for each FRW-viable theta, computes FRW luminosity distances and
    distance moduli and evaluates a simple chi^2 statistic; and
  - writes:
    - `phase4/outputs/tables/phase4_F1_frw_data_probe.json`
      (diagnostics), and
    - `phase4/outputs/tables/phase4_F1_frw_data_probe_mask.csv`
      (per-theta chi^2 and a `data_ok` flag).
- In the current repository configuration, no external data file is
  present at `phase4/data/external/frw_distance_binned.csv`. The run
  therefore records `data_available = false`, `n_data_points = 0`, and
  sets `data_ok = 0` for all rows, with chi^2 fields set to NaN. This
  keeps the rung reproducible without bundling any third-party dataset
  while leaving a clear hook for future data-level experiments.
- No changes were made to the Phase 4 Snakefile or gate; this rung is
  an optional, manual diagnostic layer consistent with the Phase 0
  claim-discipline philosophy.

## 2026-01-07 - Rung 13: FRW data probe in paper and overview

- Extended `phase4/paper/sections/03_diagnostics_stub.tex` with a dedicated
  paragraph describing the FRW data-facing probe, its inputs and outputs, and
  its current baseline behaviour (`data_available = false`, `data_ok = 0` for
  all grid points).
- Updated `phase4/OVERVIEW.md` so the Phase 4 narrative now includes the FRW
  data probe as an optional, non-binding layer on top of the FRW viability
  infrastructure.
- No changes were made to the Phase 4 Snakefile or gate; the data probe remains
  a manual, opt-in diagnostic consistent with Phase 0 claim discipline.

## 2026-01-07 - Rung 14: FRW synthesis note and explicit limitations

- Added `phase4/FRW_SYNTHESIS.md` to summarise the FRW-facing layers of Phase 4
  (sanity curve, shape corridor, FRW viability, corridors, \Lambda CDM-like
  probe, shape overlap, and the data probe scaffold) together with the key
  baseline fractions and an honest list of limitations.
- Extended `phase4/paper/sections/04_limitations_stub.tex` with a dedicated
  paragraph on FRW-facing limitations, clarifying that the current FRW layers
  are simple plausibility checks under hand-fixed background parameters and
  broad age/\Omega_\Lambda windows, not full cosmological fits.
- Kept all new material strictly non-claim-expanding: no new \theta-filters or
  data-driven claims were introduced at this rung.

## 2026-01-07 - Rung 15: Hard-novelty roadmap for Phase 4

- Added `phase4/HARD_NOVELTY_ROADMAP.md` to capture concrete directions for
  turning the current F1 + FRW infrastructure into harder scientific novelty
  (simple data-facing checks, FRW hyperparameter scans, and a sharper mapping
  back to the origin-axiom machinery).
- Framed all proposals as design-level next steps rather than present claims,
  preserving the current Phase 4 scope as primarily infrastructural and
  corridor-mapping.
- Left the Phase 4 paper unchanged at this rung; no new \theta-filters or
  data-driven results were introduced.
