#!/usr/bin/env python3
"""WP-0.9, card C4: what stands, in the commit, for each arc the candidate runs on.  A mechanical read, and no grade.

    python3 what_stands_for_the_fourteen.py CHECKOUT GATES_FILE

CHECKOUT is a checkout of the commit to read.  GATES_FILE is a gates' file that holds the vacuity checker of WP-0.7's
series 3 and 4 beside it (scripts/checks/check_test_vacuity.py): it is used to ask whether an assert in a lock can fail,
and whether a lock compares, as text, a float that a process printed.

The fourteen are read from main's own measurement (frontier/B1888_.../verification/candidate_chain.json, "arcs").
For each: its verdict; its sealed-style files; its locks, in its folder and in tests/ under its number; how many of their
tests there are and how many cannot fail; whether one compares a printed float as text; its scripts; its committed
outputs (files named *_run.txt, *_out.txt, *.json or *.jsonl beside its scripts).  Nothing is written.  Standard library."""
import ast, glob, importlib.util, json, os, re, sys

root, gates_file = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
sys.path.insert(0, os.path.join(os.path.dirname(gates_file), "..", "checks"))
sys.dont_write_bytecode = True
import check_test_vacuity as ctv

chain = json.load(open(glob.glob(os.path.join(root, "frontier", "B1888_*", "verification", "candidate_chain.json"))[0], encoding="utf-8"))
SEALS = ("PREREG*", "*DESIGN*.md", "SEALED*.md", "DECLARATION.md")
tracked = set(os.popen("git -C '%s' ls-files" % root).read().split("\n"))
rows = []
for arc in chain["arcs"]:
    d = os.path.join(root, "frontier", arc)
    v = json.load(open(os.path.join(d, "arc_verdict.json"), encoding="utf-8"))
    seals = sorted({os.path.basename(p) for pat in SEALS for p in glob.glob(os.path.join(d, pat))})
    locks = sorted(glob.glob(os.path.join(d, "verification", "test_*.py")) + glob.glob(os.path.join(root, "tests", "test_%s_*.py" % arc.split("_")[0].lower())))
    n_tests = n_cannot = 0; pins = []
    for lock in locks:
        rel = os.path.relpath(lock, root)
        tree = ast.parse(open(lock, encoding="utf-8").read())
        for fn in ast.walk(tree):
            if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)) and fn.name.startswith("test"):
                n_tests += 1
                asserts = [n for n in ast.walk(fn) if isinstance(n, ast.Assert)]
                n_cannot += (not asserts) or bool(ctv.cannot_fail(fn))
        found = ctv.printed_floats(rel, tree, ctv._finder(rel, tracked), lambda p: open(os.path.join(root, p), encoding="utf-8", errors="replace").read())[0]
        pins += sorted({f[0] for f in found})
    scripts = [p for p in glob.glob(os.path.join(d, "**", "*.py"), recursive=True) if not os.path.basename(p).startswith("test_")]
    outputs = [p for p in glob.glob(os.path.join(d, "**", "*"), recursive=True)
               if os.path.isfile(p) and re.search(r"(_run\.txt|_out\.txt|\.jsonl?)$", p) and os.path.basename(p) != "arc_verdict.json"]
    rows.append((arc, v["verdict"], bool(v.get("instrument")), seals, [os.path.relpath(l, root) for l in locks], n_tests, n_cannot, pins, len(scripts), len(outputs)))

head = os.popen("git -C '%s' rev-parse --short=9 HEAD" % root).read().strip()
print("the fourteen arcs the candidate runs on (main's B1888), read at %s\n" % head)
print("%-52s %-9s %-28s %5s %6s %7s %7s %7s" % ("arc", "verdict", "sealed-style files", "locks", "tests", "scripts", "outputs", "pins"))
for arc, verdict, inst, seals, locks, n_tests, n_cannot, pins, n_scripts, n_out in rows:
    print("%-52s %-9s %-28s %5d %6s %7d %7d %7d" % (arc[:52], verdict, (", ".join(seals) or "none")[:28], len(locks),
                                                     "%d" % n_tests + ("(%d)" % n_cannot if n_cannot else ""), n_scripts, n_out, len(pins)))
print("\ntests: the number of test functions in the arc's locks; in brackets, how many of them have no assert that can fail.")
print("pins: tests of the arc's locks that compare, as text, a float that a process printed.")
by = {}
for r in rows: by[r[1]] = by.get(r[1], 0) + 1
print("\nverdicts: " + ", ".join("%d %s" % (n, k) for k, n in sorted(by.items(), key=lambda kv: -kv[1])))
print("with no lock of its own: " + (", ".join(r[0].split("_")[0] for r in rows if not r[4]) or "none"))
print("with no sealed-style file: " + (", ".join(r[0].split("_")[0] for r in rows if not r[3]) or "none"))
print("with a test that pins a printed float: " + (", ".join("%s (%s)" % (r[0].split("_")[0], ", ".join(r[7])) for r in rows if r[7]) or "none"))
