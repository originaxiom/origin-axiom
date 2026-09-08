#!/usr/bin/env python3
"""THE REPAIRED BLOCKS REPRODUCE PARK'S TABLE 3 AT p = -2 AND p = -3 -- placements the
repair never saw -- AND THE x^6 CORRECTION IS DETERMINED.

Memo 183 addendum 2 reconstructed c_3, c_4, c_5 (the corrections to a_1's x^3, x^4, x^5
coefficients) and tested them against the large color R-matrix blocks and against
Zhat(Sigma(2,3,11)).  Both of those live at p/r = -1.  Park's Table 3 also prints Zhat
for p = -2 and p = -3, where GM Thm 1.2's transform x^u -> q^{-u^2 r/p} places block k at
u^2/|p| rather than u^2 and the residue condition r u - a in pZ selects a DIFFERENT
subset of blocks for each spin^c label a.  Nothing in the repair saw those.

TWO THINGS ARE DONE HERE:

 (1) c_6.  f_6 is read off the surgery identity at p = -1 -- with f_0..f_5 exact, g_6 is
     readable on [36+lo(g_6), 49+lo(g_7)) -- and then delta_6 gives
         c_6 = -q^{27/2} - q^{29/2} - q^{35/2} - 2 q^{37/2} + q^{41/2},
     which extends the Zhat(Sigma(2,3,11)) agreement from q^33 to q^45.  Since c_6 was
     solved FROM that target, this is bookkeeping, not evidence -- which is why (2) exists.

 (2) THE INDEPENDENT TEST.  Using ONLY f_0..f_5 -- the blocks confirmed coefficient by
     coefficient against Park's own large color R-matrix in addendum 2 -- assemble
     Zhat_a(S^3_{p}(m(5_2))) for p = -1, -2, -3 and compare with Table 3.

Gate 5: exact integer / Fraction arithmetic.

CONTROLS:
  C1  all five of Park's Table 3 series match within their horizons, with ONE overall
      factor 1/2, the same for every series (GM's F_K = (1/2)(Xi(x) - Xi(1/x))).
      "Match" includes every ZERO below the horizon, which is the strong part: Park's
      p=-2 a=0 row is 1 - q then eighteen zeros.
  C2  spin^c conjugation: at p = -3 the labels a = 1 and a = 2 give identical series,
      which the assembly does not enforce.
  C3  at p = -1 the horizon survives a conservative bound on the unused blocks'
      lowest q-power, so that row does not depend on the repair beyond f_5.
"""
import sys, io, contextlib
from fractions import Fraction as Fr
import sympy as sp

LQ = 400
# ---------- Park's f_0, f_1, and his Q(q) formulas for f_2, f_3 ----------
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

