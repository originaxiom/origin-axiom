#!/usr/bin/env python3
"""SM-C2, harvest row 1521 (WILSON_FAMILY_KERNEL_AND_LEVEL_FOUR_REGISTER_MAP @ ac28256fc): this seat's own exact check of
(a) the counts (1) N_0 = delta(L) + 2 delta(eta L), N_1 = 1 + 2 delta(L), N_j = j (j >= 2) from the line formula
N_j(L) = h0(S^(j+2) L^-1) + h0(S^(1+j) L) + h0(S^(1-j) L), and (2) the gauge-five multiplicities 4 + 2 delta(chi^2),
4 + 2 delta(chi^3); (b) the uniform-roster theorem (5) [for every eta in J[2]: chi^2, chi^3, chi^5 != 1, chi^5 != eta]
iff [chi^3 != 1 and chi^10 != 1], by enumeration of all torsion points of J = (R/Z)^2 of order dividing n <= 60;
(c) the exceptional set (6): 108 points, populations 1, 3, 8, 24, 72 for orders 1, 2, 3, 5, 10, least admissible order 4;
(d) the moves (7) on (p, q), the Hodge-norm invariance (8), the order-4 (12 -> 6) and order-7 (48 -> 24) packets and
L, R transitivity on each; (e) the permutations (10) and the quaternion intertwiner (11) for both generators; (f) the
rejecting controls: Ad(i) j = -j, g_l^4 = -1 while L^4 = 1 on the packet; (g) the fixed-state observation: no nonzero
(p, q) of order <= 40 fixed up to sign by both L and R. Planted: the condition with chi^10 != 1 dropped must disagree
with (4) somewhere."""
import json
import sys
from fractions import Fraction as F
from itertools import product
from math import gcd
from pathlib import Path

import sympy as sp

out = {}


def bf(x):
    return x // 2 if x <= 0 else -(-x // 2) - 1


def Hd(d, triv):
    return 0 if d < 0 else (d if d > 0 else int(triv))


# a character is a pair of rationals mod 1; eta in J[2]; "trivial" tests
def triv(ch):
    return ch[0] % 1 == 0 and ch[1] % 1 == 0


mul = lambda ch, k: (ch[0] * k % 1, ch[1] * k % 1)
add = lambda x, y: ((x[0] + y[0]) % 1, (x[1] + y[1]) % 1)
neg = lambda x: ((-x[0]) % 1, (-x[1]) % 1)


def h0(a, L, eta):
    return Hd(bf(a), triv(add(mul(eta, a), L)))


def Nj(j, L, eta):
    return h0(j + 2, neg(L), eta) + h0(1 + j, L, eta) + h0(1 - j, L, eta)


J2 = [(F(x, 2), F(y, 2)) for x in (0, 1) for y in (0, 1)]
sample = [(F(0), F(0)), (F(1, 3), F(0)), (F(1, 4), F(1, 2)), (F(1, 2), F(1, 2)), (F(2, 7), F(3, 7))]
a_ok = True
for L in sample:
    for eta in J2:
        d = lambda ch: int(triv(ch))
        a_ok &= Nj(0, L, eta) == d(L) + 2 * d(add(eta, L))
        a_ok &= Nj(1, L, eta) == 1 + 2 * d(L)
        a_ok &= all(Nj(j, L, eta) == j for j in range(2, 9))
        chi = L
        a_ok &= Nj(1, mul(chi, 2), eta) + Nj(3, mul(chi, 2), eta) == 4 + 2 * d(mul(chi, 2))
        a_ok &= Nj(1, mul(chi, 3), eta) + Nj(3, mul(chi, 3), eta) == 4 + 2 * d(mul(chi, 3))
out["(a)_ok"] = a_ok


def cond4(chi, eta):
    return (not triv(mul(chi, 2)) and not triv(mul(chi, 3)) and not triv(mul(chi, 5))
            and mul(chi, 5) != (eta[0] % 1, eta[1] % 1))


uniform = lambda chi: all(cond4(chi, eta) for eta in J2)
claim5 = lambda chi: not triv(mul(chi, 3)) and not triv(mul(chi, 10))
planted = lambda chi: not triv(mul(chi, 3))
mismatch, planted_mismatch, tested = 0, 0, 0
for n in range(1, 61):
    for x, y in product(range(n), repeat=2):
        if gcd(gcd(x, y), n) != 1:
            continue
        chi = (F(x, n), F(y, n))
        tested += 1
        u = uniform(chi)
        mismatch += u != claim5(chi)
        planted_mismatch += u != planted(chi)
out["(b)_points_tested"], out["(b)_mismatches"] = tested, mismatch
pts = [(F(x, 30), F(y, 30)) for x, y in product(range(30), repeat=2)]
exc = [p for p in pts if not claim5(p)]


def order(p):
    return sp.ilcm(F(p[0]).denominator, F(p[1]).denominator)


pop = {}
for p in exc:
    pop[int(order(p))] = pop.get(int(order(p)), 0) + 1
out["(c)_exceptional_count"], out["(c)_populations_by_order"] = len(exc), dict(sorted(pop.items()))
least = min(n for n in range(1, 61) if all(claim5((F(x, n), F(y, n))) for x, y in product(range(n), repeat=2)
                                           if gcd(gcd(x, y), n) == 1))
