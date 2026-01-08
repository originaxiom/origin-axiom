#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_ROOT}"

echo "==> Running Phase 0 gate..."
scripts/phase0_gate.sh

echo "==> Running Phase 1 gate..."
scripts/phase1_gate.sh

echo "==> Running Phase 2 gate..."
scripts/phase2_gate.sh

echo "==> Running Phase 3 gate..."
scripts/phase3_gate.sh

echo "==> Running Phase 4 gate..."
scripts/phase4_gate.sh

echo "==> Running Phase 5 build (gate + paper)..."
scripts/build_phase5_paper.sh

echo
echo "If all gates reported OK, canonical PDFs should now be at:"
echo "  phase0/artifacts/origin-axiom-phase0.pdf      (if gate exists)"
echo "  phase1/artifacts/origin-axiom-phase1.pdf      (if gate exists)"
echo "  phase2/artifacts/origin-axiom-phase2.pdf"
echo "  phase3/artifacts/origin-axiom-phase3.pdf"
echo "  phase4/artifacts/origin-axiom-phase4.pdf"
echo "  phase5/artifacts/origin-axiom-phase5.pdf"
