#!/usr/bin/env python3
"""WHY GM's SECTION 7.4 NEAR-MISS HAPPENED AT THE POINCARE SPHERE AND NOWHERE ELSE:
the cyclotomic series C_K CONVERGES FOR HALF OF THE TWIST KNOTS AND DIVERGES FOR THE
OTHER HALF, AND THE SPLIT IS BY THE SIGN OF THE TWIST PARAMETER.

Memo 185 CELL A showed that C_{4_1}(x,q) is not a Laurent power series -- a single
monomial receives unboundedly many, unboundedly large contributions -- while
C_{3_1}(x,q) is.  Two knots, one each way, and no account of which is which.

Memo 185 addendum 1 then tested GM section 7.4 and found the C_K route reproduces the
whole false theta of Zhat_0(Poincare sphere) and misses by exactly one additive monomial.
The Poincare sphere is (-1) surgery ON THE TREFOIL.  This certificate shows that is not
incidental: the trefoil is one of the knots for which the object converges at all.

THE COMPUTATION.  Habiro's cyclotomic coefficients are solved triangularly out of the
colored Jones polynomials, GM eq (20):

    J_{K,n}(q) = sum_{m>=0} C_m(q) (q^{n+1})_m (q^{1-n})_m ,

where (q^{n+1})_m (q^{1-n})_m vanishes for m >= n, so J_{n+1} determines C_n once
C_0..C_{n-1} are known.  Every division is EXACT in Z[q,q^-1] and that is asserted at
every step, not assumed -- which is Habiro's integrality theorem, checked.

Input: the CJTwist tables, each identified BY DETERMINANT in cj_table_ingest.py (memo
186), never by filename.  The 12 MB tables are not vendored; C_0..C_12 are, in
data/cyclotomic_twist.json.

PREREGISTERED, TWO OUTCOMES.
  CELL -- is the convergence of C_K a property of the construction, or of the knot?
    A  all four knots behave the same way        -> it is the construction.
    B  they split                                -> it is the knot, and the certificate
       must then say WHAT about the knot decides it.

CONTROLS.
  C1  3_1 must come out as GM eq (24)'s C_m = q^m -- a single monomial, PRINTED IN GM.
  C2  4_1 must come out as C_m = (-1)^m q^{-m(m+1)/2}, which memo 185 derived by a
      DIFFERENT route (from GM eq (166), not from any table).  Two derivations meeting.
  C3  A ROUND TRIP, not an assertion: the extracted C_m are pushed back through GM
      eq (20) and must rebuild the table's own J_1..J_7, for all four knots.  Every
      triangular division was additionally required to be exact in Z[q,q^-1] at
      extraction time (Habiro integrality), and the round trip is what proves it here.
  C4  the divergence is CHECKED DIRECTLY, not inferred from the valuation: for each
      knot the actual contribution of index m to the single monomial x^0 q^0 of
      C_K(x,q) is computed and printed.  A valuation going to -infinity is only a
      necessary condition for divergence; cancellation could still save it, and this
      control is what rules that out.

Gate 5: exact integer arithmetic.  No fitted constant, no measured value.

Usage: python3 cyclotomic_valuation.py           (from the vendored C_m)
"""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, "..", "data", "cyclotomic_twist.json")))
PROV = D.pop("_provenance")

def mul(A, B):
    r = {}
    for e1, c1 in A.items():
        for e2, c2 in B.items(): r[e1+e2] = r.get(e1+e2, 0) + c1*c2
    return {e: c for e, c in r.items() if c}
def add(A, B, s=1):
    r = dict(A)
    for e, c in B.items():
        r[e] = r.get(e, 0) + s*c
        if r[e] == 0: del r[e]
    return r

C = {k: [dict((int(e), int(c)) for e, c in t) for t in v["C"]] for k, v in D.items()}
P = {k: v["p"] for k, v in D.items()}
ORDER = sorted(C, key=lambda k: P[k])

print("=" * 78)
print("THE CYCLOTOMIC COEFFICIENTS OF FOUR TWIST KNOTS")
print("=" * 78)
print("   source : %s" % PROV["source"])
print("   ident  : %s" % PROV["identified_by"])
print()
OK = {}
OK["C1  3_1 gives GM eq (24)'s C_m = q^m exactly, m = 0..12"] = \
    all(C["3_1"][m] == {m: 1} for m in range(13))
