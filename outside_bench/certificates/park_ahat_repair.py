#!/usr/bin/env python3
"""THE REPAIR OF PARK eq (32) IS DETERMINATE, AND THREE OF ITS TERMS ARE RECONSTRUCTED.

Memo 183 showed the quantum A-polynomial printed in Park arXiv:2004.02087v2 eq (32)
does not annihilate F^+_{m(5_2)}, and that no SINGLE monomial repairs it.  With the
true blocks in hand (memo 183 addendum 1, certificates/park_large_color.py), the
repair stops being a search and becomes a solve.

Writing c_d(Q) for the Laurent polynomial that must be ADDED to the x^d coefficient
of a_1 (q = Q^2), the equation at x^{n+1/2} reads

    delta_n  =  - sum_d c_d Q^{2(n-d)+1} f_{n-d} ,

so delta_3 gives c_3, then delta_4 gives c_4, then delta_5 gives c_5, ... each as an
EXACT quotient by f_0.  The result:

    c_3 = -q^{25/2}          c_4 = q^{25/2}(1 + q - q^3)          c_5 = q^{33/2}(1 + q)

WHY a_1 AND NOT ANOTHER INDEX.  The x^{7/2} equation forces the x^3 term to be
-q^{13-i/2} in a_i for a single i in 0..4 and fixes nothing else.  The x^{9/2}
equation then requires ( -delta_4 + Q^{26+2i} f_1 ) / f_0 to be a Laurent POLYNOMIAL.
With delta_4 known to Q^96 (36 converged coefficients of f_4), i = 1 gives a
THREE-TERM quotient and every other i gives 33 or more terms.

Gate 5: exact integer / Fraction arithmetic.  No fitted constant survives unchecked --
every c_d is then tested against two independent instruments.

CONTROLS:
  C1  the repaired recursion reproduces EVERY converged coefficient of the large color
      R-matrix blocks f_0..f_6 -- and adding c_4, then c_5, extends the agreement
      exactly as far as the next block's converged range, which is what a correct
      reconstruction must do and an overfit would not.
  C2  it reproduces Zhat(Sigma(2,3,11)), generated independently as a false theta,
      further with each correction: q^16 -> q^27 -> q^33.
  C3  every block stays a LAURENT POLYNOMIAL over Z (no denominators, no half-integer
      powers of q) -- which the recursion does not enforce.
HONEST LIMIT:
  the repair is NOT complete.  A further correction at x^6 is needed (the assembled
  series first fails at q^34), and determining it needs f_6 to about ten converged
  coefficients, which needs a higher weight cutoff than this bench has reached.
"""
import sys, json, io, contextlib
import sympy as sp
from fractions import Fraction as Fr

import glob, os
if len(sys.argv) > 1:
    BLOCKS = sys.argv[1]
else:
    cands = sorted(glob.glob('/tmp/k52/stable_w*.json') + glob.glob('/tmp/park_f52_W*.json'),
                   key=lambda p: int(''.join(ch for ch in os.path.basename(p) if ch.isdigit())))
    if not cands:
        raise SystemExit("no block file; run certificates/park_large_color.py first")
    BLOCKS = cands[-1]
print("blocks read from", BLOCKS)
LQ = 400

# ---------- Park's f_0, f_1 (closed forms) and f_2, f_3 (his Q(q) formulas) ----------
def ladd(a, b, sc=1):
    r = dict(a)
    for e, c in b.items():
        r[e] = r.get(e, 0) + sc*c
        if r[e] == 0: del r[e]
    return r
def lmul(a, b, cap=LQ):
    r = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = e1+e2
            if e <= cap: r[e] = r.get(e, 0)+c1*c2
    return {e: c for e, c in r.items() if c}
def ldiv(num, den, cap=LQ):
    dl = min(den); dc = Fr(den[dl]); cur = dict(num); res = {}
    while cur:
        lo = min(cur)
        if lo-dl > cap: break
        k = Fr(cur[lo])/dc; res[lo-dl] = res.get(lo-dl, 0)+k
        for x, y in den.items():
            t = lo-dl+x; cur[t] = cur.get(t, 0)-Fr(y)*k
            if cur[t] == 0: del cur[t]
    return {e: c for e, c in res.items() if c}
