#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
THE AGY LANE'S SELF-CONSISTENT LOOP, PHASE 1: A FIRST INDEPENDENT CHECK.   Data-free; integers, and 40-digit
arithmetic for positions only.

The web seat (chat1), 2026-11-11, at the owner's word to the seat: "verify it please" (relayed, not confirmed to
main).  Kind: thread, except V1.  The lane's branch agy/self-consistent-loop-2026-11-11 was read at 2cc5bf4e5,
through the mask.  None of the lane's code was run and none of its output files was opened.  This script uses
nothing of the lane's: it is written from the lane's sealed specification of Phase 1 (its declared domains and
histories) and from the record's flat-fibre instrument (B1857), in the seat's own conventions.

WHAT IS CHECKED, AND WHAT IS NOT
  V1  Sector 1 of the lane (its back-edge 1): among the 95 irreducible root systems of rank 1 to 24, with the
      shortest roots of norm 2, which root lattices are even and of determinant 1.
  V2a Sector 2, first half: the Smith invariants of W - I and W + I for the metallic words W(m) = L^m R^m,
      m = 1..4.
  V2b Sector 2, second half, in the limit the seat can do exactly: on the flat-fibre bundle a fibre mode with
      label kappa/5 has, along the history's axis, least length proportional to |Q(kappa)|, where Q is the
      history's own invariant form; every mode sees the same well, scaled by |Q| and shifted along the axis.  So
      the lightest state of a sector sits on the classes of least |Q|, at every fibre area, and the sector has one
      lightest state exactly when one class of the history attains that least.  The untwisted sector is the
      integer vectors.  The twisted sector of charge q is the vectors kappa = +-q v0 modulo 5, v0 = (1, 3) the
      mark; a class is an orbit of the history's matrix, up to sign.
      Computed for the lane's declared histories with k = 1, 2, 3 golden periods: the least |Q|, how many classes
      attain it, and where each sits along one period, measured from the untwisted apex.
  NOT CHECKED HERE: the lane's finite-area spectra and its punctured-fibre test; its Sectors 3 and 4; Phases 2
  and 3.  Nothing of Phase 3's third gate is computed by the seat.

EXPECTATIONS (written before the run)
  E1  V1: the Gram matrices are all even and integral; exactly one has determinant 1, and it is E8.  G2 and F4
      have Cartan determinant 1 and Gram determinant greater than 1.
  E2  V2a: W(m) - I has invariants (m, m); W(m) + I has determinant m^2 + 4 and invariants (1, m^2 + 4) for odd m,
      (2, (m^2 + 4)/2) for even m.  So W - I is invertible only at m = 1, and there W + I has invariants (1, 5).
  E3  V2b, untwisted: (6) has one class of least |Q|, for each k.
  E4  V2b, by symmetry only: (6) closed by golden periods is a palindrome, so its classes of least |Q| are
      carried to each other by the reflection of the axis about the apex.  Their positions are symmetric about
      the apex.
  E5  V2b, the lane's claims as the seat read them, to be confirmed or not: at charge +-1 the run of 6 has two
      classes of least |Q|, a mirror pair off the apex; at charge +-2 it has one, half a period from the apex.
  Disclosed: the seat read the lane's report before writing this, and two of its numbers were visible on lines
  the mask does not star: a shift of about 0.30 at charge +-1 and of 0.50 at charge +-2.  E5 is therefore not
  blind.  Nothing was run before this file was committed; it was parsed for syntax.

CONVENTIONS
  L = rows (1,0),(1,1); R = rows (1,1),(0,1); vectors are rows, v -> v.M.  For M = rows (a,b),(c,d) the form
  Q(x, y) = b x^2 + (d - a) x y - c y^2 satisfies Q(v.M) = Q(v) (asserted).  Positions: with lam > 1 the larger
  eigenvalue and v = alpha e+ + beta e-, s(v) = log|beta/alpha| / (2 log lam) modulo 1, which is constant on a
  class up to the sign v -> -v.
"""
import itertools
import sys
from fractions import Fraction
from math import gcd

import mpmath as mp

mp.mp.dps = 40

L = ((1, 0), (1, 1))
R = ((1, 1), (0, 1))
I2 = ((1, 0), (0, 1))


def mul(a, b):
    return ((a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]),
            (a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]))


def word(s):
    m = I2
    for ch in s:
        m = mul(m, L if ch == 'L' else R)
    return m


def rowact(v, m):
    return (v[0] * m[0][0] + v[1] * m[1][0], v[0] * m[0][1] + v[1] * m[1][1])


def inv(m):
    return ((m[1][1], -m[0][1]), (-m[1][0], m[0][0]))


def smith(m):
    g = gcd(gcd(abs(m[0][0]), abs(m[0][1])), gcd(abs(m[1][0]), abs(m[1][1])))
    d = abs(m[0][0] * m[1][1] - m[0][1] * m[1][0])
    return (g, d // g if g else 0)


def det_frac(rows):
    """exact determinant by fraction elimination"""
    a = [[Fraction(x) for x in r] for r in rows]
    n = len(a)
    d = Fraction(1)
    for i in range(n):
        p = next((r for r in range(i, n) if a[r][i] != 0), None)
        if p is None:
            return Fraction(0)
        if p != i:
            a[i], a[p] = a[p], a[i]
            d = -d
        d *= a[i][i]
        for r in range(i + 1, n):
            f = a[r][i] / a[i][i]
            if f:
                for c in range(i, n):
                    a[r][c] -= f * a[i][c]
    return d


def gram_from_chain(norms, bonds):
    """Gram matrix from the simple roots' norms and the list of joined pairs (i, j): <a_i, a_j> = -max(n_i, n_j)/2"""
    n = len(norms)
    g = [[0] * n for _ in range(n)]
    for i in range(n):
        g[i][i] = norms[i]
    for i, j in bonds:
        v = -max(norms[i], norms[j]) // 2
        g[i][j] = v
        g[j][i] = v
    return g


