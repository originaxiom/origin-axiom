#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_ROOT}"

echo "[build_phase3_paper] Running Phase 3 gate..."
scripts/phase3_gate.sh

echo "[build_phase3_paper] Syncing artifact to top-level artifacts/ ..."
mkdir -p artifacts
if [[ -f phase3/artifacts/origin-axiom-phase3.pdf ]]; then
  cp phase3/artifacts/origin-axiom-phase3.pdf artifacts/origin-axiom-phase3.pdf
  echo "[build_phase3_paper] Copied phase3/artifacts/origin-axiom-phase3.pdf -> artifacts/origin-axiom-phase3.pdf"
else
  echo "[build_phase3_paper] WARNING: missing phase3/artifacts/origin-axiom-phase3.pdf" >&2
fi

echo "[build_phase3_paper] Done."
echo "[build_phase3_paper] Canonical artifacts:"
echo "  phase3/artifacts/origin-axiom-phase3.pdf"
echo "  artifacts/origin-axiom-phase3.pdf"
