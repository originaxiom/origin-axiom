#!/usr/bin/env python3
"""B1886 -- the status cells of the foundation at versions 1.64 and 1.65, read from the two commits and written to a file.

Added 2026-11-12 (Review 79).  The arc's lock compared the two versions by asking git for the older one, and SKIPPED where the
commit was not to be had (a shallow clone, an export): the test of the arc's central claim could then not fail.  And it read only
the 29 rows that open with one of the foundation's identifiers, where the findings said it compared "them all".  This script reads
BOTH kinds of row at BOTH commits -- the rows that open with an identifier, and every row of every table that has a column headed
Status -- and writes them, with each file's git blob id, to status_cells.json.  The lock compares the two snapshots in that file
wherever it runs, and checks the file against git wherever git has the commits.

    python3 build_status_cells.py            # prints what it would write and whether the committed file agrees
    python3 build_status_cells.py --write
"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
VERSIONS = {"v1.64": "8f0b03814", "v1.65": "9ace774f4"}
# (2026-11-12, Review 79: the GAP alternative below matches no row; the foundation's GAPs are bullets, not table rows.  Kept, so that
#  the pattern is the one the arc was landed with; the rows it reads are the PF, GM, SE, T-ROOT and FK rows.)
IDENT = re.compile(r"^\| ((?:PF\d|GM\d[a-d]?|SE\d|T-ROOT|FK\d+|GAP\d))\b[^|]*\|")


def identifier_rows(text):
    """the status cell of every table row that opens with one of the foundation's identifiers (the lock's first reading)"""
    out = {}
    for line in text.split("\n"):
        m = IDENT.match(line)
        if not m:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        ident = m.group(1)
        out.setdefault(ident, cells[3] if ident.startswith("PF") else cells[2])
    return out


def status_table_rows(text):
    """the status cell of every row of every table that has a column headed Status, keyed by the table's header and the row's first cell"""
    out, header, idx = {}, None, None
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if not line.lstrip().startswith("|"):
            header = None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        rule = set(line.replace("|", "").replace(" ", "")) <= set("-:")
        if header is None:
            low = [c.lower() for c in cells]
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if "status" in low and nxt.lstrip().startswith("|") and set(nxt.replace("|", "").replace(" ", "")) <= set("-:"):
                header, idx = " | ".join(cells), low.index("status")
            continue
        if rule or idx >= len(cells):
            continue
        out[header + " :: " + cells[0]] = cells[idx]
    return out


def snapshot(commit):
    def git(*a):
        r = subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True)
        return r.returncode, r.stdout
    rc, text = git("show", commit + ":GENESIS.md")
    if rc != 0:
        return None
    rc, blob = git("rev-parse", commit + ":GENESIS.md")
    return dict(commit=commit, blob=blob.strip(), identifier_rows=identifier_rows(text), status_table_rows=status_table_rows(text))


def build():
    out = {}
    for v, c in VERSIONS.items():
        s = snapshot(c)
        if s is None:
            return None
        out[v] = s
    return out


if __name__ == "__main__":
    B = build()
    if B is None:
        print("this checkout does not hold both commits; the committed file cannot be rebuilt here")
        sys.exit(2)
    text = json.dumps(B, indent=1, ensure_ascii=False, sort_keys=True) + "\n"
    f = HERE / "status_cells.json"
    if "--write" in sys.argv:
        f.write_text(text, encoding="utf-8")
    for v, s in B.items():
        print("%s @ %s: %d rows that open with an identifier, %d rows of tables with a Status column" % (v, s["commit"], len(s["identifier_rows"]), len(s["status_table_rows"])))
    print("the committed file agrees with git: %s" % (f.is_file() and f.read_text(encoding="utf-8") == text))
