#!/usr/bin/env python3
"""THE ERRATUM, LOCALISED AND MADE FAIR: PARK's PRINTED eq (32) ANNIHILATES NOTHING, BUT
THE CONSEQUENCES HE PRINTS FROM IT ARE CORRECT -- so the defect is in the TRANSCRIPTION
of the operator, not in the computation behind it.  And the operator file that was
supposed to settle this is for the WRONG KNOT.

Memo 183 found that Park's printed quantum A-polynomial (arXiv:2004.02087v2 eq (32)) does
not annihilate F^+_{m(5_2)}: the defect is [Ahat_printed F^+]_{x^{7/2}} = q^13 f_0(q),
exact on 23 nonzero coefficients to q^270.  fetch/FETCH_REQUEST_CEFF.md section B'' has
asked ever since for the primary-source operator, to say WHERE the transcription went
wrong.  Two sources arrived on 2026-09-09:

  * data/vendored/rec.twist.knot.2.m -- Garoufalidis-Sun twist.knot.data, an order-4
    inhomogeneous q-difference operator;
  * S. Garoufalidis, "Quantum knot invariants" (arXiv:1201.3314v3, Arbeitstagung survey),
    which PRINTS in section 4 an order-3 inhomogeneous recursion for the colored Jones of
    5_2 = the (-2,3,-1) pretzel knot.  It is transcribed verbatim below.

NOTHING HERE IS TAKEN ON A FILENAME OR ON A LABEL.  Every operator is identified the way
memo 186 identified the colored Jones tables: by what it actually annihilates.

WHAT IS TESTED, AND AGAINST WHAT.  This bench holds the colored Jones of five knots:
3_1, 4_1, 6_1, 9_2 (Garoufalidis-Sun tables, identified by determinant in
cj_table_ingest.py) and 5_2 (computed HERE, by the R-matrix state sum of
park_rmatrix_check.py on Park's braid word beta_2 -- see memo 185 addendum 3).

  T1  IDENTIFY rec.twist.knot.2.m by annihilation, over five knots x 2 mirrors x 3 shifts.
  T2  IDENTIFY the survey's order-3 recursion the same way.
  T3  the hypothesis that Park transcribed the WRONG twist-knot file: is eq (32) the
      operator in rec.twist.knot.2.m, up to an overall left factor?

  CELL 1 -- does Park's printed eq (32) annihilate the colored Jones of ANY knot here?
     A  yes, for some knot and some convention -> eq (32) is a correct operator that was
        merely mismatched to F^+, and memo 183's defect lies elsewhere.
     B  no -> the printed operator is defective as printed.

  CELL 2 -- are the CONSEQUENCES Park prints from eq (32) also wrong?  He prints, on the
     same page, f_2 and f_3 as explicit Q(q)-combinations of f_0 and f_1.  This bench
     computed f_0..f_5 independently, from his large-colour Verma R-matrix
     (certificates/park_large_color.py, memo 183 addendum 1).
     A  they fail too   -> the error is upstream, in the computation.
     B  they hold       -> the error is confined to the printed operator, and the
        computation behind the paper was right.  This is the outcome that is FAIR to the
        author, and it is stated as plainly as the negative.

Gate 5: exact integer and Fraction arithmetic.  No measured value.
"""
import os, re, json
from fractions import Fraction as Fr
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
x, q = sp.symbols('x q')
FS = sp.symbols('F0 F1 F2 F3 F4')

def prep(s):
    s = re.sub(r'\s+', ' ', s)
    for k, r in ((r'f\[4 \+ n\]', 'F4'), (r'f\[3 \+ n\]', 'F3'), (r'f\[2 \+ n\]', 'F2'),
                 (r'f\[1 \+ n\]', 'F1'), (r'f\[n\]', 'F0')):
        s = re.sub(k, r, s)
    s = re.sub(r'q\^\(\s*(\d+)\s*\+\s*(\d*)\*?n\s*\)',
               lambda m: '(q**%s*x**%s)' % (m.group(1), m.group(2) or '1'), s)
    s = re.sub(r'q\^n', 'x', s); s = re.sub(r'q\^(\d+)', r'q**\1', s); s = s.replace('^', '**')
    return sp.sympify(s, locals={'q': q, 'x': x, **{str(f): f for f in FS}})

