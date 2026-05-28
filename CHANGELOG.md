# Changelog

All notable changes to the Origin Axiom repository are recorded here.
Format follows [Keep a Changelog](https://keepachangelog.com/); this project is pre-1.0 and
not yet versioned for release. Detailed working history lives in `PROGRESS_LOG.md`.

---

## [Unreleased]

### Added
- Full audit of all prior work: `AUDIT_REPORT.md`, `PROVENANCE.md`.
- Phase 0 governance scaffolding: `GOVERNANCE.md`, `CLAIMS.md`, `README.md`, `ROADMAP.md`,
  `PROGRESS_LOG.md`, this changelog, `REPRODUCIBILITY.md`, `docs/ARCHIVE.md`, `.gitignore`.
- Claims ledger established: 10 `proven`, 4 `conditional`, 9 `open`, 10 `dead`.
- `legacy/` — prior history consolidated: curated text under `legacy/reports/`,
  `legacy/handoff/`, with the ~4 GB raw archive git-ignored under `legacy/raw/`.
- Phase A: the `origin_axiom` package (`src/`) and `tests/` suite locking every
  `proven` claim P1–P10 — 33 passing tests. Packaging via `pyproject.toml`.
- Session-3 integration: claims P11–P13 promoted to the proven core (exact-algebra
  results — sl(2) decomposition of `log A`, gluing-equation factorization,
  isospectrality), with tests (suite now 39 passing). Frontier probes B4
  (BKL/Gutzwiller) and B5 (Wheeler-DeWitt) added as logged observations.
- **Phase C kickoff** — `paths/` directory created: 25-path registry (20
  mathematizable E1–E20 across 11 mechanism classes; 5 philosophical P1–P5 in a
  separate register). The project's goal becomes *exhaustively surveying* the
  mechanisms by which "nothing being unstable" could produce reality, with the
  *map of attempted paths* as the deliverable. First batch selected: E14, E11, E5.
- **Session-3 synthesis** — the 2025 field-theory line reconnected to the algebraic
  skeleton. Claims **P15** (Möbius generating vector field `v(τ)=−κ(τ²−τ−1)`) and
  **P16** (derived potential `V(τ)=κ(τ³/3−τ²/2−τ)`) promoted to the proven core as
  exact algebra about A, with tests (`src/origin_axiom/mobius.py`,
  `tests/test_mobius_vector_field.py`, `tests/test_derived_potential.py`). Frontier
  probes **B6–B9** added (field equation, Fisher–KPP creation, particle spectrum
  with the non-exact `m/g≈φ` near-miss, fusion–scattering shared polynomial), each
  with caveats. Synthesis doc + scripts under `docs/SESSION3_SYNTHESIS.md` and
  `scripts/`. Four Oct-2025 genesis documents filed under `legacy/reports/genesis/`
  (historical only). Ledger: **15 `proven`**, 4 `conditional`, 9 `open`, 10 `dead`.
- Roadmap integration started with `docs/atlas/INTEGRATION_MANIFEST.md`, a
  public-safe manifest for migrating atlas, paper-candidate, campaign-synthesis,
  and review-packet material from private staging into the canonical repository.
- Research Atlas skeleton added under `docs/atlas/`: reviewer guide, research
  tree, failure atlas, success atlas, glossary, and simulator ecosystem map. This
  is a navigation layer only; governed claims remain in `CLAIMS.md`.

### Changed
- Project framing locked to the disciplined V4 / Reality-Check line; the optimistic
  `handoff.md` framing demoted to historical record.

### Notes
- This repository consolidates four prior GitHub repositories and the May-2026 session
  archive into a single canonical home.
- The four prior repositories (`origin-axiom-framework`, `origin-axiom-theta-star`,
  `origin-axiom-obstruction`, `00_origin-axiom`) have been archived read-only with
  "superseded by" pointers. They are preserved, not deleted.
