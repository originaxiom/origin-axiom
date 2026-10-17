#!/bin/sh
set -e
cd "$(dirname "$0")/tex" && latexmk -pdf -interaction=nonstopmode -quiet main.tex && cp main.pdf ../theta_triplet_note.pdf
