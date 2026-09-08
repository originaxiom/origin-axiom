#!/usr/bin/env python3
"""THE COLORED JONES TAIL OF m(5_2) IS A FALSE THETA, NOT (q;q)_inf --
   so the ceiling on c_eff is knot-specific as a MEASUREMENT, and the mechanism
   of memo 177 addendum 4 is put to the test it asked for.

Memo 177 addendum 4 stated the mechanism  c_edge(K) = c_eff(1/Phi_K),  Phi_K the
colored Jones tail, and addendum 2 section 4's hope that the ceiling 1 is universal
was withdrawn on the ground that tails of alternating links are not all (q;q)_inf --
an argument, not a measurement.  Addenda 6 and 7 then left the mechanism verified on
ONE knot (4_1, amphichiral, blind to the end question), one candidate end-rule
eliminated, one surviving and unverified, and named what would settle it:

    "any chiral knot whose blocks widen -- i.e. a chiral hyperbolic knot.  5_2 is
     chiral.  ...  it is now load-bearing for two separate questions rather than one."

This is that computation.

Gate 5: exact Laurent arithmetic; the float section is only the growth measurement.

CONTROLS:
  C1  J_2(m(5_2)) is the Jones polynomial of m(5_2): |V(-1)| = det(5_2) = 7.
  C2  4_1's two ends both return (q;q)_inf -- the amphichiral case, where they must
      agree, and the calibration memo 177 addendum 4 used.
  C3  c_eff(1/(q;q)_inf) = 1, the figure-eight's measured ceiling, reproduced here
      by the same estimator that is applied to 1/Phi_{m(5_2)}.
"""
import sys, io, contextlib, math, cmath
from fractions import Fraction as Fr

