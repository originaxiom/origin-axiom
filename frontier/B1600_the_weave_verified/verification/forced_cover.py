#!/usr/bin/env python3
"""B1600, addendum (the W6 census control): W3's forced A4 cover built on main from SnapPy's presentation of a thread,
and the sign characters of the four read on it with B1492's stacked instrument -- a control against one cell of the
SM seat's twelve-thread census (docs/dossiers/the_weave_2026-10-07/the_lines_census.json at e8406e52e): on +LR the
forced cover carries 24 sign-character members of the four (two A4 orbits of twelve, each h1 = 1, r1 = 0, n = 1);
on +LLLR none.

The forced cover: among the surjections pi_1(M) -> A4 (enumerated on the generators, relators checked; kernels counted
up to Aut(A4) = S4) the one whose composite to A4/V4 = Z/3 is the thread's own map to Z (the free part of H1) mod 3 --
the fibre to V4, the base element to a third turn (W3).  The cover is SnapPy's cover(perms) on the regular right
action of A4 on itself (twelve sheets); SnapPy composes permutations in word order, which the right action respects.

    python3 forced_cover.py b++LR b++LLLR ...   -> forced_cover_<name>.json beside this file"""
import sys, json, itertools, pathlib
import snappy
import sympy as sp
from sympy.combinatorics import Permutation
from mpmath import mpc
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "B1492_the_three_ended_companion_read" / "verification"))
sys.path.insert(0, str(HERE.parents[1] / "B1493_the_room_on_the_companions" / "verification"))
import multicusp as MC          # noqa: E402
import room as RM               # noqa: E402

# A4 as the even permutations of four points
A4 = [p for p in itertools.permutations(range(4)) if Permutation(list(p)).is_even]
E = tuple(range(4))
mul = lambda p, q: tuple(p[q[i]] for i in range(4))          # (p q)(i) = p(q(i))
inv = lambda p: tuple(sorted(range(4), key=lambda i: p[i]))
PAIRINGS = [frozenset([frozenset([0, 1]), frozenset([2, 3])]), frozenset([frozenset([0, 2]), frozenset([1, 3])]), frozenset([frozenset([0, 3]), frozenset([1, 2])])]


def to_z3(p):
    """A4 -> A4/V4 = Z/3 by the action on the three pairings (0 for V4; 1, 2 for the two classes of third turns)"""
    img = [PAIRINGS.index(frozenset(frozenset(p[i] for i in pair) for pair in P)) for P in PAIRINGS]
    if img == [0, 1, 2]:
        return 0
    return 1 if img == [1, 2, 0] else 2


def word_image(w, img):
    p = E
    for ch in w:
        p = mul(p, img[ch] if ch.islower() else inv(img[ch.lower()]))
    return p


def surjections(G):
    gens, rels = G.generators(), G.relators()
    out = []
    for imgs in itertools.product(A4, repeat=len(gens)):
        img = dict(zip(gens, imgs))
        if all(word_image(r, img) == E for r in rels):
            gen = {E}; fr = [E]
            while fr:
                p = fr.pop()
                for q in imgs:
                    s = mul(p, q)
                    if s not in gen:
                        gen.add(s); fr.append(s)
            if len(gen) == 12:
                out.append(img)
    return out


def kernels_up_to_aut(surjs, gens):
    """two surjections have the same kernel iff they differ by an automorphism of A4 (= conjugation by S4)"""
    S4 = list(itertools.permutations(range(4)))
    keys = set()
    for img in surjs:
        best = min(tuple(mul(mul(s, img[g]), inv(s)) for g in gens) for s in S4)
        keys.add(best)
    return len(keys)


def z_map(G):
    """the map pi_1 -> Z through the free part of H1 (a primitive integer vector on the generators)"""
    gens, rels = G.generators(), G.relators()
    A = sp.Matrix([[sum((1 if ch == g else -1 if ch == g.upper() else 0) for ch in r) for g in gens] for r in rels])
    ns = A.nullspace()
    assert len(ns) == 1, ("b1 != 1", A)
    v = ns[0]; v = v * sp.ilcm(*[sp.fraction(c)[1] for c in v]); g = sp.igcd(*[int(c) for c in v])
    return {gg: int(c) // g for gg, c in zip(gens, v)}


def forced(M):
    G = M.fundamental_group(); gens = G.generators(); eps = z_map(G)
    surjs = surjections(G); nk = kernels_up_to_aut(surjs, gens)
    chosen = []
    for img in surjs:
        for sign in (1, -1):
            if all(to_z3(img[g]) == (sign * eps[g]) % 3 for g in gens):
                chosen.append(img); break
    return G, eps, surjs, nk, chosen


def cover(M, img):
    G = M.fundamental_group()
    perms = [[A4.index(mul(A4[i], img[g])) for i in range(12)] for g in G.generators()]
    return M.cover(perms)


def site_of(N):
    H = N.high_precision(); S = RM.Room.__new__(RM.Room); S.name = N.name(); S.M = H; G = H.fundamental_group()
    S.gens = G.generators(); S.rels = G.relators(); S.cusps = G.peripheral_curves()
    S.rho = {g: MC.matrix([[mpc(MC.num(G.SL2C(g)[i, j].real()), MC.num(G.SL2C(g)[i, j].imag())) for j in range(2)] for i in range(2)]) for g in S.gens}
    S.m = len(S.cusps); return S


def run(name):
    M = snappy.Manifold(name)
    G, eps, surjs, nk, chosen = forced(M)
    out = {"thread": name, "homology": str(M.homology()), "generators": G.generators(), "z_map": eps,
           "A4_surjections": len(surjs), "A4_kernels_up_to_aut": nk, "forced_candidates": len(chosen)}
    ker = {tuple(sorted((g, to_z3(img[g])) for g in G.generators())) for img in chosen}
    N = cover(M, chosen[0])
    out.update({"cover": N.name(), "cover_cusps": N.num_cusps(), "cover_homology": str(N.homology()), "cover_volume_ratio": float(N.volume() / M.volume())})
    S = site_of(N)
    rows = []
    for vals, nu in RM.sign_characters(S):
        c = S.counts(S.four(nu))
        rows.append({"nu": list(vals), "h1": c["a1"], "r1": c["r1"], "n": c["n"], "t0": c["t0"]})
    members = [r for r in rows if r["n"] > 0]
    out.update({"sign_characters": len(rows), "members": len(members), "member_structures": sorted({(r["h1"], r["r1"], r["n"]) for r in members}),
                "trivial_character": next(r for r in rows if all(v == 1 for v in r["nu"])), "rows": rows})
    (HERE / f"forced_cover_{name}.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "rows"}, default=str), flush=True)


if __name__ == "__main__":
    for n in sys.argv[1:]:
        run(n)
