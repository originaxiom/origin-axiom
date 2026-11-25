#!/usr/bin/env python3
"""P-630, part B: the trace map linearised at B181's critical locus, along the metallic deviations, against B1788's
exponent set. Sealed and dependency-free: standard library, numpy and sympy; reads no file. Data-free.

    python3 -I p630_trace.py

Objects.
  The metallic trace maps (B471's family A_m; the golden m = 1 is B181's chain). For the substitution a -> a^m b,
  b -> a, with x = tr(B)/2, y = tr(A)/2, z = tr(AB)/2 and U_n the Chebyshev polynomials of the second kind,
      T_m(x, y, z) = (y, U_{m-1}(y) z - U_{m-2}(y) x, U_m(y) z - U_{m-1}(y) x),
  which preserves I = x^2 + y^2 + z^2 - 2xyz - 1. B181's critical locus is the family of surfaces I = V >= 0
  (V = lambda^2 / 4 for the Fibonacci operator of coupling lambda); V = 0 is its algebraic end (lambda = 0).
  The linearisation's spectrum: the eigenvalues of the Jacobian at a periodic point; in the substitution's own
  units, y = ln|mu| / ln(lambda_m) per step, lambda_m = (m + sqrt(m^2 + 4)) / 2.
  B1788's exponent set: on each of B1785's 41 line slopes alpha, the leading exponents of m2/m3 and m1/m3 in the
  up, down and lepton sectors and both readings, by B1788's tropical prediction (copied verbatim below from
  frontier/B1788_the_closed_form_of_the_exponents/verification/tropical.py at 88a1e9474, lines 11-52), with the
  closed form 1/2 - (||2 q_L alpha|| + ||2 q_R alpha||)/2 checked against it for m2/m3.

The reading of P-630's test, fixed here. An exponent set "lies in the spectrum" if every positive exponent on a line
equals u * y for one unit u > 0 (the unknown conversion from Im tau to ln length) and some y in the spectrum. Two
spectra are available on the critical locus:
  at V = 0, the fixed point (1, 1, 1) of every T_m;
  for V > 0, periodic orbits whose multipliers move with V (the six-cycle through (0, 0, sqrt(1 + V)) is computed).
Chirality per rung (reversing the substitution's orientation) inverts the multipliers, y -> -y, and adds nothing to
a spectrum that is symmetric. B434's filling slope changes the manifold, not the map, and is not a direction here.

Cells and expectations, written before the run (probabilities are this seat's):
  C1 exact: for m = 1 to 8, T_m preserves I, fixes (1, 1, 1), and its Jacobian there has characteristic polynomial
     (mu + 1)(mu^2 - (m^2 + 2) mu + 1): eigenvalues lambda_m^2, -1, lambda_m^-2, so y in {2, 0, -2} for every m and
     the V direction (|mu| = 1) is marginal (97 %).
  C2 exact: the Jacobian of T_1^6 at (0, 0, a), a = sqrt(1 + V), has the eigenvalue 1 and a pair mu, 1/mu; at V = 0,
     mu = phi^6 = 9 + 4 sqrt(5); on V in [0, 10], mu increases with V (90 %).
  C3 control, matched to the method: the off-diagonal Fibonacci chain (bonds r and 1 along the Fibonacci word) has
     transfer matrices R(t) = [[E/t, -t], [1/t, 0]], and at E = 0 its traces start on the six-cycle with
     V = (r - 1/r)^2 / 4. The band around E = 0 of the periodic approximant whose period is the Fibonacci word w_k
     (w_0 = b, w_1 = a, w_{k+1} = w_k w_{k-1}), found from direct products of R (not from the trace map), has width
     W_k for k = 0, 1 mod 3 up to 27; W_{k+6} / W_k approaches 1/mu(V) within 1 % at the largest k computed, for
     r = 2 and r = 5/4 (85 %).
  C4 sanity: the tropical m2/m3 exponent equals the closed form in all 41 x 3 x 2 cases (99 %).
  C5 V = 0, one direction: the positive exponents of a line lie in u {2, -2} only if they are all equal. Lines where
     this holds, with the m2/m3 set and with the m2/m3 and m1/m3 set together: at most 3 of 41 each (85 %).
  C6 V = 0, all metallic directions: ln(lambda_m) / ln(lambda_n) is rational only within one quadratic field, where
     it is a ratio of odd integers (metallic means are odd powers of the field's unit of norm -1). So a line's
     positive exponents lie in the spectrum iff each is an odd multiple of their greatest common divisor. Expected:
     fails on both lines carrying B1788's up and down pair (3/10, 1/5), alpha = 2/5 and 1/10 (99 %); holds on fewer
     than 10 of the 41 lines with the m2/m3 set (70 %).
  C7 V > 0: mu(V) takes every value in [phi^6, mu(10)] once, so on that range any one exponent ratio is matched by one
     choice of V. The comparison is not posed until the record fixes V. (A statement that follows from C2; printed.)
"""
import math
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

