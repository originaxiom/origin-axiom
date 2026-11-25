#!/usr/bin/env python3
"""POST HOC (written after the referee read of part B; p630_trace_out.txt had been read): part B's test redone with
the whole spectrum at V = 0, both units and the readings kept apart. Imports p630_trace.py from the same folder for
the maps and B1788's exponents. Data-free; reads no file but that script.

    python3 -I p630_trace_posthoc.py

The referee's point: (1, 1, 1) is the cone point of the Cayley cubic I = 0, and its spectrum (y = 2, 0, -2) is the
square of the torus map's. Every smooth periodic orbit of I = 0 should have y = 1 and -1 (and a multiplier of modulus
1). This script:
  P1 the fixed point for general m: the Jacobian of T_m at (1, 1, 1) and its characteristic polynomial, with m a symbol
     (U_n(1) = n + 1, U_n'(1) = n (n + 1)(n + 2) / 3);
  P2 smooth periodic orbits on I = 0 for m = 1, 2, 3: points from commuting pairs (x, y, z) = (cos b, cos a,
     cos(a + b)) with (a, b) rational multiples of 2 pi, denominators 5, 7, 9, 11, 13, away from the cone points; on
     the angles T_m acts as (a, b) -> (m a + b, a). For each orbit (period p, up to the sign of the angles), the
     eigenvalues of the Jacobian of T_m^p and y = ln|mu| / (p ln lambda_m);
  P3 the recount. With y in {1, 2} at V = 0 (the smooth orbits and the cone point), a line's positive exponents lie in
     the spectrum if, for one unit u,
       (L) in units of ln length (y in the substitution's own units, the same for every m): each is u or 2u;
       (S) in units of one substitution step common to every m (y ln lambda_m, any metallic m): each is c n with n odd
           or twice odd, which holds iff every exponent over the set's gcd has 2-adic valuation at most 1;
     for the m2/m3 set and for the m2/m3 and m1/m3 set, with the readings S and S~ pooled, and with them apart (a line
     passes if either reading's set passes); and with one unit for every line (the union of the lines' sets). The
     pre-registered C5 and C6 (y = 2 only) are printed beside, readings apart.
  P4 B1788's domain: the slopes at which some sector has q alpha in (1/2) Z, where B1788's closed form can be excluded
     or degenerate depending on the line's second coordinate; the counts are printed with those slopes left out.
No expectation is stated; it is a recount, labelled post hoc.
"""
import importlib.util
import math
import pathlib
import sys
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("trace", pathlib.Path(__file__).resolve().parent / "p630_trace.py")
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)


def p1():
    m, n = sp.symbols("m n", integer=True, positive=True)
    U1 = lambda k: k + 1
    dU1 = lambda k: sp.Rational(1, 3) * k * (k + 1) * (k + 2)
    # T_m(x, y, z) = (y, U_{m-1}(y) z - U_{m-2}(y) x, U_m(y) z - U_{m-1}(y) x), differentiated at (1, 1, 1)
    J = sp.Matrix([[0, 1, 0],
                   [-U1(m - 2), dU1(m - 1) - dU1(m - 2), U1(m - 1)],
                   [-U1(m - 1), dU1(m) - dU1(m - 1), U1(m)]]).applyfunc(sp.expand)
    mu = sp.symbols("mu")
    cp = sp.factor(J.charpoly(mu).as_expr())
    ok = all(sp.simplify(J.subs(m, k) - B.Tm(k).jacobian([B.X_, B.Y_, B.Z_]).subs({B.X_: 1, B.Y_: 1, B.Z_: 1})) ==
             sp.zeros(3, 3) for k in range(1, 9))
    print("P1 Jacobian of T_m at (1,1,1): %s; charpoly %s; equals the m = 1..8 Jacobians: %s" % (J.tolist(), cp, ok))


