# Future Work and Roadmap

This document sketches where the Origin Axiom program is heading and how new work should be wired into the existing phased structure. It is not a claim ledger; it is a planning map.

The current repo implements Stage I (Phases 0–5) and a set of downstream Stage 2 diagnostic belts under `stage2/`. In addition, there is a notional Stage II for deeper or broader future work that does not yet exist in this repo.

The key principles are:

- Do not silently rewrite history: retire or archive instead of erasing.
- Keep claims gated and tied to explicit artifacts.
- Treat Stage 2 as diagnostic and downstream.
- Treat Stage II as hypothetical until it is actually implemented under version control.

---

## 1. Where we are now (Stage I + Stage 2)

Stage I (implemented in this repo):

- **Phase 0** – Governance, contracts, and claim discipline (no physics claims).
- **Phase 1** – Toy ensembles (locked).
- **Phase 2** – Mode-sum model plus bounded FRW-style viability diagnostics (under audit).
- **Phase 3** – Mechanism module (active).
- **Phase 4** – FRW toy diagnostics (stub).
- **Phase 5** – Interface and sanity layer (rung 0–1).

Stage 2 (implemented, non-canonical, strictly downstream):

- `stage2/frw_corridor_analysis/` – FRW corridor and θ-family diagnostics on the Phase 4 grid.
- `stage2/mech_measure_analysis/` – Mechanism/measure diagnostics over Phase 3 tables.
- `stage2/joint_mech_frw_analysis/` – Joint mech–FRW analysis on a shared θ-grid.
- `stage2/frw_data_probe_analysis/` – FRW data-probe audit versus viability masks.
- `stage2/doc_repo_audit/` – Documentation and repo-structure audit, summarized in `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` and `stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md`.

For orientation and current status, see also:

- `docs/PHASES.md`
- `docs/STATE_OF_REPO.md`
- `docs/CLAIMS_INDEX.md`
- `stage2/docs/STAGE2_OVERVIEW_v1.md`

---

## 2. Possible Stage II directions (not yet implemented)

Stage II is a placeholder name for future expansions that would only be attempted if the existing Phase 0–5 and Stage 2 belts survive an honest audit.

Examples of possible Stage II directions include:

- **Deeper field-theoretic embedding:** formally embedding the mechanism in a more realistic field-theory or many-body setting, beyond the current toy models.
- **Broader sector contact:** structured extensions into additional sectors (for example, more detailed Standard Model structure, beyond the archived flavor experiment).
- **Multi-systems comparison:** parallelizing the axiom test across qualitatively different systems, checking whether the same non-cancellation structure appears anywhere other than the current toy pipelines.
- **Societal and ethical layers:** if the axiom survives as a serious organizing principle, designing interfaces, governance, and safeguards for how its implications are communicated and deployed.

As of 2026-01-10 there is **no Stage II directory tree** and no Stage II claims. Any future Stage II work must:

1. Declare its scope and non-claims.
2. Specify canonical artifacts and reproducibility gates.
3. Be wired into the governance discipline defined in Phase 0.
4. Be kept clearly separate from experiments and scratch work.

---

## 3. Stage 2 – Current belts and near-term roadmap

Stage 2 is already implemented and is where most near-term diagnostic work will happen. It is important to keep the semantics clear:

- Stage 2 is **diagnostic and downstream** of Phases 3 and 4.
- Stage 2 outputs can be strong evidence **for or against** promoting a result, but they are not themselves Phase claims.
- Promotion of any Stage 2 result into a Phase paper must go through explicit gates plus normal git and `PROGRESS_LOG.md` logging.

Below is a brief roadmap by belt.

### 3.1 FRW corridor axis (`stage2/frw_corridor_analysis/`)

Status:

- Implements rungs over the Phase 4 FRW grid:
  - family census and fractions,
  - overlaps between FRW-viable, LCDM-like, and toy corridors,
  - contiguity of families in θ,
  - stride-robustness and smoothing tests,
  - θ* alignment diagnostics,
  - and corridor figures (ideally as vector PDFs).

Near-term roadmap:

- Finalize figures as PDFs (vector) and ensure they are reproducible via a small, documented script.
- Decide whether to treat the current corridor definitions as provisional or lock them for a given rung.
- Tighten the narrative link between the FRW corridor doc under `stage2/docs/` and the Phase 4 FRW paper.

Promotion gate:

- Promotion of any FRW corridor result into Phase papers is gated by an explicit FRW promotion gate document (for example `docs/FRW_CORRIDOR_PROMOTION_GATE_v1.md`) and must be accompanied by:
  - a clear statement of what is being promoted,
  - a pointer to the Stage 2 rung and artifacts,
  - and a corresponding update to the relevant Phase doc and claim index.

### 3.2 Mechanism/measure axis (`stage2/mech_measure_analysis/`)

