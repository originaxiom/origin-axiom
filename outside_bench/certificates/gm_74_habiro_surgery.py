#!/usr/bin/env python3
"""GM SECTION 7.4 TESTED: THE CYCLOTOMIC SERIES IN THE SURGERY FORMULA, AT TWO SLOPES.

Memo 185 closed the naive identification f_K = C_K.  It left one sentence of GM untested,
and named it as follow-up F185-1.  GM, arXiv:1904.06057v2, p. 55, section 7.4:

    "We could try to apply the Dehn surgery formula (106) to C_K(x,q) instead of f_K(x,q),
     and see if we recover the invariants Zhat_a(q) of the surgeries.  Interestingly, we get
     the right answer for the -1 surgery (the case of the Poincare sphere), but not for
     other surgeries."

By register R80-1 that sentence is evidence about what was known when it was written and
never about what is true.  It is tested here, at both slopes it speaks about, with exact
Fraction arithmetic, and the answer is SHARPER THAN THE SENTENCE.

THE MACHINE.  GM Thm 1.2 with eq (1):

    Zhat_a(S^3_{p/r}(K)) = eps q^d  L^{(a)}_{p/r} [ (x^{1/2r} - x^{-1/2r}) F_K ],
    L^{(a)}_{p/r} : x^u q^v  ->  q^{-u^2 r/p + v}   iff  r u - a in pZ,  else 0.

The Habiro variant GM describe just above eq (22) puts C_K where f_K = F_K/(x^{1/2}-x^{-1/2})
sits, i.e. transforms  (x^{1/2} - x^{-1/2})(x^{1/2r} - x^{-1/2r}) C_K  instead.  Both routes
here go through the SAME transform code; only the transformed series differs.

INPUTS, EACH INDEPENDENTLY ANCHORED.
  F_{3_1^l} = F_{T(2,-3)} from GM Thm 1.3, verified at this bench in gm_thm13.py against
              Park's large-colour Verma R-matrix (arXiv:2004.02087) -- a different paper's
              machine.
  C_{3_1^l} = sum_m q^m (qx)_m (qx^{-1})_m, GM eq (24), whose eq (20) form is checked
              against the classical Jones polynomial in cyclotomic_vs_fk.py (control C1).

ANCHORS (these are what make the negatives below mean something).
  A1  p/r = -1 : the f_K route must give GM's own printed Zhat_0(Poincare sphere),
      eq (26)-(28):  q^{-3/2}(2 - A(q)),  A(q) = sum_n chi_+(n) q^{(n^2-1)/120}.
  A2  p/r = -1/2 : the f_K route must give Park's Table 4 line,
      Zhat(S^3_{-1/2}(m(3_1))) = Zhat(Sigma(2,3,11)) = q^{-3/2}(1 - q - q^9 + q^14 - q^19
      + q^26 + q^50 - O(q^61)) -- a second paper, printed independently.

PREREGISTERED, TWO OUTCOMES AT EACH SLOPE.
  A  the C_K route equals the f_K route up to an overall MULTIPLICATIVE monomial (which is
     all the freedom Zhat has) -> the cyclotomic series may be substituted at that slope.
  B  it does not -> it may not, and the defect is reported exactly.

Gate 5: exact integer and Fraction arithmetic.  No measured value anywhere.
"""
from fractions import Fraction as Fr

NQ = 120          # q-order cutoff for the cyclotomic series
HI = 120          # cutoff on the transformed exponent

# ---------- Laurent arithmetic in (x-exponent, q-exponent) ----------
def mul(A, B, QHI):
    r = {}
    for (a1, b1), c1 in A.items():
        for (a2, b2), c2 in B.items():
            b = b1 + b2
            if b > QHI: continue
            k = (a1 + a2, b); r[k] = r.get(k, 0) + c1 * c2
    return {k: c for k, c in r.items() if c}
def addd(A, B, s=1):
    r = dict(A)
    for k, c in B.items():
        r[k] = r.get(k, 0) + s * c
        if r[k] == 0: del r[k]
    return r

def C_trefoil(NQ):
    """GM eq (21) with eq (24)'s C_m = q^m.  Terminates: term m starts at q^m."""
    tot = {}
    for m in range(0, NQ + 1):
        t = {(0, m): 1}
        for j in range(1, m + 1):
            t = mul(t, addd({(0, 0): 1}, {(1, j): 1}, -1), NQ)
            t = mul(t, addd({(0, 0): 1}, {(-1, j): 1}, -1), NQ)
        if not t: break
        tot = addd(tot, t)
    return tot

