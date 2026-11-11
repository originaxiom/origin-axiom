#!/usr/bin/env python3
"""Re-audit 7, the finding E7: one more planted case, written AFTER e7_checks.py ran and because of its read-out.

The read-out listed the README's line on the last landing, which holds the words "0.000 BITS OF DESIGNER FREEDOM" in capitals
and does not turn the lock red.  The lock's sweep asks that a line state the zero AND name the ledger, and it reads the
second in lower case only ("designer", "freedom ledger", "B1028").  The claim as first asserted is in capitals.

EXPECTATION, written before the run:
  r11  a new page under docs/ holding the claim in its own capitals, "RETROACTIVE DESIGNER FREEDOM = 0.000 BITS, EVERY ZERO
       MACHINE-CHECKED.", with no arc named on the line                                      NOT caught

    python3 e7_one_more_plant.py --work DIR      (DIR: the scratch clone e7_checks.py left, at main's head and clean)
"""
import sys, os, re, subprocess

work = os.path.abspath(sys.argv[sys.argv.index("--work") + 1])
LOCK = "tests/test_b1028_freedom_ledger.py"
sha = subprocess.run(["git", "-C", work, "rev-parse", "--short=9", "HEAD"], capture_output=True, text=True).stdout.strip()
assert not subprocess.run(["git", "-C", work, "status", "--short"], capture_output=True, text=True).stdout.strip(), "the scratch clone is not clean"
with open(os.path.join(work, "docs", "PLANTED_PAGE.md"), "w", encoding="utf-8") as fh:
    fh.write("# A planted page\n\nRETROACTIVE DESIGNER FREEDOM = 0.000 BITS, EVERY ZERO MACHINE-CHECKED.\n")
r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", LOCK], cwd=work, capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
caught = r.returncode != 0
os.remove(os.path.join(work, "docs", "PLANTED_PAGE.md"))
print("at main %s" % sha)
print("r11  %s  %-11s expected not caught  the claim in its own capitals, no arc named on the line" % ("HOLDS" if not caught else "FAILS", "CAUGHT" if caught else "NOT CAUGHT"))
