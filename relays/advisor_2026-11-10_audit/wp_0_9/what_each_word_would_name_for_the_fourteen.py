#!/usr/bin/env python3
"""WP-0.9, card C4: for each arc the candidate runs on, which of the five words its own files could carry, and what the
word would name.  A mechanical read with the series' own checker, and no grade: the choice of a word is main's.

    python3 what_each_word_would_name_for_the_fourteen.py CHECKOUT ARC_DATA_FILE [--json OUT]

CHECKOUT is a checkout of the commit to read.  ARC_DATA_FILE is scripts/checks/arc_data.py WITH patch 1 of the series.
For each arc and each word the script gathers the arc's own files of the kind the word asks, and asks the checker's own
functions whether they are enough.  For "sealed cells held" the count of cells is not in any file this script reads: the
word is marked as possible where a sealed file stands, and the count is left to whoever grades.  Nothing is written
but the --json file.  Standard library."""
import glob, importlib.util, json, os, re, sys

root, arc_data_file = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("arc_data_with_the_patch", arc_data_file)
a = importlib.util.module_from_spec(spec); spec.loader.exec_module(a)
ctv = a._vacuity()
chain = json.load(open(glob.glob(os.path.join(root, "frontier", "B1888_*", "verification", "candidate_chain.json"))[0], encoding="utf-8"))["arcs"]
rel = lambda p: os.path.relpath(p, root).replace(os.sep, "/")
table = {}
for folder in chain:
    d = os.path.join(root, "frontier", folder)
    v = json.load(open(os.path.join(d, "arc_verdict.json"), encoding="utf-8"))
    own = [rel(p) for p in glob.glob(os.path.join(d, "**", "*"), recursive=True) if os.path.isfile(p)]
    own += [rel(p) for p in glob.glob(os.path.join(root, "tests", "test_%s_*.py" % str(v["id"]).lower()))]
    locks = sorted(p for p in own if a._a_lock_that_can_fail(os.path.join(root, p), ctv))
    scripts = sorted(p for p in own if p.endswith(".py") and not os.path.basename(p).startswith("test_"))
    outputs = sorted(p for p in own if re.search(r"(_run\.txt|_out\.txt|\.jsonl?)$", p) and os.path.basename(p) != "arc_verdict.json")
    seals = sorted(p for p in own if p.count("/") == 2 and any(__import__("fnmatch").fnmatch(os.path.basename(p), pat) for pat in a.SEAL_PATTERNS))
    table[folder] = {"verdict": v["verdict"], "theorem": locks[:1], "exact computation": (locks[:1] + scripts[:1]) if (locks and scripts) else [],
                     "numerical estimate": (scripts[:1] + outputs[:1]) if (scripts and outputs) else [],
                     "sealed cells held": seals[:1], "counts": {"locks": len(locks), "scripts": len(scripts), "outputs": len(outputs), "seals": len(seals)}}
head = os.popen("git -C '%s' rev-parse --short=9 HEAD" % root).read().strip()
print("for each arc the candidate runs on, read at %s: could its own files carry the word?  (yes = the files the word asks are there)\n" % head)
print("%-52s %-9s %-8s %-12s %-10s %-22s %s" % ("arc", "verdict", "theorem", "exact comp.", "num. est.", "sealed cells held", "process"))
for folder, t in table.items():
    yn = lambda k: "yes" if t[k] else "NO"
    print("%-52s %-9s %-8s %-12s %-10s %-22s %s" % (folder[:52], t["verdict"], yn("theorem"), yn("exact computation"), yn("numerical estimate"),
                                                     ("yes, with its count" if t["sealed cells held"] else "NO"), "yes"))
print("\nin all: a theorem %d of 14; an exact computation %d; a numerical estimate %d; sealed cells held %d; a process 14." % tuple(
    sum(1 for t in table.values() if t[k]) for k in ("theorem", "exact computation", "numerical estimate", "sealed cells held")))
print("\"yes\" says that files of the kind the word asks stand in the arc's own folder (or, for a lock, in tests/ under its number).")
print("It does not say that the word is true of the arc: that is read from the arc, and it is main's to say.")
if "--json" in sys.argv:
    open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8").write(json.dumps(table, indent=1) + "\n")
