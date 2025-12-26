# Origin Axiom — Phase 2  
## Claims and Supporting Artifacts

This document enumerates **all scientific claims made in Phase 2** of the Origin Axiom project
and maps each claim to **explicit, reproducible artifacts**.

No claim is valid unless it is supported by at least one artifact listed here.

---

## Claim Structure and Rules

Each claim in Phase 2:

- is limited in scope to **existence, robustness, or consistency**,
- avoids assertions of uniqueness, truth, or empirical confirmation,
- is supported by one or more **canonical figures** generated via Snakemake,
- is traceable to specific code paths and configuration parameters.

Claims are numbered for cross-referencing in the paper.

---

## Claim 2.1 — Existence of a Vacuum Energy Residual

**Statement**

Assuming the Origin Axiom, a QFT-inspired mode-sum model generically exhibits a **non-zero
vacuum energy residual** due to incomplete destructive interference.

This residual persists even in the absence of fine-tuning and is enforced by a global
non-cancellation constraint.

**Supporting Artifacts**

- **Figure A** — `figA_mode_sum_residual.pdf`
- Code:
  - `src/phase2/modes/mode_model.py`
  - `src/phase2/modes/run_mode_sum.py`
- Configuration:
  - `config/phase2.yaml` → `model.epsilon`, `mode_sum.*`

---

## Claim 2.2 — Robustness Under Parameter Variation

**Statement**

The vacuum energy residual enforced by the Origin Axiom is **robust** under controlled
variation of key model parameters, including:

- the global non-cancellation floor ε,
- the ultraviolet cutoff,
- the number of contributing modes.

No pathological sensitivity or fine-tuned behavior is observed across the explored ranges.

**Supporting Artifacts**

- **Figure B** — `figB_scaling_epsilon.pdf`
- **Figure C** — `figC_scaling_cutoff.pdf`
- **Figure D** — `figD_scaling_modes.pdf`
- Code:
  - `src/phase2/modes/run_sweep.py`
  - `src/phase2/modes/mode_model.py`
- Configuration:
  - `config/phase2.yaml` → `sweeps.*`

---

## Claim 2.3 — Cosmological Viability of the Residual

**Statement**

When interpreted as an effective vacuum energy density and inserted into standard flat
FRW cosmology, the Origin-Axiom residual produces **Λ-like late-time accelerated expansion**.

This behavior arises without modification of the Einstein field equations and without
introducing new gravitational dynamics.

**Supporting Artifacts**

- **Figure E** — `figE_frw_comparison.pdf`
- Code:
  - `src/phase2/cosmology/run_frw.py`
  - `src/phase2/modes/mode_model.py`
- Configuration:
  - `config/phase2.yaml` → `cosmology.*`, `calibration.*`

---

## Explicit Non-Claims

Phase 2 explicitly does NOT claim:

- a derivation of the observed value of the cosmological constant,
- identification of the microscopic origin of the interference phase,
- resolution of the cosmological constant problem in a definitive sense,
- modification of general relativity or gravitational dynamics,
- connections to Standard Model or flavor physics.

These exclusions are binding and intentional.

---

## Claims-to-Paper Mapping

The Phase 2 paper must map claims as follows:

| Paper Section | Claim(s) Addressed |
|--------------|--------------------|
| Section 3    | Claim 2.1          |
| Section 4    | Claim 2.2          |
| Section 5    | Claim 2.3          |

No additional claims may appear in the paper.

---

## Summary

Phase 2 makes **three and only three claims**, each supported by reproducible numerical
artifacts. Together, these claims establish that the Origin Axiom can naturally give rise
to a small, positive vacuum energy residual with viable cosmological consequences, while
remaining agnostic about deeper theoretical origins.