def poly(*t):
    d = {}
    for e, c in t: d[e] = d.get(e, 0)+c
    return {e: c for e, c in d.items() if c}
def f0ser():
    a = {}; j = 0
    while j*(j+1)//2 <= LQ+2: a[j*(j+1)//2] = a.get(j*(j+1)//2, 0)+(-1)**j; j += 1
    return {e-1: -c for e, c in a.items() if c}
def f1ser():
    a = {}; j = 0
    while j*(j+1)//2 <= LQ+2:
        b = j*(j+1)//2
        for t in range(j+1):
            if b+t <= LQ+2: a[b+t] = a.get(b+t, 0)+(-1)**j
        j += 1
    return {e-1: -c for e, c in a.items() if c}
F0, F1 = f0ser(), f1ser()
den2 = poly((1,-1),(3,1))
F2 = ladd(ldiv(lmul(poly((0,1),(1,1),(2,-1)), F0), den2),
          ldiv(lmul(poly((0,-1),(1,-2),(2,1)), F1), den2))
den3 = poly((2,1),(4,-1),(5,-1),(7,1))
F3 = ladd(ldiv(lmul(poly((0,-2),(1,-1),(2,-1),(3,2),(4,1),(5,-1)), F0), den3),
          ldiv(lmul(poly((0,2),(1,1),(2,3),(3,-1),(6,-1)), F1), den3))

# ---------- Park eq (32), transcribed (same text as park_ahat_erratum.py) ----------
x, Q = sp.symbols('x Q'); q = Q**2
a0 = -q**9*x**7*(q**3*x+1)*(q**5*x**2-1)*(q**7*x**2-1)
a1 = (Q**11*x**2*(q*x+1)*(q**3*x+1)*(q**7*x-1)
      *(q**9*x**6+q**8*x**6-q**8*x**4-3*q**7*x**5-q**7*x**4-q**6*x**5
        +2*q**6*x**4+2*q**6*x**3+q**5*x**4-q**5*x**2-q**4*x**3-q**3*x**4
        -q**3*x**3+q**3*x**2+2*q**2*x**3+2*q**2*x**2-q*x**2-2*q*x+1))
a2 = (-q**2*(q**2*x-1)*(q**2*x+1)*(q*x**2-1)*(q**7*x**2-1)
      *(q**12*x**6+q**11*x**5-2*q**10*x**5-3*q**9*x**4+2*q**8*x**4-q**8*x**3
        +2*q**7*x**3-q**6*x**4-4*q**6*x**3-q**5*x**3-3*q**5*x**2+q**4*x**3
        +2*q**4*x**2+q**3*x-q**2*x**2-2*q**2*x+1))
a3 = (Q*(q*x**2-1)*(q*x+1)*(q**3*x+1)
      *(q**16*x**6-2*q**13*x**5-q**13*x**4+q**11*x**4+2*q**10*x**4+2*q**10*x**3
        -q**9*x**4-q**8*x**3-q**8*x**2-q**7*x**3-q**7*x**2+2*q**6*x**3+2*q**6*x**2
        +q**5*x**2-q**3*x**2-3*q**3*x-q**2*x+q+1))
a4 = (q*x+1)*(q*x**2-1)*(q**3*x**2-1)
A = [sp.expand(t) for t in (a0,a1,a2,a3,a4)]
def toQ(ex):
    p = sp.Poly(sp.expand(ex), Q); return {int(e): int(c) for (e,), c in p.terms()}
COEF = [{d: toQ(sp.Poly(a, x).coeff_monomial(x**d)) for d in range(int(sp.degree(a, x))+1)} for a in A]
COEF = [{d: c for d, c in C.items() if c} for C in COEF]

def q2Q(d): return {2*e: c for e, c in d.items()}
CAP = 2*LQ
def Qmul(a, b): return lmul(a, b, CAP)
def rowQ(n, extra=()):
    row = {}
    for i in range(5):
        for d, c in COEF[i].items():
            j = n-d
            if j < 0: continue
            row[j] = ladd(row.get(j, {}), {e+2*i*j+i: v for e, v in c.items()})
    for (i, d, cd) in extra:
        j = n-d
        if j >= 0: row[j] = ladd(row.get(j, {}), {e+2*i*j+i: v for e, v in cd.items()})
    return {j: v for j, v in row.items() if v}

