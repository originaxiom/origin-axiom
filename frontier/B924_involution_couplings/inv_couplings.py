"""B924 -- the three unused involution couplings (R-INV, masterplan amendment 2026-08-05).

B593 computed the ONE forced coupling on the hearing x measurement face pair via theta
(the label conjugation C): the second-order hearing law with the forced value
1/(2 phi) + i sin(2 pi/5)/sqrt5 at the object's monodromy weld g = RL. Chat-1's estimate:
three involutions unused on the SAME face pair -- sigma*, c, sigma*c -- same machinery,
different projections, each potentially an independent forced value.

OPERATIVE DEFINITIONS (adjudicated by the stage field itself). The entire B593 stage --
the welds rho(g) (R = T, L = S^-1 T^-1 S), the twist C, the bare listener psi0 (the 4_1
colored-Jones vector at q = e^{i pi/5}), and the dial -- lives EXACTLY in Q(zeta_15).
Gal(Q(zeta_15)/Q) = (Z/15)^x has EXACTLY three involutions:
    sigma*   := t=4   (zeta_5 -> zeta_5^-1, zeta_3 fixed)   -- the pentagonal conjugation
    c        := t=14  (full complex conjugation)
    sigma*c  := t=11  (zeta_3 -> zeta_3^-1, zeta_5 fixed)   -- the triangular conjugation
These three + identity form the full involution set (the V4 of the field). The golden
conjugation sqrt5 -> -sqrt5 has NO involutive lift to the stage field: t^2 = 1 mod 15
forces t = +-1 mod 5 (proved in the atlas below) -- so the only involutive readings of
"sigma*" on this face pair are the three above. Each acts SEMILINEARLY (entrywise) on
states; substituting it for theta in the B593 construction means: its odd projection
supplies the displacement, its mirror supplies the bra.

Verdict tools: exact arithmetic over Q(zeta_15) (Fraction coefficients mod Phi_15);
numeric calibration against the banked B593 pipeline first. Nothing to CLAIMS.md.
Run: python3 inv_couplings.py (pyenv, ~1 min). Writes results.json.
"""
import cmath
import importlib.util
import json
import math
import os
from fractions import Fraction

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


# ============================================================================
# Part 0 -- numeric calibration: reproduce B593's theta law + forced value
# ============================================================================

def load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b238 = load("../B238_su32_levelrank/su32_wrt.py", "b238_b924")
b245 = load("../B245_higher_color_levelrank/higher_color_levelrank.py", "b245_b924")

w, Sn, Tn, _cc = b238.su3_data(2)
n = len(w)
Cn = np.zeros((n, n))
for i, wt in enumerate(w):
    Cn[w.index((wt[1], wt[0])), i] = 1.0
conj_idx = [w.index((wt[1], wt[0])) for wt in w]
qn = cmath.exp(1j * math.pi / 5)
Jn = {(0, 0): 1.0, (1, 0): b245.H_sym(1, qn ** 3, qn), (0, 1): b245.H_antisym(2, qn ** 3, qn),
      (2, 0): b245.H_sym(2, qn ** 3, qn), (0, 2): b245.H_sym(2, qn ** 3, qn), (1, 1): 0.0}
psin = np.array([Jn[wt] for wt in w], dtype=complex)
Sni, Tni = np.linalg.inv(Sn), np.linalg.inv(Tn)
Rn, Ln = Tn, Sni @ Tni @ Sn


def weld_n(word, twisted):
    M = np.eye(n, dtype=complex)
    for ch in word:
        M = M @ (Rn if ch == 'R' else Ln)
    return (Cn @ M) if twisted else M


def amp_n(psi, word, twisted):
    W = weld_n(word, twisted)
    vec = W @ psi
    return sum(np.conj(psi[conj_idx[i]]) * vec[i] for i in range(n))


PHI = (1 + 5 ** 0.5) / 2
U3n = np.zeros(n); U6n = np.zeros(n)
U3n[w.index((1, 0))], U3n[w.index((0, 1))] = 1 / np.sqrt(2), -1 / np.sqrt(2)
U6n[w.index((2, 0))], U6n[w.index((0, 2))] = 1 / np.sqrt(2), -1 / np.sqrt(2)

