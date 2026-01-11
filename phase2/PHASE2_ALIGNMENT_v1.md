# Phase 2 alignment memo (scope, claims, FRW viability, and paper)

Status (2026-01-11): This memo records how the Phase 2 paper, scope/claims/assumptions/approximation/reproducibility documents, and the current repository and Stage 2 diagnostics align. It is descriptive only and does not introduce new claims.

## 1. Inputs used for this alignment

This memo is based on:

- `phase2/SCOPE.md` – Phase 2 scope definition and non-claims.
- `phase2/CLAIMS.md` – Phase 2 claims register (locked).
- `phase2/ASSUMPTIONS.md` – Phase 2 assumptions register.
- `phase2/APPROXIMATION_CONTRACT.md` – approximation and modelling contract.
- `phase2/PHASE2_WORKFLOW_GUIDE.md` – workflow guide for running Phase 2 pipelines.
- `phase2/PHASE2_LOCK_CHECKLIST.md` – lock checklist for Phase 2.
- `phase2/REPRODUCIBILITY.md` – Phase 2 reproducibility and provenance.
- `phase2/AUDIT_REPORT.md` – structural audit snapshot for Phase 2 (P2-A1), explicitly containing TODO/TBD markers as a historic audit record rather than live claims.
- `phase2/PROGRESS_LOG.md` – Phase 2 progress log.
- `phase2/paper/main.tex` and its section files, together with:
- `artifacts/origin-axiom-phase2.pdf` – the Phase 2 paper built from the LaTeX sources.
- Stage 2 FRW diagnostics built on top of Phase 4 FRW outputs, especially:
  - `stage2/frw_corridor_analysis/docs/STAGE2_FRW_CORRIDOR_SUMMARY_v1.md`
  - `stage2/frw_data_probe_analysis/docs/STAGE2_FRW_DATA_PROBE_AUDIT_v1.md`
  - `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md`
  - `stage2/docs/STAGE2_OVERVIEW_v1.md`.

Where convenient, this memo refers to paper sections by their conceptual roles (introduction, mode-sum and bounded FRW viability construction, approximation discussion, results and corridor diagnostics, limitations and future work) rather than exact headings.

## 2. Scope: mode-sum vacuum and bounded FRW viability, pre-data

`phase2/SCOPE.md` describes Phase 2 as responsible for implementing a minimal, coarse-grained mode-sum vacuum description and a bounded FRW viability notion downstream of Phase 1. It introduces a “bounded floor” inspired by the non-cancellation mechanism and defines Phase 2’s main job as constructing a toy FRW viability corridor in a mode-sum setting, without attempting detailed data contact or full cosmological realism.

It emphasises that Phase 2:

- does not solve the cosmological constant problem,
- does not fit real cosmological data,
- does not fix a physical scale for vacuum energy or determine θ★,
- and does not claim that any toy FRW viability corridor is already “the universe”.

The Phase 2 paper’s introduction and scope statements are consistent with this: they motivate moving from finite phasor ensembles (Phase 1) to a more field-like, mode-sum picture and to an FRW-facing viability concept but explicitly state that the construction is still toy-level, not realistic cosmology. The paper presents the FRW viability notion as a bounded, structural diagnostic (e.g. the existence of certain eras, late acceleration, and basic smoothness of H²) rather than as a fit to observational data.

Across `phase2/SCOPE.md`, the paper introduction, and the global docs under `docs/PHASES.md` and `docs/PROJECT_OVERVIEW.md`, Phase 2’s scope is consistently described as constructing and testing a bounded FRW viability notion in a simplified mode-sum setting, strictly pre-data and pre-phenomenology.

## 3. Claims register vs. FRW viability construction

`phase2/CLAIMS.md` (locked) organises Phase 2 claims as a set of statements about:

