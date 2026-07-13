"""B570 Lane C spine — the theta-odd sector of E6 (the seventeenth question's home).

Verified from the incoming five-sources/theta-odd handoff (2026-07-14), exact:
  (i)   E6 exponents {1,4,5,7,8,11}; F4 exponents {1,5,7,11}; theta-odd = {4,8}
        (H^1 split: even dim 4, odd dim 2 — B347's fold, now with the exponent labels);
  (ii)  the OMEGA CONNECTION: the theta-odd Coxeter eigenvalues e^{2 pi i m/12} at
        m = 4, 8 are exactly omega and omega^2 — the Eisenstein chirality window
        (B356) and the theta-odd sector are the same structure;
  (iii) E6 level 2: exactly 9 integrable reps, 3 theta-fixed + 3 swapped pairs
        (theta-odd dimension 3) — the arena for the level-2 monodromy cell (C3);
  (iv)  the banked non-real adjoint trace (B565-H1) lies in Q(sqrt-3) \\ R —
        the holonomy fixes an embedding of the Eisenstein field (source 5).
See frontier/B570_allowed_plays/PREREGISTRATION.md (Lane C).
"""
import sympy as sp
from collections import Counter
from itertools import product


def _roots(C, n):
    allr = {tuple(1 if i == j else 0 for i in range(n)) for j in range(n)}
    frontier = set(allr)
    while frontier:
        new = set()
        for rt in frontier:
            for j in range(n):
                pj = sum(C[i][j] * rt[i] for i in range(n))
                y = list(rt)
                y[j] -= pj
                ty = tuple(y)
                if ty not in allr:
                    allr.add(ty)
                    new.add(ty)
        frontier = new
    return allr


def _exponents(C, n):
    pos = [r for r in _roots(C, n) if all(c >= 0 for c in r)]
    hts = Counter(sum(r) for r in pos)
    maxh = max(hts)
    exps = []
    for m in range(1, maxh + 1):
        exps += [m] * (hts.get(m, 0) - hts.get(m + 1, 0))
    return sorted(exps)


C6 = [[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
      [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]]
C4 = [[2, -1, 0, 0], [-1, 2, -2, 0], [0, -1, 2, -1], [0, 0, -1, 2]]


def test_theta_odd_exponents():
    e6, f4 = _exponents(C6, 6), _exponents(C4, 4)
    assert e6 == [1, 4, 5, 7, 8, 11]
    assert f4 == [1, 5, 7, 11]
    odd = sorted(set(e6) - set(f4))
    assert odd == [4, 8]                      # theta-odd dim 2; theta-even dim 4
    assert set(f4) < set(e6)                  # the fold embeds exponent-wise


def test_omega_connection():
    # Coxeter number h(E6) = 12; the theta-odd Coxeter eigenvalues are the Eisenstein pair
    w = sp.exp(2 * sp.pi * sp.I / 3)
    assert sp.simplify(sp.exp(2 * sp.pi * sp.I * sp.Rational(4, 12)) - w) == 0
    assert sp.simplify(sp.exp(2 * sp.pi * sp.I * sp.Rational(8, 12)) - w**2) == 0
    assert max(_exponents(C6, 6)) + 1 == 12


def test_e6_level2_theta_split():
    marks = [1, 2, 2, 3, 2, 1]                # Kac marks (levels of the fundamentals)
    lev2 = [w for w in product(range(3), repeat=6)
            if sum(n * a for n, a in zip(w, marks)) <= 2]
    assert len(lev2) == 9                      # nine integrable reps at level 2
    theta = lambda w: (w[5], w[1], w[4], w[3], w[2], w[0])   # 1<->6, 3<->5
    fixed = [w for w in lev2 if theta(w) == w]
    pairs = [w for w in lev2 if theta(w) > w]
    assert len(fixed) == 3 and len(pairs) == 3               # theta-odd dimension 3
    assert (0, 1, 0, 0, 0, 0) in fixed and (1, 0, 0, 0, 0, 1) in fixed


def test_nonreal_trace_in_eisenstein_field():
    tr = 37437270 + 38799960 * sp.sqrt(3) * sp.I             # B565-H1, banked
    assert sp.simplify(tr - (37437270 + 38799960 * sp.sqrt(-3))) == 0
    assert sp.simplify(tr - sp.conjugate(tr)) != 0           # conjugation broken
