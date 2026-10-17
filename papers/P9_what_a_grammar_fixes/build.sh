#!/bin/sh
# Rebuild the figures from the record's committed outputs (each checked by hash), then the PDF.
set -e
cd "$(dirname "$0")"
for f in figscripts/fig_*.py; do OMP_NUM_THREADS=1 python3 -B "$f"; done
python3 -B checks/commutator_subgroup.py
python3 -B checks/cusp_law.py
cd tex && latexmk -pdf -interaction=nonstopmode -quiet main.tex
cd .. && python3 -B checks/source_hygiene.py tex tex/main.log && cd tex
cp main.pdf ../what_a_grammar_fixes.pdf