REC_M = prep(open(os.path.join(DATA, "vendored", "rec.twist.knot.2.m")).read())
SURVEY = prep("""
- q^(9 + 7*n)*(-1 + q^n)*(-1 + q^(2 + n))*(1 + q^(2 + n))*(-1 + q^(5 + 2*n))*f[n]
+ q^(5 + 2*n)*(-1 + q^(1 + n))^2*(1 + q^(1 + n))*(-1 + q^(5 + 2*n))*(-1 + q^(1 + n)
  + q^(1 + 2*n) - q^(2 + 2*n) - q^(3 + 2*n) + q^(4 + 2*n) - q^(2 + 3*n) - q^(5 + 3*n)
  - 2*q^(5 + 4*n) + q^(6 + 5*n))*f[1 + n]
- q*(-1 + q^(2 + n))^2*(1 + q^(2 + n))*(-1 + q^(1 + 2*n))*(-1 + 2*q^(2 + n) + q^(2 + 2*n)
  + q^(5 + 2*n) - q^(4 + 3*n) + q^(5 + 3*n) + q^(6 + 3*n) - q^(7 + 3*n) - q^(7 + 4*n)
  + q^(9 + 5*n))*f[2 + n]
- (-1 + q^(1 + n))*(1 + q^(1 + n))*(-1 + q^(3 + n))*(-1 + q^(1 + 2*n))*f[3 + n]
""")
SURVEY_INHOM = prep("q^(4 + 2*n)*(1 + q^(1 + n))*(1 + q^(2 + n))*(-1 + q^(1 + 2*n))"
                    "*(-1 + q^(3 + 2*n))*(-1 + q^(5 + 2*n))")

# ---------- Park eq (32), transcribed verbatim from arXiv:2004.02087v2 p.17 ----------
t = sp.symbols('t'); Q2 = t**2                       # q = t^2, so q^{1/2} = t
def _P(e): return sp.expand(e)
P1 = _P(Q2**9*x**6+Q2**8*x**6-Q2**8*x**4-3*Q2**7*x**5-Q2**7*x**4-Q2**6*x**5+2*Q2**6*x**4
       +2*Q2**6*x**3+Q2**5*x**4-Q2**5*x**2-Q2**4*x**3-Q2**3*x**4-Q2**3*x**3+Q2**3*x**2
       +2*Q2**2*x**3+2*Q2**2*x**2-Q2*x**2-2*Q2*x+1)
P2 = _P(Q2**12*x**6+Q2**11*x**5-2*Q2**10*x**5-3*Q2**9*x**4+2*Q2**8*x**4-Q2**8*x**3
       +2*Q2**7*x**3-Q2**6*x**4-4*Q2**6*x**3-Q2**5*x**3-3*Q2**5*x**2+Q2**4*x**3
       +2*Q2**4*x**2+Q2**3*x-Q2**2*x**2-2*Q2**2*x+1)
P3 = _P(Q2**16*x**6-2*Q2**13*x**5-Q2**13*x**4+Q2**11*x**4+2*Q2**10*x**4+2*Q2**10*x**3
       -Q2**9*x**4-Q2**8*x**3-Q2**8*x**2-Q2**7*x**3-Q2**7*x**2+2*Q2**6*x**3+2*Q2**6*x**2
       +Q2**5*x**2-Q2**3*x**2-3*Q2**3*x-Q2**2*x+Q2+1)
PARK = [-Q2**9*x**7*(Q2**3*x+1)*(Q2**5*x**2-1)*(Q2**7*x**2-1),
        t**11*x**2*(Q2*x+1)*(Q2**3*x+1)*(Q2**7*x-1)*P1,
        -Q2**2*(Q2**2*x-1)*(Q2**2*x+1)*(Q2*x**2-1)*(Q2**7*x**2-1)*P2,
        t*(Q2*x**2-1)*(Q2*x+1)*(Q2**3*x+1)*P3,
        (Q2*x+1)*(Q2*x**2-1)*(Q2**3*x**2-1)]
PTERMS = []
for a in PARK:
    p = sp.Poly(sp.expand(a), x, t)
    PTERMS.append([(m[0], m[1], int(c)) for m, c in zip(p.monoms(), p.coeffs())])

