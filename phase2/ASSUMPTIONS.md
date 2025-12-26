# Origin Axiom — Phase 2  
## Explicit Assumptions

This document enumerates **all assumptions** made in Phase 2 of the Origin Axiom project.
Any assumption not listed here is considered **out of scope** or **not assumed**.

These assumptions are binding for all code, figures, and claims in this phase.

---

## A1. Validity of the Origin Axiom (Interface Assumption)

Phase 2 assumes the validity of the **Origin Axiom** introduced and demonstrated in Phase 1:
that global destructive cancellation of certain quantities is prohibited below a fixed
non-zero floor.

- The axiom is treated as a **global constraint**, not a local dynamical law.
- The axiom is not derived, justified, or explained further in Phase 2.
- Phase 2 does not depend on Phase 1 code or outputs at runtime.

This assumption is inherited and not re-examined.

---

## A2. Mode-Sum as a QFT-Inspired Approximation

Vacuum energy is modeled using a **finite mode-sum approximation** intended to capture
qualitative features of quantum field theoretic zero-point energies.

Assumptions include:

- Modes are treated as independent contributors to vacuum energy.
- Contributions may partially cancel through phase interference.
- The model is not claimed to be a complete or renormalized QFT.

This approximation is used solely to test **existence and robustness**, not to reproduce
microscopic field dynamics.

---

## A3. Global Non-Cancellation Floor (ε)

A fixed, positive non-cancellation floor ε is assumed.

- ε is treated as a **model parameter**, not a derived constant.
- ε enforces a lower bound on net cancellation.
- ε is dimensionless in code units and has no intrinsic physical identification in Phase 2.

Phase 2 explores behavior under variation of ε but does not explain its origin.

---

## A4. Phase Interference Parameter

The model assumes the existence of a phase or interference parameter that prevents
exact destructive cancellation.

- The phase is treated as generic and abstract.
- No identification with known physical phases (e.g., CP, flavor, neutrino mixing) is made.
- The phase may be rational, irrational, or fixed by construction.

Its sole role is to enable incomplete cancellation under the axiom.

---

## A5. Finite Cutoff and Finite Number of Modes

All calculations assume:

- a finite ultraviolet cutoff,
- a finite number of contributing modes.

These are **regulators**, not physical claims.

Phase 2 investigates sensitivity to these choices but does not assume their physical reality.

---

## A6. Determinism and Numerical Idealization

Numerical simulations assume:

- deterministic floating-point arithmetic,
- controlled pseudo-randomness via explicit seeds,
- absence of numerical noise beyond floating-point precision.

No claim is made about numerical exactness beyond machine precision.

---

## A7. Interpretation as Effective Vacuum Energy

When used in cosmological calculations, the vacuum energy residual is interpreted as an
**effective vacuum energy density**.

- This interpretation is phenomenological.
- No claim is made that the residual corresponds to a fundamental cosmological constant.
- The mapping from residual to cosmological parameters is explicit and declared in configuration.

---

## A8. Standard FRW Cosmology

Cosmological implications are evaluated using **standard flat FRW equations**.

Assumptions include:

- General relativity is valid at cosmological scales.
- No modification of Einstein’s equations is introduced.
- The residual enters only as an effective vacuum energy density.

Early-universe physics (inflation, reheating, phase transitions) is not modeled.

---

## A9. Late-Time Focus

Phase 2 focuses on **late-time cosmology**.

- The residual is assumed to be dynamically irrelevant at early times.
- Possible evolution of ε or phase parameters is not considered.
- Constraints from BBN, CMB, or structure formation are not evaluated.

This restriction is intentional.

---

## A10. Global (Non-Local) Character

The Origin Axiom is assumed to be **global in character**.

- Local enforcement mechanisms are not specified.
- Compatibility with locality or microcausality is not addressed.
- Possible quantum-gravitational origins are deferred.

This is acknowledged as a limitation, not a flaw.

---

## Summary of Assumptions

Phase 2 assumes:
- a global non-cancellation axiom,
- a finite mode-sum approximation,
- an abstract phase interference mechanism,
- standard cosmological dynamics,
- and a phenomenological interpretation of residual vacuum energy.

No assumption beyond these is required for Phase 2 claims.