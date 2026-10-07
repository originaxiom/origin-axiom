#!/usr/bin/env python3
"""B1494 (second route, added after the seal and disclosed): the fixed-point companion built DIRECTLY as the regular cover
with deck group T = H1(M) / <peripheral subgroup> -- the quotient of Z^gens by the rows of the relators' and the peripheral
words' exponent-sum matrix (Smith normal form with transforms) -- through SnapPy's cover(perms) with the regular action of T
on itself.  For an abelian deck group the left/right convention (B1490) does not matter.  Cross-checked against the
enumeration route (companions.py) wherever both ran.  Usage: companion_direct.py +LLLR -LR ...  or --census MAXLEN TMAX"""
import sys, json, pathlib, itertools, math
import snappy, sympy
from sympy.matrices.normalforms import smith_normal_decomp
HERE = pathlib.Path(__file__).resolve().parent


def bundle_name(state): return "b+" + ("+" if state[0] == "+" else "-") + state[1:]


def exp_vec(w, gens): return [sum((1 if ch.islower() else -1) for ch in w if ch.lower() == g) for g in gens]


def deck_map(M):
    """gens -> T = coker(E'), E' the exponent matrix of relators and peripheral words; returns (orders d_i, images of the
    generators as tuples in prod Z/d_i), using S = U E' V (Smith): the quotient Z^gens / rowspace(E') is read in the basis V"""
    G = M.fundamental_group(); gens = G.generators()
    rows = [exp_vec(r, gens) for r in G.relators()] + [exp_vec(w, gens) for ml in G.peripheral_curves() for w in ml]
    E = sympy.Matrix(rows); S, U, V = smith_normal_decomp(E, sympy.ZZ)        # S = U * E * V
    # coker(E) = Z^gens / rowspace(E); in the new column basis (coordinates y = V^-1 x ... rows of E*V = U^-1 S): Z^gens/rowspace(E V) = prod Z/S_ii
    # the class of the standard basis vector e_j (generator j) is the j-th row of V^-1... we need coordinates of e_j in the basis where rowspace is diagonal:
    # rowspace(E) V = rowspace(S) up to U (unimodular), so x -> x V sends rowspace(E) onto rowspace(S); the image of e_j is row j of V.
    n = len(gens); d = [int(S[i, i]) if i < min(S.shape) else 0 for i in range(n)]
    imgs = []
    for j in range(n):
        v = [int(x) for x in V.row(j)] if V.shape[0] == n else [int(x) for x in V[j, :]]
        imgs.append(tuple((v[i] % d[i]) if d[i] else v[i] for i in range(n)))
    # T is the torsion part: coordinates i with d_i > 1 (d_i = 1 are trivial, d_i = 0 are free -- the free part must be absent for the peripheral quotient of a state)
    tors = [i for i in range(n) if d[i] > 1]; free = [i for i in range(n) if d[i] == 0]
    assert not free, ("the quotient by the peripheral subgroup has a free part", d)
    return gens, [d[i] for i in tors], [tuple(im[i] for i in tors) for im in imgs]


def companion_direct(state):
    M = snappy.Manifold(bundle_name(state)); gens, ds, imgs = deck_map(M); T = math.prod(ds) if ds else 1
    if T == 1: C = M
    else:
        elems = list(itertools.product(*[range(x) for x in ds])); idx = {e: i for i, e in enumerate(elems)}
        perms = []
        for im in imgs:        # the regular action: t -> t + im(g)
            perms.append([idx[tuple((e[i] + im[i]) % ds[i] for i in range(len(ds)))] for e in elems])
        C = M.cover(perms)
    H = C.homology()
    return dict(state=state, T=T, deck=ds, cusps=C.num_cusps(), H1=str(H), b1=H.betti_number(), b1_minus_ends=H.betti_number() - T,
                volume_ratio=float(C.volume() / M.volume()), sym=C.symmetry_group().order() if T <= 16 else None, isosig=C.triangulation_isosig())


if __name__ == "__main__":
    out = []
    if sys.argv[1] == "--census":
        maxlen, tmax = int(sys.argv[2]), int(sys.argv[3])
        sys.path.insert(0, str(HERE.parents[1] / "B1434_the_architecture_census" / "verification"))
        import architecture_census as ac
        for w in ac.states(maxlen):
            for eps in "+-":
                M = snappy.Manifold(bundle_name(eps + w)); gens, ds, imgs = deck_map(M); T = math.prod(ds) if ds else 1
                if T > tmax: continue
                r = companion_direct(eps + w); out.append(r); print(r["state"], "|T| =", r["T"], "deck", r["deck"], "cusps", r["cusps"], "H1", r["H1"], "b1 - ends", r["b1_minus_ends"], "vol ratio", round(r["volume_ratio"], 6), flush=True)
        json.dump(out, open(HERE / f"companions_direct_len{maxlen}_T{tmax}.json", "w"), indent=1)
        print("states", len(out), "all b1 = ends:", all(r["b1_minus_ends"] == 0 and r["cusps"] == r["T"] for r in out))
    else:
        for st in sys.argv[1:]:
            r = companion_direct(st); out.append(r); print(json.dumps(r, indent=1))
