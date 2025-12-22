# Reproducibility Entrypoint — Origin Axiom (Gate 0)

This document defines the **single supported reproducibility entrypoint**
for the `origin-axiom` repository.

This is a **hard contract**.

If this entrypoint runs successfully on a clean checkout,
the Origin Axiom engine is considered reproducible.
If it fails, Gate 0 is considered violated.

---

## Scope

This entrypoint reproduces the **canonical Act III backbone**:

- Effective vacuum energy scale calibration
- θ★ observable background corridor vs ΛCDM
- Linear growth comparison and σ8-like consistency metrics

It does **not**:
- rerun large parameter sweeps
- regenerate exploratory scans
- perform observational data fitting
- introduce new physics

---

## Environment Assumptions

- Python ≥ 3.10
- Dependencies installed as documented for this repository
- Repository checked out at a clean commit
- No GPU required
- No external data access required

macOS / Linux supported.

---

## Single Entrypoint Command

From the repository root:

```bash
python3 scripts/reproduce_canonical_pipeline.py