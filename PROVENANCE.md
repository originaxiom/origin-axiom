# Origin Axiom — Provenance Map

**Compiled:** 2026-05-22 · **Compiled by:** repository consolidation audit
**Purpose:** Map every surviving artifact of the Origin Axiom project to its date, origin,
and contents, so that prior history is preserved and traceable from the new canonical repo.

This file is a *map*, not a verdict. For the reconciled status of the work (what is proven,
conditional, dead, open), see `AUDIT_REPORT.md`.

---

## 1. The project in one paragraph

"Origin Axiom" is Dritëro M.'s independent research line investigating the question
*why is there something rather than nothing* — reframed as: existence is a **frustrated
cancellation**, a remainder left when an attempt to cancel to nothing cannot complete.
The work has run across at least three eras and four GitHub repositories, and most recently
through a long series of AI-assisted computational sessions (May 2026). The artifacts below
are the full surviving record.

---

## 2. GitHub repositories — `github.com/originaxiom/`

All four are **public, not archived** as of this audit. Their commit timestamps are the
project's tamper-evident proof of progression and must not be deleted.

| Repo | Created | Last push | Commits | Branch | What it is |
|---|---|---|---|---|---|
| `origin-axiom-framework` | 2025-12-09 | 2026-01-20 | 489 | `main` | θ\*-agnostic scalar-universe framework; toy lattice + FRW simulations. Phases 0–5, stage2. The largest body of work. |
| `origin-axiom-theta-star` | 2025-12-14 | 2025-12-15 | 9 | `main` | Phenomenology module: extract/validate a candidate θ★ from CKM/PMNS mixing + SM flavor observables. "Paper D". |
| `origin-axiom-obstruction` | 2026-01-16 | 2026-01-20 | 7 | `main` | Foundational note: is exact vacuum-energy cancellation a well-posed operation? Has `paper/`, `ASSUMPTIONS`, `QUESTION.md`. |
| `00_origin-axiom` | 2026-01-25 | 2026-01-27 | 20 | `master` | "Frustrated Cancellation Dynamics". Phases 0–8, 204 passing tests, χ²/dof = 1.52 vs DESI, self-described "marginally viable". Most polished GitHub repo. |

**Approach of the GitHub era:** top-down physics — start from the axiom, parameterize by a
scalar θ\*, fit against Standard Model / cosmological observables. The May-2026 sessions
(below) explicitly judged this a *parameter-fitting* strategy and pivoted away from it.

---

## 3. Local archive — `legacy/raw/old/`

> **Path note (2026-05-22 reorganization):** the `old/` folder was moved to
> `legacy/raw/old/` (git-ignored — see `legacy/README.md`). All paths in this section are
> relative to `legacy/raw/`. Curated text extracted from this archive is committed under
> `legacy/reports/`.

### 3.0 `old/even older/e_origin axiom/`  (genesis era — ~Oct 2025)

The original "Origin Axiom / Non-Cancelling Principle" era — discovered during the
reorganization, not covered by the initial audit pass. ~3.6 GB. Contents: foundational PDFs
(`The Origin Axiom – A Principle That Prevents "Nothingness".pdf`,
`The Non-Cancelling Principle (Origin Axiom): Deep Research & Sanity Check.pdf`,
`Evaluating a Universe as a Cancellation System.pdf`, arXiv `2307.13614v2.pdf`); staged
folders `00_base_raw_archive`, `01_master_start`, `02_edh_cont`, `03_consolidatoin`; raw
ChatGPT conversation exports (Oct 2025); and large numerical result files (`.npy`, `.npz`).
**Not yet audited in detail** — flagged for a later pass if desired.

### 3.1 `old/even older/00a_OriginAxiom/`  (early `φ^φ` era — pre-GitHub)

Not a git repo. The φ^φ era. Contents: `Axiom.pdf`, `Axiom-4.pdf`,
`Final Docs/` (Main Paper, Complementary Paper, Simulation Suite), `tests/`,
`tests_grok/` (`test_g_phasewalk.py` — phase walk θ_n = n·φ^φ mod 2π), `Outputs/`.
The φ^φ axiom was later tested and dropped (see `AUDIT_REPORT.md`, dead results).

### 3.2 `old/even older/00_origin-axiom/`  (git clone of the GitHub repo)

Local working copy of `github.com/originaxiom/00_origin-axiom` (26 local commits;
remote shows 20 on `master`). Phase folders `phase0_fc … phase7b_pressure`,
`experiments/`, `tests/`, plus `STATUS_SNAPSHOT.md`, `PROGRESS_LOG.md`,
`METHODOLOGY_LESSONS_LEARNED.md`, `REPOSITORY_AUDIT.md`.

### 3.3 `old/Oa_05-26/`  (May 2026 AI-assisted sessions — the "knot-theory turn")

The most recent and most active era. This is where the project pivoted from θ\*-fitting to
the **figure-eight knot / trace-3 / golden-ratio** structure. Two sub-threads run in parallel:

**(a) The disciplined thread** — note versions v2 → v3 → v4, plus reality-check gates G1–G5.
The most claim-conservative line of work. Final position: a *classical/statistical
transfer-matrix anchor*, explicitly **not** a physics theory.

**(b) The Chatterpillar chat thread** — the long exploratory session transcribed in
`old/Chatterpillar.pdf`, which produced `handoff.md`. More ambitious:
SnapPy verification, A-polynomial, gluing→Lorentzian form, BKL/Kasner, a "path to Einstein".

Key files in this folder:

