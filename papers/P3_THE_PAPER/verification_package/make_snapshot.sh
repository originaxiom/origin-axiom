#!/usr/bin/env bash
# Make the repository snapshot that the paper's appendix cites: a tar.gz of the tracked tree at the
# current commit, named by that commit, for deposit (Zenodo or equivalent) before the arXiv upload.
# The DOI the deposit assigns is then written into the paper's appendix (paper_provenance.py, DOI line)
# and the package is rebuilt. Usage: bash make_snapshot.sh [outdir]
set -euo pipefail
ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
OUT="${1:-$ROOT/audit/paper_submission}"
mkdir -p "$OUT"
SHA="$(git -C "$ROOT" rev-parse --short=12 HEAD)"
if [ -n "$(git -C "$ROOT" status --porcelain | grep -v '^??')" ]; then echo "tree not clean at $SHA; commit first" >&2; exit 1; fi
git -C "$ROOT" archive --format=tar.gz --prefix="origin-axiom-$SHA/" -o "$OUT/origin-axiom-$SHA.tar.gz" HEAD
shasum -a 256 "$OUT/origin-axiom-$SHA.tar.gz" | tee "$OUT/origin-axiom-$SHA.tar.gz.sha256"
echo "snapshot: $OUT/origin-axiom-$SHA.tar.gz  (commit $SHA)"
