#!/usr/bin/env python3
"""The golden closings and the four (sL-12 item 3 (c)): an own-code check of a published theorem, with a control on banked
data.  Nothing here is an open outcome of the record.

- Scannell, "Infinitesimal deformations of some SO(3,1) lattices", Pacific J. Math. 194 (2000) 455-464, Theorem 4.3: for
  every m >= 4 the Fibonacci manifold F_m (the m-fold cyclic branched cover of the figure-eight knot, pi_1 = F(2, 2m); the
  record's closing Y_m, B1273/B1303) has dim H^1(pi_1 F_m; R^{3,1}) = 2 at its hyperbolic holonomy.  Checked at m = 4..8.
- The identification: F_m is the filling of the m-fold cyclic cover M_m of 4_1 (SnapPy's cover) along slope (0, 1) of the
  cover's peripheral basis, for m >= 4 (the convention differs at m = 2, 3, which are not used).  It is checked by
  |H_1| = L_{2m} - 2 (Fox's formula, Delta = t^2 - 3t + 1) and by the volumes Scannell and Mednykh-Vesnin give
  (F_4 = vol 4_1, F_6 = vol of the Borromean rings, F_8 = vol 8_18).
- The control: at its own (cusped) holonomy each level M_1..M_6 has dim H^1(M_m; R^{3,1}) = 1, the cusp's half.  That is
  sm:B1515's banked statement that no interior class of the four exists at the trivial character through level 6.
- The other fillings (p, 1), 0 < |p| <= m + 2, with the same |H_1|: the dimension at each is reported.

Route: SnapPy's high-precision holonomy (SL(2,C), 212 bits), pushed to SO(3,1) through the action A.Q = A Q A^* on Hermitian
matrices (Scannell's identification x -> [[x3+x4, x1+i x2], [x1-i x2, x4-x3]]).  H^1 = Z^1/B^1 is read from the Fox
Jacobian of SnapPy's presentation by an SVD at 50 digits, with dim B^1 = 4 (irreducible holonomy).  A dimension is accepted
only when every singular value is below 1e-30 or above 1e-3.  Run: python3 gc_fibonacci.py (about a minute)."""
import math

import mpmath as mp
import snappy

mp.mp.dps = 50
ZERO, NONZERO = mp.mpf(10) ** -30, mp.mpf(10) ** -3


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def _herm(x):
    return mp.matrix([[x[2] + x[3], x[0] + 1j * x[1]], [x[0] - 1j * x[1], x[3] - x[2]]])


HB = [_herm([1 if i == k else 0 for i in range(4)]) for k in range(4)]


def _coords(Q):
    return [mp.re(Q[0, 1]), mp.im(Q[0, 1]), mp.re(Q[0, 0] - Q[1, 1]) / 2, mp.re(Q[0, 0] + Q[1, 1]) / 2]


def so31(A):
    Ah = A.transpose_conj()
    M = mp.matrix(4, 4)
    for k in range(4):
        c = _coords(A * HB[k] * Ah)
        for i in range(4):
            M[i, k] = c[i]
    return M


def _num(x):
    return mp.mpf(str(x).replace(" ", ""))


def _sl2c(m2):
    return mp.matrix([[mp.mpc(_num(m2[i, j].real()), _num(m2[i, j].imag())) for j in range(2)] for i in range(2)])


def h1_four(M):
    """dim H^1(pi_1 M; R^{3,1}) at M's holonomy, from the Fox Jacobian (rows: relators, 4 each; columns: generators)."""
    G = M.fundamental_group()
    gens, rels = G.generators(), G.relators()
    mats = {}
    for g in gens:
        R = so31(_sl2c(G.SL2C(g)))
        mats[g], mats[g.upper()] = R, mp.inverse(R)
    J = mp.matrix(4 * len(rels), 4 * len(gens))
    for j, r in enumerate(rels):
        prefix = mp.eye(4)
        for ch in r:
            i = gens.index(ch.lower())
            if ch.islower():
                blk = prefix
                prefix = prefix * mats[ch]
            else:
                prefix = prefix * mats[ch]
                blk = -prefix
            for a in range(4):
                for b in range(4):
                    J[4 * j + a, 4 * i + b] += blk[a, b]
    raw = mp.svd_r(J, compute_uv=False)
    sv = [raw[i] for i in range(raw.rows)]
    assert all(s < ZERO or s > NONZERO for s in sv), "no clean gap"
    rank = sum(1 for s in sv if s > NONZERO)
    return 4 * len(gens) - rank - 4


def geometric(M, tries=300):
    """M itself if its solution is positively oriented, else a closed retriangulation that is (randomised)."""
    if "positively" in M.solution_type():
        return M
    G = snappy.ManifoldHP(M.filled_triangulation())
    for _ in range(tries):
        if "positively" in G.solution_type():
            return G
        G.randomize()
    raise RuntimeError("no positively oriented triangulation found")


def level(m):
    return snappy.ManifoldHP("4_1").covers(m, cover_type="cyclic")[0]


def main():
    print("L_{2m} - 2 for m = 1..8 (Fox's formula for the m-fold branched cover; the torsion orders of M_1..M_6 that "
          "sm:B1515's population A enumerated are its first six):", [lucas(2 * m) - 2 for m in range(1, 9)])
    print("control: the cusped levels at their own holonomy (sm:B1515: no interior class of the four at the trivial "
          "character through level 6, so 1 = the cusp's half):")
    print("  " + ", ".join(f"M_{m}: {h1_four(level(m))}" for m in range(1, 7)))
    print("the closings F_m at their own holonomy (Scannell, Theorem 4.3: 2):")
    for m in range(4, 9):
        C = level(m)
        F = C.copy()
        F.dehn_fill((0, 1))
        Fg = geometric(F)
        vol = mp.mpf(_num(Fg.volume()))
        others = {}
        for p in range(-(m + 2), m + 3):
            if p == 0:
                continue
            X = C.copy()
            X.dehn_fill((p, 1))
            if X.homology().order() != lucas(2 * m) - 2 or "positively" not in X.solution_type():
                continue
            d = h1_four(X)
            others[d] = others.get(d, 0) + 1
        assert Fg.homology().order() == lucas(2 * m) - 2
        print(f"  F_{m}: H_1 {Fg.homology()} (order L_{2 * m} - 2), vol {mp.nstr(vol, 12)}: "
              f"dim H^1(F_{m}; R^(3,1)) = {h1_four(Fg)}; "
              f"other fillings (p, 1) with the same |H_1|, by dimension: {dict(sorted(others.items()))}")
    print("reference volumes: 4_1 " + mp.nstr(mp.mpf(_num(snappy.ManifoldHP('4_1').volume())), 12)
          + ", Borromean rings " + mp.nstr(mp.mpf(_num(snappy.ManifoldHP('L6a4').volume())), 12)
          + ", 8_18 " + mp.nstr(mp.mpf(_num(snappy.ManifoldHP('8_18').volume())), 12))


if __name__ == "__main__":
    main()
