#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

phase="phase2"
fig_dir="$root/$phase/paper/figures"
out_fig="$root/$phase/outputs/figures"
runs_dir="$root/$phase/outputs/runs"

echo "== Phase 2 Claims Map Verification =="
echo "root: $root"
echo

need_rg () {
  command -v rg >/dev/null || { echo "ERROR: rg (ripgrep) not found"; exit 1; }
}
need_rg

# Figures required by the P2-S2 contract
figs=(
  "figA_mode_sum_residual"
  "figB_scaling_epsilon"
  "figC_scaling_cutoff"
  "figD_scaling_modes"
  "figE_frw_comparison"
)

fail=0

echo "1) Check paper figures exist (paper/figures/*.pdf)"
for f in "${figs[@]}"; do
  if [ ! -f "$fig_dir/${f}.pdf" ]; then
    echo "MISSING: $fig_dir/${f}.pdf"
    fail=1
  else
    echo "OK: $fig_dir/${f}.pdf"
  fi
done
echo

echo "2) Check run_id sidecars exist (outputs/figures/*.run_id.txt) + are non-empty"
for f in "${figs[@]}"; do
  p="$out_fig/${f}.run_id.txt"
  if [ ! -f "$p" ]; then
    echo "MISSING: $p"
    fail=1
    continue
  fi
  rid="$(tr -d ' \t\r\n' < "$p" || true)"
  if [ -z "$rid" ]; then
    echo "EMPTY: $p"
    fail=1
    continue
  fi
  echo "OK: $p -> $rid"
done
echo

echo "3) Check meta.json exists for each run_id and contains key fields"
for f in "${figs[@]}"; do
  rid="$(tr -d ' \t\r\n' < "$out_fig/${f}.run_id.txt" || true)"
  [ -n "$rid" ] || { echo "SKIP: no run_id for $f"; fail=1; continue; }

  mp="$runs_dir/$rid/meta.json"
  if [ ! -f "$mp" ]; then
    echo "MISSING: $mp"
    fail=1
    continue
  fi

  # lightweight sanity checks (no jq requirement)
  # we expect at least SOME mention of git / commit / params / pip / python
  if ! rg -n -S 'git|commit|params|pip|python' "$mp" >/dev/null 2>&1; then
    echo "WARN: $mp exists but lacks obvious provenance keys (git/commit/params/pip/python)"
  fi
  echo "OK: $mp"
done
echo

echo "4) Check Appendix run-manifest label exists"
if rg -n -F '\label{app:run_manifest}' "$root/$phase/paper/appendix/A_run_manifest.tex" >/dev/null; then
  echo "OK: app:run_manifest label present"
else
  echo "MISSING: \\label{app:run_manifest} in appendix/A_run_manifest.tex"
  fail=1
fi
echo

if [ "$fail" -ne 0 ]; then
  echo "FAIL: claims map verification failed (see above)."
  exit 1
fi

echo "OK: claims map verification passed."
