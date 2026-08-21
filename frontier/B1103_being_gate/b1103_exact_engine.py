"""Exact verification of chat1's free-group gate law on the B593 instrument.

Own arithmetic: Q(zeta60) as Z[x]/Phi60 with integer coefficient vectors and
a per-element global denominator. No sympy in the hot path.

Exact matrices built from B238's own formulas (KP sum for S, T exponents),
certified against the numeric instrument entrywise and by exact unitarity.

Convention: h(w) = - conj(u3) @ W(w) @ u3  (the twisted/banked sign; the
float pass proved twisted = -untwisted identically on the C-odd u3).

Decides exactly:
  E1  h(ab) == 1/(2phi) + i sin(2pi/5)/sqrt5      [banked B593 value]
  E2  h(abAB) == h(ab)
  E3  h(aabAAB) == -1/2 - i phi sin(2pi/5)/sqrt5
  E4  h(aB) != 0 and h(aB) not in Q(zeta5)
  E5  FACTORIZATION: for ALL 1364 strings length<=5 over {a,A,b,B}:
        g(w) := zeta3^-(p-q) h(w) is fixed by sigma11 and sigma31
        (Galois over Q(zeta5)), i.e. g(w) in Q(zeta5).
  E6  GATE both directions on the same 1364 strings:
        p-q = 0 mod 3  -> h in Q(zeta5)
        p-q != 0 mod 3 -> h = 0 or h not in Q(zeta5)
  E7  commutator census (u,v reduced len<=2): every h([u,v]) in Q(zeta5),
      Re h in the nine Niven letters EXACTLY; which letters appear.
"""
import itertools
import math
from fractions import Fraction

# ---------- Q(zeta60) engine: coeff vectors over Z, deg<16, mod Phi60 ----
D = 16
# Phi60(x) = x^16 + x^14 - x^10 - x^8 - x^6 + x^2 + 1
PHI = [1, 0, 1, 0, 0, 0, -1, 0, -1, 0, -1, 0, 0, 0, 1, 0]  # low->high for x^0..x^15 of (Phi60 - x^16)? careful below
# x^16 = -(x^14 - x^10 - x^8 - x^6 + x^2 + 1)  =>
X16 = [-1, 0, -1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, -1, 0]  # coeffs of x^16 in basis x^0..x^15

# reduction table: POW[j] = coeff vector of x^j, j = 0..130
POW = []
for j in range(131):
    if j < D:
        v = [0] * D
        v[j] = 1
        POW.append(v)
    else:
        # x^j = x * x^(j-1)
        prev = POW[j - 1]
        v = [0] * D
        carry = prev[D - 1]
        for i in range(D - 1, 0, -1):
            v[i] = prev[i - 1]
        v[0] = 0
        if carry:
            v = [v[i] + carry * X16[i] for i in range(D)]
        POW.append(v)

ZETA = {}  # zeta60^k as int vector
for k in range(60):
    ZETA[k] = POW[k][:]