def F_blocks(J):
    """GM Thm 1.3 eq (2)-(3) for the mirror T(2,-3) = the left trefoil.
       returns {m odd (both signs): (coefficient, q-exponent)}"""
    s, t = 2, 3; st = s * t; M = 2 * st; c = st - s - t
    E = {(st+s+t) % M: -1, (st-s-t) % M: -1, (st+s-t) % M: 1, (st-s+t) % M: 1}
    out = {}
    for j in range(J + 1):
        m = 2 * j + 1; e = E.get(m % M, 0)
        if not e: continue
        assert (m*m - c*c) % (4*st) == 0
        ex = -(Fr((s-1)*(t-1), 2) + Fr(m*m - c*c, 4*st))
        out[m] = (e, ex); out[-m] = (-e, ex)      # F_{-m} = -F_m
    return out

def laplace(terms, p, r, a, HI):
    """GM eq (1).  terms: iterable of (u, v, coeff) with u, v Fractions."""
    out = {}
    for u, v, c in terms:
        if ((r * u - a) / p).denominator != 1: continue      # r u - a in p Z
        E = -u * u * Fr(r, p) + v
        if E > HI: continue
        out[E] = out.get(E, 0) + c
    return {k: c for k, c in out.items() if c}

C = C_trefoil(NQ)
FT = F_blocks(400)

def route_f(r):
    half = Fr(1, 2 * r); T = []
    for m, (c, ex) in FT.items():
        T.append((Fr(m, 2) + half, ex, c)); T.append((Fr(m, 2) - half, ex, -c))
    return T
def route_C(r):
    half = Fr(1, 2 * r); T = []
    for (xe, qe), c in C.items():
        for s1 in (Fr(1, 2), Fr(-1, 2)):
            for s2 in (half, -half):
                sg = (1 if s1 > 0 else -1) * (1 if s2 > 0 else -1)
                T.append((xe + s1 + s2, Fr(qe), sg * c))
    return T

