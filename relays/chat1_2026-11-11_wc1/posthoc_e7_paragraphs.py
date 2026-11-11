#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
W-C1, POST HOC, after the referee's read of the delivery note.  The web seat (chat1), 2026-11-11.  A read-out; it
seals no expectation.  The seat's sweep for E7 read line by line, so a statement split over a line break could not be
seen.  This reads by paragraph, over exactly the pages E7's lock reads (the .md files under docs/, frontier/ and
papers/, and five pages at the root), skipping the pages the lock lists as history and the pages that carry the
correction, and prints the paths and line ranges where a paragraph states the zero.  Paths and numbers only.

Usage: posthoc_e7_paragraphs.py <path to the seat's checkout of main>
"""
import pathlib
import re
import sys

OLD = re.compile(r"0\.000 bits|0 bits of designer|zero (?:retroactive )?designer freedom|no designer freedom|designer freedom\s*=\s*0|zero retroactive|0\.000 retroactive", re.I)
ABOUT = re.compile(r"designer|freedom ledger|B1028", re.I)
MARK = "the freedom ledger's zero is not a computed quantity"
HISTORY = ("PROGRESS_LOG.md", "CHANGELOG.md", "docs/CAMPAIGN_STATUS.md", "docs/progress/", "docs/handoffs/", "docs/views/", "docs/THE_WHY_CAMPAIGN.md", "docs/CROSSING_REQUIREMENTS.md",
           "docs/FIELD_EXPLORATION_REPORT.md", "docs/GRAND_COMPUTATION_v0.md", "docs/THE_FINAL_ACTS_BAR_2026-10-29.md", "frontier/B1015_", "frontier/B1128_", "frontier/B1349_",
           "frontier/B1861_", "frontier/B1870_", "frontier/B1028_freedom_ledger/ADDENDUM", "frontier/B1028_freedom_ledger/PREREGISTRATION")
LOCK = re.compile(r"0\.000 bits|0\.000 BITS|zero (?:retroactive )?designer freedom", re.I)


def pages(root):
    for top in ("docs", "frontier", "papers"):
        for p in (root / top).rglob("*.md"):
            yield p.relative_to(root).as_posix(), p
    for rel in ("ROADMAP.md", "README.md", "GENESIS.md", "CLAIMS.md", "GOVERNANCE.md"):
        yield rel, root / rel


def main():
    root = pathlib.Path(sys.argv[1]).resolve()
    hits = []
    for rel, p in pages(root):
        if any(rel.startswith(h) or h in rel for h in HISTORY):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except Exception:
            continue
        if MARK.lower() in text.lower():
            continue
        line = 1
        for para in re.split(r"(\n\s*\n)", text):
            n = para.count("\n")
            joined = " ".join(para.split())
            if para.strip() and OLD.search(joined) and ABOUT.search(joined):
                one_line = any(OLD.search(l) and ABOUT.search(l) for l in para.splitlines())
                lock_line = any(LOCK.search(l) and re.search(r"designer|freedom ledger|B1028", l) for l in para.splitlines())
                hits.append((rel, line, line + n, one_line, lock_line))
            line += n
    print("pages E7's lock reads, outside its history and without the correction, with a paragraph that states the zero: %d"
          % len({h[0] for h in hits}))
    for rel, a, b, one, lock in hits:
        print("    %-55s lines %d-%d   on one line: %-5s   the lock's own test would see it: %s" % (rel, a, b, one, lock))
    return 0


if __name__ == "__main__":
    sys.exit(main())
