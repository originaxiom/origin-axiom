#!/usr/bin/env python3
"""The decisive lines of main's trial card for B2016 (P-885): HEAVY, because the arc's export needs sage with GAP.

It imports sage, so that the intake's static guard marks the card heavy and the rerun is made on the author's machine under
sage's Python. It runs the arc's two scripts unchanged, from the arc's verification folder: cosets_export.py (sage, which
writes coset_actions.json beside itself) and then cosets_gap.py, and prints the decisive lines of the second with
decisive.py's normalisation and its rule for B2016.
    sage -python relays/claims/main_trial/decisive_b2016.py
    python3 relays/claims/main_trial/decisive_b2016.py --from FILE   # selects from a saved output of cosets_gap.py
Exit 0 when the eight decisive lines came out; 1 when they did not; 2 when the run could not be made."""
import importlib.util
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
_s = importlib.util.spec_from_file_location("decisive_common", HERE / "decisive.py")
D = importlib.util.module_from_spec(_s); _s.loader.exec_module(D)
RULE = lambda ls: D.pick(ls, ("mod 27: |G|", "mod 81: |G|", "    the whole's stabiliser class", "    categories:",
                              "    the classes in (a)"))
N = 8


def main(argv):
    hits = sorted(D.ROOT.glob("frontier/B2016_*"))
    if len(hits) != 1:
        print("the arc B2016 is not found once under %s" % D.ROOT); return 2
    here = hits[0] / "verification"
    if "--from" in argv:
        text = pathlib.Path(argv[argv.index("--from") + 1]).read_text(encoding="utf-8")
    else:
        import sage.all  # noqa: F401  (the declaration of heaviness; the export below needs it)
        env = dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
        for script in ("cosets_export.py", "cosets_gap.py"):
            r = subprocess.run([sys.executable, "-B", script], cwd=here, capture_output=True, text=True, env=env)
            if r.returncode != 0:
                print("%s exited %d" % (script, r.returncode)); return 1
        text = r.stdout
    lines = RULE([D.normalise(l) for l in text.splitlines()])
    for l in lines:
        print("DECISIVE: " + l)
    if len(lines) != N:
        print("%d decisive line(s) came out of %d expected" % (len(lines), N)); return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
