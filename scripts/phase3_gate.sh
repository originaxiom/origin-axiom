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
      echo "[phase3_gate] Unknown argument: $1" >&2
      exit 1
      ;;
  esac
done

ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )"
cd "$ROOT"

echo "[phase3_gate] Level = ${LEVEL}"
echo "[phase3_gate] Repo root: ${ROOT}"

# At Rung 1, Level A/B both just rebuild the paper + artifact.
snakemake -s phase3/workflow/Snakefile --cores 1 all

echo "[phase3_gate] OK"