# ---- verbatim from frontier/B1788_the_closed_form_of_the_exponents/verification/tropical.py at 88a1e9474,
# ---- lines 11-52 (import of itertools added above the block)
import itertools
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
SECTORS = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
I = sp.I
QI = sp.Matrix([[I, 0], [0, -I]]); QJ = sp.Matrix([[0, 1], [-1, 0]]); QK = QI * QJ; EPS = QJ
BL = [QJ, QI, QK]
s, p, r = sp.symbols("s p r")                 # S = [[s, p], [r, -s]]
m00, m01, m10, m11 = sp.symbols("m00 m01 m10 m11")
SVARS = (s, p, r); MVARS = (m00, m01, m10, m11)


def polys(reading):
    S = sp.Matrix([[s, p], [r, -s]]) if reading == "S" else sp.Matrix([[s, r], [p, -s]])   # S~: the big entry moves to (1, 0)
    M = sp.Matrix([[m00, m01], [m10, m11]])
    Y = sp.Matrix(3, 3, lambda a, b: sp.expand(sum((BL[a].T * EPS * S * BL[b]).multiply_elementwise(M))))
    ents = [Y[a, b] for a in range(3) for b in range(3)]
    mins = [sp.expand(Y.extract(list(R_), list(C_)).det()) for R_ in itertools.combinations(range(3), 2) for C_ in itertools.combinations(range(3), 2)]
    det = sp.expand(Y.det())
    def monos(P):
        P = sp.Poly(P, *SVARS, *MVARS); return [m for m, c in P.terms() if c != 0]
    return [monos(e) for e in ents if e != 0], [monos(m) for m in mins if m != 0], monos(det)


SEXP = {"s": Fr(1, 8), "p": Fr(-1, 8), "r": Fr(3, 8)}


def trop(monolist, mu):
    ex = [SEXP["s"], SEXP["p"], SEXP["r"], mu[0], mu[1], mu[2], mu[3]]
    return min(sum(k * e for k, e in zip(m, ex)) for m in monolist)


def nd(x): x = x % 1; return min(x, 1 - x)


def E(ax, ay):
    return [nd(ax) ** 2 + nd(ay) ** 2 - Fr(1, 8), nd(ax) ** 2 + nd(ay + Fr(1, 2)) ** 2 - Fr(1, 8),
            nd(ax + Fr(1, 2)) ** 2 + nd(ay) ** 2 - Fr(1, 8), nd(ax + Fr(1, 2)) ** 2 + nd(ay + Fr(1, 2)) ** 2 - Fr(1, 8)]


def predict(P, mu):
    ents, mins, det = P
    e1 = min(trop(m, mu) for m in ents); e12 = min(trop(m, mu) for m in mins); e123 = trop(det, mu)
    return e12 - 2 * e1, (e123 - e12) - e1
# ---- end of the verbatim block


PHI = (1 + 5 ** 0.5) / 2
X_, Y_, Z_, MU = sp.symbols("x y z mu")
ALPHAS = ["0", "1/20", "1/15", "1/14", "1/13", "1/12", "1/11", "1/10", "1/9", "1/8", "2/15", "1/7", "3/20", "2/13",
          "1/6", "2/11", "1/5", "3/14", "2/9", "3/13", "1/4", "4/15", "3/11", "2/7", "3/10", "4/13", "1/3", "7/20",
          "5/14", "4/11", "3/8", "5/13", "2/5", "5/12", "3/7", "4/9", "9/20", "5/11", "6/13", "7/15", "1/2"]


def U(n, t):
    """Chebyshev U_n(t), with U_{-2} = -1 and U_{-1} = 0."""
    if n == -2:
        return sp.Integer(-1)
    a, b = sp.Integer(0), sp.Integer(1)
    if n == -1:
        return a
    for _ in range(n):
        a, b = b, sp.expand(2 * t * b - a)
    return b


def Tm(m):
    x, y, z = X_, Y_, Z_
    return sp.Matrix([y, U(m - 1, y) * z - U(m - 2, y) * x, U(m, y) * z - U(m - 1, y) * x])


def fricke(v):
    return v[0] ** 2 + v[1] ** 2 + v[2] ** 2 - 2 * v[0] * v[1] * v[2] - 1


