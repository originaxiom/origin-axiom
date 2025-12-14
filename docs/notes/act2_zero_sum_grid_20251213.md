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

## Notes (3 bullets)2
- Latest pointers updated:- Residual strength mean(|S|)/sqrt(N) varies smoothly with - Enforced zero-sum charges (
  - docs/results/cancellation_syste  - docs/results/cancellation_syste  - docs/results/cancellation_shai  - dodual_scan.png
