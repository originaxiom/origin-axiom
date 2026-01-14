# Phase 4 alignment memo (FRW toy stub, claims, Stage 2, and paper)

Status (2026-01-11): This memo records how the Phase 4 FRW toy-diagnostic stub, scope/claims/non-claims/reproducibility documents, Stage 2 FRW diagnostics, and the Phase 4 paper align. It is descriptive only and does not introduce new claims.

## 1. Inputs used for this alignment

This memo is based on:

- `phase4/SCOPE.md` – Phase 4 scope definition (draft, non-binding).
- `phase4/CLAIMS.md` – Phase 4 draft claims.
- `phase4/NON_CLAIMS.md` – Phase 4 draft non-claims and guardrails.
- `phase4/REPRODUCIBILITY.md` – Phase 4 reproducibility plan (draft) and gate criteria.
- `phase4/CLAIMS_TABLE.md` – draft claims→artifacts map.
- `phase4/design/PHASE3_INTERFACE.md` – Phase 3↔Phase 4 interface design note.
- `phase4/design/FRW_TOY_DESIGN.md` – design note for FRW-like toy diagnostics.
- `phase4/design/FRW_DATA_DESIGN.md` – design note for FRW-facing data probes.
- `phase4/design/FRW_SYNTHESIS.md` – FRW-facing synthesis design note.
- `phase4/design/PLANNING.md` and `phase4/design/HARD_NOVELTY_ROADMAP.md` – Phase 4 planning and novelty design notes (draft, non-binding, explicitly marked as such).
- `phase4/PROGRESS_LOG.md` – Phase 4 progress log.
- `phase4/docs/PHASE4_FRW_PROMOTION_DESIGN_v1.md` – Phase 4 FRW promotion design (Stage 2 design rung).
- `docs/FRW_CORRIDOR_PROMOTION_GATE_v1.md` – global FRW corridor promotion gate.
- Phase 4 FRW outputs under `phase4/outputs/tables/`, including:
  - `phase4_F1_frw_shape_probe_mask.csv`
  - `phase4_F1_frw_data_probe_mask.csv`
  - `phase4_F1_frw_viability_mask.csv`
  - `phase4_F1_frw_lcdm_probe_mask.csv`.
- Stage 2 FRW and joint diagnostics, particularly:
  - `stage2/frw_corridor_analysis/docs/STAGE2_FRW_CORRIDOR_SUMMARY_v1.md`
  - `stage2/frw_data_probe_analysis/docs/STAGE2_FRW_DATA_PROBE_AUDIT_v1.md`
  - `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md`
  - `stage2/docs/STAGE2_OVERVIEW_v1.md`
  - `stage2/theta_star_analysis/docs/STAGE2_THETA_STAR_ALIGNMENT_v1.md`.
- `artifacts/origin-axiom-phase4.pdf` – the Phase 4 paper built from `phase4/paper/main.tex`.

This memo focuses on alignment and interpretation; it does not change Phase 4 code, tables, or Stage 2 pipelines.

## 2. Scope: FRW toy diagnostics stub, not full cosmology

`phase4/SCOPE.md` describes Phase 4 as an FRW toy-diagnostic stub downstream of the Phase 3 mechanism: it consumes mechanism-derived scalars and constructs FRW-like backgrounds and viability masks on a toy grid, defining simple FRW viability notions and corridors but not attempting realistic cosmology or data fits. It explicitly states that Phase 4:

- does not solve the cosmological constant problem,
- does not fit real cosmological data in a serious way,
- does not claim that any FRW corridor is “our universe”,
- and does not introduce new physics claims beyond its toy FRW construction.

`phase4/design/FRW_TOY_DESIGN.md` and `phase4/design/FRW_SYNTHESIS.md` are consistent with this: they treat FRW quantities and masks as toy diagnostics, defining families (e.g. viability masks, LCDM-like probes, toy corridor masks) and intended summary plots without claiming physical predictions.

The Phase 4 paper, in its introduction and FRW description sections, frames Phase 4 as an FRW-facing stub that builds on Phase 3 outputs and constructed FRW masks to explore the shape of a viability band and related families. It does not claim realistic data contact or a unique solution for the real universe. Global docs (`docs/PHASES.md`, `docs/STATE_OF_REPO.md`) similarly describe Phase 4 as a “diagnostic FRW stub,” not as a full cosmological model.

