#!/usr/bin/env bash
# Build THE PAPER. Requires a TeX distribution on PATH.
set -euo pipefail
cd "$(dirname "$0")"
export PATH="/Library/TeX/texbin:$PATH"
pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null
pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null   # resolve refs
echo "built main.pdf -- $(pdfinfo main.pdf | awk '/^Pages/{print $2}') pages"
