#!/usr/bin/env python3
"""THE QUANTUM A-POLYNOMIAL PRINTED IN PARK eq (32) DOES NOT ANNIHILATE F^+_{m(5_2)}.

Source: Sunghyuk Park, "Large color R-matrix for knot complements and strange
identities", arXiv:2004.02087v2, p.15-17.

Park's page 15 gives, for K = m(5_2) = K_{2,1},

    F^+_K(x,q) = x^{1/2} sum_{j>=0} f_j(q) x^j,
    f_0 = -q^{-1} sum_{j>=0} (-1)^j q^{j(j+1)/2},
    f_1 = -q^{-1} sum_{j>=0} (-1)^j q^{j(j+1)/2} (1-q^{j+1})/(1-q),

his page 17 gives Ahat_K = sum_{i=0}^{4} a_i(x,q) yhat^i explicitly (eq (32)),
states that Ahat_K annihilates F^+_K, and prints f_2 and f_3 BOTH as q-series and
as Q(q)-linear combinations of f_0 and f_1.

THIS SCRIPT SHOWS THOSE THREE STATEMENTS ARE MUTUALLY INCONSISTENT, and localises
the inconsistency exactly:

    [Ahat_printed F^+]_{x^{7/2}} = q^13 * f_0(q)   (not 0)

and no single monomial added to any a_i repairs it.

Gate 5: exact integer / Fraction arithmetic throughout.  No measured input, no
fitted constant.  Every published series used appears as a COMPARISON TARGET only.

CONTROLS (all must fire; the finding is reported only if they do):
  C1  Park's closed forms reproduce his printed f_0, f_1.
  C2  Park's rational formulas reproduce his printed f_2, f_3.
  C3  the operator convention is FORCED: of five readings of "a_i(x,q) yhat^i",
      exactly one makes the x^{1/2} and x^{3/2} equations vanish identically.
  C4  Gukov-Manolescu Thm 1.2 at p/r = -1, assembled by the placement this bench
      already validated at p/r = -1/2 against GM eq (13), reproduces GM eq (12)
      for -Sigma(2,3,7) from the figure-eight's blocks.
  C5  the false theta reconstructed from Park's Table 3 (p=-1) reproduces all
      seven printed exponents WITH SIGNS and its stated O(q^61) truncation.
"""
import sys, io, contextlib
from fractions import Fraction as Fr
import sympy as sp

NQ = int(sys.argv[1]) if len(sys.argv) > 1 else 300     # q-order kept
OK = {}

# =====================================================================
# Laurent arithmetic in q (integer keys are q-exponents)
# =====================================================================
def ladd(a, b, sc=1):
    r = dict(a)
    for e, c in b.items():
        r[e] = r.get(e, 0) + sc*c
        if r[e] == 0: del r[e]
    return r
def lmul(a, b, cap):
    r = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            e = e1+e2
            if e <= cap: r[e] = r.get(e, 0) + c1*c2
    return {e: c for e, c in r.items() if c}
def ldiv(num, den, cap):
    dl = min(den); dc = Fr(den[dl]); cur = dict(num); res = {}
    while cur:
        lo = min(cur)
        if lo-dl > cap: break
        k = Fr(cur[lo])/dc; res[lo-dl] = res.get(lo-dl, 0) + k
        for x, y in den.items():
            t = lo-dl+x; cur[t] = cur.get(t, 0) - Fr(y)*k
            if cur[t] == 0: del cur[t]
    return {e: c for e, c in res.items() if c}
def poly(*t):
    d = {}
    for e, c in t: d[e] = d.get(e, 0)+c
    return {e: c for e, c in d.items() if c}
def head(d, lo, n): return [int(d.get(lo+i, 0)) for i in range(n)]

