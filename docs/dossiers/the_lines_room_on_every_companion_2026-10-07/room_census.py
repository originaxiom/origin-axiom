#!/usr/bin/env python3
"""The line's room on every companion: n(chi) = h1(N; chi) - r1(chi) at every sign character chi of the fixed-point
companion N of every generated state with at most 12 ends. Exact, two routes, two primes each. Structure only: no
holonomy and no count of the frame.

THE SELECTION RULE AND THE BUDGET (named before the run, in the commit that adds this file):
  - The states: every word in L, R of length 2 to 8 using both letters, primitive, up to rotation and the swap L <-> R, with
    either sign, whose companion has at most 12 ends (|2 - tr phi| <= 12): 27 states.
  - The companion: sm:B1538's fibre-direction cover with the lattice (M - 1) Z^2 and the class wbar whose monodromy fixes
    every puncture (|D| cusps). It is asserted unique for every state.
  - The characters: every character of pi_1 N of order dividing 2, all of them, no sampling.
  - The readings: route P (sm:B1538's punct_present.read on N's own presentation) and route S (Shapiro on M, sm:B1527's
    presentation, Ind chi as signed permutation matrices, M's one cusp read for N's cusps), each over GF(p) for two primes.
    All four readings must agree, or the run stops.
  - The budget: one pass, every character read once per route and prime. A crash is disclosed, and only then is the run
    repeated.
  - What counts: a character with room n(chi) >= 3 is the headline. Theorem C (sm:B1535) then allows three at the order-8
    members over it (b0 = 0, the cap b0 + n(nu^4)). Room 1 and 2 are recorded with the cusp decomposition and the deck
    orbit. n(1) = 0 is read on every companion (main's B1494 states it as a theorem).
  - Seen before the rule was named (a scratch run, 2026-10-07): the four companions of +LLLR (L8a15), -LR (m003's,
    o10_150729), +LLRR (m136's) and -LLRR (m135's). The room is 0 at every sign character except 8 of m135's companion,
    where it is 2. Routes P and S agree at all 312.

    python3 room_census.py            ->  room_census.json beside this file (minutes)"""
import importlib.util
import itertools
import json
import sys
import time
from collections import Counter
from pathlib import Path

import flint

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1538V = ROOT / "frontier" / "B1538_the_puncture_characters" / "verification"
PRIMES = (1000003, 998244353)


