# Phase 3 alignment memo (mechanism scope, claims, outputs, and paper)

Status (2026-01-11): This memo records how the Phase 3 mechanism paper, scope/claims/contract/reproducibility documents, and the current repository and Stage 2 diagnostics align. It is descriptive only and does not introduce new claims.

## 1. Inputs used for this alignment

This memo is based on:

- `phase3/README.md` – Phase 3 overview as the canonical mechanism module.
- `phase3/SCOPE.md` – Phase 3 scope definition and non-claims.
- `phase3/CLAIMS.md` – Phase 3 claims register for the mechanism module.
- `phase3/MECHANISM_CONTRACT.md` – detailed mechanism contract (non-cancellation floor, binding certificate, amplitudes and diagnostics).
- `phase3/ROLE_IN_PROGRAM.md` – Phase 3 role in the Origin Axiom ladder.
- `phase3/REPRODUCIBILITY.md` – Phase 3 reproducibility and provenance.
- `phase3/PHASE3_RUNG2_MECHANISM_A_INSTABILITY_PENALTY.md` – rung-level design note for a specific instability-penalty refinement.
- `phase3/paper/main.tex` and section files, together with:
- `artifacts/origin-axiom-phase3.pdf` – the Phase 3 mechanism paper built from the LaTeX sources.
- Phase 3 outputs and tables under `phase3/outputs/tables/`, including:
  - `mech_baseline_scan.csv`
  - `mech_binding_certificate.csv`
  - and related amplitude and diagnostic tables referenced in the paper and Stage 2.
- Stage 2 diagnostics that sit downstream of Phase 3, in particular:
  - `stage2/mech_measure_analysis/docs/STAGE2_MECH_MEASURE_SUMMARY_v1.md`
  - `stage2/joint_mech_frw_analysis/docs/STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md`
  - `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md`
  - `stage2/docs/STAGE2_OVERVIEW_v1.md`
  - `stage2/theta_star_analysis/docs/STAGE2_THETA_STAR_ALIGNMENT_v1.md`.

This memo is concerned with alignment between these documents and artifacts; it does not modify any mechanism, tables, or Stage 2 computations.

## 2. Scope: Phase 3 as mechanism module, not flavor sector

`phase3/SCOPE.md` defines Phase 3 as the mechanism module: its job is to implement a non-cancellation mechanism that enforces a vacuum floor, construct amplitude diagnostics over θ, and expose binding certificates and related scalars that can be used downstream by FRW diagnostics (Phase 4) and interface layers (Phase 5). It explicitly states that Phase 3 is not a flavor module, does not calibrate flavor patterns, and does not attempt to match Standard Model hierarchies or particle phenomenology. Any such attempts are relegated to archived experiments under `experiments/`.

`phase3/ROLE_IN_PROGRAM.md` echoes this: Phase 3 is described as the “mechanism hinge” between Phase 2 bounded vacuum constructions and Phase 4 FRW-facing diagnostics. It emphasises that Phase 3’s role is to provide a well-controlled amplitude floor and mechanism-derived scalars, not to fix θ★ or make direct observational predictions.

The Phase 3 paper (as built in `artifacts/origin-axiom-phase3.pdf`) is similarly structured: its introduction and “role in program” style sections describe Phase 3 as implementing and stress-testing the non-cancellation mechanism and producing mechanism-derived diagnostics, with explicit deferrals of any flavor or phenomenology ambitions to future or separate work. There is no evidence that the paper claims a canonical flavor sector or treats Phase 3 as a flavor-calibration phase.

Global docs under `docs/PHASES.md`, `docs/STATE_OF_REPO.md`, and `docs/CLAIMS_INDEX.md` have been updated to describe Phase 3 as the mechanism module and to label the flavor-sector experiment under `experiments/phase3_flavor_v1/` as archived and non-canonical. Under this interpretation, Phase 3 scope, role documents, paper narrative, and global docs are aligned: Phase 3 is the mechanism module and does not own flavor physics claims.

## 3. Mechanism contract and claims vs. paper construction and outputs

