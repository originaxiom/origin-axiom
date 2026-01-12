#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
echo "[build_phase5_paper] Repo root: ${REPO_ROOT}"

cd "${REPO_ROOT}"

echo "[build_phase5_paper] Running Phase 5 gate..."
scripts/phase5_gate.sh

echo "[build_phase5_paper] Running interface dashboard v1..."
python phase5/src/phase5/make_interface_dashboard_v1.py

echo "[build_phase5_paper] Building Phase 5 paper via latexmk..."
cd phase5/paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

cd "${REPO_ROOT}"

echo "[build_phase5_paper] Copying paper to Phase 5 artifact..."
mkdir -p phase5/artifacts
cp phase5/paper/main.pdf phase5/artifacts/origin-axiom-phase5.pdf

echo "[build_phase5_paper] Syncing artifact to top-level artifacts/ ..."
mkdir -p artifacts
if [[ -f phase5/artifacts/origin-axiom-phase5.pdf ]]; then
  cp phase5/artifacts/origin-axiom-phase5.pdf artifacts/origin-axiom-phase5.pdf
  echo "[build_phase5_paper] Copied phase5/artifacts/origin-axiom-phase5.pdf -> artifacts/origin-axiom-phase5.pdf"
else
  echo "[build_phase5_paper] WARNING: missing phase5/artifacts/origin-axiom-phase5.pdf" >&2
fi

echo "[build_phase5_paper] Done."
echo "[build_phase5_paper] Canonical artifacts:"
echo "  phase5/artifacts/origin-axiom-phase5.pdf"
echo "  artifacts/origin-axiom-phase5.pdf"
