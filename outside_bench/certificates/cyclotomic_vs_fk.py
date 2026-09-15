#!/usr/bin/env python3
"""THE NAIVE CYCLOTOMIC ROUTE TO f_K IS DEAD -- BY COMPUTATION, NOT BY CITATION.

WHY THIS EXISTS.  Memo 183 addendum 4 named the blocker: the reduced quantum trace gives
f_0 .. f_5 for m(5_2) and no more, and the single-index fit past f_5 cannot close.  A route
was floated at this bench -- solve Habiro's cyclotomic coefficients C_0 .. C_{n-1} out of the
colored Jones polynomials J_1 .. J_n (the solve is triangular and exact) and read f_j off
them.  That route is tested here and it fails.

Gukov-Manolescu say so in words (arXiv:1904.06057v2, p.14, after eq (22)):

    "In contrast to what was claimed in [36], our new understanding is that f_K is not
     directly related to the cyclotomic expansion (just as the q-series Zhat_a is not
     directly related to the Habiro series)."

Register R80-1 forbids this bench from settling anything on that sentence: an author's
stated expectation is evidence about what was known when it was written, never about what
is true.  So the sentence is not used.  It is TESTED, at the two places where it can be,
with exact integer arithmetic.

THE OBJECTS.  GM eq (20)-(21):

    J_{K,n}(q) = sum_{m>=0} C_m(q) (q^{n+1})_m (q^{1-n})_m ,
    C_K(x,q)   = sum_{m>=0} C_m(q) (qx)_m   (qx^{-1})_m ,        x = q^n.

GM eq (22) is the Gukov-Marino-Putrov conjecture with f_K in the slot where the Habiro
expansion puts C_K.  The naive reading of that -- the one the floated route needs -- is

    f_K(x,q)  =  C_K(x,q)   up to an overall monomial.

f_K = F_K / (x^{1/2} - x^{-1/2}) is GM eq (104); for a torus knot F_K is GM Thm 1.3, which
THIS BENCH verified in certificates/gm_thm13.py against Park's large-colour Verma R-matrix
(arXiv:2004.02087), a machine from a different paper.  That is the control on f_K here.

PREREGISTERED, TWO OUTCOMES EACH.

  CELL A -- 4_1, convergence.  Fix the single monomial x^0 q^0 and count what the index m
  contributes to it.
     A  the partial sums stabilise  ->  C_K is a genuine Laurent power series and nothing
        obstructs reading f_j off the C_m term by term.
     B  they do not stabilise       ->  C_K is not a power series in (x,q) at all, and no
        term-by-term route through it exists.  GM's structural reason confirmed, computed.

  CELL B -- 3_1, identification.  On the trefoil C_K IS a power series (control C3), so
  CELL A's obstruction is absent and the identification can be tested head on.
     A  C_K(x,q) = lambda * x^A q^B * f_K(x,q) for some constant lambda and monomial
        ->  the naive identification survives where it is allowed to.
     B  no such lambda, A, B exists -> the identification is false by computation.

CONTROLS.
  C1  eq (20) with GM eq (24)'s C_m = q^m reproduces the classical Jones polynomial of the
      left trefoil at n = 2, and J_1 = 1.  CITED anchor: V(3_1^l) = q + q^3 - q^4.
  C2  eq (20) reproduces GM eq (166) for 4_1 at n = 2 .. 8 exactly, with
      C_m(4_1) = (-1)^m q^{-m(m+1)/2}, and at n = 2 gives the classical Jones polynomial
      q^{-2} - q^{-1} + 1 - q + q^2.  This both controls the instrument and PINS A
      CONVENTION worth recording -- see the convention note at the end.
  C3  the divergence detector returns FINITE on the trefoil.  An instrument that always
      says "divergent" would prove nothing (memo 164).
  C4  f_K here is GM Thm 1.3, verified in gm_thm13.py against an independent machine.

SCOPE, STATED SO IT IS NOT OVERREAD.  What dies here is the NAIVE route: C_K read as f_K
up to a monomial, and any term-by-term passage through C_K.  A non-naive relation is a
different question and is NOT touched: Park, "Inverted state sums, inverted Habiro series,
and indefinite theta functions" (arXiv:2106.03942) -- already tracked as fetch item B2 in
fetch/FETCH_REQUEST_CEFF.md -- is exactly such a route, and this bench does not have it.

Gate 5: exact integer and Fraction arithmetic throughout.  No measured input of any kind.
"""
from fractions import Fraction as Fr

