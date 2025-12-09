#!/usr/bin/env bash
set -e

# Run from repo root: ./scripts/run_core_plots.sh
# This script:
# - ensures a venv exists,
# - installs minimal deps,
# - regenerates core .npz data and plots.

echo "[origin-axiom] Ensuring virtualenv..."

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# shellcheck disable=SC1091
source venv/bin/activate

pip install --quiet numpy matplotlib

echo "[origin-axiom] Running core 3D toy-universe demos..."

# 1. Basic 3D toy universe exploration (no constraint-focused plots)
python3 src/run_toy_universe_demo.py || exit 1
python3 notebooks/01_toy_universe_exploration.py || exit 1

# 2. Linear 3D: with vs without constraint (epsilon=0.05, mean-subtracted)
python3 src/run_toy_universe_compare_constraint.py || exit 1
python3 notebooks/03_compare_constraint_effect.py || exit 1

# 3. Nonlinear 3D (lambda = 1)
python3 notebooks/04_compare_constraint_nonlinear.py || exit 1

# 4. Constraint activity scan over epsilon, lambda
python3 src/run_toy_universe_constraint_scan.py || exit 1
python3 notebooks/05_constraint_scan_analysis.py || exit 1

echo "[origin-axiom] Running 1D twisted scalar checks..."

# 5. 1D twisted scalar (null result)
python3 src/run_1d_twisted_vacuum_scan.py || exit 1
python3 notebooks/02_1d_twisted_analysis.py || exit 1

# 6. 1D twisted scalar with defect (currently another null result)
python3 src/run_1d_defected_vacuum_scan.py || exit 1
python3 notebooks/02b_1d_defected_twist_analysis.py || exit 1

echo "[origin-axiom] All core simulations and plots regenerated."
echo "Check data/processed/ and figures/ (if used) for outputs."
