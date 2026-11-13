#!/usr/bin/env python3
"""W-C8, part 1: main's tick-parity check computed a second time on this seat's own code, and the metallic ticks.

Data-free; integer matrices only. Main's tick_parity.py is not opened or run.

    python3 -I -u wc8_part1_checks.py

DEFINITIONS (M19's words, this seat's code):
  J_m = [[m, 1], [1, 0]] (the metallic tick, det -1); A_m = J_m^2 (the metallic ground); N = m^2 + 4 = det(A_m + I).
  K = [[0, 1], [-1, 0]]. The golden case m = 1: J = J_1, A = LR = [[2, 1], [1, 1]].
  The normaliser of <A> in GL2(Z): X with det X = +-1 and X A X^-1 = A or A^-1; classes modulo <A>.
  The mark at level N: a vector v mod N of order N with A v = -v (mod N), taken as the line {k v}. For X in the
  normaliser that keeps the line, its scalar mu (X v = mu v mod N) and its hand: + if mu = +-1, - if mu = +-lambda,
  where lambda is J_m's scalar.

EXPECTATIONS, written before the run (derived by hand by this seat from the definitions):
  P1  Golden case: the search (entries |x| <= 12) finds the normaliser of <LR> in exactly 8 classes modulo <LR>, namely
      +-J^n K^e (n, e in {0, 1}); and J^2 = LR, K^2 = -I, K J K^-1 = -J^-1 exactly.
  P2  At the mark (the line of (1, 2) mod 5): J acts by 3 and K by 2 (3 * 2 = 1 and 3^2 = 2^2 = -1 mod 5), and the hand of
      +-J^n K^e is (-1)^(n+e) on all 8 classes. Control: the law (-1)^n alone fails on some class.
  P3  Metallic m = 1 to 12: A_m + I has Smith form diag(1, N) for odd m and diag(2, N/2) for even m. So a line of order
      N sent to its opposite exists exactly for odd m: v = (m, 2) mod N. Planted error: a test that accepts any nonzero
      kernel vector, whatever its order, accepts every m.
  P4  For odd m: J_m keeps the line with scalar lambda = m * 2^-1 mod N, lambda^2 = -1 mod N, and K keeps it with
      scalar -lambda; lambda is not +-1 mod N; so the hand of +-J_m^n K^e is (-1)^(n+e).
  P5  For m = 1 to 5 the search (entries |x| <= 30) finds the normaliser of <A_m> in exactly the 8 classes
      +-J_m^n K^e modulo <A_m>.
"""
import itertools
from math import gcd

import numpy as np
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form


def say(*a):
    print(*a, flush=True)


def Jm(m):
    return np.array([[m, 1], [1, 0]], dtype=object)


K = np.array([[0, 1], [-1, 0]], dtype=object)
I2 = np.eye(2, dtype=object)


def inv(X):
    a, b, c, d = X.ravel()
    det = a * d - b * c
    return det * np.array([[d, -b], [-c, a]], dtype=object)


def det(X):
    return X[0, 0] * X[1, 1] - X[0, 1] * X[1, 0]


def eq(X, Y):
    return all(int(x) == int(y) for x, y in zip(X.ravel(), Y.ravel()))


def mpow(X, n):
    P = I2.copy()
    B = X if n >= 0 else inv(X)
    for _ in range(abs(n)):
        P = P.dot(B)
    return P


def normaliser_classes(A, bound, kmax):
    Ai = inv(A)
    p, q, r, s = (int(x) for x in A.ravel())
    pi, qi, ri, si = (int(x) for x in Ai.ravel())
    found = []
    rng = range(-bound, bound + 1)
    for a, b, c, d in itertools.product(rng, repeat=4):
        dt = a * d - b * c
        if dt != 1 and dt != -1:
            continue
        xa = (a * p + b * r, a * q + b * s, c * p + d * r, c * q + d * s)
        if xa == (p * a + q * c, p * b + q * d, r * a + s * c, r * b + s * d) or \
                xa == (pi * a + qi * c, pi * b + qi * d, ri * a + si * c, ri * b + si * d):
            found.append(np.array([[a, b], [c, d]], dtype=object))
    powers = [mpow(A, k) for k in range(-kmax, kmax + 1)]
    classes = []
    for X in found:
        if not any(any(eq(X, Y.dot(P)) for P in powers) for Y in classes):
            classes.append(X)
    return found, classes


def named(Jt, A, kmax):
    names = {}
    for s in (1, -1):
        for n in (0, 1):
            for e in (0, 1):
                names[(s, n, e)] = s * mpow(Jt, n).dot(mpow(K, e))
    return names


