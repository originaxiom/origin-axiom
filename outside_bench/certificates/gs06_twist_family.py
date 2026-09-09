#!/usr/bin/env python3
"""GAROUFALIDIS-SUN's C-POLYNOMIAL FOR EVERY TWIST KNOT, IMPLEMENTED AND CONTROLLED
AGAINST FIVE KNOTS' WORTH OF THIS BENCH'S OWN DATA -- which takes memo 190's route from
one knot to the whole family.

Memo 190 broke memo 183 addendum 4's blocker for m(5_2) using the ONE quantum C-polynomial
Park prints.  Park's own words for why that is the bottleneck: "Since explicit expressions
for the quantum C-polynomials for twist knots are given in [GS06], we will use them".

[GS06] = S. Garoufalidis and X. Sun, "The C-polynomial of a knot", Algebr. Geom. Topol. 6
(2006) 1623-1653 (arXiv math/0504305), supplied by the owner 2026-09-09.  Its Definition
1.3 gives Chat_{K_p} in CLOSED FORM for every integer p:

    C_p(E,Q,q) = E^{|p|} + sum_{i=0}^{|p|-1} a_p(Q,i) E^i

with a_p(Q,i) the explicit q-binomial expression of its equation (5).  Implemented here
verbatim.

THE OPERATOR CONVENTION, derived rather than assumed.  In a term a_p(Q,i) E^i acting on
sum_m a_m E^{-m}, the shift acts first and the Q-multiplication second, so that term sends
a_m to slot l = m - i with Q evaluated at q^l.  Hence the recursion is

    a_{l+|p|} + sum_{i=0}^{|p|-1} a_p(q^l, i) a_{l+i} = 0.

CONTROLS -- three against Park's PRINTED values, then five against our OWN computations.

  C1  p = +2 must reproduce Park's printed Chat_{5_2} = E^2 + (q^2+q^3)EQ + (q^6 - q^3 E)Q^2
      + (-q^7 + q^4 E)Q^3, normal-ordered.  This is the exact operator memo 190 ran on.
  C2  p = +1 must give a_m(3_1^l) = (-1)^m q^{m(m+3)/2}, which Park prints.
  C3  p = -1 must give a_m(4_1) = 1 for all m, which Park prints.
  C4  THE ONE THAT COSTS SOMETHING: the recursion must ANNIHILATE the Habiro coefficients
      this bench computed itself, for every knot it holds them for --
        3_1 (p=+1), 4_1 (p=-1), 6_1 (p=-2), 9_2 (p=+4)   from the Garoufalidis-Sun colored
          Jones tables, extracted in memo 185 addendum 2 (data/cyclotomic_twist.json), and
        5_2 (p=+2)                                        from this bench's own R-matrix
          state sum on Park's braid word, memo 185 addendum 3 (data/cyclotomic_52.json).
      Conversion between bases is fixed, not fitted:  a_m = (-1)^m q^{m(m+1)/2} C_m.

Gate 5: exact symbolic arithmetic over Q(q,Q).  No measured value.
"""
import os, json
import sympy as sp
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
q, Q = sp.symbols('q Q')

def qbin(k, l):
    if l < 0 or k < 0 or l > k: return sp.Integer(0)
    num = den = sp.Integer(1)
    for t in range(1, l+1):
        num *= (1 - q**(k-l+t)); den *= (1 - q**t)
    return sp.cancel(sp.expand(sp.simplify(num/den)))
def poch_ratio(top, bot):
    """(q;q)_{n+top} / (q;q)_{n+bot} with Q = q^n"""
    if top == bot: return sp.Integer(1)
    if top > bot:
        r = sp.Integer(1)
        for s in range(bot+1, top+1): r *= (1 - q**s*Q)
        return r
    r = sp.Integer(1)
    for s in range(top+1, bot+1): r *= (1 - q**s*Q)
    return 1/r
def a_p(p, i):
    """GS06 Definition 1.3, equation (5)"""
    if p == 0: return sp.Integer(0)
    if p > 0:
        pre = q**((p-i)*(p+1)) * Q**(p-i)
        R = poch_ratio(p-1, i)
        s1 = sum(q**((p+i+1)*j) * Q**(2*j) * qbin(p-j, p-i) * qbin(p-i+j-1, j)
                 for j in range(0, i+1))
        s2 = sum(q**((p+i+1)*j + p) * Q**(2*j+1) * qbin(p-j-1, p-i) * qbin(p-i+j-1, j)
                 for j in range(0, i))
        return sp.cancel(sp.expand(pre*R*(s1-s2)))
    pre = q**((p-i+1)*(-p)) * Q**(p-i+1)
    R = poch_ratio(-p-1, i)
    s1 = sum(q**((-p+i)*j) * Q**(2*j) * qbin(-p-j-1, i-j) * qbin(-p-i+j, j)
             for j in range(0, i+1))
    s2 = sum(q**((-p+i)*j + (-p)) * Q**(2*j+1) * qbin(-p-j-2, i-j-1) * qbin(-p-i+j, j)
             for j in range(0, i))
    return sp.cancel(sp.expand(pre*R*(-s1+s2)))
