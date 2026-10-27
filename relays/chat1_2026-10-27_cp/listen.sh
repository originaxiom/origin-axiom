#!/bin/bash
# A silent listener (the owner, 2026-10-27: "agree with other seats to hire silent listeners to eachother").
# Polls the other seats' branches and prints nothing until a new commit there addresses this seat; then it prints one
# line per such commit and exits, so the seat is woken once, reads the news in git, and re-arms the listener.
# A commit addresses the seat when it adds or changes a file whose path matches FILE_PATTERN (the relay naming
# convention FROM_TO_<RECIPIENTS>_DATE_TITLE.md: e.g. CHAT1, ALL_SEATS), or adds lines to a .md file that match
# TEXT_PATTERN (e.g. "the web seat", which catches register and harvest rows). It never pushes, commits or writes
# into the repository; it only fetches. The state (the last commit seen per branch) lives in STATE_DIR. With no news
# it exits after MAX_SECONDS with one line, so the seat knows to re-arm.
#   listen.sh REPO STATE_DIR INTERVAL_SECONDS MAX_SECONDS FILE_PATTERN TEXT_PATTERN BRANCH...
#   e.g. listen.sh . ~/.listen 180 7000 'CHAT1|ALL_SEATS' 'web seat|chat1' main <another seat's branch>
# Seed STATE_DIR/<branch with / as _> with the last commit already read, or the first poll takes the current head.
REPO=$1; STATE=$2; INT=$3; MAX=$4; FPAT=$5; TPAT=$6; shift 6
mkdir -p "$STATE"
T0=$(date +%s)
while :; do
  git -C "$REPO" fetch -q origin 2>/dev/null || true
  hits=""
  for br in "$@"; do
    new=$(git -C "$REPO" rev-parse -q --verify "origin/$br" 2>/dev/null) || continue
    f="$STATE/$(echo "$br" | tr '/' '_')"
    old=$(cat "$f" 2>/dev/null)
    if [ -z "$old" ]; then echo "$new" > "$f"; continue; fi
    [ "$old" = "$new" ] && continue
    for c in $(git -C "$REPO" rev-list --reverse "$old..$new" 2>/dev/null); do
      files=$(git -C "$REPO" diff-tree --no-commit-id --name-only -r "$c" | grep -i -E "$FPAT" | tr '\n' ' ')
      n=$(git -C "$REPO" show --format= --unified=0 "$c" -- '*.md' | grep -E '^\+[^+]' | grep -c -i -E "$TPAT")
      if [ -n "$files" ] || [ "$n" -gt 0 ]; then
        hits="${hits}${br} $(git -C "$REPO" log -1 --format='%h %ad' --date=format:'%m-%d %H:%M' "$c"): $(git -C "$REPO" log -1 --format=%s "$c" | cut -c1-140) | files: ${files:-none} | lines naming this seat: $n"$'\n'
      fi
    done
    echo "$new" > "$f"
  done
  if [ -n "$hits" ]; then printf '%s' "$hits"; exit 0; fi
  if [ $(( $(date +%s) - T0 )) -ge "$MAX" ]; then echo "listener: no news for this seat in $MAX s; re-arm"; exit 0; fi
  sleep "$INT"
done