def cartan(g):
    n = len(g)
    return [[Fraction(2 * g[i][j], g[j][j]) for j in range(n)] for i in range(n)]


def root_systems():
    out = []
    for r in range(1, 25):
        out.append(('A%d' % r, gram_from_chain([2] * r, [(i, i + 1) for i in range(r - 1)])))
    for r in range(2, 25):
        out.append(('B%d' % r, gram_from_chain([4] * (r - 1) + [2], [(i, i + 1) for i in range(r - 1)])))
    for r in range(3, 25):
        out.append(('C%d' % r, gram_from_chain([2] * (r - 1) + [4], [(i, i + 1) for i in range(r - 1)])))
    for r in range(4, 25):
        out.append(('D%d' % r, gram_from_chain([2] * r, [(i, i + 1) for i in range(r - 2)] + [(r - 3, r - 1)])))
    out.append(('G2', [[2, -3], [-3, 6]]))
    out.append(('F4', gram_from_chain([4, 4, 2, 2], [(0, 1), (1, 2), (2, 3)])))
    for r in (6, 7, 8):
        out.append(('E%d' % r, gram_from_chain([2] * r, [(i, i + 1) for i in range(r - 2)] + [(2, r - 1)])))
    return out


def qform(m):
    a, b = m[0]
    c, d = m[1]
    return lambda v: b * v[0] * v[0] + (d - a) * v[0] * v[1] - c * v[1] * v[1]


def canon(v, m, mi, span=6):
    """a canonical representative of the class {+-v.M^j}: least (max|x|,|y|), then lexicographic"""
    best = None
    w = v
    cands = [v]
    for _ in range(span):
        w = rowact(w, m)
        cands.append(w)
    w = v
    for _ in range(span):
        w = rowact(w, mi)
        cands.append(w)
    for w in cands:
        for s in (1, -1):
            u = (s * w[0], s * w[1])
            key = (max(abs(u[0]), abs(u[1])), abs(u[0]) + abs(u[1]), u)
            if best is None or key < best:
                best = key
    return best[2]


def position(v, m):
    a, b = m[0]
    c, d = m[1]
    t = a + d
    lam = (t + mp.sqrt(t * t - 4)) / 2
    ep = (mp.mpf(c), lam - a)
    em = (mp.mpf(c), 1 / lam - a)
    den = ep[0] * em[1] - ep[1] * em[0]
    alpha = (v[0] * em[1] - v[1] * em[0]) / den
    beta = (ep[0] * v[1] - ep[1] * v[0]) / den
    s = mp.log(abs(beta / alpha)) / (2 * mp.log(lam))
    return s - mp.floor(s)


def least_classes(m, residues, modulus, box):
    """classes of least |Q| among the vectors congruent to one of `residues` modulo `modulus` (all non-zero
    integer vectors when modulus is 1), searched in the box |x|, |y| <= box"""
    q = qform(m)
    mi = inv(m)
    vals = {}
    for x in range(-box, box + 1):
        for y in range(-box, box + 1):
            if x == 0 and y == 0:
                continue
            if modulus > 1 and (x % modulus, y % modulus) not in residues:
                continue
            if modulus == 1 and gcd(abs(x), abs(y)) != 1:
                continue
            vals.setdefault(abs(q((x, y))), []).append((x, y))
    out = []
    for val in sorted(vals)[:2]:
        reps = sorted(set(canon(v, m, mi) for v in vals[val]))
        out.append((val, reps))
    return out


def frac_diff(s, s0):
    d = s - s0
    d = d - mp.floor(d)
    return d


