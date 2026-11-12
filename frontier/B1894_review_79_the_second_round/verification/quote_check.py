#!/usr/bin/env python3
"""Review 79, the second round -- every quotation of the four readers' second files, looked for in the file it names at the commit
of main the reader read (896cae025).

The readers' files are taken from their branches at the commits named below.  A quotation is looked for with runs of white space
joined, in the file the finding names, in the arc's folder, and in a short list of pages.  The control: the first quotation of the
first reader, altered by one character, must be reported missing.  The agy family's two files are read by this script and printed
by it nowhere: main reads that lane through its mask.

    python3 quote_check.py            # prints the counts and whether the committed result agrees
    python3 quote_check.py --write
"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
MAIN = ("896cae025",)
READERS = {   # reader: (the commit of its branch, its file)
    "the SM seat": ("52b484c70", "relays/REVIEW_79B_SM.md"),
    "the web seat": ("1588ed722", "relays/REVIEW_79B_CHAT1.md"),
    "agy-002": ("c68aabbd7", "relays/REVIEW_79B_AGY-002.md"),
    "agy-exp": ("0e9644320", "relays/REVIEW_79B_AGY-EXP.md"),
}
WIDE = ("GENESIS.md", "docs/LAW_MAP.md", "docs/THEOREM_REGISTRY.md", "docs/POINT_REGISTER.md", "scripts/seats/listen.py", "scripts/gates/gates.py",
        "frontier/B1861_the_closure_programme/PROGRAMME.md", "frontier/B1892_review_79_read_by_those_who_did_not_build_it/ANSWERS.md",
        "frontier/B1891_the_foundation_at_version_1_66/FINDINGS.md", "frontier/B1862_the_audits_first_corrections/verification/test_b1862_the_audits_first_corrections.py")


def git(*a):
    r = subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True)
    return r.returncode, r.stdout


_text, _files = {}, {}


def text(commit, path):
    if (commit, path) not in _text:
        _text[(commit, path)] = " ".join(git("show", "%s:%s" % (commit, path))[1].split())
    return _text[(commit, path)]


def files(commit):
    if commit not in _files:
        _files[commit] = git("ls-tree", "-r", "--name-only", commit)[1].split("\n")
    return _files[commit]


def quotations(reader, page):
    """(the arc, a file the finding names or None, the quotation) for every finding of the page"""
    out = []
    if reader == "the SM seat":
        for m in re.finditer(r"^\*\*(R79b-SM-\d+)\*\*", page, re.M):
            nxt = re.search(r"^\*\*R79b-SM-\d+\*\*|^## ", page[m.end():], re.M)
            block = page[m.start(): m.end() + (nxt.start() if nxt else len(page))]
            for q in re.findall(r"^\s*- `([^`]+)`", block, re.M):
                out.append((None, None, q))
    elif reader == "agy-exp":
        for b in re.split(r"^### Finding ", page, flags=re.M)[1:]:
            arc = re.search(r"- \*\*Arc:\*\* `([^`]+)`", b); fil = re.search(r"- \*\*File:\*\* (\S+)", b); quo = re.search(r"```text\n(.*?)\n```", b, re.S)
            if arc and fil and quo:
                out.append((arc.group(1), fil.group(1).strip("`"), quo.group(1)))
    else:
        for line in page.split("\n"):
            c = [x.strip() for x in line.strip().strip("|").split(" | ")]
            if len(c) >= 4 and (re.fullmatch(r"B\d+", c[0]) or c[0] == "window"):
                out.append((c[0] if c[0].startswith("B") else None, c[1].strip("`"), c[2]))
    return out


def found(q, arc, named):
    forms = {" ".join(q.split()), " ".join(q.strip().strip('"').strip("`").split()), " ".join(q.strip().strip("`").split())}
    for commit in MAIN:
        fs = files(commit)
        pool = ([named] if named in fs else []) + ([f for f in fs if f.startswith("frontier/%s_" % arc)] if arc else []) + [f for f in WIDE if f in fs]
        if named and named not in fs:
            pool += [f for f in fs if f.endswith(named.split("/")[-1])]
        if not arc and not named:
            pool += [f for f in fs if f.startswith(("frontier/B18", "frontier/B862_", "docs/")) and f.endswith((".md", ".json", ".py", ".txt"))]
        if any(form and form in text(commit, f) for form in forms for f in pool):
            return True
    return False


def build():
    res = {}
    for reader, (commit, path) in READERS.items():
        rc, page = git("show", "%s:%s" % (commit, path))
        if rc != 0:
            res[reader] = None
            continue
        qs = quotations(reader, page)
        hits = [found(q, arc, named) for arc, named, q in qs]
        res[reader] = {"its commit": commit, "quotations": len(qs), "found": sum(hits)}
        if reader == "the SM seat":
            # one of its entries corrects its own first file and quotes that file: those quotations are looked for there
            own = " ".join(git("show", "4d0a46b93:relays/REVIEW_79_SM.md")[1].split())
            mine = [" ".join(qq.split()) in own for (a_, n_, qq), h in zip(qs, hits) if not h]
            res[reader]["of its own first file, found there"] = sum(mine)
            res[reader]["found nowhere"] = len(mine) - sum(mine)
        if reader == "the SM seat" and qs:
            arc, named, q = qs[0]
            res[reader]["control: the first quotation altered by one character is reported missing"] = not found(q[:-1] + ("x" if q[-1] != "x" else "y"), arc, named)
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
