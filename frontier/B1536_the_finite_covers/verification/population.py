#!/usr/bin/env python3
"""B1536 -- the sealed population, listed without reading anything (PREREGISTRATION section 5).  Nothing is computed on import.

  - states: m004 = +LR (the golden state) and m003 = -LR (its sister); both have their holonomy over Q(omega);
  - covers: every connected finite cover of degree <= 12 (low_index on sm:B1527's presentation, one per conjugacy class of
    subgroups), and the Q8 tower H_m = K x| <t^m> for m in TOWER (degree 8m);
  - characters: the pulled-back characters nu = (u, kappa), u a fibre character fixed by phi (m004: 1; m003: 5) and
    kappa = nu(t') in mu_{12 L}, L the lcm of the cover's cusp t-periods (Lemma Z'' makes every other kappa count (0, 0));
  - the field for each cover: roots of unity of order N_root = lcm(120, 12 L).

    python3 population.py   ->  prints the population's size (no cohomology is computed)"""
import json
import sys
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cover_lib as CL  # noqa: E402
import gf  # noqa: E402

DMAX = 12
TOWER = (1, 2, 3, 4, 6, 9, 12, 18)


def covers(st):
    """[(cover id, perms)]: 'd<degree>.<k>' for the low-index covers (sorted by canonical form), 'Q8.m<m>' for the tower"""
    G = st["G"]
    low = CL.low_index_covers(G, DMAX)
    keyed = sorted(((len(p["a"]), CL.canonical(p, G.gens), p) for p in low), key=lambda x: (x[0], x[1]))
    out, count = [], {}
    for d, key, p in keyed:
        count[d] = count.get(d, 0) + 1
        out.append((f"d{d}.{count[d]}", p))
    for m in TOWER:
        out.append((f"Q8.m{m}", CL.q8_tower(st["img"], m)))
    return out


def lcm(a, b):
    return a * b // gcd(a, b)


def characters(st, perms):
    """the cover's cusps (with t-periods), L, N_root and the pulled-back characters [(u, kappa)]"""
    cus = CL.cusps(st["G"], perms)
    L = 1
    for c in cus:
        L = lcm(L, c["j0"])
    Nroot = gf.lcm(120, 12 * L)
    us = [(Fr(u[0]), Fr(u[1])) for u in st["fibre characters"]]
    ks = [Fr(k, 12 * L) for k in range(12 * L)]
    return cus, L, Nroot, [(u, k) for u in us for k in ks]


def main():
    tot = {}
    for name in ("m004", "m003"):
        st = CL.state(name)
        cv = covers(st)
        n_chars, big = 0, []
        for cid, p in cv:
            cus, L, Nr, chars = characters(st, p)
            n_chars += len(chars)
            big.append((cid, len(p["a"]), len(cus), L, len(chars)))
        tot[name] = {"covers": len(cv), "characters": n_chars,
                     "largest": sorted(big, key=lambda x: -x[4])[:5]}
        print(name, json.dumps(tot[name]))
    return tot


if __name__ == "__main__":
    main()
