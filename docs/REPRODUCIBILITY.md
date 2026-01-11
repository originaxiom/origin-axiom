# Reproducibility and Gates

This document explains how reproducibility works in the Origin Axiom Stage I program (Phases 0–5) and the Stage 2 diagnostic belts. It should be read together with:

- [`README.md`](../README.md) for the high-level story,
- [`docs/PROJECT_OVERVIEW.md`](PROJECT_OVERVIEW.md) for Stage I structure,
- [`docs/PHASES.md`](PHASES.md) for per-phase scope and non-claims,
- [`docs/STATE_OF_REPO.md`](STATE_OF_REPO.md) for current status,
- [`docs/CLAIMS_INDEX.md`](CLAIMS_INDEX.md) for claim mapping across phases.

The spirit is simple: any canonical claim must be backed by artifacts that a careful outsider can regenerate from this repository alone, using clearly documented steps.

---

## 1. Global principles (Phase 0 contract)

Phase 0 defines what “reproducible” and “locked” mean in this program. In practice, that translates into the following rules:

1. **Single source of truth for claims**  
   - Canonical physics claims live in the Phase papers (and, where applicable, explicit claims ledgers such as [`phase0/CLAIMS.md`](../phase0/CLAIMS.md), [`phase1/CLAIMS.md`](../phase1/CLAIMS.md), [`phase2/CLAIMS.md`](../phase2/CLAIMS.md)).  
   - Tables and figures under `phase*/outputs/` are evidentiary artifacts tied to those papers. Stage 2 results and experiments are explicitly non-canonical unless promoted via Phase 0 governance.

2. **Traceable artifacts**  
   - Every canonical table or figure used in a Phase paper must be traceable back to code in the repo (scripts, Snakemake/Make flows, or small reproducible drivers).  
   - Where possible, the Phase papers include a short reproducibility appendix summarizing which scripts to run and in what order.

3. **Environment and dependencies**  
   - Code is written to be runnable with standard Python tooling and a small set of scientific libraries. Exact versions are not pinned globally here, but Phase-specific READMEs and scripts should document any nonstandard requirements.  
   - Randomness, if used, should be seeded explicitly in scripts that generate canonical artifacts, so reruns produce the same outputs up to numerical noise.

4. **Version control discipline**  
   - Canonical artifacts (Phase papers, key tables, and figures) are checked into `artifacts/` and `phase*/outputs/`.  
   - Locking a Phase means: the relevant paper PDF under [`artifacts/`](../artifacts/) is considered the canonical narrative; changes go through standard git commits and are logged in [`PROGRESS_LOG.md`](../PROGRESS_LOG.md).

5. **Status categories**  
   - **Canonical**: lives under `phase0/`–`phase5/` with claims indexed in [`docs/CLAIMS_INDEX.md`](CLAIMS_INDEX.md); has a PDF in [`artifacts/`](../artifacts/).  
   - **Stage 2 diagnostic**: lives under `stage2/`, reads Phase outputs but does not change claims; documented in [`stage2/docs/`](../stage2/docs/).  
   - **Archived / experiment**: lives under `experiments/` or explicitly archived directories; described in [`stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md`](../stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md) or local archive banners.

When in doubt, trust the combination of `README.md`, `docs/STATE_OF_REPO.md`, and the Phase PDFs under `artifacts/` as the final word on what is canonical.

---

## 2. Canonical artifacts and papers

The primary narrative artifacts for Stage I are the Phase papers:

- Phase 0 – governance/specification: discussion is distributed across Phase 0 docs and global docs; see [`phase0/`](../phase0/) and [`phase0/CLAIMS.md`](../phase0/CLAIMS.md).  
- Phase 1 – toy ensembles: [`artifacts/origin-axiom-phase1.pdf`](../artifacts/origin-axiom-phase1.pdf).  
- Phase 2 – mode-sum + bounded FRW viability: [`artifacts/origin-axiom-phase2.pdf`](../artifacts/origin-axiom-phase2.pdf).  
- Phase 3 – mechanism module: [`artifacts/origin-axiom-phase3.pdf`](../artifacts/origin-axiom-phase3.pdf).  
- Phase 4 – FRW toy diagnostics stub: [`artifacts/origin-axiom-phase4.pdf`](../artifacts/origin-axiom-phase4.pdf).  
- Phase 5 – interface & sanity layer (early rungs): [`artifacts/origin-axiom-phase5.pdf`](../artifacts/origin-axiom-phase5.pdf).

Each paper should be read alongside:

- the corresponding `phase*/paper/` LaTeX sources, and  
- the tables and figures under `phase*/outputs/` that it references.

