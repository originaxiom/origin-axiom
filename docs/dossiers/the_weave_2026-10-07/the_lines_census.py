#!/usr/bin/env python3
"""W6 of the weave (docs/THE_WEAVE.md), the design-time structure census (no count): which threads can carry anything on
the weave's three lines. The rule, named before the run: every odd-trace state of GENESIS (a primitive word in L and R
with both letters, up to rotation and the exchange of L and R, with either sign) of length at most 6, twelve threads; on
each, the forced A4 cover N (sm:B1550's tetra_lib, W3), every A4 orbit of characters of order dividing 4, and at each
orbit's representative the structure (h1, r1, n) of nu (x) rho in route P (sm:B1549's read_P on N's own presentation).
A member is a character with n > 0; the frame's generation-shaped counts need one. The budget: one pass.

The banked library is used unchanged; its precision is raised from here (the holonomy at 160 digits, the modules at 100),
because at length 6 a relator of N loses more than 15 of the library's 50 digits (its guard, a relator equal to 1 within
1e-35, stopped -LLLLLR at 50). The guard and the rank tolerance (1e-30 of the largest entry) are unchanged.

    python3 the_lines_census.py STATE ...   ->  one JSON line per state on stdout
    python3 the_lines_census.py threads     ->  the twelve states"""
import itertools
import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent


def _root():
    for p in HERE.parents:
        if (p / "frontier").is_dir():
            return p
    raise RuntimeError("the repository root (the first parent holding frontier/) was not found")


sys.path.insert(0, str(_root() / "frontier" / "B1550_the_three_parities" / "verification"))
import tetra_lib as L  # noqa: E402  (sm:B1550's library, banked; it loads sm:B1549's three_lib)

T = L.T
HOL_DPS, DPS = 160, 100
T.DPS = DPS


def holonomy(sw):
    """sm:B1549's holonomy, solved at HOL_DPS digits instead of 60"""
    if sw not in T._HOL:
        mp.mp.dps = HOL_DPS
        A, B, Tm, _ = T.family_lib().hyperbolic_sl2(sw[0], sw[1:])
        T._HOL[sw] = {"a": T.four_mp(A), "b": T.four_mp(B), "t": T.four_mp(Tm)}
    mp.mp.dps = DPS
    return T._HOL[sw]


T.holonomy = holonomy
MATS = {"L": ((1, 1), (0, 1)), "R": ((1, 0), (1, 1))}


def trace(w):
    A = ((1, 0), (0, 1))
    for c in w:
        B = MATS[c]
        A = tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    return A[0][0] + A[1][1]


def threads(nmax=6):
    """the odd-trace states of GENESIS to length nmax, with either sign"""
    seen, out = set(), []
    for n in range(2, nmax + 1):
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            if "L" not in w or "R" not in w or any(w == w[:d] * (n // d) for d in range(1, n) if n % d == 0):
                continue
            ex = w.translate(str.maketrans("LR", "RL"))
            c = min(min(x[i:] + x[:i] for i in range(n)) for x in (w, ex))
            if c in seen:
                continue
            seen.add(c)
            if trace(c) % 2:
                out += ["+" + c, "-" + c]
    return out


def census(sw, m=4):
    t0 = time.time()
    wl, C = L.tetra_cover(sw)
    s3 = L.level3(sw)
    orbs = L.a4_orbits(sw, C, m)
    rows = []
    for o in orbs:
        c = o["orbit"][0]
        st = T.read_P(s3, C, c[0], c[1], m)["structure"]
        if st["n"] > 0:
            rows.append({"size": len(o["orbit"]), "rep": L.char_list(c), "h1": st["h1"], "r1": st["r1"], "n": st["n"],
                         "m_A": len(C.trivial_cusps(c[0], c[1], m)), "order": T.char_order(c, m)})
    return {"state": sw, "trace": (1 if sw[0] == "+" else -1) * trace(sw[1:]), "cusps": len(C.cusps),
            "characters": sum(len(o["orbit"]) for o in orbs), "orbits": len(orbs),
            "members": sum(r["size"] for r in rows), "member orbits": rows, "s": round(time.time() - t0, 1)}


if __name__ == "__main__":
    if sys.argv[1:] == ["threads"]:
        print(" ".join(threads()))
    else:
        for sw in sys.argv[1:]:
            print(json.dumps(census(sw)), flush=True)
