# Phase 1 — Scope Definition

This document defines the **exact scope** of Phase 1 of the Origin Axiom project.

Any interpretation, claim, or extrapolation outside this scope is invalid
for Phase 1 and should be treated as out of bounds.

---

## 1. Purpose of Phase 1

Phase 1 exists to answer a single foundational question:

**Can a minimal global non-cancellation axiom, imposed on otherwise canceling systems,
coherently yield a small but strictly nonzero residual?**

Phase 1 is not intended to explain all aspects of cosmology or fundamental physics.
It is a proof-of-concept stage.

---

## 2. In-Scope Topics

Phase 1 includes only the following:

- Formal statement of the Origin Axiom as a global constraint
- Minimal toy models demonstrating cancellation frustration
- Numerical simulations showing a nonzero residual floor
- Conceptual discussion of implications for vacuum energy
- Structural relation to known no-go arguments (e.g. Weinberg)
- Reproducible computational demonstrations

All content in Phase 1 directly serves these goals.

---

## 3. Explicitly Out-of-Scope Topics

Phase 1 explicitly excludes:

- ❌ Derivation of the cosmological constant value
- ❌ Claims of solving the cosmological constant problem
- ❌ Particle physics or Standard Model phenomenology
- ❌ Flavor physics, mixing angles, or θ★
- ❌ Selection or privileging of specific irrational constants (e.g. φ)
- ❌ Quantum gravity completion
- ❌ Inflation, baryogenesis, or dark matter models
- ❌ Claims of uniqueness or inevitability of the Origin Axiom

Any appearance of these topics in Phase 1 materials is illustrative only
and must not be interpreted as a physical claim.

---

## 4. Scope of Validity

Results in Phase 1 are valid only within the following limits:

- Toy models are not assumed to be fundamental
- Numerical results demonstrate qualitative behavior, not precision predictions
- Scaling arguments are heuristic unless explicitly proven
- Conclusions are conditional on the assumed axiom

Phase 1 does not establish empirical truth, only internal coherence.

---

## 5. Relationship to Later Phases

Phase 1 is designed to be **self-contained**.

Later phases may:
- refine models,
- introduce additional structure,
- explore phenomenological connections.

However:
- Phase 1 does not rely on later phases for its validity
- Failure or modification of later phases does not invalidate Phase 1 results

---

## 6. Interpretation Rule

If a statement, implication, or conclusion is not explicitly supported
by Phase 1 code, figures, or text, it is **not part of Phase 1**.

This rule supersedes informal interpretation.
---

## Companion docs: narrative, reproducibility, and paper

For readers who want more detail on how this scope is realised in code and in
the Phase 1 paper, the following documents are relevant:

- `README.md` (in `phase1/`) provides a Phase 1–specific overview of the toy
  ensembles, how they relate to the global non-cancellation axiom, and how to
  interpret Phase 1 outputs at a high level.

- `REPRODUCIBILITY.md` (in `phase1/`) records the Phase 1 reproducibility
  contract, including environment expectations, how to run the Phase 1
  workflows, and how figures/tables used in the paper are generated.

- `artifacts/origin-axiom-phase1.pdf` (at the repo root) is the consolidated
  Phase 1 paper built from `phase1/paper/main.tex` and the outputs under
  `phase1/outputs/`. This scope document should be read together with that
  paper and `phase1/CLAIMS.md` to understand what Phase 1 does and does not
  assert.
