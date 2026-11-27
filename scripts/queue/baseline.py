#!/usr/bin/env python3
"""The known-failures baseline, which may only shrink (the framework's thin path, patch T10; draft 1 §§ 4 and 9; register
row P-885).

`queue/KNOWN_FAILURES.json` lists every test that fails and every gate that is red on main, as of a full suite run on a
fresh clone. Each entry carries a register row that holds the debt, and a line of why:

    {"note": ..., "tests": [{"id": <pytest node id>, "row": "P-<n>", "why": ...}],
                  "gates": [{"id": <gate name>, "row": "P-<n>", "why": ...}]}

THE RULES (§ 9, the advisor's proposal adopted):
  - every entry names a register row of docs/POINT_REGISTER.md;
  - the list may only shrink: along main's history, no version of the file holds an entry that the version before it did
    not (the gate known-failures reads that history);
  - a landing that adds a failure or a red gate is refused (the landing tool, T11, calls `compare` below): a failure the
    list does not hold is a new failure; an entry that now passes is reported, so that the list is shrunk by it.

The list ships EMPTY. Its first entries are main's: they come from main's own full suite on a fresh clone, each with the
register row main gives it. `--draft` writes the entries a run gives, with their rows left for main to fill.

    python3 scripts/queue/baseline.py --check                       # the list's form and rows; exit 1 when it fails
    python3 scripts/queue/baseline.py --compare FAILURES [--gates RED]   # a run against the list
    python3 scripts/queue/baseline.py --draft FAILURES [--gates RED]     # print a draft list for main to fill
FAILURES is a file of failing test ids, one a line, as `pytest -rfE` prints them after "FAILED " or "ERROR " (the landing
tool, T11, runs the suite with -rfE); RED a file of red gates' names, one a line."""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
LIST = "queue/KNOWN_FAILURES.json"
REGISTER = "docs/POINT_REGISTER.md"
ROW = re.compile(r"P-\d+")
KINDS = ("tests", "gates")


def rows(root=ROOT):
    """the register's row ids"""
    p = pathlib.Path(root, REGISTER)
    return set(re.findall(r"^\| (P-\d+) \|", p.read_text(encoding="utf-8"), re.M)) if p.is_file() else set()


def form_problems(d, known_rows=None):
    if not isinstance(d, dict):
        return ["the list is not a table"]
    bad = []
    extra = sorted(set(d) - {"note", "tests", "gates"})
    if extra:
        bad.append("fields not in the schema: %s" % ", ".join(extra))
    for kind in KINDS:
        entries = d.get(kind)
        if not isinstance(entries, list):
            bad.append("%s is not a list" % kind)
            continue
        seen = set()
        for i, e in enumerate(entries):
            if not isinstance(e, dict) or sorted(e) != ["id", "row", "why"]:
                bad.append("%s entry %d is not {id, row, why}" % (kind, i))
                continue
            if not isinstance(e["id"], str) or not e["id"].strip():
                bad.append("%s entry %d has no id" % (kind, i))
            elif e["id"] in seen:
                bad.append("%s entry %s stands twice" % (kind, e["id"]))
            seen.add(e["id"])
            if not isinstance(e["row"], str) or not ROW.fullmatch(e["row"]):
                bad.append("%s entry %s names no register row" % (kind, e["id"]))
            elif known_rows is not None and e["row"] not in known_rows:
                bad.append("%s entry %s names %s, which is not a row of the register" % (kind, e["id"], e["row"]))
            if not isinstance(e["why"], str) or not e["why"].strip():
                bad.append("%s entry %s says not why" % (kind, e["id"]))
    return bad


def ids(d):
    return {kind: {e["id"] for e in d.get(kind, []) if isinstance(e, dict) and "id" in e} for kind in KINDS}


