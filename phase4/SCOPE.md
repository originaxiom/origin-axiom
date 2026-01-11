# Phase 4 Scope (Draft, non-binding)

Title (working): **Phase 4 – Vacuum-to-FRW Consistency and Scale Sanity**

Status: **DRAFT – NOT LOCKED.**  
Nothing in this document is binding until explicitly marked as such in
Phase 0 and Phase 4 claims tables.

## 1. Mission

Phase 4 tests whether the **Phase 3 mechanism vacuum** and its canonical
global amplitude \(A(\theta)\) can be connected, in a structurally
reasonable way, to toy FRW-like cosmological behaviour and vacuum-energy
proxies, while preserving the corridor / ledger semantics of Phase 0.

In plain language:

> Given the vacuum model and non-cancellation floor from Phase 3, can we
> define mappings into FRW-style dynamics or vacuum-energy-like scalars
> that yield a non-empty, non-pathological \(\theta\)-corridor?

## 2. Inputs (conceptual)

From earlier phases:

- **Phase 0**
  - Corridor and ledger semantics (filters, intersection rules).
  - Binding vs. non-binding regime notion and ablation-style expectations.
- **Phase 1**
  - Didactic interference / non-cancellation toy models.
  - Currently treated as conceptual scaffolding only (no binding
    \(\theta\)-constraints) unless later mapped explicitly to canonical
    \(\theta\).
- **Phase 2**
  - Toy vacuum-residue + FRW embedding.
  - Provides design lessons (normalisation, stability), but not binding
    numerical constraints at this stage.
- **Phase 3 (mechanism)**
  - Canonical \(\theta \in [0, 2\pi)\).
  - Unconstrained global amplitude \(A_0(\theta)\).
  - Floor-enforced amplitude \(A(\theta) = \max(A_0(\theta), \varepsilon_{\mathrm{floor}})\).
  - Binding-regime diagnostics and baseline experiments.

## 3. Outputs (conceptual)

Phase 4 is expected to deliver, at minimum:

- One or more **explicit mappings** from \(A(\theta)\) (or a derived
  residue) into:
  - a toy FRW module; and/or
  - a vacuum-energy-like observable.
- A **Phase 4 \(\theta\)-filter** (even if broad), or a documented
  conclusion that all investigated mappings lead to empty / pathological
  corridors.
- A Phase 4 paper that:
  - clearly states scope and non-claims;
  - documents mappings, diagnostics, and corridor behaviour;
  - fits cleanly into the Phase 0 ledger framework.

## 4. What Phase 4 is *not* (high level)

- Not a claim to have derived a full theory of everything.
- Not a full cosmological parameter fit.
- Not a replacement for standard \(\Lambda\)CDM or FRW analyses.
- Not a proof that the Origin Axiom is realised in nature.

A precise list of non-claims lives in `NON_CLAIMS.md`.

## 5. Relation to Phase 0 contract

Phase 4 must:

- Respect the **filter / corridor** semantics of Phase 0.
- Clearly indicate which outputs are:
  - binding filters on canonical \(\theta\), and
  - non-binding diagnostics / illustrations.
- Be compatible with the Phase 0 ledger’s way of ingesting a Phase 4
  \(\theta\)-filter, should we define one.

This scope file will be revised and eventually **locked** once the
Phase 4 design is stable. Until then, it should be treated as a
living, non-binding description of intent.

---

## Companion docs: FRW design, promotion, and Stage 2 diagnostics

For more detailed context on how this Phase 4 scope sits inside the broader FRW
and Stage 2 structure, the following documents are relevant:

- `FRW_TOY_DESIGN.md`, `FRW_DATA_DESIGN.md`, and `FRW_SYNTHESIS.md` describe the
  internal design of the FRW toy background, the data-probe layer, and how
  these pieces are meant to be synthesised inside Phase 4. They refine this
  scope but do not expand its claims.

- `docs/FRW_CORRIDOR_PROMOTION_GATE_v1.md` defines the governance gate for any
  future promotion of Stage 2 FRW corridor results into Phase 4/5 text or
  figures. Until that gate is explicitly passed, Stage 2 FRW diagnostics remain
  downstream-only and must not be described as physical predictions.

- `phase4/docs/PHASE4_FRW_PROMOTION_DESIGN_v1.md` records a design-level plan
  for which Stage 2 FRW, mech/measure, joint mech–FRW, and FRW data-probe
  artifacts might eventually be used in Phase 4/5 text under the promotion
  gate, without yet touching the LaTeX.

- `stage2/docs/STAGE2_FRW_CORRIDOR_SUMMARY_v1.md` and
  `stage2/docs/STAGE2_FRW_DATA_PROBE_SUMMARY_v1.md` summarise the Stage 2 FRW
  corridor and FRW data-probe belts as **diagnostic** analyses built strictly
  on top of Phase 4 FRW outputs. They support interpretation of Phase 4 but do
  not change Phase 4 claims in place.
