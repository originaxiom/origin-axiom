# Origin Axiom — Commit History Atlas (v1, 2025-12 → 2026-01)

This atlas is a narrative map of the Git history for the `origin-axiom` Stage I repo from the first public skeleton to the Stage 2 doc-audit belts.

It is not a replacement for `git log`, and it does not try to rewrite history. Instead, it clusters the existing commits into a few coarse “epochs” so that a reader (or future you) can jump from the governance / phase docs straight into the relevant part of the commit history when auditing claims or reconstructing how a decision was made.

---

## 1. Scope and data snapshot

- Log source: `commit_log_full.txt` (exported from `git log` in early 2026-01).
- Time span: **2025-12-09 → 2026-01-12**.
- Total commits: **420**.
- Authors: predominantly `originaxiom`, with a small number under `Driteroi` and `biri` (same human, different local Git configs).
- Coverage: this atlas focuses on the **Stage I repo** after the legacy migration, not the pre-split / archived monolith.

The atlas is intentionally coarse; it groups clusters of commits with similar dates and themes into a handful of epochs and gives example commit messages from each.

---

## 2. How to use this atlas

- When reading **Phase papers** or **global docs** and you hit a reference like “see Phase 2 structural audit” or “Stage 2 FRW corridors,” you can:
  - look up the corresponding epoch below,
  - scan the example commit subjects,
  - then drop to `git log` around those dates if you need line-level provenance.

- When auditing a **claim** in `phase0/CLAIMS.md` or a **promotion decision** in Stage 2 docs:
  - identify which phase / belt the claim sits in,
  - find the matching epoch (Phase 1–2 pipelines, Stage 2 belts, doc-audit, etc.),
  - and use commit subjects as signposts into the history.

- When planning **future phases** or **Stage II**:
  - this atlas acts as a compact memory of how quickly the repo structure hardened,
  - what kinds of changes required multiple passes,
  - and which “reorg” epochs already happened (so we don’t re-do them blindly).

The atlas is descriptive, not prescriptive. It does not change the Git history and it does not impose any new governance rules beyond Phase 0.

---

## 3. Epoch map (high-level)

We partition the 420 commits into seven coarse epochs:

1. **Epoch 0 — Toy Universe & Papers A–C** (2025-12-09 → 2025-12-15)
2. **Epoch 1 — Acts IV–VII & early phase naming** (2025-12-16 → 2025-12-24)
3. **Epoch 2 — Phase 1–2 pipelines & FRW comparison** (2025-12-25 → 2025-12-31)
4. **Epoch 3 — Phase 0 governance & Phase 2 structural audit** (2026-01-02 → 2026-01-04)
5. **Epoch 4 — Phase 3 mechanism, Phase 4 FRW stub, Phase 5 interface** (2026-01-05 → 2026-01-07)
6. **Epoch 5 — Stage 2 diagnostic belts (FRW, mech, joint, data)** (2026-01-08 → 2026-01-10)
7. **Epoch 6 — Doc audit, Belt F/G, FRW anchors** (2026-01-11 → 2026-01-12)

The boundaries are approximate but match visible clusters in `git log` (by date and by commit subjects).

---

## 4. Epoch details

### 4.1 Epoch 0 — Toy Universe & Papers A–C (2025-12-09 → 2025-12-15)

**Theme.**  
First appearance of Origin Axiom as a Toy Universe project: 1D twisted scalar models, hard constraints, early LaTeX skeletons (Papers A–C), and a very exploratory style. Governance is informal; there is no Phase 0 yet and no corridor language.

**Typical work in this epoch.**

- Build the initial code and paper skeletons for a φ^φ-style constraint and 1D/3D toy lattices.
- Run early vacuum scans and document mean-zero vs non-cancelling experiments.
- Start a Toy Universe paper structure and basic reproducibility notes.

**Example commit subjects.**

