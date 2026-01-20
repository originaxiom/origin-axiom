# Stage II – External Cosmology Hosts Design (v1, conceptual)

This document sketches a Stage II layer that would interface the Origin Axiom vacuum and mechanism story with external cosmology hosts (e.g. CLASS, CCL, Cobaya, CosmoSIS) in a way that respects the Phase 0 governance contract. It is a design note only: no Stage II code exists yet and no contact with real cosmological datasets is made inside Stage I.

---

## 1. Relationship to Stage I and Stage 2

Stage I (Phase 0–5) and Stage 2 currently implement a closed, reproducible sandbox:

- Phase 0–2: governance, toy ensembles, and a mode-sum + bounded FRW viability bridge.
- Phase 3: a mechanism module that produces θ-dependent vacuum amplitudes and bounds.
- Phase 4: a stylised FRW toy universe fed by the mechanism.
- Phase 5: an interface and sanity layer over the existing artifacts.
- Stage 2: downstream diagnostic belts (FRW corridors, mech/measure analysis, joint mech–FRW correlations, FRW data probes, doc audit, and a simple empirical background anchor).

Within this sandbox the axiom is interrogated without relying on external codes or real data. Stage II is explicitly defined as a *separate* layer that may:

- use θ-dependent outputs from Phase 3/4 as inputs,
- call external cosmology codes as host physics engines,
- and, eventually, touch real datasets under a dedicated “data gate”.

No Stage II result is allowed to modify Phase 0–5 claims or Stage 2 interpretations unless it passes a Phase 0–style promotion gate.

---

## 2. Scope and non-claims of Stage II

The intended scope of Stage II is:

- to provide a controlled environment where θ-dependent vacuum structures from Stage I can be mapped into standard cosmological parameterisations and passed through external hosts to generate background and linear-theory observables, and
- to ask disciplined questions about whether any θ-regions are compatible with chosen empirical anchors.

Stage II explicitly does **not**:

- redefine the axiom or its Phase 0 governance,
- claim to derive FRW or ΛCDM from first principles,
- claim full fits to CMB/BAO/SN data without explicit, tightly scoped data gates and independent replication,
- retroactively upgrade Stage I toy diagnostics into data-backed claims.

At v1, Stage II is a design target only. Any concrete implementation must create new, clearly marked code and docs, and must survive reproducibility checks and external review before influencing the Stage I narrative.

---

## 3. Proposed architecture

The Stage II architecture is layered to preserve separation of concerns.

### 3.1 θ and mechanism layer (upstream inputs)

This layer remains inside Stage I:

- Phase 3 provides θ ↦ vacuum amplitudes and bounds (e.g. E_vac(θ), mech_baseline_*, mech_binding_*).
- Phase 4 provides θ ↦ FRW toy backgrounds (ω_Λ-like quantities, age_Gyr, viability masks).

Stage II is not allowed to modify these definitions; it only reads them as inputs.

### 3.2 Mapping layer: θ → standard cosmological parameters

Stage II introduces a thin mapping layer, conceptually:

- θ (and possibly selected mechanism diagnostics) are mapped into standard cosmological parameters such as (Ω_m, Ω_Λ, H0, w0, wa, ...) or equivalent parameter sets used by the chosen host codes.
- This mapping is where theoretical choices live (e.g. whether θ controls only Ω_Λ, or a combination of vacuum scale and other parameters).

Design requirements for this layer:

- The mapping must be explicitly documented, with scope and non-claims.
- Multiple mapping schemes may be defined and compared; no single choice is assumed to be canonical at the outset.
- The mapping is deterministic and reproducible: given θ and a chosen scheme, it must always produce the same parameter set.

### 3.3 Host layer: external cosmology codes

The host layer wraps external codes such as:

- background and linear-theory engines (e.g. CLASS, CCL, PyCosmo),
- or full pipeline frameworks (e.g. Cobaya, CosmoSIS) if and when warranted.

Design requirements:

- External codes are treated as *black-box physics engines*: given standard cosmological parameters they produce background quantities (H(z), distances, age), linear power spectra, and other derived observables.
- Stage II records exactly which versions of the host codes, parameter files, and compilation options are used.
- Host calls are logged and their outputs are stored as Stage II artifacts (tables and, if needed, figures) separate from Phase 3/4 outputs.

### 3.4 Data and likelihood layer (optional, gated)

A further layer may incorporate real cosmological datasets through likelihood modules (e.g. CMB temperature/polarisation, BAO measurements, SN distance moduli). This layer is the most sensitive and must be protected by a “data gate”.

Design requirements:

- No data likelihoods are called until a dedicated Stage II data-gate contract is written and locked.
- Any data-facing run must record which datasets and likelihood versions are used, and which priors are applied.
- Claims are constrained to modest, audit-friendly forms, such as:
  - “For this θ-mapping scheme, the posterior weight of FRW-viable + data-consistent θ values is negligible/non-negligible.”
- Richer claims (e.g. “best-fit parameter values”, model comparisons) require additional, explicit promotion gates.

---

## 4. Gating and promotion criteria

To prevent Stage II from silently steering Stage I claims, we define ranking and gates.

### 4.1 Internal Stage II diagnostics (default)

