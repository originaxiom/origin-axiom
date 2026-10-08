#!/usr/bin/env python3
"""W23 of the weave: THE RECORD'S E8 FRAMES ON THE WEAVE'S FIBRE. How many complete chiral generations the common point
can give there, with W22's end condition.

The rule (named before the run; the census is every bundle below, none chosen):
- E8 contains G x SU(n) with G = E6 (n = 3), SO(10) (n = 4) and SU(5) (n = 5). Matter: E6's 27 with the SU(3) bundle
  V; SO(10)'s 16 with the SU(4) bundle V; SU(5)'s 10 with the SU(5)' bundle W and its 5-bar with Lambda^2 W (F-HE's
  frame).
- The bundles are built from the common point's local systems on the fibre: the four characters c_chi (chi trivial or
  one of the three parities) and the four spin doublets D_chi = chi (x) rho_Q. Every multiset of blocks of total rank n
  whose determinant is trivial (SU(n)) is read.
- The index (W22): every spin-doublet block in a matter bundle counts +1 (the condition every move keeps), every
  character block 0 (it extends over the puncture; on the torus with the odd spin structure its index is 0).
- Tensor rules (Q8): D_a (x) D_b = c_ab + c_(ab p1) + c_(ab p2) + c_(ab p3); D_a (x) c_b = D_ab; c_a (x) c_b = c_ab;
  Lambda^2 D_a = c_1; Lambda^2 c = 0; Lambda^2 of a sum by blocks.

A complete generation is one 27 (E6), one 16 (SO(10)), or one 10 with one 5-bar (SU(5)).

    python3 the_e8_frames_on_the_fibre.py   ->  the_e8_frames_on_the_fibre.json beside it
"""
import itertools
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHARS = ["1", "p1", "p2", "p3"]                     # the zero parity and the three parities (Klein four-group)
MUL = {("1", x): x for x in CHARS}
MUL.update({(x, "1"): x for x in CHARS})
for x in CHARS[1:]:
    MUL[(x, x)] = "1"
for x, y in itertools.permutations(CHARS[1:], 2):
    MUL[(x, y)] = [z for z in CHARS[1:] if z not in (x, y)][0]
BLOCKS = [("c", x) for x in CHARS] + [("D", x) for x in CHARS]


def rank(b):
    return 2 if b[0] == "D" else 1


def tensor(a, b):
    (ta, xa), (tb, xb) = a, b
    if ta == "c" and tb == "c":
        return [("c", MUL[(xa, xb)])]
    if ta == "D" and tb == "c":
        return [("D", MUL[(xa, xb)])]
    if ta == "c" and tb == "D":
        return [("D", MUL[(xa, xb)])]
    ab = MUL[(xa, xb)]
    return [("c", ab)] + [("c", MUL[(ab, p)]) for p in CHARS[1:]]


def wedge2(blocks):
    out = []
    for b in blocks:
        if b[0] == "D":
            out.append(("c", "1"))
    for a, b in itertools.combinations(blocks, 2):
        out += tensor(a, b)
    return out


def index(blocks):
    return sum(1 for b in blocks if b[0] == "D")


def det_trivial(blocks):
    d = "1"
    for t, x in blocks:
        if t == "c":
            d = MUL[(d, x)]
    return d == "1"


def bundles(n):
    out = []
    for k in range(0, n + 1):
        for combo in itertools.combinations_with_replacement(BLOCKS, k):
            if sum(rank(b) for b in combo) == n and det_trivial(combo):
                out.append(combo)
    return out


def run():
    res = {}
    e6 = Counter(index(V) for V in bundles(3))
    so10 = Counter(index(V) for V in bundles(4))
    su5 = Counter((index(W), index(wedge2(W))) for W in bundles(5))
    res["E6 (27 with the SU(3) bundle): number of chiral 27s -> how many bundles"] = {str(k): v for k, v in sorted(e6.items())}
    res["SO(10) (16 with the SU(4) bundle): chiral 16s -> bundles"] = {str(k): v for k, v in sorted(so10.items())}
    res["SU(5) (10 with W, 5-bar with Lambda^2 W): (N(10), N(5-bar)) -> bundles"] = {
        str(k): v for k, v in sorted(su5.items())}
    weaves_five = (("D", "1"), ("c", "p1"), ("c", "p2"), ("c", "p3"))
    res["the weave's five D + P (F-HE, W17): (N(10), N(5-bar))"] = [index(weaves_five), index(wedge2(weaves_five))]
    complete = {"E6": max(e6), "SO(10)": max(so10),
                "SU(5)": max((a for (a, b) in su5 if a == b), default=0)}
    res["the most complete chiral generations each frame gives"] = complete
    res["three complete generations in any of these frames"] = bool(max(complete.values()) >= 3)
    res["SU(5) anomaly of the weave's five's bulk modes (N(10) - N(5-bar))"] = index(weaves_five) - index(wedge2(weaves_five))
    return res


if __name__ == "__main__":
    out = run()
    with open(HERE / "the_e8_frames_on_the_fibre.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(json.dumps(out, indent=1, ensure_ascii=False))
