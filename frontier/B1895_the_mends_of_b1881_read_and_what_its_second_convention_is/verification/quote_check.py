#!/usr/bin/env python3
"""B1895 -- the four quotations of the reading of B1881's mends, looked for in the file each names at the commit of main that was
read (87bfa1f05).

The reader's file is taken from its branch at the commit named below.  A quotation is looked for with runs of white space joined,
in the file the finding names.  The control: the first quotation altered by one character must be reported missing.  The file is
of the agy family: it is read by this script and printed by it nowhere, since main reads that lane through its mask.

    python3 quote_check.py            # prints the counts and whether the committed result agrees
    python3 quote_check.py --write
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
MAIN = "87bfa1f05"
READER = ("c67f84c11", "relays/REVIEW_79B_AGY-002.md")
ARC = "B1881"


def git(*a):
    r = subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True)
    return r.returncode, r.stdout


def quotations(page):
    """(the file the finding names, the quotation) for every row of the page's table whose arc is B1881"""
    out = []
    for line in page.split("\n"):
        c = [x.strip() for x in line.strip().strip("|").split(" | ")]
        if len(c) >= 4 and c[0] == ARC:
            out.append((c[1].strip("`"), c[2]))
    return out


def found(q, named):
    rc, body = git("show", "%s:%s" % (MAIN, named))
    if rc != 0:
        return False
    body = " ".join(body.split())
    forms = {" ".join(q.split()), " ".join(q.strip().strip('"').strip("`").split()), " ".join(q.strip().strip("`").split())}
    return any(f and f in body for f in forms)


def build():
    rc, page = git("show", "%s:%s" % READER)
    if rc != 0:
        return None
    qs = quotations(page)
    res = {"the reader's commit": READER[0], "the commit of main read": MAIN, "quotations": len(qs), "found": sum(found(q, named) for named, q in qs),
           "files named": sorted({named.split("/")[-1] for named, q in qs})}
    if qs:
        named, q = qs[0]
        res["control: the first quotation altered by one character is reported missing"] = not found(q[:-1] + ("x" if q[-1] != "x" else "y"), named)
    return res


if __name__ == "__main__":
    R = build()
    f = HERE / "quote_check.json"
    if R is None:
        print("not checked here: the reader's commit is not in this clone")
        raise SystemExit(0)
    print(json.dumps(R, ensure_ascii=False))
    if "--write" in sys.argv:
        f.write_text(json.dumps(R, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        old = json.loads(f.read_text(encoding="utf-8")) if f.is_file() else {}
        print("the committed result agrees: %s" % (old == R))
