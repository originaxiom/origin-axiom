#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
paper="$root/phase2/paper"

need () { command -v "$1" >/dev/null || { echo "ERROR: missing $1"; exit 1; }; }
need rg
need latexmk

echo "== Phase 2 Paper Lint =="

echo "1) No TODO/FIXME/XXX/TBD in Phase 2 paper sources"
if rg -n "TODO|FIXME|XXX|TBD" "$paper" -S >/dev/null 2>&1; then
  rg -n "TODO|FIXME|XXX|TBD" "$paper" -S
  echo "FAIL: placeholders found"
  exit 1
fi
echo "OK"

echo "2) Build main.tex"
( cd "$paper" && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex >/dev/null )

echo "3) Log scan (common failures)"
rg -n 'undefined references|Warning--empty journal|Citation .* undefined' \
  "$paper/main.log" "$paper/main.blg" 2>/dev/null && { echo "FAIL: log issues"; exit 1; } || true
echo "OK: build + logs"

echo "OK: Phase 2 paper lint passed."