- `Initial commit: Origin Axiom docs and Toy Universe v0.1 skeleton`
- `Fix toy_universe_lattice package exports and add demo runner`
- `Add energy functional and Origin Axiom hard constraint demo`
- `Add first analysis script for Toy Universe v0.1`
- `Clean up docs and GitHub math formatting for Origin Axiom and Toy Universe v0.1`
- `Add conceptual Origin Axiom LaTeX skeleton and refs`

This epoch is historically important but **non-canonical** in the current Phase 0–5 staging; much of it lives in the legacy archive and in the early conceptual PDFs.

---

### 4.2 Epoch 1 — Acts IV–VII & early phase naming (2025-12-16 → 2025-12-24)

**Theme.**  
The project briefly takes an “Acts I–VII” dramaturgy: effective vacuum, FRW histories, and early attempts at theta-star bridges. These commits predate the clean Phase 0–5 decomposition but are the seed of the later FRW corridor and vacuum–FRW mapping work.

**Typical work in this epoch.**

- Build an “effective vacuum” story: microcavities, observable bands, and early FRW comparisons.
- Structure results into “Acts” with R1–R24 style rungs.
- Explore θ-band scans and first references to ΛCDM-like consistency, before the later toy FRW machinery is formalized.

**Example commit subjects.**

- `Lock vacuum bridge: theta_star core summary and effective scalingmicrocavity`
- `R2: microcavity-backed effective vacuum and FRW histories`
- `R3: FRW observables from effective vacuum`
- `R4: effective vacuum theta-star band scan`
- `R4: effective vacuum theta-band scan and figure`
- `R5: effective vacuum patch ensemble stats and writeup`
- Later in this band: `R9: theta_star bridge summary (Act II/III snapshot)`, `Act VI: theta* observable corridor and lambdaCDM consistency (R24)`, `Act VII (Gate 2): toy matter sector + growth sanity window`

These “Act” commits are now treated as **historical precursors** rather than canonical phases; the Phase 0 governance rewrite later reinterprets and fences them.

---

### 4.3 Epoch 2 — Phase 1–2 pipelines & FRW comparison (2025-12-25 → 2025-12-31)

**Theme.**  
The repo crystallizes into Phase 1 and Phase 2: toy ensembles with binding on/off tests, and a first reproducible Phase 2 pipeline with FRW comparison. We see the first serious attempt at a phase-structured repo and at freezing computational behavior.

**Typical work in this epoch.**

- Scaffold Phase 1: phasor ensembles, floor tests, and a minimal paper pipeline.
- Scaffold Phase 2: mode-sum + FRW comparison, Snakemake provenance, and reproducible figures.
- Start centralizing artifacts and trimming legacy clutter.

**Example commit subjects.**

- `chore(phase1): scaffold + scope/claims/repro contract + snakemake skeleton`
- `feat(phase1): implement Fig A phasor ensemble + floor with meta logging`
- `Phase 1: minimal Origin Axiom core + reproducible pipeline and paper`
- `Phase 2: reproducible figures and FRW comparison (computational freeze)`
- `phase2: stabilize Snakemake provenance + FRW runner; refresh governance docs`
- `chore: slim main repo to phase0/phase1/phase2; move legacy out`

This epoch is where **Phase 1 and Phase 2** first resemble their modern selves, though Phase 0 governance is still incomplete and Phase 3+ do not exist yet.

---

### 4.4 Epoch 3 — Phase 0 governance & Phase 2 structural audit (2026-01-02 → 2026-01-04)

**Theme.**  
Phase 0 is born as an explicit governance phase, and Phase 2 undergoes a structural audit. This is the moment where the project stops being just a “physics sandbox” and becomes a governance-first program.

**Typical work in this epoch.**

- Add Phase 0 paper and core governance docs (CLAIMS, SCOPE, ASSUMPTIONS, REPRODUCIBILITY).
- Rewrite Phase 0 text into a constitution: claims, falsifiability, reproducibility, and corridor vocabulary.
- Perform Phase 2 structural audit and gate: align claims, audit report, gate scripts, and LaTeX structure.