# ---------- the two printed anchors ----------
def A_series(MAX):
    """GM eq (27)-(28)"""
    d = {}; n = 1
    while (n*n - 1) // 120 <= MAX + 2:
        rr = n % 60
        ch = 1 if rr in (1, 11, 19, 29) else (-1 if rr in (31, 41, 49, 59) else 0)
        if ch and (n*n - 1) % 120 == 0:
            d[(n*n - 1)//120] = d.get((n*n - 1)//120, 0) + ch
        n += 1
    return d
ANCH = {}
_A = A_series(HI)
ANCH[1] = {0: 2}
for e, c in _A.items(): ANCH[1][e] = ANCH[1].get(e, 0) - c        # 2 - A(q)
ANCH[1] = {k: v for k, v in ANCH[1].items() if v}
ANCH[2] = {0: 1, 1: -1, 9: -1, 14: 1, 19: -1, 26: 1, 50: 1}       # Park, Table 4
ANCH_NAME = {1: "GM eq (26)-(28):  Zhat_0(Poincare) = q^{-3/2}(2 - A(q))",
             2: "Park, Table 4:    Zhat(Sigma(2,3,11)) = q^{-3/2}(1 - q - q^9 + q^14"
                " - q^19 + q^26 + q^50)"}
ANCH_HOR = {1: HI, 2: 51}

def normalise(d):
    """strip the overall multiplicative monomial: shift so the lowest exponent is 0,
       and divide by the coefficient there."""
    if not d: return {}, None, None
    lo = min(d); c0 = Fr(d[lo])
    return {k - lo: Fr(v) / c0 for k, v in d.items()}, lo, c0

OK = {}
print("=" * 78)
print("ANCHORS -- the f_K route against two independently printed series")
print("=" * 78)
LF = {}
for r in (1, 2):
    a = Fr(1, 2) if r == 2 else Fr(0)      # r u - a in pZ = Z ; r=2 puts u in (1/4)Z
    Lf = laplace(route_f(r), -1, r, a, HI); LF[r] = Lf
    n, lo, c0 = normalise(Lf)
    ref = ANCH[r]; hor = ANCH_HOR[r]
    good = all(n.get(Fr(e), 0) == Fr(v) for e, v in ref.items() if e <= hor) and \
           all(v == 0 for e, v in n.items() if e <= hor and e.denominator == 1
               and int(e) not in ref)
    print("   p/r = -1/%d : lowest exponent q^%s, coefficient %s" % (r, lo, c0))
    print("      %s" % ANCH_NAME[r])
    print("      every printed term reproduced, and every zero between them, to q^%s : %s"
          % (hor, "PASSED" if good else "FAILED"))
    OK["A%d  f_K route == the printed Zhat  (p/r = -1/%d)" % (r, r)] = good

print()
print("=" * 78)
print("THE CELLS -- the SAME transform, fed C_K instead of f_K")
print("=" * 78)
for r in (1, 2):
    a = Fr(1, 2) if r == 2 else Fr(0)
    Lc = laplace(route_C(r), -1, r, a, HI); Lf = LF[r]
    nf, _, _ = normalise(Lf); nc, _, _ = normalise(Lc)
    equal = all(nf.get(k, 0) == nc.get(k, 0) for k in set(nf) | set(nc)
                if k <= Fr(min(ANCH_HOR[r], 55)))
    diff = {k: Lf.get(k, 0) - Lc.get(k, 0) for k in set(Lf) | set(Lc)}
    diff = {k: v for k, v in diff.items() if v}
    ks = sorted(set(Lf) | set(Lc)); ks = [k for k in ks if k <= Fr(201, 8) + 1]
    print("   p/r = -1/%d" % r)
    print("      f_K route : %s" % [Lf.get(k, 0) for k in ks])
    print("      C_K route : %s" % [Lc.get(k, 0) for k in ks])
    print("      f - C, every nonzero term to q^%d : %d term(s)%s"
          % (HI, len(diff), (" -> " + ", ".join("%+d q^{%s}" % (v, k)
             for k, v in sorted(diff.items())[:6])) if len(diff) <= 6 else ""))
    print("      CELL -> OUTCOME %s" % ("A" if equal else "B"))
    OK["CELL r=%d resolved (A = substitutable, B = not) -> B" % r] = not equal
    if r == 1:
        OK["r=1 defect is EXACTLY ONE additive monomial"] = (len(diff) == 1)
    if r == 2:
        big = max(abs(v) for v in Lc.values())
        OK["r=2 C_K route diverges from a sparse false theta (max |coeff| > 1000)"] = big > 1000
        print("      the f_K route is a sparse false theta with all coefficients +-2;")
        print("      the C_K route is dense, |coefficient| reaching %d by q^%s."
              % (big, max(Lc, key=lambda k: abs(Lc[k]))))

print()
print("=" * 78)
print("CONTROLS AND CELLS")
print("=" * 78)
for k, v in OK.items():
    print("   %-64s %s" % (k, "PASSED" if v else "FAILED"))
print("""
VERDICT, sharper than the sentence it tests.

  p/r = -1 (Poincare sphere).  GM's "we get the right answer" is nearly right and not
  quite.  The C_K route reproduces THE ENTIRE FALSE THETA -- every coefficient of A(q)
  to q^120 -- and differs from the true Zhat_0 by EXACTLY ONE ADDITIVE MONOMIAL: it
  gives 1 - A(q) where the invariant is 2 - A(q).  Since Zhat carries only a
  MULTIPLICATIVE monomial ambiguity, that is a difference, not a normalisation.  The
  missing term is the u = 0, v = -1 contribution, which C_K cannot supply because C_K
  has no negative powers of q.

  p/r = -1/2 (Sigma(2,3,11)).  GM's "but not for other surgeries" is understated.  It is
  not a near miss: the f_K route is the sparse false theta with all coefficients +-2 that
  Park prints, and the C_K route is dense, its coefficients reaching six figures inside
  the same window.

  A SECOND THING FALLS OUT, and it is worth as much as the cells.  park_table3_repaired.py
  already ran GM Thm 1.2 end to end against Park's printed Table 3, but every row of that
  test starts from the 5_2 blocks.  A2 reaches Park's Table 4 line for Zhat(Sigma(2,3,11))
  -- the very target memo 183's erratum work is measured against -- FROM THE TREFOIL,
  through GM Thm 1.3, with no part of Park's 5_2 machinery involved anywhere.  Park states
  the underlying identity himself (Zhat(S^3_{-1}(m(5_2))) = Zhat(S^3_{-1/2}(m(3_1))) =
  Zhat(Sigma(2,3,11))); by R80-1 that is his statement, and it is now a computation here.
  The erratum's target therefore no longer rests on a single paper.""")
assert all(OK.values()), OK