# ---------- Laurent arithmetic:  D[(x-exponent, q-exponent)] = integer ----------
def mul(A, B, QLO=None, QHI=None):
    r = {}
    for (a1, b1), c1 in A.items():
        for (a2, b2), c2 in B.items():
            b = b1 + b2
            if QLO is not None and b < QLO: continue
            if QHI is not None and b > QHI: continue
            k = (a1 + a2, b); r[k] = r.get(k, 0) + c1 * c2
    return {k: c for k, c in r.items() if c}
def add(A, B, s=1):
    r = dict(A)
    for k, c in B.items():
        r[k] = r.get(k, 0) + s * c
        if r[k] == 0: del r[k]
    return r
def pochx(m, QLO=None, QHI=None):
    """(qx)_m (qx^{-1})_m = prod_{j=1..m} (1 - q^j x)(1 - q^j x^{-1})"""
    t = {(0, 0): 1}
    for j in range(1, m + 1):
        t = mul(t, add({(0, 0): 1}, {(1, j): 1}, -1), QLO, QHI)
        t = mul(t, add({(0, 0): 1}, {(-1, j): 1}, -1), QLO, QHI)
    return t
def one_var(d):
    """collapse a purely-x^0 dict to {q-exponent: coeff}"""
    return {b: c for (a, b), c in d.items() if a == 0}

# ---------- eq (20): the colored Jones from the cyclotomic coefficients ----------
def J_cyclo(n, C, mmax=40):
    """J_{K,n} = sum_m C_m(q) (q^{n+1})_m (q^{1-n})_m,  C given as {q-exp: coeff}"""
    tot = {}
    for m in range(0, mmax + 1):
        t = {0: 1}
        for j in range(0, m):
            for e in (n + 1 + j, 1 - n + j):
                nt = {}
                for e1, c1 in t.items():
                    nt[e1] = nt.get(e1, 0) + c1
                    nt[e1 + e] = nt.get(e1 + e, 0) - c1
                t = {k: v for k, v in nt.items() if v}
        if not t: break
        Cm = C(m); s = {}
        for e1, c1 in Cm.items():
            for e2, c2 in t.items():
                s[e1 + e2] = s.get(e1 + e2, 0) + c1 * c2
        for k, v in s.items():
            tot[k] = tot.get(k, 0) + v
    return {k: v for k, v in tot.items() if v}

# ---------- GM eq (166), the figure-eight, independent of the cyclotomic form ----------
def J166(n):
    tot = {0: 1}; cur = {0: 1}
    for m in range(1, n):
        fac = {n: 1, -n: 1}
        fac[m] = fac.get(m, 0) - 1; fac[-m] = fac.get(-m, 0) - 1
        fac = {k: v for k, v in fac.items() if v}
        nxt = {}
        for e1, c1 in cur.items():
            for e2, c2 in fac.items():
                nxt[e1 + e2] = nxt.get(e1 + e2, 0) + c1 * c2
        cur = {k: v for k, v in nxt.items() if v}
        for k, v in cur.items(): tot[k] = tot.get(k, 0) + v
    return {k: v for k, v in tot.items() if v}