Most Stage II outputs are expected to remain internal diagnostics, analogous to Stage 2 belts:

- background consistency checks (e.g. comparison of Phase 4 toy FRW backgrounds with host-computed backgrounds),
- empirical anchor kernels defined in richer observable spaces,
- qualitative assessments of whether θ-regions exist that are not obviously ruled out by simple data cuts.

These results may be summarised in Stage II docs but do not change Phase 4/5 text or figures.

### 4.2 Promotion candidates

A Stage II result becomes a candidate for promotion into Stage 4/5 (or a future dedicated phase) only if:

- it is reproducible under host-version changes and numerical settings,
- it is robust under small changes in the θ → parameter mapping and data cuts,
- it does not rely on fine-tuned, isolated θ points (measure-zero sets),
- it can be stated in a modest and interpretable way consistent with Phase 0 (e.g. “there exists a non-negligible θ corridor that passes specified background and data filters”).

Such candidates must be documented in dedicated “promotion design” docs that play the same role as the FRW promotion design in Phase 4.

### 4.3 Promotion gates

Any actual change to Phase 4/5 claims or figures driven by Stage II must pass through:

- a written promotion gate (Phase 0–style contract) that:
  - cites the Stage II artifacts being relied on,
  - records which mapping schemes and datasets were used,
  - describes robustness checks and negative results,
- updates to `docs/CLAIMS_INDEX.md` and `docs/STATE_OF_REPO.md`,
- and, ideally, independent replication of the Stage II pipeline by a second environment.

Until such gates are written and satisfied, Stage II remains descriptive and exploratory only.

---

## 5. Initial Stage II rung sketch (for future implementation)

If and when Stage II is implemented, an initial rung sequence might be:

- **I1 – background host alignment (no data):**  
  Implement a mapping from θ to an Ω_Λ-like parameter and use an external host (e.g. CLASS or CCL) to compute background quantities (H(z), age, distances) on a θ grid. Compare these to the existing Phase 4 toy FRW outputs as a cross-check.

- **I2 – extended empirical anchors (background only):**  
  Define richer background anchors (e.g. boxes in (Ω_m, Ω_Λ, H0, age)) and study the resulting kernels in θ and FRW spaces, purely at the level of host-computed backgrounds.

- **I3 – linear-theory observables (no data):**  
  Use host codes to compute linear power spectra or CMB angular spectra for θ-mapped parameter sets, comparing shapes to a fiducial ΛCDM model without invoking likelihoods.

- **I4 – gated data contact (prototype):**  
  Under a dedicated data gate, run limited likelihood evaluations for a small set of θ-mapped parameter sets to check for obvious catastrophes. Treat results strictly as diagnostics until promotion criteria are met.

This rung sketch is intentionally conservative: it emphasises background and qualitative shape information before any serious data fitting and keeps Stage II as a layered diagnostic environment rather than a direct claim engine.

---

## 6. Status

As of January 2026 this design note is **conceptual only**. It records how Stage II is intended to sit above Stage I and Stage 2 without altering their current claims. Any concrete Stage II implementation must:

- live in clearly marked Stage II directories or a separate repository,
- include its own alignment and reproducibility docs,
- and pass through explicit Phase 0–style gates before influencing Phase 4/5 text or public-facing narratives.


## Obstruction-program questions for Stage II

Stage II is designed as a host- and data-facing layer on top of the locked Stage I phases and the Stage 2 diagnostic belts. From the obstruction-program perspective, its role is not to assume that reality is literally an obstructed cancellation process, but to ask whether that picture can survive contact with realistic cosmological hosts and data gates in a controlled way.

The central obstruction-program questions for Stage II are:

- Mapping: can the θ-dependent vacuum constructions and non-cancelling floor from Stage I be mapped into standard cosmological parameterisations (for example \{\Omega_{\mathrm{m}}, \Omega_{\Lambda}, H_{0}, n_{\mathrm{s}}, \ldots\}) such that the mapping is mathematically well defined and reproducible across hosts?
- Corridor survival: under such mappings, do any of the θ corridors that survive the Stage 2 FRW viability and empirical-anchoring belts remain non-empty once passed through realistic background solvers and simple data gates, or do they collapse immediately?
- Kernel structure: when non-empty kernels do appear under host-plus-data cuts, are they structured in θ and in the mapped cosmological parameters in a way that is consistent across different host choices, or are they fragile artefacts of one particular mapping or solver?
- θ\* neutrality: do the mapped corridors and kernels treat θ\* as a neutral interior point, a boundary, or a special value, and how sensitive is this behaviour to the details of the host and data choices?
- Negative outcomes: if certain host or data combinations destroy all non-trivial θ corridors, can those failures be turned into precise statements about which obstruction-program variants are ruled out, without overreaching beyond what the Stage I artefacts actually support?

These questions are intentionally phrased as programmatic prompts rather than claims. Implementing them will require explicit host interfaces, reproducible mappings from θ into host parameter spaces, carefully defined data gates, and new promotion contracts. Until those pieces are in place and pass Phase 0 gates, Stage II remains a design-only layer, and any obstruction-program language should be treated as interpretive rather than canonical.
