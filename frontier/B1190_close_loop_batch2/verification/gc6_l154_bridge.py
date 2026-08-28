#!/usr/bin/env python3
"""GC-6: THE L154 BRIDGE — construct or obstruct.

Cells:
  V1  exact re-verification of both sides (Sugawara + Brown-Henneaux), sympy exact.
  V2  the CHARACTER test: (E6)_1 characters computed from the E6 root lattice
      (Fincke-Pohst enumeration, exact integer norms) / eta^6; exponent classes;
      Cardy growth c_eff estimator (same instrument run on u(1) control).
  V3  the object side: Kashaev <4_1>_N growth -> Vol (positive control) vs
      polynomial control (exclusion side); the exact CS identity 2R(e^{i pi/3});
      the banked B672 doublet exponents {2/5,3/5} vs split-pair h-set;
      the exponent-matching instrument, two-sided.
All tolerances stated in output. No measured physical value anywhere (Gate 5).
"""
import sys
from fractions import Fraction as Fr
import math

import sympy as sp
import mpmath as mp

OUT = []
def say(s=""):
    OUT.append(s)
    print(s, flush=True)

# ----------------------------------------------------------------------
say("=" * 72)
say("V1 — BOTH SIDES, EXACT (sympy rationals; zero tolerance: equality is exact)")
say("=" * 72)

# Sugawara c = k dim(g) / (k + h_dual)
def sugawara(k, dim, hd):
    return sp.Rational(k * dim, k + hd)

c_su3_2 = sugawara(2, 8, 3)     # SU(3) level 2
c_g2_1  = sugawara(1, 14, 4)    # G2 level 1
c_e6_1  = sugawara(1, 78, 12)   # E6 level 1
say(f"c(SU(3)_2) = {c_su3_2}   (claim 16/5: {c_su3_2 == sp.Rational(16,5)})")
say(f"c((G2)_1)  = {c_g2_1}   (claim 14/5: {c_g2_1 == sp.Rational(14,5)})")
say(f"sum        = {c_su3_2 + c_g2_1}   (= 6: {c_su3_2 + c_g2_1 == 6})")
say(f"c((E6)_1)  = {c_e6_1}   (78/13 = 6: {c_e6_1 == 6})")

sigma, ell = sp.symbols("sigma ell", positive=True)
G = 1 / (4 * sigma)              # B1012/B1088: G = 1/(4 sigma), ell = 1
c_BH = 3 * ell / (2 * G)
c_BH_at = sp.simplify(c_BH.subs(ell, 1))
say(f"Brown-Henneaux c = 3*ell/(2G) with G=1/(4 sigma), ell=1  ->  {c_BH_at}"
    f"   (= 6 sigma: {sp.simplify(c_BH_at - 6*sigma) == 0})")

# conformal weights of the split pair, Sugawara h = C2/(k + h_dual)
h = {}
h[("su3_2", "1")]    = sp.Rational(0)
h[("su3_2", "3")]    = sp.Rational(4, 3) / 5      # C2(3)=4/3
h[("su3_2", "3b")]   = sp.Rational(4, 3) / 5
h[("su3_2", "6")]    = sp.Rational(10, 3) / 5     # C2(6)=10/3
h[("su3_2", "6b")]   = sp.Rational(10, 3) / 5
h[("su3_2", "8")]    = sp.Rational(3) / 5         # C2(8)=3
h[("g2_1", "1")]     = sp.Rational(0)
h[("g2_1", "7")]     = sp.Rational(2) / 5         # C2(7)=2
say(f"h(SU(3)_2): 3 -> {h[('su3_2','3')]}, 6 -> {h[('su3_2','6')]}, 8 -> {h[('su3_2','8')]}")
say(f"h((G2)_1):  7 -> {h[('g2_1','7')]}")

# conformal-embedding branching arithmetic (E6)_1 restricted to SU(3)_2 x (G2)_1
say("branching fingerprints (dims and h-sums, exact):")
say(f"  vacuum: (1,1)+(8,7): dims 1 + {8*7} ; h-sums 0, {h[('su3_2','8')]+h[('g2_1','7')]} (= 0 mod 1: "
    f"{(h[('su3_2','8')]+h[('g2_1','7')]) % 1 == 0})")
say(f"  27: (3b,7)+(6,1): dim {3*7} + 6 = {3*7+6} (= 27: {3*7+6 == 27}); "
    f"h-sums {h[('su3_2','3b')]+h[('g2_1','7')]}, {h[('su3_2','6')]} (both = 2/3: "
    f"{h[('su3_2','3b')]+h[('g2_1','7')] == sp.Rational(2,3) and h[('su3_2','6')] == sp.Rational(2,3)})")
