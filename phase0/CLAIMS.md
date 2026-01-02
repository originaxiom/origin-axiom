# Phase 0 — Claims Ledger

Phase 0 is a **governance and method** layer for the Origin Axiom program.  
It does **not** assert physics content; it defines contracts that later phases must satisfy.

Each claim below has:
- a stable ID `P0-Cxx`,
- a type (Governance / Method / Reproducibility / Taxonomy),
- a short statement,
- evidence pointers (file paths in this repository),
- and, where relevant, obligations imposed on later phases.

---

## P0-C01 — Corridor and θ-filter are first-class governed objects

**Type:** Method / Governance  

**Statement:**  
Phase 0 defines the “corridor” \(\corridor\) and the θ-filtering procedure as first-class objects, with explicit artifacts and schemas that must be kept under version control.

**Evidence (this repo):**
- `phase0/paper/sections/02_axioms_and_definitions.tex`
- `phase0/paper/sections/03_corridor_method.tex`
- `phase0/schemas/phase_theta_filter.schema.json`
- `phase0/phase_outputs/phase_00_theta_filter.json`
- `phase0/phase_outputs/phase_01_theta_filter.json`
- `phase0/phase_outputs/theta_corridor_current.json`
- `phase0/phase_outputs/theta_corridor_history.jsonl`

**Obligations for later phases:**  
- Any use of \(\thetastar\) or θ-corridors in Phases 1–N must reference these artifacts or clearly document deviations.

---

## P0-C02 — Schema discipline for corridor artifacts

**Type:** Method / Reproducibility  

**Statement:**  
All Phase 0 corridor/filter artifacts must validate against their declared JSON Schemas, and any schema change that would invalidate existing artifacts must be versioned and documented.

**Evidence (this repo):**
- `phase0/schemas/phase_theta_filter.schema.json`
- `phase0/schemas/theta_corridor.schema.json`
- `phase0/paper/sections/05_reproducibility_contract.tex`
- `phase0/paper/appendices/B_phase_theta_filter_schema.tex`

**Obligations for later phases:**  
- When a phase consumes `phase0/phase_outputs/*.json`, it must treat schema versions as part of the reproducibility contract.
- Breaking schema changes require:
  - a new schema file or version tag,
  - an entry in `phase0/PROGRESS_LOG.md`,
  - an update to this `CLAIMS.md` if claim semantics change.

---

## P0-C03 — Reproducibility contract across phases

**Type:** Reproducibility / Governance  

**Statement:**  
For every scientific claim in any phase, there must exist a machine-executable reproduction path, with pinned configuration, seeds, and environment description, sufficient for an external reviewer to regenerate the canonical figures.

**Evidence (this repo):**
- `phase0/paper/sections/05_reproducibility_contract.tex`
- `docs/REPRODUCIBILITY.md`
- `phase1/REPRODUCIBILITY.md`
- `phase2/REPRODUCIBILITY.md`
- Snakemake workflows:
  - `phase1/workflow/Snakefile`
  - `phase2/workflow/Snakefile`

**Obligations for later phases:**  
- Each phase must:
  - define canonical figures in its paper,
  - provide Snakemake rules (or equivalent) to regenerate them from committed configs and code,
  - document the procedure in its own `REPRODUCIBILITY.md`.

---

## P0-C04 — Explicit claim taxonomy and non-claims

**Type:** Governance / Taxonomy  

**Statement:**  
Each phase must declare its allowed claim types and explicit non-claims (what it does *not* assert), and must register all claims in a global index.

**Evidence (this repo):**
- `docs/PHASES.md`
- `docs/CLAIMS_INDEX.md`
- `phase1/CLAIMS.md`
- `phase2/CLAIMS.md`
- `phase0/paper/sections/04_phase_contracts.tex`
- `phase0/paper/sections/06_falsifiability_and_failure_modes.tex`
- `phase0/paper/appendices/D_claims_checklist.tex`

**Obligations for later phases:**  
- No new claim may appear only in prose; it must:
  - have a stable ID (e.g. `P1-C03`, `P2-C21`),
  - be listed in the phase’s `CLAIMS.md`,
  - be summarized in `docs/CLAIMS_INDEX.md` with pointers to evidence.

---

## P0-C05 — Failure-mode and limitation documentation is mandatory

**Type:** Governance / Method  

**Statement:**  
Every phase that makes scientific claims must explicitly document its limitations, known failure modes, and “non-claim” regions where the model is not being asserted to describe reality.

**Evidence (this repo):**
- `phase0/paper/sections/06_falsifiability_and_failure_modes.tex`
- `phase1/paper/sections/06_limitations.tex`
- `phase2/paper/sections/07_limitations_and_nonclaims.tex`
- `docs/PHASES.md` (allowed claim types per phase)

**Obligations for later phases:**  
- New phases must include:
  - a dedicated limitations / non-claims section in the paper,
  - corresponding entries in that phase’s `CLAIMS.md`.

---

## P0-C06 — Canonical artifact locations

**Type:** Governance / Reproducibility  

**Statement:**  
Each phase must distinguish between:
- **canonical artifacts** (papers, key figures, minimal data needed for review), and  
- **ephemeral runs** (exploratory or redundant outputs),

and store them in predictable locations.

**Evidence (this repo):**
- `docs/PHASES.md` (canonical artifacts per phase)
- `docs/ARCHIVE.md`
- `phase0/paper/main.tex` (Phase 0 paper)
- `phase1/artifacts/origin-axiom-phase1.pdf`
- `phase2/outputs/figures/*.pdf` (Phase 2 canonical figures)

**Obligations for later phases:**  
- Canonical artifacts:
  - Papers in `phaseX/artifacts/` (e.g. `origin-axiom-phaseX.pdf`) or clearly referenced from there.
  - Canonical figures in `phaseX/outputs/figures/`.
- Ephemeral or bulk outputs:
  - `phaseX/outputs/runs/` (ignored by git) or external legacy archives.

---

## P0-C07 — Provenance logging for governance changes

**Type:** Governance / Reproducibility  

**Statement:**  
Changes to governance, claim taxonomy, or corridor definitions must be logged with motivation and impact to enable external auditing of project evolution.

**Evidence (this repo):**
- `phase0/PROGRESS_LOG.md`
- `phase1/PROGRESS_LOG.md`
- `phase2/PROGRESS_LOG.md`
- `docs/ARCHIVE.md` (promotion / deprecation rules)

**Obligations for later phases:**  
- Any change that affects:
  - claim semantics,
  - reproducibility guarantees,
  - corridor / schema definitions,
must be accompanied by a `PROGRESS_LOG` entry with:
  - date (preferably UTC),
  - summary of change,
  - affected files and phases,
  - rationale.

