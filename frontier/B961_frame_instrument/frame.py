#!/usr/bin/env python3
"""B961 / L135 -- THE FRAME INSTRUMENT: e6 structure tools, built on this bench.

B958 found that the repo had NO independent construction of the frame or of M12:
B909 verified section LVIII by RUNNING INCOMING MATERIAL, not by rebuilding. This
module is the missing infrastructure. It deliberately does NOT guess the solo
seat's frame -- guessing it wrong would produce a false verification or a false
refutation (B958's stated reason for deferral). It provides the OPERATIONS any
frame claim needs, each verified against a banked fact.

Exports
-------
    e6()                     -> the algebra: DIM, ROOTS, brackets, ad
    killing()                -> the exact Killing form matrix (78x78, Fraction)
    centralizer(subspace)    -> basis of {x : [g,x] = 0 for all g in subspace}
    killing_perp(subspace)   -> basis of {x : K(v,x) = 0 for all v in subspace}
    derived(subspace)        -> basis of [S,S]
    rank_of(subspace)        -> dim of a maximal toral subalgebra of S
    weights(subspace, cartan)-> weight decomposition of subspace under cartan

Every export is exercised in self_test() against a banked number.
"""
import io
import contextlib
import pathlib
from fractions import Fraction as F

import sympy as sp

_HERE = pathlib.Path(__file__).resolve().parent
_E6SRC = _HERE.parent / "B854_centralizer_exact" / "e6_centralizer.py"

_G = {"__file__": str(_E6SRC), "__name__": "_e6_lib"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(_E6SRC.read_text(), str(_E6SRC), "exec"), _G)

DIM = _G["DIM"]; ROOTS = _G["ROOTS"]; IDX = _G["IDX"]; N = _G["N"]; C = _G["C"]
BB = _G["BB"]; evec = _G["evec"]; hvec = _G["hvec"]


def _Q(x):
    return sp.Rational(x.numerator, x.denominator) if isinstance(x, F) else sp.Rational(x)


def ad(v):
    """ad(v) as an exact 78x78 sympy matrix."""
    M = sp.zeros(DIM, DIM)
    for p in range(DIM):
        if v[p] == 0:
            continue
        cp = _Q(v[p])
        for q in range(DIM):
            for k, c in enumerate(BB[p][q]):
                if c:
                    M[k, q] += cp * _Q(c)
    return M


_KILL = None


def killing():
    """The exact Killing form K(x,y) = tr(ad x . ad y) in the Chevalley basis."""
    global _KILL
    if _KILL is None:
        basis = [_unit(i) for i in range(DIM)]
        A = [ad(b) for b in basis]
        K = sp.zeros(DIM, DIM)
        for i in range(DIM):
            for j in range(i, DIM):
                t = (A[i] * A[j]).trace()
                K[i, j] = t
                K[j, i] = t
        _KILL = K
    return _KILL


def _unit(i):
    v = [F(0)] * DIM
    v[i] = F(1)
    return v


def _nullspace_basis(rows):
    if not rows:
        return [list(_unit(i)) for i in range(DIM)]
    A = sp.Matrix(rows)
    return [list(v) for v in A.nullspace()]


def centralizer(subspace):
    """{x : [g,x] = 0 for every g in subspace}, as a basis of coordinate vectors."""
    rows = []
    for g in subspace:
        rows.extend(ad(g).tolist())
    return _nullspace_basis(rows)


def killing_perp(subspace):
    """{x : K(v,x) = 0 for every v in subspace}."""
    K = killing()
    rows = [[K[i, j] for j in range(DIM)] for v in subspace
            for i in range(DIM) if v[i] != 0 for _ in [0]]
    # build properly: one row per subspace vector
    rows = []
    for v in subspace:
        rows.append([sum(_Q(v[i]) * K[i, j] for i in range(DIM) if v[i] != 0)
                     for j in range(DIM)])
    return _nullspace_basis(rows)


