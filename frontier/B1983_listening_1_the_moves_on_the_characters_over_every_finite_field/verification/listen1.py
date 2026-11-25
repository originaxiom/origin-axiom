"""Listening card 1 (main, 2026-11-25; data-free): the Fricke maps L, R (and, in a second run, the swap P) acting together on
the fibre's characters over F_p for every prime p <= 47 and every leaf kappa = x^2 + y^2 + z^2 - xyz - 2 in F_p: the orbits
of the whole action, their sizes, and the points every move fixes. Exact integer arithmetic. See ../CARD.md.
    python3 -B listen1.py > listen1_run.txt"""
import json, pathlib
from collections import Counter
PRIMES = [p for p in range(2, 48) if all(p % d for d in range(2, int(p ** 0.5) + 1))]
def maps(p, with_P):
    L = lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % p)
    R = lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % p)
    out = [L, R]
    if with_P: out.append(lambda v: (v[1], v[0], v[2]))
    return out
def kappa(v, p): return (v[0] * v[0] + v[1] * v[1] + v[2] * v[2] - v[0] * v[1] * v[2] - 2) % p
def run(p, with_P):
    pts = [(x, y, z) for x in range(p) for y in range(p) for z in range(p)]
    M = maps(p, with_P)
    for f in M: assert len({f(v) for v in pts}) == len(pts)          # each move is a bijection of F_p^3
    assert all(kappa(f(v), p) == kappa(v, p) for f in M for v in pts)  # kappa conserved
    seen, orbits = set(), []
    for v in pts:
        if v in seen: continue
        orb, stack = {v}, [v]
        while stack:
            u = stack.pop()
            for f in M:
                w = f(u)
                if w not in orb: orb.add(w); stack.append(w)
        seen |= orb; orbits.append(orb)
    by = {}
    for o in orbits:
        k = kappa(next(iter(o)), p); by.setdefault(k, []).append(len(o))
    fixed = [v for v in pts if all(f(v) == v for f in M)]
    return by, fixed
res = {}
for with_P in (False, True):
    tag = "L, R, P" if with_P else "L, R"
    print("== the moves %s" % tag)
    for p in PRIMES:
        by, fixed = run(p, with_P)
        cusp = sorted(by.get((-2) % p, []), reverse=True); nothing = sorted(by.get(2 % p, []), reverse=True)
        split = {k: sorted(v, reverse=True) for k, v in by.items() if sum(1 for s in v if s > 1) > 1}
        res["%s|%d" % (tag, p)] = {"orbits_by_kappa": {str(k): sorted(v, reverse=True) for k, v in by.items()}, "fixed": fixed}
        print("p = %2d: cusp leaf (kappa = -2) orbit sizes %s; nothing leaf (kappa = 2) %s; points fixed by every move %s; leaves split into more than one orbit of size > 1: %d of %d %s" % (
            p, cusp[:6] + (["..."] if len(cusp) > 6 else []), nothing[:6] + (["..."] if len(nothing) > 6 else []), fixed,
            len(split), p, sorted(split)[:12]))
    print()
json.dump(res, open(pathlib.Path(__file__).with_name("listen1_run.json"), "w"))
for with_P in (False, True):
    tag = "L, R, P" if with_P else "L, R"
    one = [p for p in PRIMES if p >= 5 and sum(1 for s in res["%s|%d" % (tag, p)]["orbits_by_kappa"].get(str((-2) % p), []) if s > 1) == 1]
    print("SUMMARY (%s) E1: primes p >= 5 whose cusp leaf has exactly one orbit of size > 1: %d of %d %s" % (tag, len(one), len([p for p in PRIMES if p >= 5]), [p for p in PRIMES if p >= 5 and p not in one]))
