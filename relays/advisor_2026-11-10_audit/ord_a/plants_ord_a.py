#!/usr/bin/env python3
"""The acceptance row ORD-a, run on main as main asked (its note of 2026-11-11 on the scoreboard page and the order).

ORD-a: the sealed card waits on the audit's errors in the mathematics.  Main's mend (its landing f4ff1fa1f): the
upstream audit needs WP-0.8, and the builder refuses a work order with more than one package that nothing needs.

    python3 plants_ord_a.py --ref origin/main --work DIR      (DIR outside the repository; it will hold a clone)

Each plant edits the programme's source in a scratch clone and runs main's builder there.  Nothing is pushed.

EXPECTATIONS, written before the first run:
  o0  the source as main has it                                                        BUILDS (the control)
  o1  WP-0.8 dropped from the upstream audit's needs (main's own planted case)          REFUSED
  o2  WP-0.8 moved from the upstream audit to the comparison (WP-6.1)                   BUILDS
  o3  WP-0.8 moved from the upstream audit to the independent challenge (WP-5.4)        BUILDS
In o2 and o3 the order still has one end, so main's rule is met; and the card (WP-5.3) no longer rests on WP-0.8, so
it could be sealed with the errors open.  If either builds, main's mend is weaker than ORD-a by that much.
"""
import sys, os, subprocess, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
ref = sys.argv[sys.argv.index("--ref") + 1]
work = sys.argv[sys.argv.index("--work") + 1]
SRC = "frontier/B1861_the_closure_programme/verification/programme_source.py"
BUILD = "frontier/B1861_the_closure_programme/verification/build_programme.py"


def sh(args, cwd):
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True)


sha = sh(["git", "rev-parse", "--short=9", ref], REPO).stdout.strip()
if os.path.exists(work): shutil.rmtree(work)
sh(["git", "clone", "-q", "--no-hardlinks", REPO, work], REPO)
sh(["git", "checkout", "-q", "--detach", sha], work)
orig = open(os.path.join(work, SRC), encoding="utf-8").read()
A = '"main", ["WP-0.6", "WP-0.7", "WP-0.8", "WP-0.12", "@C1", "@C2", "@C3", "@C4"], "NOT STARTED", [], [])'
A_without = A.replace('"WP-0.8", ', "")
C6 = '"the owner", ["WP-5.4"], "NOT STARTED", ["P-709"], [])'
C54 = '"another seat", ["WP-5.3"], "NOT STARTED", [], ["D:14"])'
for needle in (A, C6, C54):
    if orig.count(needle) != 1: sys.exit("the source is not as this script expects: %r occurs %d times" % (needle[:40], orig.count(needle)))


def run(name, what, text):
    open(os.path.join(work, SRC), "w", encoding="utf-8").write(text)
    r = sh([sys.executable, "-B", BUILD], work)
    out = (r.stdout + r.stderr)
    refused = [l for l in out.split("\n") if l.startswith("REFUSED:")]
    verdict = "REFUSED" if refused or r.returncode != 0 else "BUILDS"
    print("%-3s %-8s %s" % (name, verdict, what))
    for l in refused[:3]: print("      " + l[:230])
    if not refused and r.returncode != 0: print("      exit %d: %s" % (r.returncode, out.strip().split("\n")[-1][:200]))


print("ORD-a on main at %s" % sha)
run("o0", "the source as main has it (control)", orig)
run("o1", "WP-0.8 dropped from the upstream audit's needs", orig.replace(A, A_without))
run("o2", "WP-0.8 moved from the upstream audit to the comparison", orig.replace(A, A_without).replace(C6, C6.replace('["WP-5.4"]', '["WP-5.4", "WP-0.8"]')))
run("o3", "WP-0.8 moved from the upstream audit to the independent challenge", orig.replace(A, A_without).replace(C54, C54.replace('["WP-5.3"]', '["WP-5.3", "WP-0.8"]')))
