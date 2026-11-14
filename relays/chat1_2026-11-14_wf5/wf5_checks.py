#!/usr/bin/env python3
"""W-F5: the cone point is a relation among the distinctions; the odd sphere orders; where the scar can heal.

Data-free; this seat's own code. The Fox-calculus helpers (Rep, rank_mod, nullspace_mod, madd, ident) are taken by text
from W-C8 part 2a's sealed script (definitions only, up to its census), which is not re-run.

    python3 -I -u wf5_checks.py

DEFINITIONS
  W_3 = <a, b, c | a^2, b^2, c^2>, the three distinctions with no relations. x = ab, y = bc (the records), lambda =
  [x, y] = x y x^-1 y^-1 (the scar), and a lambda a = (abc)^-2 in W_3 (W-F1 A2). O_K = W_3 / <<(abc)^K>> for K = 2, 3, ...;
  K = infinity is W_3 itself. A fibre cone point of order k (W-F3) is K = 2k. The parity character: a, b, c -> -1.
  Characters of O_K: a, b, c -> +-1 with chi(abc)^K = 1. A class: a cocycle (c(a), c(b), c(c)) of the presentation
  (Fox calculus) that is not a coboundary.
  The Fricke cubic (line 3 of W-C8 part 4's page): X^2 + Y^2 + Z^2 = XYZ, (X, Y, Z) = (tr x, tr y, tr xy), equivalently
  tr[x, y] = -2. Representatives in SL(2, C): x = [[X, 1], [-1, 0]], y = [[0, s], [-1/s, Y]], s^2 + Z s + 1 = 0. The
  common point (W-F1 A2; the record's W2) is the origin X = Y = Z = 0.

EXPECTATIONS, written before the run (derived by hand from the definitions):
  F1  H_1(O_K) (Smith form of the relations 2a, 2b, 2c, K(a + b + c)) is (Z/2)^3 for K even and for K = infinity, and
      (Z/2)^2 for K odd (K = 2..13). The parity character exists exactly for K even or infinity.
  F2  In W_3, (abc)^2 = x (xy)^-1 y (a word identity). So for odd K, abc = ((abc)^2)^((1-K)/2) lies in <x, y>, and so do
      c = x^-1 (abc) and a = (abc) y^-1: the records generate all of O_K (index 1), and the split of the distinctions
      into records (an index-2 even part) is lost. For even K and K = infinity the index is 2 (the parity character).
  F3  For every finite K = 2..13 and every character of O_K, every class has c(lambda) = 0; for odd K every class also
      has c(abc) = 0. Control: at K = infinity the character (-1, -1, 1) carries a class with c(lambda) = 2 (by hand),
      so the instrument registers a class on the scar where one exists. Both primes give the same counts.
  F4  On 2000 random points of the Fricke cubic (complex X, Y; Z a root of the cubic in Z), tr[x, y] = -2 and
      [x, y] != -I: [x, y] + I is a non-zero nilpotent, so [x, y]^n != I for n = 1..24 (infinite order). At the origin,
      [x, y] = -I. Control: on the cone level sets tr[x, y] = -2 cos(pi/k), k = 2..6 (200 points each), [x, y]^(2k) = I.
  F5  At the common point lambda = -I, so lambda^k = I in SL(2, C) exactly for even k (k = 1..12); in PSL(2, C) lambda = 1.
  F4 and F5 use 40-digit arithmetic. Tolerances: 1e-25 for equalities and 1e-10 for "not equal"; in the control,
  1e-20 on the trace and 1e-15 on [x, y]^(2k) - I.
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(HERE, "..", "chat1_2026-11-14_wc8", "wc8_part2a_checks.py")).read()
ns = {}
exec(SRC.split("EXP = {}")[0], ns)
Rep, rank_mod, nullspace_mod = ns["Rep"], ns["rank_mod"], ns["nullspace_mod"]


def say(*a):
    print(*a, flush=True)


# ---------- F1: Smith form by determinantal divisors ----------
from math import gcd
from itertools import combinations


def det(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    return sum((-1) ** j * M[0][j] * det([r[:j] + r[j + 1:] for r in M[1:]]) for j in range(n))


def invariants(rel, ncols):
    out, prev = [], 1
    for r in range(1, ncols + 1):
        g = 0
        for rows in combinations(range(len(rel)), r):
            for cols in combinations(range(ncols), r):
                g = gcd(g, abs(det([[rel[i][j] for j in cols] for i in rows])))
        if g == 0:
            out.append(0)
            prev = 0
            continue
        out.append(g // prev if prev else 0)
        prev = g
    return out


f1 = True
for K in list(range(2, 14)) + [None]:
    rel = [[2, 0, 0], [0, 2, 0], [0, 0, 2]] + ([[K, K, K]] if K else [])
    inv_ = invariants(rel, 3)
    parity = all((sum(r) % 2 == 0) for r in rel)
    want = [2, 2, 2] if (K is None or K % 2 == 0) else [1, 2, 2]
    f1 &= inv_ == want and parity == (K is None or K % 2 == 0)
    say("F1 K =", K if K else "infinity", "| Smith invariants", inv_, "| parity character exists:", parity)
say("F1 holds:", f1)


# ---------- F2: the word identity in W_3 ----------
def red3(w):
    out = []
    for ch in w:
        if out and out[-1] == ch:
            out.pop()
        else:
            out.append(ch)
    return "".join(out)


inv3 = lambda w: w[::-1]
X3, Y3 = "ab", "bc"
f2 = red3("abc" * 2) == red3(X3 + inv3(X3 + Y3) + Y3)
say("F2 (abc)^2 =", red3("abc" * 2), "; x (xy)^-1 y =", red3(X3 + inv3(X3 + Y3) + Y3))
say("F2 holds:", f2)

# ---------- F3: classes on the scar ----------
LAMW = (1, 2, 2, 3, -2, -1, -3, -2)  # x y x^-1 y^-1 with x = ab, y = bc
ABC = (1, 2, 3)


def classes(chi, rels, p):
    r1 = Rep({1: [[chi[0] % p]], 2: [[chi[1] % p]], 3: [[chi[2] % p]]}, p)
    F = [[r1.fox(r, gi)[0][0] for gi in (1, 2, 3)] for r in rels]
    Z = nullspace_mod(F, p, 3)
    cob = [(chi[i] - 1) % p for i in range(3)]
    base = [cob] if any(cob) else []
    chosen = []
    for z in Z:
        if rank_mod(base + chosen + [z], p) > len(base) + len(chosen):
            chosen.append(z)
    return r1, chosen


f3, census3 = True, []
for p in (1000003, 998244353):
    rows = []
    for K in list(range(2, 14)) + [None]:
        rels = [(1, 1), (2, 2), (3, 3)] + ([ABC * K] if K else [])
        nchar, ncl, lam_nz, abc_nz = 0, 0, 0, 0
        for chi in [(s1, s2, s3) for s1 in (1, -1) for s2 in (1, -1) for s3 in (1, -1)]:
            if K and (chi[0] * chi[1] * chi[2]) ** K != 1:
                continue
            nchar += 1
            r1, cl = classes(chi, rels, p)
            for c in cl:
                z = {1: [c[0]], 2: [c[1]], 3: [c[2]]}
                ncl += 1
                lam_nz += r1.cocycle_value(z, LAMW)[0] % p != 0
                abc_nz += r1.cocycle_value(z, ABC)[0] % p != 0
        rows.append((K, nchar, ncl, lam_nz, abc_nz))
        if K:
            f3 &= lam_nz == 0 and (K % 2 == 0 or abc_nz == 0)
    # the control at K = infinity: chi = (-1, -1, 1), class c = (1, 0, 0), c(lambda) = 2
    r1, cl = classes((-1, -1, 1), [(1, 1), (2, 2), (3, 3)], p)
    vals = [r1.cocycle_value({1: [c[0]], 2: [c[1]], 3: [c[2]]}, LAMW)[0] for c in cl]
    ctrl = any(v % p for v in vals) and r1.cocycle_value({1: [1], 2: [0], 3: [0]}, LAMW)[0] % p == 2
    f3 &= ctrl
    census3.append(rows)
    for row in rows:
        say("F3 p", p, "K =", row[0] if row[0] else "infinity", "| characters", row[1], "| classes", row[2],
            "| classes with c(lambda) != 0:", row[3], "| with c(abc) != 0:", row[4])
    say("F3 control at K = infinity, chi = (-1, -1, 1): c(lambda) of c = (1, 0, 0) is 2:", ctrl)
f3 &= census3[0] == census3[1]
say("F3 holds:", f3, "; both primes give the same counts:", census3[0] == census3[1])

# ---------- F4: the Fricke cubic (40-digit arithmetic) ----------
import mpmath as mp

mp.mp.dps = 40
rng = np.random.default_rng(20261114)
I2 = mp.eye(2)
EQ, NE = mp.mpf("1e-25"), mp.mpf("1e-10")


def rep_from_traces(X, Y, Z):
    s = (-Z + mp.sqrt(Z * Z - 4)) / 2
    x = mp.matrix([[X, 1], [-1, 0]])
    y = mp.matrix([[0, s], [-1 / s, Y]])
    return x, y


def comm(x, y):
    return x * y * mp.inverse(x) * mp.inverse(y)


def mx(A):
    return max(abs(A[i, j]) for i in range(2) for j in range(2))


def rand_c():
    re, im = rng.normal(size=2)
    return mp.mpc(float(re), float(im)) * 2


f4, worst_tr, worst_nil, min_dist = True, mp.mpf(0), mp.mpf(0), mp.inf
for _ in range(2000):
    X, Y = rand_c(), rand_c()
    Z = (X * Y + mp.sqrt((X * Y) ** 2 - 4 * (X * X + Y * Y))) / 2
    x, y = rep_from_traces(X, Y, Z)
    C = comm(x, y)
    N = C + I2
    worst_tr = max(worst_tr, abs(C[0, 0] + C[1, 1] + 2))
    worst_nil = max(worst_nil, mx(N * N) / max(1, mx(N) ** 2))
    P = I2.copy()
    for n in range(1, 25):
        P = P * C
        min_dist = min(min_dist, mx(P - I2))
    f4 &= mx(N) > NE
f4 &= worst_tr < EQ and worst_nil < EQ and min_dist > NE
x0, y0 = rep_from_traces(mp.mpc(0), mp.mpc(0), mp.mpc(0))
C0 = comm(x0, y0)
origin = mx(C0 + I2) < EQ
ctrl4 = True
for k in range(2, 7):
    tau = -2 * mp.cos(mp.pi / k)
    for _ in range(200):
        X, Y = rand_c(), rand_c()
        # Fricke: tr[x, y] = X^2 + Y^2 + Z^2 - XYZ - 2 = tau
        Z = (X * Y + mp.sqrt((X * Y) ** 2 - 4 * (X * X + Y * Y - 2 - tau))) / 2
        x, y = rep_from_traces(X, Y, Z)
        C = comm(x, y)
        P = I2.copy()
        for _n in range(2 * k):
            P = P * C
        ctrl4 &= abs(C[0, 0] + C[1, 1] - tau) < mp.mpf("1e-20") and mx(P - I2) < mp.mpf("1e-15")
f4 &= origin and ctrl4
say("F4 on the cubic: max |tr[x,y] + 2| =", mp.nstr(worst_tr, 3), "; max relative |N^2| =", mp.nstr(worst_nil, 3),
    "; min over n = 1..24 of |[x,y]^n - I| =", mp.nstr(min_dist, 5))
say("F4 at the origin [x, y] = -I:", origin, "; control on the cone level sets ([x,y]^(2k) = I):", ctrl4)
say("F4 holds:", f4)

# ---------- F5: the common point and the cone orders ----------
f5 = True
P = I2.copy()
for k in range(1, 13):
    P = P * C0
    is_id, is_mid = mx(P - I2) < EQ, mx(P + I2) < EQ
    f5 &= is_id == (k % 2 == 0) and (is_id or is_mid)
say("F5 holds:", f5)