def cell_C1():
    ok = True
    for m in range(1, 9):
        T = Tm(m)
        inv = sp.expand(fricke(T) - fricke([X_, Y_, Z_])) == 0
        fixed = list(T.subs({X_: 1, Y_: 1, Z_: 1})) == [1, 1, 1]
        J = T.jacobian([X_, Y_, Z_]).subs({X_: 1, Y_: 1, Z_: 1})
        cp = sp.expand(J.charpoly(MU).as_expr())
        want = sp.expand((MU + 1) * (MU ** 2 - (m ** 2 + 2) * MU + 1))
        lam = (m + math.sqrt(m * m + 4)) / 2
        ev = sorted(complex(e).real for e in sp.Poly(cp, MU).nroots())
        ys = [math.log(abs(e)) / math.log(lam) for e in ev]
        good = inv and fixed and sp.expand(cp - want) == 0
        ok &= good
        print("C1 m=%d: invariant %s, fixes (1,1,1) %s, charpoly %s; eigenvalues %s; y = %s"
              % (m, inv, fixed, cp, " ".join("%.6g" % e for e in ev), " ".join("%+.6f" % v for v in ys)))
    return ok


def six_cycle():
    """Jacobian of T_1^6 at (0, 0, a), its characteristic polynomial, and mu(V)."""
    a = sp.symbols("a", positive=True)
    T = Tm(1)
    p = sp.Matrix([0, 0, a])
    J = sp.eye(3)
    for _ in range(6):
        J = T.jacobian([X_, Y_, Z_]).subs({X_: p[0], Y_: p[1], Z_: p[2]}) * J
        p = T.subs({X_: p[0], Y_: p[1], Z_: p[2]})
    assert list(p) == [0, 0, a]
    cp = sp.factor(J.charpoly(MU).as_expr())
    return a, J, cp


def mu_of_V(cp, a, V):
    roots = sp.Poly(cp.subs(a, sp.sqrt(1 + sp.nsimplify(V))), MU).nroots(n=30)
    return max(abs(complex(r)) for r in roots)


def cell_C2(a, cp):
    has1 = sp.simplify(cp.subs(MU, 1)) == 0
    mu0 = mu_of_V(cp, a, 0)
    exact0 = abs(mu0 - (9 + 4 * 5 ** 0.5)) < 1e-12
    Vs = np.linspace(0, 10, 201)
    mus = [mu_of_V(cp, a, float(v)) for v in Vs]
    mono = all(mus[i + 1] > mus[i] for i in range(len(mus) - 1))
    print("C2 charpoly of D(T_1^6) at (0, 0, a): %s" % cp)
    print("C2 eigenvalue 1: %s; mu(0) = %.12f (phi^6 = %.12f); mu increases on [0, 10]: %s; mu(10) = %.6g"
          % (has1, mu0, 9 + 4 * 5 ** 0.5, mono, mus[-1]))
    return has1 and exact0 and mono, mus[-1]


def R(E, t):
    return np.array([[E / t, -t], [1 / t, 0.0]])


def word(k):
    w = ["b", "a"]
    for _ in range(k - 1):
        w.append(w[-1] + w[-2])
    return w[k]


def half_trace(E, w, r):
    """tr(R(l_L) ... R(l_1)) / 2 for the word w, bonds a -> r and b -> 1; E may be an array."""
    E = np.atleast_1d(np.asarray(E, float))
    m00, m01, m10, m11 = np.ones_like(E), np.zeros_like(E), np.zeros_like(E), np.ones_like(E)
    for ch in w:
        t = r if ch == "a" else 1.0
        m00, m01, m10, m11 = (E / t) * m00 - t * m10, (E / t) * m01 - t * m11, m00 / t, m01 / t
    return 0.5 * (m00 + m11)


def band_edge(w, r):
    """The least E > 0 with |x(E)| = 1, where x(0) = 0 (the band around E = 0 is [-E, E] by the chain's symmetry)."""
    grid = np.geomspace(1e-14, 2.0, 3000)
    with np.errstate(over="ignore", invalid="ignore"):
        x = np.abs(half_trace(grid, w, r))
    j = int(np.argmax(x > 1))
    assert j > 0 and x[j] > 1 and np.all(x[:j] <= 1)
    lo, hi = grid[j - 1], grid[j]
    for _ in range(5):
        g = np.linspace(lo, hi, 201)
        with np.errstate(over="ignore", invalid="ignore"):
            x = np.abs(half_trace(g, w, r))
        j = int(np.argmax(x > 1))
        assert j > 0 and x[j] > 1
        lo, hi = g[j - 1], g[j]
    return 0.5 * (lo + hi)


