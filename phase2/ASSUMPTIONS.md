# Phase 2 — Assumptions Register

This document enumerates **all assumptions** made in Phase 2 of the Origin Axiom project.

**Rule:** Any assumption not listed here is **not assumed** and must not appear implicitly
in code, figures, or text.

Assumptions are grouped into:
- (I) interface assumptions inherited from Phase 1,
- (II) toy-model assumptions specific to Phase 2,
- (III) interpretation assumptions used only for the FRW wrapper.

---

## I. Interface assumptions (inherited; not re-examined)

### A1 — Origin Axiom is treated as an interface constraint

Phase 2 assumes the Origin Axiom introduced in Phase 1:

- There exists a fixed ε > 0 such that the relevant global cancellation quantity is constrained
  away from zero (a global non-cancellation floor).

Phase 2 does **not** derive, justify, or strengthen this axiom. Phase 2 does not depend on
Phase 1 code or outputs at runtime.

---

## II. Phase-2 toy-model assumptions (mode-sum proxy)

### A2 — Finite mode-sum is a QFT-inspired proxy

Vacuum contributions are modeled by a finite sum over modes intended to capture qualitative
features of zero-point energies and cancellation.

- The model is **not** claimed to be a complete or renormalized QFT.
- The model is used only to test **existence** and **robustness** of a residual under a
  global non-cancellation constraint.

### A3 — Global non-cancellation floor ε is a model parameter

- ε is treated as a **dimensionless control parameter** in code units.
- ε is not derived from first principles in Phase 2.
- Phase 2 explores sensitivity to ε via explicit sweeps.

### A4 — Abstract phase / interference parameter

The model assumes a phase/interference mechanism that frustrates perfect destructive
cancellation.

- The phase parameter is treated as generic and abstract.
- No identification with known physical phases (CP, flavor, neutrino mixing, etc.) is made.

### A5 — Finite regulators (cutoff and number of modes)

All calculations assume:

- a finite ultraviolet cutoff,
- a finite number of contributing modes.

These are treated as **regulators** (model inputs) rather than physical claims.

### A6 — Numerical determinism

- Runs are deterministic up to floating-point precision.
- Any pseudo-randomness (if present) is controlled by an explicit seed in `config/phase2.yaml`.

---

## III. Interpretation assumptions (FRW wrapper only)

### A7 — Residual interpreted as an effective vacuum-energy component

For the cosmology wrapper, the residual is interpreted as an **effective Λ-like component**.

- This interpretation is phenomenological.
- No claim is made that the residual equals the fundamental cosmological constant.
- Any mapping/calibration is declared explicitly in configuration.

### A8 — Standard flat FRW equations

Cosmological implications are evaluated using **standard flat FRW dynamics**.

- General relativity is assumed valid at cosmological scales.
- No modification of Einstein’s equations is introduced.
- The residual enters only as an effective vacuum-energy term.

### A9 — Late-time focus

Phase 2 focuses on late-time behavior.

- Early-universe physics (inflation, BBN, reheating, phase transitions) is not modeled.
- Data confrontation (CMB, BAO, SNe Ia) and structure formation are out of scope.

### A10 — Global/non-local character (acknowledged limitation)

- The Origin Axiom is treated as global in character.
- No local enforcement mechanism is specified.
- Locality/microcausality and quantum-gravity origins are deferred.

---

## Summary

Phase 2 assumes a global non-cancellation axiom (interface), a finite mode-sum proxy
(toy model), and a standard FRW wrapper (interpretation) to assess **existence**,
**robustness**, and **cosmological viability** only.