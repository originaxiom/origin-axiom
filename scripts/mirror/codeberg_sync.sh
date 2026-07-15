#!/bin/zsh
# Permanent GitHub -> Codeberg mirror sync for origin-axiom.
# No-ops gracefully until the codeberg-oa key is registered on Codeberg
# and the repo codeberg.org/originaxiom/origin-axiom exists.
set -u
REPO=/Users/dri/origin-axiom
LOG=$HOME/Library/Logs/codeberg-sync.log
cd "$REPO" || exit 0
echo "[$(date '+%F %T')] sync run" >> "$LOG"
ssh -o BatchMode=yes -o ConnectTimeout=15 -T git@codeberg-oa 2>&1 | grep -qi "authenticated" || {
  echo "  key not yet registered on Codeberg — skipped" >> "$LOG"; exit 0; }
git remote get-url codeberg >/dev/null 2>&1 || \
  git remote add codeberg git@codeberg-oa:originaxiom/origin-axiom.git
git fetch origin --prune >> "$LOG" 2>&1
git push codeberg 'refs/remotes/origin/*:refs/heads/*' --prune >> "$LOG" 2>&1 \
  && git push codeberg --tags >> "$LOG" 2>&1 \
  && echo "  synced OK" >> "$LOG" \
  || echo "  push failed (repo missing on Codeberg? create originaxiom/origin-axiom there)" >> "$LOG"
