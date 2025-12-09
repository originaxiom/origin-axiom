# Reproducing Figures and Processed Data

This document lists how to regenerate the core `.npz` data files and `.png`
plots used in the Origin Axiom toy-universe papers.

Assumptions:

- You are in the repository root.
- Python 3.11+ is available.
- A virtual environment `venv/` exists and has at least `numpy` and `matplotlib`
  installed (see README for setup).

Activate the environment first:

```bash
cd ~/Documents/Projects/origin-axiom
source venv/bin/activate
```

---

## 1. 3D toy universe — basic evolution (no constraint)

**Purpose:** sanity check of the 3D scalar lattice evolution, tracking global
amplitude \`|A(t)|\` and energy \`E(t)\`.

**Commands:**

```bash
python3 src/run_toy_universe_demo.py
python3 notebooks/01_toy_universe_exploration.py
```

**Key outputs (under `data/processed/`):**

- `toy_v0_1_theta_pi_constraint.npz` (or similar demo file)
- `toy_v0_1_theta_pi_Amod.png`
- `toy_v0_1_theta_pi_energy.png`

These are used as the first illustration that the numerics behave sensibly.

---

## 2. 3D toy universe — linear case, with vs without constraint

**Purpose:** show that the Origin Axiom constraint \`|A| ≥ ε\` prevents global
cancellation without significantly altering energy evolution.

**Commands:**

```bash
python3 src/run_toy_universe_compare_constraint.py
python3 notebooks/03_compare_constraint_effect.py
```

**Outputs:**

From the compare script:

- `data/processed/toy_v0_1_no_constraint_epsilon005_meanzero.npz`
- `data/processed/toy_v0_1_with_constraint_epsilon005_meanzero.npz`

From the analysis script:

- `data/processed/toy_v0_1_compare_Amod_epsilon005_meanzero.png`
- `data/processed/toy_v0_1_compare_energy_epsilon005_meanzero.png`

Interpretation:

- Without constraint: \`|A(t)|\` wanders near zero (almost perfect global cancellation).
- With constraint: \`|A(t)|\` is pinned near ε, while \`E(t)\` remains almost unchanged.

These plots are central figures in the toy-universe paper.

---

## 3. 3D toy universe — nonlinear case (λ = 1)

**Purpose:** check that the non-cancelling constraint still behaves well when a
quartic self-interaction is turned on.

**Commands:**

```bash
python3 notebooks/04_compare_constraint_nonlinear.py
```

(This script both runs the nonlinear simulations and produces the plots.)

**Outputs:**

- `data/processed/toy_v0_1_nonlinear_no_constraint_epsilon005_meanzero.npz`
- `data/processed/toy_v0_1_nonlinear_with_constraint_epsilon005_meanzero.npz`
- `data/processed/toy_v0_1_nonlinear_compare_Amod_epsilon005_meanzero.png`
- `data/processed/toy_v0_1_nonlinear_compare_energy_epsilon005_meanzero.png`

Interpretation:

- The constraint keeps \`|A(t)|\` at the non-cancellation scale ε even in the
  nonlinear regime.
- Energy remains well behaved and close between constrained and unconstrained runs.

---

## 4. 3D toy universe — constraint activity scan (ε, λ)

**Purpose:** systematically explore how often the constraint activates and how
it sets the typical \`|A|\` scale for different ε and λ.

**Commands:**

```bash
python3 src/run_toy_universe_constraint_scan.py
python3 notebooks/05_constraint_scan_analysis.py
```

**Outputs:**

From the scan:

- `data/processed/constraint_scan_eps_lambda.npz`

From the analysis:

- `data/processed/constraint_scan_Amean_vs_eps_lambda0.00.png`
- `data/processed/constraint_scan_hits_vs_eps_lambda0.00.png`
- `data/processed/constraint_scan_Amean_vs_eps_lambda1.00.png`
- `data/processed/constraint_scan_hits_vs_eps_lambda1.00.png`

Interpretation:

- For both λ = 0 and λ = 1, the mean \`|A|\` tracks ε.
- Constraint hit counts confirm how often the system attempts to enter the forbidden region.

---

## 5. 1D twisted scalar — vacuum energy vs twist (null test)

**Purpose:** test whether a global twist angle θ\* changes the total vacuum
energy in a simple 1D scalar model on a ring.

**Commands:**

```bash
python3 src/run_1d_twisted_vacuum_scan.py
python3 notebooks/02_1d_twisted_analysis.py
```

**Outputs:**

- `data/processed/twisted_1d_vacuum_scan.npz`
- `data/processed/twisted_1d_E0_vs_theta.png`
- `data/processed/twisted_1d_deltaE_vs_theta.png`

Interpretation:

- \`E0(θ*)\` is numerically flat; \`ΔE0(θ*)\` is at numerical-noise level.
- This is an important null result: in a perfectly symmetric 1D ring, a global
  twist relabels modes without shifting the total vacuum energy.

---

## 6. 1D twisted scalar with defect — vacuum energy vs twist (another null test)

**Purpose:** check whether introducing a single “defect bond” changes the
dependence of vacuum energy on the twist angle.

**Commands:**

```bash
python3 src/run_1d_defected_vacuum_scan.py
python3 notebooks/02b_1d_defected_twist_analysis.py
```

**Outputs:**

- `data/processed/defected_1d_vacuum_scan.npz`
- `data/processed/defected_1d_E0_vs_theta.png`
- `data/processed/defected_1d_deltaE_vs_theta.png`

Interpretation:

- With the current parameters, \`E0(θ*)\` remains numerically flat.
- This reinforces the lesson that simple quadratic models on a ring do not
  automatically generate twist-dependent vacuum energies.

---

## 7. Notes on \`figures/\` directory

Optionally, copies of the key `.png` outputs used directly in the papers can be
stored under `figures/`. These should always be regenerable from the commands
listed above; if a figure cannot be reproduced from a script + `.npz` listed
here, it should be considered out of date.
