# Future Work and Roadmap

This document sketches where the Origin Axiom program might go next and how to think about future rungs. It should be read together with:

- [`README.md`](../README.md) for the high-level story and current layout,
- [`docs/PROJECT_OVERVIEW.md`](PROJECT_OVERVIEW.md) for Stage I structure,
- [`docs/PHASES.md`](PHASES.md) for per-phase scope and non-claims,
- [`docs/STATE_OF_REPO.md`](STATE_OF_REPO.md) for current status,
- [`docs/CLAIMS_INDEX.md`](CLAIMS_INDEX.md) for the claim map across phases.

Nothing in this file is a claim. It is a catalogue of **questions, possible rungs, and promotion paths**.

---

## 1. Where Stage I stands

Stage I is the current program instantiated in this repo:

- Phase 0 — governance and specification (locked),
- Phase 1 — toy ensembles (locked),
- Phase 2 — mode-sum model + bounded FRW diagnostics (under audit),
- Phase 3 — mechanism module (active),
- Phase 4 — FRW toy diagnostics (stub),
- Phase 5 — interface and sanity layer (early rungs),
- Stage 2 — downstream diagnostic belts under [`stage2/`](../stage2/) (in progress, non-canonical).

The canonical narratives are the Phase papers under [`artifacts/`](../artifacts/). Stage 2 artifacts are **diagnostic only** until explicitly promoted via Phase 0 governance.

---

## 2. Stage 2 (current diagnostic belts)

Stage 2 lives under [`stage2/`](../stage2/) and is strictly downstream of Phase 3 and Phase 4. Each belt has its own summary in [`stage2/docs/`](../stage2/docs/):

- [`STAGE2_OVERVIEW_v1.md`](../stage2/docs/STAGE2_OVERVIEW_v1.md) — global Stage 2 overview,
- [`STAGE2_FRW_CORRIDOR_SUMMARY_v1.md`](../stage2/docs/STAGE2_FRW_CORRIDOR_SUMMARY_v1.md) — FRW corridor belt,
- [`STAGE2_MECH_MEASURE_SUMMARY_v1.md`](../stage2/docs/STAGE2_MECH_MEASURE_SUMMARY_v1.md) — mechanism/measure belt,
- [`STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md`](../stage2/docs/STAGE2_JOINT_MECH_FRW_SUMMARY_v1.md) — joint mech–FRW belt,
- [`STAGE2_FRW_DATA_PROBE_SUMMARY_v1.md`](../stage2/docs/STAGE2_FRW_DATA_PROBE_SUMMARY_v1.md) — FRW data-probe audit,
- [`STAGE2_DOC_AUDIT_SUMMARY_v1.md`](../stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md) — doc-audit belt (inventory, broken refs, orphans, open threads),
- [`STAGE2_ARCHIVE_STATUS_v1.md`](../stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md) — map of canonical vs archived areas.

### 2.1 Stage 2 goals

Stage 2 rungs aim to:

- probe robustness of Phase 3 and Phase 4 outputs,
- map correlations and “corridors” without tightening claims,
- reveal failure modes and blind spots in the current constructions,
- surface documentation and governance gaps via the doc-audit belt.

They are intentionally **conservative**: any interesting pattern is treated as a hint for future work, not as an automatic claim upgrade.

### 2.2 Promotion paths from Stage 2 to Phases

If a Stage 2 result seems strong enough to influence a Phase, the promotion path should look like this:

1. **Proposal note**  
   - Create a short proposal (e.g. under `docs/` or `stage2/docs/`) describing:
     - which Stage 2 artifact is in play,
     - what change it would imply to which Phase,
     - what additional tests or scans would be needed.

2. **Gate definition**  
   - Add or update a Phase 0 style gate document (for example, a “FRW Corridor Promotion Gate” in `docs/` or `phase4/`) that lists:
     - required diagnostics,
     - acceptable tolerances,
     - explicit non-claims that must remain.

3. **Execution and replication**  
   - Run the necessary Stage 2 rungs and any new scripts; document them in the relevant `stage2/docs/STAGE2_*` file and in [`PROGRESS_LOG.md`](../PROGRESS_LOG.md).  
   - Ideally, have another person or future rung replicate the result.

4. **Phase paper update**  
   - Only after the gate is satisfied should the corresponding Phase paper under [`artifacts/`](../artifacts/) be updated.  
   - Update [`docs/PHASES.md`](PHASES.md) and [`docs/CLAIMS_INDEX.md`](CLAIMS_INDEX.md) to reflect any new or strengthened claims.

If a result fails the gate or turns out to be fragile, it should still be logged (with a clear note) so that future readers know why it was not promoted.

---

## 3. Possible Stage II directions

**Stage II** refers to possible future programs beyond the current Stage I ladder. It is distinct from the Stage 2 diagnostic belts, which are already implemented.

Nothing in this section is scheduled; these are **candidate trajectories** conditioned on Stage I outcomes.

### 3.1 Deepening the mechanism module

