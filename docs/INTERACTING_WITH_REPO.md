# Interacting with the Origin Axiom Repository

This document explains how to use the repository safely and coherently: how to orient yourself in the phase structure, how to rebuild artifacts, how to add new work without breaking governance, and how to reason about what is and is not a claim.

If you are reading this, you should skim `README.md`, `docs/PROJECT_OVERVIEW.md`, `docs/STATE_OF_REPO.md`, and `docs/PHASES.md` first.

---

## 1. Who this repo is for

The repository is meant to be usable by several types of people:

- Authors and close collaborators who work directly on the core phases (Phase 0–5).
- External researchers who want to audit, reproduce, or extend specific phases.
- People who only want to run downstream Stage 2 diagnostics on top of locked Phase 3/4 outputs.
- Curious readers who mainly care about the conceptual structure and published PDFs.

The rules below are designed so that all of these groups can work in the same tree without stepping on each other.

---

## 2. Mental model of the repository

At the highest level there are three tiers:

- **Canonical phases (`phase0/`–`phase5/`)**  
  These directories hold the main program: governance (Phase 0), toy ensembles (Phase 1), mode-sum + FRW-style viability (Phase 2), mechanism module (Phase 3), FRW toy diagnostics (Phase 4 stub), and the interface/sanity layer (Phase 5). Claims are indexed in `docs/CLAIMS_INDEX.md` and in the Phase papers themselves.

- **Stage 2 diagnostic belts (`stage2/`)**  
  These modules run *downstream* of Phase 3/4 outputs. They never silently change Phase claims. Current belts include:
  - `stage2/frw_corridor_analysis`
  - `stage2/mech_measure_analysis`
  - `stage2/joint_mech_frw_analysis`
  - `stage2/frw_data_probe_analysis`  
  Their status and audit tables are documented in `stage2/docs/` (for example `STAGE2_OVERVIEW_v1.md`, `STAGE2_DOC_AUDIT_SUMMARY_v1.md`).

- **Experiments and legacy material (`experiments/`, scratch, etc.)**  
  These are non-canonical. They can contain archived attempts, exploratory scans, and prior flavors of the program. A concrete example is `experiments/phase3_flavor_v1/`, which is explicitly archived as a non-canonical flavor-sector Phase 3 experiment (see `experiments/phase3_flavor_v1/ARCHIVE_STATUS_v1.md`).

When in doubt, treat anything outside `phase0/`–`phase5/` and `stage2/` as suggestive, not binding.

---

## 3. How to run things safely

### 3.1 Phase papers and gates

Each Phase has two key ingredients:

- A **paper** under `phaseX/paper/` with a claims appendix and reproducibility notes.
- A **gate or build path** that regenerates the canonical artifacts (PDFs, tables, diagnostic figures).

Typical patterns (exact commands may differ by phase and are documented in the papers and local READMEs):

- Use `scripts/build_all_papers.sh` when you want to rebuild all Phase papers and their artifacts from a clean environment.
- For focused work, use the per-phase gate or driver documented in that Phase (for example, a small number of `phaseX/src/...` entry points).

General discipline:

- Never edit files in `phaseX/artifacts/` by hand; they are build products.
- If you change code or configuration that should affect a Phase artifact, re-run the relevant gate and verify the new artifact before treating it as canonical.
- If you are only reading, you can just open the PDFs and tables under `phaseX/artifacts/` and `phaseX/outputs/`.

### 3.2 Stage 2 diagnostics (downstream only)

Stage 2 modules live under `stage2/` and are designed to be **downstream**:

- They read Phase 3 and Phase 4 outputs (tables, masks, grids).
- They produce additional tables, plots, and documentation under `stage2/.../outputs/` and `stage2/docs/`.
- They do not rewrite Phase claims or Phase artifacts.

Typical interactions:

- Read `stage2/docs/STAGE2_OVERVIEW_v1.md` for the big picture.
- For a given belt (for example `frw_corridor_analysis`), read its local documentation and then invoke the rung scripts in `stage2/<belt>/src/`.
- Treat Stage 2 outputs as **diagnostic evidence** that may or may not later be promoted into a Phase. Promotion requires an explicit gate and documentation change, not an accidental script run.

If you are extending Stage 2, keep your work clearly separated as new rungs or modules, and document what they read and what they emit.

### 3.3 Experiments and scratch work

Anything under `experiments/` or ad-hoc scratch directories is *not* canonical:

- You may run and modify these at will.
- If some result turns out to be important, it should be migrated into a Phase or a Stage 2 module through a dedicated migration note (see `docs/PROJECT_OVERVIEW.md` and `stage2/docs/STAGE2_ARCHIVE_STATUS_v1.md`).

