#!/usr/bin/env python3
"""THE SINGLE-INDEX RECONSTRUCTION OF PARK eq (32) CANNOT CLOSE, AND THE REASON IS
EXACTLY THE THING THE DATA DOES NOT DETERMINE: THE SPLIT AMONG THE a_i.

Memo 183 addendum 2 reconstructed c_3, c_4, c_5 as corrections to a_1, and flagged
(section 4) that their shape argues they are not Park's own missing terms.  This
certificate turns that argument into a demonstration, and stops a wrong path.

THE ANSATZ TESTED.  At each x-degree d in turn, solve delta_d for the whole correction
and place it in a single a_i.  delta_d determines
      U_d(0) = sum_i c_{i,d} Q^i
uniquely and exactly, but NOT the five c_{i,d} separately.  The split is fixed only by
U_d(1), U_d(2), ... which enter delta_{d+1}, delta_{d+2}, ... -- so a sequential
single-index fit can always absorb the previous step's wrong split into the next
correction, and the error is pushed one degree up rather than removed.

WHAT HAPPENS.  a_1 has x-degree 11, so c_3..c_11 exhausts it; only a_0 and a_2 reach
x-degree 12, which is the maximum in the whole of eq (32).  Even with every one of those
degrees used, the assembled Zhat(Sigma(2,3,11)) still fails:

      c_3..c_11 in a_1                    first mismatch q^141
      c_3..c_11 in a_1, c_12 in a_0       first mismatch q^164
      c_3..c_11 in a_1, c_12 in a_2       first mismatch q^165

with horizons above q^760 in every case, so these are failures and not truncation.

WHAT THIS DOES AND DOES NOT COST.
  * Addendum 2's c_3 stands: delta_3 and delta_4 force it and force a_1 (that argument
    uses U_3(0) AND U_3(1), i.e. two exact quantities, not one).
  * Addendum 3 stands untouched: its Table 3 test uses f_0..f_5, and f_4 and f_5 were
    confirmed coefficient by coefficient against the large color R-matrix, so they are
    right however the corrections are distributed.
  * What falls is any reading of c_6..c_12 as determinations.  They are not banked.

WHAT THE REPAIR ACTUALLY NEEDS, stated so the ask is precise: the five c_{i,d} at each
degree need U_d(0), U_d(1), ..., U_d(4) -- a Vandermonde system in Q^{2i} -- and those
come from delta_d, ..., delta_{d+4}, hence from f_0 .. f_{d+4}.  Closing every degree up
to 12 therefore needs blocks to about f_16.  This bench has f_5.

Gate 5: exact integer / Fraction arithmetic.

CONTROLS:
  C1  every stage stays an integral Laurent series in q (so the failures below are not
      an arithmetic artefact of the fit).
  C2  the horizon exceeds the reported mismatch by a factor of three or more, so
      each failure is comfortably inside the range the computation controls.
"""
import sys
from fractions import Fraction as Fr
import sympy as sp
sys.path.insert(0, '/home/user/origin-axiom/outside_bench/certificates')
LQ = 500
def ladd(a, b, sc=1):
    r = dict(a)
    for e, c in b.items():
        r[e] = r.get(e, 0)+sc*c
        if r[e] == 0: del r[e]
    return r
def lmul(a, b, cap):
    r = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = e1+e2
            if e <= cap: r[e] = r.get(e, 0)+c1*c2
    return {e: c for e, c in r.items() if c}
def ldiv(num, den, cap):
    dl = min(den); dc = Fr(den[dl]); cur = dict(num); res = {}
    while cur:
        lo = min(cur)
        if lo-dl > cap: break
        k = Fr(cur[lo])/dc; res[lo-dl] = res.get(lo-dl, 0)+k
        for x, y in den.items():
            t = lo-dl+x; cur[t] = cur.get(t, 0)-Fr(y)*k
            if cur[t] == 0: del cur[t]
    return {e: c for e, c in res.items() if c}
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
def toQ(ex):
    p = sp.Poly(sp.expand(ex), Q); return {int(e): int(c) for (e,), c in p.terms()}
COEF = [{d: toQ(sp.Poly(sp.expand(a), x).coeff_monomial(x**d))
         for d in range(int(sp.degree(sp.expand(a), x))+1)} for a in (a0,a1,a2,a3,a4)]
COEF = [{d: c for d, c in C.items() if c} for C in COEF]
DEG = [max(C) for C in COEF]
CAP = 2*LQ
def q2Q(d): return {2*e: c for e, c in d.items()}
def blocks(fix, NB):
    C = [{d: dict(c) for d, c in Ci.items()} for Ci in COEF]
    for (i, d, p_) in fix: C[i][d] = ladd(C[i].get(d, {}), p_)
    F = {0: q2Q(F0), 1: q2Q(F1)}
    for n in range(2, NB+1):
        row = {}
        for i in range(5):
            for d, c in C[i].items():
                j = n-d
                if j < 0 or j > n: continue
                row[j] = ladd(row.get(j, {}), {e+2*i*j+i: v for e, v in c.items()})
        row = {j: v for j, v in row.items() if v}
        rhs = {}
        for j, rj in row.items():
            if j < n: rhs = ladd(rhs, lmul(rj, F[j], CAP))
        F[n] = ldiv({e: -c for e, c in rhs.items()}, row[n], CAP)
    return F