**Example commit subjects.**

- `docs: add global phase/claims/repro structure and backfill phase0 progress log`
- `phase0: add paper main/macros/bib + start phase0 progress log`
- `added CLAIMS.md`
- `phase0/docs: add governance claim ledger and update root/index docs`
- `phase0: rewrite introduction as governance constitution; enforce scope and no-dark-progress rule`
- `phase2: structural audit + claims-first spine + fix appendix provenance refs`
- `phase2: P2-S8 add single gate script (audit+provenance+lint+build)`
- `phase2: update audit report after claims-first revision + passing gate`

From this point onward, Phase 0 acts as the **arbiter** of what counts as canonical vs experimental, and audits become first-class citizens.

---

### 4.5 Epoch 4 — Phase 3 mechanism, Phase 4 FRW stub, Phase 5 interface (2026-01-05 → 2026-01-07)

**Theme.**  
The repo grows Phase 3, Phase 4, and the earliest Phase 5 interface. Initially, Phase 3 has a strong flavor-sector tilt (CKM/PMNS fits), but later work will reinterpret it as a mechanism module and archive the flavor-specific storyline.

**Typical work in this epoch.**

- Phase 3:
  - bootstrap Phase 3 with a θ-mechanism in the flavor sector (CKM/PMNS targets, discrete offset sweeps),
  - add Snakefile pipelines and provenance bundles,
  - strengthen falsifiability and under-claiming in the Phase 3 paper.
- Phase 4:
  - add FRW-facing design notes and stubs for toy diagnostics.
- Phase 5:
  - begin a Phase 5 “interface” concept for dashboards and sanity tables.

**Example commit subjects.**

- `Phase 3 bootstrap: scope-aligned flavor integration scaffolding + reproducibility gates`
- `Phase 3: lock theta-fit ansatz contract (YAML targets, diagnostics, provenance bundle)`
- `Phase 3: CKM+PMNS v1 targets schema + circular phase chi2; bundle artifacts regenerated`
- `Phase 3: fixed-offset PMNS hypothesis sweep (b discrete) + bundled evidence`
- `Phase 3 paper: strengthen falsifiability and limitations (under-claiming aligned)`
- Early Phase 4/5 stubs show up later in this range and are consolidated in the next epoch.

Later governance and doc passes (in Stage 2 and Belt E/F/G) will:

- treat **Phase 3 as a mechanism module** (canonical),
- move the flavor calibration into `experiments/phase3_flavor_v1/` (archived, non-canonical),
- and reframe Phase 4 as an FRW toy stub and Phase 5 as an interface/sanity layer.

---

### 4.6 Epoch 5 — Stage 2 diagnostic belts (FRW, mech, joint, data) (2026-01-08 → 2026-01-10)

**Theme.**  
Stage 2 is created as a downstream diagnostic belt over Phases 3 and 4. In parallel, Phase 5’s interface gets an early spec and the global docs are refreshed to match the Phase/Stage layout.

**Typical work in this epoch.**

- Phase 5:
  - scaffold interface v1 spec and Rungs 0–5 (dashboard, tables, figures),
  - add build scripts and hook Phase 5 into the global paper build.
- Stage 2:
  - FRW corridor belt (rungs 1–9),
  - mech/measure analysis belt (rungs 1–6),
  - joint mech–FRW belt (rungs 1–4),
  - FRW data-probe audit (rungs 1–2),
  - overview / promotion-design docs for Stage 2.
- Global docs:
  - align README, project overview, and roadmap with Phase 0–5 plus Stage 2 as a diagnostic layer.

**Example commit subjects.**