# ---------- the colored Jones this bench holds ----------
CJ = json.load(open(os.path.join(DATA, "cj_first10.json"))); CJ.pop("_provenance")
KN = {k: [dict((int(e), int(c)) for e, c in z) for z in v["J"]] for k, v in CJ.items()}
D52 = json.load(open(os.path.join(DATA, "cyclotomic_52.json")))
KN["5_2"] = [dict((int(e), int(c)) for e, c in z) for z in D52["5_2"]["J"]][:10]

def annihilates(E, order, JJ, mirror, off, NMAX=6):
    res = []
    for nn in range(1, NMAX+1):
        idx = [nn+off+i for i in range(order+1)]
        if min(idx) < 1 or max(idx) > len(JJ): continue
        sub = {x: q**(-nn) if mirror else q**nn}
        for i in range(5):
            if i <= order:
                d = JJ[idx[i]-1]
                if mirror: d = {-e: c for e, c in d.items()}
                sub[FS[i]] = sum(c*q**e for e, c in d.items())
            else: sub[FS[i]] = 0
        res.append(sp.expand(E.subs(sub)) == 0)
    return res
def sweep(E, order, name):
    hits = []
    for k, JJ in KN.items():
        for mirror in (False, True):
            for off in (0, 1, -1):
                r = annihilates(E, order, JJ, mirror, off)
                if r and all(r): hits.append((k, "mirror" if mirror else "direct", off, len(r)))
    print("   %-34s annihilates : %s" % (name, hits if hits else "NOTHING"))
    return hits

OK = {}
print("=" * 78)
print("T1 / T2  --  IDENTIFY EACH OPERATOR BY WHAT IT ANNIHILATES")
print("=" * 78)
h1 = sweep(REC_M, 4, "rec.twist.knot.2.m (order 4)")
h2 = sweep(SURVEY + SURVEY_INHOM, 3, "survey 1201.3314 (order 3)")
OK["T1  rec.twist.knot.2.m annihilates 6_1 = K_{-2}, and only 6_1"] = \
    (len(h1) == 1 and h1[0][0] == "6_1" and h1[0][3] >= 6)
OK["T2  the survey's order-3 recursion annihilates 5_2, and only 5_2"] = \
    (len(h2) == 1 and h2[0][0] == "5_2" and h2[0][3] >= 6)
print()
print("   ==> the file named rec.twist.knot.2.m holds the operator for K_{-2} = 6_1.")
print("       A LOST MINUS SIGN, the same one memo 186 found in the CJTwist filenames.")
print("   ==> the survey's printed order-3 recursion IS 5_2's, verified against this")
print("       bench's own R-matrix colored Jones at six values of n.")

print()
print("=" * 78)
print("CELL 1  --  does Park's printed eq (32) annihilate ANY colored Jones here?")
print("=" * 78)
def mul(A, B):
    r = {}
    for e1, c1 in A.items():
        for e2, c2 in B.items(): r[e1+e2] = r.get(e1+e2, 0) + c1*c2
    return {e: c for e, c in r.items() if c}
def addd(A, B):
    r = dict(A)
    for e, c in B.items():
        r[e] = r.get(e, 0) + c
        if r[e] == 0: del r[e]
    return r
def pcoef(i, n, mirror):
    d = {}; s = -1 if mirror else 1
    for jx, jt, c in PTERMS[i]:
        e = jt + s*2*n*jx; d[e] = d.get(e, 0) + c
    return {k: v for k, v in d.items() if v}
def qint(n): return {2*(n-1-2*i): 1 for i in range(n)}
phits = []; ntried = 0
for k, JJ in KN.items():
    for norm in ("J", "[n]J"):
        for mirror in (False, True):
            for off in (0, 1, -1):
                ntried += 1; res = []
                for nn in range(1, 7):
                    idx = [nn+off+i for i in range(5)]
                    if min(idx) < 1 or max(idx) > len(JJ): continue
                    tot = {}
                    for i in range(5):
                        d = JJ[idx[i]-1]
                        p = {(-2*e if mirror else 2*e): c for e, c in d.items()}
                        if norm == "[n]J": p = mul(p, qint(idx[i]))
                        tot = addd(tot, mul(pcoef(i, nn, mirror), p))
                    res.append(len(tot) == 0)
                if res and all(res): phits.append((k, norm, mirror, off))
