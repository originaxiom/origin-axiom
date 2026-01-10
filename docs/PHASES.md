# Phases

This repository is organized as a phased program. Each phase must declare scope and non-claims, register a finite set of claims, and provide reproducible artifacts as evidence. Phase 0 sets the governance and corridor method; Phases 1–5 are the canonical physics layers built on top of it. Stage 2 lives downstream as diagnostic belts and is not itself a Phase.

## Phase 0 — Governance and Corridor Method (meta-phase)

**Purpose:** define the discipline that prevents drift:
- claim taxonomy (what we are and are not claiming),
- artifact schema standards,
- the “theta corridor” narrowing concept (filters plus ledger),
- reproducibility contracts (what is tracked vs regenerated),
- failure modes and falsifiability rules.

**Outputs:** schemas, filters, and a paper skeleton describing the method, not physics results.

**Done when:**
- corridor schema and filter schema are stable,
- claim types and evidence requirements are explicitly documented,
- phase gates (what it means for a Phase to be “locked”) are defined,
- failure and retirement rules are written down.

## Phase 1 — Toy ensembles (locked)

**Purpose:** test whether a non-cancelling residue can be defined and measured in controlled toy ensembles, without any cosmology or Standard Model interpretation.

**Allowed claim types:** existence, robustness, and scaling of a residue in toy domains only.

**Canonical artifacts:**
- Phase 1 paper in `phase1/paper/`,
- canonical figures in `phase1/outputs/figures/`,
- any auxiliary tables listed in the Phase 1 reproducibility appendix.

**Status:** Phase 1 is locked. No new physics claims are added; only minor errata or formatting fixes are allowed.

## Phase 2 — Mode-sum model + FRW comparison (bounded viability checks)

**Purpose:** show that the residue mechanism survives a stricter mode-sum construction and can be compared against FRW-style observables without overclaiming full cosmology.

**Allowed claim types:**
- existence and robustness of the residue within the mode-sum model,
- bounded FRW-style viability statements formulated as toy diagnostics,
- explicitly non-cosmological interpretations unless otherwise stated and gated.

**Canonical artifacts:**
- Phase 2 paper in `phase2/paper/`,
- canonical figures in `phase2/outputs/figures/`,
- mode-sum and FRW-diagnostic tables in `phase2/outputs/tables/` as referenced by the paper.

**Status:** under audit. Claims are constrained by the Phase 0 governance rules and may be tightened but not expanded without new gated rungs.

## Phase 3 — Mechanism module

**Purpose:** lock a baseline non-cancellation floor on a global amplitude and provide binding-style diagnostics at the mechanism level. Phase 3 in the canonical tree is about the mechanism module only; flavor-sector work is archived separately.

**Allowed claim types:**
- mechanism-level existence and robustness statements for the locked non-cancellation floor,
- diagnostic statements about how the mechanism behaves across the theta grid,
- no corridor narrowing and no flavor calibration in canonical `phase3/`.

**Canonical artifacts:**
- Phase 3 paper `phase3/artifacts/origin-axiom-phase3.pdf`,
- mechanism-level tables in `phase3/outputs/tables/`,
- any additional artifacts referenced in the Phase 3 claims appendix.

**Archived flavor add-on:** past flavor-sector calibration attempts live under `experiments/phase3_flavor_v1/` and are explicitly non-canonical. They may inspire future work but do not register Phase 3 claims.

**Status:** active. The mechanism module is part of Stage I and is the upstream source for FRW-style and interface layers.

## Phase 4 — FRW toy diagnostics (stub)

**Purpose:** map Phase 3 outputs into FRW-style toy backgrounds and viability masks, and provide a data-probe hook without claiming real-world cosmology or data fits.

**Allowed claim types:**
- purely toy-level FRW diagnostics,
- statements about internal consistency of masks and probes on the theta grid,
- no real-data claims and no cosmological parameter inference.

**Canonical artifacts (stub):**
- Phase 4 paper skeleton in `phase4/paper/`,
- FRW masks and probe tables in `phase4/outputs/tables/`,
- any figures explicitly referenced by the paper.

**Status:** diagnostic stub. It is part of Stage I, but its claims are tightly scoped and remain toy-level until a future rung widens them through explicit gates.

## Phase 5 — Interface and sanity layer

**Purpose:** read locked Phase 3 and Phase 4 outputs and emit interface summaries and sanity tables that make the program inspectable as a whole. Phase 5 must not introduce new mechanism or cosmology claims.

**Allowed claim types:**
- interface-level summaries and consistency checks,
- sanity dashboards and cross-phase bookkeeping,
- no new physics content beyond what is already claimed in Phases 1–4.

**Canonical artifacts (early rungs):**
- Phase 5 paper skeleton in `phase5/paper/`,
- interface and sanity tables in `phase5/outputs/tables/`,
- any “dashboard-style” figures explicitly referenced by the paper.

**Status:** early rungs (0–1). The layer exists to make the program legible and check internal consistency rather than to extend physics scope.

## Stage 2 — Diagnostic belts (non-canonical)

Stage 2 lives under `stage2/` and is strictly downstream of Phases 3 and 4. It adds diagnostic belts over existing artifacts rather than new physics layers.

Current belts include:
- `stage2/frw_corridor_analysis` — FRW corridor families and robustness,
- `stage2/mech_measure_analysis` — mechanism and measure diagnostics over Phase 3 tables,
- `stage2/joint_mech_frw_analysis` — joint mech–FRW grid and correlation analysis,
- `stage2/frw_data_probe_analysis` — audit of FRW data-probe hooks.

Stage 2 is non-canonical until specific rungs are promoted into phase papers through explicit gates documented elsewhere (for example, promotion gates under `docs/`). Stage 2 must not silently extend the Phase claims.

## Next phases (Stage II, future)

Any future phases beyond Phase 5 (Stage II) must:
1) declare scope and non-claims,
2) define canonical artifacts,
3) add claim IDs to the global index,
4) obey all Phase 0 governance rules,
5) specify how they depend on or supersede existing Stage I and Stage 2 structures.

