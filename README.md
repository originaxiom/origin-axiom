# Origin Axiom – Phased Vacuum Mechanism

> **Origin Axiom**
>
> *“Twist Euler’s perfect cancellation,  
> then follow the residue wherever it leads.”*

This repository hosts the **phased Origin Axiom program**.

The repo is structured as a **laddered research program**, designed to make each step auditable, reproducible, and composable.

- **Scoped** — clear aims, hard non-claims
- **Reproducible** — Snakemake workflows and deterministic scripts
- **Readable** — LaTeX papers supported by explicit artifacts
- **Composable** — later phases build only on locked outputs

If you want to *understand* the structure, read the phase papers in order.  
If you want to *run* the machinery, follow the workflow instructions in each phase.

---

## Current status (high-level)

- **Phase 0 — Motivation & framing**  
  Conceptual groundwork: why *no perfect cancellation* is enforced, and what governance constraints are imposed on candidate `θ` values (irregularity, transcendence, self-reference, etc.).

- **Phase 1 — Formalization of the axiom**  
  Starts turning the philosophical non-cancellation principle into a minimal, testable axiom and toy demonstrations.

- **Phase 2 — Early dynamics & scaling tests**  
  More exploratory and “legacy-heavy”: attempts to connect the axiom to dynamical behavior and scaling, later revised and corrected.

- **Phase 3 — Mechanism baseline (locked)**  
  A concrete toy mechanism implementing a non-cancelling vacuum amplitude, with fully reproducible diagnostics and no cosmological claims.

- **Phase 4 — Vacuum → FRW consistency checks**  
  A structured, non-binding interface between the Phase 3 amplitude and FRW-like toy cosmology diagnostics. Corridor-style viability tests, no data fitting.

- **Phase 5 — Program interface & dashboard (skeleton)**  
  A meta-level phase that formalizes interfaces over Phase 3–4 outputs and prepares a viability dashboard without introducing new physics claims.

---

## Repository structure (conceptual)

Each phase lives in its own directory and follows the same internal logic:

- `paper/` — the LaTeX source for the phase paper
- `src/` — phase-specific code and scripts
- `workflow/` — Snakemake or orchestration logic (when applicable)
- `outputs/` — generated tables, figures, and JSON diagnostics
- `docs/` — supplemental notes or contracts (when applicable)

Canonical artifacts are always referenced explicitly by file path in the papers.

---

## Governance and scope

This project follows strict governance rules defined in **Phase 0**:

- claims must be bounded and explicitly stated
- non-claims are mandatory
- evidence must be file-addressable and reproducible
- corridor narrowing (e.g. on `θ`) is append-only and auditable
- failures are recorded, not hidden

Narrative motivation is **not** evidence.

---

## What this repository does *not* claim

- no derivation of a unique or preferred `θ⋆`
- no solution to the cosmological constant problem
- no fit to observational cosmological data
- no claim of physical completeness or realism

All cosmology-facing constructs are explicitly labeled as **toy**, **diagnostic**, and **non-binding**.

---

## How to engage

- **To read**: start with Phase 0, then proceed sequentially.
- **To run**: follow the workflow instructions inside each phase directory.
- **To extend**: respect phase boundaries and the Phase 0 contracts.

Any contribution or extension must preserve reproducibility and auditability.

---

## Status

The project is active, iterative, and intentionally conservative in its claims.  
Later phases are expected to refine mechanisms, mappings, and diagnostics — not to retroactively justify earlier intuition.