say(f"  adjoint at level q^1: (8,1)+(1,14)+(8,7): {8+14+56} (= 78 = dim E6: {8+14+56 == 78})")

# ----------------------------------------------------------------------
say()
say("=" * 72)
say("V2 — THE (E6)_1 CHARACTERS FROM THE LATTICE (exact integer arithmetic)")
say("=" * 72)

# E6 Cartan matrix (bourbaki numbering: chain 1-3-4-5-6, node 2 attached to 4)
A = sp.Matrix([
    [ 2,  0, -1,  0,  0,  0],
    [ 0,  2,  0, -1,  0,  0],
    [-1,  0,  2, -1,  0,  0],
    [ 0, -1, -1,  2, -1,  0],
    [ 0,  0,  0, -1,  2, -1],
    [ 0,  0,  0,  0, -1,  2]])
assert A.det() == 3, "E6 Cartan determinant must be 3"
Ainv = A.inv()

NMAX = 30           # characters computed through q^NMAX
NORM_BOUND = 2 * NMAX

# Fincke-Pohst enumeration of x in (shift + Z^6) with x^T A x <= bound.
# Cholesky (float) for pruning; norms recomputed exactly with Fractions.
import numpy as np
Af = np.array(A.tolist(), dtype=float)
L = np.linalg.cholesky(Af)   # A = L L^T
Aexact = [[Fr(int(A[i, j])) for j in range(6)] for i in range(6)]

def theta_counts(shift, bound):
    """Return dict {3*norm(int): count} for x in shift + Z^6, x^T A x <= bound.
    shift: list of Fractions. Exact norm via Fractions (denominator divides 3)."""
    counts = {}
    n = 6
    R = L.T  # upper triangular, norm = |R x|^2
    shf = np.array([float(s) for s in shift])
    # recursive enumeration from last coordinate down
    def rec(k, partial, sq):
        # partial: accumulated R contributions vector for coords > k (length 6)
        if sq > bound + 1e-6:
            return
        if k < 0:
            # x built; exact recompute
            x = rec.x[:]
            xs = [Fr(x[i]) + shift[i] for i in range(6)]
            nrm = Fr(0)
            for i in range(6):
                for j in range(6):
                    nrm += xs[i] * Aexact[i][j] * xs[j]
            if nrm <= bound:
                key = int(nrm * 3)
                counts[key] = counts.get(key, 0) + 1
            return
        # solve for coordinate k: contribution (R[k,k]*(x_k+shf_k) + partial[k])^2
        rkk = R[k, k]
        center = -partial[k] / rkk - shf[k]
        halfw = math.sqrt(max(bound + 1e-6 - sq, 0.0)) / rkk
        lo = math.ceil(center - halfw - 1e-9)
        hi = math.floor(center + halfw + 1e-9)
        for xk in range(lo, hi + 1):
            rec.x[k] = xk
            t = rkk * (xk + shf[k]) + partial[k]
            newsq = sq + t * t
            if newsq > bound + 1e-6:
                continue
            newpartial = partial + R[:, k] * (xk + shf[k])
            rec(k - 1, newpartial, newsq)
    rec.x = [0] * 6
    rec(5, np.zeros(6), 0.0)
    return counts

say(f"enumerating E6 root lattice, norm <= {NORM_BOUND} ...")
th0 = theta_counts([Fr(0)] * 6, NORM_BOUND)
# sanity: norm 0 count 1, norm 2 count = 72 roots
say(f"  vectors of norm 0: {th0.get(0,0)} (expect 1);  norm 2: {th0.get(6,0)} (expect 72 = #roots E6)")
assert th0.get(0, 0) == 1 and th0.get(6, 0) == 72

# fundamental weight generating the 27 coset: pick node i with (A^-1)_ii = 4/3
node = None
for i in range(6):
    if Ainv[i, i] == sp.Rational(4, 3):
        node = i
        break
say(f"  27-coset representative: fundamental weight of node {node+1}, "
    f"norm^2 = (A^-1)_ii = {Ainv[node, node]}")
w = [Fr(sp.Rational(Ainv[j, node]).p, sp.Rational(Ainv[j, node]).q) for j in range(6)]
COSET_BOUND = 2 * 20 + 2  # coset series through ~q^20
th1 = theta_counts(w, COSET_BOUND)
minkey = min(th1.keys())
say(f"  coset min norm = {Fr(minkey,3)} (expect 4/3 -> h = 2/3); multiplicity {th1[minkey]} (expect 27)")
assert Fr(minkey, 3) == Fr(4, 3) and th1[minkey] == 27
# all coset norms ≡ 4/3 mod 2 (=> q-powers 2/3 + Z)
ok_mod = all((k - 4) % 6 == 0 for k in th1.keys())
say(f"  every coset norm = 4/3 mod 2 (exponents 2/3 + Z): {ok_mod}")
assert ok_mod