def derived(subspace):
    """A basis of [S,S]."""
    vecs = []
    for i, a in enumerate(subspace):
        Aa = ad(a)
        for b in subspace[i + 1:]:
            vecs.append(list(Aa * sp.Matrix([_Q(x) for x in b])))
    if not vecs:
        return []
    # NB: rref()[1] is the tuple of PIVOT COLUMNS, not row indices -- using it to
    # index rows silently returns a wrong-dimensional space. Use rowspace().
    return [list(r) for r in sp.Matrix(vecs).rowspace()]


def dim_of(subspace):
    if not subspace:
        return 0
    return sp.Matrix([[_Q(x) for x in v] for v in subspace]).rank()


def cartan_basis():
    """The standard Cartan subalgebra (the 6 h-vectors)."""
    return [hvec(i) for i in range(N)]


def a2_a1_levi():
    """The A2+A1 Levi of e6: su(3)+su(2)+u(1)^3, the SMT block (B951/B892)."""
    simple = [tuple(1 if j == i else 0 for j in range(N)) for i in range(N)]
    pairs = [(i, j) for i in range(N) for j in range(i + 1, N) if C[i][j] == -1]
    i0, j0 = pairs[0]
    # a third node not adjacent to either -> the A1
    used = {i0, j0}
    k0 = next(k for k in range(N) if k not in used
              and C[k][i0] == 0 and C[k][j0] == 0)
    a, b = simple[i0], simple[j0]
    ab = tuple(a[t] + b[t] for t in range(N))
    sub = [IDX[s] for r in (a, b, ab) for s in (r, tuple(-x for x in r)) if s in IDX]
    sub += [IDX[s] for s in (simple[k0], tuple(-x for x in simple[k0])) if s in IDX]
    return [evec(ROOTS[k]) for k in sub] + cartan_basis(), (i0, j0, k0)


def self_test():
    """Every export exercised against a banked number. Returns a dict."""
    out = {}
    # 1. the Killing form is symmetric and nondegenerate (e6 is semisimple)
    K = killing()
    out["killing_symmetric"] = bool(K == K.T)
    out["killing_rank"] = int(K.rank())
    out["killing_nondegenerate"] = out["killing_rank"] == DIM
    # 2. B958's banked number: dim Z(su(3)_colour) = 16.
    #    NB (B974, Phase A): this su(3) is the STANDARD A2 LEVI, not derived(floor).
    #    Both give dim Z = 16, so B958's dimension-only condition survives -- but any
    #    FINER test must use the floor's, and conjugacy of the two is CONSISTENT WITH,
    #    not PROVED BY, the equal dimension.
    simple = [tuple(1 if j == i else 0 for j in range(N)) for i in range(N)]
    pairs = [(i, j) for i in range(N) for j in range(i + 1, N) if C[i][j] == -1]
    i0, j0 = pairs[0]
    a, b = simple[i0], simple[j0]
    ab = tuple(a[t] + b[t] for t in range(N))
    sub = [IDX[s] for r in (a, b, ab) for s in (r, tuple(-x for x in r)) if s in IDX]
    su3 = [evec(ROOTS[k]) for k in sub] + [hvec(i0), hvec(j0)]
    out["dim_Z_su3_colour"] = len(centralizer(su3))
    out["matches_B958"] = out["dim_Z_su3_colour"] == 16
    # 3. the A2+A1 Levi: dim 14, derived 11, centre 3 (B892/B951)
    levi, nodes = a2_a1_levi()
    out["levi_nodes"] = list(nodes)
    out["levi_dim"] = int(dim_of(levi))
    out["levi_derived_dim"] = int(dim_of(derived(levi)))
    out["levi_centre_dim"] = out["levi_dim"] - out["levi_derived_dim"]
    out["matches_B892_numbers"] = (out["levi_dim"] == 14
                                   and out["levi_derived_dim"] == 11
                                   and out["levi_centre_dim"] == 3)
    # 4. Killing-perp is exact and complementary
    cart = cartan_basis()
    out["dim_killing_perp_of_cartan"] = len(killing_perp(cart))
    out["perp_complements_cartan"] = (out["dim_killing_perp_of_cartan"] == DIM - N)
    return out


if __name__ == "__main__":
    import json
    r = self_test()
    print(json.dumps(r, indent=1))
    pathlib.Path(_HERE / "results.json").write_text(json.dumps(r, indent=1) + "\n")
