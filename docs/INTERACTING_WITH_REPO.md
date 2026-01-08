# Interacting with the Origin Axiom Repository

This document explains **how to use** the repository safely:

- how to set up the environment,
- how to rebuild phases and artifacts,
- how to add new code or diagnostics without breaking contracts,
- how to reason about claims and non-claims.

If you are reading this, you should have skimmed `README.md` and
`docs/PROJECT_OVERVIEW.md` first.

---

## 1. Who this repo is for

- People who want to **rebuild** the Phase 0–5 artifacts and inspect the
  intermediate tables and figures.
- People who want to **extend** the program (e.g. add diagnostics, new phases,
  or data-probe layers) while keeping the governance and reproducibility
  discipline intact.
- The core author(s), who treat this as the canonical record of the project.

It is **not** intended as a polished “plug-and-play” library; it is a
structured experimental lab notebook.

---

## 2. Environment setup

### Python

- Use a dedicated virtual environment:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt   # or equivalent project file
  ```

- Do not commit `.venv/` or local IDE files; `.gitignore` is configured to
  ignore common cruft.

### LaTeX

- Install a reasonably recent TeX distribution (e.g. TeX Live 2023+).
- Ensure `pdflatex` and `latexmk` are on your `PATH`.

### Snakemake

- Install snakemake (e.g. `pip install snakemake`) in the same environment.
- The repo assumes you can run `snakemake` from the command line.

---

## 3. Rebuilding phases and artifacts

### 3.1 One-shot rebuild of all Phase PDFs

From the repository root:

```bash
./scripts/build_all_papers.sh
```

This will:

- run the Phase 3, 4, and 5 gates at Level A,
- rebuild each phase’s paper from its LaTeX sources,
- update `phaseN/artifacts/origin-axiom-phaseN.pdf` and the top-level
  `artifacts/origin-axiom-phaseN.pdf` copies.

If this completes without errors, your local artifacts are consistent with the
current source.

### 3.2 Running phase gates individually

Each major phase has a **gate script** under `scripts/`. For example:

- Phase 3 gate: checks the mechanism diagnostics and builds the Phase 3 paper.
- Phase 4 gate: regenerates FRW diagnostics and the Phase 4 paper.
- Phase 5 gate: regenerates the interface summary and sanity table.

You can invoke them directly when working on a particular phase. Consult the
script headers and the Phase papers’ reproducibility appendices for exact
commands.

---

## 4. Claims, artifacts, and how to trust results

A core rule of this program:

> **If there is no artifact, there is no claim.**

For each Phase:

- the **paper** (in `phaseN/artifacts/`) is the human-readable statement of
  what is being claimed;
- the **claims table** (appendix) maps textual claims to artifacts:
  tables, JSON files, figures, and scripts;
- the **reproducibility appendix** documents the exact scripts and entry points
  needed to regenerate those artifacts.

When modifying code or adding new results:

1. Update the **claims table** to reflect any new or changed claims.
2. Update the **reproducibility appendix** to describe the new scripts or
   changes to existing ones.
3. Ensure that the relevant gate still passes and that the Phase paper rebuilds
   cleanly.

---

## 5. Adding new code or diagnostics

### 5.1 General principles

- Prefer **phase-local** changes: if it belongs to Phase 3, put it under
  `phase3/src/phase3/` and make it visible through Phase 3’s paper and claims.
- Do not bypass Phase 5: cross-phase tooling should consume the program’s
  outputs through the **Phase 5 interface and summary**, not by chasing
  internal file paths.

### 5.2 Typical pattern

Suppose you want to add a new diagnostic to Phase 3:

1. Add a new script under `phase3/src/phase3/`, following existing naming
   conventions.
2. Hook it into the Phase 3 workflow (e.g. Snakemake rule, or a documented
   manual entry point).
3. Write its outputs under `phase3/outputs/` with a clear structure
   (tables, JSON, figures).
4. Reference it in the Phase 3 paper, update the claims table and reproducibility
   appendix.
5. Run the Phase 3 gate and ensure it passes from a clean checkout.
6. Optionally, expose a summary of the new diagnostic via the Phase 5 interface
   if it is relevant cross-phase.

---

## 6. Working with future phases

If you introduce new phases (e.g. `phase6/`):

- follow the existing directory pattern (`paper/`, `src/phase6/`, `outputs/`,
  `artifacts/`, `config/`, `data/`, `PROGRESS_LOG.md`);
- define a **gate script** and a **clear interface** for how it consumes prior
  phases and how future work should consume it;
- ensure it does not silently change the semantics of Stage I artifacts
  without migration notes.

---

## 7. Legacy material

The legacy migration notes (`docs/LEGACY_MIGRATIONS.md` and relatives) describe
which ideas and snippets from older, non-phased repositories are candidates
for integration.

When pulling in legacy code:

- never copy it verbatim without cleanup,
- bring it into a specific phase under the same governance and reproducibility
  rules,
- update the relevant papers and appendices.

---

## 8. Summary

When in doubt:

- read the **Phase paper** and its **claims / reproducibility appendices**;
- run the **appropriate gate** or `scripts/build_all_papers.sh`;
- prefer interacting with results through **documented artifacts and the Phase 5
  interface**, not through ad-hoc paths.

This keeps the origin-axiom program **auditable, extendable, and honest** about
what it does and does not show.
