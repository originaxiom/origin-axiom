#!/usr/bin/env bash
set -euo pipefail

# Resolve repo root (one level above scripts/)
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$root"

echo "[build_paper] Unified paper rebuild via per-phase gates."
echo "[build_paper] Delegating to scripts/build_all_papers.sh ..."
echo

scripts/build_all_papers.sh

echo
echo "[build_paper] Done. Canonical PDFs (where gates exist) are at:"
echo "  phase0/artifacts/origin-axiom-phase0.pdf"
echo "  phase1/artifacts/origin-axiom-phase1.pdf"
echo "  phase2/artifacts/origin-axiom-phase2.pdf"
echo "  phase3/artifacts/origin-axiom-phase3.pdf"
echo "  phase4/artifacts/origin-axiom-phase4.pdf"
