# Stage 2 paper audit — Phase 2 (mode-sum + bounded FRW viability)

Status (2026-01-11): This note records a Stage 2–era audit of the Phase 2 paper
`artifacts/origin-axiom-phase2.pdf` against the Phase 2 contracts and the current Stage 2
verdicts. It is descriptive only and does not propose edits to the LaTeX sources.

## 1. Inputs and sections inspected

Paper:

- `artifacts/origin-axiom-phase2.pdf`

Phase 2 docs and alignment:

- Phase 2 SCOPE / assumptions / claims / reproducibility docs under `phase2/`
- `phase2/PHASE2_ALIGNMENT_v1.md` (Phase 2 alignment memo)
- global docs: `docs/PHASES.md`, `docs/CLAIMS_INDEX.md`, `docs/FUTURE_WORK_AND_ROADMAP.md`

Stage 2 context:

- FRW corridor and data-probe verdicts:
  - `stage2/frw_corridor_analysis/docs/STAGE2_FRW_VERDICT_v1.md`
  - `stage2/frw_data_probe_analysis/docs/STAGE2_FRW_DATA_PROBE_AUDIT_v1.md`
- Stage 2 master verdict:
  - `stage2/docs/STAGE2_MASTER_VERDICT_v1.md`

Paper sections explicitly inspected:

- Title page + abstract
- Sec. 1 Introduction
- Claim sections for C2.1, C2.2, C2.3 (as they appear in the main text)
- Sec. 7 (scope, non-claims, failure modes, required upgrades)
- Sec. 8 Conclusion
- Appendix A (computational provenance overview)

The aim is to check **narrative alignment**, **claims alignment**, and **scope/status language**
against the current contracts and Stage 2 picture.

## 2. Summary of the Phase 2 paper’s own story

In the paper, Phase 2 is presented as a **bounded, reproducible test** of a single operational
hypothesis: enforcing a strict global non-cancellation floor on a vacuum-like numerical system
creates a stable residual diagnostic that can be followed through a minimal pipeline without
instability or numerical pathologies.

The core ingredients, as stated in the paper, are:

- A lattice vacuum testbed with a complex scalar field and a global diagnostic amplitude \(A(t)\).
- A **hard floor constraint** \(|A(t)| \ge \varepsilon\) enforced by a uniform zero-mode correction when a
  trial update would violate the floor.
- Matched unconstrained vs constrained runs to show that the floor is responsible for the residual.
- A small set of **numerical control parameters**:
  - floor scale \(\varepsilon\),
  - discretization / UV controls (cutoff, lattice size, etc.),
  - phase parameter \(\theta\) as an external control, with an optional anchored value \(\theta_\star\).
- A simple FRW module used as a **toy background** driven by a mapping from the residual
  diagnostic to an effective cosmological term.

The manuscript is explicitly organized around **three claims**:

- **C2.1 — Existence under constraint.**  
  The constrained run, with the hard floor active, maintains a persistent nonzero diagnostic
  relative to the matched unconstrained baseline and does so without visible numerical pathology.
- **C2.2 — Robustness under numerical controls.**  
  Across controlled sweeps in floor scale and discretization parameters, the induced residual
  remains well behaved (no blow-ups, no obvious instabilities) and varies smoothly with the
  controls in the claimed parameter ranges.
- **C2.3 — FRW embedding stability.**  
  For a chosen mapping from the residual diagnostic into an effective FRW term and for specified
  integration settings, the FRW module produces trajectories that remain stable; the floor-induced
  residual can be carried through this toy FRW embedding without the FRW solver failing.

The conclusion reiterates that Phase 2’s core contribution is **methodological and
reproducibility-focused**: a concrete constrained mechanism is specified and implemented,
stress-tested, and documented with a per-figure run manifest and deterministic build path.
It explicitly states that Phase 2 does **not**:

- derive the axiom from a local action,
- claim quantitative agreement with the observed cosmological constant,
- establish a continuum-limit theorem,
- or prove uniqueness or physical selection of \(\theta_\star\).

The FRW part is framed as a toy, transparent embedding, not as a realistic cosmological model.

## 3. Alignment with Phase 2 contracts and global program docs

Comparing the paper with:

- Phase 2 SCOPE / assumptions / claims / reproducibility docs under `phase2/`,
- `phase2/PHASE2_ALIGNMENT_v1.md`,
- and global docs `docs/PHASES.md` and `docs/CLAIMS_INDEX.md`,

the following alignment holds at the Stage 2 snapshot:

- **Role and identity.**  
  Phase 2 is consistently described as a **mode-sum + bounded FRW viability testbed**, not as a
  full physical model. This matches the Phase 2 alignment memo and `docs/PHASES.md`, where
  Phase 2 is defined as an operational, toy-level test of the non-cancellation principle and a
  first bounded FRW-facing sanity layer.

- **Claims structure.**  
  The three claims C2.1–C2.3 in the paper match the Phase 2 claims register: existence of a
  floor-induced residual, robustness under numerical controls, and a toy FRW embedding that
  is stable under the chosen mapping and settings. None of these claims are stated as physical
  predictions; they are framed as behavior of the **implemented system**.

- **Non-claims and scope boundaries.**  
  The non-claims section in the paper lines up with the Phase 2 non-claims and approximation
  contract: no identification of \(\varepsilon\) with a physical constant, no claim of continuum universality,
  no assertion of realistic field content, and no claim that the FRW module matches real data.

- **Reproducibility.**  
  The paper’s description of the run manifests, run IDs, and build system matches the Phase 2
  reproducibility docs and workflow guide: figures are traceable to tagged runs under
  `outputs/runs/<run_id>/` with recorded code state and configs, and the build path is a
  deterministic Snakemake target plus latexmk.

