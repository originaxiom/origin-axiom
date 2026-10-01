"""B1508 -- the audit lane's partial-filling witness (its PARTIAL_FILLING.md, 2026-09-07; main's L202(b)) recomputed with own code.

A degree-5 cover of m004 with three cusps; filling cusp 0 along the slope (2, 1) leaves two complete cusps and a chiral hyperbolic
manifold.  Three things are checked here:
  (i)   the witness: the cover, the filling, the volume, CS and the symmetry group (numerical, SnapPy; the audit lane's interval
        certificate needs Sage and is cited, not rerun);
  (ii)  the descent of flat data along a filling (R57): pi1(M(s)) = pi1(M)/<<s>>, so a representation descends iff it kills s; its
        abelian shadow, H1(M(s)) = H1(M)/<[s]>, is checked by Smith normal form;
  (iii) the peripheral ranks (B1368/B1369's free-cusp criterion) on the witness and, as a control, on m004's degree-5 covers.
        Item (iii) on the witness was computed without a seal: a fact about one manifold, not a test of any hypothesis.
"""
import json
import sys
from pathlib import Path

import snappy
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

TRI = "kLLLPLQkcefegijjiijiieldllxtxa_aBbBabBbbacb"
SLOPE = (2, 1)


def _vec(gens, word):
    v = [0] * len(gens)
    for ch in word:
        v[gens.index(ch.lower())] += 1 if ch.islower() else -1
    return v


def peripheral_ranks(P):
    """b1 and, per cusp, the rank of the image of H1(T_c; Q) in H1(M; Q); a cusp is free iff its rank is below b1"""
    G = P.fundamental_group()
    gens = G.generators()
    rels = [_vec(gens, r) for r in G.relators()]
    R = sp.Matrix(rels) if rels else sp.zeros(0, len(gens))
    rr = R.rank() if rels else 0
    b1 = len(gens) - rr
    ranks = []
    for mu, lam in G.peripheral_curves():
        S = sp.Matrix.vstack(R, sp.Matrix([_vec(gens, mu), _vec(gens, lam)])) if rels else sp.Matrix([_vec(gens, mu), _vec(gens, lam)])
        ranks.append(int(S.rank() - rr))
    return b1, ranks


def _invariants(M):
    """the abelian invariants of Z^n / rowspace(M), as a sorted list (0 = a free summand)"""
    n = M.shape[1]
    D = smith_normal_form(M, domain=sp.ZZ)
    diag = [abs(int(D[i, i])) for i in range(min(D.shape))]
    nonzero = [d for d in diag if d != 0]
    free = n - len(nonzero)
    return sorted([d for d in nonzero if d != 1]) + [0] * free


def witness():
    M = snappy.Manifold(TRI)
    base = snappy.Manifold("m004")
    hits = []
    for i, C in enumerate(base.covers(5)):
        if C.num_cusps() == M.num_cusps() and C.is_isometric_to(M):
            hits.append({"index": i, "type": C.cover_info()["type"], "degree": C.cover_info()["degree"]})
    F = M.copy()
    F.dehn_fill(SLOPE, 0)
    P = F.filled_triangulation()
    cs = float(F.chern_simons())
    G = P.symmetry_group()
    return {
        "cusps": M.num_cusps(), "tets": M.num_tetrahedra(), "H1": str(M.homology()),
        "vol_ratio": round(float(M.volume() / base.volume()), 10), "m004_covers_isometric": hits,
        "filled_cusps": P.num_cusps(), "filled_solution": F.solution_type(), "filled_volume": round(float(F.volume()), 9),
        "filled_cs": round(cs, 12), "cs_distance_from_mirror_classes": round(min(abs(cs % 0.5 - x) for x in (0, 0.25, 0.5)), 9),
        "filled_symmetry_group": str(G), "filled_amphicheiral": bool(G.is_amphicheiral()), "filled_H1": str(P.homology()),
    }


def descent():
    """H1(M(s)) = H1(M)/<[s]>: the abelian shadow of the exact filling transport pi1(M(s)) = pi1(M)/<<s>>"""
    M = snappy.Manifold(TRI)
    G = M.fundamental_group()
    gens = G.generators()
    rels = [_vec(gens, r) for r in G.relators()]
    mu, lam = G.peripheral_curves()[0]
    s = [SLOPE[0] * a + SLOPE[1] * b for a, b in zip(_vec(gens, mu), _vec(gens, lam))]
    before = _invariants(sp.Matrix(rels))
    after = _invariants(sp.Matrix(rels + [s]))
    F = M.copy()
    F.dehn_fill(SLOPE, 0)
    snappy_after = str(F.filled_triangulation().homology())
    return {"H1_M": before, "H1_M_mod_s": after, "snappy_H1_filled": snappy_after,
            "agree": after == [0, 0] and snappy_after == "Z + Z"}


def ranks():
    M = snappy.Manifold(TRI)
    F = M.copy()
    F.dehn_fill(SLOPE, 0)
    P = F.filled_triangulation()
    b1w, rw = peripheral_ranks(P)
    b1u, ru = peripheral_ranks(M)
    control = []
    for i, C in enumerate(snappy.Manifold("m004").covers(5)):
        b1, r = peripheral_ranks(C)
        control.append({"index": i, "cusps": C.num_cusps(), "b1": b1, "ranks": r, "free": [x < b1 for x in r]})
    return {"unfilled": {"b1": b1u, "ranks": ru, "free": [x < b1u for x in ru]},
            "filled": {"b1": b1w, "ranks": rw, "free": [x < b1w for x in rw]},
            "m004_degree5_covers": control}


def main():
    return {"witness": witness(), "descent": descent(), "ranks": ranks()}


if __name__ == "__main__":
    res = main()
    out = json.dumps(res, indent=1, sort_keys=True)
    print(out)
    if "--record" in sys.argv:
        (Path(__file__).with_name("partial_filling_run.txt")).write_text(out + "\n", encoding="utf-8")
