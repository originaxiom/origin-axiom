# Phase 2 — Reproducibility and Provenance

This document defines the **reproducibility guarantees, provenance tracking, and execution
rules** for Phase 2.

**Rule:** No scientific claim is valid unless it is backed by a fully reproducible artifact
listed in `CLAIMS.md`.

---

## 1. Single source of truth

All parameters are declared in:

- `config/phase2.yaml`

No script may use hidden defaults that affect scientific results. If a parameter influences
any computed quantity or plotted output, it must appear in the YAML and be captured into
run metadata.

---

## 2. Canonical runner

The only canonical way to generate Phase 2 artifacts is:

- `snakemake -c 1 all`

Directly running scripts is allowed for local debugging, but **does not produce canonical
artifacts** unless the outputs are identical and the run metadata is complete.

---

## 3. Canonical artifacts and run pointers

Canonical figures are the five PDFs in:

- `outputs/figures/`

Each canonical figure has a stable run pointer file:

- `outputs/figures/<figure_basename>.run_id.txt`

This file contains a single `run_id`, and the corresponding run directory:

- `outputs/runs/<run_id>/`

must contain:

- `params.json` — full resolved parameter snapshot (including derived values)
- `meta.json` — environment metadata (Python version, package versions, platform)
- `summary.json` — scalar outputs and derived metrics used in text/captions
- `raw/*.npz` — raw arrays for all plots
- `figures/*.pdf` — run-local figures used to build canonical figures
- `logs/` — Snakemake logs or script logs, if produced

---

## 4. Determinism

Phase 2 runs are deterministic up to floating-point precision.

If any stochastic component exists, it must be controlled via:

- `global.seed`

and the seed must be recorded in `params.json`.

---

## 5. Modification policy (anti-drift)

Any change that modifies:

- a canonical figure A–E,
- any claim statement,
- any configuration key affecting outputs,
- any derived scalar used in the paper,

requires:

1. Updating the relevant Snakemake rule or script.
2. Regenerating canonical artifacts A–E.
3. Updating `outputs/figures/*.run_id.txt`.
4. Updating `CLAIMS.md` provenance pointers if any file paths changed.
5. Recording the change in `PROGRESS_LOG.md`.

---

## 6. What “locked” means

Phase 2 is considered **locked** when:

- `snakemake -c 1 all` reproduces **exactly** the canonical figures A–E,
- `paper/main.tex` compiles (via the Snakemake paper rule),
- every claim in the paper is present in `CLAIMS.md` and backed by A–E,
- there are no hidden defaults and no extra “canonical” figures.

---

## 7. Minimal review packet

A reviewer should need only:

- `SCOPE.md`
- `CLAIMS.md`
- `ASSUMPTIONS.md`
- `REPRODUCIBILITY.md`
- `outputs/figures/` (A–E + run pointers)
- `paper/`

to evaluate Phase 2 within scope.

---