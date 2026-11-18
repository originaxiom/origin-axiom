#!/usr/bin/env python3
"""Status section 28 (main's M69), the second count: this seat's harvest-ledger rows before 2026-11-15 whose disposition
says they were read or verified only in part. Data-free. Post hoc and not sealed: computed once. A search in scratch
space with the same words came first, after rv69_headrows.py had run; this script makes it reproducible.

    python3 -I -u rv69_partrows.py <a checkout of main at 996638890> <the mask script>

It selects rows as rv69_headrows.py does and keeps those whose disposition's first 240 characters match, without
regard to case, any of: "in part", "partly", "partial", "skim", "scope only", "at its scope", "not read",
"summary only", "abstract". For each row it prints the ledger's line number, the last date, the delivery's first 150
characters and the disposition's first 200, as the mask shows them.
"""
import re
import subprocess
import sys

MAIN, MASK = sys.argv[1], sys.argv[2]
out = subprocess.run([sys.executable, "-I", MASK, "docs/HARVEST_LEDGER.md"], cwd=MAIN, capture_output=True, text=True).stdout
PAT = re.compile(r"in part|partly|partial|skim|scope only|at its scope|not read|summary only|abstract", re.I)
hits = []
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
    dates = re.findall(r"20\d\d-\d\d-\d\d", cells[-1])
    last = dates[-1] if dates else ""
    if not last or last >= "2026-11-15":
        continue
    d = cells[5].lstrip("*").strip()
    if PAT.search(d[:240]):
        hits.append((line[:6].strip(), last, cells[2][:150], d[:200]))
print("matching: %d" % len(hits))
for ln, dt, what, disp in hits:
    print("%s | %s | %s || %s" % (ln, dt, what, disp))
