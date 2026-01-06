# Phase 3 Progress Log

## 2026-01-05
- Bootstrapped Phase 3 contract docs (scope/non-claims/assumptions/approx contract/claims table).
- Added Phase 3 gate skeleton and workflow skeleton.
- Next: implement θ-fit runner + injection runner; generate first paper bundle.

## 2026-01-05 — Phase 3 θ-fit contract lock (bootstrap placeholder)
- Added `phase3/fit/ANSATZ_CONTRACT.md` + `phase3/fit/targets.yaml` (placeholder_mode=true).
- Upgraded `run_fit.py` to be contract-driven (YAML targets, provenance, diagnostics).
- Promoted fit diagnostics + meta to first-class artifacts in Snakemake + paper bundle.
- Updated CLAIMS_TABLE to point to the new artifacts.

## 2026-01-05 — Phase 3 baseline fixed-offset selected (b_PMNS = pi)
- Used discrete hypothesis sweep (theta_offset_sweep.csv) to select the baseline fixed offset.
- Winner: b_PMNS = pi (lowest chi2); locked into phase3/fit/targets.yaml as ansatz v1b-baseline-bpmns-pi.
- Added note: phase3/notes/offset_model_selection.md

## 2026-01-05 — Phase 3 baseline fixed-offset selected (b_PMNS = pi)
- Used discrete hypothesis sweep (theta_offset_sweep.csv) to select the baseline fixed offset.
- Winner: b_PMNS = pi (lowest chi2); locked into phase3/fit/targets.yaml as ansatz v1b-baseline-bpmns-pi.
- Added note: phase3/notes/offset_model_selection.md


## 2026-01-06 — Rung 1: Phase 3 Snakemake emits canonical PDF

- Updated `phase3/workflow/Snakefile` so that `build_phase3_paper_pdf` writes both:
  - `phase3/outputs/paper/phase3_paper.pdf` (staging)
  - `phase3/artifacts/origin-axiom-phase3.pdf` (canonical)
- Updated `rule all` to require the canonical artifact at `phase3/artifacts/origin-axiom-phase3.pdf`.
- Ran `snakemake -s phase3/workflow/Snakefile -c 1 build_phase3_paper_pdf` and confirmed both `phase3/outputs/paper/phase3_paper.pdf` and `phase3/artifacts/origin-axiom-phase3.pdf` were produced with matching sizes.
- Next: align global docs and Phase 3 paper text with this canonical artifact and existing claim IDs as defined in `phase3/CLAIMS.md`.


## 2026-01-06 — Rung 3: Phase 3 paper reproducibility appendix

- Expanded `phase3/paper/appendix/B_reproducibility.tex` to summarize the Phase 3 gate levels (A/B/C),
  the Snakemake entry point, and the paper bundle location, while keeping `phase3/REPRODUCIBILITY.md`
  as the authoritative contract.
- No changes to claim IDs (`C3.1`–`C3.3`) or physics content; this is purely an exposition improvement
  for reproducibility and audit clarity.


## 2026-01-06 - Rung 5: Phase 3 gate B (full rebuild + bundle verification)

- Ran `bash scripts/phase3_gate.sh --level B` to perform a full Phase 3 rebuild via Snakemake
  and verify the Phase 3 paper bundle.
- Confirmed that `phase3/outputs/tables/`, `phase3/outputs/figures/`, `phase3/artifacts/origin-axiom-phase3.pdf`,
  and `phase3/outputs/paper_bundle/run_index.json` + `bundle_manifest.json` were present and consistent.
- No changes to the ansatz, targets, or claim IDs; this rung only records that Gate B passed on this
  repository state.


## 2026-01-06 - Rung 6: Phase 0 ledger sees Phase 3 theta_filter

- Created a symlink `phase0/phase_outputs/phase_03_theta_filter.json` pointing to
  `../phase3/outputs/theta_filter/phase_03_theta_filter.json` so that the Phase 0 ledger
  can consume the Phase 3 theta filter without copying the file.
- This keeps Phase 0 corridor aggregation reading filters from a single phase_outputs/
  namespace while preserving Phase 3 as the source of truth for the Phase 3 theta filter.
- (Planned verification) Run:
  - `cd phase0 && python scripts/phase0_ledger.py update`
  - `cd phase0 && python scripts/phase0_ledger.py status`
  to confirm the corridor now includes Phase 3 as `phase_03_theta_filter.json`.


## 2026-01-06 — Rung 7: Phase 3 ledger-aligned claims and paper text

- Updated `phase3/CLAIMS.md` (C3.3) to include ledger-based falsifiability: Phase 3 is treated as
  falsified for the locked ansatz/target combination when the Phase 0 corridor ledger reports an
  empty combined corridor after applying the Phase 3 θ-filter.
- Extended `phase3/paper/sections/01_scope_and_nonclaims.tex` with a ledger-level outcome paragraph,
  explicitly stating that, in the current configuration, the Phase 0 ledger reports an empty
  corridor once the Phase 3 filter is applied, and that this is interpreted as a negative test for
  this specific ansatz/target choice (not a proof that the Origin Axiom is false).
- Added a ledger-incompatibility failure mode to
  `phase3/paper/sections/04_falsifiability.tex`, treating an empty combined corridor as evidence
  against the locked Phase 3 ansatz/target combination.
- Extended `phase3/paper/appendix/D_theta_filter.tex` with a subsection describing the current
  ledger outcome and how it is recorded in `phase0/phase_outputs/theta_corridor_history.jsonl`,
  so future Phase 3/4 runs can be compared against this baseline.
