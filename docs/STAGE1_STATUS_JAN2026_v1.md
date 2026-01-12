# Stage I + Stage 2 Status Snapshot — January 2026

This document records the status of the Origin Axiom Stage I program and its Stage 2 diagnostic belts as of January 2026. It is a narrative companion to `docs/STATE_OF_REPO.md`, `docs/PHASES.md`, and the various Stage 2 overview docs, aimed at making the current position of the project legible to an informed but external reader.

The central question of the program remains: can a single non-cancelling phase twist (θ★ or a closely related structure) be made precise and stress-tested across toy ensembles, mechanism modules, and FRW-style diagnostics without collapsing into either triviality or fine-tuned coincidence? Stage I and Stage 2 do not answer this definitively; they instead build a disciplined scaffold that makes both positive structure and clean failures auditable.

---

## 1. Canonical Stage I phases (Phase 0–5)

The Stage I phases are implemented under `phase0/`–`phase5/`, with papers built via `scripts/build_papers.sh` and PDFs collected under `artifacts/` and phase-level `artifacts/` directories.

- **Phase 0 — Governance and specification (locked).**  
  Defines what a claim is, how it is backed by artifacts, how locking and promotion work, and how experimental or archived work is separated from canonical phases. Phase 0 is the reason the repo has so many explicit contracts, non-claims, and alignment memos: it trades convenience for long-run auditability.

- **Phase 1 — Toy ensembles (locked).**  
  Establishes a set of controlled toy ensembles where a non-cancelling residue can be made precise and stress-tested. The Phase 1 paper and figures live under `phase1/paper/` and `phase1/artifacts/` and are treated as locked; they serve as the first “existence and robustness” rung for the axiom in a simplified landscape.

- **Phase 2 — Mode-sum + bounded FRW viability (under audit but structurally in place).**  
  Encodes the Phase 2 mode-sum and FRW-style viability story, including contracts, claims tables, and an internal structural audit. The Phase 2 paper builds cleanly. The large audit report now lives under `phase2/audit/AUDIT_REPORT.md` and is explicitly documented as a historical structural snapshot rather than a live to-do list. Phase 2 is the bridge between toy ensembles and FRW-flavoured viability: it shows that the axiom can be threaded through controlled approximations into a non-empty, bounded FRW-like corridor without obviously self-destructing.

- **Phase 3 — Mechanism module (active but identity locked).**  
  Phase 3 is now unambiguously the *mechanism module*, not a flavour-calibration phase. Canonical Phase 3 lives under `phase3/` and consists of:
  - mechanism contracts and scope docs (`MECHANISM_CONTRACT.md`, `SCOPE.md`, `ROLE_IN_PROGRAM.md`, alignment + reproducibility memos),
  - numerical outputs under `phase3/outputs/tables/`, including `mech_baseline_scan.csv`, `mech_binding_certificate.csv`, and related diagnostics.
  The archived flavour-sector experiment lives under `experiments/phase3_flavor_v1/` with an explicit archive banner. Phase 3 delivers θ-dependent amplitudes and bounds that behave smoothly and predictably over the θ grid.

- **Phase 4 — FRW toy diagnostics (stub, but structurally coherent).**  
  Phase 4 hosts a stylised FRW toy universe fed by the Phase 3 vacuum story. The main artifacts are FRW tables under `phase4/outputs/tables/`:
  - `phase4_F1_frw_shape_probe_mask.csv`,
  - `phase4_F1_frw_viability_mask.csv`,
  - `phase4_F1_frw_data_probe_mask.csv`,
  - `phase4_F1_frw_lcdm_probe_mask.csv`.
  These encode θ, an effective vacuum scale, an ωΛ-like quantity, an age in Gyr, and a small set of Boolean probes (matter era, late acceleration, smooth H², etc.). Phase 4 is explicitly documented as a toy diagnostic stub, not a full cosmology pipeline.

- **Phase 5 — Interface and sanity layer (rung 0–1).**  
  Phase 5 currently provides an interface layer that reads Phase 3/4 artifacts and emits summaries and sanity checks. It does not introduce new physics claims. The intent is for Phase 5 to become the “dashboard” that external readers see first: a place where Stage 2 diagnostics can later be distilled into human-readable sanity statements without re-deriving the internal machinery.

