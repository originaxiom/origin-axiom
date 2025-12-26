# Origin Axiom — Phase 2  
**Quantitative Vacuum Energy Residual and Cosmological Implications**

---

## Overview

Phase 2 of the Origin Axiom project investigates whether the global non-cancellation principle
established in Phase 1 can give rise to a **small, positive vacuum energy residual** in a
more realistic, QFT-inspired setting, and whether such a residual is **cosmologically viable**.

This phase focuses on **quantitative behavior**, **robustness**, and **cosmological response**.
It does not attempt to identify the microscopic origin of the interference phase or connect
the mechanism to particle physics sectors.

Phase 1 is treated strictly as an **interface**: its axiom is assumed, not modified or re-derived.

---

## Scope and Claims (Phase 2)

Phase 2 demonstrates that:

- The Origin Axiom enforces a **non-zero vacuum energy residual** in a finite mode-sum model.
- The residual is **robust** under variation of the global floor parameter ε, the UV cutoff,
  and the number of contributing modes.
- When interpreted as an effective vacuum energy density, the residual produces
  **Λ-like late-time acceleration** in a standard flat FRW cosmology.

This phase does **not**:

- identify the microscopic origin of the interference phase,
- claim an exact numerical match to the observed cosmological constant,
- modify Einstein’s equations or introduce new gravitational dynamics,
- address Standard Model, flavor, or unification questions.

All such issues are explicitly deferred to later phases.

---

## Modeling Approach

Phase 2 uses a **QFT-inspired mode-sum model** as its primary engine.

- Vacuum energy is modeled as a sum over paired modes with phase interference.
- A global non-cancellation constraint (ε) prevents exact destructive cancellation.
- All parameters are treated as **dimensionless control variables** in code units.

An optional lattice-based model is included for future extensions but is disabled by default.

---

## Figures and Their Roles

Phase 2 produces five canonical figures:

- **Figure A** — Existence of a non-zero vacuum energy residual under the Origin Axiom.
- **Figures B–D** — Robustness of the residual under variation of:
  - ε (global non-cancellation floor),
  - UV cutoff,
  - number of contributing modes.
- **Figure E** — Cosmological response of a flat FRW universe to the residual,
  compared against matter-only and observed ΛCDM expansion.

Figure E demonstrates **Λ-like behavior**, not Λ-scale fitting.

---

## Reproducibility and Workflow

Phase 2 follows strict reproducibility rules inherited from Phase 1:

- All parameters are declared in a single YAML file: `config/phase2.yaml`.
- All figures are generated via **Snakemake**; no manual figures are permitted.
- Every numerical run produces:
  - a run directory with full metadata,
  - raw machine-readable outputs,
  - a summary JSON file.
- Canonical figures are copied into `outputs/figures/` and tracked by the workflow.

Randomness is fully controlled by an explicit seed.

---

## Canonical Reproduction

To reproduce all Phase 2 results and figures:

```bash
cd phase2
snakemake -c 1