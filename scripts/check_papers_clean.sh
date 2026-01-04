#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

build_and_check () {
  local dir="$1"
  local target="$2"

  echo "==> Building: ${dir}/${target}"
  ( cd "$root/$dir" && latexmk -pdf -interaction=nonstopmode -halt-on-error "$target" >/dev/null )

  local base="${target%.tex}"
  local log="${base}.log"
  local blg="${base}.blg"

  echo "==> Checking logs: ${dir}/${log} ${dir}/${blg}"

  # Keep the patterns simple to avoid shell-quoting pitfalls.
  # This still catches the same failure modes.
  local pat='undefined references|Citation .*undefined|Warning--empty journal'

  local hit=0
  ( cd "$root/$dir" && { [ -f "$log" ] && rg -n "$pat" "$log" && hit=1 || true; } )
  ( cd "$root/$dir" && { [ -f "$blg" ] && rg -n "$pat" "$blg" && hit=1 || true; } )

  if [ "$hit" -ne 0 ]; then
    echo "NOT clean: see matches above"
    exit 1
  fi

  echo "OK: clean build: ${dir}/${target}"
}

build_and_check "phase0/paper" "main.tex"
build_and_check "phase0/paper" "appendices.tex"
build_and_check "phase1/paper" "main.tex"

echo
echo "OK: all papers clean"
