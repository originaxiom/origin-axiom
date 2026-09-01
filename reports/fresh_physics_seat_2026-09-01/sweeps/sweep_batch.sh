#!/usr/bin/env bash
# Batch absence sweep (owner's rule, 2026-09-01): one line per claim in CLAIMS_TSV
#   id <TAB> content-regex (ERE, case-insensitive; empty = skip) <TAB> filename-regex (ERE; empty = skip)
# For every remote head: ls-tree filename hits + git-grep content hits (seat's own report dir excluded),
# then deleted-file history over all refs. Output is the raw evidence a verdict must quote.
set -u
cd "$(git rev-parse --show-toplevel)" || exit 1
TSV="${1:?claims tsv}"; OUT="${2:?output file}"
HEADS=$(git ls-remote --heads origin | awk '{print $1" "$2}' | sed 's#refs/heads/##')
DEL=$(git log --all --diff-filter=D --name-only --pretty=format:'%h %ad %s' --date=short)
: > "$OUT"
while IFS=$'\t' read -r id cre fre; do
  [ -z "$id" ] && continue; case "$id" in \#*) continue;; esac
  { echo "################ $id"; echo "content=/$cre/  filename=/$fre/"; } >> "$OUT"
  while read -r h name; do
    fh=""; ch=""
    [ -n "$fre" ] && fh=$(git ls-tree -r --name-only "$h" | grep -E -i "$fre" | grep -v '^reports/fresh_physics_seat')
    [ -n "$cre" ] && ch=$(git grep -I -l -E -i "$cre" "$h" -- . ':(exclude)reports/fresh_physics_seat_2026-09-01' 2>/dev/null | sed "s#^$h:##")
    nf=$(printf '%s' "$fh" | grep -c .); nc=$(printf '%s' "$ch" | grep -c .)
    echo "-- $name ($h): filename hits=$nf content hits=$nc" >> "$OUT"
    [ "$nf" -gt 0 ] && printf '%s\n' "$fh" | sed 's/^/     F /' | head -25 >> "$OUT"
    [ "$nc" -gt 0 ] && printf '%s\n' "$ch" | sed 's/^/     C /' | head -25 >> "$OUT"
  done <<< "$HEADS"
  if [ -n "$fre" ]; then
    d=$(printf '%s\n' "$DEL" | grep -E -i -B3 "$fre" | grep -v '^--$')
    echo "-- deleted-in-history (all refs) filename hits: $(printf '%s' "$d" | grep -c '^[a-z]' )" >> "$OUT"
    [ -n "$d" ] && printf '%s\n' "$d" | sed 's/^/     D /' | head -20 >> "$OUT"
  fi
done < "$TSV"
echo "== done: $(grep -c '^################' "$OUT") claims swept ==" >> "$OUT"
