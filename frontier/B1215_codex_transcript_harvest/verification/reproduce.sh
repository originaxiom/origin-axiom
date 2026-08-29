#!/usr/bin/env bash
# B1215 -- the tail-selection rule, and the wrapper-honesty census.
set -euo pipefail
cd "$(dirname "$0")"
python3 tail_selection.py | tee _out.txt | tail -6
cd ../../..
echo
echo "wrapper census (reproduce.sh printing REPRODUCES with no gate on the result):"
bad=0
for f in frontier/*/verification/reproduce.sh; do
  if grep -q "echo REPRODUCES" "$f" 2>/dev/null && ! grep -qE "grep -q|\[ .* \]|&&|assert" "$f"; then
    bad=$((bad+1)); echo "  UNGATED: $f"
  fi
done
echo "  ungated: $bad (was 4 at B1215)"
grep -q VERIFIED frontier/B1215_codex_transcript_harvest/verification/_out.txt \
  && [ "$bad" -eq 0 ] && echo REPRODUCES || { echo FAILED; exit 1; }