def cell_C3(a, cp):
    ok = True
    for r in (2.0, 1.25):
        V = (r - 1 / r) ** 2 / 4
        mu = mu_of_V(cp, a, V)
        x0 = [half_trace(0.0, word(k), r)[0] for k in range(0, 4)]
        ks = [k for k in range(6, 28) if k % 3 in (0, 1)]
        W = {k: 2 * band_edge(word(k), r) for k in ks}
        ratios = [(k, W[k + 6] / W[k]) for k in ks if k + 6 in W]
        kl, last = ratios[-1]
        good = abs(last * mu - 1) < 0.01
        ok &= good
        print("C3 r=%.2f V=%.6f: traces at E=0, k=0..3: %s; 1/mu(V) = %.8e" % (r, V, np.round(x0, 6), 1 / mu))
        for k, q in ratios:
            print("     W_%d/W_%d = %.8e   (ratio to 1/mu: %.6f)" % (k + 6, k, q, q * mu))
        print("C3 r=%.2f: at k = %d, |W ratio * mu - 1| = %.2e -> %s" % (r, kl, abs(last * mu - 1), good))
    return ok


def exponent_sets():
    P = {rd: polys(rd) for rd in ("S", "St")}
    sets, sanity = {}, True
    for al in ALPHAS:
        a = Fr(al)
        e2s, e3s = [], []
        for sec, (lf, rf) in SECTORS.items():
            ql, qr = SIXY[lf], SIXY[rf]
            mu = E(ql * a, qr * a)
            for rd in ("S", "St"):
                e2, e3 = predict(P[rd], mu)
                sanity &= e2 == Fr(1, 2) - (nd(2 * ql * a) + nd(2 * qr * a)) / 2
                e2s.append(e2)
                e3s.append(e3)
        sets[al] = (e2s, e3s)
    return sets, sanity


def gcd_frac(v):
    den = 1
    for x in v:
        den = den * x.denominator // math.gcd(den, x.denominator)
    g = 0
    for x in v:
        g = math.gcd(g, int(x * den))
    return Fr(g, den)


def odd_multiples(v):
    v = [x for x in v if x > 0]
    if not v:
        return True
    g = gcd_frac(v)
    return all((x / g).denominator == 1 and (x / g).numerator % 2 == 1 for x in v)


def all_equal(v):
    v = {x for x in v if x > 0}
    return len(v) <= 1


def main():
    res = {"C1": cell_C1()}
    a, J, cp = six_cycle()
    res["C2"], mu10 = cell_C2(a, cp)
    res["C3"] = cell_C3(a, cp)
    sets, res["C4"] = exponent_sets()
    print("C4 tropical m2/m3 = closed form in all %d cases: %s" % (len(ALPHAS) * 6, res["C4"]))
    c5 = {"m2/m3": 0, "both": 0}
    c6 = {"m2/m3": 0, "both": 0}
    print("\nper line: alpha | m2/m3 exponents (up S, up St, down S, down St, lep S, lep St) | m1/m3 exponents |"
          " C5 (m2/m3, both) | C6 (m2/m3, both)")
    for al in ALPHAS:
        e2, e3 = sets[al]
        f5 = (all_equal(e2), all_equal(e2 + e3))
        f6 = (odd_multiples(e2), odd_multiples(e2 + e3))
        c5["m2/m3"] += f5[0]; c5["both"] += f5[1]
        c6["m2/m3"] += f6[0]; c6["both"] += f6[1]
        print("  %-5s | %s | %s | %s %s | %s %s" % (al, " ".join(str(x) for x in e2), " ".join(str(x) for x in e3),
                                                 *f5, *f6))
    allpos2 = sorted({x for al in ALPHAS for x in sets[al][0] if x > 0})
    allpos = sorted({x for al in ALPHAS for s in sets[al] for x in s if x > 0})
    print("\nC5 lines where the positive exponents are all equal: m2/m3 %d of 41, both %d of 41; across all lines,"
          " %d distinct positive m2/m3 values" % (c5["m2/m3"], c5["both"], len(allpos2)))
    res["C5"] = c5["m2/m3"] <= 3 and c5["both"] <= 3
    pair_lines = [al for al in ("2/5", "1/10") if not odd_multiples(sets[al][0])]
    print("C6 lines where the positive exponents are odd multiples of their gcd: m2/m3 %d of 41, both %d of 41;"
          " fails on alpha = 2/5 and 1/10 (m2/m3): %s; across all lines together: m2/m3 %s, both %s"
          % (c6["m2/m3"], c6["both"], pair_lines == ["2/5", "1/10"], odd_multiples(allpos2), odd_multiples(allpos)))
    res["C6"] = pair_lines == ["2/5", "1/10"] and c6["m2/m3"] < 10
    print("C7 mu(V) is increasing from phi^6 = %.6f at V = 0 to %.6g at V = 10 (C2): any one ratio in that range is"
          " matched by one V" % (9 + 4 * 5 ** 0.5, mu10))
    print("\n" + ", ".join("%s %s" % (k, "holds" if v else "FAILS") for k, v in res.items()))


if __name__ == "__main__":
    main()
