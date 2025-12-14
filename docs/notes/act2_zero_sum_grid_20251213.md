# Act II closure  zero_sum_grid_20251213 (zero-sum note 
## Command
python3 -m src.cancellation_system.run_chain_residual_scan \
  --theta-min 2.45 --theta-max 2.75 --n-theta 121 \
  --Ns 16,32,64,128,256,512,1024 \
  --n-samples 400 --seed 1234 \
  --max-charge 3 --noise-sigma 0.0 \
  --run-id zero_sum_grid_20251213 \
  --resume \
  --write-latest

## Outputs
- CSV:
  - docs/results/cancellation_system/runs/zero_sum_grid_20251213/chain_residual_scan.csv
- Plots:
  - figures/cancellation_system/runs/zero_sum_grid_20251213/chain_residual_scan.png
  - figures/cancellation_system/runs/zero_sum_grid_20251213/theta_scan_N1024.png
  - figures/cancellation_system/runs/zero_sum_grid_20251213/theta_scan_min_over_N.png

## Notes (2–3 bullets)
- Enforced zero-sum charges (Σ q_j = 0), q_max=3, sigma=0, n_samples=400.
- Best θ per N (min mean|S|/sqrtN) stays in a narrow band θ ≈ 2.67–2.72 across N=16…1024:
  - N=16: θ=2.6800 → 0.8525
  - N=32: θ=2.7175 → 0.8136
  - N=64: θ=2.6800 → 0.8639
  - N=128: θ=2.6750 → 0.8507
  - N=256: θ=2.6900 → 0.8513
  - N=512: θ=2.6900 → 0.8621
  - N=1024: θ=2.6950 → 0.8355
- θ★ ≈ 2.595 is not preferred in this toy model: at N=1024, θ=2.595 gives mean|S|/sqrtN ≈ 1.7816.