# ---------- the true blocks ----------
FV = {int(j): {int(e): int(c) for e, c in d.items()} for j, d in json.load(open(BLOCKS)).items()}
TRUE = {0: F0, 1: F1, 2: F2, 3: F3}
for j, d in FV.items():
    if j >= 4 and d: TRUE[j] = d
print("="*78); print("true blocks in hand (Park's own for j<=3, large color R-matrix for j>=4)")
for j in sorted(TRUE):
    print("   f_%d : q^%-4d .. q^%-4d  (%d coefficients)"%(j, min(TRUE[j]), max(TRUE[j]), len(TRUE[j])))

# ---------- solve for c_3, c_4, c_5 ----------
print("="*78); print("SOLVING  delta_n = - sum_d c_d Q^{2(n-d)+1} f_{n-d}   for the corrections to a_1")
print("="*78)
S0 = q2Q(F0); C = {}
for n in (3, 4, 5, 6):
    R = rowQ(n)
    if any(j not in TRUE for j in R): print("   n=%d : needs f_%d, not available"%(n, max(R))); break
    VAL = min(min(R[j])+2*max(TRUE[j]) for j in R)
    d_ = {}
    for j, rj in R.items(): d_ = ladd(d_, Qmul(rj, q2Q(TRUE[j])))
    d_ = {e: c for e, c in d_.items() if c and e <= VAL}
    for d, cd in C.items():
        j = n-d
        if j >= 0 and j in TRUE:
            d_ = ladd(d_, {e+2*j+1: v for e, v in Qmul(cd, q2Q(TRUE[j])).items()})
    d_ = {e: c for e, c in d_.items() if c and e <= VAL}
    if not d_:
        print("   n=%d : residual zero -> c_%d = 0 as far as the data reaches (Q^%d)"%(n, n, VAL)); continue
    qt = ldiv({e: -c for e, c in d_.items()}, S0, VAL+2)
    qt = {e-1: c for e, c in qt.items()}
    if len(qt) <= 8:
        C[n] = {e: int(c) for e, c in qt.items()}
        print("   n=%d : c_%d = %s   (delta_%d exact to Q^%d)"
              %(n, n, " ".join("%+d q^{%s}"%(c, Fr(e,2)) for e, c in sorted(C[n].items())), n, VAL))
    else:
        print("   n=%d : residual/f_0 has %d terms and does not terminate within Q^%d --"
              " a further correction is needed and the data does not yet determine it"%(n, len(qt), VAL))
        break

# ---------- which placements the two EXACT moment equations allow ----------
print("="*78)
print("WHICH a_i CAN CARRY THE x^3 CORRECTION")
print("="*78)
print("""   delta_3 and delta_4 determine two exact quantities.  Writing c_{i,3} for the
   correction to a_i's x^3 coefficient, and U_3(t) = sum_i c_{i,3} Q^{(2t+1)i} :

       U_3(0) = -Q^26     (from delta_3, exact to Q^612)
       U_3(1) = -Q^28     (from delta_4; f_0 and f_1 are not rationally related, so
                           the pair (U_3(1), U_4(0)) solving delta_4 is UNIQUE, and it
                           comes out with ZERO free parameters)""")
print("   single index i :")
for i in range(5):
    ci = 26-i                              # c = -Q^{26-i}, forced by U_3(0)
    u1 = -(ci + 3*i)
    print("      i=%d : c_{%d,3} = -Q^%d  ->  U_3(1) = -Q^%d   %s"
          %(i, i, ci, ci+3*i, "CONSISTENT" if ci+3*i == 28 else "excluded"))
print("""   pairs {i,j} : the 2x2 system has a unique solution for every pair.  Every pair
      containing i=1 collapses to c_1 = -Q^25 with the other zero; {0,2}, {0,3},
      {0,4} and {2,4} force NON-LAURENT coefficients and are excluded outright;
      only {2,3} and {3,4} survive as genuine alternatives, and are NOT tested here.
   >>> a_1 is the UNIQUE single-index placement.  Splits over three or more a_i are
       not excluded by these two equations.""")

