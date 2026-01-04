#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

build_one () {
  local dir="$1"
  local target="$2"
  echo "==> Building: ${dir}/${target}"
  ( cd "$root/$dir" && latexmk -pdf -interaction=nonstopmode -halt-on-error "$target" >/dev/null )
  echo "OK: ${dir}/${target}"
}

build_one "phase0/paper" "main.tex"
build_one "phase0/paper" "appendices.tex"
build_one "phase1/paper" "main.tex"
build_one "phase2/paper" "main.tex"

echo
echo "Done. PDFs should exist at:"
echo "  phase0/paper/main.pdf"
echo "  phase0/paper/appendices.pdf"
echo "  phase1/paper/main.pdf"