`phase3/MECHANISM_CONTRACT.md` spells out the contract for the Phase 3 mechanism: how the non-cancellation floor is implemented, how amplitudes and derived scalars are defined over θ, what the binding certificate encodes, and what diagnostics (e.g. baseline amplitudes, penalties, and binding measures) Phase 3 is responsible for producing. It also describes allowed parameter ranges, expected regularity properties, and what constitutes a valid binding regime.

`phase3/CLAIMS.md` organises Phase 3 claims around this contract. Typical classes of claims include:

- Existence and well-definedness of the mechanism implementation and vacuum floor under specified conditions.
- Existence and regularity of mechanism-derived scalars over θ (e.g. baseline amplitudes and penalties as continuous or at least well-behaved functions on the sampled grid).
- Existence of binding regimes characterised by a binding certificate table that meets specified diagnostic checks.
- Non-claims that limit interpretation: Phase 3 does not promote any single scalar to a canonical measure over θ and does not assert that θ★ is selected or preferred by the mechanism in isolation.

The Phase 3 paper’s mechanism construction and results sections describe an implementation of the mechanism that matches this contract: it defines a vacuum floor and a set of scalars (baseline, penalty, and binding quantities) derived from the mechanism and presents tables or figures (via `phase3/outputs/tables/*.csv`) that expose these quantities over θ. The paper describes binding regimes and penalties in ways that match the contract’s expectations (e.g. boundedness, smoothness, and diagnostic flags), and the objects it uses (baseline scans, binding certificates) correspond to the actual CSVs under `phase3/outputs/tables/`.

The Stage 2 mech/measure analysis confirms that these scalars behave as claimed: `STAGE2_MECH_MEASURE_SUMMARY_v1.md` and related CSVs show that Phase 3 amplitude columns are well-behaved, bounded, and numerically stable, and that they can be treated as candidate measures or flags for Stage 2 diagnostics. At the same time, the Stage 2 mech rungs are careful not to promote any single scalar to a canonical θ-measure, in line with Phase 3 non-claims.

On this axis, `MECHANISM_CONTRACT.md`, `phase3/CLAIMS.md`, the Phase 3 mechanism paper, and the actual outputs under `phase3/outputs/tables/` are aligned: they describe the same mechanism, the same scalars, and the same diagnostic expectations, and they all refrain from over-interpreting any scalar as a final measure.

## 4. Reproducibility and environment vs. implementation and Stage 2

`phase3/REPRODUCIBILITY.md` describes how to run the Phase 3 mechanism code to generate the tables and figures used in the paper: environment setup (pinned dependencies), key scripts for baseline scans and binding certificates, and how to regenerate the Phase 3 paper and artifacts from `phase3/paper/main.tex` and the outputs. It emphasises that mechanism tables used as evidence must be produced by deterministic scripts under version-controlled configs and that run provenance and logs are recorded.

The Phase 3 repo layout under `phase3/` matches this: there are source directories for the mechanism implementation, configuration files, outputs under `outputs/tables/`, and the paper sources under `paper/`. The Stage 2 mech/measure and joint analysis scripts read these Phase 3 tables as inputs, which is an additional check that the tables are well-formed and stable enough to support downstream diagnostics.

From the paper’s methods and results sections, figures and tables are presented as outputs of reproducible mechanism scans and diagnostics, not as hand-picked curiosities. This is consistent with `REPRODUCIBILITY.md` and the presence of structured CSVs consumed by Stage 2 scripts.

Taken together, Phase 3 reproducibility docs, repo structure, mechanism paper, and Stage 2 usage of Phase 3 tables are aligned: Phase 3 artifacts are treated as reproducible, script-generated objects with clear provenance, and Stage 2 depends on them in a way that would fail visibly if reproducibility assumptions were violated.

## 5. Relation to Stage 2 mech/measure and joint mech–FRW diagnostics

Stage 2 mech/measure analysis (`stage2/mech_measure_analysis/`) and joint mech–FRW analysis (`stage2/joint_mech_frw_analysis/`) are explicitly downstream of Phase 3 and Phase 4. They read Phase 3 tables such as `mech_baseline_scan.csv` and `mech_binding_certificate.csv` and Phase 4 FRW tables to analyse the behavior and correlations of these quantities.