On the scope axis, `phase4/SCOPE.md`, the design docs, the paper narrative, and the global description are aligned: Phase 4 is a toy FRW diagnostic module, pre-data and pre-phenomenology.

## 3. Claims and non-claims vs. FRW masks, Stage 2 corridors, and data probes

`phase4/CLAIMS.md` and `phase4/CLAIMS_TABLE.md` (both draft, non-binding) organise Phase 4 claims around:

- construction of FRW scalars and viability masks from Phase 3 mechanism outputs,
- existence of a non-empty, structured FRW viability band on the toy grid,
- existence of additional FRW-related masks (e.g. LCDM-like subsets, toy corridor families) defined at the design level,
- explicit non-claims about any data-conditioned corridor or realistic cosmology until gated by promotion.

`phase4/NON_CLAIMS.md` reinforces the non-claims: Phase 4 does not claim that any corridor is data-selected or physically realised and does not claim special status for θ★.

Phase 4 outputs under `phase4/outputs/tables/` implement FRW scalars and masks that Stage 2 uses as inputs. Stage 2 FRW diagnostics report that:

- there is a broad, contiguous FRW-viable band on the θ-grid (about half the grid, with exact fractions tabulated in Stage 2 belts),
- basic sanity checks such as `has_matter_era` and `smooth_H2` are always true on the current sample,
- FRW viability (`frw_viable`) is effectively equivalent to the presence of late acceleration in this configuration,
- the aggregate data flag `frw_data_ok` is identically false in the current snapshot (no grid point satisfies it),
- θ★ lies inside the FRW-viable band but is not singled out by FRW viability or current corridor definitions.

These findings are consistent with a conservative reading of the Phase 4 claims and non-claims: Phase 4 can legitimately claim the existence of a toy FRW viability band and families defined on top of it; it cannot legitimately claim a data-conditioned FRW corridor or a special selection of θ★ with the current pipeline. Stage 2 documents explicitly record that `frw_data_ok` is empty and treat all corridors as pre-data in this snapshot, framing this as a pipeline state rather than a physical exclusion.

As long as Phase 4 text and claims are interpreted as describing toy FRW viability and corridor structure (pre-data), Phase 4 claims and non-claims are aligned with the actual FRW masks and Stage 2 diagnostics.

## 4. Reproducibility, promotion design, and gating

`phase4/REPRODUCIBILITY.md` is a draft reproducibility plan that describes how FRW quantities and masks are generated from Phase 3 outputs, how tables and figures for the Phase 4 paper are produced, and what would be required for a future lock (e.g. clean builds, no TODO/FIXME in the LaTeX, reproducible figures, documented promotion of Stage 2 artifacts).

`phase4/docs/PHASE4_FRW_PROMOTION_DESIGN_v1.md` and `docs/FRW_CORRIDOR_PROMOTION_GATE_v1.md` define how Stage 2 FRW, mech, joint, and data-probe artifacts could eventually be promoted into Phase 4 or Phase 5 text and figures. They:

- propose Option A style minimal promotions (e.g. a small number of corridor figures and fraction tables, plus brief textual summaries),
- insist that any promotion must pass a gate that checks reproducibility, robustness, interpretability, and θ★ neutrality,
- and explicitly keep all Stage 2 artifacts as internal diagnostics until that gate is passed.

The Phase 4 paper, in its current form, is consistent with this arrangement as long as it is read alongside the promotion design: it may describe FRW quantities and corridors and reference them qualitatively, but any detailed use of Stage 2 artifacts as evidence (e.g. promotion of specific Stage 2 plots) is deferred to the promotion gate. Global docs (Stage 2 overviews and the promotion design) explicitly state that no Stage 2 artifacts have been promoted into Phase 4/5 text yet and treat current Phase 4 text as pre-promotion.

On this axis, `phase4/REPRODUCIBILITY.md`, the promotion design docs, and the intended interpretation of the Phase 4 paper are aligned: reproducibility expectations are clear, promotion gates are in place, and Stage 2 diagnostics remain internal until explicitly promoted.