Each phase has its own scope, non-claims, reproducibility notes, and alignment memos, which are kept in phase-level root directories. Design and audit docs that are not binding have been compactified into `phase2/audit/` and `phase3/design/` / `phase4/design/`, with mapping notes recorded in the phase-level alignment memos and in the root `PROGRESS_LOG.md`.

---

## 2. Stage 2 diagnostic belts

Stage 2 lives under `stage2/` and is explicitly downstream of Phase 3/4 outputs. It does not change phase-level claims unless results are later promoted through a Phase 0–compatible gate. As of January 2026 the following belts are implemented and documented:

- **FRW corridor belt (rungs 1–9).**  
  Uses Phase 4 FRW tables to define FRW families (ALL_GRID, FRW_VIABLE, LCDM_LIKE, TOY_CORRIDOR, intersections) and tests:
  - fractions of the θ grid,
  - contiguity in θ,
  - stride and smoothing robustness,
  - θ★ location relative to each family,
  - θ★ alignment diagnostics.
  Verdict: a broad, contiguous FRW-viable band exists (roughly half the θ grid). The toy corridor machinery picks out coherent segments but does not single out θ★ in a striking way at the current resolution.

- **Mechanism / measure belt (rungs 1–6).**  
  Operates on Phase 3 mechanism tables:
  - inventories tables and columns,
  - identifies probability-like, bounded, non-degenerate columns,
  - splits them into “measure-like” and “flag-like” candidates,
  - studies θ-profiles,
  - selects numerically well-behaved candidates.
  Verdict: Phase 3 produces smooth, well-controlled diagnostics over θ, but no single column is promoted to a canonical measure over θ. This is a structured negative result: the system has reasonable candidates but no obvious unique choice.

- **Joint mech–FRW belt (rungs 1–4).**  
  Builds a joint θ grid that contains both FRW scalars (E_vac, omega_lambda, age_Gyr) and mechanism amplitudes/bounds. Computes:
  - correlations between FRW scalars and mech amplitudes,
  - family-wise correlations restricted to FRW_VIABLE, TOY_CORRIDOR, etc.
  Verdict: the mechanism amplitudes are strongly correlated with FRW scalars; they behave as smooth reparameterisations of the FRW background rather than revealing hidden, independent structure. θ★ is not picked out by these correlations at the current resolution.

- **FRW data-probe belt (rungs 1–2).**  
  Audits the Phase 4 data-probe table:
  - column-level stats for sanity checks and data-like flags,
  - cross-tables between FRW viability and data probes.
  Verdict: the current snapshot satisfies:
  - `has_matter_era` and `smooth_H2` are always true,
  - `frw_viable` is effectively equivalent to “late acceleration present”,
  - `frw_data_ok` is identically false across the grid.
  Interpretation: the FRW toy pipeline already has a nontrivial viability corridor, but the aggregate data flag is not yet meaningful. All FRW families are currently interpreted as pre-data corridors.

- **Doc / repo audit belt.**  
  Uses scripts under `stage2/doc_repo_audit/` to:
  - inventory docs,
  - detect broken references and orphan candidates,
  - list open threads / TODO patterns.
  These results drove a series of documentation cleanups, archive banners, and layout compactifications. The belt is explicitly diagnostic-only: it never auto-edits docs. Its outputs are documented in `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` and `stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md`.

- **Empirical background anchor belt (new, A1–A6).**  
  Introduces a simple, explicit empirical anchor at the level of background cosmology only:
  - defines a small box in \((\omega_\Lambda, \text{age}_{\mathrm{Gyr}})\) space via `stage2/frw_data_probe_analysis/config/empirical_anchor_box_v1.json`,
  - applies this box to the Phase 4 FRW grid to produce an empirical anchor mask,
  - studies intersections with FRW_VIABLE and the Stage 2 toy corridor,
  - characterises the kernel geometry on the joint mech–FRW grid,
  - visualises the kernel in FRW space.

  Numerically, on the current 2048-point θ grid:
  - the empirical anchor yields a kernel of 18 points,
  - the kernel lies inside the FRW-viable corridor and the toy corridor,
  - it splits into two short contiguous segments in θ (9 points each),
  - neither segment contains θ★, and the closest kernel points are at |θ − θ★| ≈ O(1).

  In FRW space (omega_lambda vs age_Gyr), the kernel appears as a small, compact subset of the FRW-viable corridor: structured and non-empty, but not anomalous. All empirical-anchor artifacts are explicitly treated as Stage 2 diagnostics only; no Phase 4/5 claims have been updated in light of this belt.