def rowQ(n, extra):
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
T = {e-1: c for e, c in theta(60000).items()}
NB = 30
print("="*78)
print("Park eq (32): x-degrees of a_0..a_4 = %s   -- the maximum anywhere is %d" % (DEG, max(DEG)))
print("a_1, which addendum 2 shows must carry the x^3 term, has degree %d." % DEG[1])
print("="*78)
FIX = [(1,3,{25:-1}), (1,4,{25:1,27:1,31:-1}), (1,5,{33:1,35:1}),
       (1,6,{27:-1,29:-1,35:-1,37:-2,41:1})]
def solveU(FX, d):
    F = blocks(FX, NB); fq = {m: {e//2: int(v) for e, v in F[m].items()} for m in F}
    acc = {e: -c for e, c in fq[0].items()}
    for m in range(1, d):
        g = ladd(fq[m-1], fq[m], -1)
        for e, c in g.items(): acc[e+m*m] = acc.get(e+m*m, 0)+c
    Rz = {e: T.get(e,0)-acc.get(e,0) for e in range(-2, (d+2)**2)}
    Rz = {e: c for e, c in Rz.items() if c}
    if not Rz: return None
    CUT = (d+1)**2 + min(min(fq[d]), min(fq[d+1]))
    gd = {e-d*d: c for e, c in Rz.items() if e < CUT}
    fd = {e: fq[d-1].get(e,0)-gd.get(e,0) for e in range(min(gd), CUT-d*d)}
    fd = {e: c for e, c in fd.items() if c}
    TRUE = {m: fq[m] for m in range(0, d)}; TRUE[d] = fd
    R = rowQ(d, FX); VAL = min(min(R[j])+2*max(TRUE[j]) for j in R)
    dd = {}
    for j, rj in R.items(): dd = ladd(dd, lmul(rj, q2Q(TRUE[j]), 10**7))
    dd = {e: c for e, c in dd.items() if c and e <= VAL}
    if not dd: return {}
    return ldiv({e: -c for e, c in dd.items()}, q2Q(fq[0]), VAL+2)
for d in range(7, 12):
    U = solveU(FIX, d)
    FIX = FIX + [(1, d, {e-1: int(c) for e, c in U.items() if c})]
U12 = solveU(FIX, 12)
print("U_12(0) = sum_i c_{i,12} Q^i = %s" % sorted((e, int(c)) for e, c in U12.items()))
print("   every exponent even, as the parity of the equation requires : %s"
      % all(e % 2 == 0 for e in U12))
def horizon(FX):
    F = blocks(FX, NB)
    if any(e % 2 for m in F for e in F[m]): return None, None, "half-integer q power"
    fq = {m: {e//2: v for e, v in F[m].items()} for m in F}
    if any(Fr(v).denominator != 1 for m in fq for v in fq[m].values()): return None, None, "non-integral"
    a = {e: -c for e, c in fq[0].items()}
    for m in range(1, NB+1):
        g = ladd(fq[m-1], fq[m], -1)
        for e, c in g.items(): a[e+m*m] = a.get(e+m*m, 0)+c
    a = {e: c for e, c in a.items() if c}
    H = min((NB+1)**2 + min(min(fq[m]) for m in fq), 4000)
    bad = [e for e in range(-1, H) if a.get(e, 0) != T.get(e, 0)]
    return (bad[0] if bad else None), H, "integral Laurent"
rows = [("c_3..c_11 all in a_1", FIX)]
for i in (0, 2):
    rows.append(("c_3..c_11 in a_1, c_12 in a_%d" % i, FIX + [(i, 12, {e-i: int(c) for e, c in U12.items()})]))
print("="*78)
c1 = c2 = True
for lab, FX in rows:
    b, H, kind = horizon(FX)
    c1 &= (kind == "integral Laurent")
    ok = (b is not None) and (H > 3*b)
    c2 &= ok
    print("   %-32s : %s   horizon q^%s (%.1fx the mismatch)   [%s]"
          % (lab, ("first mismatch q^%d" % b) if b else "MATCHES to the horizon", H,
             (H/b if b else 0), kind))
print("="*78)
print("""   x-degree 12 is the maximum anywhere in eq (32), so this ansatz has no degree
   left to use -- and it still fails, far inside its horizon.  The single-index
   reconstruction CANNOT CLOSE.

   The reason is structural: delta_d determines U_d(0) = sum_i c_{i,d} Q^i exactly but
   not the five c_{i,d} separately; the split is fixed by U_d(1)..U_d(4), which live in
   delta_{d+1}..delta_{d+4}.  A sequential single-index fit therefore absorbs each
   wrong split into the next correction and pushes the error one degree up.  Closing
   every degree to 12 needs blocks to about f_16; this bench has f_5.""")
print("   C1 every stage integral Laurent :", "PASSED" if c1 else "FAILED")
print("   C2 horizon exceeds the mismatch threefold :", "PASSED" if c2 else "FAILED")
if not (c1 and c2): raise SystemExit("A CONTROL FAILED -- nothing reported.")
print("ALL CONTROLS PASSED.")