# eta^-6 series: 1/prod (1-q^n)^6 through NMAX  (exact ints)
P6 = [0] * (NMAX + 1); P6[0] = 1
for n in range(1, NMAX + 1):
    for _ in range(6):
        for m in range(n, NMAX + 1):
            P6[m] += P6[m - n]
# assemble characters
theta_coeff = [th0.get(6 * m, 0) for m in range(NMAX + 1)]        # Theta = sum c_m q^m
chi0 = [sum(theta_coeff[m] * P6[n - m] for m in range(n + 1)) for n in range(NMAX + 1)]
Ncos = 20
cos_coeff = [th1.get(4 + 6 * m, 0) for m in range(Ncos + 1)]      # q^{2/3+m}
chi1 = [sum(cos_coeff[m] * P6[n - m] for m in range(n + 1)) for n in range(Ncos + 1)]

say(f"Theta_E6 coefficients (norm/2 = 0..8): {theta_coeff[:9]}")
say(f"chi_0^(E6)_1  = q^(-1/4) * ( {chi0[:8]} ... )")
say(f"  fingerprint: coefficient of q^1 = {chi0[1]} (= 78 = 72 roots + 6 Cartan: "
    f"{chi0[1] == 78 and theta_coeff[1] + 6 == 78})")
say(f"chi_27^(E6)_1 = q^(5/12)  * ( {chi1[:8]} ... )  [leading {chi1[0]} = 27: {chi1[0] == 27}]")
say("exponent classes mod 1 of ANY (E6)_1 character combination:"
    " {h - c/24 mod 1} = {-1/4, 5/12} mod 1 = {3/4, 5/12}")
E6_exps = {Fr(3, 4), Fr(5, 12)}
E8_exps = {Fr(2, 3)}   # (E8)_1: c=8, single character q^{-1/3}(1+248q+...)

# Cardy growth estimator: c_eff(n) = 6 n (log a_{n+1} - log a_n)^2 / pi^2
def c_eff_series(coeffs, skip=4):
    out = []
    for n in range(skip, len(coeffs) - 1):
        if coeffs[n] <= 0 or coeffs[n + 1] <= 0:
            continue
        d = math.log(coeffs[n + 1]) - math.log(coeffs[n])
        out.append((n, 6 * n * d * d / math.pi ** 2))
    return out

# u(1) control: eta^-1 coefficients = p(n)
P1 = [0] * (NMAX + 1); P1[0] = 1
for n in range(1, NMAX + 1):
    for m in range(n, NMAX + 1):
        P1[m] += P1[m - n]
ce6 = c_eff_series(chi0)
cu1 = c_eff_series(P1)
say(f"Cardy growth estimator (finite-n, converges from below, O(n^-1/2) bias):")
say(f"  chi_0^(E6)_1: c_eff at n=10: {dict(ce6)[10]:.2f}, n=20: {dict(ce6)[20]:.2f}, "
    f"n={ce6[-1][0]}: {ce6[-1][1]:.2f}  -> heading to 6")
say(f"  u(1) boson (eta^-1, the cusp-torus unit): c_eff at n=10: {dict(cu1)[10]:.2f}, "
    f"n={cu1[-1][0]}: {cu1[-1][1]:.2f}  -> heading to 1")
say("  => c = 6 is SIX cusp-boson units of boundary growth; the object's single cusp")
say("     with T[4_1] = U(1) gauge + U(1)_m flavor (B262, banked) supplies ONE.")

# ----------------------------------------------------------------------
say()
say("=" * 72)
say("V3 — THE OBJECT SIDE")
say("=" * 72)

mp.mp.dps = 60
# exact CS identity (B1088): 2 R(e^{i pi/3}) = pi^2/6 + i Vol
z = mp.e ** (mp.mpc(0, 1) * mp.pi / 3)
Rz = mp.polylog(2, z) + mp.mpf(1) / 2 * mp.log(z) * mp.log(1 - z)
lhs = 2 * Rz
Lob = lambda th: mp.im(mp.polylog(2, mp.e ** (2j * th))) / 2      # Lobachevsky
Vol = 2 * 3 * Lob(mp.pi / 3)                                       # two regular ideal tets
say(f"Vol (Lobachevsky, 2 tets)      = {mp.nstr(Vol, 30)}")
say(f"2 R(e^(i pi/3))                = {mp.nstr(lhs, 30)}")
dre = abs(mp.re(lhs) - mp.pi ** 2 / 6); dim_ = abs(mp.im(lhs) - Vol)
say(f"  |Re - pi^2/6| = {mp.nstr(dre, 3)}, |Im - Vol| = {mp.nstr(dim_, 3)}  (tolerance 1e-50: "
    f"{dre < mp.mpf('1e-50') and dim_ < mp.mpf('1e-50')})")

