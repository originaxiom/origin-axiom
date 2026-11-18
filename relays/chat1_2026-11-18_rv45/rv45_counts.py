#!/usr/bin/env python3
"""The row counts of the status page's section 7.3 (main's M45), after its referee read. Data-free. Post hoc and not
sealed: computed once, in scratch space first.

    python3 -I -u rv45_counts.py <a checkout of main at 7022a9dae> <the mask script>

It reads main's harvest ledger only through the mask (the mask script is run as a subprocess; its output keeps dates
and upper-case disposition words, and hides digits on some lines). It selects this seat's rows by main's instrument's
rule (scripts/checks/harvest_debt.py: the seat cell contains "web seat" or "chat1"; on a masked line "chat1" shows as
"chat#", and no other seat's cell names "chat"), and prints counts only:
  - the rows, and those whose last date is before 2026-11-15;
  - among those, the dispositions that open with RECEIVED, split by whether the opening says "read in full";
    those that open with REGISTERED; those that open with UNREAD or say "the results UNREAD"; and those read only at the
    head ("READ AT HEADLINE", "READ AT ITS HEAD", "FIRST TWO SECTIONS READ", "NOT YET", "ITS HEAD READ").
"""
import re
import subprocess
import sys

MAIN, MASK = sys.argv[1], sys.argv[2]
out = subprocess.run([sys.executable, "-I", MASK, "docs/HARVEST_LEDGER.md"], cwd=MAIN, capture_output=True, text=True).stdout
rows = []
for line in out.splitlines():
    body = line[7:]                       # the mask prefixes a line number and a flag
    if not body.startswith("|"):
        continue
    cells = [c.strip() for c in body.strip().strip("|").split("|")]
    if len(cells) < 6 or not re.fullmatch(r"[\d#]+", cells[0]):
        continue
    seat = cells[1].lower()
    if not ("web seat" in seat or "chat1" in seat or "chat#" in seat):
        continue
    dates = re.findall(r"20\d\d-\d\d-\d\d", cells[-1])
    rows.append((dates[-1] if dates else "", cells[5]))
before = [d for dt, d in rows if dt and dt < "2026-11-15"]
undated = sum(1 for dt, _ in rows if not dt)


def opening(d):
    return d.lstrip("*").strip()


rec_full = sum(1 for d in before if opening(d).startswith("RECEIVED") and "read in full" in opening(d)[:60].lower())
rec_other = sum(1 for d in before if opening(d).startswith("RECEIVED")) - rec_full
reg = sum(1 for d in before if opening(d).startswith("REGISTERED"))
unread = sum(1 for d in before if opening(d).startswith("UNREAD") or "the results UNREAD" in opening(d)[:60])
head = sum(1 for d in before if re.search(r"READ AT HEADLINE|READ AT ITS HEAD|FIRST TWO SECTIONS READ|NOT YET|ITS HEAD READ",
                                          opening(d)[:160]))
print("rows of this seat: %d (undated %d); dated before 2026-11-15: %d" % (len(rows), undated, len(before)))
print("of those: RECEIVED, read in full %d; RECEIVED, other %d; REGISTERED %d; UNREAD %d; read only at the head %d"
      % (rec_full, rec_other, reg, unread, head))