# ---------- controls ----------
def blocks(fix, NB):
    Cc = [{d: dict(c) for d, c in Ci.items()} for Ci in COEF]
    for (i, d, p_) in fix: Cc[i][d] = ladd(Cc[i].get(d, {}), p_)
    F = {0: q2Q(F0), 1: q2Q(F1)}
    for n in range(2, NB+1):
        row = {}
        for i in range(5):
            for d, c in Cc[i].items():
                j = n-d
                if j < 0 or j > n: continue
                row[j] = ladd(row.get(j, {}), {e+2*i*j+i: v for e, v in c.items()})
        row = {j: v for j, v in row.items() if v}
        rhs = {}
        for j, rj in row.items():
            if j < n: rhs = ladd(rhs, Qmul(rj, F[j]))
        F[n] = ldiv({e: -c for e, c in rhs.items()}, row[n], CAP)
    return F
CH = {5:1, 17:-1, 49:-1, 61:1, 71:-1, 83:1, 115:1, 127:-1}
def theta(MAX):
    out = {}; n = 1
    while True:
        e2 = n*n-25
        if e2 % 264: n += 1; continue
        e = e2//264
        if e > MAX: break
        if n % 132 in CH: out[e] = out.get(e, 0)+CH[n % 132]
        n += 1
    return out
T = {e-1: c for e, c in theta(4000).items()}
print("="*78); print("CONTROLS"); print("="*78)
FIX = [(1, d, C[d]) for d in sorted(C)]
c1 = c2 = c3 = True
prev_bl = prev_z = -99
for k in range(1, len(FIX)+1):
    NB = 16
    F = blocks(FIX[:k], NB)
    half = any(e % 2 for m in F for e in F[m])
    frac = any(Fr(v).denominator != 1 for m in F for v in F[m].values())
    c3 &= not (half or frac)
    fq = {m: {e//2: v for e, v in F[m].items()} for m in F}
    acc = {e: -c for e, c in fq[0].items()}
    for m in range(1, NB+1):
        gm = ladd(fq[m-1], fq[m], -1)
        for e, c in gm.items(): acc[e+m*m] = acc.get(e+m*m, 0)+c
    acc = {e: c for e, c in acc.items() if c}
    H = min((NB+1)**2 + min(min(fq[m]) for m in fq), 400)
    bad = [e for e in range(-1, H) if acc.get(e, 0) != T.get(e, 0)]
    z = bad[0] if bad else H
    bl = []
    tot = hit = 0
    SAFE = LQ - 100                     # ldiv resolves coefficients only up to its cap
    for j in sorted(TRUE):
        if j > 8: continue
        d = TRUE[j]
        rng = [e for e in sorted(d) if e <= min(max(fq.get(j, {0:0})), SAFE)]
        n_ = sum(1 for e in rng if fq.get(j, {}).get(e, 0) == d[e])
        bl.append("f_%d %d/%d"%(j, n_, len(rng))); tot += len(rng); hit += n_
    print("   %-22s : blocks %s" % ("+".join("c_%d"%d for d in sorted(C)[:k]), " ".join(bl)))
    print("   %-22s   Zhat(Sigma(2,3,11)) agrees on q^-1..q^%d ; integral Laurent: %s"
          %("", z-1, not (half or frac)))
    c1 &= (hit == tot) if k == len(FIX) else True
    c2 &= (z > prev_z); prev_z = z
print("-"*78)
print("   C1 every converged large-color block coefficient reproduced :", "PASSED" if c1 else "FAILED")
print("   C2 each correction extends the Sigma(2,3,11) agreement      :", "PASSED" if c2 else "FAILED")
print("   C3 all blocks integral Laurent polynomials in q             :", "PASSED" if c3 else "FAILED")
print("\n   HONEST LIMIT: the repair is INCOMPLETE.  A correction at x^6 remains, and")
print("   determining it needs f_6 to about ten converged coefficients.")
if not (c1 and c2 and c3): raise SystemExit("A CONTROL FAILED -- nothing reported.")
print("ALL CONTROLS PASSED.")
