# Stage 2 paper audit — Phase 4 (vacuum→FRW toy corridor stub)

Status (2026-01-11): This note records a Stage 2–era audit of the Phase 4 paper `artifacts/origin-axiom-phase4.pdf` against the Phase 4 contracts and the current Stage 2 FRW, joint, and θ★ verdicts. It is descriptive only and does not propose edits to the LaTeX sources.

## 1. Inputs and sections inspected

Paper:

- `artifacts/origin-axiom-phase4.pdf`

Phase 4 docs and alignment:

- Phase 4 SCOPE / PLANNING / CLAIMS / NON_CLAIMS / REPRODUCIBILITY docs under `phase4/`
- `phase4/PHASE4_ALIGNMENT_v1.md`
- FRW promotion design docs:
  - `phase4/docs/PHASE4_FRW_PROMOTION_DESIGN_v1.md`
  - `docs/FRW_CORRIDOR_PROMOTION_GATE_v1.md`
- global docs: `docs/PHASES.md`, `docs/CLAIMS_INDEX.md`, `docs/FUTURE_WORK_AND_ROADMAP.md`

Stage 2 context:

- FRW corridor and verdict docs:
  - `stage2/frw_corridor_analysis/docs/STAGE2_FRW_CORRIDOR_SUMMARY_v1.md`
  - `stage2/frw_corridor_analysis/docs/STAGE2_FRW_VERDICT_v1.md`
- FRW data-probe audit:
  - `stage2/frw_data_probe_analysis/docs/STAGE2_FRW_DATA_PROBE_AUDIT_v1.md`
- Joint mech–FRW verdict:
  - `stage2/joint_mech_frw_analysis/docs/STAGE2_JOINT_VERDICT_v1.md`
- θ★ and master verdict:
  - `stage2/theta_star_analysis/docs/STAGE2_THETA_STAR_ALIGNMENT_v1.md`
  - `stage2/docs/STAGE2_MASTER_VERDICT_v1.md`

Paper sections explicitly inspected:

- Title page + abstract
- Sec. 1 Introduction
- The definition of the E_vac(θ) mapping and the F1 diagnostic stack
- FRW viability and LCDM-like probe sections
- Discussion of corridor families and their interpretation
- Conclusion / outlook-style paragraphs

The aim is to check narrative alignment, claims alignment, and scope/status language against the current Phase 4 contracts and Stage 2 verdicts.

## 2. Summary of the Phase 4 paper’s own story

The Phase 4 paper presents Phase 4 as an FRW-facing **toy corridor stub** built on top of the Phase 3 amplitude output A(θ). It takes as input a Phase 3 amplitude sample θ ↦ A(θ) and defines a simple mapping to an effective vacuum term,

- E_vac(θ) = α A(θ)^β,

with a fixed toy choice (α, β) = (1, 4). Using this mapping it builds a five-layer diagnostic stack, which can be summarised as:

1. An F1 sanity curve that probes basic properties of E_vac(θ) as a function over θ (range, smoothness, sign, obvious pathologies).
2. F1 shape diagnostics that define a purely toy “corridor” based on amplitude thresholds or similar simple cuts in E_vac space.
3. FRW-inspired toy checks that embed E_vac(θ) into a simple FRW model and test basic viability (e.g. existence of a sensible expansion history).
4. A viability mask over the θ-grid, capturing points that pass the toy FRW criteria.
5. A broad ΛCDM-like probe that places windows on Ω_Λ(θ) and the toy age t_0(θ) on top of the viability mask.

The FRW sector is explicitly constructed from a minimal FRW model with fixed toy parameters (e.g. Ω_m ≈ 0.3, Ω_r ≈ 0, a fiducial H_0), and the ΛCDM-like windows are broad tolerances around target values (e.g. Ω_Λ ≈ 0.7 and age ≈ 13.8 Gyr). The manuscript uses these to define families akin to:

- a toy F1 corridor,
- an FRW-viable subset,
- and a ΛCDM-like subset within the viable region.

Throughout, the text emphasises that these are **corridor-style diagnostics** in a toy FRW setup, not a final cosmological model. The paper does not claim to identify a preferred θ⋆ or to be in contact with precision cosmology; instead it aims to show that:

- the Phase 3 mechanism’s amplitude output can be mapped into FRW-like quantities in a numerically stable way,
- corridor-style families over θ can be defined and interrogated,
- and these constructions are fully reproducible and inspectable.

## 3. Alignment with Phase 4 contracts and global program docs

Comparing the paper with the Phase 4 docs and alignment memo:

- Role and identity:

  - The paper consistently describes Phase 4 as a **vacuum-to-FRW consistency and scale sanity** rung: a corridor-style testbed using a simple E_vac mapping and FRW stub.
  - This matches `phase4/PHASE4_ALIGNMENT_v1.md` and `docs/PHASES.md`, which describe Phase 4 as an FRW-facing diagnostic stub, not as a full data-facing cosmology phase.

- Claims structure:

  - The paper’s implicit claims are about the existence and behaviour of toy FRW viability bands and ΛCDM-like windows under the chosen E_vac mapping and FRW model.
  - Phase 4 claims docs and the alignment memo frame these as **internal diagnostics** built on Phase 3 outputs and do not upgrade them to physical predictions.
  - There is no claim in the paper that a canonical θ-corridor has been discovered in a data-conditioned sense or that θ⋆ is singled out.

