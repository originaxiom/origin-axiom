# Run: 20251212_chain_residual_scan (reconstructed from terminal log)

## Metadata
- Date/time (local): 2025-12-12 (exact timestamps in terminal log)
- Git commit (rebuild commit): 782f123
- Script: scripts/cancellation_system/rebuild_chain_residual_scan_from_log.py
- Source log: data/raw/chain_residual_scan_results.txt (local, gitignored)

## Parameters (from log)
- theta grid: linspace(2.45, 2.75, 121)
- Ns: 16, 32, 64, 128, 256, 512, 1024
- n_samples: 400
- seed: 1234
- max_charge: 3
- noise_sigma: 0.0
- enforce_zero_sum: both False and True segments exist (see run folders)

## Outputs (committed)
- docs/results/cancellation_system/runs/20251212_chain_residual_scan__seg1__no_zero_sum__ns400__seed1234/chain_residual_scan.csv
- docs/results/cancellation_system/runs/20251212_chain_residual_scan__seg2__zero_sum__ns400__seed1234/chain_residual_scan.csv
- docs/results/cancellation_system/runs/20251212_chain_residual_scan__seg3__zero_sum__ns400__seed1234/chain_residual_scan.csv
- figures/cancellation_system/runs/20251212_chain_residual_scan__seg*/theta_scan_*.png

## Status
- Reconstructed (no rerun). Original long scan had interruptions; terminal outputs were saved and parsed.

## Result summary
- See `theta_scan_N1024.png` and `theta_scan_min_over_N.png` for candidate minima.
- Next: run objective θ★ locking checklist (seed sweep, max_charge sweep, noise sweep) using run-id/resume runner