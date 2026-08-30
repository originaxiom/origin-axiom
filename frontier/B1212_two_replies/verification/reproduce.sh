#!/usr/bin/env bash
# B1212 -- codex's R024 certificate, re-run on this bench from their committed inputs.
set -euo pipefail
cd "$(dirname "$0")"
python3 r024_lepton_character_datum.py | tee r024_rerun.txt | tail -8
grep -q "PASS" r024_rerun.txt && grep -q "UNRESOLVED" r024_rerun.txt && echo REPRODUCES