The key Stage 2 findings as recorded in `STAGE2_MECH_MEASURE_SUMMARY_v1.md`, `STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md`, `STAGE2_BELT_OVERVIEW_v1.md`, and the θ★ alignment doc are:

- Phase 3 amplitudes and binding-related scalars are smooth, bounded, and numerically well-behaved over the θ-grid, making them good diagnostics.
- Several amplitude columns behave as “probability-like” candidates (bounded, non-degenerate distributions), and Stage 2 splits them into measure-like vs flag-like candidates, but explicitly does not promote any one of them to a canonical θ-measure.
- On the joint grid built from Phase 3 and Phase 4 tables, FRW scalars (such as effective vacuum energy, ω_Λ, and age_Gyr) and mechanism amplitudes are very strongly correlated (|r| close to 1 for several pairs), indicating that the mechanism scalars essentially reparameterise FRW scalars on the current grid.
- θ★ lies within the FRW-viable band and within ranges where mechanism amplitudes behave regularly but is not singled out or specially preferred by any present machinery.

These findings are consistent with Phase 3’s claims and non-claims:

- Phase 3 claims the existence and regularity of mechanism-derived scalars and binding regimes, which Stage 2 confirms.
- Phase 3 does not claim a canonical θ-measure or a special status for θ★; Stage 2 diagnostics explicitly record the negative result that no special θ★ selection emerges in the current toy setup.

From an alignment perspective, there is no contradiction between Phase 3 mechanism claims and Stage 2 mech/joint diagnostics; Stage 2 refines and quantifies Phase 3’s narrative (mechanism-derived scalars are smooth and FRW-correlated) without promoting them beyond the boundaries set by Phase 3 and the global docs.

## 6. Non-claims, boundaries, and Phase 3 flavor archive

Phase 3 documents and the paper enforce several important non-claims:

- Phase 3 does not fix θ★ or assert that θ★ or any particular irrational (e.g. φ or φ^φ) is physically selected. Any such selection would require additional principles and phases.
- Phase 3 does not claim a canonical measure over θ; its scalars are diagnostic quantities that can be used in Stage 2 belts and future phases.
- Phase 3 does not make direct claims about realistic cosmological data or observations; it operates in a toy mechanism world whose outputs are fed into FRW diagnostics and interface layers downstream.
- Flavor-sector experiments under `experiments/phase3_flavor_v1/` are explicitly archived and non-canonical; they are not part of Phase 3’s mechanism claims.

Global docs (`docs/ARCHIVE.md`, `stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md`, and the archived flavor SCOPE) are consistent with this: they mark the flavor experiment as archived, separated from the canonical Phase 3 mechanism, and reiterate that Phase 3’s canonical identity is the mechanism module.

Stage 2 θ★ alignment diagnostics further reinforce a conservative interpretation of Phase 3: they record that θ★ lies within the viable band but is not singled out and categorise this as a negative-result sanity check, not a hidden “prediction”.

Under this reading, Phase 3 scope, mechanism contract, claims register, reproducibility docs, paper, global docs, and Stage 2 diagnostics all draw the same boundaries, and there is no evidence that any Phase 3 document over-claims relative to these guardrails.

## 7. Potential future doc rungs (not yet executed)

This memo suggests, but does not enact, the following documentation rungs for future passes:

- Add a short pointer from `phase3/SCOPE.md` or `phase3/README.md` to `phase3/PHASE3_ALIGNMENT_v1.md` as the canonical alignment memo for Phase 3.
- If new mechanism variants or additional scalars are introduced, ensure that `phase3/MECHANISM_CONTRACT.md` and `phase3/CLAIMS.md` are updated first and that the paper and Stage 2 diagnostics are brought into line with them only afterwards.
- If future work promotes any mechanism-derived scalar to a canonical θ-measure, introduce this as a separate, tightly scoped promotion rung with explicit Phase 0 gates and updates to Phase 3 and Phase 5 claims and non-claims, rather than retrofitting existing text.

These steps are deferred to later doc-audit or promotion rungs and do not change the current Phase 3 scope, mechanism contract, claims, or reproducibility contract.
