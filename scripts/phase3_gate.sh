#!/usr/bin/env bash
set -euo pipefail

LEVEL="A"
if [[ "${1:-}" == "--level" ]]; then
  LEVEL="${2:-A}"
elif [[ -n "${1:-}" ]]; then
  LEVEL="${1}"
fi

echo "[phase3_gate] Level = ${LEVEL}"
echo "[phase3_gate] Repo root: $(pwd)"

# Basic structure checks
test -f phase3/SCOPE.md
test -f phase3/NON_CLAIMS.md
test -f phase3/REPRODUCIBILITY.md
test -f phase3/workflow/Snakefile

verify_bundle () {
  python phase3/src/phase3/provenance/verify_bundle.py \
    --run_index phase3/outputs/paper_bundle/run_index.json \
    --manifest phase3/outputs/paper_bundle/bundle_manifest.json
}

if [[ "${LEVEL}" == "A" ]]; then
  echo "[phase3_gate] Level A: verify bundle exists + manifests"
  test -f phase3/outputs/paper_bundle/run_index.json
  test -f phase3/outputs/paper_bundle/bundle_manifest.json
  verify_bundle
  echo "[phase3_gate] OK"
  exit 0
fi

if [[ "${LEVEL}" == "B" ]]; then
  echo "[phase3_gate] Level B: regenerate artifacts + bundle"
  snakemake -s phase3/workflow/Snakefile -c 1 all
  verify_bundle
  echo "[phase3_gate] OK"
  exit 0
fi

if [[ "${LEVEL}" == "C" ]]; then
  echo "[phase3_gate] Level C: developer heavy runs (optional)"
  snakemake -s phase3/workflow/Snakefile -c 1 all
  verify_bundle
  echo "[phase3_gate] OK"
  exit 0
fi

echo "[phase3_gate] Unknown level: ${LEVEL}"
exit 2