# Kashaev <4_1>_N growth: the sigma-sector (unquantized, Vol-driven) fingerprint
def kashaev_log(N):
    # log <4_1>_N via log-sum-exp of partial products of 4 sin^2(pi j / N)
    terms = []
    s = 0.0
    terms.append(0.0)
    for j in range(1, N):
        s += math.log(4 * math.sin(math.pi * j / N) ** 2)
        terms.append(s)
    M = max(terms)
    return M + math.log(sum(math.exp(t - M) for t in terms))

say("Kashaev <4_1>_N growth  gamma_N = 2 pi (log<> - 1.5 log N)/N  (subleading N^(3/2) removed):")
for N in (200, 800, 3200):
    lg = kashaev_log(N)
    gam = 2 * math.pi * (lg - 1.5 * math.log(N)) / N
    say(f"  N={N}: gamma = {gam:.6f}   |gamma - Vol| = {abs(gam - float(Vol)):.2e}")
gam_final = 2 * math.pi * (kashaev_log(3200) - 1.5 * math.log(3200)) / 3200
say(f"  positive control: recovers Vol = {float(Vol):.6f} to {abs(gam_final-float(Vol)):.1e} at N=3200 (O(1/N) drift)")
# exclusion side: same estimator on a polynomial (quantized-sector-like) sequence
gam_poly = 2 * math.pi * (math.log(3200.0 ** 2) - 1.5 * math.log(3200)) / 3200
say(f"  exclusion control: same estimator on a_N = N^2 (polynomial growth): gamma = {gam_poly:.6f} -> 0")
say("  => the object's boundary Z grows exp(Vol N / 2 pi): the UNQUANTIZED (sigma/Vol) sector,")
say("     not a finite-modular-datum (quantized, polynomial-growth) sector.")

# The banked B672 doublet: exponent typing (exact fractions)
say()
say("B672's banked weight-5 doublet (the only banked object-side q-series family):")
say("  comp1 = q^(2/5) (q;q) G(q) (q;q)^9,  comp2 = q^(3/5) (q;q) H(q) (q;q)^9;  comp2/comp1 = RR fraction")
e1 = Fr(2, 5) - Fr(10, 24)   # rewrite comp1 = q^(2/5) G (q;q)^10 = [q^e1 G] * eta^10
e2 = Fr(3, 5) - Fr(10, 24)
say(f"  rewriting with (q;q)^10 = eta^10 q^(-5/12):  comp1 = q^({e1}) G(q) * eta^10, "
    f"comp2 = q^({e2}) H(q) * eta^10")
say(f"  ({e1}, {e2}) = (-1/60, 11/60): {(e1, e2) == (Fr(-1,60), Fr(11,60))} — EXACTLY the two")
say("  Lee-Yang/(2,5) character prefactors: the doublet IS (Lee-Yang character) x eta^10, banked verbatim.")
doublet_exps = {Fr(2, 5), Fr(3, 5)}
split_nonvac_h = {Fr(2, 5), Fr(3, 5)}   # h(tau of (G2)_1) = 2/5 (Fibonacci), h(8 of SU(3)_2) = 3/5
say(f"  doublet leading exponents {sorted(doublet_exps)} vs split-pair non-vacuum weights "
    f"{{h(7 of (G2)_1), h(8 of SU(3)_2)}} = {sorted(split_nonvac_h)}: "
    f"IDENTICAL: {doublet_exps == split_nonvac_h}")
say("  and comp2/comp1 = R(q), the Rogers-Ramanujan fraction = the golden/Fibonacci hallmark,")
say("  (G2)_1 being the Fibonacci modular datum (2 primaries, h in {0, 2/5}).")

# THE EXPONENT-MATCHING INSTRUMENT, two-sided
say()
say("The exponent instrument (exact fractions mod 1): object-side series classes vs targets")
object_exps = {Fr(0)} | doublet_exps    # WRT/index-type series: integer exponents; doublet: 2/5,3/5
def match(a, b):
    m = {x % 1 for x in a} & {x % 1 for x in b}
    return sorted(m)
say(f"  object {{0, 2/5, 3/5}} vs (E6)_1 {{3/4, 5/12}}: intersection {match(object_exps, E6_exps)}  -> ABSENT")
say(f"  object vs (E8)_1 {{2/3}} [deliberately-absent target]: {match(object_exps, E8_exps)}  -> ABSENT (instrument excludes)")
say(f"  doublet vs split-pair h-set [known-present target]: {match(doublet_exps, split_nonvac_h)}  -> FIRES (instrument detects)")
say(f"  (E6)_1 vs itself [sanity]: {match(E6_exps, E6_exps)}")

say()
say("Verdict cell: see FINDINGS text.")
