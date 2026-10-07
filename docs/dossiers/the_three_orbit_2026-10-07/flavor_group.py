#!/usr/bin/env python3
"""The three-orbit's flavor group (structure only: no holonomy, no count). On +LLLR's companion L8a15, for every free deck
orbit of characters chi of order dividing m (m = 2 and 4), the image of pi_1(+LLLR) under the induced representation
Ind chi (Ind chi(g)_{x,y} = chi(u_x g u_y^-1), y = x.g), exactly: monomial 3 x 3 matrices with entries in mu_m, stored as
(permutation, exponents mod m). For each image G:
  - its order, centre and derived group; its element orders; sum |tr|^2 / |G| (1 iff Ind chi is irreducible);
  - G n SL_3 with its order, centre, derived group and element orders;
  - the image of M's cusp group <l, t'> and of the generators a, b, t;
  - the orbit's ends (m_A) and the character's order.

    python3 flavor_group.py   ->  flavor_group.json beside this file (seconds)"""
import cmath
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1538V = ROOT / "frontier" / "B1538_the_puncture_characters" / "verification"


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


def companion(st, d):
    (a, b), (c, e) = st.M
    cols = [(a - 1, c), (b, e - 1)]
    lats = [L for L in PC.lattices(st.M, d, d) if all(PC.in_lattice(L, v) for v in cols)]
    assert len(lats) == 1
    hits = [C for C in (PC.Cover(st, lats[0], wl) for wl in range(d)) if len(C.cusps) == d]
    assert len(hits) == 1
    return hits[0]


def deck_action(C, ez, es, m):
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


# ------------------------------------------------------------------------------------------------ monomial groups
def mul(A, B, m):
    (pa, ea), (pb, eb) = A, B
    n = len(pa)
    return (tuple(pb[pa[x]] for x in range(n)), tuple((ea[x] + eb[pa[x]]) % m for x in range(n)))


def inv(A, m):
    p, e = A
    q, f = [0] * len(p), [0] * len(p)
    for x in range(len(p)):
        q[p[x]], f[p[x]] = x, (-e[x]) % m
    return (tuple(q), tuple(f))


def ident(n):
    return (tuple(range(n)), (0,) * n)


def closure(gens, m):
    one = ident(len(gens[0][0]))
    G, frontier = {one}, [one]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = mul(x, g, m)
                if y not in G:
                    G.add(y)
                    nxt.append(y)
        frontier = nxt
    return G


def order_of(x, m):
    one, k, y = ident(len(x[0])), 1, x
    while y != one:
        y, k = mul(y, x, m), k + 1
    return k


def perm_sign(p):
    s, seen = 1, set()
    for i in range(len(p)):
        if i not in seen:
            j, L = i, 0
            while j not in seen:
                seen.add(j)
                j, L = p[j], L + 1
            s *= -1 if L % 2 == 0 else 1
    return s


def is_det_one(x, m):
    """det = sign(p) * z_m^(sum e) = 1"""
    tot = sum(x[1]) % m
    return (perm_sign(x[0]) == 1 and tot == 0) or (perm_sign(x[0]) == -1 and m % 2 == 0 and tot == m // 2)


def invariants(G, m):
    G = list(G)
    Z = [z for z in G if all(mul(z, g, m) == mul(g, z, m) for g in G)]
    comms = {mul(mul(inv(x, m), inv(y, m), m), mul(x, y, m), m) for x in G for y in G}
    D = closure(list(comms), m)
    return {"order": len(G), "centre": len(Z), "derived": len(D),
            "element orders": {str(k): v for k, v in sorted(Counter(order_of(x, m) for x in G).items())}}


def word_elt(I, w, m, d):
    X = ident(d)
    for c in w:
        X = mul(X, I[c] if c.islower() else inv(I[c.lower()], m), m)
    return X


def ind(C, ez, es, m):
    vals = C.rs_values(ez, es, m)
    out = {}
    for g in "abt":
        perm = tuple(C.perms[g][x] for x in range(C.d))
        ex = tuple(C.chi_exp(C.u[x] + g + PC.inv_word(C.u[perm[x]]), vals, m) for x in range(C.d))
        out[g] = (perm, ex)
    return out


def char_order(c, m):
    for k in range(1, m + 1):
        if m % k == 0 and all((e * k) % m == 0 for e in c[0]) and (c[1] * k) % m == 0:
            return k


def analyse(sw="+LLLR", d=3, m=2):
    st = PC.State(sw)
    C = companion(st, d)
    chars = [(ez, es) for ez in C.characters(m) for es in range(m)]
    acts = {c: deck_action(C, c[0], c[1], m) for c in chars}
    seen, rows = set(), []
    for c in chars:
        if c in seen:
            continue
        orb = sorted({acts[c][x] for x in range(C.d)})
        seen |= set(orb)
        if len(orb) < C.d:
            continue
        I = ind(C, orb[0][0], orb[0][1], m)
        for r in st.G.rels:
            assert word_elt(I, r, m, C.d) == ident(C.d), "Ind chi is not a representation"
        G = closure(list(I.values()), m)
        tr2 = sum(abs(sum(cmath.exp(2j * cmath.pi * x[1][i] / m) for i in range(C.d) if x[0][i] == i)) ** 2 for x in G)
        G1 = [x for x in G if is_det_one(x, m)]
        cusp = [word_elt(I, w, m, C.d) for w in st.G.cusp]
        rows.append({"orbit": [list(o[0]) + [o[1]] for o in orb], "character order": char_order(orb[0], m),
                     "ends where trivial (m_A)": len(C.trivial_cusps(orb[0][0], orb[0][1], m)),
                     "G": invariants(G, m), "sum |tr|^2 / |G|": round(tr2 / len(G), 9),
                     "G n SL3": invariants(G1, m),
                     "generators (permutation, exponents mod m)": {g: [list(v[0]), list(v[1])] for g, v in I.items()},
                     "cusp words": list(st.G.cusp), "cusp images": [[list(x[0]), list(x[1])] for x in cusp],
                     "cusp image": invariants(closure(cusp, m), m)})
    return rows


def main():
    out = {}
    for m in (2, 4):
        out[f"m = {m}"] = analyse("+LLLR", 3, m)
        for r in out[f"m = {m}"]:
            print(m, r["orbit"], "order", r["character order"], "m_A", r["ends where trivial (m_A)"], "|G|", r["G"]["order"],
                  "Z", r["G"]["centre"], "[G,G]", r["G"]["derived"], "irr", r["sum |tr|^2 / |G|"], "|G n SL|",
                  r["G n SL3"]["order"], r["G n SL3"]["element orders"], "cusp", r["cusp image"]["order"], flush=True)
    (HERE / "flavor_group.json").write_text(json.dumps(out, indent=1) + "\n")


if __name__ == "__main__":
    main()
