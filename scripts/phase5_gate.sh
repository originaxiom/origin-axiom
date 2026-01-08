#!/usr/bin/env bash
set -euo pipefail

LEVEL="${PHASE5_LEVEL:-A}"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
echo "[phase5_gate] Level = ${LEVEL}"
echo "[phase5_gate] Repo root: ${REPO_ROOT}"

echo "Assuming unrestricted shared filesystem usage."
echo "host: $(hostname)"

cd "${REPO_ROOT}"

echo "[phase5_gate] Running Phase 5 interface v1..."
python phase5/src/phase5/phase5_interface_v1.py

echo "[phase5_gate] OK"
