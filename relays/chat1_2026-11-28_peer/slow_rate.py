#!/usr/bin/env python3
"""This seat's own computation of the six-move slow rate on the cusp's leaf, for its peer notes on two offered cards
(written 2026-11-28; data-free). It shares no file with either producer: it reads no file, imports none of their code
or main's, and builds every object from the definitions the two cards state.

    python3 relays/chat1_2026-11-28_peer/slow_rate.py            # decisive: exit 0 when every expectation holds
    python3 relays/chat1_2026-11-28_peer/slow_rate.py --control  # the failing control: must exit 1

THE OBJECTS, as the cards define them. A reading is a triple (x, y, z) of residues mod N = p^k. The moves are
L(x, y, z) = (x, z, xz - y), R(x, y, z) = (z, y, yz - x) and X(x, y, z) = (y, yz - x, z), with their inverses
L^-1(a, b, c) = (a, ab - c, b), R^-1(a, b, c) = (ab - c, b, a) and X^-1(a, b, c) = (ac - b, a, c). The points over
the common point are the readings with every coordinate 0 mod p on the cusp's leaf x^2 + y^2 + z^2 - xyz = 0 mod N.
Their orbits are taken under L and R (a finite set, so the inverses add nothing), and the largest is the object. W is
the sum of the six moves' push-forward matrices on it, a symmetric matrix since each move's inverse is its
transpose; its top eigenvalue is 6, on the constants. The slow rate is W's largest eigenvalue below 6.

CONDITION, written before this script's first run:
  S1 X maps the largest orbit to itself at every level run (else W does not act on it and the run stops);
  S2 at mod 125, the slow rate is 2 sqrt(6 + sqrt 5) = 5.743124... to 1e-9, x^4 - 48 x^2 + 496 vanishes there to
     1e-7, and that polynomial is irreducible over Q (the offered card of seat fam2-v1-unset-01);
  S3 at mod 27, 125 and 343 the slow rate is 2 sqrt(5 + 4 cos(pi/p)) to 1e-9: 2 sqrt 7, 2 sqrt(6 + sqrt 5) and
     5.866... (the offered card of seat fam3-v1-high-01);
  S4 (an extension, no expectation either way) the same comparison one level up, at mod 81 = 3^4 and 625 = 5^4, and
     one level down, at mod 9, 25 and 49, is printed; "from p^3 on" predicts agreement at 81 and 625.
  The verdict holds if S1 to S3 hold; S4 is reported. The control runs S3's comparison against the prediction made
  wrong on purpose, 2 sqrt(5 + 4 cos(pi/(2p))), at mod 27: it must miss by more than 1e-9, so the control exits 1,
  with no traceback.
"""
import math
import sys

import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import eigsh


def points(p, k):
    N = p ** k
    m = np.arange(0, N, p, dtype=np.int64)
    x, y, z = np.meshgrid(m, m, m, indexing="ij")
    on = (x * x + y * y + z * z - x * y * z) % N == 0
    return N, list(zip(x[on].tolist(), y[on].tolist(), z[on].tolist()))


def moves(N):
    return [lambda v: (v[0], v[2], (v[0] * v[2] - v[1]) % N),
            lambda v: (v[2], v[1], (v[1] * v[2] - v[0]) % N),
            lambda v: (v[1], (v[1] * v[2] - v[0]) % N, v[2]),
            lambda v: (v[0], (v[0] * v[1] - v[2]) % N, v[1]),
            lambda v: ((v[0] * v[1] - v[2]) % N, v[1], v[0]),
            lambda v: ((v[0] * v[2] - v[1]) % N, v[0], v[2])]


def largest_orbit(pts, mv):
    seen, best = set(), []
    for v in pts:
        if v in seen:
            continue
        orb, stack = {v}, [v]
        while stack:
            u = stack.pop()
            for f in mv[:2]:
                w = f(u)
                if w not in orb:
                    orb.add(w)
                    stack.append(w)
        seen |= orb
        if len(orb) > len(best):
            best = sorted(orb)
    return best


