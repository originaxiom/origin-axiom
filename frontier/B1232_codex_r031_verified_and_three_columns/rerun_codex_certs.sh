#!/bin/sh
# Codex's R031A/R031B certs, RE-RUN ON THIS BENCH (integrate-don't-merge: verify, then rebank).
# Their seat lives at /Users/dri/oa-audit-seat/aud1t/codex-r023 on this machine.
set -e
D=/Users/dri/oa-audit-seat/aud1t/codex-r023
python3 "$D/certificates/r031a_b0_character_field/b0_character_field.py"
python3 "$D/certificates/r031b_rcft_scope/rcft_scope.py"
