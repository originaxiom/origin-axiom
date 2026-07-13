"""B574 — the off-principal proposal: the two locks.

  (1) the minimal nilpotent orbit of E6 (= the A1 orbit, highest-root sl2) has
      reductive centralizer of dimension 35 = A5 = su(6) — NOT 45 = D5 = so(10);
      adjoint grading under the highest-root coweight = (1, 20, 30, 20, 1);
  (2) the 27 under the minimal sl2 = 6 V1 + 15 V0 (gradings {+-1: 6, 0: 15}) —
      every summand self-dual: the fifth wall applies verbatim at the minimal
      embedding; the obstruction is rank-1-ness, not the choice of orbit.
See frontier/B574_offprincipal/FINDINGS.md.
"""
from collections import Counter

import sympy as sp

C6 = sp.Matrix([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
                [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]])


def _roots():
    allr = {tuple(1 if i == j else 0 for i in range(6)) for j in range(6)}
    fr = set(allr)
    while fr:
        new = set()
        for rt in fr:
            for j in range(6):
                pj = sum(C6[i, j] * rt[i] for i in range(6))
                y = list(rt)
                y[j] -= pj
                ty = tuple(y)
                if ty not in allr:
                    allr.add(ty)
                    new.add(ty)
        fr = new
    return [sp.Matrix(r) for r in allr]


def test_minimal_orbit_centralizer_is_a5_not_d5():
    roots = _roots()
    assert len(roots) == 72
    pos = [r for r in roots if all(c >= 0 for c in r)]
    theta = max(pos, key=lambda r: sum(r))
    assert list(theta) == [1, 2, 2, 3, 2, 1]                 # the highest root
    ip = lambda x, y: (x.T * C6 * y)[0, 0]
    grading = Counter(int(ip(r, theta)) for r in roots)
    assert dict(grading) == {-2: 1, -1: 20, 0: 30, 1: 20, 2: 1}
    z_triple = (grading[0] + 6) - 1                          # ker(ad e_theta: g0 -> g2)
    assert z_triple == 35                                    # = dim A5 = su(6)
    assert z_triple != 45                                    # != dim D5 = so(10)


def test_27_at_minimal_embedding_self_dual():
    roots = _roots()
    pos = [r for r in roots if all(c >= 0 for c in r)]
    theta = max(pos, key=lambda r: sum(r))
    G6 = C6.inv()
    seen = {tuple(G6[:, 0])}
    frontier = [G6[:, 0]]
    while frontier:
        new = []
        for v in frontier:
            for j in range(6):
                pj = sum(C6[i, j] * v[i] for i in range(6))
                u = sp.Matrix(v)
                u[j] = v[j] - pj
                tu = tuple(u)
                if tu not in seen:
                    seen.add(tu)
                    new.append(u)
        frontier = new
    ip = lambda x, y: (x.T * C6 * y)[0, 0]
    g27 = Counter(int(2 * ip(sp.Matrix(m), theta) / ip(theta, theta)) for m in seen)
    assert dict(g27) == {-1: 6, 0: 15, 1: 6}                 # 6 V1 + 15 V0: all self-dual
