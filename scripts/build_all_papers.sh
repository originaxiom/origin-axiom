#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

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

echo "==> Running Phase 5 gate..."
scripts/phase5_gate.sh

# Aggregate canonical PDFs into top-level artifacts/
ARTIFACT_DIR="$REPO_ROOT/artifacts"
mkdir -p "$ARTIFACT_DIR"

for phase in 0 1 2 3 4 5; do
    src="$REPO_ROOT/phase${phase}/artifacts/origin-axiom-phase${phase}.pdf"
    dst="$ARTIFACT_DIR/origin-axiom-phase${phase}.pdf"

    if [[ -f "$src" ]]; then
        cp "$src" "$dst"
        echo "[build_all_papers] Copied phase${phase} -> artifacts/$(basename "$dst")"
    else
        echo "[build_all_papers] WARNING: missing artifact: $src" >&2
    fi
done

echo
echo "Canonical phase PDFs are at:"
for phase in 0 1 2 3 4 5; do
    echo "  phase${phase}/artifacts/origin-axiom-phase${phase}.pdf"
done

echo
echo "Aggregated copies are at:"
ls -1 "$ARTIFACT_DIR" || true
