#!/usr/bin/env bash
set -euo pipefail

LEVEL="A"
if [[ "${1:-}" == "--level" ]]; then
  LEVEL="${2:-A}"
elif [[ -n "${1:-}" ]]; then
  LEVEL="${1}"
fi

echo "[experiments/phase3_flavor_v1_gate] Level = ${LEVEL}"
echo "[experiments/phase3_flavor_v1_gate] Repo root: $(pwd)"

# Basic structure checks
test -f experiments/phase3_flavor_v1/SCOPE.md
test -f experiments/phase3_flavor_v1/NON_CLAIMS.md
test -f experiments/phase3_flavor_v1/REPRODUCIBILITY.md
test -f experiments/phase3_flavor_v1/workflow/Snakefile

verify_bundle () {
  python experiments/phase3_flavor_v1/src/experiments/phase3_flavor_v1/provenance/verify_bundle.py \
    --run_index experiments/phase3_flavor_v1/outputs/paper_bundle/run_index.json \
    --manifest experiments/phase3_flavor_v1/outputs/paper_bundle/bundle_manifest.json
}

if [[ "${LEVEL}" == "A" ]]; then
  echo "[experiments/phase3_flavor_v1_gate] Level A: verify bundle exists + manifests"
  test -f experiments/phase3_flavor_v1/outputs/paper_bundle/run_index.json
  test -f experiments/phase3_flavor_v1/outputs/paper_bundle/bundle_manifest.json
  verify_bundle
  echo "[experiments/phase3_flavor_v1_gate] OK"
  exit 0
fi

if [[ "${LEVEL}" == "B" ]]; then
  echo "[experiments/phase3_flavor_v1_gate] Level B: regenerate artifacts + bundle"
  snakemake -s experiments/phase3_flavor_v1/workflow/Snakefile -c 1 all
  verify_bundle
  echo "[experiments/phase3_flavor_v1_gate] OK"
  exit 0
fi

if [[ "${LEVEL}" == "C" ]]; then
  echo "[experiments/phase3_flavor_v1_gate] Level C: developer heavy runs (optional)"
  snakemake -s experiments/phase3_flavor_v1/workflow/Snakefile -c 1 all
  verify_bundle
  echo "[experiments/phase3_flavor_v1_gate] OK"
  exit 0
fi

echo "[experiments/phase3_flavor_v1_gate] Unknown level: ${LEVEL}"
exit 2
