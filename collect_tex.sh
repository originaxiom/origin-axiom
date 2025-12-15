#!/bin/bash

set -euo pipefail

# Run this from the repo root: ~/Documents/projects/origin-axiom
ROOT="$(pwd)"

# Put the collected files *inside the repo*, not at filesystem root
TARGET_DIR="$ROOT/tex_consolidated"

echo "Collecting .tex files under: $ROOT"
echo "Target directory: $TARGET_DIR"
mkdir -p "$TARGET_DIR"

# Find all .tex files but ignore virtualenvs and build dirs if any
find "$ROOT" \
  -type f -name "*.tex" \
  ! -path "*/venv/*" \
  ! -path "*/build/*" \
  ! -path "*/_minted-*/*" \
  -print \
  -exec bash -c '
    src="$1"
    target_dir="$2"
    root="$3"

    # Make a flat, unique name that still encodes the path
    rel="${src#"$root/"}"          # strip leading root/
    rel="${rel//\//__}"            # replace / with __
    cp "$src" "$target_dir/$rel.txt"
  ' _ {} "$TARGET_DIR" "$ROOT" \;

echo
echo "Done. Collected files in: $TARGET_DIR"
ls "$TARGET_DIR"