| File | Date | Contents |
|---|---|---|
| `origin_axiom_all_prior_bundles_MASTER.zip` | 05-21 18:17 | **Canonical consolidated archive.** 28 MB, 85 files: 60+ sub-bundle zips under `bundles/`, 21 reports under `standalone_reports/`, `MANIFEST.json` (sizes + SHA256). Supersedes every individual bundle zip in this folder. |
| `origin_axiom_v4_paper_bundle.zip` | 05-21 20:17 | **Latest paper** — `ORIGIN_AXIOM_V4_PAPER.md` + executive summary. Most disciplined manuscript. |
| `origin_axiom_v3_paper_bundle.zip` | 05-21 08:11 | v3 paper (md/tex/pdf). |
| `origin_axiom_v2_source_bundle.zip` | 05-20 09:09 | v2 research note (LaTeX source). |
| `origin axiom final.pdf` | 05-20 10:16 | 10-page, 9-figure "final" paper assembled inside the Chatterpillar chat. |
| `Chat history.pdf` | 05-20 15:45 | A ChatGPT session the user shared into the Chatterpillar chat. |
| `origin_axiom_full_progress_log.md` | 05-20 01:16 | 42 KB running progress log. |
| `origin_axiom_research_plan.md`, `origin_axiom_execution_plan.md` | 05-19 20:55 | Early plans for the knot-theory phase. |
| `factorization census results.md`, `novel findings honest.md` | 05-19/20 | Specific computational result write-ups. |
| `paper1_golden_ratio_quantum_spectra.md`, `paper3_origin_axiom.md` | 05-19 | Early paper drafts (Paper 1 / Paper 3). |
| `origin_axiom_minimal_persistent_records_note.tex` | 05-20 01:28 | The "minimal persistent record" note (the v2 backbone). |
| `phi0526.pdf` | 05-20 12:38 | PDF artifact. |
| `Reptilian elite…pdf`, `Continuing the Anunnaki…pdf` | 05-19 | Prior (non-physics) conversation exports — context only, not project work. |
| `origin axiom complete.zip` (and an earlier session bundle) | 05-19 | Early session bundles (also inside MASTER zip). |
| `origin_axiom_causal_record_lattice/` | 05-20 13:08 | Unzipped bundle: causal-lattice derivation script + CSV/PNG outputs. |
| `origin_axiom_corrected_boundary_bulk_paper_bundle/` | 05-20 19:52 | Unzipped: the corrected boundary/bulk paper + referee prompt. |
| ~35 individual `origin_axiom_*_bundle.zip` files | 05-20/21 | Per-topic bundles — **all also contained inside the MASTER zip**, hence redundant. |

**Standalone reports inside the MASTER zip** (`standalone_reports/`): `ORIGIN_AXIOM_V4_PAPER.md`,
`ORIGIN_AXIOM_REALITY_CHECK_v1.md`, `G5_REALITY_CHECK_UPDATE_AFTER_G4D.md`, the G1–G5 gate
reports, `EMPIRICAL_ANCHOR_NOTE_v1.md`, and others. These are the authoritative
self-assessments of the disciplined thread.

### 3.4 `old/Chatterpillar.pdf`

142-page transcript of the long May-2026 AI-assisted session. Opens with mythology/history
discussion, pivots (~p.34) into the physics, runs ~100 pages of computation, and ends with
the decision to move to a local development environment. The source narrative for `handoff.md`.

---

## 4. Repo root — current new canonical repo (`/Users/dri/origin-axiom`)

| File | Origin | Role |
|---|---|---|
| `legacy/handoff/handoff.md` | Created at the end of the Chatterpillar chat, 05-21; moved to `legacy/` in the 05-22 reorg | Hand-off summary for the local-development phase. Represents the **optimistic / frontier** framing. Per `GOVERNANCE.md` §2 it is a historical record, **not** a source of claims. |
| `PROVENANCE.md` | This file | Artifact map. |
| `AUDIT_REPORT.md` | This audit | Reconciled status + repo-strategy recommendation. |
| `GOVERNANCE.md`, `CLAIMS.md`, `ROADMAP.md`, `README.md`, `PROGRESS_LOG.md`, `CHANGELOG.md`, `REPRODUCIBILITY.md`, `docs/ARCHIVE.md` | Phase 0 build, 05-22 | Governance scaffolding — see `ROADMAP.md`. |
| `legacy/` | 05-22 reorganization | Frozen prior history: `reports/` (committed curated text), `handoff/`, `raw/` (git-ignored ~4 GB archive). See `legacy/README.md`. |

---

## 5. Chronology

```
~2025-10      e_origin axiom             genesis: "Non-Cancelling Principle" (Origin Axiom)
pre-2025-12   00a_OriginAxiom            φ^φ axiom era (φ^φ later dropped)
2025-12-09    origin-axiom-framework     θ*-agnostic scalar framework begins (→489 commits)
2025-12-14    origin-axiom-theta-star    θ★ flavor phenomenology
2026-01-16    origin-axiom-obstruction   "is cancellation well-posed?" note
2026-01-25    00_origin-axiom            Frustrated Cancellation, phases 0–8, DESI test
2026-05-19..21  Oa_05-26                 knot-theory turn: v2→v3→v4, G1–G5, MASTER zip
2026-05-21    handoff.md                 hand-off written; project moves to local development
2026-05-22    (now)                      new canonical repo + this audit
```

---

## 6. Redundancy / cleanup notes

- The ~35 loose `origin_axiom_*_bundle.zip` files in `Oa_05-26/` are **all duplicated
  inside `origin_axiom_all_prior_bundles_MASTER.zip`**. For the consolidated repo, keep the
  MASTER zip and drop the loose duplicates.
- `00_origin-axiom` exists both as a GitHub repo and a local clone — they are the same thing.
- Binary archives (zips, PDFs) should **not** be committed into git history. See
  `AUDIT_REPORT.md` §6 for the recommended legacy-archive handling.
