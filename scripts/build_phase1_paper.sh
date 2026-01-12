#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_ROOT}"

echo "[build_phase1_paper] Running Phase 1 gate..."
scripts/phase1_gate.sh

echo "[build_phase1_paper] Syncing artifact to top-level artifacts/ ..."
mkdir -p artifacts
if [[ -f phase1/artifacts/origin-axiom-phase1.pdf ]]; then
  cp phase1/artifacts/origin-axiom-phase1.pdf artifacts/origin-axiom-phase1.pdf
  echo "[build_phase1_paper] Copied phase1/artifacts/origin-axiom-phase1.pdf -> artifacts/origin-axiom-phase1.pdf"
else
  echo "[build_phase1_paper] WARNING: missing phase1/artifacts/origin-axiom-phase1.pdf" >&2
fi

echo "[build_phase1_paper] Done."
echo "[build_phase1_paper] Canonical artifacts:"
echo "  phase1/artifacts/origin-axiom-phase1.pdf"
echo "  artifacts/origin-axiom-phase1.pdf"
