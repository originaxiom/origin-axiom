#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

echo "== Phase 2 Gate =="
echo "root: $root"
echo "git:  $(git rev-parse --short HEAD) ($(git rev-parse --abbrev-ref HEAD))"
echo

echo "[1/4] Structural audit"
bash scripts/phase2_structural_audit.sh >/dev/null
echo "OK: audit"

echo "[2/4] Provenance verification"
bash scripts/phase2_verify_provenance.sh >/dev/null
echo "OK: provenance"

echo "[3/4] Paper lint"
bash scripts/phase2_paper_lint.sh >/dev/null
echo "OK: lint"

echo "[4/4] Clean build"
( cd phase2/paper && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex >/dev/null )
echo "OK: build"

echo
echo "PASS: Phase 2 gate"
