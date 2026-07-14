"""B589 — L83(a): exact identification of the three E6_2 per-pair amplitudes.

Rebuilds the E6 level-2 stage with the Weyl sum collected EXACTLY (a Counter
over rational exponents mod 1, denominator | 42 — zero float error in the
51840-term sums), evaluates at 50 digits (mpmath), re-verifies the banked
amplitudes, then identifies them in closed form:

    p_j = r_j * zeta_14^{k_j}   (blind observation: k = {+3, -2, -1})

with the moduli r_j pinned against the sin(j pi/14) basis and certified to
~40 digits. Comparison to stage gradings (conformal weights, q-dims) happens
AFTER the identification prints (blind-then-check).

Run: python3 pair_amplitudes.py (pyenv, ~3 min). Nothing to CLAIMS.md.
"""
import importlib.util
import os
from collections import Counter
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np

mp.mp.dps = 50
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "c3", os.path.join(HERE, "..", "B570_allowed_plays", "c3_e6_level2_monodromy.py"))
c3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c3)

KH = 14
PRIM, NAMES = c3.PRIM, c3.NAMES

# exact rational lambda+rho in the root basis: Cinv is rational (det C6 = 3)
C6 = [[Fr(x) for x in row] for row in c3.C6]
import copy


def mat_inv3(A):
    n = len(A)
    M = [row[:] + [Fr(1) if i == j else Fr(0) for j in range(n)] for i, row in enumerate(A)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[col])]
    return [row[n:] for row in M]


CINV = mat_inv3(C6)


def root_coords(labels):
    return [sum(CINV[i][j] * Fr(labels[j]) for j in range(6)) for i in range(6)]


RHO = root_coords([1] * 6)
SHIFT = [[a + b for a, b in zip(root_coords(p), RHO)] for p in PRIM]


def ip(x, y):
    return sum(Fr(c3.C6[i][j]) * x[i] * y[j] for i in range(6) for j in range(6))


print("building W(E6) (51840 elements) ...")
W, eps = c3.weyl_group()
assert len(W) == 51840

print("collecting the exact Weyl sums (Counter over exponents mod 1, denom | 42) ...")
ST = {}                                     # S-tilde entries as Counters {Fraction q: int}
for a in range(9):
    for b in range(a, 9):
        cnt = Counter()
        vb = SHIFT[b]
        Gvb = [sum(Fr(c3.C6[i][j]) * vb[j] for j in range(6)) for i in range(6)]
        va = SHIFT[a]
        for w, e in zip(W, eps):
            wa = [sum(Fr(int(w[i][j])) * va[j] for j in range(6)) for i in range(6)]
            q = (-sum(wa[i] * Gvb[i] for i in range(6)) / KH) % 1
            cnt[q] += int(e)
        ST[(a, b)] = ST[(b, a)] = cnt

ZROOT = {}


def ev(cnt):
    tot = mp.mpc(0)
    for q, c in cnt.items():
        if c:
            key = q
            if key not in ZROOT:
                ZROOT[key] = mp.e ** (2j * mp.pi * mp.mpf(key.numerator) / mp.mpf(key.denominator))
            tot += c * ZROOT[key]
    return tot


Sm = mp.matrix(9, 9)
for a in range(9):
    for b in range(9):
        Sm[a, b] = ev(ST[(a, b)])
# unitary normalization, S00 > 0
norm = mp.sqrt(sum(Sm[0, j] * mp.conj(Sm[0, j]) for j in range(9)).real)
for a in range(9):
    for b in range(9):
        Sm[a, b] = Sm[a, b] / norm
if Sm[0, 0].real < 0:
    Sm = -Sm

hs = [ip(root_coords(p), [x + 2 * r for x, r in zip(root_coords(p), RHO)]) / (2 * KH)
      for p in PRIM]
cc = Fr(2 * 78, KH)
Tm = mp.matrix(9, 9)
for i in range(9):
    q = (hs[i] - cc / 24) % 1
    Tm[i, i] = mp.e ** (2j * mp.pi * mp.mpf(q.numerator) / mp.mpf(q.denominator))

