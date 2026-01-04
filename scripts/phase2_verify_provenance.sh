#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
phase="phase2"

out_fig="$root/$phase/outputs/figures"
runs_dir="$root/$phase/outputs/runs"

need () { command -v "$1" >/dev/null || { echo "ERROR: missing $1"; exit 1; }; }
need rg
need python3

figs=(
  "figA_mode_sum_residual"
  "figB_scaling_epsilon"
  "figC_scaling_cutoff"
  "figD_scaling_modes"
  "figE_frw_comparison"
)

echo "== Phase 2 Provenance Verification (P2-S3) =="
echo "root: $root"
echo

fail=0

echo "1) Check required sidecars exist + run_id resolves"
for f in "${figs[@]}"; do
  sid="$out_fig/${f}.run_id.txt"
  if [ ! -f "$sid" ]; then
    echo "MISSING: $sid"
    fail=1
    continue
  fi
  rid="$(tr -d ' \t\r\n' < "$sid" || true)"
  if [ -z "$rid" ]; then
    echo "EMPTY: $sid"
    fail=1
    continue
  fi
  echo "OK: $f -> $rid"
done
echo

echo "2) For each run_id: enforce required files exist"
req_files=("meta.json" "params_resolved.json" "pip_freeze.txt" "summary.json")
for f in "${figs[@]}"; do
  rid="$(tr -d ' \t\r\n' < "$out_fig/${f}.run_id.txt" || true)"
  [ -n "$rid" ] || { echo "SKIP: no run_id for $f"; fail=1; continue; }

  rdir="$runs_dir/$rid"
  if [ ! -d "$rdir" ]; then
    echo "MISSING RUN DIR: $rdir"
    fail=1
    continue
  fi

  for rf in "${req_files[@]}"; do
    if [ ! -f "$rdir/$rf" ]; then
      echo "MISSING: $rdir/$rf"
      fail=1
    fi
  done

  # also require figures/ exists (even if empty is suspicious)
  if [ ! -d "$rdir/figures" ]; then
    echo "MISSING: $rdir/figures/"
    fail=1
  fi
done
echo

echo "3) Minimal content checks (no jq): meta.json must mention git/commit and params"
for f in "${figs[@]}"; do
  rid="$(tr -d ' \t\r\n' < "$out_fig/${f}.run_id.txt" || true)"
  [ -n "$rid" ] || { fail=1; continue; }
  mp="$runs_dir/$rid/meta.json"
  if [ ! -f "$mp" ]; then
    echo "MISSING: $mp"
    fail=1
    continue
  fi

  if ! rg -n -S 'git|commit' "$mp" >/dev/null 2>&1; then
    echo "FAIL: $mp lacks git/commit info"
    fail=1
  fi
  if ! rg -n -S 'param|config|yaml|resolved' "$mp" >/dev/null 2>&1; then
    echo "WARN: $mp lacks obvious param/config hints (ok if params are in params_resolved.json)"
  fi
done
echo

if [ "$fail" -ne 0 ]; then
  echo "FAIL: provenance verification failed."
  exit 1
fi

echo "OK: provenance verification passed."