def slow_rate(p, k):
    N, pts = points(p, k)
    mv = moves(N)
    orb = largest_orbit(pts, mv)
    idx = {v: i for i, v in enumerate(orb)}
    for v in orb:                                     # the inverses invert, and every move stays on the orbit (S1)
        assert mv[3](mv[0](v)) == v and mv[4](mv[1](v)) == v and mv[5](mv[2](v)) == v
        if any(f(v) not in idx for f in mv):
            return N, len(orb), None
    rows, cols = [], []
    for v in orb:
        for f in mv:
            rows.append(idx[f(v)])
            cols.append(idx[v])
    n = len(orb)
    W = sps.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))
    asym = abs(W - W.T).sum()
    if n <= 2000:
        ev = np.linalg.eigvalsh(W.toarray())
    else:
        ev = eigsh(W, k=6, which="LA", tol=1e-13, return_eigenvectors=False, v0=np.ones(n) / math.sqrt(n) + 1e-3 *
                   np.cos(np.arange(n)))
    ev = np.sort(ev)[::-1]
    below = max(e for e in ev if e < 6 - 1e-9)
    return N, n, (float(ev[0]), float(below), float(asym))


def law(p, cosarg=None):
    return 2 * math.sqrt(5 + 4 * math.cos(math.pi / (cosarg or p)))


def main(control=False):
    if control:
        N, n, r = slow_rate(3, 3)
        miss = abs(r[1] - law(3, 6))
        print("control: mod %d slow rate %.9f against 2 sqrt(5 + 4 cos(pi/6)) = %.9f made wrong on purpose: difference "
              "%.2e; S3's comparison: %s" % (N, r[1], law(3, 6), miss, "holds (the control has FAILED to fail)"
                                             if miss < 1e-9 else "fails, as it must"))
        return 0 if miss < 1e-9 else 1
    ok, res = True, {}
    for p, k in ((3, 2), (5, 2), (7, 2), (3, 3), (5, 3), (7, 3), (3, 4), (5, 4)):
        N, n, r = slow_rate(p, k)
        res[(p, k)] = r
        if r is None:
            print("DECISIVE: mod %d: the largest orbit has %d points and X leaves it (S1 fails)" % (N, n))
            ok &= k not in (3,)
            continue
        d = abs(r[1] - law(p))
        print("DECISIVE: mod %d: largest orbit %d points; top eigenvalue %.9f; slow rate %.9f; 2 sqrt(5 + 4 cos(pi/%d)) "
              "= %.9f; difference %s" % (N, n, r[0], r[1], p, law(p), "below 1e-9" if d < 1e-9 else "%.3e" % d))
        if k == 3:
            ok &= d < 1e-9 and abs(r[0] - 6) < 1e-9
    v = res[(5, 3)][1]
    pv = v ** 4 - 48 * v ** 2 + 496
    import sympy
    xs = sympy.symbols("x")
    irr = sympy.Poly(xs ** 4 - 48 * xs ** 2 + 496, xs).is_irreducible
    s2 = abs(v - 2 * math.sqrt(6 + math.sqrt(5))) < 1e-9 and abs(pv) < 1e-7 and irr
    print("DECISIVE: mod 125: slow rate against 2 sqrt(6 + sqrt 5) within 1e-9: %s; x^4 - 48 x^2 + 496 there within "
          "1e-7 of 0: %s; irreducible over Q: %s" % (abs(v - 2 * math.sqrt(6 + math.sqrt(5))) < 1e-9, abs(pv) < 1e-7, irr))
    ok &= s2
    for p in (3, 5):
        r = res[(p, 4)]
        print("DECISIVE: S4 (extension) mod %d: %s" % (p ** 4, "X leaves the largest orbit" if r is None else
              "slow rate %s 2 sqrt(5 + 4 cos(pi/%d)) within 1e-9" % ("equals" if abs(r[1] - law(p)) < 1e-9 else
                                                                    "does NOT equal", p)))
    print("DECISIVE: verdict: %s" % ("S1 to S3 hold" if ok else "S1 to S3 do NOT all hold"))
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main(control=sys.argv[1:] == ["--control"]))