The rest of this document sketches how to think about rerunning those outputs, without being a substitute for the detailed instructions in each Phase’s paper and local README.

---

## 3. Re-running Stage I phases (high-level)

### 3.1 Phase 0 – Governance & specification

- Location: [`phase0/`](../phase0/), plus global docs under [`docs/`](./).  
- There is no numerical gate to re-run here; reproducibility is about understanding the rules that bind the other phases.  
- Before trusting or extending any claim, read:
  - [`phase0/CLAIMS.md`](../phase0/CLAIMS.md) for method claims,
  - [`docs/PHASES.md`](PHASES.md) for phase definitions,
  - [`docs/CLAIMS_INDEX.md`](CLAIMS_INDEX.md) for the map of claim IDs.

### 3.2 Phase 1 – Toy ensembles

- Location: [`phase1/`](../phase1/).  
- Canonical paper: [`artifacts/origin-axiom-phase1.pdf`](../artifacts/origin-axiom-phase1.pdf).  
- Canonical outputs: toy-domain figures and any supporting tables under `phase1/outputs/`.  
- Reproducibility pattern:
  - From the repo root, run the scripts or workflows documented in the Phase 1 paper’s reproducibility appendix and any `phase1/README` files.  
  - Confirm that the figures in `phase1/outputs/figures/` match those referenced in the paper.

### 3.3 Phase 2 – Mode-sum + bounded FRW viability

- Location: [`phase2/`](../phase2/).  
- Canonical paper: [`artifacts/origin-axiom-phase2.pdf`](../artifacts/origin-axiom-phase2.pdf).  
- Canonical outputs: tables and figures under `phase2/outputs/`, with a focus on mode-sum scans and FRW-style diagnostic masks.  
- Reproducibility pattern:
  - Use the Phase 2 paper’s reproducibility appendix and any local READMEs under `phase2/` to identify the entrypoint scripts or workflows.  
  - Rerun those to regenerate the diagnostic tables and figures; check that shapes and key numbers agree within numerical tolerance.

### 3.4 Phase 3 – Mechanism module

- Location: [`phase3/`](../phase3/).  
- Canonical paper: [`artifacts/origin-axiom-phase3.pdf`](../artifacts/origin-axiom-phase3.pdf).  
- Canonical outputs: mechanism-level tables and diagnostics under `phase3/outputs/tables/`.  
- Reproducibility pattern:
  - Follow the Phase 3 paper and [`phase3/ROLE_IN_PROGRAM.md`](../phase3/ROLE_IN_PROGRAM.md) to see how the mechanism module is defined and how its tables are used downstream.  
  - Use the scripts under `phase3/src/` (as documented in the paper and local READMEs) to regenerate the tables in `phase3/outputs/tables/`.  
  - Confirm that the table schemas and key summary numbers match those cited in the paper.

### 3.5 Phase 4 – FRW toy diagnostics

- Location: [`phase4/`](../phase4/).  
- Canonical paper (stub): [`artifacts/origin-axiom-phase4.pdf`](../artifacts/origin-axiom-phase4.pdf).  
- Canonical outputs: FRW-like shape, data, and viability masks under `phase4/outputs/tables/`.  
- Reproducibility pattern:
  - Identify the FRW construction scripts in `phase4/src/` (or equivalent drivers) as referenced in the Phase 4 paper.  
  - Rerun them to rebuild the masks; verify that the resulting CSVs agree in structure and aggregate statistics with the ones used by Stage 2 belts.

### 3.6 Phase 5 – Interface & sanity layer

- Location: [`phase5/`](../phase5/).  
- Canonical paper (early rungs): [`artifacts/origin-axiom-phase5.pdf`](../artifacts/origin-axiom-phase5.pdf).  
- Canonical outputs: interface summaries and sanity tables that sit on top of Phase 3/4 outputs.  
- Reproducibility pattern:
  - Use the Phase 5 paper and any local README/driver scripts to regenerate the interface artifacts from the locked Phase 3/4 tables.  
  - The key check is that Phase 5 does not introduce new mechanism or cosmology claims; it reads, summarizes, and sanity-checks.

---

## 4. Stage 2 diagnostic belts

Stage 2 lives under [`stage2/`](../stage2/) and is explicitly **downstream** of Phases 3/4. Stage 2 scripts:

- read tables produced by the Phases,  
- emit new diagnostic tables and, in some cases, figures,  
- never overwrite Phase artifacts or change Phase claims.

Stage 2 is non-canonical by default. Promotion of any Stage 2 result into a Phase paper requires a Phase 0–style gate and an explicit update to the relevant docs.

### 4.1 FRW corridor analysis

