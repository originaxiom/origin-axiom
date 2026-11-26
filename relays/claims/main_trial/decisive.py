#!/usr/bin/env python3
"""The decisive lines of main's seven trial cards (B2011 to B2017; the framework's trial, P-885).

The arcs' banked scripts predate the claim card's "DECISIVE:" mark, and banked files are not edited. This wrapper runs one
arc's decisive script unchanged, from the arc's own verification folder and on one thread, and prints the lines that
decide its card, each marked "DECISIVE:". The lines are normalised in two ways only:
  - a trailing timing bracket "  [<n> s]" and trailing spaces are removed;
  - a number in scientific notation whose absolute value is below 1e-10 is printed as 0, because its last digits depend on
    the linear-algebra library and its threads (B2014's S2 prints 2.8e-16 where a sum vanishes).
Which lines decide is written below, one rule per arc, before any run of this wrapper.

    python3 relays/claims/main_trial/decisive.py ARC              # runs the arc's script
    python3 relays/claims/main_trial/decisive.py ARC --from FILE  # selects from a saved output of that script
B2016 has its own wrapper, decisive_b2016.py, because its export needs sage with GAP.
Exit 0 when the arc's decisive lines all came out, as many as its rule expects; 1 when they did not; 2 when the run could
not be made (a missing script or program)."""
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
PY = sys.executable                      # the arcs' scripts run under the interpreter this wrapper runs under
TIMING = re.compile(r"\s+\[\d+ s\]\s*$")
TINY = re.compile(r"(?<![\w.])-?\d\.\d+e-(\d+)\b")


def normalise(line):
    line = TIMING.sub("", line.rstrip())
    return TINY.sub(lambda m: "0" if int(m.group(1)) > 10 else m.group(0), line)


def block(lines, opener, keep):
    """the lines of the block that opens with `opener` (up to the next line that opens with 'mod ') matching `keep`"""
    out, inside = [], False
    for l in lines:
        if l.startswith("mod "):
            inside = l.startswith(opener)
        if inside and any(k in l for k in keep):
            out.append(l)
    return out


def pick(lines, starts):
    return [l for l in lines if any(l.startswith(s) for s in starts)]


ARCS = {
    # A1: the orbit of (3,3,3) mod 135 keeps C's three fixed points, yet 10 of 959 charged roots go unpaired
    "B2011": dict(arc="frontier/B2011_*", cmd=[PY, "-B", "c60_levels.py"], n=5,
                  rule=lambda ls: block(ls, "mod 135,", ("mod 135,", "degree of gcd", "charged left unpaired",
                                                         "reduction mod 27 maps", "A1:"))),
    # N1: the four-move sum's pairing law on six orbits
    "B2012": dict(arc="frontier/B2012_*", cmd=[PY, "-B", "blind_checks.py"], n=6,
                  rule=lambda ls: pick(ls, ("N1 ",))),
    # Review 87's lock: its two tests, run without pytest
    "B2013": dict(arc="frontier/B2013_*", cmd=[PY, "-B", "-c",
                  "import importlib.util, sys; s = importlib.util.spec_from_file_location('t', 'test_b2013_review_87.py'); "
                  "m = importlib.util.module_from_spec(s); s.loader.exec_module(m); "
                  "names = sorted(n for n in dir(m) if n.startswith('test_')); "
                  "[(getattr(m, n)(), print(n, 'passed')) for n in names]"], n=2,
                  rule=lambda ls: [l for l in ls if l.endswith(" passed")]),
    # S1, S2, S3 and S5: the two walks, their sector law, the sisters, the fixed points up the tower
    "B2014": dict(arc="frontier/B2014_*", cmd=[PY, "-B", "walks.py"], n=21,
                  rule=lambda ls: pick(ls, ("S1 ", "S2 ", "S3:", "    (3, 3, 15)", "    (3, 3, 12)", "    on (3,3,15)",
                                            "S5: fixed-point counts"))),
    # R1: the value's minimal polynomial divides W's characteristic polynomial at the five levels
    "B2015": dict(arc="frontier/B2015_*", cmd=[PY, "-B", "rate_law.py"], n=5,
                  rule=lambda ls: [l for l in ls if "divides charpoly(W)" in l]),
    # the census over every orbit at seven levels
    "B2017": dict(arc="frontier/B2017_*", cmd=[PY, "-B", "census.py"], n=22,
                  rule=lambda ls: pick(ls, ("mod ", "    categories:", "    orbits in (a)", "over all levels"))),
}


def main(argv):
    if not argv or argv[0] not in ARCS:
        print(__doc__)
        return 2
    a = ARCS[argv[0]]
    hits = sorted(ROOT.glob(a["arc"]))
    if len(hits) != 1:
        print("the arc %s is not found once under %s" % (argv[0], ROOT))
        return 2
    here = hits[0] / "verification"
    if "--from" in argv:
        text = pathlib.Path(argv[argv.index("--from") + 1]).read_text(encoding="utf-8")
    else:
        env = dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1",
                   PYTHONDONTWRITEBYTECODE="1")
        try:
            r = subprocess.run(a["cmd"], cwd=here, capture_output=True, text=True, env=env)
        except FileNotFoundError as exc:
            print("the run could not be made: %s" % exc)
            return 2
        text = r.stdout
        if r.returncode != 0:
            print("the arc's script exited %d: %s" % (r.returncode, r.stderr.strip().splitlines()[-1:] or ""))
            return 1
    lines = a["rule"]([normalise(l) for l in text.splitlines()])
    for l in lines:
        print("DECISIVE: " + l)
    if len(lines) != a["n"]:
        print("%d decisive line(s) came out of %d expected" % (len(lines), a["n"]))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
