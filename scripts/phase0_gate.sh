#!/usr/bin/env bash
set -euo pipefail

# Resolve repo root (one level above scripts/)
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "[phase0_gate] Level = A"
echo "[phase0_gate] Repo root: $root"
echo "Assuming unrestricted shared filesystem usage."
echo "host: $(hostname)"

# Build Phase 0 paper(s)
cd "$root/phase0/paper"

echo "[phase0_gate] Building Phase 0 main.tex with latexmk..."
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

# Phase 0 historically also has appendices.tex; keep that behaviour.
if [ -f appendices.tex ]; then
  echo "[phase0_gate] Building Phase 0 appendices.tex with latexmk..."
  latexmk -pdf -interaction=nonstopmode -halt-on-error appendices.tex
fi

# Ensure canonical output and artifact directories exist
mkdir -p ../outputs/paper ../artifacts

# Canonical Phase 0 main paper locations
cp main.pdf ../outputs/paper/phase0_paper.pdf
cp main.pdf ../artifacts/origin-axiom-phase0.pdf

# Optional convenience: if appendices.pdf exists, copy to outputs
if [ -f appendices.pdf ]; then
  cp appendices.pdf ../outputs/paper/phase0_appendices.pdf
fi

echo "[phase0_gate] OK"
