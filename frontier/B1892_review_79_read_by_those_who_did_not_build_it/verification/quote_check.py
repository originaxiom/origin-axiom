#!/usr/bin/env python3
"""Review 79 -- every quotation of the readers' files, looked for in the file it names at the commit of main the reader read.

Each reader's file is taken from its branch at the commit named below.  A quotation is the exact text a finding rests on; it is
looked for, with runs of white space joined, in the files of the arc the finding is under and in the pages it names.  A finding
whose quotation is not there is set aside.  The control: the first quotation of the first reader, altered by one character, must
be reported missing.

The agy family's two files are read by this script and printed by it nowhere: main reads that lane through its mask.

    python3 quote_check.py            # prints the counts and whether the committed result agrees
    python3 quote_check.py --write

Where a reader's commit is not in the clone, that reader's count is reported as not checked here, and the committed result stands
for it.

[CHANGED 2026-11-12 (Review 80; found by a reading on another family of model, which planted five cases against this script and
its lock, all five passing).  The rule above is WIDE: a quotation counts as found when it stands in any file of the finding's
arc or in one of eighteen wide pages, so a quotation set under the wrong file passed.  The wide count is kept, since the
committed result was made by it, and beside it each quotation is now placed STRICTLY: in the file its finding names; or, where
the reader's file names no file, in the arc's own folder; or on a wide page only.  An empty quotation is no longer found.  The
rows of a reader's table that this script does not read are counted: a row with more cells than its table's header (a pipe
inside a cell), and a line that begins as a row and gives fewer than four cells.]
"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
READERS = {   # reader: (the commit of its branch, its file, the commits of main it read)
    "the SM seat": ("4d0a46b93", "relays/REVIEW_79_SM.md", ("323f92327", "0dda7b472")),
    "the web seat": ("0455e766c", "relays/REVIEW_79_CHAT1.md", ("323f92327", "0dda7b472")),
    "agy-002": ("7af2a8670", "relays/REVIEW_79_AGY-002.md", ("0dda7b472",)),
    "agy-exp": ("18634218e", "relays/REVIEW_79_AGY-EXP.md", ("0dda7b472",)),
}
WIDE = ("GENESIS.md", "ROADMAP.md", "WORKING_RULES.md", "GOVERNANCE.md", "CLAIMS.md", "README.md", "docs/POINT_REGISTER.md", "docs/HARVEST_LEDGER.md",
        "docs/THEOREM_REGISTRY.md", "docs/LAW_MAP.md", "docs/seats/README.md", "frontier/B1858_the_closure_map/NODES.json",
        "scripts/gates/gates.py", "scripts/checks/point_debt.py", "scripts/checks/harvest_debt.py", "scripts/checks/relay_debt.py", "scripts/checks/commit_day.py", "scripts/seats/listen.py")


def git(*a):
    r = subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True)
    return r.returncode, r.stdout


_text = {}


def text(commit, path):
    if (commit, path) not in _text:
        _text[(commit, path)] = " ".join(git("show", "%s:%s" % (commit, path))[1].split())
    return _text[(commit, path)]


def quotations(reader, page):
    """(the arc or 'window', a file the finding names or None, the quotation) for every finding of the page"""
    out = []
    if reader == "the SM seat":
        heads = [(m.start(), m.group(1)) for m in re.finditer(r"^## (B\d+|M4)", page, re.M)]
        for m in re.finditer(r"^\*\*(R79-SM-\d+)\*\*", page, re.M):
            nxt = re.search(r"^\*\*R79-SM-\d+\*\*|^## |^\*\*Could not check|^\*\*Read and found sound|^\*\*Seen outside", page[m.end():], re.M)
            block = page[m.start(): m.end() + (nxt.start() if nxt else len(page))]
            arc = [a for p, a in heads if p < m.start()][-1]
            for q in re.findall(r"^\s*- `([^`]+)`", block, re.M):
                out.append((arc if arc != "M4" else "window", None, q))
    elif reader == "agy-exp":             # a block for each finding: the arc, the file, and the quotation in a fenced block
        for b in re.split(r"^### Finding ", page, flags=re.M)[1:]:
            arc = re.search(r"- \*\*Arc:\*\* `([^`]+)`", b); fil = re.search(r"- \*\*File:\*\* (\S+)", b); quo = re.search(r"```text\n(.*?)\n```", b, re.S)
            if arc and fil and quo:
                out.append((arc.group(1), fil.group(1).strip("`"), quo.group(1)))
    else:
        for line in page.split("\n"):
            c = [x.strip() for x in line.strip().strip("|").split(" | ")]
            if len(c) >= 4 and (re.fullmatch(r"B\d+", c[0]) or c[0] in ("window", "(the governing pages)")):
                out.append((c[0] if c[0].startswith("B") else "window", c[1].strip("`"), c[2].strip().strip('"').strip("`")))
    return out


def found(q, arc, named, commits):
    q = " ".join(q.split())
    if not q:
        return False                                  # an empty quotation is in every file; it is a quotation of nothing
    for commit in commits:
        rc, ls = git("ls-tree", "-r", "--name-only", commit)
        files = ls.split("\n")
        pool = ([named] if named in files else []) + [f for f in files if arc != "window" and f.startswith("frontier/%s_" % arc)] + [f for f in WIDE if f in files]
        if named and named not in files:
            pool += [f for f in files if f.endswith(named.split("/")[-1])]
        if any(q in text(commit, f) for f in pool):
            return True
    return False


def placed(q, arc, named, commits):
    """where the quotation stands, strictly: 'named' (in the file the finding names, or one of that name where the path is not at
    the commit), 'arc' (the reader names no file: in the arc's own folder), 'wide' (on a wide page only), or None"""
    q = " ".join(q.split())
    if not q:
        return None
    wide = False
    for commit in commits:
        files = git("ls-tree", "-r", "--name-only", commit)[1].split("\n")
        if named:
            cand = [named] if named in files else [f for f in files if f.endswith(named.split("/")[-1])]
            if any(q in text(commit, f) for f in cand):
                return "named"
        elif arc != "window" and any(q in text(commit, f) for f in files if f.startswith("frontier/%s_" % arc)):
            return "arc"
        wide = wide or any(q in text(commit, f) for f in WIDE if f in files)
    return "wide" if wide else None


def rows_not_read(reader, page):
    """the lines of a reader's table that quotations() does not read as it should: (more cells than the header, fewer than four)"""
    if reader in ("the SM seat", "agy-exp"):
        return (0, 0)                                 # their files are not tables
    more = few = 0; ncol = None; lines = page.split("\n")
    for i, line in enumerate(lines):
        if not line.startswith("|"):
            ncol = None; continue
        c = [x.strip() for x in line.strip().strip("|").split(" | ")]
        if i + 1 < len(lines) and set(lines[i + 1].strip()) <= set("|-: ") and lines[i + 1].strip():
            ncol = len(c); continue
        if set(line.strip()) <= set("|-: "):
            continue
        if re.match(r"\|\s*(B\d+|window)\s*\|", line):
            if len(c) < 4:
                few += 1
            elif ncol is not None and len(c) > ncol:
                more += 1
    return (more, few)


def build():
    res = {}
    for reader, (commit, path, read) in READERS.items():
        rc, page = git("show", "%s:%s" % (commit, path))
        if rc != 0:
            res[reader] = None
            continue
        qs = quotations(reader, page)
        hits = [found(q, arc, named, read) for arc, named, q in qs]
        res[reader] = {"its commit": commit, "quotations": len(qs), "found": sum(hits)}
        where = [placed(q, arc, named, read) for arc, named, q in qs]
        more, few = rows_not_read(reader, page)
        res[reader].update({"in the file the finding names": where.count("named"), "in the arc's own folder, no file being named": where.count("arc"),
                            "on a wide page only": where.count("wide"), "placed nowhere": where.count(None),
                            "rows with more cells than their table's header": more, "lines that begin as a row and give fewer than four cells": few})
        if reader == "the SM seat" and qs:
            arc, named, q = qs[0]
            res[reader]["control: the first quotation altered by one character is reported missing"] = not found(q[:-1] + ("x" if q[-1] != "x" else "y"), arc, named, read)
    return res


if __name__ == "__main__":
    R = build()
    f = HERE / "quote_check.json"
    old = json.loads(f.read_text(encoding="utf-8")) if f.is_file() else {}
    for reader, r in R.items():
        print("%-14s %s" % (reader, "not checked here: its commit is not in this clone" if r is None else json.dumps(r, ensure_ascii=False)))
    if "--write" in sys.argv:
        f.write_text(json.dumps({k: v for k, v in R.items() if v is not None}, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        print("the committed result agrees where it was checked: %s" % all(old.get(k) == v for k, v in R.items() if v is not None))
