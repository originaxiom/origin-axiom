#!/usr/bin/env python3
"""The three-orbit: structure only, no count at any class.

On +LLLR's companion (the unique degree-3 cover of the punctured-torus bundle +LLLR with three cusps; SnapPy identifies
it with L8a15), list the eight sign characters, the ends on which each is trivial, and how the order-3 isometries that
cycle the three ends (the deck transformations over +LLLR among them) permute the characters. Also the uniqueness of
trace 5 among the states: for a positive word in L and R of length n using both letters the trace is at least n + 1,
attained by L^(n-1) R, so trace 5 needs n <= 4, and among the words of length at most 4 only LLLR (up to rotation and
the L <-> R swap) has trace 5.

    python3 three_orbit.py   ->  three_orbit.json beside this file (a minute)"""
import itertools
import json
from pathlib import Path

import snappy
from sympy import Matrix

HERE = Path(__file__).resolve().parent
L = Matrix([[1, 0], [1, 1]])
R = Matrix([[1, 1], [0, 1]])


def words(n):
    for w in itertools.product("LR", repeat=n):
        if "L" in w and "R" in w:
            yield "".join(w)


def trace(w):
    A = Matrix.eye(2)
    for ch in w:
        A = A * (L if ch == "L" else R)
    return int(A.trace())


def canon(w):
    rots = [w[i:] + w[:i] for i in range(len(w))]
    sw = w.translate(str.maketrans("LR", "RL"))
    rots += [sw[i:] + sw[:i] for i in range(len(sw))]
    return min(rots)


def main():
    rec = {}
    by_len = {}
    for n in range(2, 9):
        tr = {}
        for w in words(n):
            tr.setdefault(canon(w), trace(w))
        by_len[n] = {"least trace": min(tr.values()), "words of trace 5": sorted(w for w, t in tr.items() if t == 5)}
    rec["traces of positive words by length"] = by_len
    M = snappy.Manifold("b++LLLR")
    covers = [C for C in M.covers(3) if C.num_cusps() == 3]
    C = covers[0]
    rec["state"] = {"name": "b++LLLR", "H1": str(M.homology()), "cusps": M.num_cusps()}
    rec["degree-3 covers with three cusps"] = len(covers)
    rec["companion"] = {"H1": str(C.homology()), "census names": [str(x).split("(")[0] for x in C.identify()],
                        "isometric to L8a15": bool(snappy.Manifold("L8a15").is_isometric_to(C))}
    G = C.fundamental_group()
    gens = list(G.generators())

    def vec(w):
        v = [0] * len(gens)
        for ch in w:
            v[gens.index(ch.lower())] += 1 if ch.islower() else -1
        return v

    rel = [vec(r) for r in G.relators()]
    per = [(vec(m), vec(lo)) for (m, lo) in G.peripheral_curves()]
    chars = [e for e in itertools.product((0, 1), repeat=len(gens))
             if all(sum(a * b for a, b in zip(e, r)) % 2 == 0 for r in rel)]

    def val(e, v):
        return sum(a * b for a, b in zip(e, v)) % 2

    pv = {e: tuple(val(e, v) for pair in per for v in pair) for e in chars}
    assert len(set(pv.values())) == len(chars), "characters not determined by their peripheral values"
    inv = {v: e for e, v in pv.items()}

    def trivial_ends(e):
        return [i for i in range(len(per)) if pv[e][2 * i] == 0 and pv[e][2 * i + 1] == 0]

    iso = C.is_isometric_to(C, return_isometries=True)
    cyc = [f for f in iso if sorted(f.cusp_images()) == [0, 1, 2] and all(f.cusp_images()[i] != i for i in range(3))]

    def pull(e, f):
        p, maps, out = f.cusp_images(), f.cusp_maps(), []
        for i in range(3):
            j, A = p[i], f.cusp_maps()[i]
            mj, lj = pv[e][2 * j], pv[e][2 * j + 1]
            out += [(A[0][0] * mj + A[1][0] * lj) % 2, (A[0][1] * mj + A[1][1] * lj) % 2]
        return inv[tuple(out)]

    orbit_sets = set()
    for f in cyc:
        perm = {e: pull(e, f) for e in chars}
        seen, orbits = set(), []
        for e in chars:
            if e in seen:
                continue
            orb, x = [], e
            while x not in orb:
                orb.append(x)
                x = perm[x]
            seen |= set(orb)
            orbits.append(tuple(sorted(orb)))
        orbit_sets.add(tuple(sorted(orbits)))
    assert len(orbit_sets) == 1, "the end-cycling isometries do not share their orbits"
    orbits = sorted(orbit_sets.pop(), key=len)
    rec["sign characters"] = len(chars)
    rec["isometries"] = len(iso)
    rec["isometries cycling the three ends"] = len(cyc)
    rec["orbits (characters as values on the generators; the ends each is trivial on)"] = [
        [{"character": "".join(map(str, e)), "trivial on ends": trivial_ends(e)} for e in orb] for orb in orbits]
    (HERE / "three_orbit.json").write_text(json.dumps(rec, indent=1) + "\n")
    print(json.dumps({k: rec[k] for k in ("degree-3 covers with three cusps", "companion", "sign characters",
                                          "isometries cycling the three ends")}))
    for orb in rec["orbits (characters as values on the generators; the ends each is trivial on)"]:
        print(orb)
    print({n: v for n, v in by_len.items()})


if __name__ == "__main__":
    main()
