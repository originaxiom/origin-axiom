# Origin Axiom

A disciplined, multi-phase attempt to see whether a single **non-cancelling phase twist** (θ\* or a closely related structure) could sit at the root of vacuum, fields, and large-scale structure – and if not, to learn *precisely why not* in a way that is reusable for future work.

This repo is the **Stage I** program: a gated, reproducible ladder of phases, each with:

- a clearly declared scope and *non-claims*,
- explicit, versioned artifacts (papers, tables, figures),
- and a governance layer (Phase 0) that constrains what we are allowed to say.

The goal is *not* to hand-wave a “theory of everything”. The goal is to build a **testable, falsifiable narrative** from:

> axiom → toy ensembles → mechanisms → FRW-style diagnostics → interfaces & sanity checks

and to do so in a way that an external collaborator could clone, run, and audit.

---

## 0) Phased program at a glance

Each Phase is a rung with its own paper, gates, and claims discipline; Stage 2 belts sit downstream of Phases 3/4 as diagnostics.

- **Phase 0 – Governance & Specification (Locked)**  
  - Define what “claims” even mean in this program.
  - Specify locking, gating, and reproducibility standards.
  - Declare how we handle legacy work, retired ideas, and “tempting but under-evidenced” patterns.

- **Phase 1 – Toy Ensembles (Locked)**  
  - Construct and stress-test toy ensembles that can support or falsify a non-cancelling phase twist.
  - Establish that a residue can exist and be robust/scalable in toy models.

- **Phase 2 – Mode-Sum + Bounded FRW Viability (Under Audit)**  
  - Build a mode-sum model with a bounded FRW-style viability notion (toy cosmology, not full data contact).
  - Provide the first bridge from mechanism-like amplitudes to FRW-like observables.

- **Phase 3 – Mechanism Module (Active)**  
  - Treat Phase 3 as a *mechanism* for enforcing a non-cancellation floor, not a flavor calibration phase.
  - Provide binding-style diagnostics and a clean “non-cancelling floor” over θ.
  - No flavor calibration or corridor narrowing in the canonical Phase 3.

- **Phase 4 – FRW Toy Diagnostics (Diagnostic Stub)**  
  - Map Phase 3 outputs into FRW-style toy backgrounds and viability masks.
  - Provide a data-probe hook without claiming real-data contact.

- **Phase 5 – Interface & Sanity Layer (Rung 0–1)**  
  - Read locked Phase 3/4 outputs and emit interface summaries/sanity tables.
  - No new mechanism or cosmology claims.

- **Stage 2 – Diagnostic Belts (In Progress)**  
  - Downstream analyses over Phase 3/4 outputs: FRW corridor, mech/measure, joint mech–FRW, FRW data-probe, θ★ diagnostics, empirical anchors/hosts, and documentation/paper-audit belts.
  - Non-canonical until promoted.

Flavor-sector calibration work lives under [`experiments/phase3_flavor_v1/`](experiments/phase3_flavor_v1/) as an archived add-on. The canonical Phase 3 is the mechanism module described above.

---

## 1) What this is *about*

**Core question:**  
Is there a *single*, structurally inevitable way for the vacuum to “want” to twist that can survive being projected into different levels (toy ensembles, mechanism module, FRW-like backgrounds) without being tuned into existence?

We are not trying to “fit the universe” in one shot. We are trying to:

- formulate a **coherent axiom** about non-cancellation,
- **stress-test** it in toy ensembles (Phase 1),
- encode it as a **mechanism** with explicit diagnostics (Phase 2/3),
- and **map** that into FRW-style toy cosmology (Phase 4),

while being honest about what is locked, what is provisional, and what is archived.

The non-cancelling twist is currently represented by a candidate θ\* linked to the golden ratio via φ^φ. The program does **not** assume θ\* is “the answer”; it asks whether θ\* (or a nearby structure) can:

- sit at the root of toy vacuum constructions,
- survive through mechanism-level diagnostics,
- and remain compatible with FRW-style viability corridors,

or whether it fails in a way that tells us something non-trivial.

