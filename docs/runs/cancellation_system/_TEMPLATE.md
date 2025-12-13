# Run: <RUN_ID>

## Metadata
- Date/time (local): <YYYY-MM-DD HH:MM:SS> (Europe/Belgrade)
- Git commit: <hash>
- Script: <path>
- Command:
  - `<exact command line>`

## Parameters
- thetas: <range or explicit list>
- Ns: <list>
- n_samples: <int>
- seed: <int>
- max_charge: <int>
- noise_sigma: <float>
- enforce_zero_sum: <true/false>

## Outputs
- CSV: <path(s)>
- Figures: <path(s)>
- Meta: <meta.json path>

## Status
- Full / Partial: <full|partial>
- Notes: <interruptions, resume points>

## Result summary
- Candidate θ★ region: <…>
- Key comparisons: <…>
- Anomalies / warnings: <…>
EOF

cat > docs/runs/cancellation_system/20251212_chain_residual_scan.md <<'EOF'
# Run: 20251212_chain_residual_scan (reconstructed from terminal log)

## Metadata
- Source: terminal output saved as `data/raw/chain_residual_scan_results.txt` (local, gitignored)
- Rebuild commit: 782f123
- Rebuilder: scripts/cancellation_system/rebuild_chain_residual_scan_from_log.py

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
- Reconstructed (no rerun). Original scan had interruptions; outputs were preserved in the log and parsed.

## Result summary
- Use the run-folder PNGs to identify candidate minima.
- Next: execute θ★ locking checklist (seed sweep, max_charge sweep, noise sweep) using run-id + resume runner.
