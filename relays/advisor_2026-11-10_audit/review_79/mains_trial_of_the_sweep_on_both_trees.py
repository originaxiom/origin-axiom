#!/usr/bin/env python3
"""Main's trial of the retraction sweep (B1894), run again on main's head and on the series: does series 3's patch on the
sweep change what counts as a mention?

    python3 mains_trial_of_the_sweep_on_both_trees.py <a checkout at main's head> <a checkout with series 3 applied>

Main's trial adds ten phrases in memory, leaves the registry as it is, and runs the sweep as it stands.  The ten are read
here from main's own output of that trial.  The same is done on both trees, and the lines reported are compared.
Nothing is written into either checkout."""
import importlib.util
import os
import re
import sys

MAIN, SERIES = (os.path.abspath(p) for p in sys.argv[1:3])
trial = open(os.path.join(MAIN, "frontier", "B1894_review_79_the_second_round", "verification",
                          "what_the_retraction_sweep_would_report_out.txt"), encoding="utf-8").read()
ten = [m.group(1) for m in re.finditer(r"^\s+\d+  (.+)$", trial, re.M)]
said = re.search(r"phrases registered today: (\d+); added for the trial: (\d+); lines the sweep would report: (\d+)", trial)
print("main's trial, as its output says: %s phrases registered, %s added, %s lines reported" % said.groups())
print("the phrases read from that output: %d" % len(ten))


def run(tree, name):
    spec = importlib.util.spec_from_file_location("sweep_of_" + name, os.path.join(tree, "scripts", "checks", "retraction_sweep.py"))
    rs = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(rs)
    registered = list(rs._phrases())
    before = rs.sweep()
    rs._phrases = lambda: registered + [p for p in ten if p not in registered]
    after = rs.sweep()
    return registered, before, after


out = {}
for name, tree in (("main's head", MAIN), ("the series", SERIES)):
    registered, before, after = run(tree, name.replace(" ", "_").replace("'", ""))
    of_the_ten = sorted((rel, n, p) for rel, n, p in after if p in ten)
    out[name] = of_the_ten
    print("\n%s" % name)
    print("   phrases the sweep reads from the registry: %d;   lines it reports today: %d" % (len(registered), len(before)))
    print("   with the ten added: %d lines reported, %d of them for the ten" % (len(after), len(of_the_ten)))
a, b = out["main's head"], out["the series"]
print("\nthe lines reported for the ten: the same on both trees: %s" % ("YES" if a == b else "NO"))
for rel, n, p in sorted(set(a) - set(b))[:10]:
    print("   on main's head only: %s:%d -> %s" % (rel, n, p))
for rel, n, p in sorted(set(b) - set(a))[:10]:
    print("   on the series only:  %s:%d -> %s" % (rel, n, p))
