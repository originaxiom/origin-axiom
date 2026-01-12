#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_ROOT}"

echo "[build_phase4_paper] Running Phase 4 gate..."
scripts/phase4_gate.sh

echo "[build_phase4_paper] Syncing artifact to top-level artifacts/ ..."
mkdir -p artifacts
if [[ -f phase4/artifacts/origin-axiom-phase4.pdf ]]; then
  cp phase4/artifacts/origin-axiom-phase4.pdf artifacts/origin-axiom-phase4.pdf
  echo "[build_phase4_paper] Copied phase4/artifacts/origin-axiom-phase4.pdf -> artifacts/origin-axiom-phase4.pdf"
else
  echo "[build_phase4_paper] WARNING: missing phase4/artifacts/origin-axiom-phase4.pdf" >&2
fi

echo "[build_phase4_paper] Done."
echo "[build_phase4_paper] Canonical artifacts:"
echo "  phase4/artifacts/origin-axiom-phase4.pdf"
echo "  artifacts/origin-axiom-phase4.pdf"