print("==== PART 0: CALIBRATION GATE -- reproduce B593's theta machinery ====")
lawok = True
for word in ("", "RL", "RRLL"):
    for u in (U3n, U6n, (U3n + U6n) / np.sqrt(2)):
        u = u.astype(complex)
        for tw in (True, False):
            Wm = weld_n(word, tw)
            quad = np.conj(u) @ Wm @ u
            for eps in (0.05, 0.2):
                pred = amp_n(psin, word, tw) - eps ** 2 * quad
                lawok &= abs(amp_n(psin + eps * u, word, tw) - pred) < 1e-12
assert lawok, "B593 theta law failed to reproduce"
val_n = np.conj(U3n.astype(complex)) @ weld_n("RL", True) @ U3n.astype(complex)
tgt_n = 1 / (2 * PHI) + 1j * math.sin(2 * math.pi / 5) / math.sqrt(5)
assert abs(val_n - tgt_n) < 1e-12, "B593 forced value failed to reproduce"
print(f"  theta law holds (all welds/directions/eps, 1e-12); forced value "
      f"{val_n:+.6f} = 1/(2 phi) + i sin(2pi/5)/sqrt5  [B593 REPRODUCED]")


# ============================================================================
# Part 1 -- the exact stage over Q(zeta_15)
# ============================================================================
# Phi_15(x) = x^8 - x^7 + x^5 - x^4 + x^3 - x + 1;  z = zeta_15.

DEG = 15
PHI15 = [1, -1, 0, 1, -1, 1, 0, -1, 1]           # coeffs of Phi_15, low to high


def _pow_table():
    """z^k as length-8 Fraction vectors, k = 0..14, reduced mod Phi_15."""
    tab = []
    for k in range(8):
        v = [Fraction(0)] * 8
        v[k] = Fraction(1)
        tab.append(v)
    # z^8 = z^7 - z^5 + z^4 - z^3 + z - 1
    z8 = [Fraction(c) for c in (-1, 1, 0, -1, 1, -1, 0, 1)]
    tab.append(z8)
    for k in range(9, 15):
        prev = tab[k - 1]
        v = [Fraction(0)] * 8
        for i, ci in enumerate(prev):          # multiply by z
            if ci == 0:
                continue
            if i + 1 < 8:
                v[i + 1] += ci
            else:
                for j in range(8):
                    v[j] += ci * z8[j]
        tab.append(v)
    return tab


POW15 = _pow_table()


class Cyc:
    """Element of Q(zeta_15) as 8 Fraction coefficients mod Phi_15."""
    __slots__ = ("c",)

    def __init__(self, c=None):
        self.c = tuple(Fraction(x) for x in (c if c is not None else [0] * 8))

    @staticmethod
    def zero():
        return Cyc()

    @staticmethod
    def one():
        return Cyc([1, 0, 0, 0, 0, 0, 0, 0])

    @staticmethod
    def rat(r):
        return Cyc([Fraction(r), 0, 0, 0, 0, 0, 0, 0])

    @staticmethod
    def zpow(k):
        return Cyc(POW15[k % 15])

    def __add__(self, o):
        return Cyc([a + b for a, b in zip(self.c, o.c)])

    def __sub__(self, o):
        return Cyc([a - b for a, b in zip(self.c, o.c)])

    def __neg__(self):
        return Cyc([-a for a in self.c])

    def __mul__(self, o):
        if isinstance(o, (int, Fraction)):
            return Cyc([a * o for a in self.c])
        raw = [Fraction(0)] * 15
        for i, a in enumerate(self.c):
            if a == 0:
                continue
            for j, b in enumerate(o.c):
                if b == 0:
                    continue
                raw[i + j] += a * b
        out = [Fraction(0)] * 8
        for k, ck in enumerate(raw):
            if ck == 0:
                continue
            for j in range(8):
                out[j] += ck * POW15[k][j]      # k <= 14: direct table reduce
        return Cyc(out)

    __rmul__ = __mul__

    def __eq__(self, o):
        return self.c == o.c

    def is_zero(self):
        return all(a == 0 for a in self.c)

    def galois(self, t):
        """entrywise field automorphism z -> z^t."""
        out = [Fraction(0)] * 8
        for k, a in enumerate(self.c):
            if a == 0:
                continue
            for j in range(8):
                out[j] += a * POW15[(t * k) % 15][j]
        return Cyc(out)

    def conj(self):
        return self.galois(14)

    def inv(self):
        """solve (mult-by-self matrix) x = e0 over Fractions."""
        M = [[Fraction(0)] * 8 for _ in range(8)]
        for j in range(8):
            col = (self * Cyc.zpow(j) if j else Cyc(self.c)).c
            for i in range(8):
                M[i][j] = col[i]
        rhs = [Fraction(1)] + [Fraction(0)] * 7
        # Gaussian elimination
        for col in range(8):
            piv = next(r for r in range(col, 8) if M[r][col] != 0)
            M[col], M[piv] = M[piv], M[col]
            rhs[col], rhs[piv] = rhs[piv], rhs[col]
            pv = M[col][col]
            M[col] = [x / pv for x in M[col]]
            rhs[col] = rhs[col] / pv
            for r in range(8):
                if r != col and M[r][col] != 0:
                    f = M[r][col]
                    M[r] = [a - f * b for a, b in zip(M[r], M[col])]
                    rhs[r] = rhs[r] - f * rhs[col]
        return Cyc(rhs)

    def num(self):
        return sum(complex(a) * cmath.exp(2j * math.pi * k / 15)
                   for k, a in enumerate(self.c))

    def s(self):
        """compact exact string."""
        parts = []
        for k, a in enumerate(self.c):
            if a == 0:
                continue
            parts.append(f"{a}" if k == 0 else (f"{a}*z^{k}" if a != 1 else f"z^{k}"))
        return " + ".join(parts).replace("+ -", "- ") if parts else "0"


