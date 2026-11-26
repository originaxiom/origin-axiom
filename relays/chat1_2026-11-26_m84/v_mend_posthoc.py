#!/usr/bin/env python3
"""V-MEND post hoc (chat1, 2026-11-26; labelled post hoc: written after V-MEND's output was read, to word A84 § 1).
On each line where this seat's rerun of the corrected listen4.py and main's committed output differ: do the printed
top lists agree position by position in modulus (so every difference is among eigenvalues of equal modulus), and do
they hold the same multiset of values (a pure reorder) or a different one (the five printed are a different choice
among equal moduli)?

    python3 -B v_mend_posthoc.py <checkout of main at 6f80ac0e5>
"""
import sys, re, pathlib, subprocess
from collections import Counter

main_dir = pathlib.Path(sys.argv[1]).resolve()
head = subprocess.run(["git", "-C", str(main_dir), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
if not head.startswith("6f80ac0e5"):
    sys.exit("refused: checkout at %s" % head[:9])
card = next((main_dir / "frontier").glob("B1986_*")) / "verification"
ORB = re.compile(r"orbit of\s+(\d+): W\+ top (.*?) \| W\+- top (.*?) \| non-constant W\+ modes with \|eigenvalue\| = 2: (.*)$")

def parse(s):
    out = []
    for t in s.split(", "):
        m = re.fullmatch(r"(-?[\d.]+)([+-][\d.]+)i", t)
        out.append(complex(float(m.group(1)), float(m.group(2))) if m else complex(float(t), 0))
    return out

rerun = subprocess.run([sys.executable, "-B", "listen4.py"], cwd=card, capture_output=True, text=True).stdout.splitlines()
new = (card / "listen4_run.txt").read_text().splitlines()
tally = Counter()
for i, (a, b) in enumerate(zip(rerun, new)):
    if a == b:
        continue
    ma, mb = ORB.search(a), ORB.search(b)
    for k, name in ((2, "W+ top"), (3, "W+- top")):
        x, y = parse(ma.group(k)), parse(mb.group(k))
        if x == y:
            continue
        mod_ok = len(x) == len(y) and all(abs(abs(u) - abs(v)) < 1e-4 for u, v in zip(x, y))
        same = Counter(x) == Counter(y)
        tally[(name, "moduli agree" if mod_ok else "MODULI DIFFER", "same values reordered" if same else "different choice")] += 1
for k, v in sorted(tally.items()):
    print("%-8s %-14s %-22s %d lines" % (k + (v,)))