def coeffs(p): return [sp.simplify(a_p(p, i)) for i in range(abs(p))]

OK = {}
print("=" * 78); print("C1  p = +2 against Park's PRINTED Chat_{5_2}"); print("=" * 78)
PARK2 = {0: q**6*Q**2 - q**7*Q**3, 1: q**3*Q + q**4*Q - q**5*Q**2 + q**7*Q**3}
c2 = coeffs(2)
c1ok = all(sp.simplify(sp.expand(c2[i] - PARK2[i])) == 0 for i in (0, 1))
for i in (0, 1):
    print("   a_2(Q,%d) = %s" % (i, sp.expand(c2[i])))
print("   identical to Park's printed operator :", c1ok)
OK["C1  GS06 p=+2 == Park's printed Chat_{5_2}"] = c1ok

print(); print("=" * 78); print("C2 / C3  the two knots Park prints a_m for in closed form")
print("=" * 78)
def a_seq(p, M, a0=None):
    """run the recursion forward from known low terms; returns a_0..a_M or None"""
    P = abs(p); C = coeffs(p)
    a = list(a0)
    for l in range(0, M - P + 1):
        nxt = -sum(C[i].subs(Q, q**l) * a[l+i] for i in range(P))
        a.append(sp.simplify(sp.expand(nxt)))
    return a
t = a_seq(1, 6, [sp.Integer(1)])
want = [sp.simplify((-1)**m * q**sp.Rational(m*(m+3), 2)) for m in range(7)]
c2ok = all(sp.simplify(t[m]-want[m]) == 0 for m in range(7))
print("   p=+1 (3_1^l) : %s" % [sp.factor(x) for x in t[:5]])
print("   Park prints  : (-1)^m q^{m(m+3)/2}  ->", c2ok)
OK["C2  p=+1 gives Park's a_m(3_1) = (-1)^m q^{m(m+3)/2}"] = c2ok
f = a_seq(-1, 6, [sp.Integer(1)])
c3ok = all(sp.simplify(x-1) == 0 for x in f)
print("   p=-1 (4_1)   : %s   Park prints a_m = 1  -> %s" % ([sp.factor(x) for x in f[:5]], c3ok))
OK["C3  p=-1 gives Park's a_m(4_1) = 1"] = c3ok

print(); print("=" * 78)
print("C4  the recursion must ANNIHILATE this bench's own Habiro coefficients")
print("=" * 78)
D = json.load(open(os.path.join(DATA, "cyclotomic_twist.json"))); D.pop("_provenance", None)
D52 = json.load(open(os.path.join(DATA, "cyclotomic_52.json")))
KN = {k: (v["p"], [dict((int(e), int(c)) for e, c in t) for t in v["C"]]) for k, v in D.items()}
KN["5_2"] = (2, [dict((int(e), int(c)) for e, c in t) for t in D52["5_2"]["C"]])
c4 = True
for name in sorted(KN, key=lambda z: KN[z][0]):
    p, C = KN[name]
    A = [sp.expand(sum(cc * q**e for e, cc in C[m].items()) * (-1)**m * q**sp.Rational(m*(m+1), 2))
         for m in range(len(C))]
    co = coeffs(p); P = abs(p); bad = []
    for l in range(0, len(A) - P):
        r = A[l+P] + sum(co[i].subs(Q, q**l) * A[l+i] for i in range(P))
        if sp.simplify(sp.expand(r)) != 0: bad.append(l)
    n = len(A) - P
    c4 &= (not bad and n > 0)
    print("   %-5s p = %-3d  relation holds at l = 0..%d  (%d checks) : %s"
          % (name, p, n-1, n, "ALL PASS" if not bad else "FAILS at l=%s" % bad[:3]))
OK["C4  GS06's recursion annihilates our own a_m for all five knots"] = c4

print(); print("=" * 78); print("CONTROLS"); print("=" * 78)
for k, v in OK.items(): print("   %-62s %s" % (k, "PASSED" if v else "FAILED"))
print("""
WHAT THIS UNLOCKS.  Memo 190 broke the f_6 blocker for m(5_2) using the single quantum
C-polynomial Park prints.  GS06 gives that operator in closed form for EVERY twist knot,
and it is now implemented and controlled -- three times against values Park prints, and
once, at five knots, against Habiro coefficients this bench computed for itself from two
independent sources (the Garoufalidis-Sun colored Jones tables, and our own R-matrix state
sum).  The route of memo 190 therefore runs on the whole family, not on one knot.

WHAT IS NOT CLAIMED.  Running it still needs, per knot, the boundary ansatz that fixes
a_{-1} -- Park solves that with a continued fraction for 5_2 and says "the same type of
ansatz seems to work for all twist knots", which is his expectation and is NOT tested here.
And Conjecture 2 remains a conjecture (memo 190 section 6).  What is established here is
the OPERATOR for every p, not the blocks for every p.""")
assert all(OK.values()), OK