rho = Tm * Tm * Sm * Tm
# gates: banked B586 values reproduced at high precision
pairs = [(1, 2, "27"), (3, 4, "351'"), (7, 8, "351")]
BANKED = [mp.mpc("0.13151189", "0.57619122"),
          mp.mpc("0.20449548", "-0.25642922"),
          mp.mpc("0.66399264", "-0.31976200")]
P = []
for j, (a, b, nm) in enumerate(pairs):
    p = (rho[a, a] - rho[a, b] - rho[b, a] + rho[b, b]) / 2
    P.append(p)
    assert abs(p - BANKED[j]) < 1e-7, (nm, p)
assert abs(sum(P) - 1) < mp.mpf(10) ** (-40)
print("gates: banked B586 amplitudes reproduced at 50 digits; sum = 1 exact  PASS")

print("\nTHE IDENTIFICATION (blind reads):")
z14 = lambda k: mp.e ** (2j * mp.pi * k / mp.mpf(14))
ks = []
for j, (a, b, nm) in enumerate(pairs):
    arg = mp.arg(P[j]) / (2 * mp.pi) * 14
    k = int(mp.nint(arg))
    ks.append(k)
    resid = P[j] * z14(-k)
    assert abs(resid.imag) < mp.mpf(10) ** (-40) and resid.real > 0, (nm, arg)
    print(f"  p[{nm:>4}] = r_{j+1} * zeta_14^{k:+d}   (arg exact to 40+ digits)")
r = [(P[j] * z14(-ks[j])).real for j in range(3)]
s = lambda j: mp.sin(j * mp.pi / 14)
print("\n  moduli relations (certified to 40 digits):")
rel1 = r[0] / r[1] - 2 * s(5)
rel2 = r[2] * (2 * s(1)) - r[1]
print(f"    r_1 = r_2 * 2 sin(5pi/14):  dev = {mp.nstr(abs(rel1), 3)}")
print(f"    r_3 = r_2 / (2 sin(pi/14)): dev = {mp.nstr(abs(rel2), 3)}")
assert abs(rel1) < mp.mpf(10) ** (-40) and abs(rel2) < mp.mpf(10) ** (-40)
poly = mp.findpoly(r[1], 6, maxcoeff=10 ** 6)
print(f"    minimal-ish polynomial of r_2 (findpoly deg<=6): {poly}")
print(f"    r_1 = {mp.nstr(r[0], 30)}")
print(f"    r_2 = {mp.nstr(r[1], 30)}")
print(f"    r_3 = {mp.nstr(r[2], 30)}")
# try the natural stage candidates for r_2: S-entries / q-dim combinations
print("\n  candidate matches among stage quantities:")
cands = {
    "S(0,27)": Sm[0, 1], "S(0,351')": Sm[0, 3], "S(0,351)": Sm[0, 7],
    "S(27,27)": Sm[1, 1], "S(27,27b)": Sm[1, 2],
    "1/sqrt7": 1 / mp.sqrt(7), "2 sin(1)/sqrt7": 2 * s(1) / mp.sqrt(7),
    "2 sin(2)/sqrt7": 2 * s(2) / mp.sqrt(7), "2 sin(3)/sqrt7": 2 * s(3) / mp.sqrt(7),
    "2 sin(4)/sqrt7": 2 * s(4) / mp.sqrt(7), "2 sin(5)/sqrt7": 2 * s(5) / mp.sqrt(7),
    "2 sin(6)/sqrt7": 2 * s(6) / mp.sqrt(7),
}
for j in range(3):
    hits = [nm for nm, v in cands.items() if abs(abs(v) - r[j]) < mp.mpf(10) ** (-35)]
    print(f"    r_{j+1}: {hits if hits else 'no direct match in the candidate list'}")

print("\nAFTER-THE-FACT comparison (registered as post-hoc): the exponents k_j vs")
print(f"  the T-phases 2(h-c/24) mod 1: h = {[str(h) for h in hs]}")
for j, (a, b, nm) in enumerate(pairs):
    tj = (hs[a] - cc / 24) % 1
    print(f"  pair {nm:>4}: k/14 = {ks[j]}/14 = {Fr(ks[j],14)};  (h-c/24) mod 1 = {tj}")
print("\nALL GATES PASS")
