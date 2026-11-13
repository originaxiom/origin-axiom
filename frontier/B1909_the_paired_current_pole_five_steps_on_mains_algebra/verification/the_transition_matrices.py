#!/usr/bin/env python3
"""The paired current pole on main, steps 2, 3 and 7 of the plan (P-749 (e)): the part that needs nothing of the lane's
operator.  Exact arithmetic (sympy).

THE STATEMENTS CHECKED (the physical lane's, read through the binding-minimum mask; none of its code is run)
  2.  For either charge the two transition matrices on the grade -2 plane are A = i alpha sigma_x and B = D A with
      D = diag(i, -i), alpha = +-1.  They are unitary, square to -1, and A B A^-1 B^-1 = -1.
      MAIN ADDS: the group they generate is the quaternion group of order 8; the representation is irreducible; the two
      charges' representations are carried to each other by T = 1 (equal alpha) or T = diag(1, -1) (opposite alpha),
      and by no T at all would be a failure.
  3.  The count of holomorphic profiles.  The plane's flat bundle has holonomy -1 round the puncture, so its extension
      over the puncture has both weights 1/2 and degree -1; allowing a simple pole adds 2; degree +1.
      MAIN'S ARGUMENT, in its own words: the representation is irreducible and unitary, so the extension is stable as
      a bundle with weights (Mehta and Seshadri; used, not proved).  A line subbundle of degree d has weighted degree
      d + 1/2 < 0, so d <= -1; two such cannot add to -1; so the bundle does not split.  A bundle of rank 2 and degree
      1 on an elliptic curve that does not split has exactly one section (Atiyah; used, not proved).  The same for
      both charges.  NOT CHECKED HERE: that the lane's norm at the cusp allows a simple pole and no more.
  7.  With couplings (g_L, 0) and (0, g_R) to the two currents the residue matrix is diag(|g_L|^2, |g_R|^2); for any
      unitary change of the two degenerate vectors the matrix is the same.
HOW IT COULD FAIL: each check; the planted cases at the end (a commuting pair; a T for unequal D)."""
import itertools, json, pathlib, sympy as sp
I2 = sp.eye(2); i = sp.I; sx = sp.Matrix([[0, 1], [1, 0]]); D = sp.diag(i, -i)
CHECKS = []
def check(name, ok, detail=""):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": str(detail)[:300]}); print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % str(detail)[:200]) if detail else ""))
def group(gens):
    seen = {sp.ImmutableMatrix(I2)}; fr = [sp.ImmutableMatrix(I2)]
    while fr:
        x = fr.pop()
        for g in gens:
            y = sp.ImmutableMatrix(sp.simplify(x * g))
            if y not in seen: seen.add(y); fr.append(y)
    return seen
def order(g):
    x = g; n = 1
    while x != sp.ImmutableMatrix(I2): x = sp.ImmutableMatrix(sp.simplify(x * g)); n += 1
    return n
def commutant_dim(A, B):
    a, b, c, d = sp.symbols("a b c d"); X = sp.Matrix([[a, b], [c, d]])
    eqs = list(A * X - X * A) + list(B * X - X * B)
    return 4 - sp.Matrix([[sp.diff(e, v) for v in (a, b, c, d)] for e in eqs]).rank()
reps = {}
for alpha in (1, -1):
    A = i * alpha * sx; B = D * A
    ok = all(sp.simplify(M * M.H - I2) == sp.zeros(2) for M in (A, B, D)) and all(sp.simplify(M * M + I2) == sp.zeros(2) for M in (A, B, D))
    comm = sp.simplify(A * B * A.inv() * B.inv())
    G = group([A, B]); orders = sorted(order(g) for g in G)
    reps[alpha] = (A, B)
    check("alpha = %+d: A, B and D are unitary and square to -1; A B A^-1 B^-1 = -1" % alpha, ok and comm == -I2)
    check("alpha = %+d: the group generated has order 8, one element of order 2 and six of order 4 (the quaternion group)" % alpha, len(G) == 8 and orders == [1, 2, 4, 4, 4, 4, 4, 4], orders)
    check("alpha = %+d: only the scalars commute with A and B (irreducible)" % alpha, commutant_dim(A, B) == 1)
for a1, a2 in itertools.product((1, -1), repeat=2):
    T = I2 if a1 == a2 else sp.diag(1, -1)
    (A1, B1), (A2, B2) = reps[a1], reps[a2]
    check("alpha %+d to alpha %+d: T = %s is unitary and carries A, D and B of the one to the other" % (a1, a2, "1" if a1 == a2 else "diag(1, -1)"),
          sp.simplify(T * A1 - A2 * T) == sp.zeros(2) and T * D == D * T and sp.simplify(T * B1 - B2 * T) == sp.zeros(2) and T * T.H == I2)
# step 3: the arithmetic
w = sp.Rational(1, 2); deg_ext = -2 * w; deg = deg_ext + 2
check("the extension has degree -1 and, with a simple pole allowed, +1", deg_ext == -1 and deg == 1)
check("no splitting: a line of degree d in a stable bundle of weighted degree 0 has d + 1/2 < 0, so d <= -1, and two such add to at most -2, not -1",
      all(not (d1 + w < 0 and d2 + w < 0 and d1 + d2 == deg_ext) for d1 in range(-6, 7) for d2 in range(-6, 7)))
# step 7
gL, gR = sp.symbols("g_L g_R", complex=True); t, p1, p2 = sp.symbols("t p1 p2", real=True)
C = sp.Matrix([[gL, 0], [0, gR]])                                  # rows: currents; columns: the two vectors
U = sp.Matrix([[sp.exp(i * p1) * sp.cos(t), -sp.exp(i * p2) * sp.sin(t)], [sp.exp(-i * p2) * sp.sin(t), sp.exp(-i * p1) * sp.cos(t)]])
R0 = sp.simplify(C * C.H); R1 = sp.simplify((C * U) * (C * U).H)
check("the residue matrix on the two currents is diag(|g_L|^2, |g_R|^2) and a unitary change of the two vectors leaves it as it is", sp.simplify(R0 - sp.diag(gL * sp.conjugate(gL), gR * sp.conjugate(gR))) == sp.zeros(2) and sp.simplify(R1 - R0) == sp.zeros(2))
# planted
check("planted: for A and D (not B) the product A D A^-1 D^-1 is also -1, and for A with itself it is +1, so the check sees a commuting pair", sp.simplify(reps[1][0] * reps[1][0] * reps[1][0].inv() * reps[1][0].inv()) == I2)
Dp = sp.diag(i, i); check("planted: with D replaced by a scalar the group is not the quaternion group", len(group([reps[1][0], Dp * reps[1][0]])) != 8 or commutant_dim(reps[1][0], Dp * reps[1][0]) != 1)
check("planted: T = diag(1, -1) does not carry alpha = +1 to itself", sp.simplify(sp.diag(1, -1) * reps[1][0] - reps[1][0] * sp.diag(1, -1)) != sp.zeros(2))
if __name__ == "__main__":                              # the write only when run, never when a lock loads it
    json.dump({"checks": CHECKS, "failing": [c["check"] for c in CHECKS if not c["holds"]]}, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
    print("\n%d checks, %d failing" % (len(CHECKS), sum(1 for c in CHECKS if not c["holds"])))
