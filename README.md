# Origin Axiom – Phased Program Repository

This repository hosts a phased, fully reproducible program exploring a
non-cancelling residue mechanism in simple field / mode-sum models and its
potential cosmology-adjacent implications.

The project is structured into **phases**, each with:

- a clearly declared **scope** and **non-claims**,  
- a small set of **canonical artifacts** (paper, figures, outputs),  
- a **claims ledger** pointing to concrete evidence (runs, figures),  
- a reproducible workflow driven by configuration files and Snakemake.

Legacy exploratory work (early notebooks, one-off scans, etc.) has been moved
outside this repository; only what is needed for defensible, end-to-end
reproduction is kept here.

---

## Phased structure (overview)

A more detailed description lives in `docs/PHASES.md`. This is the high-level
map:

### Phase 0 – Governance, corridor method, and contracts

**Goal:** Define the *rules of the game* for all subsequent phases:

- formalize the **corridor / theta-filter** bookkeeping as JSON artifacts
  validated by explicit schemas,
- define **claim taxonomy** (existence / robustness / bounded viability, etc.),
- fix **reproducibility requirements** and failure-mode reporting,
- separate **method claims** (Phase 0) from **physics claims** (Phase 1+).

**Key artifacts:**

- `phase0/paper/main.tex` (+ `macros.tex`, `references.bib`) – Phase 0 paper,
- `phase0/artifacts/` – compiled Phase 0 paper PDF and other fixed outputs,
- `phase0/phase_outputs/` – corridor / theta-filter JSONs,
- `phase0/schemas/` – JSON Schemas for filters / corridors,
- `phase0/scripts/` – small utilities for generating / updating filters,
- `phase0/PROGRESS_LOG.md` – audit trail of Phase 0 evolution.

Phase 0 intentionally makes **no physics claims**. It only makes
**method/governance claims** about how phases are allowed to operate.

---

### Phase 1 – Lattice toy models and residue mechanism

**Goal:** Demonstrate the existence and basic robustness of the
non-cancelling residue mechanism in controlled toy domains.

- finite-size lattice models with constrained and unconstrained phases,
- identification of a **residual amplitude** that persists under constraints,
- basic **scaling** tests vs. lattice size and parameters.

**Allowed claim types (Phase 1):**

- existence (the mechanism appears in clearly defined toy systems),
- robustness (persists across parameter variations within stated bounds),
- scaling (within the toy-model domain only).

**Key artifacts:**

- `phase1/paper/main.tex` – Phase 1 paper source,
- `phase1/artifacts/origin-axiom-phase1.pdf` – compiled Phase 1 paper,
- `phase1/outputs/figures/` – canonical figures,
- `phase1/outputs/runs/` – run manifests and result bundles (ignored by git,
  but reproducible via Snakemake),
- `phase1/CLAIMS.md` – formal Phase 1 claims and evidence pointers,
- `phase1/ASSUMPTIONS.md`, `phase1/SCOPE.md`, `phase1/REPRODUCIBILITY.md`,
- `phase1/workflow/Snakefile` – Phase 1 Snakemake pipeline,
- `phase1/src/` – Phase 1 implementation.

---

### Phase 2 – Mode-sum model and FRW-style comparisons

**Goal:** Test whether the residue mechanism survives a stricter
mode-sum model and can be compared against FRW-style observables, **without
promoting this to a cosmology claim**.

- mode-sum model for an effective vacuum contribution,
- scaling tests vs. cutoffs / number of modes / ε parameters,
- FRW-style background and growth comparisons as **bounded viability checks**.

**Allowed claim types (Phase 2):**

- existence / robustness (within the mode-sum framework),
- bounded viability (FRW comparisons under clearly stated assumptions),
- explicitly **non-cosmological** unless otherwise and narrowly stated.

**Key artifacts:**

- `phase2/paper/main.tex` – Phase 2 paper source,
- `phase2/artifacts/` – compiled Phase 2 paper and fixed outputs,
- `phase2/outputs/figures/` – canonical figures A–F,
- `phase2/outputs/paper_bundle/` – reproducibility bundle for paper figures,
- `phase2/outputs/runs/` – full run manifests and raw outputs,
- `phase2/CLAIMS.md`, `phase2/ASSUMPTIONS.md`, `phase2/SCOPE.md`,
  `phase2/REPRODUCIBILITY.md`,
- `phase2/workflow/Snakefile` – Phase 2 Snakemake pipeline,
- `phase2/src/` – Phase 2 implementation (modes, FRW, scripts).

---

### Future phases (3+)

Future phases (e.g. connections to more realistic sectors, further
phenomenology, or synthesis) must:

1. declare scope and non-claims up front,
2. define canonical artifacts (paper, figures, bundles),
3. register claim IDs in `docs/CLAIMS_INDEX.md`,
4. obey all Phase 0 governance rules.

