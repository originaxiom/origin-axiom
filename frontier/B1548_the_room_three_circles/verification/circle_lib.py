"""B1548 -- the library: N45's room-three circles and the members on them, in two routes.

It loads sm:B1547's member_lib by path, unchanged, and adds only the population.  On N45 the cusp-trivial characters with
room three (n = 3) at orders 2 to 6 are the points t.v of five circles, one tau-orbit (the dossier
docs/dossiers/room_three_circles_2026-10-07).  Each route finds its own circles:
  - the five room-three characters of order 2 (member_lib.room3) give v mod 2, and the five lines of room-three characters of
    order 3 give v mod 3 up to sign; the direction v is the lift with entries in {-1, 0, 1} (unique, since v mod 6 is then
    determined), and it is checked against both;
  - the circle of chi0 (the room-three order-2 character with the least key, sm:B1547's) is the population's circle;
  - its points of exact order m are j.v (j a unit mod m), exponent vectors on the route's own generators, named by their keys
    (values mod m on the 46 common loops), so the i-th member of an order is the same character in both routes.
A member nu is built from its exponent vector and a root of unity of order m in the route's field."""
import importlib.util
import itertools
import sys
from math import gcd
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
MLP = ROOT / "frontier" / "B1547_the_room_three_members" / "verification" / "member_lib.py"


def _load(alias, path):
    if alias not in sys.modules:
        spec = importlib.util.spec_from_file_location(alias, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[alias] = mod
        spec.loader.exec_module(mod)
    return sys.modules[alias]


ML = _load("b1548_member_lib", MLP)
FL = ML.FL


def root(cv, route, m):
    """a root of unity of exact order m in the route's field"""
    if route == "R":
        return cv.root(m)
    return FL.F().root_of_order(cv.p, m)


def line_n(CH, cv, route, e, m):
    """n of the line with exponent vector e (mod m) on the route's generators"""
    p = cv.p
    z = root(cv, route, m)
    if route == "R":
        mod = cv.R.CMod([np.array([[pow(z, int(x) % m, p)]], dtype=np.int64) for x in e], p)
        return int(cv.R.Coh(cv.cov, mod).n)
    cov = cv.cov
    sys_ = {(x, g): np.array([[pow(z, int(e[cov.edge(x, g)]) % m, p)]], dtype=np.int64) for x in range(cov.d) for g in cov.gens}
    return int(FL.F().Coh(cov, sys_, p).n)


def exponents(CH, a, m):
    """the exponent vector (mod m) of the character with free-lattice coefficients a"""
    return np.asarray(sum(int(ai) * CH.F[i] for i, ai in enumerate(a)), dtype=np.int64) % m


def room_lines(CH, cv, route, m):
    """the lines {t a} (t a unit mod m) of characters of exact order m on the free part with n = 3, as sorted coefficient
    tuples (a census: m^4 characters)"""
    seen, lines = set(), []
    for a in itertools.product(range(m), repeat=CH.F.shape[0]):
        g = m
        for x in a:
            g = gcd(g, x)
        if g != 1 or a in seen:
            continue
        L = sorted({tuple((t * x) % m for x in a) for t in range(1, m) if gcd(t, m) == 1})
        seen.update(L)
        if line_n(CH, cv, route, exponents(CH, a, m), m) == 3:
            lines.append(L)
    return lines


def int_values(CH, e, loops):
    """the character's integer values on the based loops (no reduction): the loops' images under the homomorphism e"""
    big = 1 << 40
    return tuple(x if x < big // 2 else x - big for x in CH.values(np.asarray(e, dtype=np.int64), loops, big))


def solve_direction(CH, w, loops):
    """the coefficients v (integers, in the route's own lattice basis) of the homomorphism whose loop values are w; the
    solution must exist, be unique and integral"""
    import sympy as sp
    A = sp.Matrix([list(int_values(CH, CH.F[i], loops)) for i in range(CH.F.shape[0])])     # rows: the basis on the loops
    sol, params = A.T.gauss_jordan_solve(sp.Matrix(list(w)))
    assert params.shape[0] == 0, "the direction is not unique"
    v = [int(x) for x in sol]
    assert all(x == y for x, y in zip(sol, v)), "the direction is not integral"
    assert tuple(int_values(CH, sum(vi * CH.F[i] for i, vi in enumerate(v)), loops)) == tuple(w)
    return tuple(v)


def directions(CH, cv, route, loops):
    """the five circles' directions v (entries in {-1, 0, 1}), each with its order-2 point's key, sorted by that key (route R's
    basis; route F takes the circle through solve_direction, from its loop values)"""
    r2, _ = ML.room3(CH, loops)
    l3 = room_lines(CH, cv, route, 3)
    out = []
    for key2, f in r2:
        # f is a 0/1 combination of F's rows: its coefficients are v mod 2
        a2 = None
        for coeffs in itertools.product([0, 1], repeat=CH.F.shape[0]):
            if any(coeffs) and np.array_equal(sum(c * CH.F[i] for i, c in enumerate(coeffs)) % 2, np.asarray(f) % 2):
                a2 = coeffs
                break
        cands = []
        for v in itertools.product((-1, 0, 1), repeat=CH.F.shape[0]):
            if tuple(x % 2 for x in v) != tuple(a2):
                continue
            if any(tuple(x % 3 for x in v) in L for L in l3):
                cands.append(v)
        # v and -v are one circle
        cands = sorted({min(v, tuple(-x for x in v)) for v in cands})
        assert len(cands) == 1, ("the direction is not determined", key2, cands)
        out.append((key2, cands[0]))
    assert len(out) == 5 and len(l3) == 5
    return sorted(out, key=lambda t: t[0])


def circle_points(CH, loops, v, m):
    """the points of exact order m on the circle t -> t v: [(key, e)] sorted by key"""
    pts = []
    for j in range(1, m):
        if gcd(j, m) != 1:
            continue
        e = exponents(CH, [j * x for x in v], m)
        pts.append((CH.values(e, loops, m), e))
    pts.sort(key=lambda t: t[0])
    assert len({k for k, _ in pts}) == len(pts)
    return pts


def nu_values(cv, route, e, m):
    """the member's values on the route's generators (route R: a list on the Schreier generators; route F: a dict on edges)"""
    p = cv.p
    z = root(cv, route, m)
    if route == "R":
        return [pow(z, int(x) % m, p) for x in e]
    cov = cv.cov
    return {(x, g): pow(z, int(e[cov.edge(x, g)]) % m, p) for x in range(cov.d) for g in cov.gens}


def member(cv, route, e, m):
    nu = nu_values(cv, route, e, m)
    return ML.RMember(cv, nu) if route == "R" else ML.FMember(cv, nu)