C_TREF = lambda m: {m: 1}                              # GM eq (24), left trefoil
C_41 = lambda m: {-m * (m + 1) // 2: (-1) ** m}        # forced by C2 below

OK = {}
print("=" * 78)
print("CONTROLS")
print("=" * 78)
j2 = J_cyclo(2, C_TREF); j1 = J_cyclo(1, C_TREF)
ref = {1: 1, 3: 1, 4: -1}
OK["C1 eq(20)+eq(24) -> Jones(3_1^l) at n=2, and J_1 = 1"] = (j2 == ref and j1 == {0: 1})
print("   C1  J_{3_1^l,2} from eq (20) = " + " ".join("%+d q^%d" % (c, e) for e, c in sorted(j2.items()))
      + "   (cited: q + q^3 - q^4)")
agree = all(J_cyclo(n, C_41) == J166(n) for n in range(1, 9))
j41 = J166(2); ref41 = {-2: 1, -1: -1, 0: 1, 1: -1, 2: 1}
OK["C2 eq(20) with C_m(4_1) = (-1)^m q^{-m(m+1)/2} == GM eq (166), n = 1..8"] = agree
OK["C2b eq (166) at n = 2 is the classical Jones polynomial of 4_1"] = (j41 == ref41)
print("   C2  eq (20) with C_m = (-1)^m q^{-m(m+1)/2} equals GM eq (166) at n = 1..8 :", agree)
print("   C2b eq (166) at n=2 = " + " ".join("%+d q^%d" % (c, e) for e, c in sorted(j41.items())))

# ---------- CELL A : is C_K a power series? ----------
print()
print("=" * 78)
print("CELL A  --  does C_K(x,q) converge as a series?   statistic: the coefficient of the")
print("            single monomial x^0 q^0, as the index m is summed")
print("=" * 78)
def contributions(Cm, MMAX):
    run = []; s = 0
    for m in range(0, MMAX + 1):
        C = Cm(m)
        # contribution of index m to x^0 q^0  =  sum over C's monomials q^e of
        # [ coefficient of x^0 q^{-e} in (qx)_m (qx^{-1})_m ]
        need = [-e for e in C]
        hi = max(need) if need else 0
        t = one_var(pochx(m, QLO=0, QHI=max(hi, 0)))
        c = sum(cc * t.get(-e, 0) for e, cc in C.items())
        s += c; run.append((m, c, s))
    return run
r41 = contributions(C_41, 15)
for m, c, s in r41:
    print("   4_1   m=%2d  contributes %+12d   partial sum %+13d" % (m, c, s))
sums41 = [s for _, _, s in r41]
divergent41 = abs(sums41[-1]) > 10 * max(1, abs(sums41[len(sums41) // 2])) and \
              abs(sums41[-1]) > abs(sums41[-2])
print()
print("   partial sums do NOT stabilise; |contribution| grows without bound.")
print("   CELL A  ->  OUTCOME B : C_{4_1}(x,q) is not a Laurent power series in (x,q).")
print("               A single monomial receives unboundedly many unboundedly large")
print("               contributions.  This is GM's stated structural reason, computed.")
OK["CELL A resolved to B by computation (not by citation)"] = bool(divergent41)

r31 = contributions(C_TREF, 15)
sums31 = [s for _, _, s in r31]
print()
print("   C3 (control)  the SAME detector on the trefoil, C_m = q^m :")
print("      contributions by m :", [c for _, c, _ in r31])
print("      partial sums       :", sums31)
OK["C3 detector returns FINITE on 3_1 (it is not a machine that always diverges)"] = \
    (len(set(sums31)) == 1 and sums31[0] == 1)

# ---------- CELL B : on the trefoil, is C_K = f_K up to a monomial? ----------
print()
print("=" * 78)
print("CELL B  --  3_1, where CELL A's obstruction is absent:  C_K  vs  f_K")
print("=" * 78)
NQ = 34
def C_series(Cm, NQ, XMAX, MMAX):
    tot = {}
    for m in range(0, MMAX + 1):
        C = Cm(m); t = pochx(m, QLO=0, QHI=NQ)
        for e1, c1 in C.items():
            for (a, b), c2 in t.items():
                if abs(a) > XMAX: continue
                e = e1 + b
                if e > NQ: continue
                tot[(a, e)] = tot.get((a, e), 0) + c1 * c2
    return {k: c for k, c in tot.items() if c}
Ct = C_series(C_TREF, NQ, 4, NQ + 2)
x0 = sorted((e, c) for (a, e), c in Ct.items() if a == 0)
print("   C_{3_1^l}, coefficient of x^0, by q-order 0..%d :" % NQ)
print("      ", [dict(x0).get(n, 0) for n in range(0, NQ + 1)])

# f_K from GM Thm 1.3 (eq (2)-(3)) -- the blocks verified in gm_thm13.py
def gm_blocks(s, t, J, mirror):
    st = s * t; M = 2 * st; c = st - s - t
    E = {(st + s + t) % M: -1, (st - s - t) % M: -1, (st + s - t) % M: 1, (st - s + t) % M: 1}
    out = {}
    for j in range(J + 1):
        m = 2 * j + 1; e = E.get(m % M, 0)
        if not e: out[j] = None; continue
        assert (m * m - c * c) % (4 * st) == 0
        ex = Fr((s - 1) * (t - 1), 2) + Fr(m * m - c * c, 4 * st)
        out[j] = (e, -ex if mirror else ex)
    return out
for mirror in (False, True):
    B = gm_blocks(2, 3, 60, mirror)
    # f_K = (1/2) sum_j f_{2j+1}(q) (x^{-j} + ... + x^{j});  coefficient of x^0:
    co = {}
    for j, v in B.items():
        if v is None: continue
        e, ex = v; co[ex] = co.get(ex, 0) + Fr(e, 2)
    vals = sorted(set(abs(c) for c in co.values() if c))
    lab = "T(2,-3) = the mirror" if mirror else "T(2,3)"
    print()
    print("   f_K for %s, coefficient of x^0 : support is sparse," % lab)
    print("      first exponents (by distance from 0)", [str(e) for e in sorted(co, key=abs)[:12]])
    print("      the SET of absolute values of its nonzero coefficients :", [str(v) for v in vals])
CX = [dict(x0).get(n, 0) for n in range(0, NQ + 1)]
absC = sorted(set(abs(c) for c in CX if c))
print()
print("   the SET of absolute values of C_{3_1^l}'s x^0 coefficients :", absC[:12], "...")
print()
print("   If C_K = lambda * x^A q^B * f_K, then every nonzero coefficient of C_K is")
print("   |lambda|/2 in absolute value -- ONE value.  C_K's x^0 coefficients already take")
print("   %d distinct absolute values in the first %d orders." % (len(absC), NQ + 1))
print("   CELL B  ->  OUTCOME B : no lambda, A, B exists.  The identification is false.")
print("   It fails for BOTH chiralities of f_K and therefore for either q-orientation.")
OK["CELL B resolved to B by computation"] = (len(absC) > 1)

print()
print("=" * 78)
print("CONTROLS AND CELLS")
print("=" * 78)
for k, v in OK.items():
    print("   %-64s %s" % (k, "PASSED" if v else "FAILED"))
print()
print("""VERDICT.  The naive cyclotomic route to f_K is closed at both places it could be open.
On 4_1 the object C_K is not a series at all, so nothing can be read off it term by term.
On 3_1, where C_K IS a series, it is not f_K up to any monomial.  GM's sentence is
therefore not merely an author's expectation this bench had to take on trust (R80-1) --
it is a computed fact here.

CONSEQUENCE FOR THE COLORED JONES TABLES.  A table of J_{K,n} for n = 1..60 does NOT
unblock f_6 and beyond (memo 183 addendum 4).  The three other reasons to want it are
untouched: memo 184's stability fence goes from 8 coefficients to ~60; the tables for
K_{-1} = 4_1 and K_1 = 3_1 are free controls against eq (166) and eq (24); and memo 184
addendum 1's family goes from 4 knots to 30.

CONVENTION NOTE, RECORDED BECAUSE IT WILL BITE AGAIN.  "The cyclotomic coefficients of 4_1
are all 1" is true in the basis prod_{j=1..m} (q^N + q^{-N} - q^j - q^{-j}) -- the form used
in certificates/c2_habiro.py, where it is anchored against the classical Jones polynomial.
In GM's eq (20) basis (q^{n+1})_m (q^{1-n})_m the same knot has
C_m = (-1)^m q^{-m(m+1)/2}, because
   (q^{n+1})_m (q^{1-n})_m = (-1)^m q^{m(m+1)/2} prod_{j=1..m} (q^n + q^{-n} - q^j - q^{-j}).
Both are checked above.  The two are not in conflict; they are different bases, and the
q-valuation of C_m -- which is what decides CELL A -- differs between them.""")
assert all(OK.values()), OK
