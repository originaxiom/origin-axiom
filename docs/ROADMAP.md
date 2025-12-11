# Origin Axiom – Scalar Universe Roadmap

This document defines what this repository is *for* and how we progress without drift.

## 1. Role of this repo in the larger program

This repo is the **scalar-universe backbone** of the Origin Axiom program.

- It implements the **non-cancelling principle** in a **θ\*-agnostic** way.
- It studies a **single real scalar field** on lattices (1D/2D/3D) with:
  - vacuum stiffness / mass terms,
  - optional non-cancelling constraints,
  - noise, dissipation, and structured media (interfaces, cavities).
- It does **not** decide what θ\* is (no hard-coded φ or φ^φ),
  and it does **not** attempt to derive flavor or gravity directly.

Other modules (outside this repo) can build on this:
gravity/FRW, φ-based ladders, Yukawas, etc.

## 2. Current status (v0.1 – in progress)

We already have:

- A conceptual formulation of the non-cancelling axiom.
- A scalar field toy model implemented on lattices.
- Verified dispersion and stable dynamics in the linear regime.
- Wave-transport experiments: interfaces, gradients, cavities.
- A first round of verification notes summarizing numerical tests.

What is *missing* (the focus of this roadmap):

- A clean, θ-agnostic formal write-up (Paper A/B) tied tightly to code.
- A systematic study of the **cancellation system**:
  when does the non-cancelling constraint matter,
  and when is it effectively just a boundary condition?
- A clear hand-off interface to higher-level modules
  (gravity, flavor, θ\* candidates).

## 3. Phase A – Lock in scalar toy universe v1

**Goal:** A coherent, documented v1 of the scalar universe with non-cancelling
constraint, ready to be cited by other work.

### A1. Documentation

- [ ] Ensure `README.md` scope section (this repo = scalar backbone, θ-agnostic).
- [ ] Maintain this `docs/ROADMAP.md` as the source of truth for phases.
- [ ] Create/maintain `docs/PROGRESS_LOG.md` as a chronological log of major runs
      and decisions (date, script, key result, short interpretation).

### A2. Code baseline

- [ ] Identify and freeze a reference scalar model implementation in `src/`
      (single source of truth for the toy scalar equations).
- [ ] Tag the main dispersion and cavity scripts used for validation
      (e.g. `src/phaseI_...`, `src/phaseII_...`, `src/phaseIII_...`).
- [ ] Ensure each core script:
      - takes parameters from a config or CLI,
      - writes outputs into `data/processed/...`,
      - is referenced by at least one notebook or figure.

### A3. Reference run

- [ ] Choose one "reference run" (scenario) and document end-to-end:
      - which script and parameters,
      - which output .npz/.csv files,
      - which plots,
      - which section in the write-up.
- [ ] Use this as a template for future experiments.

**Exit criterion for Phase A:**
We can point a new collaborator to:
- `README.md` + `docs/ROADMAP.md`,
- one reference script + its data + its figure,
- and a draft write-up (Paper A/B),
and they can reconstruct what the scalar toy universe *is* without guessing.

## 4. Phase B – Cancellation system & null tests

**Goal:** Understand, with brutal honesty, what the non-cancelling constraint does
and where it reduces to a mild bias or boundary condition.

We introduce a dedicated module:

`src/cancellation_system/`

with at least three experiments:

1. **Energy-scaling test**

   Script: `run_constraint_energy_scaling.py`

   - Same initial condition, vary the constraint strength / tolerance.
   - Measure:
     - total energy vs time,
     - final state statistics,
     - any systematic trend with constraint strength.
   - Question: does the constraint inject/remove energy, or is it neutral?

2. **Random-phase ensemble**

   Script: `run_constraint_random_phases.py`

   - Many random-phase initial states with and without constraint.
   - Compare distributions of:
     - mode amplitudes,
     - spatial correlations,
     - long-time averages.
   - Question: does the constraint meaningfully alter the ensemble, or
     is it just selecting a thin shell of allowed configurations?

3. **Multimode interference**

   Script: `run_constraint_multimode_interference.py`

   - Superposition of several modes designed to nearly cancel.
   - Compare the dynamics with and without constraint.
   - Question: are certain destructive interference patterns
     suppressed or destabilized?

### B1. Paper C – Cancellation System

We prepare a focused write-up (Paper C) with:

- A precise definition of the cancellation system and constraint rule.
- Implementation details in this scalar universe.
- Results from the three experiments above.
- Interpretation: identifying when the axiom is nontrivial vs when it reduces
  to a fancy boundary condition.

**Exit criterion for Phase B:**
We can answer:
> "What does the non-cancelling axiom *operationally* do in this scalar universe?"

with data and clearly separated "yes/no/unknown" statements.

## 5. Phase C – Interface to higher modules

**Goal:** Make this repo a clean dependency for:

- Gravity/FRW & Λ models.
- θ\* candidate selection (φ, φ^φ, etc.).
- Flavor/mass toy models.

Tasks:

- [ ] Extract a θ-agnostic formal statement of the axiom suitable to reuse:
      (e.g. as a constraint on allowed field configurations or sectors).
- [ ] Specify what this scalar universe *guarantees*:
      coherence properties, dispersion, dephasing laws, etc.
- [ ] Document which parts of this repo are "stable" (won't change often)
      and can be treated as a library.

**Exit criterion for Phase C:**
We can write a short "interface spec" (1–2 pages) that a gravity or flavor
module can rely on, without inheriting φ- or φ^φ-specific assumptions.

## 6. Working principles (guardrails)

- θ\* is **agnostic** in this repo.
- Every new idea must appear as:
  1. A hypothesis in words,
  2. An implementation in `src/`,
  3. A result in `data/`,
  4. An entry in `docs/PROGRESS_LOG.md`,
  5. A sentence or figure in a write-up.

- We always distinguish:
  - Axiom-level statements,
  - Model-specific choices,
  - Speculative extrapolations.


## Phase S: θ*-agnostic scalar vacuum

- Extract minimal scalar vacuum sector with non-cancelling constraint, independent of any specific choice of θ*.
- Implement:
  - 1D dispersion & stability checks in `src/scalar_vacuum_theta/`.
  - Noise + dephasing + residue (`η_k`, V_k) with clear scaling laws.
  - Interface / cavity experiments as θ*-agnostic templates.
- Deliverables:
  - Figures and CSV summaries under `data/processed/scalar_vacuum_theta/`.
  - One coherent Methods section for Paper B / C.