- the existence of a well-defined, bounded FRW viability corridor in the toy setting (e.g. a non-empty set of θ or parameter points that satisfy basic FRW viability checks),
- the internal consistency of the mode-sum + bounded floor implementation (e.g. that the constructed FRW quantities satisfy the basic equations and constraints under the approximations declared),
- the existence of a structured viability corridor in the toy world (e.g. nontrivial band rather than isolated points),
- the relation between the bounded floor and FRW viability (e.g. that the floor does not trivially destroy or guarantee viability, within tolerances of the toy model).

The Phase 2 paper’s core sections on the mode-sum construction and FRW viability diagnostics (again, by conceptual role rather than specific headings) construct a vacuum sector and FRW scalars (such as H², energy densities, and an effective vacuum contribution) and then define FRW viability masks based on simple criteria (e.g. presence of a matter era, late acceleration, smoothness conditions). The claims in the paper about a non-empty, structured FRW viability band and about the toy corridor are phrased in a way that matches the claims register: they apply to the toy mode-sum and FRW diagnostics implemented in Phase 2, not to real data or a realistic cosmology.

Later Stage 2 FRW diagnostics (built on top of Phase 4 FRW outputs) confirm that, in the current snapshot:

- there is a broad, contiguous FRW-viable band on the θ-grid,
- basic sanity masks such as “has_matter_era” and “smooth_H2” are always true on the sampled grid,
- FRW viability collapses to a condition equivalent to “late acceleration present” in the current toy configuration,
- and the aggregate data flag `frw_data_ok` is empty (no points satisfy it).

These findings are consistent with the more modest Phase 2 claims: Phase 2 claims existence and structure of a pre-data FRW viability band, not existence of a data-conditioned corridor. Stage 2 FRW diagnostics sharpen the picture but do not contradict the locked Phase 2 claims as long as Phase 2’s “FRW viability corridor” is interpreted as a pre-data structural notion.

Within this frame, `phase2/CLAIMS.md`, the paper’s main FRW viability construction, and the Stage 2 FRW results align: they all describe a non-empty, structured FRW viability band in a toy setting without claiming a populated data-conditioned corridor.

## 4. Assumptions and approximation contract vs. paper approximations

`phase2/ASSUMPTIONS.md` lists modelling assumptions about the mode-sum vacuum and FRW construction: the choice of truncations, coarse-graining, effective parameters, and the approximate treatment of vacuum contributions. It emphasises that Phase 2 operates under controlled but idealised assumptions and that any claim must be interpreted within those limitations.

`phase2/APPROXIMATION_CONTRACT.md` refines this by specifying a contract for approximations: which quantities are approximated, which regimes are trusted, how error terms are treated, and how these approximations constrain the interpretation of results. It separates “structural” claims (about the existence of a viable band under the approximations) from any potential future attempts to contact real data, which are explicitly declared out of Phase 2 scope.

The Phase 2 paper’s derivations and methods sections state approximations of the same kind: they present a mode-sum treatment with cutoffs, effective parameter choices, and simplified FRW equations. Whenever the paper discusses FRW behavior or corridors, it does so in the context of these approximations and does not claim realism beyond what the assumption and approximation documents allow. Sections discussing limitations and future work note that moving to realistic data and more complete treatments would require additional phases and more sophisticated modelling.

On this axis, `ASSUMPTIONS.md`, the approximation contract, and the paper are aligned: they describe the same approximations and interpret Phase 2 results as conditional on those approximations rather than as exact statements about the real universe.

## 5. Reproducibility, audit, and lock checklist vs. repo and paper

`phase2/REPRODUCIBILITY.md` describes how to run Phase 2 pipelines: environment setup, mode-sum construction scripts, FRW viability mask generation, and figure/table builds for the Phase 2 paper. It emphasises that numerical artifacts used as evidence must be generated by deterministic scripts under version-controlled configs, and it describes how provenance and run logs are recorded.