def shrink_problems(root=ROOT, ref="HEAD", path=LIST):
    """along ref's first-parent history: no version holds an entry the version before it did not"""
    r = subprocess.run(["git", "log", "--first-parent", "--reverse", "--format=%H", ref, "--", path], cwd=root,
                       capture_output=True, text=True)
    if r.returncode != 0:
        return ["the history of %s cannot be read" % path]
    bad, before = [], None
    for c in r.stdout.split():
        s = subprocess.run(["git", "show", "%s:%s" % (c, path)], cwd=root, capture_output=True, text=True)
        if s.returncode != 0:
            continue
        try:
            now = ids(json.loads(s.stdout))
        except ValueError:
            bad.append("%s at %s is not JSON" % (path, c[:9]))
            continue
        if before is not None:
            for kind in KINDS:
                grown = sorted(now[kind] - before[kind])
                if grown:
                    bad.append("%s at %s adds %s: the list may only shrink" % (path, c[:9], ", ".join(grown[:5])))
        before = now
    return bad


def working_problems(d, root=ROOT, path=LIST):
    """the list as read against its last committed version: an entry the commit does not hold is a growth too (main's M65:
    the history alone missed a list grown in the working tree)"""
    s = subprocess.run(["git", "show", "HEAD:%s" % path], cwd=root, capture_output=True, text=True)
    if s.returncode != 0:
        return []                                 # not committed yet: its first version is what lands
    try:
        head = ids(json.loads(s.stdout))
    except ValueError:
        return ["%s at HEAD is not JSON" % path]
    now = ids(d)
    return ["%s adds %s to its last committed version: the list may only shrink" % (path, ", ".join(sorted(now[k] - head[k])[:5]))
            for k in KINDS if now[k] - head[k]]


def compare(d, failures, red_gates):
    """(new failures and red gates the list does not hold, entries that now pass): a landing with any new one is refused"""
    known = ids(d)
    new = ["test %s" % t for t in sorted(set(failures) - known["tests"])] + \
          ["gate %s" % g for g in sorted(set(red_gates) - known["gates"])]
    gone = ["test %s" % t for t in sorted(known["tests"] - set(failures))] + \
           ["gate %s" % g for g in sorted(known["gates"] - set(red_gates))]
    return new, gone


def test_id(line):
    """the test id of one line of a run: "FAILED " or "ERROR " (a collection error, `pytest -rfE`) taken off, and the id
    read up to the first " - " that stands outside brackets, so a parametrised id that holds " - " is kept whole (M65)"""
    line = line.strip()
    for mark in ("FAILED ", "ERROR "):
        if line.startswith(mark):
            line = line[len(mark):]
            break
    depth = 0
    for i, ch in enumerate(line):
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth = max(0, depth - 1)
        elif depth == 0 and line.startswith(" - ", i):
            return line[:i].strip()
    return line.strip()


def _lines(path):
    return [i for i in (test_id(l) for l in pathlib.Path(path).read_text(encoding="utf-8").splitlines()) if i]


def load(root=ROOT):
    return json.loads(pathlib.Path(root, LIST).read_text(encoding="utf-8"))


def main(argv):
    arg = lambda k: argv[argv.index(k) + 1] if k in argv else None
    d = load()
    if "--check" in argv:
        bad = form_problems(d, rows()) + shrink_problems() + working_problems(d)
        for b in bad:
            print(b)
        print("%d problem(s); %d test(s) and %d gate(s) on the list" % (len(bad), len(d["tests"]), len(d["gates"])))
        return 1 if bad else 0
    failures = _lines(arg("--compare") or arg("--draft"))
    red = _lines(arg("--gates")) if arg("--gates") else []
    if "--draft" in argv:
        print(json.dumps({"note": d.get("note", ""), "tests": [{"id": t, "row": "P-?", "why": "?"} for t in sorted(set(failures))],
                          "gates": [{"id": g, "row": "P-?", "why": "?"} for g in sorted(set(red))]}, indent=1))
        return 0
    new, gone = compare(d, failures, red)
    for n in new:
        print("NEW: " + n)
    for g in gone:
        print("now passes, to be taken off the list: " + g)
    print("%d new, %d now passing" % (len(new), len(gone)))
    return 1 if new else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