- Location: [`stage2/frw_corridor_analysis/`](../stage2/frw_corridor_analysis/).  
- Summary doc: [`stage2/docs/STAGE2_FRW_CORRIDOR_SUMMARY_v1.md`](../stage2/docs/STAGE2_FRW_CORRIDOR_SUMMARY_v1.md).  
- Inputs: FRW masks and diagnostic tables from [`phase4/outputs/tables/`](../phase4/outputs/tables/).  
- Outputs: corridor/viability tables under `stage2/frw_corridor_analysis/outputs/tables/` and, optionally, figures under `outputs/figures/`.  
- Reproducibility pattern:
  - Ensure Phase 4 outputs are present.  
  - Run the scripts in `stage2/frw_corridor_analysis/src/` as described in the summary doc to regenerate the Stage 2 tables.  
  - Use the Stage 2 summary doc to interpret the results; remember they are diagnostic only.

### 4.2 Mechanism/measure analysis

- Location: [`stage2/mech_measure_analysis/`](../stage2/mech_measure_analysis/).  
- Summary doc: [`stage2/docs/STAGE2_MECH_MEASURE_SUMMARY_v1.md`](../stage2/docs/STAGE2_MECH_MEASURE_SUMMARY_v1.md).  
- Inputs: Phase 3 mechanism tables under [`phase3/outputs/tables/`](../phase3/outputs/tables/).  
- Outputs: inventories, column stats, candidate measures, and preferred-measure diagnostics under `stage2/mech_measure_analysis/outputs/tables/`.  
- Reproducibility pattern:
  - Confirm Phase 3 outputs exist and are up to date.  
  - Run the Rung 1–6 scripts in `stage2/mech_measure_analysis/src/` to recreate the diagnostic tables.  
  - Use the summary doc to see how these diagnostics relate to the mechanism module; they do not change the Phase 3 claims.

### 4.3 Joint mech–FRW analysis

- Location: [`stage2/joint_mech_frw_analysis/`](../stage2/joint_mech_frw_analysis/).  
- Summary doc: [`stage2/docs/STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md`](../stage2/docs/STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md).  
- Inputs: Phase 3 mechanism tables and Phase 4 FRW masks.  
- Outputs: joint θ-grid tables and correlation summaries under `stage2/joint_mech_frw_analysis/outputs/tables/`.  
- Reproducibility pattern:
  - Ensure both Phase 3 and Phase 4 outputs are present.  
  - Run the Stage 2 scripts to rebuild the joint grid and diagnostic tables.  
  - Confirm that the joint grid respects θ-alignment checks (scripts will usually assert this).

### 4.4 FRW data-probe audit

- Location: [`stage2/frw_data_probe_analysis/`](../stage2/frw_data_probe_analysis/).  
- Summary doc: [`stage2/docs/STAGE2_FRW_DATA_PROBE_SUMMARY_v1.md`](../stage2/docs/STAGE2_FRW_DATA_PROBE_SUMMARY_v1.md).  
- Inputs: Phase 4 FRW data-probe mask tables under [`phase4/outputs/tables/`](../phase4/outputs/tables/).  
- Outputs: column stats and cross-tables relating data probes to viability under `stage2/frw_data_probe_analysis/outputs/tables/`.  
- Reproducibility pattern:
  - Check that Phase 4 data-probe masks exist.  
  - Run the Stage 2 scripts in `src/` to regenerate the Stage 2 tables.

### 4.5 Documentation audit belt

- Location: `stage2/doc_repo_audit/` (local git-ignored working directory; may not be present in a clean checkout).  
- Summary doc: [`stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md`](../stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md).  
- Outputs (CSV tables under `stage2/doc_repo_audit/outputs/tables/`):
  - `stage2_doc_inventory_v1.csv` – inventory of docs and key files,  
  - `stage2_doc_broken_refs_v1.csv` – suspected broken references (empty when clean),  
  - `stage2_doc_orphan_candidates_v1.csv` – potential orphan or legacy docs,  
  - `stage2_doc_open_threads_v1.csv` – explicit TODO-style narrative threads.

Reproducibility pattern:

- From the repo root, run the Stage 2 doc-audit scripts in `stage2/doc_repo_audit/src/` to regenerate the four CSVs.  
- Use [`stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md`](../stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md) alongside the CSVs to decide whether each orphan should be wired, archived, or retired.  
- The audit does not change any docs automatically; all edits are manual and must be logged in [`PROGRESS_LOG.md`](../PROGRESS_LOG.md).

---

## 5. Rebuild strategies

There are two typical ways to “start from scratch” with this repo.

### 5.1 Canonical Phase rebuild