- Non-claims and guardrails:

  - The Phase 4 non-claims and planning docs state that Phase 4 does not claim real-data agreement, does not fix the mapping E_vac(θ) uniquely, and does not attempt full cosmological parameter inference.
  - The paper’s abstract and conclusion are consistent with this: they present the FRW pipeline as a transparent test of whether the Phase 3 mechanism can be chained into FRW-like quantities, not as an end-point.

- Reproducibility:

  - The paper mentions FRW masks, ΛCDM-like windows, and corridor structures in a way that corresponds to the Phase 4 FRW tables under `phase4/outputs/tables/` and the Phase 4 reproducibility docs.
  - This is aligned with the Phase 4 reproducibility plan and the alignment memo, which treat these tables as the concrete artifacts that Stage 2 FRW belts later read and analyse.

Net: the Phase 4 paper’s story is consistent with the Phase 4 contracts and global program docs now locked in the Stage 2 snapshot.

## 4. Alignment with Stage 2 FRW, data-probe, joint, and θ★ verdicts

Stage 2 FRW and related verdicts assert that:

- On the current 2048-point θ-grid, there is a broad, contiguous FRW-viable band defined by a viability mask derived from Phase 4 FRW tables.
- FRW corridor families (viable, ΛCDM-like, toy corridor, and intersections) are structurally nontrivial and robust under contiguity and smoothing tests, but they are **pre-data**: the aggregate `frw_data_ok` flag is currently false everywhere.
- In the joint mech–FRW space, mechanism-derived scalars are highly redundant with FRW scalars (vacuum energy, ω_Λ, age).
- θ★ lies inside the FRW-viable band but is not singled out by any corridor or ΛCDM-like family.

The Phase 4 paper is broadly consistent with these conclusions:

- It defines viability and ΛCDM-like windows using the same kind of FRW construction that Stage 2 later reads from Phase 4 tables.
- It presents corridor and ΛCDM-like families as **diagnostic bands** in a toy FRW model, not as data-conditioned or observationally confirmed structures.
- It does not assert that the ΛCDM-like window is uniquely or canonically defined, nor that it is tied to real observational constraints; rather, it is framed as a broad sanity window.

The paper does not introduce a data-conditioned `frw_data_ok` gate of the kind Stage 4/Stage 2 would require for real-data contact, and it does not treat any corridor as having passed such a gate. This is compatible with the Stage 2 FRW data-probe verdict that the current aggregate data flag is closed and that all FRW families should be treated as pre-data corridors.

The paper also does not claim that FRW behaviour alone selects θ⋆. Any reference to θ⋆ is as a point that can be inspected within the bands, not as a value determined by the FRW pipeline. This is aligned with the Stage 2 θ★ verdict.

## 5. Scope and limitation language audit

From the abstract, introduction, and concluding sections:

- The paper is explicit that its aim is:

  - to test **numerical stability and transparency** of the chain “Phase 3 amplitude → E_vac(θ) → FRW-like quantities → corridor-style diagnostics”,
  - and to do so in a way that is reproducible and easy to interrogate.

- It does not present the FRW toy model or the ΛCDM-like windows as physical inference machinery.
- References to “ΛCDM-like” are clearly qualified as toy windows around target values for Ω_Λ and t_0 given a fixed, simplified FRW model.

There is no suggestion that:

- the corridor or ΛCDM-like bands are already constrained by real data,
- the present toy FRW module is calibrated to observations,
- or the program has already identified a physically preferred θ.

This matches the Stage 2 master verdict, which views the Phase 4 + Stage 2 FRW stack as:

- a nontrivial internal structure with broad viability bands and robust corridors,
- but still a pre-data construction without a canonical measure or θ-selection.

## 6. Potential future tightening (for a later editing rung)

This audit does not propose LaTeX edits, but for a future editing rung it might be beneficial to:

- Add a short explicit remark in the conclusion that later Stage 2 FRW belts and promotion design docs treat all corridors as pre-data and that the aggregate data gate is currently closed.
- Optionally cross-reference the Phase 5 interface role, clarifying that Phase 4’s results will appear as internal verdict tables rather than as external predictions until a data gate is opened and a promotion gate is passed.

These would be minor clarifications. The existing Phase 4 language is already careful and does not misrepresent the Stage 2 FRW picture.

## 7. Verdict

For the Stage 2 snapshot:

- The Phase 4 paper accurately presents Phase 4 as an FRW-facing corridor stub built on top of the Phase 3 amplitude output via a simple E_vac mapping and a transparent FRW toy model.
- Its FRW viability and ΛCDM-like constructions match the conceptual role assigned to Phase 4 in the contracts and alignment memo and are compatible with the Stage 2 FRW and data-probe verdicts.
- The paper does not claim data-conditioned corridors, canonical θ-selection, or quantitative agreement with real cosmological parameters; it frames its constructions as toy diagnostics to be used and refined by later phases.

No contradictions were found between the Phase 4 paper and the current Stage 2 FRW, joint, and θ★ verdicts. Any future edits can be limited to minor clarifications and explicit cross-links to Stage 2 and Phase 5, rather than substantive changes in claims.