print("   five knots x 2 normalisations x 2 mirrors x 3 shifts = %d conventions tried" % ntried)
print("   annihilated : %s" % (phits if phits else "NOTHING"))
print("   CELL 1 -> OUTCOME %s" % ("A" if phits else "B"))
OK["CELL 1 -> B : eq (32) as printed annihilates no colored Jones we hold"] = not phits

print()
print("=" * 78)
print("T3  --  was it simply the wrong file?  is eq (32) the 6_1 operator up to a factor?")
print("=" * 78)
GS = [sp.factor(sp.expand(sp.diff(REC_M, FS[i]))) for i in range(5)]
PK = [sp.expand(a.subs(t, sp.sqrt(q))) for a in PARK]
R = [sp.cancel(GS[i]/PK[i]) for i in range(5)]
prop = all(sp.simplify(sp.cancel(R[i]/R[0]) - 1) == 0 for i in range(5))
print("   a_i(6_1 operator) / a_i(eq 32) constant in i ? : %s" % prop)
print("   (a_0 and a_4 do share factors -- that is the generic twist-knot shape, not a match)")
print("   T3 -> the wrong-file hypothesis is REFUTED.")
OK["T3  eq (32) is NOT the 6_1 operator either -- hypothesis tested and refuted"] = not prop

print()
print("=" * 78)
print("T4  --  the CLASSICAL limit, and the fourth uploaded file")
print("=" * 78)
m_, w_ = sp.symbols('m w')
eps = sp.symbols('eps')
lead = []
for a in [sp.expand(sp.diff(SURVEY, FS[i])) for i in range(4)]:
    ser = sp.series(sp.simplify(a.subs(q, 1+eps)), eps, 0, 6).removeO()
    pp = sp.Poly(sp.expand(ser), eps)
    kk = min(mo[0] for mo in pp.monoms())
    lead.append(sp.expand(sp.simplify(pp.coeff_monomial(eps**kk))))
ACL = sp.factor(sp.expand(sum(lead[j]*w_**j for j in range(4)).subs(x, m_**2)))
BRACKET = sp.expand(ACL / sp.factor((m_-1)**3*(m_+1)**3*(m_**2+1)**2) * -1)
UP = (m_**14*w_**3 + (-m_**14+2*m_**12+2*m_**10-m_**6+m_**4)*w_**2
      + (m_**10-m_**8+2*m_**4+2*m_**2-1)*w_ + 1)
same = sp.simplify(sp.expand(w_**3*UP.subs(w_, 1/w_)) - BRACKET) == 0
print("   the uploaded A_polynomial_5_2.txt is NOT a primary-source data file -- it is a")
print("   typed summary -- so it is verified rather than used.")
print("   classical limit of the VERIFIED order-3 operator, after removing the extraneous")
print("   factor (m-1)^3 (m+1)^3 (m^2+1)^2 that the q -> 1 limit of a non-commutative")
print("   A-polynomial always carries:")
print("      %s" % BRACKET)
print("   w^3 * A_uploaded(1/w) equals it exactly : %s" % same)
print("   => the uploaded file is CORRECT, written with the reciprocal longitude")
print("      convention (w <-> 1/w).  Chain: our own colored Jones -> the survey's")
print("      operator -> its classical limit -> this file.")
OK["T4  the uploaded A_polynomial_5_2.txt is verified against the operator's q->1 limit"] = same

print()
print("=" * 78)
print("CELL 2  --  are the consequences Park PRINTS from eq (32) also wrong?")
print("=" * 78)
BJ = json.load(open(os.path.join(DATA, "park_f52_blocks_w16.json")))
B = {int(k): {int(e): Fr(int(c)) for e, c in v.items()} for k, v in BJ["blocks"].items()}
NCn = {int(k): v for k, v in BJ["_counts"].items()}
def lmul(A, B_, cap):
    r = {}
    for e1, c1 in A.items():
        for e2, c2 in B_.items():
            e = e1+e2
            if e <= cap: r[e] = r.get(e, 0) + c1*c2
    return {e: c for e, c in r.items() if c}
def ladd(A, B_):
    r = dict(A)
    for e, c in B_.items():
        r[e] = r.get(e, 0) + c
        if r[e] == 0: del r[e]
    return r