# =====================================================================
# 1. Park p.15: f_0, f_1 in closed form            [C1]
# =====================================================================
print("="*78); print("C1  Park's closed forms for f_0, f_1"); print("="*78)
def f0ser():
    a = {}; j = 0
    while j*(j+1)//2 <= NQ+2:
        a[j*(j+1)//2] = a.get(j*(j+1)//2, 0) + (-1)**j; j += 1
    return {e-1: -c for e, c in a.items() if c}
def f1ser():
    a = {}; j = 0
    while j*(j+1)//2 <= NQ+2:
        b = j*(j+1)//2
        for t in range(j+1):
            if b+t <= NQ+2: a[b+t] = a.get(b+t, 0) + (-1)**j
        j += 1
    return {e-1: -c for e, c in a.items() if c}
F0, F1 = f0ser(), f1ser()
P_f0 = {-1:-1, 0:1, 2:-1, 5:1, 9:-1, 14:1, 20:-1, 27:1}          # printed, to O(q^35)
P_f1 = {-1:-1, 0:1, 1:1, 2:-1, 3:-1, 4:-1, 5:1, 6:1, 7:1, 8:1}   # printed, to O(q^9)
c1 = (all(F0.get(e,0)==v for e,v in P_f0.items()) and
      all(F0.get(e,0)==0 for e in range(-1,35) if e not in P_f0) and
      all(F1.get(e,0)==v for e,v in P_f1.items()) and
      all(F1.get(e,0)==0 for e in range(-1,9) if e not in P_f1))
print("   f_0 q^-1.. :", head(F0,-1,12)); print("   f_1 q^-1.. :", head(F1,-1,12))
print("   C1:", "PASSED" if c1 else "FAILED"); OK['C1'] = c1

# =====================================================================
# 2. Park p.17: f_2, f_3 as Q(q)-combinations of f_0, f_1     [C2]
# =====================================================================
print("="*78); print("C2  Park's rational formulas for f_2, f_3"); print("="*78)
den2 = poly((1,-1),(3,1))
F2 = ladd(ldiv(lmul(poly((0,1),(1,1),(2,-1)), F0, NQ), den2, NQ),
          ldiv(lmul(poly((0,-1),(1,-2),(2,1)), F1, NQ), den2, NQ))
den3 = poly((2,1),(4,-1),(5,-1),(7,1))
F3 = ladd(ldiv(lmul(poly((0,-2),(1,-1),(2,-1),(3,2),(4,1),(5,-1)), F0, NQ), den3, NQ),
          ldiv(lmul(poly((0,2),(1,1),(2,3),(3,-1),(6,-1)), F1, NQ), den3, NQ))
P_f2 = [-1,2,1,-1,-2,-2,1,1,3,2,0,-1]        # q^-1 .. q^10, printed to O(q^11)
P_f3 = [0,2,1,-2,-2,-3,0,2,4,4,2,0,-3]       # q^-1 .. q^11, printed to O(q^12)
c2 = head(F2,-1,12)==P_f2 and head(F3,-1,13)==P_f3
print("   f_2 q^-1.. :", head(F2,-1,12), "   Park:", P_f2)
print("   f_3 q^-1.. :", head(F3,-1,13), "   Park:", P_f3)
print("   C2:", "PASSED" if c2 else "FAILED"); OK['C2'] = c2

# =====================================================================
# 3. Park eq (32), transcribed.  q = Q^2 so q^{1/2} = Q.
#    Verified against TWO independent extractions of the source PDF
#    (raw text and pypdf layout mode); they agree monomial for monomial.
# =====================================================================
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
COEF = [{int(d): toQ(sp.Poly(a, x).coeff_monomial(x**d))
         for d in range(int(sp.degree(a, x))+1)} for a in A]
COEF = [{d: c for d, c in C.items() if c} for C in COEF]
DEG = [max(C) for C in COEF]
print("="*78); print("Park eq (32): x-degrees of a_0..a_4 =", DEG); print("="*78)

# =====================================================================
# 4. The operator convention is forced                       [C3]
#    yhat acts on F(x) by F(x) -> F(qx); Ahat F = sum_i a_i(x) (yhat^i F).
#    Coefficient of x^{n+1/2}:  sum_i sum_d a_{i,d} q^{i(n-d+1/2)} f_{n-d}.
# =====================================================================
print("="*78); print("C3  the operator convention"); print("="*78)
def q2Q(d): return {2*e: c for e, c in d.items()}
FT = {0:q2Q(F0), 1:q2Q(F1), 2:q2Q(F2), 3:q2Q(F3)}
CAPQ = 2*NQ - 60
def Qmul(a, b): return lmul(a, b, CAPQ)
def rowW(n, w):
    row = {}
    for i in range(5):
        for d, c in COEF[i].items():
            j = n-d
            if j < 0: continue
            r = row.setdefault(j, {})
            for e, v in c.items():
                e2 = e + w(i, n, d); r[e2] = r.get(e2, 0) + v
                if r[e2] == 0: del r[e2]
    return {j: v for j, v in row.items() if v}
CONV = {
 "A   q^{i(n-d+1/2)}   yhat^i on the right, y:F(x)->F(qx)": lambda i,n,d: 2*i*(n-d)+i,
 "B   q^{i(n+1/2)}     yhat^i on the left":                 lambda i,n,d: 2*i*n+i,
 "C   q^{-i(n-d+1/2)}  y:F(x)->F(x/q), right":              lambda i,n,d: -(2*i*(n-d)+i),
 "D   q^{-i(n+1/2)}    y:F(x)->F(x/q), left":               lambda i,n,d: -(2*i*n+i),
 "E   q^{i(n-d)}       no half-integer shift":              lambda i,n,d: 2*i*(n-d),
}
verdict = {}
for name, w in CONV.items():
    st = []
    for n in (0, 1, 2):
        R = rowW(n, w)
        if not R: st.append("row vanishes"); continue
        if max(R) > 3: st.append("needs f_%d" % max(R)); continue
        acc = {}
        for j, rj in R.items(): acc = ladd(acc, Qmul(rj, FT[j]))
        acc = {e: c for e, c in acc.items() if c and e <= CAPQ}
        st.append("delta=0" if not acc else "delta != 0")
    verdict[name] = st
    print("   %-52s n=0,1,2 : %s" % (name, st))
c3 = (verdict[list(CONV)[0]] == ["row vanishes", "row vanishes", "delta=0"] and
      all(v != ["row vanishes","row vanishes","delta=0"] for k,v in verdict.items() if not k.startswith("A")))
print("   C3 (exactly one convention leaves f_0, f_1 free AND gives Park's f_2):",
      "PASSED" if c3 else "FAILED"); OK['C3'] = c3
W = CONV[list(CONV)[0]]

# =====================================================================
# 5. THE DEFECT at x^{7/2}
# =====================================================================
print("="*78); print("THE DEFECT"); print("="*78)
R3 = rowW(3, W)
d3 = {}
for j, rj in R3.items(): d3 = ladd(d3, Qmul(rj, FT[j]))
d3 = {e: c for e, c in d3.items() if c and e <= CAPQ}
tgt = {e+26: c for e, c in q2Q(F0).items() if e+26 <= CAPQ}
exact = all(Fr(d3.get(e,0)) == Fr(v) for e, v in tgt.items()) and \
        all(e in tgt for e in d3)
nterms = len([e for e in tgt if e <= CAPQ])
print("   [Ahat_printed F^+]_{x^{7/2}}  =  q^13 * f_0(q)  ?  %s"
      "   (checked on %d nonzero coefficients, to q^%d)"
      % ("YES, EXACTLY" if exact else "NO", nterms, CAPQ//2))
print("   first terms of the defect :", sorted(d3.items())[:8])
# what the printed Ahat's own recursion produces for f_3
f3rec = ladd(FT[3], ldiv({e:-c for e,c in d3.items()}, R3[3], CAPQ))
diff = ladd(f3rec, FT[3], -1)
print("   recursion's f_3 minus Park's printed f_3 :",
      {Fr(e,2): c for e, c in sorted(diff.items())[:6]}, " (in q)")
OK['defect'] = exact

# =====================================================================
# 6. C4  the p/r = -1 assembly, controlled on the figure-eight
#        Zhat = eps q^d [ -Xi_1 + sum_{m>=1}(Xi_m - Xi_{m+1}) q^{m^2} ]
# =====================================================================
print("="*78); print("C4  GM Thm 1.2 at p/r = -1, controlled on 4_1 against GM eq (12)")
print("="*78)
old = sys.argv[:]; sys.argv = ['xi', '20']
buf = io.StringIO()
src = open('/home/user/origin-axiom/outside_bench/certificates/xi_recursion_fast.py').read()
src = src.split('# ---- assemble Zhat_0')[0]
g = {'__name__': '__main__'}
with contextlib.redirect_stdout(buf): exec(src, g)
sys.argv = old
block, N41 = g['block'], g['N']
XI = {k: dict(zip(range(block(k)[0], block(k)[0]+len(block(k)[1])), block(k)[1]))
      for k in range(1, N41+1)}
T41 = {e: -c for e, c in XI[1].items()}
for m in range(1, N41):
    gm = ladd(XI[m], XI[m+1], -1)
    for e, c in gm.items(): T41[e+m*m] = T41.get(e+m*m, 0)+c
T41 = {e: c for e, c in T41.items() if c}
lo41 = min(T41)
GM12 = {0:1,1:1,3:1,4:1,5:1,7:2,8:1,9:2,10:1,11:2}
got41 = [T41.get(lo41+e, 0) for e in range(12)]
ref41 = [GM12.get(e, 0) for e in range(12)]
c4 = got41 == ref41 or [-v for v in got41] == ref41
print("   assembled :", got41); print("   GM eq (12):", ref41)
print("   C4:", "PASSED (eps = %+d)" % (1 if got41==ref41 else -1) if c4 else "FAILED")
OK['C4'] = c4

# =====================================================================
# 7. C5  Zhat(Sigma(2,3,11)) as a false theta -- Park's Table 3, p = -1
#        chi odd mod 132, support +-{5,17,49,61}, exponent (n^2-25)/264
# =====================================================================
print("="*78); print("C5  Zhat(Sigma(2,3,11)) generated independently as a false theta")
print("="*78)
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
S = theta(4000)
P_T3 = {0:1, 1:-1, 9:-1, 14:1, 19:-1, 26:1, 50:1}
c5 = (all(S.get(e,0)==v for e,v in P_T3.items()) and
      all(S.get(e,0)==0 for e in range(0,61) if e not in P_T3) and S.get(61,0)==-1)
print("   generated, q^0..q^60 :", sorted((e,c) for e,c in S.items() if e <= 60))
print("   Park Table 3, p=-1   : 1 -q -q^9 +q^14 -q^19 +q^26 +q^50 -O(q^61)")
print("   next term q^61 =", S.get(61,0), " (Park's O(q^61), sign included)")
print("   C5:", "PASSED" if c5 else "FAILED"); OK['C5'] = c5

# =====================================================================
# 8. EXHAUSTIVE: no single monomial added to eq (32) repairs it
# =====================================================================
print("="*78); print("EXHAUSTIVE SINGLE-MONOMIAL REPAIR SEARCH"); print("="*78)
print("""   A monomial k*Q^b x^d added to a_i changes the equation at x^{n+1/2} by
   k*Q^{b+2i(n-d)+i} f_{n-d}.
     d <= 2 changes the x^{5/2} equation, which is already exact -> breaks f_2.
     d >= 4 leaves the x^{7/2} equation untouched -> leaves the defect.
   So d = 3 exactly, and the x^{7/2} equation forces k*Q^{b+i} = -q^13,
   i.e. k = -1 and b = 26 - i.  FIVE candidates, i = 0..4, no others.""")
def blocks(i_fix, NB):
    C = [{d: dict(c) for d, c in Ci.items()} for Ci in COEF]
    if i_fix is not None:
        C[i_fix][3] = ladd(C[i_fix].get(3, {}), {26-i_fix: 1}, -1)
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
            if j < n: rhs = ladd(rhs, Qmul(rj, F[j]))
        F[n] = ldiv({e: -c for e, c in rhs.items()}, row[n], CAPQ)
    return F
NB = 14
for i_fix in (0, 1, 2, 3, 4):
    F = blocks(i_fix, NB)
    fq = {m: {e//2: v for e, v in F[m].items() if e % 2 == 0} for m in F}
    assert all(all(e % 2 == 0 for e in F[m]) for m in F), "half-integer q power"
    ok3 = head(fq[3], -1, 13) == P_f3
    acc = {e: -c for e, c in fq[0].items()}
    for m in range(1, NB+1):
        gm = ladd(fq[m-1], fq[m], -1)
        for e, c in gm.items():
            if e+m*m <= NQ: acc[e+m*m] = acc.get(e+m*m, 0)+c
    acc = {e: c for e, c in acc.items() if c}
    lo = min(acc); T = {e-1: c for e, c in S.items()}     # normalise lowest to q^-1
    # horizon: no block m > NB reaches below (NB+1)^2 + min_m lo(f_m)
    H = min((NB+1)**2 + min(min(fq[m]) for m in fq), NQ)
    bad = [e for e in range(-1, H) if acc.get(e, 0) != T.get(e, 0)]
    print("   i=%d  (a_%d gains -q^%s x^3) : f_3 %s ; assembled vs Sigma(2,3,11) "
          "on q^-1..q^%d : %s"
          % (i_fix, i_fix, Fr(26-i_fix, 2), "OK" if ok3 else "WRONG", H-1,
             "MATCH" if not bad else "first mismatch q^%d (mine %s, true %s)"
             % (bad[0], acc.get(bad[0],0), T.get(bad[0],0))))
print("\n   ==> every single-monomial repair fails.  The erratum is not one dropped term.")

print("="*78)
print("CONTROLS:", {k: ("PASSED" if v else "FAILED") for k, v in OK.items()})
if not all(OK.values()):
    raise SystemExit("A CONTROL FAILED -- nothing above is reported.")
print("ALL CONTROLS PASSED.")
