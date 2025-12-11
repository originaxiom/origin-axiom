## 2025-12-11 – θ★ cancellation chain test (non-cancelling vs cancelling)

**Scripts**
- `cancellation_system/run_chain_residual_scan.py`

**Common setup**
- `theta = 2.598` (θ★ from 4D Δα(θ) minimum)
- `Ns = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096]`
- `max_charge = 3`, `noise_sigma = 0.0`
- `n_samples = 400`, `seed = 1234`

### 1. Non-cancelling universe (no global zero-sum)

Command:

PYTHONPATH=src python3 -m cancellation_system.run_chain_residual_scan \
  --theta 2.598 \
  --Ns 16,32,64,128,256,512,1024,2048,4096 \
  --max-charge 3 \
  --noise-sigma 0.0 \
  --n-samples 400 \
  --seed 1234 \
  --no-zero-sum

- enforce_zero_sum = False
- Output CSV: `data/processed/cancellation_system/chain_residual_scan_theta_star_non_cancelling.csv`
- Output fig: `figures/cancellation_system/chain_residual_scan.png`
- mean|S|/sqrt(N) grows from ~0.915 (N=16) to ~3.145 (N=4096).

### 2. Cancelling (Gaussian) universe (global zero-sum enforced)

Command:

PYTHONPATH=src python3 -m cancellation_system.run_chain_residual_scan \
  --theta 2.598 \
  --Ns 16,32,64,128,256,512,1024,2048,4096 \
  --max-charge 3 \
  --noise-sigma 0.0 \
  --n-samples 400 \
  --seed 1234

- enforce_zero_sum = True
- Output CSV: `data/processed/cancellation_system/chain_residual_scan.csv`
- Output fig: `figures/cancellation_system/chain_residual_scan.png` (overwrites with cancelling version)
- mean|S|/sqrt(N) grows from ~0.870 (N=16) to ~3.221 (N=4096).

### 3. Comparison to φ^φ baseline

Earlier baseline (θ ≈ 2.1784576, max_charge=5, enforce_zero_sum=True, N = 8…128)
shows mean|S|/sqrt(N) ≈ 0.84–1.06, consistent with a near-Gaussian random walk.

At θ★ ≈ 2.598, both cancelling and non-cancelling scans show a strong growth of the
mean|S|/sqrt(N) coefficient, reaching ~3 at N ≈ 4000. The effect survives the
global zero-sum constraint, so it is driven by θ-structured correlations, not by
trivial selection.

**Interpretation:** θ★ is not just a special point for the 4D lattice Δα(θ) and
the scalar mass shift; it also marks a regime where cancellation chains exhibit
anomalously large residuals. This supports the "non-cancelling principle" idea:
a θ-structured vacuum where micro-cancellations do not fully erase the global
remainder, even under a zero-sum constraint.

