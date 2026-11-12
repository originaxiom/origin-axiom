#!/usr/bin/env python3
"""The ten specifications of checks that two sessions sent (main's M7): what each would meet on main's head today.

    python3 what_the_ten_specifications_would_reach_on_mains_head.py <a checkout at main's head> [<a checkout with series 4 applied>]

A count for each form that a syntax tree or a file's text can show.  Each count is of a FORM, by a first rough reader, and
is no judgement of any lock or script: it says how long a list "held by name as found" would be on the day a rule came.
Nothing is written into the checkout.  The second checkout is used only for its reader of the ways a test may not run."""
import ast
import importlib.util
import json
import os
import re
import subprocess
import sys
import warnings

warnings.simplefilter("ignore")           # a script of an arc may hold an escape that the parser warns of; it is not this reader's
MAIN = os.path.abspath(sys.argv[1])
SERIES = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else None


def tracked(*globs):
    r = subprocess.run(["git", "-C", MAIN, "ls-files", "--", *globs], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return [p for p in r.stdout.splitlines() if p]


def tree_of(rel):
    try:
        return ast.parse(open(os.path.join(MAIN, rel), encoding="utf-8", errors="replace").read())
    except SyntaxError:
        return None


print("main's head: " + subprocess.run(["git", "-C", MAIN, "rev-parse", "--short=9", "HEAD"], capture_output=True, text=True).stdout.strip())

# ---- the locks --------------------------------------------------------------------------------------------------------
locks = [p for p in tracked("tests/test_*.py", "frontier/*/verification/test_*.py") if os.path.basename(p).startswith("test_")]
arc_locks = [p for p in locks if p.startswith("frontier/") or re.match(r"tests/test_b\d", p)]
print("\nTHE LOCKS: %d files, of which %d are an arc's (in its folder, or tests/test_b<number>...)" % (len(locks), len(arc_locks)))

LOADS = {"spec_from_file_location", "import_module", "run_path", "run_module", "__import__", "exec", "eval", "SourceFileLoader"}
STARTS = {"run", "check_output", "check_call", "Popen", "call", "system", "getoutput"}


def forms(rel):
    """the forms a lock's tree shows: it starts a process; it loads a module by a path; it reads a .json or a .txt"""
    t = tree_of(rel)
    if t is None:
        return None
    out = set()
    for n in ast.walk(t):
        if isinstance(n, ast.Call):
            name = n.func.attr if isinstance(n.func, ast.Attribute) else getattr(n.func, "id", "")
            if name in STARTS and isinstance(n.func, ast.Attribute) and getattr(n.func.value, "id", "") in ("subprocess", "os"):
                out.add("starts a process")
            if name in LOADS:
                out.add("loads or executes code by a path or a name")
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and re.search(r"\.(json|txt|jsonl|csv)(\.gz)?$", n.value):
            out.add("names a committed output")
        if isinstance(n, (ast.Import, ast.ImportFrom)):
            mod = (n.module or "") if isinstance(n, ast.ImportFrom) else " ".join(a.name for a in n.names)
            if re.search(r"\bsys\b", mod):
                out.add("imports sys")
    src = open(os.path.join(MAIN, rel), encoding="utf-8", errors="replace").read()
    if re.search(r"sys\.path\.(insert|append)", src):
        out.add("puts a folder on the import path")
    return out


count = {}
unreadable = 0
neither = 0
for rel in arc_locks:
    f = forms(rel)
    if f is None:
        unreadable += 1
        continue
    for x in f:
        count[x] = count.get(x, 0) + 1
    if not (f & {"starts a process", "loads or executes code by a path or a name", "puts a folder on the import path"}):
        neither += 1
print("   specification Six and the second check of the other session (a lock does not import or run its producer):")
for x in ("starts a process", "loads or executes code by a path or a name", "puts a folder on the import path", "names a committed output"):
    print("      %5d of %d arc locks: %s" % (count.get(x, 0), len(arc_locks), x))
print("      %5d of %d arc locks do none of the first three; %d could not be parsed" % (neither, len(arc_locks), unreadable))

if SERIES:
    spec = importlib.util.spec_from_file_location("vacuity_reader", os.path.join(SERIES, "scripts", "checks", "check_test_vacuity.py"))
    v = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(v)
    may_skip = files = 0
    for rel in locks:
        try:
            found = v.switches(open(os.path.join(MAIN, rel), encoding="utf-8", errors="replace").read())
        except Exception:
            continue
        n = sum(1 for how_many in (found or {}).values() if how_many)          # the table: a test (or "" for the module) -> its ways not to run
        may_skip += n
        files += bool(n)
    print("   specification Six, its third part (a lock does not skip): %d test(s) or module(s) in %d of the %d lock files can skip or are marked to,"
          % (may_skip, files, len(locks)))
    print("      by the reader of series 4's fourth patch, which holds what stood at its anchor and refuses a new one")

# ---- a literal at a key that claims ------------------------------------------------------------------------------------
CLAIMS = re.compile(r"(holds|verified|reproduced|passed|invariant|extends|acyclic|vanishes|^is_|^has_|^all_|^ok$|unimodular|unique|closes|preserved|cancels)", re.I)
scripts = [p for p in tracked("frontier/*/verification/*.py") if not os.path.basename(p).startswith("test_")]
hit_files = hits = parsed = 0
for rel in scripts:
    t = tree_of(rel)
    if t is None:
        continue
    parsed += 1
    here = 0
    for n in ast.walk(t):
        if isinstance(n, ast.Dict):
            for k, val in zip(n.keys, n.values):
                if isinstance(k, ast.Constant) and isinstance(k.value, str) and CLAIMS.search(k.value) \
                        and isinstance(val, ast.Constant) and (val.value is True or (val.value == 0 and val.value is not False)):
                    here += 1
    hits += here
    hit_files += bool(here)
print("\nTHE PRODUCERS: %d scripts in the arcs' verification folders that are not locks, %d parsed" % (len(scripts), parsed))
print("   specification Two and the first check of the other session (a claim is not a typed True or a typed zero):")
print("      %5d dictionary entries in %d scripts: a key that reads as a claim, and a value that is the literal True or the literal 0" % (hits, hit_files))

# ---- a correction that did not travel ----------------------------------------------------------------------------------
MARK = re.compile(r"\[(CORRECTED|Corrected|Wrong|WRONG|Scoped|SCOPED|Retracted|RETRACTED|Amended|AMENDED)\b")
with_mark = lonely = 0
for rel in tracked("frontier/*/FINDINGS.md"):
    text = open(os.path.join(MAIN, rel), encoding="utf-8", errors="replace").read()
    if not MARK.search(text):
        continue
    with_mark += 1
    verdict = os.path.join(MAIN, os.path.dirname(rel), "arc_verdict.json")
    try:
        body = open(verdict, encoding="utf-8", errors="replace").read()
    except OSError:
        body = ""
    if not MARK.search(body):
        lonely += 1
print("\nTHE ARCS' PAGES")
print("   specification Seven, its first part (a correction travels to the verdict file):")
print("      %5d FINDINGS.md carry a dated mark of correction in brackets; in %d of them the arc's verdict file carries none" % (with_mark, lonely))