If the Phase 3 mechanism module remains coherent and useful after further scrutiny, Stage II could include:

- richer mechanism families exploring different non-cancellation structures,
- more detailed scaling and stability analyses across wider parameter ranges,
- coupling the mechanism to additional toy sectors (still clearly toy, not yet SM-level).

All such work would require new rungs, updated claims tables, and clear non-claims in [`docs/PHASES.md`](PHASES.md).

### 3.2 Beyond toy FRW backgrounds

If the FRW toy diagnostics in Phase 4 and the Stage 2 corridor/data-probe belts prove robust:

- extend FRW constructions to more realistic expansion histories,
- investigate how sensitive the viability masks are to changes in model assumptions,
- explore whether any corridor-like structures survive under these perturbations.

Any move toward contact with real cosmological data would need:

- explicit data provenance,
- careful statistical treatment,
- a very conservative claim set documented in new gates and Phase docs.

### 3.3 Interface, tooling, and audit infrastructure

Independent of physics depth, there is room for a Stage II focused on infrastructure:

- more formalized gating/CI flows that automatically check:
  - reproducibility of canonical outputs,
  - integrity of Stage 2 diagnostics,
  - documentation consistency,
- richer “interface” layers in Phase 5:
  - dashboards or notebooks that make the program easier to audit,
  - scripted checks that verify claim–artifact wiring.

This type of Stage II is about making the program more **auditable and extensible**, not about new physics claims.

### 3.4 Revisiting flavor-sector structure

Flavor-sector attempts currently live in the archived experiment under [`experiments/phase3_flavor_v1/`](../experiments/phase3_flavor_v1/), with status documented in [`experiments/phase3_flavor_v1/ARCHIVE_STATUS_v1.md`](../experiments/phase3_flavor_v1/ARCHIVE_STATUS_v1.md). They are **non-canonical**.

A future Stage II could revisit flavor in a more disciplined way, but only if:

- Stage I plus Stage 2 belts reveal a compelling structural reason to look there, and
- a new Phase or Stage declaration is made with:
  - clear scope,
  - explicit non-claims,
  - clean reproducibility gates.

---

## 4. Open questions that guide the roadmap

The following questions are deliberately broad and should be treated as guiding prompts, not assumptions:

- **Vacuum structure**  
  - Can the non-cancelling twist be characterized in a way that is stable under different toy ensembles and mechanism realizations?

- **Corridor robustness**  
  - Do apparent “corridors” of θ survive when:
    - the mode-sum model is perturbed,
    - FRW diagnostics are varied,
    - and Stage 2 belts are re-run with stricter thresholds?

- **Mapping layers**  
  - Is there a principled way to move between:
    - mechanism-level quantities,
    - FRW toy diagnostics,
    - and any potential future interface to richer sectors (without over-claiming)?

- **Program longevity**  
  - How can we ensure that, even if the core axiom is ultimately rejected, the methods, gates, and diagnostic structure remain reusable for other work?

Progress on these questions should be logged in [`PROGRESS_LOG.md`](../PROGRESS_LOG.md) and, when stable, reflected in updates to the Phase papers and Stage 2 docs.

---

## 5. How to propose future work

If you want to propose a new rung, Stage 2 belt, or Stage II direction:

1. Draft a short **proposal note** (for example in `docs/` or `stage2/docs/`) that states:
   - scope,
   - allowed claim types,
   - explicit non-claims,
   - expected artifacts and scripts.

2. Reference this file and the relevant Phase/Stage docs to show where it fits.

3. Open an issue or submit a pull request that:
   - adds the note,
   - sketches the gating strategy,
   - and, if ready, includes initial code or diagnostics.

4. Once merged, log the new direction in [`PROGRESS_LOG.md`](../PROGRESS_LOG.md).

This keeps the roadmap **living but disciplined**: ideas are welcomed, but only become part of the canonical story once they satisfy the same standards as the existing phases.


## Phase 5 roadmap companion

For a more detailed narrative of how Phase 5 should build on the existing
Phase 3–4 stack (mechanism + FRW toy corridors) without retroactively changing
their roles, see:

- `docs/phase5_roadmap.md` – Phase 5 roadmap from FRW toy corridors to
  data-contact.

This roadmap is planning-level text that complements, but does not replace, the
Phase 5 paper and governance docs.

---

## Consolidating open threads and TODOs

As part of the Stage 2 documentation/repo audit, open threads and TODO/TBD
items discovered in various Phase and Stage docs are being consolidated into
this roadmap where possible. The intent is:

- to keep **public-facing phase documents** focused on established scope and
  claims, and
- to collect **future work and unresolved questions** here, under an explicit
  “future work” contract.

The Stage 2 doc-audit belt tracks which files still contain TODO/TBD-style
markers and which have been cleaned up or redirected. For details, see:

- `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` (including the “Doc-audit status”
  section), and
- `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md` for the role of the doc/repo audit
  belt.

Future rungs may move or rephrase additional TODO/TBD paragraphs from phase
docs into this roadmap, but the canonical place to look for planned work and
open questions is here.