- `Unify Phase 0–4 paper gates and add global build_paper driver`
- `docs: scaffold Phase 5 roadmap and log interface-focused plan`
- `phase5: add interface v1 spec and connectivity diagnostics`
- `phase5: add build script + artifact wiring (Rung 4)`
- `Stage2: FRW corridors rungs 1–5 (families, overlaps, PDF visuals)`
- `Stage2: FRW corridor Rung 9 (segments + theta* alignment)`
- `Stage2: Phase 3 mech/measure analysis rungs 1–6 (inventory, candidates, shortlist)`
- `Stage2: add joint mech–FRW theta grid, family stats, and correlation diagnostics`
- `Stage2: audit FRW data probes (rungs 1–2, data_ok status)`
- `Docs: align README and project overview with Phase/Stage structure`
- `Docs: refresh FUTURE_WORK_AND_ROADMAP for Stage I + Stage 2/II roadmap`

By the end of this epoch, Stage 2 is a **coherent belt**: FRW corridors, mechanism diagnostics, joint mech–FRW correlations, and FRW data-probe sanity checks, all downstream-only.

---

### 4.7 Epoch 6 — Doc audit, Belt F/G, FRW anchors (2026-01-11 → 2026-01-12)

**Theme.**  
The focus shifts from new physics to **repo hygiene, doc audit, and navigation**. Belt F (doc spine) and Belt G (doc layout / subdirs) are implemented, Stage 2 doc-audit outputs are acted on, and a light FRW anchor belt is added.

**Typical work in this epoch.**

- Stage 2 docs:
  - add belt overviews for FRW, mech, joint, data, and θ★ alignment,
  - document the doc/repo-audit belt (inventory, broken refs, orphans, open threads),
  - create promotion-design docs (Option A/B) for possible future Phase 4/5 citations.
- Doc re-org (Belt F/G):
  - create `phase2/audit/` and `phase3/design/`, `phase4/design/` for structural clarity,
  - move audit and design docs into those subtrees,
  - update references and add alignment memos explaining the layout.
- Global navigation:
  - add `docs/REPO_MAP_AND_ATLAS_v1.md` skeleton and hook it from README and STATE_OF_REPO,
  - make the root `REPRODUCIBILITY.md` a clear entrypoint,
  - surface archive status and Stage 2 belt status in global docs.
- FRW anchors:
  - add an empirical FRW anchor belt in Stage 2: background-only diagnostics that set reference “anchor” boxes for FRW scalars.

**Example commit subjects.**

- `Stage2/docs: add FRW/mech/joint/data belt summary stubs`
- `Stage2/docs: add FRW/mech/joint/data belt summary docs`
- `Docs: add repo map and atlas skeleton`
- `Docs/Stage2: clarify doc-audit working dir and fix links`
- `Docs: link repo atlas from README and STATE_OF_REPO`
- `Docs: surface FRW promotion gate and Phase 5 roadmap`
- `Experiments/Phase3 flavor: mark SCOPE as archived and point to canonical Phase 3`
- `Docs: Belt F – doc spine and phase doc layout notes`
- `Docs: Belt G – phase 2–4 doc hierarchy (design/audit subdirs)`
- `Scripts: unify paper build entrypoints (per-phase + global)`
- `Stage2: add empirical FRW anchor belt (background box A1–A4 + summary)`

This epoch is where the repo becomes **readable as a program**: phases, belts, archives, and audit tools all have explicit docs and a relatively stable layout.

---

## 5. Relation to other docs

This atlas should be read alongside:

- `docs/STATE_OF_REPO.md` — current phase and Stage 2 status.
- `docs/PHASES.md` — phase-by-phase descriptions and statuses.
- `docs/REPO_MAP_AND_ATLAS_v1.md` — file/folder structure and navigation.
- `docs/CLAIMS_INDEX.md` — where the binding claims actually live.
- `stage2/docs/STAGE2_BELT_OVERVIEW_v1.md` — detailed Stage 2 belt map.
- `stage2/docs/STAGE2_DOC_AUDIT_SUMMARY_v1.md` — how the doc-audit CSVs are used.

If there is ever a need to compactify history (e.g. new repo or squashed export), this atlas + the Phase 0 governance docs should be treated as the **authoritative verbal description** of what happened in the original 420-commit Stage I history.

