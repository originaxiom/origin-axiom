# Claims Index

This document is the global map of claims in the Origin-Axiom program. It tells you where to find the canonical statements, what kind of claims each phase is allowed to make, and which artifacts count as evidence. Anything not listed here (or explicitly marked as canonical in the relevant phase) should be treated as suggestive or experimental, not binding.

Phase 0 defines the governance and corridor method; Phases 1–5 are the canonical physics layers; Stage 2 adds downstream diagnostic belts and does not introduce new claims.

---

## Phase 0 — Method and Governance Claims

**Source of truth:** `phase0/CLAIMS.md`

**Scope (summary):**
- Claim types and evidence requirements for the whole program.
- Corridor and filter language (how we narrow or track theta corridors).
- Reproducibility, logging, and retirement rules for phases and rungs.
- Constraints on what later phases are allowed to claim.

Phase 0 does not contain physics results about the universe. Its claims are about method and governance only.

---

## Phase 1 — Toy-Domain Physics Claims (Locked)

**Source of truth:** `phase1/CLAIMS.md` and the Phase 1 paper (`phase1/paper/`)

**Scope (summary):**
- Existence, robustness, and scaling of a non-cancelling residue in toy ensembles.
- Claims restricted to the toy domains and models explicitly defined in Phase 1.

**Canonical artifacts:**
- Phase 1 paper in `phase1/paper/`.
- Figures and tables referenced from the paper, primarily under `phase1/outputs/figures/` and `phase1/outputs/tables/`.

Phase 1 is locked. No new physics claims are added; only errata-level corrections are allowed.

---

## Phase 2 — Mode-Sum + Bounded FRW Diagnostics (Under Audit)

**Source of truth:** `phase2/CLAIMS.md` and the Phase 2 paper (`phase2/paper/`)

**Scope (summary):**
- Existence and robustness of the residue in a stricter mode-sum model.
- Bounded FRW-style viability statements formulated as toy diagnostics.
- Explicit non-cosmological interpretation unless a claim is gated through Phase 0 rules.

**Canonical artifacts:**
- Phase 2 paper in `phase2/paper/`.
- Mode-sum and FRW-diagnostic tables in `phase2/outputs/tables/`.
- Figures referenced by the paper in `phase2/outputs/figures/`.

Phase 2 is under audit. Some claims may be tightened but should not be broadened without new rungs and explicit gates.

---

## Phase 3 — Mechanism Module (Canonical) and Flavor Add-On (Archived)

### 3.1 Canonical Phase 3: Mechanism Module

**Source of truth:** Phase 3 paper claims appendix (`phase3/paper/appendix/A_claims_table.tex`) and `phase3/ROLE_IN_PROGRAM.md`

There is no standalone `phase3/CLAIMS.md` at this rung. The claims live in the paper’s appendix and in the role document.

**Scope (summary):**
- Baseline non-cancellation floor on a global amplitude-like observable.
- Mechanism-level diagnostics and tables over the theta grid.
- No flavor calibration and no corridor narrowing in canonical `phase3/`.

**Canonical artifacts:**
- Phase 3 paper `phase3/artifacts/origin-axiom-phase3.pdf`.
- Mechanism tables in `phase3/outputs/tables/`.
- Any additional artifacts explicitly cited in the Phase 3 claims appendix.

### 3.2 Archived Flavor-Sector Experiment (Non-Canonical)

**Source of truth for archive status:** `experiments/phase3_flavor_v1/ARCHIVE_STATUS_v1.md`

**Scope (summary):**
- Historical flavor-sector calibration attempts (CKM/PMNS-based).
- Useful as an experiment log and idea reservoir.

These artifacts are explicitly non-canonical. They do not register Phase 3 claims. Any future reintroduction of flavor-sector structure must:
1. Be documented in `docs/PHASES.md` and `docs/STATE_OF_REPO.md`.
2. Declare its own scope, non-claims, artifacts, and gates.
3. Pass through the same Phase 0 governance discipline as other phases.

---

## Phase 4 — FRW Toy Diagnostics (Stub)

**Source of truth:** Phase 4 paper skeleton in `phase4/paper/` and `phase4/OVERVIEW.md`

**Scope (summary):**
- Toy-level FRW masks and viability diagnostics derived from Phase 3 outputs.
- Internal consistency statements about FRW-style masks and probes on the theta grid.
- No real-data claims and no cosmological parameter inference at this rung.

At present there is no separate `phase4/CLAIMS.md`. Any Phase 4 claims are template-level and live in the paper skeleton and its referenced tables. Before Phase 4 registers full claims, it must:
- Declare claim IDs and evidence in a claims appendix.
- Be aligned with Phase 0 governance and corridor language.

---

## Phase 5 — Interface and Sanity Layer (Early Rungs)

**Source of truth:** Phase 5 paper skeleton in `phase5/paper/` and `phase5/SCOPE.md`

**Scope (summary):**
- Interface-level summaries of locked Phase 3 and Phase 4 artifacts.
- Sanity dashboards and cross-phase consistency checks.
- No new physics claims beyond what is already registered in Phases 1–4.

At present there is no standalone `phase5/CLAIMS.md`. Any claims live as interface statements in the paper and associated tables. Full Phase 5 claims will require:
- A claims appendix with IDs and explicit pointers into Phase 1–4 artifacts.
- Confirmation that no new mechanism or cosmology content is being quietly introduced.

---

## Stage 2 — Diagnostic Belts (Non-Canonical)

Stage 2 adds diagnostic belts over existing Phase 3/4 artifacts and lives under `stage2/`. It does not introduce new physics claims; instead it refines how we understand and stress-test existing outputs.

Current belts include:
- `stage2/frw_corridor_analysis`: FRW corridor families, overlaps, robustness, and basic visualization.
- `stage2/mech_measure_analysis`: inventory of Phase 3 tables and diagnostics over measure-like columns.
- `stage2/joint_mech_frw_analysis`: joint theta grid and correlation analysis linking mechanism outputs and FRW diagnostics.
- `stage2/frw_data_probe_analysis`: audit of FRW data-probe hooks versus viability masks.

Stage 2 results may motivate updates to phase papers or new claims, but promotion must be explicit:
- via documented promotion gates (for example under `docs/`),
- with changes to the relevant phase claims appendix and this index.

Until such promotion happens, Stage 2 is strictly diagnostic and non-canonical.

---

## How to Use This Index

When you encounter a claim (in a README, a figure caption, or a talk slide), you should be able to trace it back here:

1. Identify which phase the claim belongs to.
2. Find the corresponding claims ledger (Phase claims file or paper appendix).
3. Verify that:
   - the claim is explicitly stated,
   - the evidence artifacts are present and reproducible,
   - the claim type is allowed for that phase under Phase 0 governance.

If you cannot map a statement to this index, treat it as non-canonical. Either it belongs in an experiment or Stage 2 diagnostic, or this document needs to be updated as part of a gated rung.