def main():
    print('THE AGY LANE\'S LOOP, PHASE 1: A FIRST INDEPENDENT CHECK')
    print()
    # ------------------------------------------------------------------ V1
    print('V1  root lattices, shortest roots of norm 2')
    systems = root_systems()
    even = 0
    unimod = []
    notes = {}
    for name, g in systems:
        ok_even = all(g[i][i] % 2 == 0 for i in range(len(g)))
        even += ok_even
        d = det_frac(g)
        if d == 1:
            unimod.append(name)
        if name in ('G2', 'F4', 'E6', 'E7', 'E8', 'A1', 'A4', 'B2', 'B8', 'C3', 'C8', 'D4', 'D8', 'D16', 'D24'):
            notes[name] = (d, det_frac(cartan(g)))
    print('    systems: %d; even and integral: %d; of determinant 1: %s' % (len(systems), even, unimod))
    print('    (Gram determinant, Cartan determinant): ' + ', '.join('%s %s' % (k, (str(v[0]), str(v[1]))) for k, v in notes.items()))
    e1 = len(systems) == 95 and even == 95 and unimod == ['E8'] and notes['G2'][1] == 1 and notes['F4'][1] == 1 and notes['G2'][0] > 1 and notes['F4'][0] > 1
    print('E1: %s' % ('HOLDS' if e1 else 'FAILS'))
    print()
    # ------------------------------------------------------------------ V2a
    print('V2a  metallic words W(m) = L^m R^m: invariants of W - I and of W + I')
    e2 = True
    for m in range(1, 5):
        w = word('L' * m + 'R' * m)
        sm = smith(((w[0][0] - 1, w[0][1]), (w[1][0], w[1][1] - 1)))
        sp = smith(((w[0][0] + 1, w[0][1]), (w[1][0], w[1][1] + 1)))
        print('    m = %d  W = %s  trace %d   W - I: %s   W + I: %s' % (m, w, w[0][0] + w[1][1], sm, sp))
        e2 = e2 and sm == (m, m) and sp == ((1, m * m + 4) if m % 2 else (2, (m * m + 4) // 2))
    print('E2: %s' % ('HOLDS' if e2 else 'FAILS'))
    print()
    # ------------------------------------------------------------------ V2b
    print('V2b  classes of least |Q|, by sector; positions along one period, measured from the untwisted apex')
    v0 = (1, 3)
    hist = [('(6)', 'LLLLLLR'), ('(2,1,2,1,2)', 'LLRLLRLLR'), ('(2,1,1,1,2)', 'LLRLRLLR'), ('(2,2,2) as the lane writes it', 'LLRRLL'),
            ('golden ground', 'LR')]
    e3 = True
    e4 = True
    e5 = True
    for name, dep in hist:
        for k in (1, 2, 3):
            w = dep + 'LR' * k
            m = word(w)
            q = qform(m)
            for test in ((1, 3), (2, 5), (-3, 7), (11, -4)):
                assert q(rowact(test, m)) == q(test)
            img = rowact(v0, m)
            keeps = (img[0] % 5, img[1] % 5) in ((v0[0] % 5, v0[1] % 5), ((-v0[0]) % 5, (-v0[1]) % 5))
            print('    %s, k = %d: word %s, trace %d, keeps +-v0: %s' % (name, k, w, m[0][0] + m[1][1], keeps))
            box = 60
            un = least_classes(m, None, 1, box)
            un2 = least_classes(m, None, 1, 2 * box)
            stable = un == un2
            s_apex = position(un[0][1][0], m)
            print('        untwisted: least |Q| = %d on %d class(es) %s; next %d; box doubled gives the same: %s'
                  % (un[0][0], len(un[0][1]), un[0][1], un[1][0], stable))
            if name == '(6)':
                e3 = e3 and len(un[0][1]) == 1 and stable
            if not keeps:
                print('        twisted sectors: not defined, the history does not keep the mark')
                continue
            for qc in (1, 2):
                res = set()
                for sgn in (1, -1):
                    res.add(((sgn * qc * v0[0]) % 5, (sgn * qc * v0[1]) % 5))
                tw = least_classes(m, res, 5, 5 * box)
                tw2 = least_classes(m, res, 5, 10 * box)
                st = tw == tw2
                pos = sorted(frac_diff(position(r, m), s_apex) for r in tw[0][1])
                print('        charge +-%d: least |Q| = %d on %d class(es) %s; next %d; box doubled gives the same: %s'
                      % (qc, tw[0][0], len(tw[0][1]), tw[0][1], tw[1][0], st))
                print('                   positions from the apex: %s' % ', '.join(mp.nstr(p, 6) for p in pos))
                if name == '(6)':
                    sym = all(any(abs(frac_diff(-p, 0) - p2) < mp.mpf(10) ** -20 or abs(frac_diff(-p, 0) - p2 - 1) < mp.mpf(10) ** -20
                                  or abs(frac_diff(-p, 0) - p2 + 1) < mp.mpf(10) ** -20 for p2 in pos) for p in pos)
                    e4 = e4 and sym and st
                    if qc == 1:
                        e5 = e5 and len(pos) == 2 and all(abs(p) > mp.mpf('0.01') and abs(p - 1) > mp.mpf('0.01') for p in pos)
                    else:
                        e5 = e5 and len(pos) == 1 and abs(pos[0] - mp.mpf('0.5')) < mp.mpf(10) ** -20
    print('E3: %s' % ('HOLDS' if e3 else 'FAILS'))
    print('E4: %s' % ('HOLDS' if e4 else 'FAILS'))
    print('E5: %s' % ('HOLDS' if e5 else 'FAILS'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
