#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_ROOT}"

echo "[build_phase2_paper] Running Phase 2 gate..."
scripts/phase2_gate.sh

echo "[build_phase2_paper] Syncing artifact to top-level artifacts/ ..."
mkdir -p artifacts
if [[ -f phase2/artifacts/origin-axiom-phase2.pdf ]]; then
  cp phase2/artifacts/origin-axiom-phase2.pdf artifacts/origin-axiom-phase2.pdf
  echo "[build_phase2_paper] Copied phase2/artifacts/origin-axiom-phase2.pdf -> artifacts/origin-axiom-phase2.pdf"
else
  echo "[build_phase2_paper] WARNING: missing phase2/artifacts/origin-axiom-phase2.pdf" >&2
fi

echo "[build_phase2_paper] Done."
echo "[build_phase2_paper] Canonical artifacts:"
echo "  phase2/artifacts/origin-axiom-phase2.pdf"
echo "  artifacts/origin-axiom-phase2.pdf"
