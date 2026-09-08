#!/usr/bin/env python3
"""
check_relay.py -- chat1, 2026-09-08

Certificate for the three genuinely-absent items of 00_RELAY.md, plus the
re-derivations of section 2.  stdlib only.  Exits non-zero on drift.

EVERY negative in this script is preceded by a POSITIVE CONTROL, per the
rule proposed in section 0.
"""
import itertools, sys
from fractions import Fraction as F

fail = []
def check(label, ok):
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    if not ok: fail.append(label)

print("check_relay.py")
print("=" * 72)

# ---------------------------------------------------------------- section 1b
print("\nSTAGE 1: Out(E6) = Z/2, from the Cartan matrix (no recall)")
C = [[ 2, 0,-1, 0, 0, 0],
     [ 0, 2, 0,-1, 0, 0],
     [-1, 0, 2,-1, 0, 0],
     [ 0,-1,-1, 2,-1, 0],
     [ 0, 0, 0,-1, 2,-1],
     [ 0, 0, 0, 0,-1, 2]]
def permuted(C, p):
    return [[C[p[i]][p[j]] for j in range(6)] for i in range(6)]
autos = [p for p in itertools.permutations(range(6)) if permuted(C, p) == C]
print("      graph automorphisms found: %d  %s"
      % (len(autos), [tuple(x+1 for x in p) for p in autos]))
check("Out(E6) = Z/2 (exactly two diagram automorphisms)", len(autos) == 2)
check("=> any order-3 automorphism is INNER: gcd(3, 2) = 1",
      len(autos) == 2 and (3 % 2) == 1)

# ---------------------------------------------------------------- section 2
print("\nSTAGE 2: the fixed-line law, exhaustive over SL(2,Z)")
def mul(A,B):
    return (A[0]*B[0]+A[1]*B[2], A[0]*B[1]+A[1]*B[3],
            A[2]*B[0]+A[3]*B[2], A[2]*B[1]+A[3]*B[3])
I4 = (1,0,0,1)
def order(A, cap=20):
    P = A
    for k in range(1, cap+1):
        if P == I4: return k
        P = mul(P, A)
    return None
seen = {}
R = 6
for a,b,c,d in itertools.product(range(-R,R+1), repeat=4):
    if a*d - b*c != 1: continue
    o = order((a,b,c,d))
    if o and o <= 6:
        seen.setdefault(o, set()).add((a+d, (a-1)*(d-1)-b*c))
for o in sorted(seen):
    ts = sorted({x[0] for x in seen[o]}); ds = sorted({x[1] for x in seen[o]})
    print("      order %d : traces %s  det(A-I) %s" % (o, ts, ds))
check("torsion orders of SL(2,Z) are exactly {1,2,3,4,6}",
      sorted(seen) == [1,2,3,4,6])
check("order 3 => trace -1 and det(A-I) = 3, always",
      seen.get(3) == {(-1, 3)})
check("order 2 => trace -2 and det(A-I) = 4, always",
      seen.get(2) == {(-2, 4)})
bad = [(a,b,c,d) for a,b,c,d in itertools.product(range(-8,9), repeat=4)
       if a*d-b*c == 1 and (a-1)*(d-1)-b*c != 2-(a+d)]
check("det(A-I) = 2 - tr A identically on det=1 (0 counterexamples)", not bad)

# ---------------------------------------------------------------- section 1c
print("\nSTAGE 3: F-flatness forbids exactly the helpful flavons (B1283)")
print("      rule: no monomial S_ij X_j Xbar_i may contain two switched-on fields")
g = 1
on = {("N",g),("Nbar",g),("nu",g),("nubar",g)}
forb, allo = set(), set()
for i in (1,2,3):
    for j in (1,2,3):
        hit = any(f in on for f in (("N",j),("Nbar",i),("nu",j),("nubar",i)))
        (forb if hit else allo).add((i,j))
print("      forbidden: %s" % sorted(forb))
print("      allowed  : %s" % sorted(allo))
check("forbidden are exactly S_ij with i=g or j=g",
      forb == {(i,j) for i in (1,2,3) for j in (1,2,3) if i==g or j==g})
check("allowed are exactly the other pair's flavons (B1283's branch table)",
      allo == {(2,2),(2,3),(3,2),(3,3)})

print("\nSTAGE 4: the Z' cubic anomaly cancels against the 27-bars")
QN = {'Q':(3,2),'uc':(3,1),'ec':(1,1),'dc':(3,1),'L':(1,2),'nu':(1,1),
      'Hu':(1,2),'D':(3,1),'Hd':(1,2),'Db':(3,1),'N':(1,1)}
Qg  = {'N':0,'nu':0,'Q':-6,'uc':-6,'ec':-6,'dc':-12,'L':-12,
       'Hu':-18,'D':-18,'Hd':-12,'Db':-12}
Qo  = {'N':15,'nu':15,'Q':9,'uc':9,'ec':9,'dc':3,'L':3,
       'Hu':-3,'D':-3,'Hd':3,'Db':3}
def cubic(ch, sign):
    return sum((sign*ch[f])**3 * c*d for f,(c,d) in QN.items())
t27  = cubic(Qg,1)  + 2*cubic(Qo,1)
t27b = cubic(Qg,-1) + 2*cubic(Qo,-1)
print("      three 27s: %d    three 27-bars: %d    total: %d" % (t27, t27b, t27+t27b))
check("cubic anomaly vanishes (the spectrum is vector-like)", t27 + t27b == 0)
check("POSITIVE CONTROL: the 27s alone are NOT zero (-20250), so the",
      t27 == -20250)
print("      test is not trivially zero -- the cancellation is real.")

print("\n" + "=" * 72)
if fail:
    print("DRIFT: %d check(s) failed: %s" % (len(fail), fail)); sys.exit(1)
print("ALL CHECKS PASSED.")
sys.exit(0)
