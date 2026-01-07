#!/usr/bin/env bash
set -euo pipefail

LEVEL="A"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --level)
      LEVEL="$2"
      shift 2
      ;;
    *)
      echo "[phase4_gate] Unknown argument: $1" >&2
      exit 1
      ;;
  esac
done

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${HERE}"
if [[ -f "${HERE}/../phase0/SCOPE.md" ]]; then
  ROOT="${HERE}/.."
fi

echo "[phase4_gate] Level = ${LEVEL}"
echo "[phase4_gate] Repo root: ${ROOT}"

cd "${ROOT}"

PHASE4_WORKFLOW="${ROOT}/phase4/workflow/Snakefile"

if [[ ! -f "${PHASE4_WORKFLOW}" ]]; then
  echo "[phase4_gate] ERROR: Phase 4 Snakefile not found at ${PHASE4_WORKFLOW}" >&2
  exit 1
fi

case "${LEVEL}" in
  A|a)
    echo "[phase4_gate] Level A: rebuild Phase 4 paper and canonical artifact"
    snakemake \
      --snakefile "${PHASE4_WORKFLOW}" \
      --cores 1 \
      --use-envmodules \
      all
    ;;
  *)
    echo "[phase4_gate] ERROR: unsupported level '${LEVEL}'. Only A is defined at this rung." >&2
    exit 1
    ;;
esac

echo "[phase4_gate] OK"
