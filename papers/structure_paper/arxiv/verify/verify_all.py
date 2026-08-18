#!/usr/bin/env python3
"""Appendix B — run every verification the paper ships, print a table, exit non-zero
on any drift.

DESIGN CONSTRAINT, and it is the whole point of the appendix. The empirical failure
mode of this programme is RETRIEVAL, not computation: across a full day inside the
corpus every error was navigational and every computation reproduced exactly. The
repo's own review banner says it -- "zero mathematics, all retrieval". So the paper
must carry its verification INLINE, and a reader must never need the corpus.

Therefore every script in this directory:
  * imports NOTHING project-internal (sympy and the stdlib only),
  * uses EXACT arithmetic in every verdict-bearing comparison -- no float decides
    anything,
  * prints its own expected values, and
  * exits non-zero on drift.

This runner adds nothing to those guarantees; it just makes them one command.

Run:  python3 verify_all.py            (from anywhere)
      python3 verify_all.py --list     (names only)

Exit 0 = every check reproduced. Exit 1 = at least one did not.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def scripts():
    """Every check_*.py beside this file, in stable order."""
    return sorted(f for f in os.listdir(HERE)
                  if f.startswith("check_") and f.endswith(".py"))


def main(argv):
    names = scripts()

    if "--list" in argv:
        for n in names:
            print(n)
        return 0

    # An empty suite must FAIL. A verification appendix that verifies nothing is
    # the exact shape of a check that cannot fail, and this file will not be it.
    if not names:
        print("FAIL: no check_*.py found in verify/ -- an empty suite is not a pass")
        return 1

    print("=" * 70)
    print("Appendix B — verification suite")
    print("=" * 70)

    # Dependency preflight.  Nine of the eleven scripts need SymPy; without it they
    # fail one at a time with an import error that looks like nine separate defects
    # rather than one missing package.  Name it once, up front, and say what to do.
    try:
        import sympy  # noqa: F401
    except ImportError:
        print("FAIL: SymPy is not installed, and 9 of the "
              f"{len(names)} checks require it.")
        print("      Install it and re-run:")
        print("          python3 -m pip install -r requirements.txt")
        print("      (tested with Python 3.12 and SymPy 1.12; only")
        print("       check_homology.py and check_shadow_modulus.py are stdlib-only)")
        return 1

    results = []
    for name in names:
        proc = subprocess.run([sys.executable, os.path.join(HERE, name)],
                              capture_output=True, text=True)
        ok = proc.returncode == 0
        results.append((name, ok, proc))
        print(f"  [{'PASS' if ok else 'FAIL'}]  {name}")
        if not ok:
            tail = (proc.stdout or "").rstrip().splitlines()[-15:]
            for line in tail:
                print(f"           {line}")
            if proc.stderr.strip():
                for line in proc.stderr.rstrip().splitlines()[-8:]:
                    print(f"           ! {line}")

    passed = sum(1 for _n, ok, _p in results if ok)
    print("-" * 70)
    print(f"  {passed} / {len(results)} verifications reproduced")
    print()
    print("  SCOPE. This runner executes block (a) of the Appendix B table -- the")
    print("  self-contained scripts that travel inside the submitted source. Block")
    print("  (b) of that table depends on the repository snapshot (SnapPy, the")
    print("  character tables, the chain ledger) and is NOT run here. Exit 0 means")
    print("  block (a) reproduced; it is not a statement about block (b).")

    if passed != len(results):
        print("\nFAIL: at least one claim in the paper did not reproduce.")
        return 1
    print("\nPASS: every check in BLOCK (a) reproduced exactly.")
    print("      This says nothing about block (b), which was not run.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