out["(c)_least_admissible_order"] = least
c_ok = len(exc) == 108 and pop == {1: 1, 2: 3, 3: 8, 5: 24, 10: 72} and least == 4
# (d) moves, norm, packets
tau, dp, dq = sp.symbols("tau dp dq")
taub = sp.Symbol("taubar")
Lm = lambda v, n: (v[0] % n, (v[0] + v[1]) % n)
Rm = lambda v, n: ((v[0] + v[1]) % n, v[1] % n)
numR = (dq - (tau / (tau + 1)) * (dp + dq)) - (dq - tau * dp) / (tau + 1)
numL = ((dp + dq) - (tau + 1) * dp) - (dq - tau * dp)
x, y = sp.symbols("x y", real=True)
t = x + sp.I * y
imR = sp.simplify(sp.im(sp.expand_complex(t / (t + 1))) - y / ((x + 1) ** 2 + y ** 2))
d_ok = sp.simplify(numR) == 0 and sp.simplify(numL) == 0 and imR == 0


def packet(n):
    prim = [(a, b) for a, b in product(range(n), repeat=2) if gcd(gcd(a, b), n) == 1]
    cls = {}
    for v in prim:
        key = min(v, ((-v[0]) % n, (-v[1]) % n))
        cls.setdefault(key, set()).add(v)
    reps = sorted(cls)
    canon = lambda v: min(v, ((-v[0]) % n, (-v[1]) % n))
    seen, frontier = {reps[0]}, [reps[0]]
    while frontier:
        v = frontier.pop()
        for w in (canon(Lm(v, n)), canon(Rm(v, n))):
            if w not in seen:
                seen.add(w)
                frontier.append(w)
    return len(prim), len(reps), len(seen) == len(reps)


p4, p7 = packet(4), packet(7)
out["(d)_order4_packet"], out["(d)_order7_packet"] = p4, p7
d_ok = d_ok and p4 == (12, 6, True) and p7 == (48, 24, True)
# (e) permutations and the quaternion intertwiner
st = {"A": (1, 0), "B": (0, 1), "C": (1, 1), "D": (1, 2), "E": (1, 3), "F": (2, 1)}
canon4 = lambda v: min(v, ((-v[0]) % 4, (-v[1]) % 4))
name = {canon4(v): k for k, v in st.items()}
Lp = {k: name[canon4(Lm(v, 4))] for k, v in st.items()}
Rp = {k: name[canon4(Rm(v, 4))] for k, v in st.items()}
out["(e)_L_perm"], out["(e)_R_perm"] = Lp, Rp
e_perm_ok = (Lp == {"A": "C", "C": "D", "D": "E", "E": "A", "B": "B", "F": "F"}
             and Rp == {"B": "C", "C": "F", "F": "E", "E": "B", "A": "A", "D": "D"})
Qt = sp.algebras.Quaternion
qi, qj, qk = Qt(0, 1, 0, 0), Qt(0, 0, 1, 0), Qt(0, 0, 0, 1)
gl = Qt(1 / sp.sqrt(2), 1 / sp.sqrt(2), 0, 0)
gr = Qt(1 / sp.sqrt(2), 0, -1 / sp.sqrt(2), 0)
Ad = lambda g, v: (g * v * g.inverse()).simplify() if hasattr(g * v, "simplify") else g * v * g.inverse()
qmap = {"A": qj, "B": qi, "C": qk, "D": -qj, "E": -qk, "F": -qi}
eqq = lambda p, q_: all(sp.simplify(a_ - b_) == 0 for a_, b_ in zip([p.a, p.b, p.c, p.d], [q_.a, q_.b, q_.c, q_.d]))
e_int_ok = all(eqq(Ad(gl, qmap[k]), qmap[Lp[k]]) and eqq(Ad(gr, qmap[k]), qmap[Rp[k]]) for k in st)
out["(e)_ok"] = e_perm_ok and e_int_ok
# (f) controls
f1 = eqq(Ad(qi, qj), -qj)
gl4 = gl * gl * gl * gl
f2 = eqq(gl4, Qt(-1, 0, 0, 0))
L4_id = all(canon4(Lm(Lm(Lm(Lm(v, 4), 4), 4), 4)) == canon4(v) for v in st.values())
out["(f)_ok"] = f1 and f2 and L4_id
# (g) fixed states
fixed = []
for n in range(2, 41):
    for a_, b_ in product(range(n), repeat=2):
        if (a_, b_) == (0, 0):
            continue
        v = (a_, b_)
        isfix = lambda w: w == v or w == ((-v[0]) % n, (-v[1]) % n)
        if isfix(Lm(v, n)) and isfix(Rm(v, n)):
            fixed.append((n, v))
out["(g)_nonzero_fixed_states"] = fixed[:5]
g_ok = not fixed
out["checks_ok"] = {"a": a_ok, "b": mismatch == 0, "c": c_ok, "d": d_ok, "e": out["(e)_ok"], "f": out["(f)_ok"], "g": g_ok}
out["PLANTED_condition_without_chi10_mismatches"] = planted_mismatch
out["PLANTED_caught"] = planted_mismatch > 0
out["all_claims_hold_and_plants_caught"] = bool(all(out["checks_ok"].values()) and out["PLANTED_caught"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1, default=str))
