#!/usr/bin/env python3
"""W-F22 (M31): B1922's negative half and R82-1's item 12, structurally. Data-free; this seat's own code (its own theta
series and Serre derivative). No frame output is computed; the readings are evaluated at random generic points, none
on the golden thread or at a line of the record.

    python3 -I -u wf22_checks.py

DEFINITIONS
  gamma = T R = [[2, 1], [1, 1]] (the golden thread's monodromy, B1922); on lines, (a, b) -> (a - b, 2b - a) (B1922's
  law; M = [[1, -1], [-1, 2]]). Lines: B1713's 266 lines of exact order 1 to 12 up to sign (B1726's lines()).
  The triplet a = DR, R = (-theta2^2, -theta4^2, i theta3^2) / (theta2 theta3 theta4), D the Serre derivative of weight
  -1/2 (B1691; S = a_i QI + a_j QJ + a_k QK). For g = [[p, q], [c, d]] in SL(2, Z): a(g tau) = (c tau + d)^(3/2) rho(g)
  a(tau), with rho(g) fitted from three points and checked on a fourth (principal branch; c tau + d in the upper half
  plane). The readings' components: S -> a; S~ = eps conj(S) eps^T -> conj(a) (eps conj(Q_k) eps^T = Q_k); S* = conj(S) ->
  Dg conj(a), Dg = diag(-1, 1, -1) (conj QI = -QI, conj QJ = QJ, conj QK = -QK). A reading is covariant under g, at the
  level of its components, when its components transform by a matrix proportional to rho(g): conj(rho) ~ rho for S~,
  Dg conj(rho) Dg ~ rho for S*.

EXPECTATIONS, written before the run (by hand):
  L1  Exactly two of B1713's 266 lines are fixed by gamma up to sign: (1/5, 2/5) and (2/5, 4/5) (the kernel of M + I mod 1
      is the five points k (2/5, 4/5); M - I has determinant -1, so fixes only 0).
  L2  gamma and gamma^2 are not in Gamma^0(2) (b odd); gamma^3 = [[13, 8], [8, 5]] is in Gamma(2).
  C2  For g = T, R, gamma, gamma^2, gamma^3 the fitted rho(g) passes the fourth-point check (relative residual below 1e-8),
      and rho(T) = [[w, 0, 0], [0, 0, w], [0, w^-3, 0]], w = e^{i pi / 4} (W-B1's E2).
  C0  Control: S~ is covariant under all five (conj(rho) ~ rho, residual below 1e-8), as B1724 found for SL(2, Z).
  C1  S* is covariant under R and gamma^3 (residual below 1e-8) and not under T, gamma, gamma^2 (residual above 1e-3).
      Reported, no expectation: the lines fixed up to sign by gamma^2 and by gamma^3.
  Plant: weight 1/2 in place of 3/2 fails the fourth-point check for every g with c != 0.
"""
import random
from fractions import Fraction as Fr
from math import gcd

import mpmath as mp

mp.mp.dps = 30
rng = random.Random(1922)
NK = 60


def say(*a):
    print(*a, flush=True)


# ---------------- L1, L2
def lines():
    def block(lo, hi):
        seen, out = set(), []
        for N in range(lo, hi + 1):
            for j in range(N):
                for k in range(N):
                    if gcd(gcd(j, k), N) != 1:
                        continue
                    a, b = Fr(j, N), Fr(k, N)
                    key = min((a, b), ((-a) % 1, (-b) % 1))
                    if key in seen:
                        continue
                    seen.add(key)
                    out.append(key)
        return out
    return block(1, 7) + block(8, 12)


def act(Mx, v):
    return ((Mx[0][0] * v[0] + Mx[0][1] * v[1]) % 1, (Mx[1][0] * v[0] + Mx[1][1] * v[1]) % 1)


def mmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


M1 = [[1, -1], [-1, 2]]
LN = lines()
fixed = {}
Mk = [[1, 0], [0, 1]]
for k in (1, 2, 3):
    Mk = mmul(Mk, M1)
    fixed[k] = [v for v in LN if act(Mk, v) in (v, ((-v[0]) % 1, (-v[1]) % 1))]
l1 = len(LN) == 266 and sorted(fixed[1]) == sorted([(Fr(1, 5), Fr(2, 5)), (Fr(2, 5), Fr(4, 5))])
say("L1 lines:", len(LN), "| fixed by gamma up to sign:", [tuple(str(x) for x in v) for v in fixed[1]], "| holds:", l1)
say("   reported: fixed by gamma^2:", len(fixed[2]), [tuple(str(x) for x in v) for v in fixed[2]])
say("   reported: fixed by gamma^3:", len(fixed[3]), [tuple(str(x) for x in v) for v in fixed[3]])
G = [[2, 1], [1, 1]]
G2, G3 = mmul(G, G), mmul(mmul(G, G), G)
in_up = lambda g: g[0][1] % 2 == 0
in_full = lambda g: g[0][1] % 2 == 0 and g[1][0] % 2 == 0 and g[0][0] % 2 == 1 and g[1][1] % 2 == 1
l2 = (not in_up(G)) and (not in_up(G2)) and in_full(G3) and G3 == [[13, 8], [8, 5]]
say("L2 gamma", G, "gamma^2", G2, "gamma^3", G3, "| holds:", l2)


