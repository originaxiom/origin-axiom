#!/usr/bin/env bash
set -euo pipefail

# Resolve repo root (one level above scripts/)
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "[phase2_gate] Level = A"
echo "[phase2_gate] Repo root: $root"
echo "Assuming unrestricted shared filesystem usage."
echo "host: $(hostname)"

# 1) Run Snakemake to ensure Phase 2 diagnostics / figures are up to date.
cd "$root/phase2/workflow"
snakemake --cores 1

# 2) Build the Phase 2 paper and copy canonical artifacts.
cd "$root/phase2/paper"
echo "[phase2_gate] Building Phase 2 paper with latexmk..."
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

# Ensure canonical output and artifact directories exist.
mkdir -p "$root/phase2/outputs/paper" "$root/phase2/artifacts"

# Copy main.pdf to canonical Phase 2 locations.
cp main.pdf "$root/phase2/outputs/paper/phase2_paper.pdf"
cp main.pdf "$root/phase2/artifacts/origin-axiom-phase2.pdf"

echo "[phase2_gate] OK"
