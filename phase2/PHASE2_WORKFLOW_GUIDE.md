# Phase 2 — Workflow Guide (Phase-1 Style)

This file defines the intended “Phase 1 style” workflow for Phase 2: a disciplined,
artifact-first, drift-resistant process.

This guide is a procedure document; it is not a scientific claim source.

---

## 1. Principles

1. **Artifacts are the source of truth.**
   The paper must match Figures A–E; not the other way around.

2. **Claims are bounded.**
   Only existence, robustness, and viability claims are allowed.

3. **Provenance is mandatory.**
   Every canonical figure must map to a single run directory with complete metadata.

4. **No hidden defaults.**
   Any value influencing outputs must be declared in `config/phase2.yaml`.

---

## 2. Canonical execution

The canonical build command is:

- `snakemake -c 1 all`

This must produce:

- `outputs/figures/figA...figE.pdf`
- `outputs/figures/*.run_id.txt`
- `paper/main.pdf` (if the paper rule is enabled)

---

## 3. Run directory structure

Each run lives in:

- `outputs/runs/<run_id>/`

and must contain, at minimum:

- `params.json`
- `meta.json`
- `summary.json`
- `raw/*.npz`
- `figures/*.pdf`

The run_id must be stable for that run and recorded via the figure pointer.

---

## 4. Canonical figure pointers

The canonical figure directory:

- `outputs/figures/`

contains:

- the canonical figure PDF,
- a `*.run_id.txt` file pointing to the provenance-complete run.

The pointer file must contain exactly one run_id line. No comments, no extra whitespace.

---

## 5. Changing figures, claims, or config

If you change anything that affects results:

1. Make the code/config change.
2. Run `snakemake -c 1 all`.
3. Verify new A–E.
4. Update `outputs/figures/*.run_id.txt` if run_ids changed.
5. Update claim pointers in `CLAIMS.md` if raw output filenames changed.
6. Log the change in `PROGRESS_LOG.md`.

Never “hand edit” PDFs in `outputs/figures/`.

---

## 6. Paper discipline rules

The paper must:

- reference only canonical figures A–E,
- contain only the claims listed in `CLAIMS.md`,
- explicitly state non-claims and limitations,
- separate axiom/interface assumptions from toy-model choices and from FRW interpretation.

---

## 7. Minimal collaboration procedure (you + me)

We work in this order:

1. Lock MD documents (scope/claims/assumptions/provenance rules).
2. Audit scripts for hidden defaults and parameter correctness.
3. Regenerate A–E and freeze run pointers.
4. Populate LaTeX sections with rich argument that mirrors `CLAIMS.md`.
5. Final “lock checklist” pass.

---

## 8. Definition of Done

Phase 2 is done when:

- A–E are reproducible and pinned,
- the paper compiles and matches claims,
- no hidden defaults remain,
- repo contains no runtime junk and no ambiguous run history.

---
---

Doc status: Phase 2 workflow guide (Phase-1 style) describing how to run and audit the Phase 2 pipeline; operational guidance only; for formal contracts and claims, see `phase2/PHASE2_ALIGNMENT_v1.md` and the Phase 2 paper.