def zmul(a, b):
    """multiply two int coeff vectors mod Phi60."""
    out = [0] * (2 * D - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    out[i + j] += ai * bj
    v = [0] * D
    for j in range(2 * D - 2, -1, -1):
        c = out[j]
        if c:
            if j < D:
                v[j] += c
            else:
                pj = POW[j]
                for i in range(D):
                    if pj[i]:
                        v[i] += c * pj[i]
    return v


def zadd(a, b):
    return [a[i] + b[i] for i in range(D)]


def zsub(a, b):
    return [a[i] - b[i] for i in range(D)]


def zscale(a, s):
    return [s * x for x in a]


def zzero(a):
    return all(x == 0 for x in a)


def galois(a, k):
    """sigma_k: zeta60^j -> zeta60^(jk mod 60), on an int vector."""
    v = [0] * D
    for j in range(D):
        if a[j]:
            t = ZETA[(j * k) % 60]
            for i in range(D):
                if t[i]:
                    v[i] += a[j] * t[i]
    return v


import cmath
Z60C = [cmath.exp(2j * cmath.pi * k / 60) for k in range(60)]
BASISC = [Z60C[1] ** j for j in range(D)]


def tofloat(a, den=1):
    return sum(a[j] * BASISC[j] for j in range(D)) / den


# ---------- element = (vec, den) with den a positive int -----------------
class E:
    __slots__ = ("v", "d")

    def __init__(self, v, d=1):
        self.v = v
        self.d = d

    def __add__(s, o):
        if s.d == o.d:
            return E(zadd(s.v, o.v), s.d)
        return E(zadd(zscale(s.v, o.d), zscale(o.v, s.d)), s.d * o.d)

    def __sub__(s, o):
        if s.d == o.d:
            return E(zsub(s.v, o.v), s.d)
        return E(zsub(zscale(s.v, o.d), zscale(o.v, s.d)), s.d * o.d)

    def __mul__(s, o):
        return E(zmul(s.v, o.v), s.d * o.d)

    def gal(s, k):
        return E(galois(s.v, k), s.d)

    def iszero(s):
        return zzero(s.v)

    def eq(s, o):
        return zzero((s - o).v)

    def f(s):
        return tofloat(s.v, s.d)

    def reduce(s):
        from math import gcd
        g = 0
        for x in s.v:
            g = gcd(g, abs(x))
        g = gcd(g, s.d)
        if g > 1:
            return E([x // g for x in s.v], s.d // g)
        return s


def zeta(k, den=1):
    return E(ZETA[k % 60][:], den)


ZERO = E([0] * D)
ONE = zeta(0)
Z3 = zeta(20)      # zeta3
Z3i = zeta(40)     # zeta3^-1
Z5 = zeta(12)      # zeta5
NEG = zeta(30)     # -1 = zeta60^30
I = zeta(15)       # i

# sanity: zeta3 not fixed by sigma11; zeta5 fixed
assert not Z3.gal(11).eq(Z3) and Z5.gal(11).eq(Z5)
assert not Z3.gal(31).eq(Z3) or True  # 31 mod 3 = 1 -> sigma31 FIXES zeta3
# careful: 31 = 1 mod 3, so sigma31 fixes zeta3; 31 mod 5 = 1 fixes zeta5.
# subgroup fixing Q(zeta5) inside (Z/60)* is {1,11,31,41}; sigma31 also
# fixes zeta3?? then it acts trivially on zeta15... but must move zeta4:
assert not I.gal(31).eq(I)   # 31 mod 4 = 3 -> conjugates i. good.

# ---------- exact S, T from B238's formulas ------------------------------
K = 2
KAP = 5
weights = [(a, b) for a in range(K + 1) for b in range(K + 1 - a)]
n = len(weights)


def Lvec(w):
    return (Fraction(w[0] + w[1] + 2), Fraction(w[1] + 1), Fraction(0))


def ip(u, v):
    s = sum(u) * sum(v) / 3
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2] - s


perms = list(itertools.permutations(range(3)))


def sgn(p):
    return (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))


# raw S entries: sum sgn(p) * exp(-2pi i * ip(Ll[p], Lm)/5); ip has denom 3
# -> exponent = -ip/5 turns; as fraction of a full turn: -ip/5 = m/15.
Sraw = [[ZERO for _ in range(n)] for _ in range(n)]
for i, wl in enumerate(weights):
    Ll = Lvec(wl)
    for j, wm in enumerate(weights):
        Lm = Lvec(wm)
        acc = E([0] * D)
        for p in perms:
            Lp = (Ll[p[0]], Ll[p[1]], Ll[p[2]])
            t = -ip(Lp, Lm) / KAP  # fraction of full turn
            frac = t % 1
            k60 = frac * 60
            assert k60.denominator == 1, (t, k60)
            acc = acc + zeta(int(k60) % 60, 1) * E([sgn(p) * x for x in ZETA[0]], 1)
        Sraw[i][j] = acc

# normalization: nu^2 = sum_i |Sraw[i][0]|^2 ; claim nu = 5*sqrt(3),
# i.e. S = Sraw/(5 sqrt3). 1/sqrt3 = -i(z3 - z3^2)/3 exactly.
nu2 = ZERO
for i in range(n):
    a = Sraw[i][0]
    nu2 = nu2 + a * a.gal(59)  # a * conj(a)
nu2 = nu2.reduce()
print("nu^2 =", nu2.v, "/", nu2.d, "-> float", nu2.f().real)
assert nu2.eq(E(zscale(ZETA[0], 75), 1)), "normalization is not 75!"

inv_sqrt3 = (E([0]*D) - I) * (Z3 - Z3.gal(59))  # -i (z3 - conj z3) = -i*(i sqrt3) = sqrt3
# so inv_sqrt3 currently = sqrt3; want 1/(5 sqrt3) = sqrt3/15
SCALE = E(inv_sqrt3.v, 15)  # sqrt3 / 15
Sx = [[(Sraw[i][j] * SCALE).reduce() for j in range(n)] for i in range(n)]

# T exact: exponent = C2/(2 kap) - c/24 with the file's formula
c = Fraction(K * 8, K + 3)
Tdiag = []
for (a, b) in weights:
    expo = (Fraction(2, 3) * (a * a + a * b + b * b) + 2 * (a + b)) / (2 * KAP) - c / 24
    frac = expo % 1
    k60 = frac * 60
    assert k60.denominator == 1, expo
    Tdiag.append(zeta(int(k60) % 60))

# certify against numeric instrument
import importlib.util, os
import numpy as np
REPO = "."
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(REPO, "frontier/B238_su32_levelrank/su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)
wn, Sn, Tn, cn = b238.su3_data(2)
assert wn == weights
errS = max(abs(Sx[i][j].f() - Sn[i, j]) for i in range(n) for j in range(n))
errT = max(abs(Tdiag[i].f() - Tn[i, i]) for i in range(n))
print(f"exact-vs-numeric certification: max|dS| = {errS:.2e}, max|dT| = {errT:.2e}")
assert errS < 1e-12 and errT < 1e-12

# exact unitarity of S: S . conj(S)^T = I  (S symmetric here, but do full)
for i in range(n):
    for j in range(n):
        acc = ZERO
        for k_ in range(n):
            acc = acc + Sx[i][k_] * Sx[j][k_].gal(59)
        target = ONE if i == j else ZERO
        assert acc.eq(target), (i, j, acc.v, acc.d)
print("exact unitarity of S: PASS")

# ---------- exact R, L, inverses -----------------------------------------
def matmul(A, B):
    return [[sum((A[i][k_] * B[k_][j] for k_ in range(n)), ZERO).reduce()
             for j in range(n)] for i in range(n)]


Rm = [[Tdiag[i] if i == j else ZERO for j in range(n)] for i in range(n)]
Rinv = [[Tdiag[i].gal(59) if i == j else ZERO for j in range(n)] for i in range(n)]
Sconj = [[Sx[i][j].gal(59) for j in range(n)] for i in range(n)]
# S^-1 = conj(S)^T; S symmetric -> S^-1 = conj(S). Use conj-transpose to be safe.
SconjT = [[Sconj[j][i] for j in range(n)] for i in range(n)]
Tinv = Rinv
Lm = matmul(matmul(SconjT, Tinv), Sx)
Linv = matmul(matmul(SconjT, Rm), Sx)
# certify L numerically + L*Linv = I exactly
Sni, Tni = np.linalg.inv(Sn), np.linalg.inv(Tn)
Ln = Sni @ Tni @ Sn
errL = max(abs(Lm[i][j].f() - Ln[i, j]) for i in range(n) for j in range(n))
print(f"exact L vs numeric: max|dL| = {errL:.2e}")
assert errL < 1e-11
LL = matmul(Lm, Linv)
for i in range(n):
    for j in range(n):
        assert LL[i][j].eq(ONE if i == j else ZERO)
print("exact L * L^-1 = I: PASS")

MATS = {"a": Rm, "A": Rinv, "b": Lm, "B": Linv}

i10, i01 = weights.index((1, 0)), weights.index((0, 1))


def hval(M):
    """h = -(M[i10][i10] - M[i10][i01] - M[i01][i10] + M[i01][i01]) / 2
    (conj(u3) W u3 with real u3 entries +-1/sqrt2; twisted sign folded)."""
    t = M[i10][i10] - M[i10][i01] - M[i01][i10] + M[i01][i01]
    return E(t.v, t.d * 2) * NEG


def inQ5(x):
    return x.gal(11).eq(x) and x.gal(31).eq(x)


# exact targets
SQRT5 = (Z5 + zeta(48)) - (zeta(24) + zeta(36))     # z5 + z5^4 - z5^2 - z5^3
HALF = E(ZETA[0][:], 2)
QUARTER = E(ZETA[0][:], 4)
inv2phi = (SQRT5 - ONE) * QUARTER                    # (sqrt5-1)/4
isin72 = E(zsub(ZETA[12], ZETA[48]), 2)              # (z5 - z5^-1)/2 = i sin72
inv_sqrt5 = E(SQRT5.v, 5 * SQRT5.d)                  # sqrt5/5
banked = inv2phi + isin72 * inv_sqrt5
phi_over_sqrt5 = E(zadd(SQRT5.v, zscale(ZETA[0], 5 * SQRT5.d // SQRT5.d)), 10 * SQRT5.d)
# careful: phi/sqrt5 = (sqrt5+5)/10; SQRT5.d == 1 here
assert SQRT5.d == 1
phi_over_sqrt5 = E(zadd(SQRT5.v, zscale(ZETA[0], 5)), 10)
t5target = (ZERO - HALF) - isin72 * phi_over_sqrt5

# word machinery with prefix cache
CACHE = {"": [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]}


def wordmat(word):
    if word in CACHE:
        return CACHE[word]
    M = matmul(wordmat(word[:-1]), MATS[word[-1]])
    CACHE[word] = M
    return M


def pqdiff(word):
    return (word.count("a") - word.count("A")) - (word.count("b") - word.count("B"))


print("\n== E1: h(ab) exact ==")
hab = hval(wordmat("ab"))
print("h(ab) float:", f"{hab.f():.9f}")
print("E1", "PASS" if hab.eq(banked) else "FAIL")

print("\n== E2: h(abAB) == h(ab) exact ==")
habab = hval(wordmat("abAB"))
print("E2", "PASS" if habab.eq(hab) else "FAIL")

print("\n== E3: h(aabAAB) exact ==")
h6 = hval(wordmat("aabAAB"))
print("h(aabAAB) float:", f"{h6.f():.9f}")
print("E3", "PASS" if h6.eq(t5target) else "FAIL")

print("\n== E4: h(aB) nonzero and NOT in Q(zeta5) ==")
h_aB = hval(wordmat("aB"))
print("E4", "PASS" if (not h_aB.iszero()) and (not inQ5(h_aB)) else "FAIL")

print("\n== E5+E6: factorization + gate, all strings len<=5 ==")
letters = "aAbB"
fact_fail, gate_fail, zero_count = [], [], 0
count = 0
for ln in range(1, 6):
    for tup in itertools.product(letters, repeat=ln):
        s = "".join(tup)
        M = wordmat(s)
        hv = hval(M)
        d = pqdiff(s) % 3
        g = hv * (Z3i if d == 1 else (Z3 if d == 2 else ONE))
        # g = zeta3^-(p-q) h  (zeta3^-1 for d=1, zeta3^-2 = zeta3 for d=2)
        if not inQ5(g):
            fact_fail.append(s)
        memb = inQ5(hv)
        if d == 0:
            if not memb:
                gate_fail.append((s, "d=0 but h not in Q5"))
        else:
            if memb and not hv.iszero():
                gate_fail.append((s, "d!=0, h nonzero, yet in Q5"))
        if hv.iszero():
            zero_count += 1
        count += 1
print(f"strings: {count}; factorization failures: {len(fact_fail)}; "
      f"gate failures: {len(gate_fail)}; h=0 count: {zero_count}")
print("E5", "PASS" if not fact_fail else f"FAIL {fact_fail[:5]}")
print("E6", "PASS" if not gate_fail else f"FAIL {gate_fail[:5]}")

print("\n== E7: commutator census exact ==")
red = []
for ln in (1, 2):
    for tup in itertools.product(letters, repeat=ln):
        s = "".join(tup)
        if any(s[i] + s[i + 1] in ("aA", "Aa", "bB", "Bb") for i in range(len(s) - 1)):
            continue
        red.append(s)


def invw(word):
    return "".join(c.swapcase() for c in reversed(word))


NIVEN_EXACT = [
    ("0", ZERO), ("+1/2", HALF), ("-1/2", ZERO - HALF),
    ("+1/(2phi)", inv2phi), ("-1/(2phi)", ZERO - inv2phi),
    ("+phi/2", (SQRT5 + ONE) * QUARTER), ("-phi/2", ZERO - (SQRT5 + ONE) * QUARTER),
    ("+1", ONE), ("-1", ZERO - ONE),
]
seen, comms = set(), []
for u_ in red:
    for v_ in red:
        cw = u_ + v_ + invw(u_) + invw(v_)
        if cw not in seen:
            seen.add(cw)
            comms.append(cw)
all_q5, all_letter, hit = True, 0, set()
offl = []
for cw in comms:
    hv = hval(wordmat(cw))
    if not inQ5(hv):
        all_q5 = False
    re_ = E(zadd(hv.v, galois(hv.v, 59)), hv.d * 2)  # (h + conj h)/2
    m = [nm for nm, ex in NIVEN_EXACT if re_.eq(ex)]
    if m:
        all_letter += 1
        hit.add(m[0])
    else:
        offl.append((cw, hv.f()))
print(f"commutators: {len(comms)}; all in Q(zeta5): {all_q5}; "
      f"Re in Niven letters: {all_letter}/{len(comms)}")
print(f"letters hit ({len(hit)}):", sorted(hit))
if offl:
    print("off-letter:", offl[:5])
print("\nDONE")