# ---------- Park eq (32) plus the reconstructed corrections to a_1 ----------
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
C3 = {25: -1}; C4 = {25: 1, 27: 1, 31: -1}; C5 = {33: 1, 35: 1}
C6 = {27: -1, 29: -1, 35: -1, 37: -2, 41: 1}
FIX5 = [(1, 3, C3), (1, 4, C4), (1, 5, C5)]
NB = 18
F = blocks(FIX5, NB)
assert not any(e % 2 for m in F for e in F[m]), "half-integer q power"
fq = {m: {e//2: int(v) for e, v in F[m].items()} for m in F}
print("="*78)
print("blocks from the repaired recursion (c_3, c_4, c_5 only; f_0..f_5 are the ones")
print("addendum 2 confirmed against Park's large color R-matrix)")
for m in range(0, 9):
    print("   f_%d : q^%-5d lowest" % (m, min(fq[m])))

# ---------- (1) c_6 ----------
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
T = {e-1: c for e, c in theta(6000).items()}
def assemble_p1(fqd, NBm):
    acc = {e: -c for e, c in fqd[0].items()}
    for m in range(1, NBm+1):
        g = ladd(fqd[m-1], fqd[m], -1)
        for e, c in g.items(): acc[e+m*m] = acc.get(e+m*m, 0)+c
    return {e: c for e, c in acc.items() if c}
print("="*78); print("(1) the x^6 correction")
acc = assemble_p1(fq, NB)
bad = [e for e in range(-1, 200) if acc.get(e, 0) != T.get(e, 0)]
print("   with c_3,c_4,c_5 : Zhat(Sigma(2,3,11)) agrees on q^-1 .. q^%d" % (bad[0]-1))
F6 = blocks(FIX5+[(1, 6, C6)], NB)
fq6 = {m: {e//2: int(v) for e, v in F6[m].items()} for m in F6}
acc6 = assemble_p1(fq6, NB)
bad6 = [e for e in range(-1, 200) if acc6.get(e, 0) != T.get(e, 0)]
print("   with c_6 added   : Zhat(Sigma(2,3,11)) agrees on q^-1 .. q^%d" % (bad6[0]-1))
print("   c_6 = " + " ".join("%+d q^{%s}" % (c, Fr(e, 2)) for e, c in sorted(C6.items())))
print("   [solved FROM that target, so the extension is bookkeeping, not evidence]")

# ---------- (2) the independent test: Table 3 at p = -1, -2, -3 ----------
print("="*78)
print("(2) Park's Table 3, assembled from f_0..f_5 ALONE via GM Thm 1.2 + eq (1)")
print("    F_K = F+(x) - F+(1/x); prefactor (x^{1/2r} - x^{-1/2r}); L: x^u -> q^{-u^2 r/p}")
print("    if r u - a in pZ.  Blocks land at u^2/|p|, so p = -2, -3 place them where")
print("    nothing in the repair ever looked.")
print("="*78)
TRUST = 5
def assemble(P, r, a, LOF):
    out = {}; H = None
    for k in range(1, 60):
        h = Fr(2*k-1, 2)
        for eps in (1, -1):
            for s in (1, -1):
                u = eps*h + Fr(s, 2*r); sg = eps*s
                if (r*u - a) % P != 0: continue
                E = -u*u*Fr(r, P)
                if k-1 <= TRUST:
                    for eq, c in fq[k-1].items(): out[E+eq] = out.get(E+eq, 0)+sg*c
                else:
                    E2 = E + LOF(k-1); H = E2 if H is None else min(H, E2)
    return {e: c for e, c in out.items() if c}, H
LO_OWN = lambda j: Fr(min(fq[j])) if j in fq else Fr(-((2*j+1)**2), 40)
LO_CONS = lambda j: Fr(-(j-3)**2)
T3 = {-1: [(0, [(0,1),(1,-1),(9,-1),(14,1),(19,-1),(26,1),(50,1)], 60)],
      -2: [(0, [(0,1),(1,-1),(18,1),(25,-1),(31,1),(40,-1)], 90),
           (1, [(0,-1),(3,1),(6,-1),(11,1),(45,-1)], 55)],
      -3: [(0, [(0,1),(1,-1),(8,1),(13,-1),(17,1),(24,-1)], 44),
           (1, [(0,-1),(3,1),(27,-1),(36,1)], 83)]}
def check(P, a, ref, LOF):
    out, H = assemble(P, 1, a, LOF)
    lo = min(out); rel = {e-lo: c for e, c in out.items()}
    sc = Fr(ref[0][1], rel[Fr(0)]); hor = H - lo
    nz = {y for y, _ in ref}
    good = all(sc*rel.get(Fr(y), 0) == c for y, c in ref if y < hor) and \
           all(sc*c == 0 for y, c in rel.items() if y < hor and y.denominator == 1 and int(y) not in nz)
    n = sum(1 for y, _ in ref if y < hor)
    return good, hor, n, sc, rel, lo
c1 = True; scs = set()
for P in (-1, -2, -3):
    for (a, ref, _) in T3[P]:
        good, hor, n, sc, rel, lo = check(P, a, ref, LO_OWN)
        c1 &= good; scs.add(sc)
        zer = sum(1 for y in range(int(hor)) if Fr(y) not in rel or rel[Fr(y)] == 0)
        print("   p=%-3d a=%d : lo = q^%-6s verified to q^%-5s -> %d of Park's %d printed terms,"
              " and %d zeros  %s" % (P, a, lo, hor, n, len(ref), zer, "MATCH" if good else "MISMATCH"))
print("   one overall factor for every series : %s  ->  %s"
      % (sorted(scs), "PASSED" if len(scs) == 1 else "FAILED"))
c1 &= (len(scs) == 1)
o1, _ = assemble(-3, 1, 1, LO_OWN); o2, _ = assemble(-3, 1, 2, LO_OWN)
c2 = (o1 == o2)
print("   C2 spin^c conjugation, p=-3: a=1 and a=2 give identical series :", "PASSED" if c2 else "FAILED")
good, hor, n, sc, _, _ = check(-1, 0, T3[-1][0][1], LO_CONS)
c3 = good and n >= 5
print("   C3 p=-1 under the conservative bound lo(f_j) >= -(j-3)^2 : verified to q^%s,"
      " %d printed terms, %s" % (hor, n, "MATCH" if good else "MISMATCH"))
print("""
   FENCE.  At p = -2 and p = -3 the horizon is finite only if the blocks' lowest
   q-powers fall more slowly than the placements u^2/|p| grow -- which is GM's own
   applicability condition (177), 4c + r/p > 0.  The horizons above use the repaired
   recursion's computed lo(f_j) through j = %d and -(2j+1)^2/40 beyond, the slope the
   measured blocks show; under the much harsher -(j-3)^2 the p = -2, -3 sums do not
   converge at all and those two rows say nothing.  This is a genuine dependence and
   it is not hidden: what those rows verify is CONDITIONAL on 5_2's block edge falling
   at roughly the measured rate.""" % NB)
print("="*78)
OK = {"C1 Table 3 matches": c1, "C2 spin^c conjugation": c2, "C3 p=-1 unconditional": c3}
print("CONTROLS:", {k: ("PASSED" if v else "FAILED") for k, v in OK.items()})
if not all(OK.values()): raise SystemExit("A CONTROL FAILED -- nothing reported.")
print("ALL CONTROLS PASSED.")