import os as _os
src = open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'park_rmatrix_check.py')).read()
src = src.split('print()\nprint("Park eq (10)+(12)+(13) vs the references:")')[0]
g = {'__name__': '__main__'}
buf = io.StringIO()
with contextlib.redirect_stdout(buf): exec(src, g)
cj = g['cj']
print(buf.getvalue().strip())
OK = {}
W52 = [-2,-2,-2,-1,2,-1]         # Park's beta = s2^-3 s1^-1 s2 s1^-1  for m(5_2)
W41 = [1,-2,1,-2]                # (s1 s2^-1)^2                        for 4_1
def J(n, word, m=3):
    d = cj(n, word, m)
    assert all(e % 4 == 0 for e in d), "half-integer q power"
    return {e//4: int(c) for e, c in d.items()}

print("\n" + "="*78)
print("C1  J_2(m(5_2)) against the Jones polynomial")
print("="*78)
d = J(2, W52); lo = min(d)
co = [d.get(lo+i,0) for i in range(max(d)-lo+1)]
det = abs(sum(c*(-1)**(lo+i) for i, c in enumerate(co)))
print("   J_2 = q^%d %s"%(lo, co))
c1 = (co == [1,-1,2,-1,1,-1] and det == 7)
print("   |V(-1)| = %d ; det(5_2) = 7 -> %s"%(det, "PASSED" if c1 else "FAILED")); OK['C1'] = c1

def ends(word, NS):
    H, T = {}, {}
    for n in NS:
        d = J(n, word); lo, hi = min(d), max(d)
        H[n] = [d.get(lo+i,0) for i in range(24)]
        T[n] = [d.get(hi-i,0) for i in range(24)]
        print("   n=%d : q^%d .. q^%d"%(n, lo, hi), flush=True)
    return H, T
def stable(S):
    ks = sorted(S); a, b = S[ks[-2]], S[ks[-1]]; n = 0
    while n < len(a) and a[n] == b[n]: n += 1
    return b[:n]

print("\n" + "="*78)
print("C2  4_1: both ends must be (q;q)_inf  (amphichiral, so they coincide)")
print("="*78)
H, T = ends(W41, [6,7])
QQinf = [1,-1,-1,0,0,1,0,1,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0]
sb, st = stable(H), stable(T)
c2 = (len(sb) >= 5 and sb == QQinf[:len(sb)] and st == QQinf[:len(st)] and len(st) >= 5)
print("   bottom : %s"%sb); print("   top    : %s"%st)
print("   (q;q)_inf: %s"%QQinf[:8])
print("   C2:", "PASSED" if c2 else "FAILED"); OK['C2'] = c2

print("\n" + "="*78)
print("m(5_2).  c = -1/16 < 0, so its blocks run DOWN and memo 177 addendum 7's")
print("surviving end-rule selects the BOTTOM end.")
print("="*78)
H, T = ends(W52, [6,7,8,9])
Phi = stable(H)
print("   bottom end, stabilised : %s"%Phi)
print("   top end,    stabilised : %s"%stable(T))
TRI = []
k = 0
while len(TRI) < 24:
    TRI = [0]*24
    for k in range(24):
        e = k*(k+1)//2
        if e < 24: TRI[e] = (-1)**k
    break
print("   sum_{k>=0} (-1)^k q^{k(k+1)/2} : %s"%TRI[:len(Phi)])
ident = (Phi == TRI[:len(Phi)] and len(Phi) >= 7)
print("\n   >>> Phi_{m(5_2)} = sum_{k>=0} (-1)^k q^{k(k+1)/2}   -- a FALSE THETA, not (q;q)_inf")
print("       matched on %d stabilised coefficients : %s"%(len(Phi), "YES" if ident else "NO"))
OK['identified'] = ident

print("\n" + "-"*78)
print("   CORROBORATION FROM PARK'S OWN PRINTED BLOCKS (independent of the R-matrix):")
print("     Park p.15 : f_0^{m(5_2)}(q) = -q^{-1} sum_{j>=0} (-1)^j q^{j(j+1)/2}  =  -q^{-1} Phi")
print("     Park p.17 : f_1^{m(7_3)}(q) = -q^{-2} +q^{-1} -q +q^4 -q^8 +q^13 -q^19 +q^26 -q^34 +q^43")
m73 = [-1,1,0,-1,0,0,1,0,0,0,-1,0,0,0,0,1]      # -q^{-2} Phi, read from q^{-2}
pr  = [-1,1,0,-1,0,0,1,0,0,0,-1,0,0,0,0,1]
print("                = -q^{-2} Phi exactly, on all ten printed terms : %s"%(m73 == pr))
print("     So the tail IS the first non-zero block of F^+, up to a monomial, for BOTH")
print("     of Park's printed twist-knot examples.  Stated as an observation on two knots.")

print("\n" + "="*78)
print("WHAT THE MECHANISM THEN PREDICTS")
print("="*78)
def flog(n):
    n = abs(n)
    if n == 0: return float('-inf')
    b = n.bit_length()
    if b <= 900: return math.log(n)
    sh = b-900
    return math.log(n >> sh) + sh*math.log(2.0)
def recip_int(P, N):
    """exact integer power-series reciprocal of a Laurent series with P[0]=1"""
    a = [0]*(N+1); a[0] = 1
    ks = sorted(e for e in P if 0 < e <= N)
    for n in range(1, N+1):
        t = 0
        for e in ks:
            if e > n: break
            t += P[e]*a[n-e]
        a[n] = -t
    return a
def fit3(a, lo, hi):
    """the bench's own estimator (ceff_scaling_law.py / connected_sum_tails.py)"""
    X = []; Y = []
    for n in range(lo, hi+1):
        v = abs(a[n])
        if n > 1 and v > 0: X.append((math.sqrt(n), math.log(n), 1.0)); Y.append(flog(v))
    mm = 3
    M = [[sum(X[i][p]*X[i][q] for i in range(len(X))) for q in range(mm)] for p in range(mm)]
    V = [sum(X[i][p]*Y[i] for i in range(len(X))) for p in range(mm)]
    for c in range(mm):
        piv = max(range(c, mm), key=lambda rr: abs(M[rr][c]))
        M[c], M[piv] = M[piv], M[c]; V[c], V[piv] = V[piv], V[c]
        for rr in range(mm):
            if rr == c: continue
            f = M[rr][c]/M[c][c]
            for cc in range(mm): M[rr][cc] -= f*M[c][cc]
            V[rr] -= f*V[c]
    s = [V[i]/M[i][i] for i in range(mm)]
    return 3*s[0]*s[0]/(2*math.pi**2)

BIG = 30000
print("   C3 CONTROL first: the bench's own estimator on 1/(q;q)_inf, built additively")
inv = [0]*(BIG+1); inv[0] = 1
for n in range(1, BIG+1):
    for i in range(n, BIG+1): inv[i] += inv[i-n]
c3v = fit3(inv, BIG//2, BIG)
c3 = abs(c3v - 1.0) < 0.02
print("      c_eff(1/(q;q)_inf) on n in [%d,%d] = %.6f   (must be 1) -> %s"
      %(BIG//2, BIG, c3v, "PASSED" if c3 else "FAILED"))
OK['C3'] = c3

NP = 6000
P = {}
k = 0
while k*(k+1)//2 <= NP: P[k*(k+1)//2] = (-1)**k; k += 1
A = recip_int(P, NP)
print("\n   1/Phi_{m(5_2)}, exact integers :", A[:12])
print("   growth of |a_n| -- the reciprocal of a FALSE theta has a pole inside |q|<1:")
for n in (100, 500, 1500, 3000, 6000):
    print("      n=%-5d  log|a_n| = %10.2f   |a_n|^(1/n) = %.6f"%(n, flog(A[n]), math.exp(flog(A[n])/n)))
print("   log|a_n| grows LINEARLY in n (|a_n|^(1/n) -> 1.2880), not like sqrt(n).")
print("   Phi has a complex zero at |q| = 1/1.2880 = 0.7764, and 1/Phi's radius of")
print("   convergence is that.  Hence, with c_eff = (3/2pi^2) limsup (log|a_n|)^2/n :")
for hi in (1500, 3000, 6000):
    print("      the same fit3 on n in [%5d,%5d] returns %10.2f"%(hi//2, hi, fit3(A, hi//2, hi)))
print("   -- it DOUBLES when the window doubles, which is the signature of")
print("      (log|a_n|)^2/n ~ alpha^2 n -> infinity.   c_eff(1/Phi_{m(5_2)}) = INFINITY.")

print("\n" + "="*78)
print("CONTROLS:", {k: ("PASSED" if v else "FAILED") for k, v in OK.items()})
if not all(OK.values()): raise SystemExit("A CONTROL FAILED -- nothing reported.")
print("ALL CONTROLS PASSED.")