def p2():
    for m in (1, 2, 3):
        T = B.Tm(m)
        f = sp.lambdify((B.X_, B.Y_, B.Z_), list(T), "numpy")
        Jf = sp.lambdify((B.X_, B.Y_, B.Z_), T.jacobian([B.X_, B.Y_, B.Z_]), "numpy")
        lam = (m + math.sqrt(m * m + 4)) / 2
        seen, ys = set(), []
        for N in (5, 7, 9, 11, 13):
            for i in range(N):
                for j in range(N):
                    th = (i % N, j % N)
                    if (2 * th[0]) % N == 0 and (2 * th[1]) % N == 0:
                        continue                                    # a cone point (the angles are fixed by -1)
                    key = min(th, ((-th[0]) % N, (-th[1]) % N))
                    if (N, key) in seen:
                        continue
                    orbit, cur = [], th
                    while True:
                        k = min(cur, ((-cur[0]) % N, (-cur[1]) % N))
                        if (N, k) in seen:
                            break
                        seen.add((N, k))
                        orbit.append(cur)
                        cur = ((m * cur[0] + cur[1]) % N, cur[0])
                    if not orbit:
                        continue
                    a, b = 2 * math.pi * orbit[0][0] / N, 2 * math.pi * orbit[0][1] / N
                    v = np.array([math.cos(b), math.cos(a), math.cos(a + b)])
                    J = np.eye(3)
                    for _ in range(len(orbit)):
                        J = np.array(Jf(*v), float) @ J
                        v = np.array(f(*v), float)
                    ev = np.linalg.eigvals(J)
                    y = sorted(math.log(abs(e)) / (len(orbit) * math.log(lam)) for e in ev)
                    ys.append((N, len(orbit), tuple(round(t, 9) for t in y)))
        distinct = sorted({t[2] for t in ys})
        print("P2 m=%d: %d smooth periodic orbits on I = 0 (denominators 5 to 13, periods %s); distinct y-sets: %s"
              % (m, len(ys), sorted({t[1] for t in ys}), distinct))


def v2(k):
    k = abs(k)
    c = 0
    while k and k % 2 == 0:
        k //= 2
        c += 1
    return c


def passes_S(v):
    v = [x for x in v if x > 0]
    if not v:
        return True
    g = B.gcd_frac(v)
    return all((x / g).denominator == 1 and v2((x / g).numerator) <= 1 for x in v)


def passes_L(v):
    v = sorted({x for x in v if x > 0})
    if len(v) <= 1:
        return True
    return len(v) == 2 and v[1] == 2 * v[0]


def domain_sensitive(al):
    a = Fr(al)
    for lf, rf in B.SECTORS.values():
        for q in (B.SIXY[lf], B.SIXY[rf]):
            if (q * a) % Fr(1, 2) == 0:
                return True
    return False


def p3():
    sets, _ = B.exponent_sets()
    # the order inside each list: up S, up St, down S, down St, lep S, lep St
    def by_reading(lst, rd):
        return [x for i, x in enumerate(lst) if i % 2 == (0 if rd == "S" else 1)]
    rules = {"(L) ln length, y in {1, 2}": passes_L, "(S) one step, y in {1, 2}": passes_S,
             "C5 as sealed, y = 2": B.all_equal, "C6 as sealed, y = 2": B.odd_multiples}
    sens = [al for al in B.ALPHAS if domain_sensitive(al)]
    print("P4 slopes where some sector has q alpha in (1/2) Z: %s" % sens)
    for rname, rule in rules.items():
        for setname in ("m2/m3", "both"):
            cnt = {"pooled": [], "apart": []}
            for al in B.ALPHAS:
                e2, e3 = sets[al]
                full = e2 if setname == "m2/m3" else e2 + e3
                cnt["pooled"].append(al) if rule(full) else None
                sep = []
                for rd in ("S", "St"):
                    s = by_reading(e2, rd) + ([] if setname == "m2/m3" else by_reading(e3, rd))
                    sep.append(rule(s))
                cnt["apart"].append(al) if any(sep) else None
            union = [x for al in B.ALPHAS for x in (sets[al][0] if setname == "m2/m3" else sets[al][0] + sets[al][1])]
            union_ok = rule(union)
            union_apart = any(rule([x for al in B.ALPHAS for x in (by_reading(sets[al][0], rd) + (
                [] if setname == "m2/m3" else by_reading(sets[al][1], rd)))]) for rd in ("S", "St"))
            for mode in ("pooled", "apart"):
                L = cnt[mode]
                print("P3 %-28s %-5s readings %-6s: %2d of 41 lines %s; outside the P4 slopes %d of %d; one unit for"
                      " every line: %s" % (rname, setname, mode, len(L), L, len([x for x in L if x not in sens]),
                                           41 - len(sens), union_ok if mode == "pooled" else union_apart))


if __name__ == "__main__":
    p1()
    p2()
    p3()