Avoid wiring experimental outputs directly into Phase gates without an explicit, documented migration.

---

## 4. Claims, non-claims, and how to read them

The repository distinguishes carefully between:

- **Claims** – formal statements with IDs (for example `P1-C1`, `P2-C3`) backed by an evidence trail, defined scope, and explicit non-claims.
- **Non-claims** – things explicitly *not* being asserted (for example, “this does not derive the Standard Model”).
- **Diagnostics** – numerical and visual summaries that illustrate behavior but are not themselves claims.

To navigate:

- Start with `docs/CLAIMS_INDEX.md` for the global map.
- For a given Phase, read:
  - the main narrative of the Phase paper,
  - the claims and non-claims appendix,
  - the reproducibility section that explains how to regenerate the evidence.

Stage 2 diagnostic belts do **not** introduce new claims by themselves. They may help promote or demote claims later, but only via explicit edits to the Phase papers and `docs/CLAIMS_INDEX.md`, not silently.

If you ever see a strong statement that is not supported by the claims ledger, treat it as a red flag and open an issue or add a doc-audit note rather than assuming it is canonical.

---

## 5. Adding new work

When you want to contribute code, analysis, or text, follow this decision process:

1. **Is it core to the phased program?**  
   - If yes, it probably belongs under `phase0/`–`phase5/`.  
   - You should:
     - define scope and non-claims,
     - update or draft claims if appropriate,
     - and ensure reproducibility.

2. **Is it a downstream diagnostic over existing Phase outputs?**  
   - If yes, it belongs under `stage2/` as a new belt or rung.  
   - Document clearly:
     - which Phase tables/artifacts it reads,
     - what new tables/plots it emits,
     - and how (if at all) it could influence promotion decisions.

3. **Is it speculative, exploratory, or not yet disciplined?**  
   - If yes, put it under `experiments/` or a clearly marked scratch area.  
   - If a path becomes promising, write a migration note and move it into a Phase or Stage 2 with full governance.

In all cases:

- Add or update local `README.md` files so future readers understand what lives in a directory.
- Keep code headers clear about what a script does, what it depends on, and what it produces.
- Log significant changes in `PROGRESS_LOG.md` with dates and minimal but precise summaries.

---

## 6. Safe ways to explore

If you are just trying to understand the program or validate ideas:

- Prefer reading **PDFs and tables** over inspecting internal intermediate files.
- When running code:
  - use fresh environments or throwaway branches,
  - avoid editing canonical artifacts by hand,
  - record any deviations from the documented pipelines.
- When experimenting with new ideas:
  - fork them into new scripts or notebooks instead of modifying existing, locked gates,
  - keep notes about what you tried so they can be archived or migrated cleanly.

This keeps the main line of the project predictable and auditable, while still leaving room for creative exploration.

---

## 7. Summary

- Phases (`phase0/`–`phase5/`) hold the canonical program and its claims.
- Stage 2 (`stage2/`) holds downstream diagnostic belts that never silently change claims.
- Experiments (`experiments/`) and scratch work are non-canonical and should be treated as such.
- Claims are centralized in `docs/CLAIMS_INDEX.md` and the Phase papers; nothing else magically upgrades itself into a claim.

When in doubt:

- Read the relevant Phase paper and its claims and reproducibility appendices.
- Run the appropriate gate or `scripts/build_all_papers.sh` instead of ad-hoc commands.
- Prefer interacting with results through documented artifacts and, where available, the Phase 5 interface and Stage 2 diagnostics, not through private or undocumented paths.

This is how we keep the origin-axiom program auditable, extendable, and honest about what it does and does not show.
## Additional navigation and audit tools

For readers who want a deeper structural or audit-level view of the repository:

- `docs/REPO_MAP_AND_ATLAS_v1.md` provides a directory-level map of the repo,
  including phase trees, Stage 2 belts, experiments, sandbox areas, and global
  build/gate scripts.

- `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md` summarises the Stage 2 diagnostic
  belts (FRW corridor, mech/measure, joint mech–FRW, FRW data-probe, θ★
  diagnostics, and the doc/repo audit belt) as downstream-only analyses that
  never mutate Phase 3/4 artifacts.

- `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` documents the Stage 2
  documentation audit CSVs and the manual doc-audit rungs applied on top. It is
  useful when preparing publication-grade passes or checking that central docs
  and links are consistent with the current repo state.

These tools are optional for everyday use but are part of the audit trail for
how the repository is maintained and interpreted over time.