Phase 0 enforces that we:

- track **what is claimed** vs **what is merely suggestive**,
- keep a clean separation between **canonical Phases**, **Stage 2 diagnostics**, and **archived experiments**,
- and ensure everything is reproducible from the repo.

---

## 2) Repository structure (Stage I + Stage 2)

See also [`docs/REPO_MAP_AND_ATLAS_v1.md`](docs/REPO_MAP_AND_ATLAS_v1.md) for a more detailed map.

Top-level layout (canonical Phases, Stage 2 belts, and archived experiment):

- [`phase0/`](phase0/) – Governance & specification  
  - Contracts, claims registers, and governance rules.
  - Phase-0 paper lives under [`paper/`](phase0/paper/) and is exported to `artifacts/origin-axiom-phase0.pdf`.

- [`phase1/`](phase1/) – Toy ensembles  
  - Toy constructions and diagnostics.
  - Phase-1 paper under [`paper/`](phase1/paper/) → `artifacts/origin-axiom-phase1.pdf`.

- [`phase2/`](phase2/) – Mode-sum + bounded FRW viability (under audit)  
  - Mode-sum model, FRW-style viability checks, and structural audit material.
  - Paper under [`paper/`](phase2/paper/) → `artifacts/origin-axiom-phase2.pdf`.
  - Audit report under [`audit/`](phase2/audit/) → `phase2/audit/AUDIT_REPORT.md`.

- [`phase3/`](phase3/) – Mechanism module  
  - Mechanism/scalar diagnostics over θ, tables, and mechanism contracts.
  - Paper under [`paper/`](phase3/paper/) → `artifacts/origin-axiom-phase3.pdf`.
  - Mechanism contracts and design notes under [`MECHANISM_CONTRACT.md`](phase3/MECHANISM_CONTRACT.md) and [`design/`](phase3/design/).
  - [`outputs/tables/`](phase3/outputs/tables/) – Mechanism-level tables and diagnostics.  
  - [`ROLE_IN_PROGRAM.md`](phase3/ROLE_IN_PROGRAM.md) – How the mechanism module fits into the overall program.

- [`phase4/`](phase4/) – FRW toy diagnostics (stub)  
  - FRW-like background construction and viability masks.  
  - Shape/data/viability masks live under [`outputs/tables/`](phase4/outputs/tables/).

- [`phase5/`](phase5/) – Interface + sanity layer (rung 0–1)  
  - Interface summaries and sanity checks over locked Phase 3/4 outputs.

- [`stage2/`](stage2/) – Diagnostic belts (downstream, non-canonical)  
  - [`frw_corridor_analysis/`](stage2/frw_corridor_analysis/) – FRW viability/corridor belts.
  - [`mech_measure_analysis/`](stage2/mech_measure_analysis/) – Mechanism/measure belts over Phase 3 tables.
  - [`joint_mech_frw_analysis/`](stage2/joint_mech_frw_analysis/) – Joint mech–FRW θ-grid analysis.
  - [`frw_data_probe_analysis/`](stage2/frw_data_probe_analysis/) – Toy FRW data-probe audit (no real data claims).
  - [`theta_star_analysis/`](stage2/theta_star_analysis/) – θ★ alignment diagnostics on the FRW grid.
  - [`external_cosmo_host/`](stage2/external_cosmo_host/) and [`external_frw_host/`](stage2/external_frw_host/) – empirical anchor and external FRW host belts.
  - doc_repo_audit/ – Local Stage 2 doc-audit scratch directory (see `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md`).

- [`experiments/phase3_flavor_v1/`](experiments/phase3_flavor_v1/) – Archived flavor-sector add-on (non-canonical)  
  - Historical attempt at flavor-sector calibration, explicitly archived.  
  - See [`experiments/phase3_flavor_v1/ARCHIVE_STATUS_v1.md`](experiments/phase3_flavor_v1/ARCHIVE_STATUS_v1.md) for status.

