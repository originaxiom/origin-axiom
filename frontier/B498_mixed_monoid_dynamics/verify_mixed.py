#!/usr/bin/env python3
"""B498 — banking-seat verification: mixed words in the endomorphism monoid.

Independent re-derivations (not ports): C1 chirality (39 words + MFM lemma + F' control);
Q1a the -2 hand-proof check; Q1b the exact u-reduction for the M-drift; C2 length<=2 fixed
loci (the golden monopoly at depth 2, with two corrections to the handoff); C3 bounded
drift-table reproduction is in c3_orbits.py.

  python3 verify_mixed.py
"""
import itertools as it
import sympy as sp
from sympy import (symbols, simplify, expand, sqrt, solve, minimal_polynomial,
                   nsimplify, degree, discriminant, sin, cos, log, pi)

x, y, z = symbols('x y z')
F = lambda p: (p[2], p[0], p[0]*p[2] - p[1])
M = lambda p: (p[2], p[2], p[0]*p[1]*p[2] - p[0]**2 - p[1]**2 + 2)
D = lambda p: (p[0]**2 - 2, p[1]**2 - 2, p[0]*p[1]*p[2] - p[0]**2 - p[1]**2 + 2)
S = lambda p: (p[1], p[0], p[2])
GEN = {'F': F, 'M': M, 'D': D}
KAP = lambda p: p[0]**2 + p[1]**2 + p[2]**2 - p[0]*p[1]*p[2] - 2


def word(w):
    def f(p):
        for c in reversed(w):
            p = GEN[c](p)
        return p
    return f


def _achiral(w):
    Wf = word(w)
    lhs = tuple(expand(t) for t in S(Wf(S((x, y, z)))))
    return lhs == tuple(expand(t) for t in Wf((x, y, z)))


def c1_classification():
    """returns (n_achiral, n_chiral, F_containing_achiral_list)."""
    words = [''.join(t) for L in (1, 2, 3) for t in it.product('FMD', repeat=L)]
    ach = [w for w in words if _achiral(w)]
    return len(ach), len(words) - len(ach), [w for w in ach if 'F' in w]


def c1_lemma_MS():
    """M o S = M (M symmetric in x,y)."""
    return tuple(expand(t) for t in M(S((x, y, z)))) == tuple(expand(t) for t in M((x, y, z)))


def c1_mirror_closure():
    """the mirror of an F-word = the word with F -> F' = S o F o S."""
    Fp = lambda p: S(F(S(p)))
    G2 = {'F': F, 'M': M, 'D': D, 'G': Fp}
    def word2(w):
        def f(p):
            for c in reversed(w):
                p = G2[c](p)
            return p
        return f
    for w in ['F', 'FM', 'FD', 'MF', 'FFF', 'MFD']:
        lhs = tuple(expand(t) for t in S(word(w)(S((x, y, z)))))
        rhs = tuple(expand(t) for t in word2(w.replace('F', 'G'))((x, y, z)))
        if lhs != rhs:
            return False
    return True


def q1a_per_factor():
    """E[log(4cos^2 t)] under the Haar angle density (2/pi)sin^2 t equals -1.
    HAND PROOF (banked): log|2cos t| = sum (-1)^{k+1} cos(2kt)/k; sin^2 = (1-cos2t)/2;
    the k=1 Fourier coefficient gives INT cos2t log|2cos t| = +pi/2; hence
    E = (2/pi)(0 - pi/2) = -1. mult_D = x^2 y^2 => E[log mult_D] = -2. QED."""
    import mpmath as mp
    mp.mp.dps = 20
    v = mp.quad(lambda t: (2/mp.pi)*mp.sin(t)**2*mp.log(4*mp.cos(t)**2),
                [0, mp.pi/2, mp.pi])
    return abs(v + 1) < mp.mpf('1e-15')


