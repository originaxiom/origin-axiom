#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

echo "==> Running Phase 0 gate..."
if [ -x scripts/phase0_gate.sh ]; then
  scripts/phase0_gate.sh
else
  echo "Phase 0 gate script not found; skipping."
fi

echo "==> Running Phase 1 gate..."
if [ -x scripts/phase1_gate.sh ]; then
  scripts/phase1_gate.sh
else
  echo "Phase 1 gate script not found; skipping."
fi

echo "==> Running Phase 2 gate..."
if [ -x scripts/phase2_gate.sh ]; then
  scripts/phase2_gate.sh
else
  echo "Phase 2 gate script not found; skipping."
fi

echo "==> Running Phase 3 gate..."
if [ -x scripts/phase3_gate.sh ]; then
  scripts/phase3_gate.sh
else
  echo "Phase 3 gate script not found; skipping."
fi

echo "==> Running Phase 4 gate..."
if [ -x scripts/phase4_gate.sh ]; then
  scripts/phase4_gate.sh
else
  echo "Phase 4 gate script not found; skipping."
fi

echo
echo "If all gates reported OK, canonical PDFs should now be at:"
echo "  phase0/artifacts/origin-axiom-phase0.pdf      (if gate exists)"
echo "  phase1/artifacts/origin-axiom-phase1.pdf      (if gate exists)"
echo "  phase2/artifacts/origin-axiom-phase2.pdf"
echo "  phase3/artifacts/origin-axiom-phase3.pdf"
echo "  phase4/artifacts/origin-axiom-phase4.pdf"
