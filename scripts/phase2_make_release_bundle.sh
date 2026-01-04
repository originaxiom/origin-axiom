#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

ts="$(date -u +"%Y%m%dT%H%M%SZ")"
rel="phase2/outputs/release/phase2_release_${ts}"
mkdir -p "$rel"

echo "== Phase 2 Release Bundle =="
echo "root: $root"
echo "out:  $rel"
echo

# 1) Build paper
echo "[1/5] Build Phase 2 paper"
( cd phase2/paper && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex >/dev/null )
cp -f phase2/paper/main.pdf "$rel/main.pdf"

# 2) Lint + provenance checks
echo "[2/5] Run lint + provenance checks"
set +e
bash scripts/phase2_paper_lint.sh >/dev/null
lint_rc=$?
bash scripts/phase2_verify_provenance.sh >/dev/null
prov_rc=$?
set -e

# 3) Copy paper bundle (figures + run_index)
echo "[3/5] Copy paper_bundle snapshot"
if [ -d "phase2/outputs/paper_bundle" ]; then
  mkdir -p "$rel/paper_bundle"
  rsync -a --delete "phase2/outputs/paper_bundle/" "$rel/paper_bundle/"
else
  echo "WARN: phase2/outputs/paper_bundle missing (skipping)" >&2
fi

# 4) Export run manifest sources
echo "[4/5] Export run manifest sources"
mkdir -p "$rel/manifest"
cp -f phase2/paper/appendix/A_run_manifest.tex "$rel/manifest/A_run_manifest.tex"
if [ -f "phase2/outputs/paper_bundle/run_index.json" ]; then
  cp -f "phase2/outputs/paper_bundle/run_index.json" "$rel/manifest/run_index.json"
fi

# 5) Write checks summary
echo "[5/5] Write checks summary"
git_hash="$(git rev-parse --short HEAD 2>/dev/null || echo unknown)"
branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo unknown)"

{
  echo "Phase 2 release bundle"
  echo "UTC: $ts"
  echo "Git: $git_hash ($branch)"
  echo
  echo "lint_rc=$lint_rc (0 means pass)"
  echo "prov_rc=$prov_rc (0 means pass)"
  echo
  echo "Includes:"
  echo " - main.pdf"
  echo " - manifest/A_run_manifest.tex"
  echo " - manifest/run_index.json (if available)"
  echo " - paper_bundle/ (if available)"
} > "$rel/checks.txt"

echo
echo "OK: wrote $rel"
