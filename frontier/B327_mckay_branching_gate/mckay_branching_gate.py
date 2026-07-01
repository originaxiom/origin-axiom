"""B327 — the hierarchy CRUX = 27|_2T self-duality (Chat-1 handoff, verified + sharpened).

Two computations, both in-sandbox:
  (1) E6 27 principal-SL(2) decomposition, from the Weyl orbit of omega_1 + principal grading.
      Resolves the cross-chat contradiction: it is V(16)+V(8)+V(0) (spins 8,4,0) -- Chat-2 right,
      Chat-1's 9V0+6V1 wrong.
  (2) 2T (24 Hurwitz quaternions): the two order-3 classes share SU(2) trace -1, so any
      SU(2)-restricted (hence self-dual) character is equal on them => n1 = n2. Half-integer
      spins do NOT escape this -- self-duality, not integrality, is the forcing.
Firewalled: decides which LEVEL the hierarchy lives at, not any mass value. Nothing to CLAIMS.
"""
import sympy as sp
import itertools
from collections import Counter

# --- (1) E6 principal decomposition of the 27 ------------------------------------------
A = sp.Matrix([
    [2, 0, -1, 0, 0, 0],
    [0, 2, 0, -1, 0, 0],
    [-1, 0, 2, -1, 0, 0],
    [0, -1, -1, 2, -1, 0],
    [0, 0, 0, -1, 2, -1],
    [0, 0, 0, 0, -1, 2]])
N = 6


def principal_decomposition():
    r = 2 * (A.inv() * sp.Matrix([1] * N))          # grade(mu) = mu . r
    start = (1, 0, 0, 0, 0, 0)
    orbit, frontier = {start}, [start]
    while frontier:
        mu = frontier.pop()
        for i in range(N):
            nu = tuple(mu[j] - mu[i] * A[i, j] for j in range(N))
            if nu not in orbit:
                orbit.add(nu); frontier.append(nu)
    grades = Counter(int(sum(mu[i] * r[i] for i in range(N))) for mu in orbit)
    spins, mult = Counter(), Counter(grades)
    while any(v > 0 for v in mult.values()):
        top = max(k for k, v in mult.items() if v > 0)
        for k in range(-top, top + 1, 2):
            mult[k] -= 1
        spins[sp.Rational(top, 2)] += 1
    return len(orbit), dict(grades), dict(spins)


def U_at(nn, x):
    """spin-j SU(2) character U_{2j}(x) at x=cos(phi/2); here evaluated symbolically for x=-1/2, -1."""
    # U_n(-1/2): period-3 pattern {0:1, 1:-1, 2:0}; U_n(-1) = (n+1)*(-1)^n
    if x == sp.Rational(-1, 2):
        return {0: 1, 1: -1, 2: 0}[nn % 3]
    if x == -1:
        return (nn + 1) * (-1) ** nn
    raise ValueError


def characters(spins):
    chi_g = sum(m * U_at(int(2 * j), sp.Rational(-1, 2)) for j, m in spins.items())  # order-3 elt
    chi_m1 = sum(m * U_at(int(2 * j), -1) for j, m in spins.items())                 # -I
    return chi_g, chi_m1


# --- (2) 2T from Hurwitz quaternions: order-3 classes share SU(2) trace ----------------
def qmul(a, b):
    w1, x1, y1, z1 = a; w2, x2, y2, z2 = b
    return (w1*w2 - x1*x2 - y1*y2 - z1*z2, w1*x2 + x1*w2 + y1*z2 - z1*y2,
            w1*y2 - x1*z2 + y1*w2 + z1*x2, w1*z2 + x1*y2 - y1*x2 + z1*w2)


def two_T_classes():
    h = sp.Rational(1, 2)
    elts = set()
    for p in itertools.permutations(range(4)):
        for s in (1, -1):
            v = [0, 0, 0, 0]; v[p[0]] = s; elts.add(tuple(v))
    for signs in itertools.product((h, -h), repeat=4):
        elts.add(tuple(signs))
    elts = list(elts)
    assert len(elts) == 24

    def conj(g, x):
        gi = (g[0], -g[1], -g[2], -g[3])
        return qmul(qmul(g, x), gi)
    seen, classes = set(), []
    for x in elts:
        if x in seen:
            continue
        cl = frozenset(conj(g, x) for g in elts)
        classes.append(cl); seen |= cl

    def order(x):
        p, one = x, (1, 0, 0, 0)
        for k in range(1, 13):
            if p == one:
                return k
            p = qmul(p, x)
    # (class size, SU(2) trace 2w, order) per class
    return sorted((len(c), 2 * next(iter(c))[0], order(next(iter(c)))) for c in classes)


if __name__ == '__main__':
    size, grades, spins = principal_decomposition()
    print("orbit:", size, " principal spins:", spins)
    print("grades:", grades)
    chi_g, chi_m1 = characters(spins)
    print("chi_27(order-3)=", chi_g, "(real => n1=n2)   chi_27(-I)=", chi_m1)
    print("2T classes (size, SU(2)-trace, order):")
    for row in two_T_classes():
        print("  ", row)
