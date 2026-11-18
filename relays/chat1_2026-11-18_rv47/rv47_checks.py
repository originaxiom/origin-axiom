#!/usr/bin/env python3
"""The check behind the status page's section 9 (main's M47). Data-free. Post hoc and not sealed: computed once.

    python3 -I -u rv47_checks.py <a checkout of main at a5e967af9> <a directory of reruns of main's checks>

G1  Main's new and changed check scripts for this seat's notes (the web_*.py files added to or changed in B1957's
    checks between c458df8ce and a5e967af9), rerun on a clean checkout of main: each rerun's output against the run
    file main committed, line by line. Only whether the lines are equal, and for unequal lines whether only numbers below 1e-6 differ, is printed;
    the outputs' text is not printed.
G2  The two checks main seeded at M47 (web_wb1_on_main, web_wf5_on_main), each run twice: the two runs compared.
"""
import os
import re
import subprocess
import sys

MAIN, RERUN = sys.argv[1], sys.argv[2]
NUM = re.compile(r"[-+]?\d+(?:\.\d*)?(?:[eE][-+]?\d+)?")
REL = "frontier/B1957_the_seats_claims_register/verification/checks/"
new = subprocess.run(["git", "diff", "--name-only", "--diff-filter=AM", "c458df8ce", "a5e967af9", "--", REL], cwd=MAIN,
                     capture_output=True, text=True).stdout.split()
names = sorted(os.path.basename(p)[:-3] for p in new if re.fullmatch(r".*/web_[^/]*\.py", p))
print("G1: %d new or changed check scripts" % len(names))
for s in names:
    a_path, b_path = os.path.join(RERUN, s + ".out"), os.path.join(MAIN, REL, s + "_run.txt")
    if not os.path.exists(a_path) or not os.path.exists(b_path):
        print("G1: %-26s missing %s" % (s, "rerun" if not os.path.exists(a_path) else "run file"))
        continue
    A, B = open(a_path).read().splitlines(), open(b_path).read().splitlines()
    unequal, only_small, worst = 0, True, 0.0
    for a, b in zip(A, B):
        if a == b:
            continue
        unequal += 1
        if NUM.sub("#", a) != NUM.sub("#", b):
            only_small = False
            continue
        for x, y in zip(NUM.findall(a), NUM.findall(b)):
            if x != y:
                fx, fy = float(x), float(y)
                if max(abs(fx), abs(fy)) >= 1e-6:
                    only_small = False
                worst = max(worst, max(abs(fx), abs(fy)))
    same_len = len(A) == len(B)
    verdict = ("identical" if unequal == 0 and same_len else
               "only numbers below 1e-6 differ (largest %.1e)" % worst if only_small and same_len else "DIFFERS")
    print("G1: %-26s lines %d against %d; unequal %d; %s" % (s, len(A), len(B), unequal, verdict))

# G2: the two checks main seeded at M47, each run twice here: the two runs against each other.
for s in ("web_wb1_on_main", "web_wf5_on_main"):
    p1, p2 = os.path.join(RERUN, s + ".out"), os.path.join(RERUN, s + ".second.out")
    if os.path.exists(p1) and os.path.exists(p2):
        print("G2: %-26s two runs here: %s" % (s, "identical" if open(p1).read() == open(p2).read() else "DIFFER"))
