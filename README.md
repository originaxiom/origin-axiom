# Origin Axiom

This repository collects the first systematic attempt to formulate and test the **Origin Axiom**:  
a structural rule that forbids the universe from ever reaching a perfectly cancelling global state.

The project is deliberately modest and technical:

- Paper **A** (principle) motivates the axiom from the incoherence of “absolute nothingness” and defines it as a constraint on global amplitudes A(C) over configuration space.
- Paper **B** (toy universe) implements the axiom in a minimal complex scalar field on a discrete 3-torus and studies how a global non-cancelling constraint behaves in explicit simulations.
- Paper **C** (planned) analyses “universe as a cancellation system” and collects deeper sanity checks and null results.

The code in src/ and notebooks/ backs the figures and claims in the papers.  
Everything important is logged to PROGRESS_LOG.md and data/processed/.

---

## 1. Concept in one paragraph

In many physical models, large contributions cancel almost perfectly: positive and negative charges, oscillating fields, vacuum energies in different sectors. The Origin Axiom proposes that there exists at least one global complex amplitude A(C) such that **exact cancellation is structurally forbidden**:

> physically realised configurations avoid a small neighbourhood of a reference value A* (usually A* = 0) in amplitude space.

In the simplest implementation used here, this becomes a hard rule |A(C)| ≥ ε for some small non-cancellation scale ε. Companion simulations show that this rule can be imposed on a scalar toy universe without destabilising the dynamics or spoiling energy conservation.

---

## 2. Repository structure

README.md                 ← this file (high-level overview)
docs/
  01_origin_axiom.md      ← prose version of the principle
  02_research_program.md  ← longer motivation + context
  03_toy_universe_v0_1.md ← narrative description of the toy model
  PROGRESS_LOG.md         ← dated log of simulations and results
  ROADMAP.md              ← project phases and planned work

paper/
  origin_axiom_A_principle.tex     ← LaTeX draft: principle / motivation
  origin_axiom_B_toy_universe.tex  ← LaTeX draft: scalar toy universe
  # (future) origin_axiom_C_*.tex  ← cancellation-system & sanity check paper

src/
  toy_universe_lattice/            ← 3D scalar lattice, energy, constraint, etc.
  run_toy_universe_demo.py         ← basic evolution without constraint
  run_toy_universe_with_constraint.py
  run_toy_universe_compare_constraint.py
  run_toy_universe_constraint_scan.py
  toy_universe_1d/                 ← 1D twisted / defected scalar models
  run_1d_twisted_vacuum_scan.py
  run_1d_defected_vacuum_scan.py

notebooks/
  01_toy_universe_exploration.py         ← plots for basic 3D run
  02_1d_twisted_analysis.py              ← 1D twist model plots
  02b_1d_defected_twist_analysis.py      ← 1D twist with defect bond
  03_compare_constraint_effect.py        ← 3D linear comparison plots
  04_compare_constraint_nonlinear.py     ← 3D nonlinear comparison plots
  05_constraint_scan_analysis.py         ← epsilon / lambda scan plots

data/
  raw/                                   ← (reserved for future inputs)
  processed/                             ← .npz outputs + generated PNGs

figures/
  *.png                                  ← copies of key plots used in papers

(Some filenames may evolve; the directory layout is the important part.)

---

## 3. Quickstart: run the toy universe

Requirements: Python 3.11+ recommended.

Create and activate a virtual environment:

cd ~/Documents/Projects/origin-axiom

python3 -m venv venv
source venv/bin/activate

# Install minimal dependencies
pip install numpy matplotlib
# or, if you later add a requirements file:
# pip install -r requirements.txt

### 3.1 Basic 3D toy universe (no constraint)

python3 src/run_toy_universe_demo.py

This runs a small complex scalar field on a 16^3 lattice with periodic
boundary conditions and prints the global amplitude |A(t)| and energy E(t)
over time.

### 3.2 With vs without Origin Axiom constraint

To see the non-cancelling rule in action (mean-subtracted initial data, ε = 0.05):