Until such phases are created, this repository only supports **Phase 0–2**.

---

## Repository layout

Only the most important top-level items are listed here:

- `phase0/` – governance layer (corridor method, contracts, schemas, Phase 0 paper).
- `phase1/` – lattice toy models, Phase 1 paper, figures, and pipelines.
- `phase2/` – mode-sum + FRW comparison, Phase 2 paper, figures, and pipelines.
- `docs/`  
  - `PHASES.md` – detailed description of each phase, scope, and canonical artifacts.  
  - `CLAIMS_INDEX.md` – global claims index (P0-Cxx, P1-Cxx, P2-Cxx, …).  
  - `REPRODUCIBILITY.md` – repo-wide reproducibility guidelines.  
  - `ARCHIVE.md` – policy for archiving/deprecating exploratory material.
- `.gitignore` – keeps LaTeX build artifacts, Snakemake caches, and
  `**/outputs/runs/` out of version control.

Each phase additionally contains:

- `README.md` – phase-local overview,  
- `CLAIMS.md`, `ASSUMPTIONS.md`, `SCOPE.md`, `REPRODUCIBILITY.md`,  
- `PROGRESS_LOG.md` – reviewer-facing change log for that phase.

---

## Reproducibility (quick start)

The repository is designed so that a referee can reproduce the main numerical
and figure results of each phase starting from a clean checkout.

A more detailed description lives in:

- `docs/REPRODUCIBILITY.md` – repo-wide rules and expectations,
- `<phaseX>/REPRODUCIBILITY.md` – phase-specific instructions.

Typical workflow:

1. **Clone the repo**

   ```bash
   git clone git@github.com:originaxiom/origin-axiom.git
   cd origin-axiom
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # or: source .venv/bin/activate.fish / Scripts/activate on Windows
   ```

3. **Install dependencies**

   Each phase provides its own configuration and (where needed) frozen
   requirements. See the corresponding `REPRODUCIBILITY.md` for the currently
   supported commands (for example, a `requirements-phase1-freeze.txt` for
   Phase 1).

4. **Run Snakemake pipelines**

   Phase 1:

   ```bash
   cd phase1
   snakemake -c 1 all
   ```

   Phase 2:

   ```bash
   cd phase2
   snakemake -c 1 all
   ```

   These pipelines regenerate canonical figures and populate `outputs/runs/`
   with run manifests. Each run bundle includes `meta.json`, `params_resolved.json`,
   `summary.json`, and a `pip_freeze.txt` snapshot of the environment.

5. **Build LaTeX papers**

   For each phase paper:

   ```bash
   cd phase0/paper   # or phase1/paper, phase2/paper
   latexmk -pdf main.tex
   ```

   Compiled PDFs are stored under the corresponding `artifacts/` directory to
   keep the git history clean.

---

## Claims discipline

A central design choice of this project is to make claims **explicit, bounded,
and evidence-backed**.

- `docs/CLAIMS_INDEX.md` lists all registered claims and their phase owner.  
- Each phase has a `CLAIMS.md` file defining:
  - claim IDs (e.g. `P1-C1`, `P2-C3`),
  - the type of claim (existence, robustness, bounded viability, etc.),
  - pointers to **canonical figures** and/or **pinned run IDs**,
  - explicit non-claims (what is *not* being asserted).

**Phase 0** makes only method/governance claims.  
**Phase 1+** may make physics-adjacent claims, but only within their declared
scope and under the assumptions listed in `ASSUMPTIONS.md`.

---

## Status and roadmap

Current status (early 2026):

- Phase 0:
  - paper skeleton and governance contracts in place,
  - corridor and filter artifacts backed by JSON Schemas,
  - progress log backfilled for repository re-organization.
- Phase 1:
  - paper and canonical figures available under `phase1/artifacts/` and
    `phase1/outputs/figures/`,
  - Snakemake pipeline generates the runs and figures referenced by the paper.
- Phase 2:
  - paper structure, mode-sum implementation, FRW-style comparison scripts,
    and run bundles in place,
  - pipeline support for scaling tests and binding certificate runs.

Future work:

- complete and refine Phase 0 paper narrative (governance + corridor method),
- finalize Phase 2 paper and tighten its claims vs. evidence mapping,
- define and instantiate Phase 3+ once Phase 1–2 are fully locked and audited.

For more detail, see:

- `docs/PHASES.md` – phase roles and constraints,
- per-phase `PROGRESS_LOG.md` – reviewer-facing change logs.

---

## Citation and contact

This repository is under active development. If you use any part of this work
in academic or applied contexts, please cite the relevant phase paper
(e.g. `phase1/artifacts/origin-axiom-phase1.pdf` and future Phase 0/2 papers)
and reference this repository.

The canonical public home of this code and documentation is:

- `https://github.com/originaxiom/origin-axiom`
