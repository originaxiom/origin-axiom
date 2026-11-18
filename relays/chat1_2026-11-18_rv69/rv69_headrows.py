#!/usr/bin/env python3
"""Status section 28 (main's M69): this seat's harvest-ledger rows before 2026-11-15 whose disposition does not say
they were read in full. Data-free. Post hoc and not sealed: computed once.

    python3 -I -u rv69_headrows.py <a checkout of main at 996638890> <the mask script>

It reads main's harvest ledger only through the mask (the mask script is run as a subprocess). It selects this seat's
rows by main's instrument's rule, as rv45_counts.py does, and keeps those whose last date is before 2026-11-15. Section
7.3's count matched upper-case phrases only. This one matches without regard to case, in the disposition's first 240
characters, any of: "headline", "at its head", "its head read", "first two sections read", "not yet", "queued",
"pending", "unread", and RECEIVED without "read in full". For each row it prints the ledger's line number, the last
date, the delivery's first 150 characters and the disposition's first 200, as the mask shows them. Which of these were
read in full later, or are in the register, is checked by hand at source in the section itself.
"""
import re
import subprocess
import sys

MAIN, MASK = sys.argv[1], sys.argv[2]
out = subprocess.run([sys.executable, "-I", MASK, "docs/HARVEST_LEDGER.md"], cwd=MAIN, capture_output=True, text=True).stdout
PAT = re.compile(r"headline|at its head|its head read|first two sections read|not yet|queued|pending|unread", re.I)
hits = []
n_rows = n_before = 0
for line in out.splitlines():
    body = line[7:]
    if not body.startswith("|"):
        continue
    cells = [c.strip() for c in body.strip().strip("|").split("|")]
    if len(cells) < 6 or not re.fullmatch(r"[\d#]+", cells[0]):
        continue
    seat = cells[1].lower()
    if not ("web seat" in seat or "chat1" in seat or "chat#" in seat):
        continue
    n_rows += 1
    dates = re.findall(r"20\d\d-\d\d-\d\d", cells[-1])
    last = dates[-1] if dates else ""
    if not last or last >= "2026-11-15":
        continue
    n_before += 1
    d = cells[5].lstrip("*").strip()
    head = d[:240]
    rec_not_full = d.startswith("RECEIVED") and "read in full" not in d[:60].lower()
    if PAT.search(head) or rec_not_full:
        hits.append((line[:6].strip(), last, cells[2][:150], d[:200]))
print("rows of this seat: %d; dated before 2026-11-15: %d; matching: %d" % (n_rows, n_before, len(hits)))
for ln, dt, what, disp in hits:
    print("%s | %s | %s || %s" % (ln, dt, what, disp))