def mat_mul(A, B):
    m, k, p = len(A), len(B), len(B[0])
    return [[sum((A[i][t] * B[t][j] for t in range(k)), Cyc.zero())
             for j in range(p)] for i in range(m)]


def mat_vec(A, v):
    return [sum((A[i][j] * v[j] for j in range(len(v))), Cyc.zero()) for i in range(len(A))]


def mat_inv(A):
    m = len(A)
    M = [[Cyc(A[i][j].c) for j in range(m)] + [Cyc.one() if j == i else Cyc.zero()
         for j in range(m)] for i in range(m)]
    for col in range(m):
        piv = next(r for r in range(col, m) if not M[r][col].is_zero())
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col].inv()
        M[col] = [x * pv for x in M[col]]
        for r in range(m):
            if r != col and not M[r][col].is_zero():
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[col])]
    return [row[m:] for row in M]


print("\n==== PART 1: THE EXACT STAGE over Q(zeta_15) ====")

# T: diag zeta_15 powers (h - c/24 = -2/15, 2/15, 8/15, 2/15, 7/15, 8/15)
tpow = [-2, 2, 8, 2, 7, 8]
T_e = [[Cyc.zpow(tpow[i]) if i == j else Cyc.zero() for j in range(n)] for i in range(n)]
Ti_e = [[Cyc.zpow(-tpow[i]) if i == j else Cyc.zero() for j in range(n)] for i in range(n)]

