# Phase 2 Approximation Contract
Origin Axiom — Phase 2 (Vacuum residual + scaling + FRW implication)

## Purpose
Phase 2 is a *controlled toy approximation* meant to test one narrow statement:

> If a global non-cancellation constraint (the “Origin Axiom”) prevents exact cancellation of large vacuum-like contributions, then a small positive residual generically remains; that residual exhibits stable scaling under parameter sweeps; and, when interpreted as an effective vacuum term, it produces late-time acceleration in a standard FRW model.

This is **not** a full quantum field theory derivation, and it does **not** identify the physical source of the phase offset or connect to Standard Model flavor physics.

---

## Scope Allowed in Phase 2
Phase 2 is allowed to claim:
1. A residual “vacuum-like” quantity remains after near-cancellation, due to the axiom (global constraint).
2. The residual behaves stably under sweeps (ε, cutoff choice/value, number of modes / volume proxy).
3. A standard FRW model responds as expected when the residual is interpreted as an effective vacuum term using an explicit mapping knob.

Phase 2 is *not* allowed to claim:
- the microscopic origin of the phase (θ, CKM/PMNS, etc.),
- definitive solution of the cosmological constant problem,
- a full QFT renormalization procedure,
- a UV-complete theory of quantum gravity.

---

## What the Model Is (Mathematical Object)
### 1) Mode ensemble
We consider a finite set of modes indexed by k = 1..N.

Each mode contributes a complex phasor:
- amplitude weight: w_k (a real scalar; may encode cutoff weighting),
- phase: φ_k (model-controlled phase prescription).

Define the total complex amplitude:
\[
A \equiv \sum_{k=1}^{N} w_k\,e^{i\phi_k}.
\]

The “residual” reported by the code is:
- `residual_raw = |A_raw|`
- `residual_constrained = |A_constrained|`

(“Raw” means before applying the axiom; “constrained” means after applying the axiom rule below.)

### 2) Cutoff / weighting
A cutoff scheme is implemented as a mapping that determines weights w_k and/or truncation:
- Examples: hard cutoff, smooth cutoff, or numeric parameter controlling effective support.
- In Phase 2, this is treated as a **model definition choice**, not as QFT renormalization.

### 3) Phase prescription
Phases φ_k are assigned by a controlled prescription (e.g., deterministic offset, irrational twist, etc.).
In Phase 2, phases are a **parameterized mechanism** to generate near-cancellation without requiring physical identification.

---

## Option A (Chosen): Generalized Origin Axiom as a Global Non-Cancellation Constraint
### Axiom (Phase 2 operational form)
There exists a floor parameter ε > 0 such that the system cannot realize a total cancellation below ε, expressed as:
\[
|A| \ge \varepsilon.
\]

Operationally:
- If `|A_raw| >= ε`, the axiom is **silent** (no change).
- If `|A_raw| < ε`, the axiom **acts** and returns a minimally modified configuration such that `|A| = ε` (or `|A| >= ε`), while recording that the constraint was applied.

### What “minimally modified” means in Phase 2
Phase 2 implements a deterministic, auditable rule to enforce the constraint. The exact enforcement mechanism is part of the model definition and is recorded by provenance metadata (constraint applied flag + details).

This is a **global** axiom: it constrains the *sum* A, not each mode separately.

---

## Interpretation Layer (Strict Separation)
### Code-level residual
The residual produced by the mode sum is a **dimensionless proxy** in the model’s internal units.

Phase 2 treats this as:
- a stable observable of the toy model,
- subject to scaling tests.

### Mapping to cosmology (explicit knob; not hidden)
To compare with FRW / ΛCDM-style behavior, Phase 2 introduces an explicit mapping knob (example):
- `Omega_L_eff = residual_to_omega_lambda * residual_constrained`

This mapping is:
- **explicit in config**,
- **reported in summary.json**,
- **not claimed as derived** unless/ until a later phase provides that derivation.

Thus FRW results in Phase 2 are: “If the residual is interpreted as an effective vacuum term via an explicit mapping, the qualitative/quantitative FRW response is consistent with late-time acceleration.”

---

## Scaling / Robustness Contract
When sweeps are executed (ε, cutoff, N modes / volume proxy), the workflow must produce:
- a table of sweep points (CSV),
- a scaling plot (PDF),
- a summary.json enumerating sweep values and key results.

Phase 2’s robustness claim is limited to:
- stability under these controlled parameter variations *within the model definition*,
- absence of numerical pathologies or “wild artifacts” in these sweeps.

No claim is made that this replaces QFT renormalization or captures all Standard Model contributions.

---

## Provenance & Reproducibility Contract
Every canonical figure under `outputs/figures/` must be traceable to a run directory:
`outputs/runs/<run_id>/` containing:
- `params.json` (resolved config snapshot),
- `meta.json` (timestamp, git commit if available, platform),
- `pip_freeze.txt`,
- `summary.json`,
- raw arrays (NPZ) and tables (CSV),
- per-run figure PDFs.

Snakemake is the sole authority for producing canonical figures:
manual figures are not part of the Phase 2 contract.

---

## “No Overreach” Summary (One paragraph)
Phase 2 demonstrates a toy-model mechanism: under a global non-cancellation floor ε acting on a finite mode-sum amplitude, near-cancellation halts at a small residual whose scaling can be tested, and whose FRW implication can be illustrated via an explicit mapping knob. Phase 2 does not identify the physical origin of the phase structure, does not claim UV completeness, and does not claim a definitive solution to the cosmological constant problem.