- Re-ran `bash scripts/phase3_gate.sh --level B` to confirm that the updated text, claims, and
  θ-filter appendix leave the Phase 3 workflow and paper bundle reproducible and gate-clean.


## 2026-01-06 - Rung 8: Phase 3 abstract + introduction upgrade

- Replaced the Phase 3 abstract with a structured summary that states the ansatz,
  external flavor targets, grid scan, injection into Phase 2, and the ledger outcome
  (empty combined corridor in the baseline configuration).
- Renamed `\\section{Scope and Non-Claims}` to `\\section{Introduction}` and
  updated the label to `sec:introduction` so the Phase 3 paper front matter reads
  like a conventional introduction while preserving the existing scope / non-claims content.
- No changes to claim IDs (C3.1–C3.3), filters, or numerical results; this rung only
  improves the narrative structure of the front section.


## 2026-01-06 - Rung 9: Phase 3 methods + injection results rewrite

- Rewrote `phase3/paper/sections/02_fit_pipeline.tex` as a structured Methods
  section for the flavor-sector fit, covering external targets, ansatz and
  offset hypotheses, grid scan and objective, uncertainty interval, offset
  sweep, and export of the ledger-facing `phase_03_theta_filter.json` artifact.
- Rewrote `phase3/paper/sections/03_injection_pipeline.tex` as a structured
  Results/Diagnostics section for the injection of the fitted \(\theta\) into
  the Phase 2 vacuum-residue mechanism, including a clear definition of the
  diagnostic curve \(\Delta\rho_{\mathrm{vac}}(\theta)\) and the role
  of the Phase 3 fit interval.
- Kept claim IDs (C3.1–C3.3), numerical artifacts, and gate workflow unchanged;
  this rung tightens the scientific narrative without altering the underlying
  computations.


## 2026-01-06 - Rung 10: Discussion/limitations + appendix labels

- Added explicit LaTeX labels for the Phase 3 claims table
  (`app:phase3_claims_table`), offset sweep table (`app:offset_sweep_table`),
  and theta-filter appendix (`sec:theta_filter_artifact`) so that cross-references
  from the Methods and Results sections remain stable.
- Rewrote `phase3/paper/sections/05_limitations.tex` as a structured Discussion
  and Limitations section, summarizing the negative corridor outcome, clarifying
  dependence on external flavor data and ansatz choices, and providing an outlook
  for future Phase 3 iterations and potential Phase 4+ extensions.
- Kept claim IDs (C3.1–C3.3), numerical artifacts, and the Phase 3 gate workflow
  unchanged; this rung improves scientific narrative and cross-reference hygiene
  without altering computations.


## 2026-01-06 - Rung 9: Phase 3 methods-style fit and injection sections

- Rewrote `phase3/paper/sections/02_fit_pipeline.tex` as a structured
  methods-style description of the flavor-phase fit: external targets and
  ansatz, objective function and scan, and the resulting fit artifacts
  (tables, diagnostics figure, and the ledger-facing θ-filter).
- Rewrote `phase3/paper/sections/03_injection_pipeline.tex` as a structured
  description of the one-way injection of θ into the Phase 2 vacuum-residue
  mechanism and the interpretation of the resulting
  Δρ_{\mathrm{vac}}(θ) diagnostic curve.
- No changes to the numerical results, fit configuration, or claim IDs;
  this rung only improves the clarity and conventional ``Methods'' feel of
  the core Phase 3 sections.

## 2026-01-06 — Rung 12: Phase 3 ansatz sketch + methods clarification

- Extended `phase3/paper/sections/02_fit_pipeline.tex` with a schematic
  equation summarizing the Phase 3 flavor-phase ansatz, keeping the explicit
  parameterization and offset hypotheses versioned in
  `phase3/fit/ANSATZ_CONTRACT.md`.
- Clarified the description of the $\chi^2$ grid scan and uncertainty interval,
  and made explicit that the numerical values of $\hat{\theta}$ and its
  admissible interval live in `theta_fit_summary.csv` and
  `theta_fit_diagnostics.json` as part of the formal methods contract.
- No changes to claim IDs, numerical artifacts, or workflow gates; this rung
  tightens the methods exposition only.


## 2026-01-06 - Rung 12: Phase 3 cross-reference cleanup

- Replaced the placeholder cross-reference `Section ??` in `phase3/paper/sections/05_limitations.tex` with `Section~\\ref{{sec:phase3-fit}}` so the Discussion points to the
  Phase 3 flavor-phase fit Methods section.
- Replaced the placeholder `Appendix ??` in `phase3/paper/sections/05_limitations.tex` with `Appendix~\\ref{{app:offset_sweep_table}}`, tying the discussion of
  fixed-offset choices to the labeled offset-sweep appendix.
- Updated `phase3/paper/sections/03_injection_pipeline.tex` so the
  reference to the Phase 3 θ-filter appendix uses `Appendix~\\ref{{sec:theta_filter_artifact}}` instead of a hard-coded
  letter, keeping the cross-reference robust under appendix reordering.
- No changes to claim IDs, numerical artifacts, or gate workflow; this
  rung only cleans up LaTeX cross-references for a more stable and
  readable Phase 3 paper.

## 2026-01-06 - Rung 13: Conclusion/outlook + reference hooks

- Added a `Conclusion and outlook` subsection to `phase3/paper/sections/05_limitations.tex` to summarise the negative-corridor result and frame Phase 3 as a calibration rung with an explicit failure mode.
- No changes to claim IDs (C3.1–C3.3), numerical artifacts, or gate workflow; this rung only improves narrative closure and reference hygiene.