def ldiv(num, den, cap):
    dl = min(den); dc = Fr(den[dl]); cur = dict(num); res = {}
    while cur:
        lo = min(cur)
        if lo-dl > cap: break
        kk = Fr(cur[lo])/dc; res[lo-dl] = res.get(lo-dl, 0)+kk
        for a, b in den.items():
            tt = lo-dl+a; cur[tt] = cur.get(tt, 0)-Fr(b)*kk
            if cur[tt] == 0: del cur[tt]
    return {e: c for e, c in res.items() if c}
def PP(*co):
    d = {}
    for e, c in co: d[e] = d.get(e, 0)+Fr(c)
    return {e: c for e, c in d.items() if c}
REL = {2: (PP((0,1),(1,1),(2,-1)), PP((0,-1),(1,-2),(2,1)), PP((1,-1),(3,1))),
       3: (PP((0,-2),(1,-1),(2,-1),(3,2),(4,1),(5,-1)),
           PP((0,2),(1,1),(2,3),(3,-1),(6,-1)), PP((2,1),(4,-1),(5,-1),(7,1)))}
CAP = min(min(B[0])+NCn[0]-1, min(B[1])+NCn[1]-1)
c2 = True
for j, (na, nb, den) in REL.items():
    pred = ldiv(ladd(lmul(na, B[0], CAP+20), lmul(nb, B[1], CAP+20)), den, CAP)
    act = B[j]; hor = min(CAP, min(act)+NCn[j]-1)
    ex = list(range(int(min(min(pred), min(act))), int(hor)+1))
    bad = [e for e in ex if pred.get(e, 0) != act.get(e, 0)]
    c2 &= not bad
    print("   Park's printed f_%d  vs  the bench's own block : %s   over q^%d..q^%d,"
          " %d coefficients" % (j, "MATCH" if not bad else "MISMATCH at q^%d" % bad[0],
                                ex[0], ex[-1], len(ex)))
print("   (the horizon is set by f_0's 16 stored coefficients, not by any disagreement)")
print("   CELL 2 -> OUTCOME %s" % ("B" if c2 else "A"))
OK["CELL 2 -> B : the printed consequences HOLD, so the computation behind them was right"] = c2

print()
print("=" * 78)
print("CONTROLS AND CELLS")
print("=" * 78)
for k, v in OK.items(): print("   %-72s %s" % (k, "PASSED" if v else "FAILED"))
print("""
THE ERRATUM, NOW LOCALISED AND FAIR.

  1.  eq (32) AS PRINTED is defective.  Memo 183 showed it fails to annihilate F^+_{m(5_2)}
      with an exactly measured defect.  CELL 1 adds an independent second witness on a
      DIFFERENT object: it annihilates no colored Jones of any of the five knots this
      bench holds, in sixty conventions.
  2.  IT IS NOT A WRONG-FILE ERROR.  T3 tested the natural hypothesis -- that the K_{-2}
      file was picked up instead of K_2 -- and refuted it.
  3.  THE COMPUTATION BEHIND THE PAPER WAS RIGHT.  CELL 2 is the part that is fair to the
      author: the f_2 and f_3 he prints on the same page, as Q(q)-combinations of f_0 and
      f_1, agree with this bench's independently computed blocks on every coefficient
      compared.  Whatever went wrong, went wrong between his computation and the printed
      operator.

WHAT IS NOW HELD THAT WAS NOT BEFORE.  A VERIFIED non-commutative A-polynomial for 5_2:
the survey's order-3 recursion, checked against this bench's own R-matrix colored Jones at
six values of n.  fetch section B'' asked for exactly this, and it arrived in a survey
rather than in a data file.

NAMED OPEN ITEM, with what was tried so the next seat does not repeat it.  Converting that
colored-Jones operator into the x-block recursion for F^+ does NOT work by the naive
ansatz.  Tried: Ahat = sum_j a_j(x,q) yhat^j with yhat: x -> qx, F^+ = sum_j f_j x^{j+1/2},
collecting powers of x, in all four q- and x-mirror orientations.  Each gives a triangular
system that determines f_2..f_5 from f_0, f_1 -- and each disagrees with the bench's known
blocks, at the first or second coefficient.  So the F_K annihilator is not literally the
colored-Jones annihilator in this convention.  NOT SOLVED, NOT CLAIMED.""")
assert all(OK.values()), OK
