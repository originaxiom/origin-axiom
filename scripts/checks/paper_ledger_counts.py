#!/usr/bin/env python3
"""The paper's prose counts of ledger rows must equal the table's actual rows.

Twice now a summary has described a pre-revision table: first "three discrete label rows" against
four, then "four non-continuous rows" against six after two rows were added to fix an earlier
finding. Both were caught by an external referee, and the second was introduced BY the first fix.
A count written by hand beside a table that changes is a defect waiting to happen, so this derives
it from the table instead.

    python3 scripts/checks/paper_ledger_counts.py            # report
    python3 scripts/checks/paper_ledger_counts.py --selftest # bite control
"""
import io
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
PAPER = ROOT / "papers" / "P3_THE_PAPER" / "main.tex"
WORDS = {2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight"}


def counts(text=None):
    s = text if text is not None else io.open(PAPER, encoding="utf-8").read()
    starts = [m.start() for m in re.finditer(r"\\begin\{longtable\}", s)]
    tab = s[starts[-1]:s.index("\\end{longtable}", starts[-1])]
    types = re.findall(r"&\s*((?:continuous|one |finite|\$\\leq 3\$ continuous|dimensionful)[^&]{0,40}?)\s*&", tab)
    # "dimensionful unit" is the ell row: EXTERNAL BY DESIGN, not a non-continuous ledger row (B1237: the
    # first draft of this tool counted it and reported 7 vs the prose's six -- the tool was wrong, not the paper).
    non_cont = [t.strip() for t in types if "continuous" not in t and "dimensionful" not in t]
    return len(types), len(non_cont)


def prose(text=None):
    s = text if text is not None else io.open(PAPER, encoding="utf-8").read()
    a = re.search(r"and (\w+) non-continuous rows", s)
    b = re.search(r"carries (\w+) discrete inputs that are externally supplied", s)
    return (a.group(1) if a else None), (b.group(1) if b else None)


if __name__ == "__main__":
    total, nc = counts()
    said_nc, said_ext = prose()
    ok_nc = said_nc == WORDS.get(nc)
    ok_ext = said_ext == WORDS.get(nc - 1)      # all but the one relational row
    print(f"table rows: {total}   non-continuous: {nc}")
    print(f"abstract says non-continuous = {said_nc!r}  (table: {WORDS.get(nc)!r})  {'OK' if ok_nc else 'MISMATCH'}")
    print(f"section 8 says externally supplied = {said_ext!r}  (table: {WORDS.get(nc-1)!r})  {'OK' if ok_ext else 'MISMATCH'}")
    if "--selftest" in sys.argv:
        s = io.open(PAPER, encoding="utf-8").read()
        broken = s.replace("and six non-continuous rows", "and four non-continuous rows", 1)
        bad_nc, _ = prose(broken)
        fired = bad_nc != WORDS.get(nc)
        print(f"\nPLANT (abstract says four, table says {WORDS.get(nc)}): reported = {fired}")
        print("CONTROLS", "PASS" if fired else "FAIL")
        sys.exit(0 if fired and ok_nc and ok_ext else 1)
    sys.exit(0 if (ok_nc and ok_ext) else 1)