Status:

- Inventories Phase 3 tables and column types.
- Identifies measure-like and flag-like candidates.
- Analyzes θ-profiles of these candidates.
- Proposes a small set of preferred measure candidates in `stage2_mech_rung6_phase3_preferred_measure_candidates_v1.csv`.

Near-term roadmap:

- Cross-reference the preferred candidates with the Phase 3 paper and its appendices, ensuring no contradictions with how the mechanism is presented.
- Decide whether any candidate deserves a promotion to a Phase 3 claim, or whether they remain Stage 2 diagnostics only.
- If none are ready for promotion, record that explicitly in the doc belt (for example, in a Stage 2 mech/measure summary doc).

### 3.3 Joint mech–FRW axis (`stage2/joint_mech_frw_analysis/`)

Status:

- Builds a joint θ-grid aligning Phase 3 mechanism outputs and Phase 4 FRW masks.
- Provides family summaries across:
  - FRW-viable,
  - LCDM-like,
  - toy corridor,
  - overlaps such as CORRIDOR_AND_VIABLE and CORRIDOR_AND_LCDM.
- Computes correlations between mechanism variables and FRW diagnostics.

Near-term roadmap:

- Interpret the joint correlations more systematically:
  - assess which correlations are structurally nontrivial versus trivially induced by shared dependence on θ or E_vac,
  - check robustness under simple rescalings and transformations.
- Decide whether the joint patterns suggest any new Stage 2 belt or Phase gate changes.

### 3.4 FRW data-probe audit (`stage2/frw_data_probe_analysis/`)

Status:

- Audits the FRW data-probe mask versus the FRW viability mask.
- Enumerates how well the data-probe columns discriminate or fail to discriminate viable from non-viable regions.

Near-term roadmap:

- Decide whether any probe is effectively redundant (for example, if it always mirrors the FRW viability flag).
- Consider small adjustments to the data-probe design (under the Phase 4 paper’s governance) if the Stage 2 audit reveals systematic blind spots or redundancies.
- Document any such adjustments in both Phase 4 and Stage 2 docs.

### 3.5 Documentation and archive audit (`stage2/doc_repo_audit/`)

Status:

- Inventories documentation files and their roles.
- Identifies broken references and orphan candidates.
- Collects open narrative threads from TODOs and similar markers.
- Summarized in:
  - `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md`
  - `stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md`

Near-term roadmap:

- Use the audit CSVs to:
  - fix or retire broken references,
  - archive non-canonical or legacy docs cleanly,
  - close or explicitly mark open narrative threads.
- Re-run the audit after any major refactor or promotion pass.

---

## 4. Process roadmap – how work should move

Beyond specific belts, the roadmap is also about **how** work should move through the program.

### 4.1 From experiment to Stage 2

If you create a new experiment (for example under `experiments/`):

1. Clearly mark it as non-canonical and describe its scope and non-claims in a local README.
2. When it stabilizes and becomes useful as a diagnostic lens, either:
   - migrate it into a Stage 2 belt under `stage2/`, or
   - archive it with an explicit status doc if it is no longer active.

No experiment should quietly masquerade as a Phase claim.

### 4.2 From Stage 2 to Phase promotion

If a Stage 2 result appears robust and important enough to influence Phase claims:

1. Draft a promotion note that:
   - names the Stage 2 rung and artifacts,
   - explains what is being promoted and why,
   - spells out the impact on the relevant Phase doc and claims.
2. Update the relevant Phase doc (for example, Phase 3, Phase 4, or Phase 5) and `docs/CLAIMS_INDEX.md`.
3. Log the change in `PROGRESS_LOG.md`.
4. Re-run any relevant Stage 2 belts to ensure consistency.

Promotion is a deliberate act, not an automatic consequence of a pretty plot.

### 4.3 From internal repo to external publication

For external publication:

1. Lock the relevant Phase paper and appendices with clear claim statements and evidence.
2. Ensure that all figures and tables in the paper are generated from scripts and data under version control.
3. Use Stage 2 belts to stress-test any claims you intend to publish.
4. Consider a separate “externalization” checklist doc that must be satisfied before submitting.

No external claim should be stronger than what is actually present in the locked Phases and Stage 2 belts.

---

## 5. How to extend this roadmap

This document should be updated when:

- A new Stage 2 belt is added or an existing belt changes shape.
- A Stage 2 result is promoted into a Phase doc.
- A Stage II direction is concretely instantiated under version control.
- A major refactor changes the layout or semantics of phases.

When you update it, keep the following discipline:

- Do not overwrite history; describe what changed and why.
- Keep the Phase and Stage terminology aligned with `docs/PHASES.md` and `docs/STATE_OF_REPO.md`.
- Make sure any new directions are reflected in local READMEs and claim indices where relevant.