def which(X, names, A, kmax):
    powers = [mpow(A, k) for k in range(-kmax, kmax + 1)]
    for key_, Y in names.items():
        if any(eq(X, Y.dot(P)) for P in powers):
            return key_
    return None


# ---- P1
J = Jm(1)
A = J.dot(J)
LR = np.array([[2, 1], [1, 1]], dtype=object)
rel = eq(A, LR) and eq(K.dot(K), -I2) and eq(K.dot(J).dot(inv(K)), -inv(J))
found, classes = normaliser_classes(LR, 12, 12)
names = named(J, LR, 12)
idx = [which(X, names, LR, 12) for X in classes]
say("P1 normaliser elements found:", len(found), "; classes modulo <LR>:", len(classes), "; named as +-J^n K^e:", sorted(idx))
say("P1 relations J^2 = LR, K^2 = -I, K J K^-1 = -J^-1:", rel)
p1 = rel and len(classes) == 8 and None not in idx and len(set(idx)) == 8
say("P1 holds:", p1)


# ---- P2, P4 helpers
def scalar(X, v, N):
    w = [int(x) % N for x in X.dot(np.array(v, dtype=object))]
    for mu in range(N):
        if all((mu * int(v[i]) - w[i]) % N == 0 for i in range(2)):
            return mu
    return None


v5 = (1, 2)
sJ, sK = scalar(J, v5, 5), scalar(K, v5, 5)
hands = {}
for key_, Y in names.items():
    mu = scalar(Y, v5, 5)
    hands[key_] = 1 if mu in (1, 4) else -1 if mu in (2, 3) else None
law = all(hands[(s, n, e)] == (-1) ** (n + e) for (s, n, e) in hands)
ctrl = all(hands[(s, n, e)] == (-1) ** n for (s, n, e) in hands)
say("P2 J acts by", sJ, "; K by", sK, "; hands (sign, n, e) -> hand:", {k: hands[k] for k in sorted(hands)})
say("P2 the parity law (-1)^(n+e) holds on all 8:", law, "; control (-1)^n holds on all 8:", ctrl)
say("P2 holds:", sJ == 3 and sK == 2 and law and not ctrl)

# ---- P3, P4
p3 = p4 = True
planted_all = True
for m in range(1, 13):
    Jt = Jm(m)
    Am = Jt.dot(Jt)
    N = m * m + 4
    S = smith_normal_form(Matrix([[int(x) for x in row] for row in (Am + I2)]))
    d1, d2 = abs(int(S[0, 0])), abs(int(S[1, 1]))
    kernel = [(x, y) for x in range(N) for y in range(N)
              if (x, y) != (0, 0) and all(int(z) % N == 0 for z in (Am + I2).dot(np.array([x, y], dtype=object)))]
    full = [v for v in kernel if gcd(gcd(v[0], v[1]), N) == 1]
    planted_all &= len(kernel) > 0
    want_smith = (1, N) if m % 2 else (2, N // 2)
    line_exists = len(full) > 0
    p3 &= (d1, d2) == want_smith and line_exists == (m % 2 == 1)
    msg = "m %2d N %3d Smith %s line of order N sent to -1: %s" % (m, N, (d1, d2), line_exists)
    if m % 2:
        v = (m % N, 2)
        lam = scalar(Jt, v, N)
        muK = scalar(K, v, N)
        two_inv = pow(2, -1, N)
        okv = v in full
        p4 &= okv and lam == (m * two_inv) % N and (lam * lam) % N == N - 1 and muK == (-lam) % N and lam not in (1, N - 1)
        msg += " ; J_m by %s, K by %s, lambda^2 = %s mod N" % (lam, muK, (lam * lam) % N)
    say("P3", msg)
say("P3 holds:", p3, "; planted error (any nonzero kernel vector) accepts every m:", planted_all)
say("P4 holds:", p4)

# ---- P5
p5 = True
for m in range(1, 6):
    Jt = Jm(m)
    Am = Jt.dot(Jt)
    found_m, classes_m = normaliser_classes(Am, 30, 8)
    names_m = named(Jt, Am, 8)
    idx_m = [which(X, names_m, Am, 8) for X in classes_m]
    ok = len(classes_m) == 8 and None not in idx_m and len(set(idx_m)) == 8
    p5 &= ok
    say("P5 m", m, "elements found:", len(found_m), "; classes:", len(classes_m), "; all named +-J_m^n K^e:", ok)
say("P5 holds:", p5)