- [`docs/`](docs/) – Global docs and contracts  
  - [`PROJECT_OVERVIEW.md`](docs/PROJECT_OVERVIEW.md) – High-level Stage I overview.  
  - [`PHASES.md`](docs/PHASES.md) – Phase-by-phase definitions.  
  - [`STATE_OF_REPO.md`](docs/STATE_OF_REPO.md) – Current status and claims indexing.  
  - [`CLAIMS_INDEX.md`](docs/CLAIMS_INDEX.md) – Map of claims across phases.  
  - [`FUTURE_WORK_AND_ROADMAP.md`](docs/FUTURE_WORK_AND_ROADMAP.md) – Stage II / future directions.  

- [`stage2/docs/`](stage2/docs/) – Stage 2 specific docs:  
  - [`STAGE2_OVERVIEW_v1.md`](stage2/docs/STAGE2_OVERVIEW_v1.md) – narrative overview of Stage 2 as a diagnostic belt.
  - [`STAGE2_BELT_OVERVIEW_v1.md`](stage2/docs/STAGE2_BELT_OVERVIEW_v1.md) – catalogue of all belts (FRW, mech/measure, joint, data, θ★, empirical anchors/hosts, doc/paper audits).
  - [`STAGE2_FRW_CORRIDOR_SUMMARY_v1.md`](stage2/docs/STAGE2_FRW_CORRIDOR_SUMMARY_v1.md) – FRW corridor belt summary.
  - [`STAGE2_MECH_MEASURE_SUMMARY_v1.md`](stage2/docs/STAGE2_MECH_MEASURE_SUMMARY_v1.md) – mechanism/measure belt summary.
  - [`STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md`](stage2/docs/STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md) – joint mech–FRW belt summary.
  - [`STAGE2_FRW_DATA_PROBE_SUMMARY_v1.md`](stage2/docs/STAGE2_FRW_DATA_PROBE_SUMMARY_v1.md) – FRW data-probe audit summary.
  - [`STAGE2_DOC_AUDIT_SUMMARY_v1.md`](stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md) – documentation/repo-audit belt and CSV usage.
  - [`STAGE2_ARCHIVE_STATUS_v1.md`](stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md) – map of canonical vs archived areas.
  - empirical-anchor, external-host, and paper-audit docs (see the belt catalogue for details).

- [`PROGRESS_LOG.md`](PROGRESS_LOG.md) – Chronological log of work.  
  - Early entries may reference legacy paths (`src/`, `data/`, `figures/`); see the note at the top.  
  - New entries should reference the current Phase/Stage structure.

---

## 3) How to run things (very short version)

For full details, see [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) and the phase papers’ appendices. This section is just a quick orientation.

### 3.1 Phase 0–2 papers and contracts

- **Phase 0**  
  - Paper: see `phase0/paper/` for LaTeX, `artifacts/origin-axiom-phase0.pdf` for the compiled PDF.
  - Contracts and claims: `phase0/CLAIMS.md`, `phase0/GOVERNANCE.md`, and related docs.

- **Phase 1**  
  - Paper: `phase1/paper/` → `artifacts/origin-axiom-phase1.pdf`.
  - Toy ensemble code and figures live under `phase1/src/` and `phase1/outputs/`.

- **Phase 2** (under audit)  
  - Paper: `phase2/paper/` → `artifacts/origin-axiom-phase2.pdf`.
  - Claims and contracts: `phase2/CLAIMS.md`, `phase2/SCOPE.md`, `phase2/ASSUMPTIONS.md`, `phase2/APPROXIMATION_CONTRACT.md`.
  - Structural audit: `phase2/audit/AUDIT_REPORT.md` (historical snapshot), plus `phase2/PHASE2_ALIGNMENT_v1.md` for how it lines up with the current claims and paper.

### 3.2 Phase 3–5 mechanism, FRW stub, and interface

- **Phase 3 – Mechanism module**  
  - Paper: `phase3/paper/` → `artifacts/origin-axiom-phase3.pdf`.  
  - Mechanism contracts: `phase3/MECHANISM_CONTRACT.md`, `phase3/SCOPE.md`, `phase3/ROLE_IN_PROGRAM.md`.  
  - Outputs: `phase3/outputs/tables/` for mechanism diagnostics (e.g. `mech_baseline_scan.csv`, `mech_binding_certificate.csv`).  
  - Design notes: `phase3/design/` for rung-level mechanism refinements (non-binding).