`phase2/PHASE2_WORKFLOW_GUIDE.md` and `phase2/PHASE2_LOCK_CHECKLIST.md` further specify the expected workflow and checks required before declaring Phase 2 “locked”. They link to scripts, config files, and relevant outputs and state which conditions must be satisfied (e.g. clean builds, no TODO/FIXME markers in the paper, reproducible figures and tables).

`phase2/AUDIT_REPORT.md` is a more detailed structural audit that checks for TODO/TBD/XXX markers, inconsistencies, and missing links and records them as part of a historic audit snapshot (P2-A1). Sections in this report that explicitly quote TODOs or TBDs are part of the audit log rather than live claims; they describe what was outstanding at the time of that audit, not what Phase 2 currently claims.

The Phase 2 paper’s methods and results sections, together with the repo’s structure under `phase2/` (scripts, config, outputs, and paper sources), are consistent with the reproducibility contract: they present figures and tables as outputs of documented pipelines rather than hand-crafted results. Subsequent Stage 2 diagnostics (which treat Phase 3/4 outputs as inputs) further attest to the reproducibility of core FRW quantities.

Taken together, `REPRODUCIBILITY.md`, the workflow guide, the lock checklist, the audit report, and the actual repo structure align with the Phase 2 paper’s depiction of its numerics: Phase 2 is reproducible under the declared environment and scripts, and any residual audit TODOs are either structural and tracked or have been superseded by later documentation and Stage 2 diagnostics.

## 6. Non-claims, boundaries, and interpretation with Stage 2

Across Phase 2 documents and the paper, the following non-claims and boundaries are consistently enforced:

- Phase 2 does not claim contact with real cosmological data; FRW viability is a pre-data structural notion.
- Phase 2 does not claim a populated data-conditioned FRW corridor; the `frw_data_ok` gate is not treated as satisfied in canonical claims.
- Phase 2 does not fix the value of θ★, does not identify φ or φ^φ as distinguished, and does not claim that any particular θ is selected by the toy viability corridor; any such selection would require later phases and additional principles.
- Phase 2 does not claim a complete description of the vacuum sector or realistic FRW evolution; it operates under simplified approximations documented in `ASSUMPTIONS.md` and `APPROXIMATION_CONTRACT.md`.

Stage 2 FRW diagnostics, as currently implemented, reinforce these boundaries:

- They find a broad, contiguous FRW-viable band on the θ-grid, consistent with Phase 2’s claims of a structured viability notion.
- They show that the aggregate data flag `frw_data_ok` is empty, which means that, in the current snapshot, any talk of a “data-conditioned corridor” would be premature and remains explicitly future work.
- They show that θ★ lies inside the viable band but is not singled out by present FRW machinery, which is aligned with Phase 2’s non-commitment on θ★ and with global docs that treat θ★ as a hypothesis rather than a promoted result.

Interpreted this way, there is no contradiction between Phase 2 claims and the Stage 2 FRW diagnostics; Stage 2 sharpens and clarifies Phase 2’s toy FRW viability story rather than overturning it.

## 7. Potential future doc rungs (not yet executed)

This memo suggests, but does not enact, the following documentation rungs for later passes:

- Add a short pointer from `phase2/SCOPE.md` or `phase2/README.md` to `phase2/PHASE2_ALIGNMENT_v1.md` as the canonical alignment memo for Phase 2.
- If the Phase 2 paper or FRW code are revised to reflect updated Stage 2 diagnostics, ensure that `phase2/CLAIMS.md` and `phase2/ASSUMPTIONS.md` are updated first and that the paper text is brought into line with them, not vice versa.
- When the FRW data gate (`frw_data_ok`) is eventually populated in a future pipeline, introduce new claims in `phase2/CLAIMS.md` and/or later phases under a clear promotion gate, rather than retrofitting Phase 2 text to suggest that a data-conditioned corridor was already present.

These steps are deferred to later doc-audit or promotion rungs and do not change the current Phase 2 scope, claims, approximations, or reproducibility contract.