Overall, the paper’s internal story is consistent with the Phase 2 contracts and with the way Phase 2
is described in the global program docs.

## 4. Alignment with Stage 2 FRW and master verdicts

Stage 2 FRW and master verdicts emphasise:

- a broad, contiguous **FRW-viable band** on a 2048-point \(\theta\)-grid,
- structurally nontrivial but pre-data FRW corridors (the FRW data gate is closed),
- strongly redundant mechanism and FRW scalars on the joint grid,
- and a **negative-result** status for \(\theta_\star\) (inside the viable band but not specially selected).

The Phase 2 paper predates and lives “upstream” of the full Stage 2 FRW belts (which are built on
Phase 4 tables). Its FRW module is more modest: a simple background solver driven by the Phase 2
residual via a specified mapping.

Audit verdict:

- The Phase 2 FRW section and Claim C2.3 only assert that:
  - the chosen mapping yields FRW trajectories that remain numerically stable,
  - the residual can be carried into the FRW module without causing the solver to fail,
  - and the behavior is inspected under the stated settings.
- The paper **does not**:
  - claim a populated, data-conditioned FRW corridor,
  - claim a broad FRW viability band on a \(\theta\)-grid of the kind Stage 2 later explores,
  - claim selection of \(\theta_\star\) via FRW behavior,
  - or imply that the FRW module is tuned to real cosmological data.

Thus there is **no conflict** between the Phase 2 paper and the Stage 2 FRW verdicts:

- Phase 2’s FRW module is a **toy embedding demo** for one constrained residual and one
  mapping, which Stage 2 effectively supersedes with a richer Phase 4/Stage 2 FRW pipeline.
- Stage 2 does not contradict any Phase 2 claim; instead, it **extends** and reframes FRW-facing
  diagnostics at a later phase, with Phase 2 remaining as a bounded, internal test.

## 5. Scope and status language audit

From the introduction, scope sections, and conclusion:

- The paper consistently emphasises:
  - bounded scope;
  - operational non-cancellation, not derivation from first principles;
  - toy embeddings and testbeds, not external phenomenology.
- References to \(\theta\) and \(\theta_\star\) are framed as:
  - an external control parameter and optional anchor,
  - used to test **pipeline coherence** and phase dependence,
  - not as a physically selected or predicted value.
- Late sections explicitly list **required upgrades** before any physical interpretation:
  - mechanism upgrade (local formulation or symmetry),
  - universality (refinement / convergence),
  - mapping (physical normalization and calibration),
  - model upgrade (richer field content),
  - and data-connection upgrades.

This matches the Stage 2 master verdict’s view that:

- Phase 2 is a methodological foundation,
- the current toy pipelines are internally consistent but not yet predictive,
- and stronger interpretive targets (data gates, canonical measures, θ-selection) are deferred.

## 6. Potential future tightening (for a later editing rung)

This audit does not propose edits, but for future LaTeX rungs it may be useful to:

- Make one short, explicit cross-reference in the Phase 2 introduction or conclusion to the fact
  that later phases (Phase 4 + Stage 2 FRW belts) will provide more systematic FRW corridor
  analysis, so that the Phase 2 FRW demo is clearly positioned as a **first stub**.
- Ensure that any mentions of “FRW viability” in Phase 2 are clearly marked as **toy** viability
  under the specific mapping used, not as a general statement about cosmology.

At present, however, the existing language is already cautious, and there is no urgent misalignment
that demands immediate paper edits.

## 7. Verdict

For the Stage 2 snapshot:

- The Phase 2 paper accurately presents Phase 2 as a bounded, reproducible test of a global
  non-cancellation floor in a vacuum testbed with a toy FRW embedding.
- The three claims C2.1–C2.3, as stated in the paper, match the Phase 2 contracts and do not
  exceed what the implementation and Stage 2 diagnostics support.
- The non-claims and upgrade lists in the paper are consistent with the global program docs and
  Stage 2 master verdict: Phase 2 is a methodological foundation, not a full physical solution.

No contradictions were found between the Phase 2 paper and the current Stage 2 FRW and master
verdicts. Any future edits, if undertaken, can be limited to mild clarifications and cross-links rather
than substantive changes in claims.

---

## Phase 2 audit verdict (Stage 2 perspective, 2026-01-15)

From the Stage 2 paper-audit perspective, the Phase 2 paper, contracts, and current diagnostics support a clear verdict:

- The Phase 2 paper’s narrative around C2.1–C2.3 matches the Phase 2 contracts:
  - it presents the mode-sum residual as a toy, internal diagnostic,
  - it emphasises robustness and stability over interpretation,
  - and it explicitly avoids any real-data, scale-fixing, or θ\*-selection claim.
- Stage 2 FRW and joint-mechanism diagnostics:
  - are consistent with the bounded-FRW viability notion used in Phase 2,
  - clarify that current FRW corridors are pre-data and live in Phase 4/Stage 2 rather than in Phase 2,
  - and do not force any revision of Phase 2’s claims at this time.

Given this, Stage 2 does not currently recommend any change to the substance of the Phase 2 claims. Instead, it recommends:

- keeping Phase 2 labelled “Under Audit” at the global program level for forward-looking reasons:
  - to allow for future rungs that tie Phase 2’s FRW wrapper more explicitly into the mature Phase 4/Stage 2 FRW belts and any future data gates,
  - and to keep open the option of tightening, but not broadening, the Phase 2 story as the program’s FRW and measure layers evolve.

In other words:

- Phase 2 is internally coherent and modest as written,
- the “Under Audit” label reflects a deliberate conservatism and a desire for future tightening, not a current inconsistency,
- and any eventual promotion to “Locked” should be tied to a small, well-scoped audit belt that either confirms the present story or documents precise, limited adjustments.