- **Phase 4 – FRW toy diagnostics (stub)**  
  - Paper (stub): `phase4/paper/` → `artifacts/origin-axiom-phase4.pdf`.  
  - FRW masks and probes: `phase4/outputs/tables/phase4_F1_frw_*_mask.csv`.  
  - FRW promotion design: `phase4/docs/PHASE4_FRW_PROMOTION_DESIGN_v1.md`.  
  - Design notes: `phase4/design/` for mapping families, FRW toy design, data-probe design, and Phase 3–4 interface sketches.

- **Phase 5 – Interface and sanity layer (rung 0–1)**  
  - Paper (rung 0–1): `phase5/paper/` → `artifacts/origin-axiom-phase5.pdf`.  
  - Scope and non-claims: `phase5/SCOPE.md`, `phase5/NON_CLAIMS.md`, `phase5/ROLE_IN_PROGRAM.md`.  
  - Early interface/sanity design: `phase5/PHASE5_VISION_RUNG0.md`.

You can invoke them directly when working on a particular phase. Consult the script headers and the Phase papers’ reproducibility appendices for exact commands.

### 3.3 Stage 2 diagnostics (downstream only)

Stage 2 work lives under [`stage2/`](stage2/) and is **strictly downstream** of the Phase 3/4 artifacts. It does not modify Phase papers or claims. See the local README or docs within each Stage 2 module for entry points.

Current belts include (all downstream of Phase 3/4):

- [`frw_corridor_analysis/`](stage2/frw_corridor_analysis/) – FRW corridor/viability analysis on the Phase 4 masks.  
- [`mech_measure_analysis/`](stage2/mech_measure_analysis/) – probability-like and measure/flag diagnostics over Phase 3 tables.  
- [`joint_mech_frw_analysis/`](stage2/joint_mech_frw_analysis/) – joint θ-grid and correlation diagnostics combining Phase 3 mechanisms and Phase 4 FRW outputs.  
- [`frw_data_probe_analysis/`](stage2/frw_data_probe_analysis/) – audit of the FRW data-probe hooks (toy-level, no real-data claims).  
- [`theta_star_analysis/`](stage2/theta_star_analysis/) – θ★–FRW alignment diagnostics.  
- [`external_cosmo_host/`](stage2/external_cosmo_host/) and [`external_frw_host/`](stage2/external_frw_host/) – empirical anchor and external FRW host belts.  
- doc_repo_audit/ – local (git-ignored) Stage 2 doc-audit directory (see `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md`).  
- Stage 2 paper-audit docs under [`stage2/docs/`](stage2/docs/) – Phase 0–5 paper audit notes and plans.

Stage 2 results are **non-canonical** until explicitly promoted via Phase 0 governance and a documented gate (e.g. “FRW Corridor Promotion Gate”).

---

## 4) Big questions (and guardrails)

The program is intentionally conservative about what it claims.

We are *not* claiming to have:

- a complete, realistic cosmology,
- a fully justified measure over θ,
- or a data-selected θ\*.

Instead, we are asking:

1. Can we formulate a **non-cancelling axiom** that survives:
   - toy ensembles (Phase 1),
   - mechanism-level encoding (Phase 3),
   - and FRW-style toy diagnostics (Phase 4)?

2. Does this axiom force a **narrow corridor** in θ that remains viable under:
   - changes of toy ensemble,
   - changes of mechanism parameters,
   - and changes of FRW-style diagnostics?

3. Is θ\* ≈ φ^φ **structurally preferred** (e.g. by mechanisms, FRW viability corridors, or interface constraints) or does it get ruled out in a clean, reusable way?

Phase 0’s job is to make sure that:

- “interesting patterns” are not quietly turned into claims,
- every claim is backed by a *reproducible* chain of artifacts,
- and retired ideas are moved into `experiments/` or `docs/ARCHIVE.md` rather than being silently dropped.

