#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_ROOT}"

echo "[build_papers] DEPRECATED helper; delegating to scripts/build_paper.sh"
echo "[build_papers] This now runs all phase gates (0–5) and aggregates artifacts."
echo

exec scripts/build_paper.sh
