"""P-229, GENESIS §5 and FK9: main's own check of the SM seat's sm:B1523 (the flexible states).

  mirror:   the 758 word states to length 12 fall into 536 manifolds (isometry signatures); on 262 of them no isometry
            inverts the fibre boundary (131 per sign; 220 chiral, 42 whose orientation-reversing symmetries keep it).
            The fibre boundary is the homological longitude (b1 = 1, the fibre a Seifert surface).
  rigidity: in rigidity_mp.py (60 digits).  A first float64 route in this file miscounted ranks and was voided before
            the census was read as a result (FINDINGS, Disclosed); it is not kept.
Written from the seat's read-out (its verdict and section 0), not its scripts.
"""
import sys, json, itertools, pathlib
import numpy as np
import snappy

HERE = pathlib.Path(__file__).resolve().parent


def word_states(maxlen=12):
    seen = set(); out = []
    def cyc_min(w): return min(w[i:] + w[:i] for i in range(len(w)))
    def swap(w): return w.translate(str.maketrans("LR", "RL"))
    def primitive(w): return all(w != w[:d] * (len(w) // d) for d in range(1, len(w)) if len(w) % d == 0)
    for n in range(2, maxlen + 1):
        for p in itertools.product("LR", repeat=n):
            w = "".join(p)
            if len(set(w)) < 2 or not primitive(w): continue
            key = min(cyc_min(w), cyc_min(swap(w)))
            if key in seen: continue
            seen.add(key); out.append(key)
    return [eps + w for w in out for eps in "+-"]


def hom_longitude(M):
    """the primitive peripheral class that dies in H1(M; Q) (b1 = 1, one cusp): (a, b) in SnapPy's (meridian, longitude)"""
    from fractions import Fraction
    import math
    G = M.fundamental_group(); gens = G.generators(); g = len(gens)
    def ab(word):
        v = [0] * g
        for ch in word:
            if ch.islower(): v[gens.index(ch)] += 1
            else: v[gens.index(ch.lower())] -= 1
        return v
    R = [ab(r) for r in G.relators()]
    # phi: a rational functional vanishing on the relators (unique up to scale when b1 = 1)
    import sympy
    ns = sympy.Matrix(R).nullspace() if R else [sympy.eye(g)[:, 0]]
    assert len(ns) == 1, len(ns)
    phi = list(ns[0])
    m, l = G.peripheral_curves()[0]
    pm = sum(a * b for a, b in zip(phi, ab(m))); pl = sum(a * b for a, b in zip(phi, ab(l)))
    a, b = sympy.Rational(pl), -sympy.Rational(pm)
    den = sympy.ilcm(sympy.fraction(a)[1], sympy.fraction(b)[1]); a, b = int(a * den), int(b * den)
    gg = math.gcd(a, b); a, b = a // gg, b // gg
    return (a, b)


def mirror():
    states = word_states()
    mans = {}
    for s in states:
        M = snappy.Manifold("b+" + s)
        sig = M.isometry_signature()
        mans.setdefault(sig, []).append(s)
    rows = []
    for sig, sts in mans.items():
        M = snappy.Manifold("b+" + sts[0])
        hl = hom_longitude(M)
        isos = M.is_isometric_to(M, return_isometries=True)
        inv = False; orev = False
        for I in isos:
            A = np.array(I.cusp_maps()[0].list(), dtype=int).reshape(2, 2)
            if round(np.linalg.det(A)) < 0: orev = True
            img = A @ np.array(hl)
            if tuple(img) == tuple(-np.array(hl)): inv = True
        rows.append(dict(states=sts, sign=sts[0][0], n_isom=len(isos), orientation_reversing=orev,
                         longitude_inverting=inv))
    broken = [r for r in rows if not r["longitude_inverting"]]
    out = dict(states=len(states), manifolds=len(rows), mirror_broken=len(broken),
               broken_by_sign={e: sum(1 for r in broken if r["sign"] == e) for e in "+-"},
               broken_chiral=sum(1 for r in broken if not r["orientation_reversing"]),
               broken_with_orientation_reversing=sum(1 for r in broken if r["orientation_reversing"]),
               states_on_broken=sum(len(r["states"]) for r in broken))
    # by length: the shortest word of each broken manifold
    bylen = {}
    for r in broken:
        L = min(len(s) - 1 for s in r["states"]); bylen[L] = bylen.get(L, 0) + 1
    out["broken_by_length_manifolds"] = dict(sorted(bylen.items()))
    print(out)
    json.dump(dict(summary=out, manifolds=rows), open(HERE / "main_b1523_mirror.json", "w"), indent=0)

if __name__ == "__main__":
    if sys.argv[1] == "mirror": mirror()
