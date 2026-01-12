#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_ROOT}"

echo "[build_phase0_paper] Running Phase 0 gate..."
scripts/phase0_gate.sh

echo "[build_phase0_paper] Syncing artifact to top-level artifacts/ ..."
mkdir -p artifacts
if [[ -f phase0/artifacts/origin-axiom-phase0.pdf ]]; then
  cp phase0/artifacts/origin-axiom-phase0.pdf artifacts/origin-axiom-phase0.pdf
  echo "[build_phase0_paper] Copied phase0/artifacts/origin-axiom-phase0.pdf -> artifacts/origin-axiom-phase0.pdf"
else
  echo "[build_phase0_paper] WARNING: missing phase0/artifacts/origin-axiom-phase0.pdf" >&2
fi

echo "[build_phase0_paper] Done."
echo "[build_phase0_paper] Canonical artifacts:"
echo "  phase0/artifacts/origin-axiom-phase0.pdf"
echo "  artifacts/origin-axiom-phase0.pdf"