This is appropriate if you want to audit or extend the core program.

1. Clone the repo and check out the desired commit or tag.  
2. Read `README.md`, [`docs/PROJECT_OVERVIEW.md`](PROJECT_OVERVIEW.md), [`docs/PHASES.md`](PHASES.md), and [`docs/STATE_OF_REPO.md`](STATE_OF_REPO.md) to understand which phases are locked, under audit, or stubbed.  
3. For each Phase you care about:
   - Read the Phase paper under [`artifacts/`](../artifacts/) and the LaTeX sources under `phase*/paper/`.  
   - Follow the reproducibility appendix and local READMEs to regenerate `phase*/outputs/` tables and figures.  
   - Compare outputs to those referenced in the paper.

### 5.2 Downstream Stage 2 audit

This is appropriate if you accept the current Phase outputs as given, and want to poke at them diagnostically.

1. Make sure the relevant Phase outputs exist (especially `phase3/outputs/tables/` and `phase4/outputs/tables/`).  
2. For each Stage 2 belt:
   - Read the corresponding `stage2/docs/STAGE2_*_SUMMARY_v1.md` file.  
   - Run the scripts under the belt’s `src/` directory to regenerate its `outputs/` tables and figures.  
   - Use the summary docs and CSVs to interpret results; remember they are non-canonical unless explicitly promoted.

---

## 6. Logging changes

Any change that affects:

- a Phase paper or its canonical outputs,  
- the status of a Phase (locked, under audit, stub),  
- the definition or activation of a Stage 2 belt,  
- or the canonical/archived status of a directory,

should be logged in [`PROGRESS_LOG.md`](../PROGRESS_LOG.md), with:

- date,  
- brief description of the change,  
- which Phase/Stage it touches,  
- and, if relevant, updated claim IDs or gates.

This ensures that anyone reading the repo can reconstruct not just *what* the artifacts are, but *when* and *under which rules* they were produced.

---

## 6. Repo audit checklist (Stage 2 belt)

For external auditors (or future selves) who want to check that the repository
state and documentation are consistent with the Phase 0 contracts and Stage 2
diagnostic belts, a minimal audit pass can proceed as follows:

1. **Build all Phase papers cleanly.**  
   - Use the top-level build scripts (see `scripts/`) to compile the Phase 0–5
     papers and confirm clean builds (no LaTeX errors, no lingering TODO/FIXME
     markers in the papers themselves).
   - Verify that the resulting PDFs match the consolidated artifacts under
     `artifacts/origin-axiom-phase*.pdf`.

2. **Check global docs and repo map.**  
   - Read `docs/PROJECT_OVERVIEW.md`, `docs/PHASES.md`, and
     `docs/STATE_OF_REPO.md` to confirm that the described phase/Stage structure
     matches the actual directory layout.
   - Use `docs/REPO_MAP_AND_ATLAS_v1.md` as a directory-level map to spot any
     unexpected or undocumented areas.

3. **Inspect Stage 2 diagnostic belts (FRW, mech, joint, data, θ★).**  
   - Read `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md` and the belt-level summaries
     under `stage2/docs/` (FRW corridor, mech/measure, joint mech–FRW, FRW
     data-probe).
   - Confirm that Stage 2 scripts only read Phase 3/4 outputs and write under
     `stage2/`, without mutating Phase artifacts in place.

4. **Review the Stage 2 doc/repo audit status.**  
   - Read `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md`, including the
     “Doc-audit status as of …” section, to see which documentation rungs have
     already been applied and which areas remain for future passes.
   - Optionally re-run the Stage 2 doc-audit scripts locally to regenerate the
     CSV snapshots if deeper inspection is needed.

5. **Cross-check claims against phase-local docs.**  
   - For any specific claim, use `docs/CLAIMS_INDEX.md` and the phase-local
     `SCOPE.md`, `CLAIMS.md`, and `REPRODUCIBILITY.md` files to verify:
       - where the claim is made,
       - which code/tables/figures support it, and
       - that the relevant scripts and artifacts live in the expected phase tree.

6. **Verify archive and experiment boundaries.**  
   - Use `docs/ARCHIVE.md`, `docs/GATES_AND_STATUS.md`, and
     `stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md` to check that:
       - archived or experimental work (e.g. `experiments/phase3_flavor_v1/`,
         `sandbox/`) is clearly marked as non-canonical,
       - canonical Phase 0–5 trees are not silently mixed with experimental
         artifacts, and
       - any promotions from Stage 2 into phases are gated and logged.

This checklist is intentionally conservative: it is designed to catch
misalignments between documentation, directory layout, and artifacts before any
stronger physics claims are considered.