## 5. Non-claims, θ★, and Phase 4 design notes

`phase4/NON_CLAIMS.md` and the global Stage 2 docs record important non-claims:

- Phase 4 does not fix θ★ or claim that the current FRW machinery selects θ★ or φ^φ in a nontrivial way.
- Phase 4 does not claim a data-conditioned FRW corridor; data probes and `frw_data_ok` are treated as future work.
- Any observed inclusion of θ★ in a viable band is treated as a sanity check, not a prediction or evidence of special status.

Stage 2 θ★ alignment diagnostics are consistent with this: they find that θ★ lies inside the FRW-viable band but is not singled out by corridor families and explicitly record this as a negative-result sanity check.

`phase4/design/PLANNING.md` and `phase4/design/HARD_NOVELTY_ROADMAP.md` are now explicitly labelled as draft, non-binding design documents that cannot override the Phase 4 scope or claims and that are governed by the FRW promotion gate and Phase 4 promotion design. This protects Phase 4 from accidentally inheriting strong claims from early design brainstorming.

Under this interpretation, Phase 4 scope, claims, non-claims, FRW outputs, Stage 2 diagnostics, promotion design, and design notes are aligned: Phase 4 is a toy FRW stub with cautious claims and explicit guardrails around θ★ and data-conditioned corridors.

## 6. Potential future doc rungs (not yet executed)

This memo suggests, but does not enact, the following documentation rungs:

- Add a short pointer from `phase4/SCOPE.md` or `phase4/OVERVIEW.md` to `phase4/PHASE4_ALIGNMENT_v1.md` as the canonical alignment memo for Phase 4.
- If and when specific Stage 2 FRW artifacts are promoted into the Phase 4 paper (e.g. a corridor histogram, a fraction table), update `phase4/CLAIMS.md` and `phase4/CLAIMS_TABLE.md` first, pass the FRW promotion gate, and then adjust the LaTeX and Stage 2 docs in a coordinated rung.
- When the FRW data gate (`frw_data_ok`) is populated in a future pipeline, ensure that any resulting data-conditioned corridor claims are introduced via a separate, tightly scoped phase or promotion rung with explicit Phase 0 gating and updated non-claims.

These are deferred to later rungs and do not change current Phase 4 scope, claims, non-claims, or reproducibility status.

---

### Note on documentation layout (Belt G)

As of 2026-01-11 Phase 4 design and planning documents live under:

- `phase4/design/PLANNING.md`
- `phase4/design/HARD_NOVELTY_ROADMAP.md`
- `phase4/design/FRW_SYNTHESIS.md`
- `phase4/design/MAPPING_FAMILIES.md`
- `phase4/design/FRW_TOY_DESIGN.md`
- `phase4/design/PHASE3_INTERFACE.md`
- `phase4/design/FRW_DATA_DESIGN.md`

Canonical contracts (SCOPE, CLAIMS, NON_CLAIMS, CLAIMS_TABLE, REPRODUCIBILITY, alignment, OVERVIEW, PROGRESS_LOG) remain in the `phase4/` root. Historical references in PROGRESS_LOG entries preserve the original paths used at the time and may point to pre-reorg locations.

---

### FRW toy ↔ host ↔ anchor alignment (Stage 2 pointer)

For the Phase 4 FRW-like toy, the equation-level wiring and its Stage 2
host/anchor analysis are documented in:

- `phase4/docs/PHASE4_FRW_TOY_EQUATIONS_v1.md`
- `stage2/frw_data_probe_analysis/` (empirical anchor box + mask)
- `stage2/joint_mech_frw_analysis/` (anchor intersections, kernel, profiles, sensitivity)
- `stage2/external_frw_host/` (flat-FRW background host and age cross-checks)

This alignment note is the place to check:

- which toy columns are treated as \(\Omega_\Lambda\) and \(t_0\),
- how the empirical anchor box in \((\Omega_\Lambda, t_0)\) is defined,
- how the external flat-FRW host is calibrated and compared to the toy.

Phase 4 CLAIMS and NON_CLAIMS remain governed by this file; the host
and anchor belts are Stage 2 diagnostics only.
