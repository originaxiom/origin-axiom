#!/usr/bin/env python3
"""THE PREDICTION BANKED IN MEMO 185 ADDENDUM 2 IS TESTED, AND HOLDS -- without the file
that was supposed to decide it.

Addendum 2 measured, on four twist knots whose colored Jones tables the owner supplied:

    p > 0 :  val C_m = m
    p < 0 :  val C_m = -(2|p| - 1) m(m+1)/2

and banked a falsifiable consequence BEFORE any further data arrived:

    "5_2 = K_2 has p = +2.  The prediction is val C_m(5_2) = m for every m, and C_K(5_2)
     a genuine power series.  CJTwist.2 is the file memo 186 F186-1 asks for and did not
     receive; when it arrives this is decided in one run."

CJTwist.2 still has not arrived.  It is decided here anyway, from a DIFFERENT ROUTE that
touches no table at all: the colored Jones of 5_2 is computed at this bench, by the
R-matrix state sum of certificates/park_rmatrix_check.py, on Park's braid word
beta_2 = sigma_2^{-3} sigma_1^{-1} sigma_2 sigma_1^{-1} (three strands) -- the same word
certificates/park_large_color.py used to reproduce every block Park prints.  Habiro's
C_m are then solved triangularly out of J_1..J_9 through GM eq (20).

PREREGISTERED (the prediction is already in the record; this only resolves it).
  A  val C_m(5_2) = m for every m computed  ->  addendum 2's law survives its first test
     on a knot it was not fitted to.
  B  it does not                            ->  the law is refuted and addendum 2 must be
     marked SUPERSEDED.

CONTROLS.
  C1  3_1 through the SAME machine and the SAME extraction must give GM eq (24)'s printed
      C_m = q^m -- a single monomial -- for every m = 0..8.
  C2  CHIRALITY, which is the one thing that could invert the answer.  3_1's J_2 and J_3
      out of this machine must equal the CJTwist table's own J_2 and J_3 for K_1, term
      for term.  That is what ties this machine's convention to Garoufalidis-Sun's K_p
      convention, and so what makes "5_2 = K_2, p = +2" the correct reading rather than
      its mirror.  Without C2 the cell would be meaningless.
  C3  ROUND TRIP: the extracted C_m rebuild J_1..J_9 through GM eq (20), both knots.
  C4  det(5_2) = |J_2(-1)| = 7, so the braid closure really is 5_2.

Gate 5: exact integer arithmetic.  No fitted constant, no measured value.
"""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, "..", "data", "cyclotomic_52.json")))
C = {k: [dict((int(e), int(c)) for e, c in t) for t in v["C"]] for k, v in D.items()}
J = {k: [dict((int(e), int(c)) for e, c in t) for t in v["J"]] for k, v in D.items()}
NM = len(C["5_2"])

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
def poch(n, m):
    t = {0: 1}
    for j in range(0, m):
        for e in (n+1+j, 1-n+j): t = add(t, mul(t, {e: 1}), -1)
    return t

OK = {}
print("=" * 78)
print("THE MACHINE AND ITS CONVENTION")
print("=" * 78)
for k in ("3_1", "5_2"):
    print("   %-5s braid %s on %d strands" % (k, D[k]["word"], D[k]["strands"]))
# C2 -- chirality, tied to the table
TAB = {2: {1: 1, 3: 1, 4: -1},
       3: {2: 1, 5: 1, 7: -1, 8: 1, 9: -1, 10: -1, 11: 1}}
c2 = all(J["3_1"][n-1] == TAB[n] for n in (2, 3))
print("   C2  3_1 out of this machine, J_2 = %s"
      % " ".join("%+d q^%d" % (c, e) for e, c in sorted(J["3_1"][1].items())))
print("       CJTwist table for K_1, J_2 = +1 q^1 +1 q^3 -1 q^4   (and J_3 also compared)")
OK["C2  chirality: this machine's 3_1 == the table's K_1 at J_2 and J_3"] = c2
det = abs(sum(c * (-1)**e for e, c in J["5_2"][1].items()))
print("   C4  det(5_2) = |J_2(-1)| = %d" % det)
OK["C4  the braid closure has determinant 7, so it is 5_2"] = (det == 7)
OK["C1  3_1 gives GM eq (24)'s printed C_m = q^m, m = 0..%d" % (NM-1)] = \
    all(C["3_1"][m] == {m: 1} for m in range(NM))
rt = True
for k in C:
    for n in range(1, NM+1):
        acc = {}
        for m in range(0, n): acc = add(acc, mul(C[k][m], poch(n, m)))
        rt &= (acc == J[k][n-1])
OK["C3  ROUND TRIP: the C_m rebuild J_1..J_%d, both knots" % NM] = rt

print()
print("=" * 78)
print("THE CELL  --  memo 185 addendum 2's prediction:  val C_m(5_2) = m")
print("=" * 78)
val = [min(c) for c in C["5_2"]]
print("   measured val C_m(5_2), m = 0..%d : %s" % (NM-1, val))
print("   predicted                        : %s" % list(range(NM)))
hit = (val == list(range(NM)))
print("   CELL -> OUTCOME %s" % ("A -- the prediction HOLDS" if hit else "B -- REFUTED"))
OK["CELL: val C_m(5_2) = m on every m computed"] = hit

nt = [len(c) for c in C["5_2"]]
pos = [all(v == 1 for v in c.values()) for c in C["5_2"]]
print()
print("   incidentally, and recorded so it is not banked by someone later:")
print("      number of nonzero terms in C_m(5_2) : %s" % nt)
print("      every coefficient equal to +1?       : %s" % pos)
print("      The first four counts are 1, 2, 4, 8.  That looks like 2^m and IS NOT:")
print("      m = 4 gives %d, not 16, and the coefficients stop being all +1 there too."
      % nt[4])
print("      Four terms of a pattern is not a pattern.  Nothing is banked from this.")
OK["the tempting 2^m reading is recorded as FAILING at m = 4"] = (nt[4] != 16)

print()
print("=" * 78)
print("CONTROLS AND CELL")
print("=" * 78)
for k, v in OK.items(): print("   %-70s %s" % (k, "PASSED" if v else "FAILED"))
print("""
WHAT THIS IS WORTH.

The law in addendum 2 was measured on four knots -- 3_1, 9_2 (p > 0) and 4_1, 6_1 (p < 0).
5_2 is a FIFTH, it was not used to build the law, and its data does not come from the
same place: the four came from Garoufalidis-Sun's tables, and this one comes from this
bench's own R-matrix state sum on Park's braid word.  Different source, different machine,
prediction stated first.

It also settles, for the one knot memos 183 and 184 are about, that C_K(5_2) IS a genuine
power series in (x,q) -- so whatever blocks the naive cyclotomic route for 5_2, it is NOT
convergence.  Memo 185 CELL B is the block there, and CELL B has still been run on one
positive knot only (3_1), because f_K is known in closed form there and is not known for
5_2 past f_5.  That scope limit is unchanged by this certificate.""")
assert all(OK.values()), OK
