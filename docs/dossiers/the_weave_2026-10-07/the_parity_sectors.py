#!/usr/bin/env python3
"""R2 of the weave's laws (docs/THE_WEAVES_LAWS.md), in Theorem S's sense: the design-time structure census (no count) of
what the three parities carry at the tick where the weave's cover separates them, on every state at once.

The rule, named before the run:
- every state of GENESIS (a primitive word in L and R with both letters, up to rotation and the exchange of L and R,
  with either sign) of length at most 6: 24 states;
- on each, its resolving tick k, the order of phi mod 2 (3 at odd trace, 2 when phi mod 2 is an involution, 1 when
  phi = I mod 2), and the state at that tick, monodromy (eps w)^k;
- every character of that tick's group of order dividing m = 12 whose restriction to the fibre is a parity: the three
  non-zero parities (1/2, 0), (0, 1/2), (1/2, 1/2), and the zero parity as a reference, each with the twelve values on
  the stable letter: 48 characters per state;
- at each, the structure (h1, r1, n) of nu (x) rho in route P (sm:B1549's read_P, on the degree-one cover of the tick,
  the banked library unchanged, its precision raised from here as in the_lines_census.py), and m_A.
A member is a character with n > 0. The budget: one pass.

The control, banked: sm:B1530 on the silver pair at their own tick (k = 1).
- m135 = -LLRR at kappa = 1: members at (0, 1/2) and (1/2, 0) with h1 = 2 and one interior class (non-simple), and a
  simple member at (1/2, 1/2).
- m136 = +LLRR at kappa = -1: members at (0, 1/2) and (1/2, 0), none at (1/2, 1/2).

    python3 the_parity_sectors.py STATE ...   ->  one JSON line per state on stdout
    python3 the_parity_sectors.py states      ->  the 24 states"""
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
PC = L.PC
HOL_DPS, DPS = 160, 100
T.DPS = DPS
M = 12
PARITIES = {"zero": (0, 0), "(1/2, 0)": (1, 0), "(0, 1/2)": (0, 1), "(1/2, 1/2)": (1, 1)}


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


def matrix(w):
    A = ((1, 0), (0, 1))
    for c in w:
        B = MATS[c]
        A = tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    return A


def resolving_tick(w):
    """the order of the word's matrix mod 2 (the sign is the identity mod 2)"""
    a = tuple(tuple(x % 2 for x in r) for r in matrix(w))
    X, k = a, 1
    while X != ((1, 0), (0, 1)):
        X = tuple(tuple(sum(X[i][l] * a[l][j] for l in range(2)) % 2 for j in range(2)) for i in range(2))
        k += 1
    return k


def states(nmax=6):
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
            out += ["+" + c, "-" + c]
    return out


def census(sw, m=M):
    t0 = time.time()
    w = sw[1:]
    k = resolving_tick(w)
    sign = sw[0] if k % 2 else "+"
    swk = sign + w * k
    C = PC.Cover(PC.State(swk), (1, 0, 1), 0)
    assert C.d == 1 and C.gword == ["a", "b"] and len(C.cusps) == 1, (sw, C.gword)
    invariant = {tuple(ez) for ez in C.characters(m)}
    rows = []
    for name, (pa, pb) in PARITIES.items():
        ez = ((m // 2) * pa, (m // 2) * pb)
        assert ez in invariant, ("the parity does not extend to the tick", sw, name)
        for es in range(m):
            st = T.read_P(swk, C, ez, es, m)["structure"]
            rows.append({"parity": name, "kappa": f"{es}/{m}", "h1": st["h1"], "r1": st["r1"], "n": st["n"],
                         "m_A": len(C.trivial_cusps(ez, es, m))})
    members = [r for r in rows if r["n"] > 0]
    by_parity = {name: [r["kappa"] for r in members if r["parity"] == name] for name in PARITIES}
    return {"state": sw, "trace": (1 if sw[0] == "+" else -1) * (matrix(w)[0][0] + matrix(w)[1][1]),
            "resolving tick": k, "the tick's state": swk, "members": len(members), "members by parity": by_parity,
            "readings": rows, "s": round(time.time() - t0, 1)}


if __name__ == "__main__":
    if sys.argv[1:] == ["states"]:
        print(" ".join(states()))
    else:
        for sw in sys.argv[1:]:
            print(json.dumps(census(sw)), flush=True)
