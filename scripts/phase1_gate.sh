#!/usr/bin/env bash
set -euo pipefail

# Resolve repo root (one level above scripts/)
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "[phase1_gate] Level = A"
echo "[phase1_gate] Repo root: $root"
echo "Assuming unrestricted shared filesystem usage."
echo "host: $(hostname)"

# Build Phase 1 paper
cd "$root/phase1/paper"

echo "[phase1_gate] Building Phase 1 main.tex with latexmk..."
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

# Ensure canonical output and artifact directories exist
mkdir -p ../outputs/paper ../artifacts

# Canonical Phase 1 main paper locations
cp main.pdf ../outputs/paper/phase1_paper.pdf
cp main.pdf ../artifacts/origin-axiom-phase1.pdf

echo "[phase1_gate] OK"