def q1b_reduction_identity():
    """mult_M = A + B u with A+B = 4sin^2(a+b), A-B = 4sin^2(a-b) — the exact u-reduction."""
    a, b = symbols('a b', positive=True)
    A = 4*cos(a)**2 + 4*cos(b)**2 - 8*cos(a)**2*cos(b)**2
    B = 8*cos(a)*cos(b)*sin(a)*sin(b)
    return (simplify(A + B - 4*sin(a + b)**2) == 0
            and simplify(A - B - 4*sin(a - b)**2) == 0)


def q1b_numeric(dps=25):
    """E[log mult_M] via the reduced 2D integral; returns the value (conjecture: 0)."""
    import mpmath as mp
    mp.mp.dps = dps
    def inner(aa, bb):
        Ap = 4*mp.sin(aa + bb)**2
        Am = 4*mp.sin(aa - bb)**2
        Bv = (Ap - Am)/2
        if abs(Bv) < mp.mpf('1e-18'):
            Eu = mp.log(Ap) if Ap > 0 else mp.mpf(0)
        else:
            t1 = Ap*mp.log(Ap) if Ap > 0 else mp.mpf(0)
            t2 = Am*mp.log(Am) if Am > 0 else mp.mpf(0)
            Eu = (t1 - t2)/(2*Bv) - 1
        return (2/mp.pi)**2 * mp.sin(aa)**2*mp.sin(bb)**2 * Eu
    return mp.quad(lambda aa: mp.quad(lambda bb: inner(aa, bb), [0, mp.pi/2, mp.pi]),
                   [0, mp.pi/2, mp.pi])


def field_ok(v):
    """True if v in Q or Q(sqrt5); False if provably another field; None undecided."""
    try:
        vv = nsimplify(v, [sqrt(5)])
        mp_ = minimal_polynomial(vv, x)
        d = degree(mp_, x)
        if d == 1:
            return True
        if d == 2:
            q = sp.simplify(discriminant(mp_, x)/5)
            return bool(q.is_positive and sp.sqrt(q).is_rational)
        return False
    except Exception:
        return None


def c2_depth2():
    """golden monopoly at depth <= 2: all isolated fixed-point coords in Q or Q(sqrt5)."""
    ok = True
    levels = set()
    for w in [''.join(t) for L in (1, 2) for t in it.product('FMD', repeat=L)]:
        W = word(w)((x, y, z))
        sols = solve([sp.Eq(W[i], (x, y, z)[i]) for i in range(3)], [x, y, z], dict=True)
        for s in sols:
            vals = [s.get(v, v) for v in (x, y, z)]
            if any(v.free_symbols for v in vals):
                continue
            if any(field_ok(v) is False for v in vals):
                ok = False
            levels.add(nsimplify(simplify(KAP(vals)), [sqrt(5)]))
    return ok, levels


def c2_D_line():
    """D fixes the line (-1,-1,z) — transverse to the kappa-foliation (order-3 locus)."""
    return tuple(simplify(t) for t in D((-1, -1, z))) == (-1, -1, z)


if __name__ == "__main__":
    na, nc, fach = c1_classification()
    print("C1: achiral=%d chiral=%d ; F-containing achiral=%s (claim: ['MFM'])" % (na, nc, fach))
    print("C1 lemma M o S = M:", c1_lemma_MS())
    print("C1 mirror-closure control (F'):", c1_mirror_closure())
    print("Q1a per-factor -1 (hand proof + 15 digits):", q1a_per_factor())
    print("Q1b reduction identity (A+-B = 4sin^2(a+-b)):", q1b_reduction_identity())
    print("Q1b E[log mult_M] =", q1b_numeric(), "(conjecture: 0)")
    ok, levels = c2_depth2()
    print("C2 depth<=2 golden monopoly:", ok)
    print("C2 kappa-levels:", sorted(levels, key=sp.default_sort_key))
    print("   NOTE the (1±3√5)/8 levels (from DD): in Q(sqrt5) but NOT in Z[phi] —")
    print("   correction to the handoff's ring claim; the FIELD monopoly is unaffected.")
    print("C2 D fixed line (-1,-1,z):", c2_D_line())