python3 src/run_toy_universe_compare_constraint.py
python3 notebooks/03_compare_constraint_effect.py

This produces:

- data/processed/toy_v0_1_compare_Amod_epsilon005_meanzero.png
- data/processed/toy_v0_1_compare_energy_epsilon005_meanzero.png

which show:

- Without constraint: the global amplitude |A(t)| stays near zero (almost perfect cancellation).
- With constraint: |A(t)| is kept at a minimal value |A| = ε, while the total energy E(t) remains almost unchanged.

### 3.3 Nonlinear case and constraint scan

Nonlinear self-interaction (λ = 1):

python3 src/run_toy_universe_compare_constraint_nonlinear.py
python3 notebooks/04_compare_constraint_nonlinear.py

Constraint-activity scan over ε and λ:

python3 src/run_toy_universe_constraint_scan.py
python3 notebooks/05_constraint_scan_analysis.py

This generates summary plots such as:

- constraint_scan_Amean_vs_eps_lambda*.png (mean |A| vs ε)
- constraint_scan_hits_vs_eps_lambda*.png (constraint hits vs ε)

showing that ε cleanly sets the non-cancellation scale and that the constraint
can act frequently without spoiling energy behaviour.

### 3.4 1D twisted scalar checks

To reproduce the 1D twisted / defected scalar results:

python3 src/run_1d_twisted_vacuum_scan.py
python3 notebooks/02_1d_twisted_analysis.py

python3 src/run_1d_defected_vacuum_scan.py
python3 notebooks/02b_1d_defected_twist_analysis.py

These generate plots of vacuum energy vs twist angle θ*, and in both cases the
total vacuum energy is numerically flat, serving as a null test.

---

## 4. Papers and documentation

- paper/origin_axiom_A_principle.tex  
  Conceptual and mathematical statement of the Origin Axiom as a constraint on configuration space.

- paper/origin_axiom_B_toy_universe.tex  
  Technical paper describing the 3D scalar toy universe, the hard non-cancelling constraint,
  and all numerical experiments implemented here.

- docs/01_origin_axiom.md, docs/02_research_program.md, docs/03_toy_universe_v0_1.md  
  Markdown explanations of the axiom, the research programme and the toy model,
  aimed at humans before they open the TeX.

- PROGRESS_LOG.md  
  Dated log of every significant simulation run, parameter set, and interpretation.

- docs/ROADMAP.md  
  Project phases and planned work (what “v0.1” means, what comes after).

---

## 5. Development notes

- All numerics are intentionally minimal: pure NumPy, no heavy frameworks.
- Important results are written to data/processed/*.npz and plotted with scripts in notebooks/.
- The repository aims to be a reproducible research bundle:
  when a figure appears in a paper, it should be traceable back to a script and a specific cached output here.

---

## 6. Status

The current target is a v0.1 research release containing:

- stable toy-universe code,
- documented simulations and figures,
- LaTeX drafts of Papers A and B,
- and an initial version of Paper C (cancellation systems / sanity check).

The long-term programme (microstructure choices, θ* phenomenology,
possible connections to vacuum energy) is tracked in docs/ROADMAP.md.

---

## Project scope (scalar universe module)

This repository implements the **Origin Axiom / non-cancelling principle** in the
simplest possible setting: a **θ\*-agnostic scalar lattice universe**.

- We treat the fundamental twist angle θ\* as **unknown**.  
- We do **not** assume θ\* = φ or θ\* = φ^φ or any other specific constant here.  
- This module focuses on:
  - scalar-field vacuum dynamics on lattices,
  - the implementation of a non-cancelling constraint at the level of fields/states,
  - numerical sanity checks: dispersion, energy flow, interfaces, cavities, noise, etc.
- It does **not** include:
  - flavor physics or CKM/PMNS mixing,
  - detailed cosmology or gravity,
  - φ-based mass ladders or Yukawa textures.

Those topics live in **separate, dependent modules** in the broader Origin Axiom
program and will cite the results of this scalar-universe backbone.
