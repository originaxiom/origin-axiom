# Phase 2 — Scope Definition

This document defines the **exact scope** of Phase 2 of the Origin Axiom project.

Any interpretation, claim, or extrapolation outside this scope is invalid for Phase 2.

---

## 1. Purpose of Phase 2

Phase 2 exists to answer a constrained, quantitative question:

**Conditional on the Origin Axiom (Phase 1), can a QFT-inspired finite mode-sum toy model
exhibit a stable, non-zero vacuum-energy proxy residual; is that residual robust to
controlled parameter variation; and is it *cosmologically viable* (in the limited sense
of producing a Λ-like late-time acceleration signature) when inserted into standard flat
FRW dynamics?**

Phase 2 is a *discipline phase*: it tightens definitions, provenance, and robustness
checks, without expanding the ontological reach of the project.

---

## 2. In-Scope Topics

Phase 2 includes **only** the following:

- A QFT-inspired **finite mode-sum** model used as a qualitative proxy for vacuum
  contributions (no claim of full QFT completeness or renormalization).
- An explicit **Origin Axiom enforcement operator** (a global non-cancellation floor
  parameterized by ε).
- A numerical demonstration of:
  - **existence** of a non-zero residual (Claim 2.1),
  - **robustness** under controlled sweeps in ε, cutoff, and number of modes (Claim 2.2).
- A standard **flat FRW** wrapper showing *viability* of interpreting the residual as an
  effective Λ-like component (Claim 2.3), without modifying Einstein’s equations.
- Strict reproducibility: a single YAML config, Snakemake as the canonical runner, and
  complete run provenance.

---

## 3. Explicitly Out-of-Scope Topics

Phase 2 explicitly excludes:

- ❌ Derivation of ε from first principles.
- ❌ An exact numerical match to the observed cosmological constant.
- ❌ Claims of solving the cosmological constant problem in a definitive sense.
- ❌ Identification of the microscopic origin of the interference phase.
- ❌ Modified gravity, new gravitational dynamics, or changes to Einstein’s equations.
- ❌ Early-universe modeling (inflation, reheating, phase transitions), structure
  formation, or data confrontation (CMB, BAO, SNe Ia).
- ❌ Standard Model / flavor / neutrino physics connections.
- ❌ Any unification narrative (dark matter, baryogenesis, etc.).

---

## 4. Scope of Validity

Phase 2 results are valid only within the following limits:

- Models are **toy proxies**, not claimed fundamental.
- Numerical results establish **existence/robustness/consistency**, not precision
  predictions.
- Cosmological interpretation is **phenomenological** and explicitly parameterized in
  configuration.
- Conclusions are conditional on the assumed axiom.

---

## 5. Relationship to Phase 1

- Phase 1 remains **frozen** (conceptually and numerically).
- Phase 2 **inherits** the Origin Axiom as an interface constraint.
- Phase 2 does **not** reinterpret, strengthen, or modify Phase 1.
- Phase 2 does **not** depend on Phase 1 code or outputs at runtime.

---

## 6. Interpretation Rule

If a statement is not explicitly supported by Phase 2 code, figures, and the claims
register (`CLAIMS.md`), it is **not part of Phase 2**.

This rule supersedes informal interpretation.
---

## Companion docs: workflow, lock checklist, and audit snapshot

For operational and audit-level context around this scope, the following
Phase 2 documents are relevant:

- `PHASE2_WORKFLOW_GUIDE.md` describes how to run the Phase 2 pipeline in
  practice, including which Snakemake targets to use, how figures and tables
  are produced, and how releases are prepared from the `phase2/` tree.

- `PHASE2_LOCK_CHECKLIST.md` records the conditions that must be satisfied
  before Phase 2 can be treated as locked (e.g. paper build cleanliness,
  reproducibility checks, and claim-to-artifact consistency).

- `AUDIT_REPORT.md` is a structural audit snapshot for Phase 2, generated at a
  specific point in time to inventory files, residual TODO markers, and
  potential cleanups. It is not a claims document; see this scope, `CLAIMS.md`,
  and `REPRODUCIBILITY.md` for the authoritative Phase 2 contract.
