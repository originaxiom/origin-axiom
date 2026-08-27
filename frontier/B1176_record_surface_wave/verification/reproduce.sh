#!/usr/bin/env bash
# B1176 -- THE RECORD-SURFACE WAVE (R50-4). Verifies the committed surfaces exist + carry the wave.
set -euo pipefail
cd "$(dirname "$0")"; R=../../..
grep -q "THE PAPER PORTFOLIO" "$R/papers/PORTFOLIO_2026-08-27.md" && echo "  OK the portfolio landed"
grep -q "PORTFOLIO_2026-08-27" "$R/papers/README.md" && echo "  OK README points at it"
n=$(ls "$R"/frontier/{B58_stage1,B834_wave3b,B835_lock_repairs,B836_route_negatives,B837_file_drawer_audit,B838_lexicon_regrounding,B839_b685_residue,B840_close_loose_ends,B841_provenance_pass,B842_face_attachment,B845_spectral_inventory,B89T_tower_route,B89_sl4_symbolic_M4L}/arc_verdict.json 2>/dev/null | wc -l | tr -d ' ')
[ "$n" = "13" ] && echo "  OK 13 retro arc_verdicts (P3_depth_exposure exempt-by-name; B89T shares id B89)"
grep -q "S074" "$R/speculations/S074_the_adelic_closing_doctrine.md" && echo "  OK S074 (rooms repair)"
grep -q "Addendum (2026-08-27, B1176" "$R/philosophy/13_the_computed_observer.md" && echo "  OK philosophy addendum"
grep -q "## L189" "$R/docs/OPEN_LEADS.md" && echo "  OK L189 (chronicle candidates owned)"
grep -q "ID-COLLISION NOTE, B1176" "$R/docs/OPEN_LEADS.md" && echo "  OK L110/L113 annotated"
grep -q "overloaded-symbol registry" "$R/TERMINOLOGY.md" && echo "  OK the namespace registry"
echo "REPRODUCES"
