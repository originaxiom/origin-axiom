#!/usr/bin/env python3
"""The seats' intake (from 2026-11-24, at the author's word; docs/CLAIM_CARD.md).

For every seat branch named in docs/HARVEST_LEDGER.md's Pins table: the commits and changed files since its pin, and
every claim card (a file under relays/claims/ whose first line starts '# CLAIM CARD') added since the pin, sorted into
tiers by its 'touches' and 'effect' fields:
  A  effect removes, conditions or refutes, and it touches a scoreboard code (A01-A12, F1-F4, S01-S03, LAMBDA),
     an identification (I-n) or names one of the 19;
  B  effect supports or adds, on such a code;
  C  anything else.
Run `git fetch --all` first.  Prints one table; writes nothing.
    python3 scripts/checks/seat_intake.py [--seat KEY]"""
import re, subprocess, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
CODE = re.compile(r"\b(A0[1-9]|A1[0-2]|F[1-4]|S0[1-3]|LAMBDA|I-\d+)\b")
NINETEEN = re.compile(r"\b(mass|mixing|CKM|PMNS|theta|coupling|Higgs|weak angle|Yukawa|lepton factor)\b", re.I)


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True).stdout


def pins():
    t = (ROOT / "docs" / "HARVEST_LEDGER.md").read_text(encoding="utf-8")
    sec = re.search(r"^## Pins.*?(?=^## |\Z)", t, re.M | re.S)
    out = []
    for line in (sec.group(0).splitlines() if sec else []):
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) >= 3 and re.fullmatch(r"[a-z0-9]+", c[0]) and re.fullmatch(r"`?[0-9a-f]{7,40}`?", c[2]):
            b = re.search(r"origin/[^`\s)]+", c[1])
            if b: out.append((c[0], b.group(0), c[2].strip("`")))
    return out


def field(text, name):
    m = re.search(r"^- %s:\s*(.*)$" % re.escape(name), text, re.M | re.I)
    return m.group(1).strip() if m else ""


def tier(touches, effect):
    coded = bool(CODE.search(touches)) or bool(NINETEEN.search(touches))
    e = effect.lower()
    if coded and re.search(r"\b(removes|conditions|refutes)\b", e): return "A"
    if coded and re.search(r"\b(supports|adds)\b", e): return "B"
    return "C"


def main(argv):
    only = argv[argv.index("--seat") + 1] if "--seat" in argv else None
    rows, cards = [], []
    for key, branch, pin in pins():
        if only and key != only: continue
        if not git("rev-parse", "--verify", "-q", branch).strip(): continue
        base = git("merge-base", pin, branch).strip() or pin
        n = git("rev-list", "--count", "%s..%s" % (base, branch)).strip() or "0"
        if n == "0": continue
        changed = [p for p in git("diff", "--name-only", "--no-renames", base, branch).split() if p]
        rows.append((key, branch, n, len(changed)))
        for p in changed:
            if not p.startswith("relays/claims/") or not p.endswith(".md"): continue
            text = git("show", "%s:%s" % (branch, p))
            if not text.startswith("# CLAIM CARD"): continue
            touches, effect = field(text, "touches"), field(text, "effect")
            cards.append((tier(touches, effect), key, p, text.splitlines()[0][len("# CLAIM CARD"):].strip(" —-"), touches, effect,
                          field(text, "second computation"), field(text, "already on main?")))
    print("SEATS WITH NEW WORK SINCE THEIR PINS:")
    for key, branch, n, f in rows: print("  %-14s %-44s %5s commits, %5d files" % (key, branch, n, f))
    print("CLAIM CARDS: %d (A %d, B %d, C %d)" % (len(cards), *(sum(1 for c in cards if c[0] == t) for t in "ABC")))
    for c in sorted(cards):
        print("  [%s] %s %s\n      %s\n      touches: %s | effect: %s\n      second computation: %s | already on main?: %s" % (
            c[0], c[1], c[2], c[3][:150], c[4][:120], c[5][:80], (c[6] or "none")[:80], (c[7] or "not stated")[:80]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