# ---------------- the triplet
def thetas(tau):
    q = mp.exp(1j * mp.pi * tau)
    t3 = mp.fsum(q ** (n * n) for n in range(-NK, NK + 1))
    t4 = mp.fsum((-1) ** abs(n) * q ** (n * n) for n in range(-NK, NK + 1))
    t2 = mp.fsum(mp.exp(1j * mp.pi * tau * (n + mp.mpf(1) / 2) ** 2) for n in range(-NK, NK + 1))
    return t2, t3, t4


def Rv(tau):
    t2, t3, t4 = thetas(tau)
    D = t2 * t3 * t4
    return [-t2 * t2 / D, -t4 * t4 / D, 1j * t3 * t3 / D]


def E2f(tau):
    q = mp.exp(2j * mp.pi * tau)
    return 1 - 24 * mp.fsum(mp.fsum(d for d in range(1, n + 1) if n % d == 0) * q ** n for n in range(1, 400))


def av(tau, h=mp.mpf(10) ** -9):
    rp, rm = Rv(tau + h), Rv(tau - h)
    der = [(x - y) / (2 * h) / (2j * mp.pi) for x, y in zip(rp, rm)]
    e2 = E2f(tau)
    return [d - (mp.mpf(-1) / 2) / 12 * e2 * r for d, r in zip(der, Rv(tau))]


def mob(g, t):
    return (g[0][0] * t + g[0][1]) / (g[1][0] * t + g[1][1])


GS = {"T": [[1, 1], [0, 1]], "R": [[1, 0], [1, 1]], "gamma": G, "gamma^2": G2, "gamma^3": G3}


def base_points(g, n):
    c, d = g[1][0], g[1][1]
    y0 = mp.mpf(1) if c == 0 else mp.mpf(1) / c
    x0 = mp.mpf(0.2) if c == 0 else mp.mpf(-d) / c
    return [mp.mpc(x0 + rng.uniform(-0.15, 0.15) * y0, y0 * (1 + rng.uniform(-0.15, 0.15))) for _ in range(n)]


def fit(g, weight):
    c, d = g[1][0], g[1][1]
    pts = base_points(g, 4)
    cols_x, cols_y = [], []
    for t in pts:
        fac = (c * t + d) ** weight
        cols_x.append(av(t))
        cols_y.append([v / fac for v in av(mob(g, t))])
    X = mp.matrix(cols_x[:3]).T
    Y = mp.matrix(cols_y[:3]).T
    rho = Y * mp.inverse(X)
    pred = rho * mp.matrix(cols_x[3])
    res = max(abs(pred[i] - cols_y[3][i]) for i in range(3)) / max(abs(v) for v in cols_y[3])
    lo = min(mp.im(mob(g, t)) for t in pts)
    return rho, res, lo


def prop_res(A, B):
    """min over lambda of |A - lambda B| / |B|, lambda from the largest entry of B"""
    i, j = max(((i, j) for i in range(3) for j in range(3)), key=lambda ij: abs(B[ij[0], ij[1]]))
    lam = A[i, j] / B[i, j]
    num = max(abs(A[r, s] - lam * B[r, s]) for r in range(3) for s in range(3))
    return num / max(abs(B[r, s]) for r in range(3) for s in range(3))


Dg = mp.diag([-1, 1, -1])
w = mp.exp(1j * mp.pi / 4)
TR_hand = mp.matrix([[w, 0, 0], [0, 0, w], [0, w ** -3, 0]])
c2 = c0 = c1 = True
plant = True
for name, g in GS.items():
    rho, res, lo = fit(g, mp.mpf(3) / 2)
    conj_rho = mp.matrix([[mp.conj(rho[i, j]) for j in range(3)] for i in range(3)])
    r_tilde = prop_res(conj_rho, rho)
    r_star = prop_res(Dg * conj_rho * Dg, rho)
    c2 &= res < 1e-8
    c0 &= r_tilde < 1e-8
    want_star = name in ("R", "gamma^3")
    c1 &= (r_star < 1e-8) if want_star else (r_star > 1e-3)
    extra = ""
    if name == "T":
        dT = max(abs(rho[i, j] - TR_hand[i, j]) for i in range(3) for j in range(3))
        c2 &= dT < 1e-8
        extra = "| rho(T) against the hand matrix %s" % mp.nstr(dT, 3)
    if g[1][0] != 0:
        _, res_bad, _ = fit(g, mp.mpf(1) / 2)
        plant &= res_bad > 1e-4
    say("%-8s fourth-point residual %s (lowest Im of the images %s) | S~: %s | S*: %s %s" % (
        name, mp.nstr(res, 3), mp.nstr(lo, 3), mp.nstr(r_tilde, 3), mp.nstr(r_star, 3), extra))
say("C2 holds:", c2, "| C0 holds:", c0, "| C1 holds:", c1, "| plant (weight 1/2) fails the check for every c != 0:", plant)
