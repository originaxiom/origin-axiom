#!/usr/bin/env bash
# Absence-claim sweep (owner's rule, 2026-09-01): before concluding "we don't have X",
# sweep every remote head's tree (content + filenames) and the deleted-file history.
# usage: sweep_absence.sh '<content regex>' '<filename regex>'
set -u
CRE="${1:-}"; FRE="${2:-}"
cd "$(git rev-parse --show-toplevel)" || exit 1   # pathspecs below are repo-root relative
git fetch origin --quiet 2>/dev/null               # heads must be local for git grep / ls-tree
echo "== heads (git ls-remote --heads origin) =="
git ls-remote --heads origin | awk '{print $2" "$1}'
for h in $(git ls-remote --heads origin | awk '{print $1}'); do
  name=$(git ls-remote --heads origin | awk -v s=$h '$1==s{print $2}' | sed 's#refs/heads/##')
  if [ -n "$FRE" ]; then
    hits=$(git ls-tree -r --name-only "$h" | grep -E -i "$FRE" | grep -v "^reports/fresh_physics_seat" )
    [ -n "$hits" ] && { echo "-- filename hits on $name ($h):"; echo "$hits"; }
  fi
  if [ -n "$CRE" ]; then
    hits=$(git grep -I -l -E -i "$CRE" "$h" -- . ':(exclude)reports/fresh_physics_seat_2026-09-01' 2>/dev/null | sed "s#^$h:##")
    [ -n "$hits" ] && { echo "-- content hits on $name ($h):"; echo "$hits"; }
  fi
done
echo "== deleted files in history (all refs) matching filename regex =="
[ -n "$FRE" ] && git log --all --diff-filter=D --name-only --pretty=format:'%h %ad %s' --date=short | grep -E -i -B3 "$FRE" | head -40
echo "== done =="