---

## 5) Claims, non-claims, and archive

If you want to know **what is claimed where**, start from:

- [`docs/CLAIMS_INDEX.md`](docs/CLAIMS_INDEX.md) – global map of claims.
- [`phase0/CLAIMS.md`](phase0/CLAIMS.md) – Phase 0 claims and governance rules.
- `phase2/CLAIMS.md`, Phase 2 paper appendices – Phase 2 physics claims (under audit).
- Phase 3 paper appendices – Phase 3 physics claims (there is no standalone `phase3/CLAIMS.md`; claims are embedded in the paper).

Non-claims and guardrails:

- Each Phase has a non-claims doc (`NON_CLAIMS.md` or equivalent) clarifying **what we are explicitly *not* claiming** at that rung.
- Phase 4 and 5 non-claims are particularly important: they make it explicit that we are *not* yet making real-data FRW claims or endorsing any θ-measure.

Archive and historical experiments:

- [`docs/ARCHIVE.md`](docs/ARCHIVE.md) – archive policy and major archived branches.
- [`experiments/phase3_flavor_v1/ARCHIVE_STATUS_v1.md`](experiments/phase3_flavor_v1/ARCHIVE_STATUS_v1.md) – flavor-sector experiment status.
- Stage 2 doc-audit and paper-audit docs record which areas are “legacy”, “draft”, or “under audit”.

Everything else lives either in Stage 2 diagnostics or clearly marked experiments.

---

## 6) How to interact with this repo

If you are a new collaborator, a reasonable path is:

1. **Read the overview docs**  
   - `README.md` (this file),
   - `docs/PROJECT_OVERVIEW.md`,
   - `docs/PHASES.md`.

2. **Skim the Phase papers**  
   - Start with `artifacts/origin-axiom-phase0.pdf` and `origin-axiom-phase1.pdf` for governance and toy ensembles.
   - Then Phase 2–3 papers for mode-sum, FRW viability, and mechanism module.
   - Treat Phase 4–5 papers as stubs/early interfaces, not final word.

3. **Inspect Stage 2 diagnostics**  
   - `stage2/docs/STAGE2_OVERVIEW_v1.md` and `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md` for a narrative of what the belts do.
   - The individual Stage 2 belt docs and tables if you care about FRW corridors, mechanism diagnostics, joint mech–FRW structure, data-probe audits, θ★ alignment, empirical anchors/hosts, or doc/paper audits.

4. **Look up claims and non-claims**  
   - `docs/CLAIMS_INDEX.md` for where claims live across phases.
   - `artifacts/origin-axiom-phase*.pdf` for the Phase 0–5 papers (see the “Phase artifacts” section above for links and roles).

4. **Stage 2 diagnostic belts and repo audit**
   - `docs/STAGE2_OVERVIEW.md` and `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md` for Stage 2 as a downstream diagnostic layer (FRW, mech/measure, joint, data, θ★, empirical anchors/hosts, doc/repo + paper audits).
   - `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` for the documentation/repo audit belt and its current status.

5. **Governance and archive**
   - `docs/ARCHIVE.md`, `docs/GATES_AND_STATUS.md`, and `docs/THETA_ARCHITECTURE.md` for the global archive policy, status labels, and θ/corridor architecture enforced by Phase 0.

---

## 7) How to contribute (or just audit)

If you want to contribute or audit:

- Treat Phase 0 as the constitution: do not add claims without updating Phase 0/Phase docs and PROGRESS_LOG.
- Keep new diagnostics in **Stage 2** unless there is a clear, documented promotion gate.
- If you are unsure whether something is canonical or experimental:
  - check `docs/STATE_OF_REPO.md`,
  - check `docs/ARCHIVE.md`,
  - and check the latest entries in `PROGRESS_LOG.md`.

Pull requests, issue reports, or private notes are welcome, especially if they:

- tighten reproducibility,
- clarify claims vs non-claims,
- or propose well-scoped new rungs (e.g. “Phase 3 – Rung N: refined mechanism diagnostic”).

