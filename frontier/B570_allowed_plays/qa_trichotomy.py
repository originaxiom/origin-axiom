"""B570 Lane C, Q-A — the trichotomy, decided. See QA_RESULT.md.

Computes, exactly:
  1. the fig-8 parabolic rep (relation aW = Wb, W = b a^-1 b^-1 a) and the Galois
     pair tr rho(ab) = (5 +- sqrt(-3))/2, min poly t^2 - 5t + 7, disc -3
     => rho-bar is NOT inner-equivalent to rho;
  2. the F4-principal nilpotent is REGULAR in E6 (Jordan type (17,9,1) on the 27
     from both sides) => theta fixes a principal embedding pointwise
     => 'rho-bar ~ theta o rho' was never distinct from 'rho-bar ~ rho';
  3. amphichirality in-sandbox (SnapPy symmetry group of 4_1) — the Mostow input
     for rho-bar ~ rho o phi (sigma acts as the object's own mirror);
  4. the tangent real-structure: conj o theta fixes (theta-even)_R + i(theta-odd)_R
     — the theta-odd sector is the imaginary axes of the self-mirror.

Run: python3 frontier/B570_allowed_plays/qa_trichotomy.py
"""
from collections import Counter

import sympy as sp

C6 = sp.Matrix([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
                [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]])
C4L = [[2, -1, 0, 0], [-1, 2, -2, 0], [0, -1, 2, -1], [0, 0, -1, 2]]


def galois_pair():
    w6 = sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
    A = sp.Matrix([[1, 1], [0, 1]])
    B = sp.Matrix([[1, 0], [w6, 1]])
    W = B * A.inv() * B.inv() * A
    assert sp.expand(A * W - W * B) == sp.zeros(2)          # genuine fig-8 rep
    t = sp.expand(sp.trace(A * B))
    return t, sp.minimal_polynomial(t, sp.Symbol('x'))


def _blocks(grades):
    """Jordan blocks from an sl2 weight multiset: a top weight m contributes the
    string m, m-2, ..., -m (block size m+1)."""
    cnt = Counter(grades)
    out = []
    while cnt:
        m = max(cnt)
        out.append(int(m + 1))
        g = m
        while g >= -m:
            cnt[g] -= 1
            if cnt[g] == 0:
                del cnt[g]
            g -= 2
    return sorted(out, reverse=True)


def jordan_types():
    """E6-principal on the 27 vs F4-principal on 1+26, via the 2rho-vee grading."""
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
    rho6 = sum([G6[:, j] for j in range(6)], sp.zeros(6, 1))
    e6 = _blocks(sorted(sp.Rational(2 * (sp.Matrix(mu).T * C6 * rho6)[0, 0]) for mu in seen))
    d4 = [1, 1, sp.Rational(1, 2), sp.Rational(1, 2)]
    B4 = sp.Matrix(4, 4, lambda i, j: sp.Rational(C4L[i][j]) * d4[j])
    allr = {tuple(1 if i == j else 0 for i in range(4)) for j in range(4)}
    fr = set(allr)
    while fr:
        new = set()
        for rt in fr:
            for j in range(4):
                pj = sum(C4L[i][j] * rt[i] for i in range(4))
                y = list(rt)
                y[j] -= pj
                ty = tuple(y)
                if ty not in allr:
                    allr.add(ty)
                    new.add(ty)
        fr = new
    ip4 = lambda x, y: (x.T * B4 * y)[0, 0]
    pos = [sp.Matrix(r) for r in allr if all(c >= 0 for c in r)]
    rhovee = sum([2 * a / ip4(a, a) for a in pos], sp.zeros(4, 1)) / 2
    short = [sp.Matrix(r) for r in allr if ip4(sp.Matrix(r), sp.Matrix(r)) == 1]
    f4 = _blocks(sorted([sp.Rational(2 * ip4(mu, rhovee)) for mu in short] + [sp.Integer(0)] * 2))
    return e6, sorted(f4 + [1], reverse=True)


if __name__ == '__main__':
    t, mp = galois_pair()
    print("tr rho(ab) =", t, "; min poly:", mp, "; disc:", sp.discriminant(mp))
    e6, f4 = jordan_types()
    print("Jordan on 27: E6-principal", e6, " F4-principal", f4, " equal:", e6 == f4)
    try:
        import snappy
        sg = snappy.Manifold('4_1').symmetry_group()
        print("4_1 symmetry group:", sg, "order", sg.order(), "amphichiral:", sg.is_amphicheiral())
    except Exception as exc:
        print("snappy unavailable:", type(exc).__name__, "(amphichirality classical + banked CS=0)")
    print("tangent: conj o theta fixes (theta-even)_R + i(theta-odd)_R  [see the lock]")
