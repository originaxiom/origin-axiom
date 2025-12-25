#!/usr/bin/env bash

ZSHRC="$HOME/.zshrc"

add_alias() {
  grep -q "$1" "$ZSHRC" || echo "$1" >> "$ZSHRC"
}

echo "▶ Installing Origin Axiom aliases"

add_alias "alias oa='cd ~/Documents/Projects/origin-axiom'"
add_alias "alias oat='cd ~/Documents/Projects/origin-axiom-theta-star'"
add_alias "alias venv='source .venv/bin/activate'"

echo "✅ Aliases installed (restart shell)"