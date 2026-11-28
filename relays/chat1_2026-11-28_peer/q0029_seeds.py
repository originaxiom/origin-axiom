#!/usr/bin/env python3
"""Starting points for the peer check of Q0029 (q0029_check.py): not a test, and not decisive.

The check's first run (commit b4aff7623) found no geometric closed orbit of LLLRRR: its Newton search from random starts
in the chart falls, start after start, to the chart's origin, a super-attracting fixed point. The geometric orbits of
the long words of C9 are harder still. This script writes starting points for that search and nothing else: for each
word W the check needs, the tetrahedron shapes of the punctured-torus bundle b++ W' in SnapPy's high-precision kernel,
where W' is W read backwards with L and R exchanged (the convention under which SnapPy's shapes seed this seat's
chart; found by trial on LLLLLLRLR, LLLRLLRR and LLRRLLRLR), and SnapPy's volume of b++ W, which the check prints
beside its own as a cross-check it does not judge. The check derives a chart point from two of the shapes, solves the
orbit equations by its own Newton at 80 digits, and accepts only an orbit whose every shape has positive imaginary
part; the starting point's source does not enter what it then computes.

SnapPy is not among the packages the sandbox allows, so this script is run once, here, and its output is committed
beside the check as q0029_seeds.json.

    python3 relays/chat1_2026-11-28_peer/q0029_seeds.py      # writes q0029_seeds.json beside itself
"""
import json
import pathlib
import warnings

warnings.filterwarnings("ignore")
import snappy  # noqa: E402

WORDS = ["LR", "LLRR", "LLLRRR"]
for H, P, K in (("LLLLLLR", "LR", 12), ("LLRRLLR", "LR", 12), ("LLLRRRRLLLR", "LR", 12), ("LLLR", "LLRR", 9),
                ("LLLLRR", "LLLRRR", 8)):
    WORDS += [H + P * k for k in (K - 2, K - 1, K)]


def flip(w):
    return w[::-1].translate(str.maketrans("LR", "RL"))


NOTE = "SnapPy %s, ManifoldHP; shapes of b++ (W reversed, L and R exchanged); volume of b++ W"
out = {"note": NOTE % snappy.__version__, "words": {}}
for w in WORDS:
    M = snappy.ManifoldHP("b++" + flip(w))
    shapes = [("%s %s" % (str(s.real()).replace(" E", "E"), str(s.imag()).replace(" E", "E")))
              for s in M.tetrahedra_shapes("rect")]
    out["words"][w] = {"solution": M.solution_type(), "shapes": shapes,
                       "volume": str(snappy.ManifoldHP("b++" + w).volume())}
    print(w, M.solution_type(), str(snappy.ManifoldHP("b++" + w).volume())[:30])
pathlib.Path(__file__).with_name("q0029_seeds.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
