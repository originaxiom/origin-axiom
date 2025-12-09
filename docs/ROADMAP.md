# Origin Axiom — Research Roadmap

This document tracks the concrete steps for the **Origin Axiom** project inside this repository.
It focuses on physics and math: configuration space, global amplitudes, toy models and sanity checks.

Big picture goal for this repo:

> Deliver a clean, reproducible research package (code + papers) that
> defines the Origin Axiom, tests it in explicit models, and is ready for
> Zenodo / arXiv / peer discussion.

---

## Phase 0 — Foundation *(mostly done)*

- Git repository with a clear structure (`src/`, `docs/`, `paper/`, `data/`).
- Minimal 3D scalar toy universe on a discrete 3-torus.
- Implementation of a global non-cancelling constraint \(|A| \ge \epsilon\).
- Basic 1D twisted scalar models for analytic / null checks.
- Draft LaTeX:
  - `origin_axiom_A_principle.tex` — principle and motivation;
  - `origin_axiom_B_toy_universe.tex` — scalar toy universe.
- `docs/PROGRESS_LOG.md` with dated entries for all important simulations.

---

## Phase 1 — v0.1 Research Package

**Goal:** lock a first serious, defensible package of work.

### 1.1 Documentation

- [ ] Keep `README.md` aligned with the actual code and paper structure.
- [ ] Maintain `docs/PROGRESS_LOG.md` for every new experiment.
- [ ] Expand `docs/03_toy_universe_v0_1.md` with:
  - short derivation of the discrete equations;
  - explanation of the constraint projection in math + plain language.

### 1.2 Papers

- [ ] Tighten **Paper A**:
  - clarify the role of the global amplitude \(A(C)\);
  - make the formal statement of the Origin Axiom as clean as possible;
  - ensure consistency with toy-universe implementation.

- [ ] Tighten **Paper B**:
  - align the equations and parameter choices with the actual scripts;
  - insert final versions of the key figures (3D comparisons, nonlinear runs, epsilon/lambda scans, 1D null results);
  - cross-reference `docs/PROGRESS_LOG.md` where appropriate.

- [ ] Draft **Paper C** (working title):  
  *“Universe as a Cancellation System: Non-Cancelling Principle and Sanity Checks”*.
  - summarise the idea of viewing the universe as a giant cancellation system;
  - integrate insights from the internal PDFs (Non-Cancelling Principle, cancellation system evaluation);
  - clearly separate speculation from solid numerics.

### 1.3 Code quality

- [ ] Add docstrings and comments to the main modules in `src/toy_universe_lattice/` and `src/toy_universe_1d/`.
- [ ] Provide at least a minimal `tests/` or `scripts/` folder with:
  - quick numerical sanity checks (e.g. energy conservation without constraint; flat E\_0 vs twist in 1D);
  - a “smoke test” script that runs the main demos end-to-end.

- [ ] Ensure all key figures can be regenerated from a small set of commands,
  ideally collected in a `docs/REPRODUCING_FIGURES.md` or a makefile.

### 1.4 Release

- [ ] Tag a `v0.1` GitHub release once Papers A and B and the core simulations are stable.
- [ ] Link the release to Zenodo to obtain a DOI.
- [ ] Treat `v0.1` as a frozen reference point for future work.

---

## Phase 2 — Extensions and Microstructure

**Goal:** explore the Origin Axiom beyond the simplest toy model while keeping v0.1 stable.  
This phase can create branches or new subfolders; v0.1 remains reproducible.

Possible directions (to be prioritised later):

- **Alternative global amplitudes \(A(C)\):**
  - weighted sums, currents, or functionals involving spatial structure;
  - study how different choices change the statistics of constraint hits and energy.

- **Richer microstructure:**
  - other discrete topologies (e.g. different lattices, graphs, defects);
  - multiple scalar components; coupling to an effective “metric” field.

- **More analytic work:**
  - continuum approximations of the lattice models;
  - more detailed analysis of twisted / defected systems;
  - bounds relating the non-cancellation scale \(\epsilon\) to vacuum-like energies.

All Phase-2 explorations should log their results in `docs/PROGRESS_LOG.md`
and, where appropriate, branch into new LaTeX sections or separate notes.

---

## Phase 3 — External Exposure

**Goal:** share the work with the outside world once you are comfortable with its solidity.

- [ ] Prepare arXiv submissions for:
  - Paper A (principle),
  - Paper B (toy universe),
  - optionally Paper C (cancellation systems / sanity checks).

- [ ] Attach code and data references in each submission (GitHub + Zenodo DOI).

- [ ] Prepare a short human-friendly summary (e.g. blog/Medium post) that:
  - explains the intuition of the Origin Axiom in non-technical language,
  - points interested readers to this repo for the technical details.

- [ ] Start targeted conversations with a few open-minded physicists / communicators.
  The aim is not hype, but honest feedback and potential collaboration.

---

## Phase 4 — Beyond this repo (future work)

The broader ideas that motivated the Origin Axiom—possible roles in cosmology,
vacuum energy, information, even societal / governance analogies—are deliberately
kept \*outside\* this repository for now.

Once the v0.1 package is stable and public, these wider directions can spin off
into separate documents or projects, always anchored back to the clean core:
a well-defined, well-tested non-cancelling principle over configuration space.

