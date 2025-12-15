
# Origin Axiom

This repository collects the first systematic scalar–field experiments built around the **Origin Axiom**:

> the universe is structurally forbidden from ever reaching a perfectly cancelling global state.

We implement this as a **non‑cancelling rule** on a complex scalar amplitude \(A(\mathcal{C})\) over configuration space, and explore its consequences in a family of deliberately simple “toy universes”.

The project is deliberately modest and technical:

- **Act I – principle & motivation**  
  Motivates the axiom from the incoherence of “absolute nothingness”, classical vs quantum vacuum tension, and the idea that “the universe can never fully cancel itself away”.
- **Act II – flavor bridge (separate repo)**  
  The companion repo [`origin-axiom-theta-star`](https://github.com/originaxiom/origin-axiom-theta-star) fits a small number of θ★ ansätze to PMNS/CKM data and exports a **θ★ prior** used here.
- **Act III+ – cosmology and microstructure (future work)**  
  Extend from scalar toy universes to more realistic effective theories, FRW backgrounds, and microstructure.

This repo is intentionally small and reproducible: a handful of scripts, a thin config layer, and notebooks that tell the story step by step.

---

## 1. Repository layout

```text
origin-axiom/
  src/
    toy_universe.py                    # core scalar toy-universe integrator
    toy_universe_constraint.py         # non‑cancelling constraint implementation
    toy_universe_nonlinear.py          # 3D nonlinear extension
    twisted_chain_1d.py                # 1D θ‑twisted vacuum chain
    defected_chain_1d.py               # 1D chain with a local defect
    theta_star_prior_1d_vacuum.py      # helper for θ★ prior → 1D vacuum
    theta_star_prior_1d_microcavity.py # helper for θ★ prior → 1D microcavity
    two_field_bump_1d.py               # coupled (φ, χ) localized bump model
    theta_star_config.py               # thin loader for config/theta_star_config.json
    ...
  scripts/
    show_theta_star_config.py          # print current θ★ prior used by this repo
    inspect_two_field_bump_1d.py       # plots for the two‑field bump run
    ...
  notebooks/
    01_toy_universe_exploration.py     # plots / diagnostics for scalar toy universes
    02_1d_twisted_analysis.py          # 1D twisted chain analysis
    02b_1d_defected_twist_analysis.py  # 1D defected chain analysis
    03_compare_constraint_effect.py    # 3D toy: with vs without constraint
    04_compare_constraint_nonlinear.py # nonlinear 3D toy: constraint effect
    05_constraint_scan_analysis.py     # ε–λ scan diagnostics
    06_theta_star_microcavity_analysis.py # θ★ prior in a 1D microcavity
    07_two_field_bump_analysis.py      # coupled (φ, χ) bump evolution
  config/
    theta_star_config.json             # imported θ★ prior from Act II
  data/
    raw/                               # reserved for future raw inputs
    processed/                         # .npz outputs from scripts
  figures/
    *.png                              # copied / generated plots
  docs/
    paper/
      ACTII_theta_star_section.tex     # LaTeX section describing the θ★ bridge
    PROGRESS_LOG.md                    # running log of what has been tried
```

The exact file list will evolve, but the roles above should remain stable.

---

## 2. Act II θ★ prior and the “bridge” to flavor

The companion repo [`origin-axiom-theta-star`](https://github.com/originaxiom/origin-axiom-theta-star) performs detailed fits of several θ★ ansätze to neutrino (PMNS) and quark (CKM) flavor data. Act II currently exports a compact θ★ prior into this repo as:

```text
config/theta_star_config.json
```

The file stores:

- `theta_star_fid_rad` – fiducial θ★ in radians (global median from all high‑quality scans),
- `theta_star_band_rad` – \([θ_{\min}, θ_{\max}]\) band used in scans,
- `provenance` – metadata (source repo, run IDs, χ² cut),
- versioning fields for future updates.

This JSON is read only through:

```python
from theta_star_config import load_theta_star_config

cfg = load_theta_star_config()
theta_fid = cfg.theta_star_fid_rad
theta_lo, theta_hi = cfg.theta_star_band_rad
```

You can also inspect it from the command line:

```bash
PYTHONPATH=src python3 scripts/show_theta_star_config.py
```

This **θ★ config** is the *only* point where flavor data enter this repo. Everything else is pure scalar‑field dynamics with and without the non‑cancelling rule.

---

## 3. Quickstart: run the scalar toy universes

Requirements: **Python 3.11+** recommended.

Create and activate a virtual environment:

```bash
cd ~/Documents/Projects/origin-axiom

python3 -m venv venv
source venv/bin/activate      # on macOS / Linux
# .\venv\Scripts\activate     # on Windows PowerShell
```

Install dependencies (minimal):

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing or minimal, start with `numpy`, `scipy`, `matplotlib`.

### 3.1 Baseline toy universe and constraint

Run the simplest complex scalar toy universe:

```bash
PYTHONPATH=src python3 src/run_toy_universe_demo.py
```

This prints the evolution of the global amplitude \(|A|\) in time for an unconstrained run.

Compare with the non‑cancelling constraint:

```bash
PYTHONPATH=src python3 src/run_toy_universe_compare_constraint.py
```

This script evolves the same initial condition twice:

- **no_constraint** – pure Hamiltonian evolution;
- **with_constraint** – repeatedly projects back to a fixed \(|A|\) shell whenever the amplitude tries to cancel too much.

Both branches save `.npz` data in `data/processed/` for analysis in the `01_*` and `03_*` notebooks.

### 3.2 Nonlinear toy universe and constraint scan

A 3D nonlinear extension:

```bash
PYTHONPATH=src python3 src/run_toy_universe_compare_constraint_nonlinear.py
```

and an \((\epsilon, \lambda)\) scan of constraint strength vs nonlinearity:

```bash
PYTHONPATH=src python3 src/run_toy_universe_constraint_scan.py
```

The scan writes:

```text
data/processed/constraint_scan_eps_lambda.npz
```

for later analysis in the `05_constraint_scan_analysis.py` notebook.

---

## 3.3 1D twisted and defected vacua

1D chain with θ‑twisted boundary conditions:

```bash
PYTHONPATH=src python3 src/run_1d_twisted_vacuum_scan.py
```

and the same chain with a local defect:

```bash
PYTHONPATH=src python3 src/run_1d_defected_vacuum_scan.py
```

Both scripts save `.npz` data in `data/processed/` for the 1D analysis notebooks (`02_*`).

---

## 3.4 Using the θ★ prior in a 1D vacuum

Use the Act II θ★ prior directly in a 1D vacuum model:

```bash
PYTHONPATH=src python3 src/run_1d_theta_star_prior_scan.py
```

This samples a handful of θ★ values across the Act II band and computes the corresponding vacuum energies in a simple 1D model. The script prints a small table and saves:

```text
data/processed/theta_star_prior_1d_vacuum_samples.npz
```

for later use.

---

## 3.5 1D θ★‑dependent microcavity

A toy “microcavity” where the bare mass is modulated inside a finite segment:

```bash
PYTHONPATH=src python3 src/run_1d_theta_star_microcavity_scan.py
```

and the full θ★ band scan:

```bash
PYTHONPATH=src python3 src/scan_1d_theta_star_microcavity_full_band.py
```

These scripts use the θ★ prior to compute the vacuum energy shift ΔE(θ★) between uniform and cavity configurations, saving:

```text
data/processed/theta_star_prior_1d_microcavity_samples.npz
data/processed/theta_star_microcavity_scan_full_2pi.npz
data/processed/figures/theta_star_microcavity_deltaE_full_2pi.png
```

The `06_theta_star_microcavity_analysis.py` notebook visualizes these results (including the Act II band overlay).

---

## 3.6 Two‑field localized bump experiment

Localized coupled (φ, χ) bump in 1D, with and without the non‑cancelling constraint:

```bash
PYTHONPATH=src python3 src/run_two_field_bump_1d.py \
  --steps 2000 \
  --snapshot-stride 20 \
  --g 0.02
```

Inspect the results and produce summary plots:

```bash
PYTHONPATH=src python3 scripts/inspect_two_field_bump_1d.py
```

This writes:

```text
data/processed/figures/two_field_bump_1d_loc_amp.png
data/processed/figures/two_field_bump_1d_phi_final.png
data/processed/figures/two_field_bump_1d_chi_final.png
```

which summarize how the constraint slightly reduces localization and the bump amplitudes over long times.

---

## 4. Reproducibility and logging

- **Environment** – pin your Python version and dependencies via `requirements.txt`.  
- **Random seeds** – scripts set explicit seeds where stochastic sampling is used.  
- **Data** – all scripts write `.npz` outputs into `data/processed/` with descriptive filenames.  
- **Figures** – scripts place `.png` plots in `figures/` (or `data/processed/figures/` for some sub‑plots).  
- **Progress log** – `docs/PROGRESS_LOG.md` records:
  - which scans have been run,
  - major parameter changes,
  - links to relevant output files and figures,
  - notes on what is considered “frozen” vs “exploratory”.

If you add new experiments, **please log them** there together with any non‑default parameters.

---

## 5. Relation to other repos

- **`origin-axiom-theta-star`** – Act II flavor fits (PMNS/CKM) and θ★ posterior construction. This repo *consumes* only the resulting θ★ prior JSON.
- Future repos may cover:
  - FRW / cosmological toy models using the non‑cancelling rule,
  - richer microstructure (e.g. multi‑field lattices, realistic dispersion),
  - phenomenological links to the observed vacuum energy.

---

## 6. License and citation

License: **TBD** (currently private research).  
If you use ideas or code from this repo, please cite the eventual “Origin Axiom – Act II” paper and/or this GitHub repository.

For questions, comments, or collaboration ideas, please open an issue or contact the author(s).