OK["C2  4_1 gives C_m = (-1)^m q^{-m(m+1)/2} -- memo 185's independent derivation"] = \
    all(C["4_1"][m] == {-m*(m+1)//2: (-1)**m} for m in range(13))
# C3 is a ROUND TRIP, not an assertion: rebuild J_1..J_N from the extracted C_m through
# GM eq (20) and require it to reproduce the table's own colored Jones polynomials.
def poch(n, m):
    t = {0: 1}
    for j in range(0, m):
        for e in (n+1+j, 1-n+j): t = add(t, mul(t, {e: 1}), -1)
    return t
rt = True; NJ = 0
for k in D:
    Js = [dict((int(e), int(c)) for e, c in t) for t in D[k]["J"]]
    NJ = len(Js)
    for n in range(1, NJ+1):
        acc = {}
        for m in range(0, n): acc = add(acc, mul(C[k][m], poch(n, m)))
        rt &= (acc == Js[n-1])
OK["C3  ROUND TRIP: the extracted C_m rebuild J_1..J_%d through GM eq (20), 4 knots" % NJ] = rt

VAL = {k: [min(c) if c else None for c in C[k]] for k in C}
for k in ORDER:
    print("   %-5s p = %-3d  min q-valuation of C_m, m = 0..12 :" % (k, P[k]))
    print("            %s" % VAL[k])

# ---------- the split ----------
conv = [k for k in ORDER if VAL[k][-1] > VAL[k][0]]
divg = [k for k in ORDER if VAL[k][-1] < VAL[k][0]]
print()
print("=" * 78)
print("CELL  --  is the convergence of C_K a property of the construction or the knot?")
print("=" * 78)
print("   valuation RISING  (C_K can be a power series) :", conv, "-> p =", [P[k] for k in conv])
print("   valuation FALLING (it cannot)                 :", divg, "-> p =", [P[k] for k in divg])
print("   CELL -> OUTCOME %s" % ("B" if conv and divg else "A"))
OK["CELL resolved -> B : the knot decides, not the construction"] = bool(conv and divg)
OK["the split is exactly the SIGN of the twist parameter p"] = \
    (all(P[k] > 0 for k in conv) and all(P[k] < 0 for k in divg))

# closed forms, measured on m = 0..12
f_pos = all(VAL[k][m] == m for k in conv for m in range(13))
f_neg = all(VAL[k][m] == -(2*abs(P[k]) - 1) * m*(m+1)//2 for k in divg for m in range(13))
print()
print("   measured on m = 0..12, exactly:")
print("      p > 0 :  val C_m = m                              %s"
      % ("HOLDS for p = %s" % [P[k] for k in conv] if f_pos else "FAILS"))
print("      p < 0 :  val C_m = -(2|p| - 1) * m(m+1)/2         %s"
      % ("HOLDS for p = %s" % [P[k] for k in divg] if f_neg else "FAILS"))
OK["the two closed forms hold exactly on every m = 0..12"] = (f_pos and f_neg)

# ---------- C4 : the direct divergence check ----------
def pochx(m, QLO, QHI):
    t = {(0, 0): 1}
    for j in range(1, m+1):
        for d in (1, -1):
            nt = {}
            for (a, b), c in t.items():
                for (da, db), cc in (((0, 0), 1), ((d, j), -1)):
                    bb = b + db
                    if bb < QLO or bb > QHI: continue
                    kk = (a+da, bb); nt[kk] = nt.get(kk, 0) + c*cc
            t = {kk: c for kk, c in nt.items() if c}
    return t
print()
print("=" * 78)
print("C4  --  the DIRECT check: what index m contributes to the single monomial x^0 q^0")
print("=" * 78)
for k in ORDER:
    run = []; s = 0
    for m in range(0, 13):
        need = [-e for e in C[k][m]]
        hi = max(need) if need else 0
        t = pochx(m, 0, max(hi, 0))
        v = sum(cc * t.get((0, -e), 0) for e, cc in C[k][m].items())
        s += v; run.append(v)
    print("   %-5s p = %-3d  contributions : %s" % (k, P[k], run))
    print("            partial sums   : %s" % [sum(run[:i+1]) for i in range(len(run))])
    grew = abs(run[-1]) > 1000
    OK["C4  %-5s : %s" % (k, "contributions blow up" if P[k] < 0 else
                          "only finitely many indices contribute")] = \
        (grew if P[k] < 0 else all(v == 0 for v in run[1:]))

print()
print("=" * 78)
print("CONTROLS AND CELLS")
print("=" * 78)
for k, v in OK.items(): print("   %-72s %s" % (k, "PASSED" if v else "FAILED"))
print("""
WHAT THIS EXPLAINS.

GM section 7.4 reports that feeding C_K into the surgery formula "gets the right answer
for the -1 surgery (the case of the Poincare sphere), but not for other surgeries."  The
Poincare sphere is (-1) surgery ON THE TREFOIL.  The trefoil has p = +1, and p > 0 is
exactly the half of this family for which C_K is a genuine power series.  The near-miss
did not happen at a random place: it happened at one of the only places where the object
being fed into the formula exists at all.  (Memo 185 addendum 1 then showed that even
there it is off by one additive monomial.)

It also SHARPENS memo 185 CELL A.  That cell resolved to B on 4_1, and the wording could
be read as "C_K never converges".  It is not that.  Convergence fails for p < 0 and holds
for p > 0, and when it fails the rate is quantitative: the valuation falls like
-(2|p| - 1) m(m+1)/2, so it fails FASTER the more the knot is twisted.

WHAT IT DOES NOT SAY.  For p > 0 the naive route is not blocked BY CONVERGENCE.  It is
still blocked -- memo 185 CELL B showed C_K is not f_K up to any monomial on 3_1 -- but
that cell has been run on ONE positive knot, because f_K is known there in closed form
(GM Thm 1.3) and is not known for 9_2.  Stated so it is not overread.

A FALSIFIABLE PREDICTION, BANKED BEFORE THE FILE ARRIVES.  5_2 = K_2 has p = +2.  The
prediction is  val C_m(5_2) = m  for every m, with C_K(5_2) therefore a genuine power
series.  6_1 = K_{-2} is its opposite-sign partner and gives -3 m(m+1)/2.  CJTwist.2 is
the file memo 186 F186-1 asks for and did not receive; when it arrives this is decided in
one run.  Support for the prediction as it stands: two knots each side, m = 0..12.""")
assert all(OK.values()), OK
