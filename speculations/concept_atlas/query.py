#!/usr/bin/env python3
"""The Concept Atlas query tool.

Usage:
  python3 query.py list             # all cards + statuses
  python3 query.py card <name>      # print one card (substring match)
  python3 query.py status <WORD>    # all cards whose status line contains WORD
"""
import os
import re
import sys

CARDS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "CARDS.md")


def load():
    text = open(CARDS).read()
    cards = re.split(r"^## ", text, flags=re.M)[1:]
    out = []
    for c in cards:
        name = c.splitlines()[0].strip()
        m = re.search(r"^- status: (.+)$", c, flags=re.M)
        status = m.group(1).strip() if m else "?"
        out.append((name, status, "## " + c.rstrip()))
    return out


def main():
    cards = load()
    if len(sys.argv) < 2 or sys.argv[1] == "list":
        w = max(len(n) for n, _, _ in cards)
        for n, s, _ in cards:
            print(f"  {n:<{w}}  {s}")
        print(f"\n  {len(cards)} cards. (card <name> | status <WORD>)")
    elif sys.argv[1] == "card" and len(sys.argv) > 2:
        key = " ".join(sys.argv[2:]).lower()
        hits = [c for c in cards if key in c[0].lower()]
        for _, _, full in hits:
            print(full + "\n")
        if not hits:
            print(f"no card matching '{key}'")
    elif sys.argv[1] == "status" and len(sys.argv) > 2:
        key = sys.argv[2].upper()
        for n, s, _ in cards:
            if key in s.upper():
                print(f"  {n}  —  {s}")
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
