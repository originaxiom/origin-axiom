#!/bin/bash
# A silent listener (the owner, 2026-10-27: "agree with other seats to hire silent listeners to eachother").
# Polls the other seats' branches and prints nothing until a new commit there addresses this seat; then it prints one
# line per such commit and exits, so the seat is woken once, reads the news in git, and re-arms the listener.
# A commit addresses the seat when it adds or changes a file whose path matches FILE_PATTERN, or adds lines to a .md
# file that match TEXT_PATTERN (e.g. "the web seat", which catches register and harvest rows, and a running relay
# file whose sections name their readers). Under the record's naming, FROM_TO_RECIPIENTS_DATE_TITLE.md, read only the
# recipients part of a name, so that a short token does not match a title word or an unrelated file:
#   FILE_PATTERN='_TO_([A-Z0-9]+_)*(CHAT1|ALL_SEATS)_([A-Z0-9]+_)*20[0-9][0-9]-'   (put the seat's own tokens inside)
# It runs only git fetch and read-only git commands: it never commits, pushes, or touches the working tree or local
# branches. The state (the last commit read per branch) lives in STATE_DIR, written only after the news is printed.
# With no news it exits after MAX_SECONDS with one line (and the count of failed fetches), so the seat re-arms. It
# exits loudly, never silently, on a branch it cannot find or a read point that is not in this clone.
#   listen.sh REPO STATE_DIR INTERVAL_SECONDS MAX_SECONDS FILE_PATTERN TEXT_PATTERN BRANCH...
#   e.g. listen.sh . ~/.listen 180 7000 '_TO_([A-Z0-9]+_)*(CHAT1|ALL_SEATS)_([A-Z0-9]+_)*20[0-9][0-9]-' 'web seat|chat1' main <another seat's branch>
# Seed STATE_DIR/<branch with / as _> with the last commit already read, or the first poll takes the current head.
REPO=$1; STATE=$2; INT=$3; MAX=$4; FPAT=$5; TPAT=$6; shift 6
mkdir -p "$STATE"
T0=$(date +%s); fails=0
while :; do
  timeout 300 git -C "$REPO" fetch -q origin 2>/dev/null || fails=$((fails + 1))
  hits=""; declare -A next=()
  for br in "$@"; do
    new=$(git -C "$REPO" rev-parse -q --verify "origin/$br^{commit}" 2>/dev/null) \
      || { echo "listener: origin/$br not found; fix the branch list and re-arm"; exit 1; }
    f="$STATE/$(echo "$br" | tr '/' '_')"
    old=$(cat "$f" 2>/dev/null)
    if [ -z "$old" ]; then echo "$new" > "$f"; continue; fi
    [ "$old" = "$new" ] && continue
    git -C "$REPO" cat-file -e "$old^{commit}" 2>/dev/null \
      || { echo "listener: read point $old of $br is not in this clone; re-seed and re-arm"; exit 1; }
    list=$(git -C "$REPO" rev-list --reverse "$old..$new" 2>/dev/null) \
      || { echo "listener: cannot list $br from $old; re-seed and re-arm"; exit 1; }
    for c in $list; do
      files=$(git -C "$REPO" diff-tree --no-commit-id --name-only -r "$c" | grep -i -E "$FPAT" | tr '\n' ' ')
      n=$(git -C "$REPO" show --format= --unified=0 "$c" -- '*.md' | grep -E '^\+[^+]' | grep -c -i -E "$TPAT")
      if [ -n "$files" ] || [ "$n" -gt 0 ]; then
        hits="${hits}${br} $(git -C "$REPO" log -1 --format='%h %ad' --date=format-local:'%m-%d %H:%M' "$c"): $(git -C "$REPO" log -1 --format=%s "$c" | cut -c1-140) | files: ${files:-none} | lines naming this seat: $n"$'\n'
      fi
    done
    next[$f]=$new
  done
  if [ -n "$hits" ]; then printf '%s' "$hits"; fi
  for f in "${!next[@]}"; do echo "${next[$f]}" > "$f"; done
  if [ -n "$hits" ]; then exit 0; fi
  if [ $(( $(date +%s) - T0 )) -ge "$MAX" ]; then
    echo "listener: no news for this seat in $MAX s ($fails failed fetches); re-arm"; exit 0
  fi
  sleep "$INT"
done