def load(alias, path):
    if alias not in sys.modules:
        if str(path.parent) not in sys.path:
            sys.path.append(str(path.parent))
        spec = importlib.util.spec_from_file_location(alias, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[alias] = mod
        spec.loader.exec_module(mod)
    return sys.modules[alias]


PC = load("punct_covers", B1538V / "punct_covers.py")
RP = load("punct_present", B1538V / "punct_present.py")


# ------------------------------------------------------------------------------------------------ the states
def canon(w):
    rots = [w[i:] + w[:i] for i in range(len(w))]
    sw = w.translate(str.maketrans("LR", "RL"))
    rots += [sw[i:] + sw[:i] for i in range(len(sw))]
    return min(rots)


def primitive(w):
    n = len(w)
    return all(w != w[k:] + w[:k] for k in range(1, n) if n % k == 0)


def states(nmax=8, dmax=12):
    out = set()
    for n in range(2, nmax + 1):
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            if "L" in w and "R" in w and primitive(w):
                out.add(canon(w))
    res = []
    for w in sorted(out, key=lambda x: (len(x), x)):
        for sign in "+-":
            (a, b), (c, d_) = PC.State(sign + w).M
            d = abs(2 - (a + d_))
            if d <= dmax:
                res.append((sign + w, d))
    return res


def companion(st, d):
    (a, b), (c, e) = st.M
    cols = [(a - 1, c), (b, e - 1)]
    lats = [L for L in PC.lattices(st.M, d, d) if all(PC.in_lattice(L, v) for v in cols)]
    assert len(lats) == 1, (st.name, lats)
    hits = [C for C in (PC.Cover(st, lats[0], wl) for wl in range(d)) if len(C.cusps) == d]
    assert len(hits) == 1, (st.name, len(hits))
    return lats[0], hits[0]


def deck_action(C, ez, es, m):
    """chi conjugated by u_x for every x in D: (ez', es')"""
    out = {}
    for x in range(C.d):
        ux = C.u[x]
        ez2 = []
        for y in C.gword:
            vec = C.abelian(C.rewrite(PC.inv_word(ux) + y + ux))
            ez2.append(sum(e * v for e, v in zip(ez, vec)) % m)
        k = PC.inv_word(ux) + C.st.phi(C.w + ux + PC.inv_word(C.w))
        vec = C.abelian(C.rewrite(k))
        out[x] = (tuple(ez2), (es + sum(e * v for e, v in zip(ez, vec))) % m)
    return out


# ------------------------------------------------------------------------------------------------ route S, exact
def ind_signs(C, ez, es):
    """Ind chi(g) for g = a, b, t: the permutation x -> x.g and the sign chi(u_x g u_(x.g)^-1) as an exponent mod 2"""
    vals = C.rs_values(ez, es, 2)
    out = {}
    for g in "abt":
        perm = [C.perms[g][x] for x in range(C.d)]
        ex = [C.chi_exp(C.u[x] + g + PC.inv_word(C.u[perm[x]]), vals, 2) for x in range(C.d)]
        out[g] = (perm, ex)
    return out


def _eye(d, p):
    return flint.nmod_mat([[int(i == j) for j in range(d)] for i in range(d)], p)


def _stack(blocks, p, horizontal):
    if horizontal:
        rows = blocks[0].nrows()
        return flint.nmod_mat([[int(B[i, j]) for B in blocks for j in range(B.ncols())] for i in range(rows)], p)
    cols = blocks[0].ncols()
    return flint.nmod_mat([[int(B[i, j]) for j in range(cols)] for B in blocks for i in range(B.nrows())], p)


def _fox(A, Ai, word, d, p):
    """the d x 3d block of z -> z(word) for left cocycles, and the word's matrix"""
    out = [flint.nmod_mat(d, d, p) for _ in range(3)]
    Pre = _eye(d, p)
    for c in word:
        j = "abt".index(c.lower())
        if c.islower():
            out[j] = out[j] + Pre
            Pre = Pre * A[c]
        else:
            Pre = Pre * Ai[c.lower()]
            out[j] = out[j] - Pre
    return _stack(out, p, True), Pre


def read_S(st, C, ez, es, p):
    d = C.d
    A = {}
    for g, (perm, ex) in ind_signs(C, ez, es).items():
        M = [[0] * d for _ in range(d)]
        for x in range(d):
            M[x][perm[x]] = (-1) ** ex[x] % p
        A[g] = flint.nmod_mat(M, p)
    Ai = {g: A[g].inv() for g in "abt"}
    I = _eye(d, p)
    blocks = []
    for r in st.G.rels:
        F, W = _fox(A, Ai, r, d, p)
        assert W == I, "a relator is not 1 in Ind chi"
        blocks.append(F)
    fox = _stack(blocks, p, False)
    h0 = d - _stack([A[g] - I for g in "abt"], p, False).rank()
    h1 = 3 * d - fox.rank() - (d - h0)
    Z, nul = fox.nullspace()
    (F1, W1), (F2, W2) = (_fox(A, Ai, w, d, p) for w in st.G.cusp)
    BP = _stack([W1 - I, W2 - I], p, False)
    if nul:
        Zb = flint.nmod_mat([[int(Z[i, j]) for j in range(nul)] for i in range(3 * d)], p)
        r1 = _stack([BP, _stack([F1, F2], p, False) * Zb], p, True).rank() - BP.rank()
    else:
        r1 = 0
    return {"h1": h1, "r1": r1, "n": h1 - r1}


# ------------------------------------------------------------------------------------------------ the census
def census(sw, d):
    st = PC.State(sw)
    lat, C = companion(st, d)
    Pr = RP.Presentation(C)
    chars = [(ez, es) for ez in C.characters(2) for es in range(2)]
    acts = {c: deck_action(C, c[0], c[1], 2) for c in chars}
    orbit_of, sizes = {}, []
    for c in chars:
        if c not in orbit_of:
            orb = {acts[c][x] for x in range(C.d)}
            assert orb <= set(acts), "a deck image is not a character"
            for x in orb:
                orbit_of[x] = len(sizes)
            sizes.append(len(orb))
    rows = []
    for c in chars:
        reads = [RP.read(Pr, c[0], c[1], 2, p) for p in PRIMES] + [read_S(st, C, c[0], c[1], p) for p in PRIMES]
        key = {(x["h1"], x["r1"], x["n"]) for x in reads}
        assert len(key) == 1, ("the routes or the primes disagree", sw, c, reads)
        h1, r1, n = key.pop()
        triv = C.trivial_cusps(c[0], c[1], 2)
        rows.append({"character": list(c[0]) + [c[1]], "m_A": len(triv), "trivial on cusps": triv, "h1": h1, "r1": r1,
                     "n": n, "deck orbit": orbit_of[c], "orbit size": sizes[orbit_of[c]]})
    trivial = [r for r in rows if not any(r["character"])]
    assert len(trivial) == 1
    hist = Counter((r["m_A"], r["h1"], r["r1"], r["n"], r["orbit size"]) for r in rows)
    return {"state": sw, "ends": d, "lattice": list(lat), "wbar": list(C.wbar), "cusps": len(C.cusps),
            "deck group order": C.d, "sign characters": len(rows), "n(1)": trivial[0]["n"],
            "max room": max(r["n"] for r in rows),
            "room histogram": {str(k): v for k, v in sorted(Counter(r["n"] for r in rows).items())},
            "(m_A, h1, r1, n, orbit size): characters": {str(list(k)): v for k, v in sorted(hist.items())},
            "characters with room": [r for r in rows if r["n"] > 0]}


def main():
    out = {"primes": list(PRIMES), "states": []}
    for sw, d in states():
        t0 = time.time()
        r = census(sw, d)
        r["seconds"] = round(time.time() - t0, 1)
        out["states"].append(r)
        print(sw, "ends", d, "chars", r["sign characters"], "n(1)", r["n(1)"], "max room", r["max room"],
              "rooms", r["room histogram"], f'{r["seconds"]}s', flush=True)
    out["max room over all companions"] = max(s["max room"] for s in out["states"])
    out["companions with room"] = [s["state"] for s in out["states"] if s["max room"] > 0]
    (HERE / "room_census.json").write_text(json.dumps(out, indent=1) + "\n")


if __name__ == "__main__":
    main()
