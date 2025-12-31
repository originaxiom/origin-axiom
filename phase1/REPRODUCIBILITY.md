# Phase 1 — Reproducibility Protocol

This document defines the reproducibility guarantees for Phase 1 of the
Origin Axiom project.

All results reported in Phase 1 are generated deterministically from
version-controlled code and configuration files.

---

## 1. Reproducibility Guarantee

Phase 1 guarantees the following:

- All figures appearing in the paper can be regenerated automatically committed figures (when present) are convenience artifacts, not source of truth.
- All numerical values plotted or reported originate from tracked scripts
- No manual data processing or figure editing is required
- All stochastic components are seeded and deterministic
- All outputs are traceable to a specific code state and configuration

Reproduction is expected to succeed on any standard Linux or macOS system
with Python ≥ 3.10.

---

## 2. Environment Reproduction

Phase 1 uses a pinned Python environment.

To reproduce the environment:

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements-phase1-freeze.txt