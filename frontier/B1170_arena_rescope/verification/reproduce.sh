#!/usr/bin/env bash
# B1170 -- THE ARENA RESCOPE. cc3's B8143 (4-commit chain, CORRECTED at bf3e426d) + codex's R019
# rescope the gravity charter's G1/E2 row: the anomaly-forcing package is ARENA-GENERIC.
# "THE OBJECT SUPPLIES THE ARENA; THE ANOMALIES SUPPLY THE CONTENT."
# This runner re-derives the core INDEPENDENTLY (own code path: Fraction Gaussian elimination +
# explicit homogeneous-cubic analysis; no sympy.solve): over the SM-visible 5-field alphabet,
# 252 contents, 222 killed by [SU(3)]^3 alone, exactly TWO rigid+chiral+anomaly-free survivors --
# the SM 15-plet (1/6,-2/3,1/3,-1/2,1) and its conjugate. Zero object tokens enter any equation.
set -euo pipefail
cd "$(dirname "$0")"
python3 independent_enumeration.py | tee enumeration_out.txt
echo
echo "CROSS-CHECKS (run on this bench 2026-08-27, cited):"
echo "  - cc3 lane steps 4-6 (origin/paper/structure-genesis-first, frontier/B8143_anomaly_lane/):"
echo "    step4 -> the same 2 survivors; step5 -> adjoints 7 / (3,3) 14 (uniqueness alphabet-dependent,"
echo "    minimality not); step6 token-audit -> object_tokens_in_executable_code = NONE."
echo "  - codex R019 (codex/seat-r001 4652f450): hypercharge_trinification_scope.py BYTE-IDENTICAL --"
echo "    36/36 SM in all three color frames, universal reduction Yl/Yq=-3, Ye/Yq=6, (Yu+Yd)/Yq=-2,"
echo "    cubic=-18(Yu/Yq-2)(Yu/Yq+4); 'the frame, physical 15-plet, gauging and overall normalization"
echo "    are not selected.'"