The Stage 2 belts are summarised in `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md` and `stage2/docs/STAGE2_OVERVIEW_v1.md`, with the empirical anchor belt detailed in `stage2/docs/STAGE2_EMPIRICAL_ANCHOR_SUMMARY_v1.md`.

---

## 3. What we now know (and do not know) about θ★ and the axiom

Within the current Stage I + Stage 2 sandbox, the following picture has emerged.

What we **do** know:

- The non-cancelling phase twist can be made precise in controlled toy ensembles (Phase 1) and threaded through approximations into a bounded FRW-like viability corridor (Phase 2) without immediate pathologies.
- The mechanism module (Phase 3) yields smooth, well-behaved θ-dependent scalars and bounds that correlate strongly with the FRW vacuum sector in Phase 4.
- The FRW toy diagnostics produce a sizeable, contiguous FRW-viable band and a coherent toy corridor structure that is robust under simple contiguity and smoothing checks.
- A simple empirical background box in \((\omega_\Lambda, \text{age}_{\mathrm{Gyr}})\) carves out a small, non-empty kernel inside this FRW-viable corridor; the kernel is structured but modest.

What we **do not** have (yet):

- No canonical, physically compelling measure over θ has been promoted from the mechanism side; the candidates identified so far remain diagnostic only.
- No current Stage 2 belt finds a strong, nontrivial “snap” onto θ★. θ★ lies inside the FRW-viable band, but neither the FRW corridor machinery nor the empirical background box singles it out in an obviously privileged way.
- No contact with full cosmological data (CMB, BAO, SN, etc.) has been made inside Stage I; all data-facing language is deliberately restricted to toy probes and a simple background box, with explicit non-claims.

Taken together, Stage I + Stage 2 now define a worked-out, reproducible counterexample to several naive hopes about the axiom (for example, that a simple, unique θ-measure or a sharp θ★-locking would emerge at low diagnostic cost), while preserving enough structure to justify more ambitious future work.

---

## 4. Positioning for future work

From this status point there are three natural directions, all of which require new, explicitly gated contracts before they affect phase-level claims:

1. **External-facing snapshot and communication.**  
   Use this document, `docs/STATE_OF_REPO.md`, and the Phase 0–2/3 papers as the basis for an external “Stage I + Stage 2 status” summary. The goal is not to over-claim, but to demonstrate:
   - a functioning, auditable program,
   - nontrivial structure and clean negative results,
   - a clear separation between canonical phases and diagnostic belts.

2. **Stage II – external cosmology hosts and real data.**  
   Design a gated Stage II layer that:
   - defines a θ-dependent mapping into standard cosmological parameters,
   - interfaces the existing vacuum/FRW story with external codes (e.g. CLASS, CCL, Cobaya, CosmoSIS) as downstream physics engines,
   - introduces proper “data gates” and promotion criteria for any confrontation with real cosmological datasets.
   The current empirical background anchor belt serves as a baseline for such work: any more sophisticated anchor should be compared back to its small, two-island kernel.

3. **Mechanism-side refinements within the current sandbox.**  
   Explore alternative non-cancelling ansätze or refinements of the mechanism module that:
   - preserve Phase 0 discipline,
   - stay within the existing Phase 3 + Phase 4 FRW toy universe,
   - and test whether qualitative features of the FRW corridor and empirical kernel are robust to such changes.
   This line treats the current snapshot as a reference implementation rather than the final word on how a θ-based mechanism must behave.

Any of these paths can be pursued without discarding the work already done. The value of the current Stage I + Stage 2 scaffold is precisely that it makes both progress and failure modes legible, so that future extensions can be reasoned about rather than improvised.