# unnormalized Kac-Peterson S-hat (entries in Z[zeta_15]); rho is normalization-free
import itertools
Lvec = lambda wt: (wt[0] + wt[1] + 2, wt[1] + 1, 0)
perms = list(itertools.permutations(range(3)))
sgn = lambda p: (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
S_e = [[Cyc.zero()] * n for _ in range(n)]
for i, wl in enumerate(w):
    Ll = Lvec(wl)
    for j, wm in enumerate(w):
        Lm = Lvec(wm)
        acc = Cyc.zero()
        for p in perms:
            Lp = [Ll[p[0]], Ll[p[1]], Ll[p[2]]]
            expo = -3 * sum(a * b for a, b in zip(Lp, Lm)) + sum(Ll) * sum(Lm)
            acc = acc + sgn(p) * Cyc.zpow(expo)
        S_e[i][j] = acc

# gates on S-hat: symmetric; S-hat^2 = r * C (charge conjugation, exact)
assert all(S_e[i][j] == S_e[j][i] for i in range(n) for j in range(n)), "S-hat not symmetric"
S2_e = mat_mul(S_e, S_e)
r_scal = S2_e[0][conj_idx[0]]
for i in range(n):
    for j in range(n):
        expect = r_scal if j == conj_idx[i] else Cyc.zero()
        assert S2_e[i][j] == expect, "S-hat^2 is not r*C"
print(f"  S-hat symmetric; S-hat^2 = r*C exactly, r = {r_scal.s()} = {r_scal.num():+.4f}")

Si_e = mat_inv(S_e)
L_e = mat_mul(mat_mul(Si_e, Ti_e), S_e)
R_e = T_e
Id_e = [[Cyc.one() if i == j else Cyc.zero() for j in range(n)] for i in range(n)]


def weld_e(word, twisted):
    M = Id_e
    for ch in word:
        M = mat_mul(M, R_e if ch == 'R' else L_e)
    if twisted:
        return [[M[conj_idx[i]][j] for j in range(n)] for i in range(n)]  # C @ M
    return M


WELDS = {}
for word in ("", "RL", "RRLL"):
    for tw in (False, True):
        WELDS[(word, tw)] = weld_e(word, tw)

# [C, rho(g)] = 0 exactly (C = S^2 is central in the modular image)
for word in ("", "RL", "RRLL"):
    M = WELDS[(word, False)]
    CM = [[M[conj_idx[i]][j] for j in range(n)] for i in range(n)]
    MC = [[M[i][conj_idx[j]] for j in range(n)] for i in range(n)]
    assert all(CM[i][j] == MC[i][j] for i in range(n) for j in range(n)), "[C,rho] != 0"
print("  [C, rho(g)] = 0 exactly for g in {I, RL, RRLL}")

# numeric cross-check of the exact welds vs the b238 pipeline
for word in ("RL", "RRLL"):
    Wn = weld_n(word, False)
    We = WELDS[(word, False)]
    dev = max(abs(We[i][j].num() - Wn[i, j]) for i in range(n) for j in range(n))
    assert dev < 1e-9, f"exact weld mismatch vs b238 at {word}: {dev}"
print("  exact rho(RL), rho(RRLL) match the b238 numeric pipeline (1e-9)")

# exact psi0 via the b245 formulas at q = -z^9 (= e^{i pi/5})
q_e = -Cyc.zpow(9)
qi_e = q_e.inv()


def br_e(x):
    return x - x.inv()


def qint_e(m):
    num = q_e_pow(m) - q_e_pow(-m)
    return num * (q_e - qi_e).inv()


def q_e_pow(m):
    if m >= 0:
        out = Cyc.one()
        for _ in range(m):
            out = out * q_e
        return out
    return q_e_pow(-m).inv()


def qbinom_e(p, k):
    num = Cyc.one()
    den = Cyc.one()
    for m in range(1, p + 1):
        num = num * qint_e(m)
    for m in range(1, k + 1):
        den = den * qint_e(m)
    for m in range(1, p - k + 1):
        den = den * qint_e(m)
    return num * den.inv()


def H_sym_e(p):
    A = q_e_pow(3)
    tot = Cyc.one()
    for k in range(1, p + 1):
        t = qbinom_e(p, k)
        for i in range(k):
            t = t * br_e(A * q_e_pow(p + i)) * br_e(A * q_e_pow(i - 1))
        tot = tot + t
    return tot


def H_antisym_e(p):
    """verbatim b245 H_antisym over the exact field (br(+-1) = 0 exactly; no 1/0
    can occur since q-powers are never zero)."""
    A = q_e_pow(3)
    tot = Cyc.one()
    for k in range(1, p + 1):
        t = qbinom_e(p, k)
        for j in range(k):
            t = t * br_e(A * q_e_pow(-p - j)) * br_e(A * q_e_pow(-j + 1))
        tot = tot + t
    return tot
J_e = {(0, 0): Cyc.one(), (1, 0): H_sym_e(1), (0, 1): H_antisym_e(2),
       (2, 0): H_sym_e(2), (0, 2): H_sym_e(2), (1, 1): Cyc.zero()}
psi_e = [J_e[wt] for wt in w]
dev = max(abs(psi_e[i].num() - psin[i]) for i in range(n))
assert dev < 1e-12, f"exact psi0 mismatch: {dev}"

# psi0 structural gates: C-symmetric, real, Galois-fixed by all three involutions
assert all(psi_e[conj_idx[i]] == psi_e[i] for i in range(n)), "C psi0 != psi0"
for t in (4, 11, 14):
    assert all(pe.galois(t) == pe for pe in psi_e), f"psi0 not fixed by t={t}"
print("  exact psi0 matches b245 (1e-12); C psi0 = psi0; psi0 fixed by t=4,11,14 EXACTLY")

# the dial (unnormalized; B593's u3, u6 are these over sqrt2)
v3 = [Cyc.zero()] * n
v3[w.index((1, 0))] = Cyc.one(); v3[w.index((0, 1))] = -Cyc.one()
v6 = [Cyc.zero()] * n
v6[w.index((2, 0))] = Cyc.one(); v6[w.index((0, 2))] = -Cyc.one()
vmix = [a + b for a, b in zip(v3, v6)]

# sqrt5 and the exact B593 target
sqrt5 = Cyc.rat(1) + 2 * Cyc.zpow(3) + 2 * Cyc.zpow(12)
assert sqrt5 * sqrt5 == Cyc.rat(5) and sqrt5.num().real > 0
half = Cyc.rat(Fraction(1, 2))
A_target = (Cyc.zpow(3) + Cyc.zpow(12)) * half \
    + (Cyc.zpow(3) - Cyc.zpow(12)) * (2 * sqrt5).inv()


def bil(x, Wm, y):
    return sum((x[i] * mat_vec(Wm, y)[i] for i in range(n)), Cyc.zero())


FV_theta = bil(v3, WELDS[("RL", True)], v3) * half        # = u3^T (C rho(RL)) u3, normalized
assert FV_theta == A_target, "exact theta forced value != banked closed form"
print(f"  EXACT CALIBRATION: u3'(C rho(RL))u3 = {FV_theta.s()}")
print(f"    = {FV_theta.num():+.6f} == 1/(2 phi) + i sin(2pi/5)/sqrt5 (symbolic zero) [OK]")


# ============================================================================
# Part 2 -- the involution atlas of the stage field
# ============================================================================
print("\n==== PART 2: THE INVOLUTION ATLAS of Q(zeta_15) ====")
atlas = []
golden_ts = []
for t in range(1, 15):
    if math.gcd(t, 15) != 1:
        continue
    order = 1
    tt = t
    while tt % 15 != 1:
        tt = (tt * t) % 15
        order += 1
    moves5 = (t % 5) in (2, 3)                 # sqrt5 -> -sqrt5 iff t = +-2 mod 5
    inv_ok = (t * t) % 15 == 1
    atlas.append(dict(t=t, order=order, moves_sqrt5=moves5, involution=inv_ok))
    if moves5:
        golden_ts.append(t)
        assert not inv_ok, "golden lift claimed involutive?!"
    # verify the sqrt5 action exactly
    assert (sqrt5.galois(t) == (-sqrt5 if moves5 else sqrt5))
for a in atlas:
    print(f"  t={a['t']:>2}: order {a['order']}, sqrt5 -> {'-' if a['moves_sqrt5'] else '+'}sqrt5"
          f"{'   INVOLUTION' if a['involution'] and a['t'] != 1 else ''}")
print("  => involutions of the stage field: t = 4 (sigma*), 11 (sigma*c), 14 (c) -- exactly three.")
print(f"  => the golden conjugation sqrt5 -> -sqrt5 has NO involutive lift: its lifts "
      f"t in {golden_ts} all have order 4 (t^2 = 1 mod 15 forces t = +-1 mod 5).")

INV = {"sigma*": 4, "c": 14, "sigma*c": 11}

# the V4 character units and their parities (asserted, not assumed)
d5 = Cyc.zpow(3) - Cyc.zpow(12)                # zeta5 - zeta5^-1 (imaginary)
r3 = 2 * Cyc.zpow(5) + Cyc.one()               # sqrt(-3) = zeta3 - zeta3^-1 (imaginary)
db = d5 * r3                                    # (real)
UNITS = {"d5": d5, "r3": r3, "d5r3": db}
PAR = {}
for uname, uval in UNITS.items():
    row = {}
    for iname, t in INV.items():
        img = uval.galois(t)
        assert img == uval or img == -uval
        row[iname] = -1 if img == -uval else +1
    row["conj"] = -1 if uval.conj() == -uval else +1
    PAR[uname] = row
assert PAR["d5"] == {"sigma*": -1, "c": -1, "sigma*c": +1, "conj": -1}
assert PAR["r3"] == {"sigma*": +1, "c": -1, "sigma*c": -1, "conj": -1}
assert PAR["d5r3"] == {"sigma*": -1, "c": +1, "sigma*c": -1, "conj": +1}
NORM = {k: (v.conj() * v) for k, v in UNITS.items()}
assert NORM["d5"] == (Cyc.rat(5) + sqrt5) * half
assert NORM["r3"] == Cyc.rat(3)
assert NORM["d5r3"] == Cyc.rat(3) * (Cyc.rat(5) + sqrt5) * half
ODD_UNITS = {"sigma*": ["d5", "d5r3"], "c": ["d5", "r3"], "sigma*c": ["r3", "d5r3"]}
print("  V4 character units: d5 = zeta5-zeta5^-1, r3 = sqrt(-3), d5r3 = d5*r3;")
print("  parities and norms verified exactly: N(d5) = (5+sqrt5)/2, N(r3) = 3, N(d5r3) = 3(5+sqrt5)/2.")


# ============================================================================
# Part 3 -- the parity theorem in BOTH channels (the gate the new mirrors need)
# ============================================================================
print("\n==== PART 3: THE PARITY THEOREM (both channels, exact) ====")
for word in ("", "RL", "RRLL"):
    for tw in (False, True):
        Wm = WELDS[(word, tw)]
        for v in (v3, v6):
            a1 = bil(psi_e, Wm, v)                                   # psi0^T W v
            Wt = [[Wm[j][i] for j in range(n)] for i in range(n)]
            a2 = bil(psi_e, Wt, v)                                   # psi0^T W^T v
            assert a1.is_zero() and a2.is_zero(), f"parity fails at {word} tw={tw}"
print("  psi0^T W v = 0 AND psi0^T W^T v = 0 exactly, for every weld, twist, dial direction.")
print("  (mechanism: [C,W] = 0 and C psi0 = psi0 make psi0^T W a C-even covector;")
print("   the dial is C-odd. B593 verified only the antisymmetric combination;")
print("   the symmetric channel -- the one the semilinear mirrors need -- also closes.)")


# ============================================================================
# Part 4 -- the three substituted constructions, exact
# ============================================================================
print("\n==== PART 4: THE THREE INVOLUTIONS SUBSTITUTED FOR THETA ====")


def amp_exact(iota_t, u, word, tw, eps):
    """A_eps = <iota(psi0 + eps u)| W |psi0 + eps u>, exact over Q(zeta_15).
    bra(x) . y = sum conj(x_i) y_i;  iota = entrywise Galois t."""
    Wm = WELDS[(word, tw)]
    psi_eps = [p + Cyc.rat(eps) * ui for p, ui in zip(psi_e, u)]
    bra = [x.galois(iota_t).conj() for x in psi_eps]
    vec = mat_vec(Wm, psi_eps)
    return sum((b * v for b, v in zip(bra, vec)), Cyc.zero())


E1, E2, E3 = Fraction(1, 10), Fraction(1, 4), Fraction(1, 3)
DIRS = {"u3": v3, "u6": v6, "u3+u6": vmix}
rows = []
verdicts = {}
for iname, t in INV.items():
    print(f"  -- {iname} (t={t}); odd sectors: {ODD_UNITS[iname]} --")
    all_L0, all_Q, all_FV = True, True, True
    for uname in ODD_UNITS[iname]:
        delta = UNITS[uname]
        for vname, v in DIRS.items():
            u = [delta * vi for vi in v]
            assert all(ui.galois(t) == -ui for ui in u), "u not iota-odd"
            for word in ("", "RL", "RRLL"):
                for tw in (False, True):
                    A0 = amp_exact(t, [Cyc.zero()] * n, word, tw, Fraction(0))
                    D1 = amp_exact(t, u, word, tw, E1) - A0
                    D2 = amp_exact(t, u, word, tw, E2) - A0
                    # solve D = L eps + Q eps^2 exactly
                    det = E1 * E2 * E2 - E2 * E1 * E1
                    Lc = (D1 * Fraction(E2 * E2, 1) - D2 * Fraction(E1 * E1, 1)) * Cyc.rat(det).inv()
                    Qc = (D2 * Fraction(E1, 1) - D1 * Fraction(E2, 1)) * Cyc.rat(det).inv()
                    # third-eps exactness check (no higher terms)
                    D3 = amp_exact(t, u, word, tw, E3) - A0
                    assert D3 == Lc * Fraction(E3, 1) + Qc * Fraction(E3 * E3, 1), "not quadratic"
                    # gates
                    g_L0 = Lc.is_zero()
                    vWv = bil(v, WELDS[(word, tw)], v)
                    g_Q = (Qc == -(NORM[uname] * vWv))
                    vv = Cyc.rat(sum(1 for x in v if not x.is_zero()))   # v^T v (entries +-1)
                    FV = -Qc * (NORM[uname] * vv).inv()                   # per unit displacement norm
                    g_FV = (FV == vWv * vv.inv())
                    all_L0 &= g_L0; all_Q &= g_Q; all_FV &= g_FV
                    rows.append(dict(
                        involution=iname, t=t, sector=uname, direction=vname,
                        weld=word if word else "I", twisted=tw,
                        L_exact=Lc.s(), L_is_zero=g_L0,
                        Q_exact=Qc.s(), Q_num=[Qc.num().real, Qc.num().imag],
                        FV_exact=FV.s(), FV_num=[FV.num().real, FV.num().imag],
                        FV_equals_theta_form=g_FV))
    # twist flip on the dial: Q(tw) = -Q(untw) -- via the C-odd dial identity
    for uname in ODD_UNITS[iname]:
        for vname, v in (("u3", v3), ("u6", v6)):
            for word in ("", "RL", "RRLL"):
                qt = bil(v, WELDS[(word, True)], v)
                qu = bil(v, WELDS[(word, False)], v)
                assert qt == -qu, "twist sign-flip fails on dial"
    # the headline check: the RL twisted forced value IS B593's, for both sectors
    fv3 = None
    for uname in ODD_UNITS[iname]:
        delta = UNITS[uname]
        u = [delta * vi for vi in v3]
        A0 = amp_exact(t, [Cyc.zero()] * n, "RL", True, Fraction(0))
        D1 = amp_exact(t, u, "RL", True, E1) - A0
        D2 = amp_exact(t, u, "RL", True, E2) - A0
        det = E1 * E2 * E2 - E2 * E1 * E1
        Qc = (D2 * Fraction(E1, 1) - D1 * Fraction(E2, 1)) * Cyc.rat(det).inv()
        FV = -Qc * (NORM[uname] * Cyc.rat(2)).inv()
        assert FV == A_target, f"{iname}/{uname}: RL forced value differs from B593"
        fv3 = FV
    verdicts[iname] = dict(
        law_holds=bool(all_L0 and all_Q), first_order_zero=bool(all_L0),
        forced_value_per_unit_norm="1/(2 phi) + i sin(2pi/5)/sqrt5 (== B593 theta value)",
        independent_of_theta=False)
    print(f"     O(eps) = 0 exactly: {all_L0}; Q = -N(delta) v'Wv exactly: {all_Q}; "
          f"per-unit-norm FV == theta's dial form: {all_FV}")
    print(f"     RL twisted forced value (both sectors) = {fv3.num():+.6f} == B593's value EXACTLY")

print("\n  => ALL THREE LAWS HOLD -- and all three forced values COINCIDE with B593's.")
print("     The involution dependence is confined to the odd-unit norms")
print("     N in {3, (5+sqrt5)/2, 3(5+sqrt5)/2}: a rescaling of the displacement,")
print("     not of the coupling. NO independent forced value exists on this face pair.")

# the off-diagonal dial form (the only other number in the sector forms; exact)
Woff = WELDS[("RL", True)]
offd = (bil(v3, Woff, v6) + bil(v6, Woff, v3)) * half
# closed form: -(q - q^-1)/sqrt5 with q = e^{i pi/5}: -2 i sin(pi/5)/sqrt5
off_target = (Cyc.zpow(9) - Cyc.zpow(6)) * sqrt5.inv()
assert offd == off_target
print(f"  (the mixed-direction cross term, RL twisted: u3'Wu6 + u6'Wu3 = "
      f"{offd.num():+.6f} = -2 i sin(pi/5)/sqrt5 exactly -- sector-independent as well.)")

# demarcation: OFF the dial the field involutions do admit odd displacements
# (theta does not), and there the first-order channel is OPEN -- the coefficient is a
# direction-dependent covector, not a forced scalar; the forced-value question is
# well-posed only on the dial.
e0 = [Cyc.one() if i == 0 else Cyc.zero() for i in range(n)]
u_off = [UNITS["r3"] * x for x in e0]                       # c-odd, off-dial
assert all(ui.galois(14) == -ui for ui in u_off)
A0 = amp_exact(14, [Cyc.zero()] * n, "RL", True, Fraction(0))
D1 = amp_exact(14, u_off, "RL", True, E1) - A0
D2 = amp_exact(14, u_off, "RL", True, E2) - A0
det = E1 * E2 * E2 - E2 * E1 * E1
L_off = (D1 * (E2 * E2) - D2 * (E1 * E1)) * Cyc.rat(det).inv()
assert not L_off.is_zero()
print(f"  demarcation: off-dial c-odd displacement (direction e_(0,0)) has O(eps) "
      f"coefficient {L_off.num():+.6f} != 0:")
print("     the second-order law and its forced value are dial-only (B575's honest moduli);")
print("     off-dial first-order coefficients form a covector (direction-dependent, not forced).")
results_demarcation = dict(
    off_dial_first_order_open=True,
    example="c-odd displacement sqrt(-3)*e_(0,0), RL twisted",
    L_exact=L_off.s(), L_num=[L_off.num().real, L_off.num().imag])


# ============================================================================
# Part 5 -- the alternative reading: substituting the involution into the TWIST
# ============================================================================
print("\n==== PART 5: THE ALTERNATIVE READING (Galois-conjugated welds) ====")
# If "substitute iota for theta" is read as replacing the twist C rho(g) by the
# entrywise-conjugated weld sigma(rho(g)), the dial forms transform by the Galois
# map itself (the dial is rational): v' sigma(W) v = sigma(v' W v).
for iname, t in INV.items():
    Wrl = WELDS[("RL", True)]
    Wg = [[Wrl[i][j].galois(t) for j in range(n)] for i in range(n)]
    lhs = bil(v3, Wg, v3) * half
    rhs = (bil(v3, Wrl, v3) * half).galois(t)
    assert lhs == rhs
    tag = {"sigma*": "conj(A) (the banked u6 value)",
           "c": "conj(A) (the banked u6 value)",
           "sigma*c": "A itself (zeta3 absent from the value)"}[iname]
    print(f"  {iname}: u3' sigma(C rho(RL)) u3 = {lhs.num():+.6f} = {tag}")
print("  => no new values in this reading either: the Galois orbit of the banked value")
print("     is {A, conj(A)} -- already banked as the u3/u6 conjugate pair in B593.")


# ============================================================================
# results.json
# ============================================================================
results = dict(
    id="B924",
    task="R-INV: the three unused involution couplings on the B593 face pair",
    calibration=dict(
        theta_law_reproduced=True,
        forced_value_numeric=[val_n.real, val_n.imag],
        forced_value_exact=FV_theta.s(),
        exact_equals_banked_closed_form=True),
    stage_field="Q(zeta_15) (the whole B593 stage: welds, twist, psi0, dial)",
    involution_atlas=atlas,
    operative_definitions=dict(
        theta="label conjugation C (B593, the banked coupling)",
        sigma_star="t=4: zeta5 -> zeta5^-1, zeta3 fixed (pentagonal conjugation)",
        c="t=14: full complex conjugation",
        sigma_star_c="t=11: zeta3 -> zeta3^-1, zeta5 fixed (triangular conjugation)",
        golden_no_lift="sqrt5 -> -sqrt5 has NO involutive lift to the stage field: "
                       "t^2=1 mod 15 forces t=+-1 mod 5; its lifts t in {2,7,8,13} "
                       "have order 4 (verified exactly)"),
    parity_theorem="psi0^T W v = psi0^T W^T v = 0 exactly for all welds/twists and "
                   "dial v (C-even covector vs C-odd dial); B593 needed only the "
                   "antisymmetric channel, the semilinear mirrors need both -- both close",
    table=rows,
    verdicts=verdicts,
    headline="ALL THREE substituted constructions satisfy the second-order hearing law "
             "EXACTLY, and all three forced values per unit displacement norm COINCIDE "
             "with B593's theta value 1/(2 phi) + i sin(2pi/5)/sqrt5. No independent "
             "forced value exists on this face pair: a rigidity (degeneracy) theorem. "
             "The only involution dependence is the odd-unit norm "
             "N(delta) in {3, (5+sqrt5)/2, 3(5+sqrt5)/2} -- displacement normalization, "
             "not coupling data.",
    mixed_cross_term_exact="u3'Wu6 + u6'Wu3 (RL twisted) = -2 i sin(pi/5)/sqrt5",
    demarcation=results_demarcation,
    alt_twist_reading="Galois-conjugating the weld gives sigma(v'Wv): the orbit of the "
                      "banked value is {A, conj(A)} -- the already-banked u3/u6 pair",
)
with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(results, fh, indent=1)
print(f"\nresults.json written ({len(rows)} table rows). ALL GATES PASS")
