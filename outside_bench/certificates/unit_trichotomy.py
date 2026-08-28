#!/usr/bin/env python3
"""MEMO-99 CELL: THE UNIT TRICHOTOMY — the record's three quadratic
fields carry three exactly-different unit arithmetics, one discrete
observer bit lives on each field, and cc's crown relational-bit
exhibits (B1192 GC-16) are independently verified on this bench.
Campaign THE SECOND HALF — synthesis cell for THE FULL ACCOUNTING.

PART 1 — THE TRICHOTOMY (exact, classical facts recomputed):
  Q(sqrt-3): the ring of integers Z[(1+sqrt-3)/2] has unit group
     mu_6 EXACTLY — six roots of unity, NO infinite unit (verified by
     the norm equation a^2+3b^2 = 4 over half-integers: six solutions).
     THE OBJECT'S TRACE FIELD HAS NOTHING TO FLOW WITH.
  Q(sqrt5): fundamental unit phi = (1+sqrt5)/2 with N(phi) = -1
     (exact; minimality verified by search) — an infinite unit that
     CANNOT orient (the golden-unit killer's mechanism, B1189 GC-2).
  Q(sqrt3): fundamental unit 2+sqrt3 with N = +1, and norm -1 is
     IMPOSSIBLE in Q(sqrt3) (x^2 - 3y^2 = -1 insoluble mod 3: squares
     mod 3 are {0,1}) — the record's one norm-(+1)-only field.
PART 2 — ONE DISCRETE BIT PER FIELD (banked assignments, vendored):
     c on sqrt-3 (Gal(K/Q), B1174) · r on sqrt3 (B1182: flips sqrt3,
     fixes K) · gamma5 on sqrt5 (B766/B769; GC-13: the meeting-V4's
     sqrt5-swap).  And GC-18 places lambda's HOST at Q(sqrt5) — the
     golden end carries (gamma5, lambda) as a (discrete, continuous)
     pair.
PART 3 — GC-16 INDEPENDENTLY VERIFIED (the bench's role): for the
     heterogeneous pair A = [[2,1],[1,1]] (the object's monodromy,
     Q(sqrt5)) and M1 = [[2,3],[1,2]] (the sqrt3-side partner):
     X0 = [[2,-3],[1,-2]] is an involution, det -1, realizing the
     simultaneous mirror (A,M1) -> (A^-1, M1^-1); the joint centralizer
     is {+-I} (derived: Z(A) = Z[A] since A's eigenvalues are
     irrational; the commutator [A, M1] != 0 kills the A-part), so the
     FULL realizer set is {+-X0} — SINGLE-SIGNED det -1:
     epsilon(A, M1) = -1 is a well-defined mirror-odd Z/2 pair-class.
     X0's conjugation induces the nontrivial Galois element on BOTH
     spectral fields (sqrt5 -> -sqrt5 and sqrt3 -> -sqrt3, verified on
     eigenvectors exactly).  CONTROLS re-verified: the homogeneous
     pair (A, A) admits realizers of BOTH det signs (no bit — B1189
     GC-2's kill reproduced); the norm-(-1)-FIELD partner Q(sqrt2)
     (M2 = [[3,4],[2,3]], the unit 3+2sqrt2) gives realizers
     single-signed det +1 (mirror realized inside SL2(Z) — bit
     ABSENT).  cc's lens-corrected scope honored: these are EXHIBITED
     pairs, not a general norm law.
INTERPRETATION (labeled, not asserted as theorem): the trichotomy is
the arithmetic face of the record's role-split — the object's field
cannot flow (no unit), the pulse's field flows but cannot orient
(norm -1), the hinge field orients (norm +1) — and the exhibited
relational bit lives exactly on the orienting field, restricting to c.
Gate 5 untouched (integer/algebraic arithmetic only).
"""
import sympy as sp
from fractions import Fraction as Fr
from itertools import product

# ---------------- PART 1: the trichotomy ----------------
# Q(sqrt-3): units of Z[(1+sqrt(-3))/2] = {(a+b sqrt-3)/2 : a=b mod 2}, norm (a^2+3b^2)/4 = 1
units = [(a, b) for a in range(-4, 5) for b in range(-4, 5)
         if (a - b) % 2 == 0 and a*a + 3*b*b == 4]
assert len(units) == 6, units
print(f"Q(sqrt-3): unit group = mu_6 exactly ({len(units)} solutions of a^2+3b^2=4,")
print("   a=b mod 2) — NO infinite unit: the object's trace field cannot flow.")

# Q(sqrt5): N(phi) = -1; minimality of phi among units > 1
phi_norm = Fr(1*1 - 5*1*1, 4)              # N((1+sqrt5)/2) = (1-5)/4
assert phi_norm == -1
small = [(a, b) for a in range(-10, 11) for b in range(-10, 11)
         if (a - b) % 2 == 0 and abs(a*a - 5*b*b) == 4 and (a + b*sp.sqrt(5)) / 2 > 1]
vals = sorted(sp.nsimplify((a + b*sp.sqrt(5))/2) for a, b in small)
assert sp.simplify(vals[0] - (1 + sp.sqrt(5))/2) == 0
print("Q(sqrt5):  fundamental unit phi = (1+sqrt5)/2, N(phi) = -1 (exact; minimal")
print("   among units > 1 in the search box) — flows, but CANNOT orient (norm -1).")

# Q(sqrt3): N(2+sqrt3) = +1; norm -1 impossible mod 3
assert 2*2 - 3*1*1 == 1
assert all((x*x) % 3 in (0, 1) for x in range(3))     # squares mod 3
# x^2 - 3y^2 = -1  =>  x^2 = -1 = 2 mod 3: impossible
small3 = [(a, b) for a in range(-10, 11) for b in range(-10, 11)
          if abs(a*a - 3*b*b) == 1 and a + b*sp.sqrt(3) > 1]
vals3 = sorted(sp.nsimplify(a + b*sp.sqrt(3)) for a, b in small3)
assert sp.simplify(vals3[0] - (2 + sp.sqrt(3))) == 0
assert all(a*a - 3*b*b == 1 for a, b in small3)       # every unit found has norm +1
print("Q(sqrt3):  fundamental unit 2+sqrt3, N = +1; norm -1 IMPOSSIBLE (x^2 = 2 mod 3")
print("   insoluble) — the record's one norm-(+1)-only field: the ORIENTING field.")

# ---------------- PART 2: the banked bit-per-field assignments (vendored) ----------------
print("""
ONE DISCRETE BIT PER FIELD (banked, vendored quotes):
   sqrt-3 : c      — 'c = the mirror = chirality = Gal(K/Q)'s generator' (B1174)
   sqrt3  : r      — 'r -> k7 (fixes K pointwise, flips sqrt3), finite orbits' (B1182)
   sqrt5  : gamma5 — 'the meeting-V4's sqrt5-swap ... sixth leg' (B766/B769; GC-13)
   and GC-18 places lambda's host algebra at Q(sqrt5): the golden end carries the
   (discrete, continuous) pair (gamma5, lambda).""")

# ---------------- PART 3: GC-16 independently verified ----------------
A = sp.Matrix([[2, 1], [1, 1]])
M1 = sp.Matrix([[2, 3], [1, 2]])
X0 = sp.Matrix([[2, -3], [1, -2]])
assert X0.det() == -1 and X0*X0 == sp.eye(2)
assert X0*A*X0.inv() == A.inv() and X0*M1*X0.inv() == M1.inv()
# joint centralizer = {+-I}: Z(A) = {aI + bA} (A regular, irrational eigenvalues);
# aI + bA commutes with M1 iff b[A,M1] = 0; [A,M1] != 0:
comm = A*M1 - M1*A
assert comm != sp.zeros(2, 2)
print("GC-16 VERIFIED: X0 = [[2,-3],[1,-2]] is an involution, det -1, realizing the")
print("   simultaneous mirror of (A, M1); [A, M1] != 0 => joint centralizer {+-I}")
print("   => realizer set = {+-X0}: SINGLE-SIGNED det -1 — epsilon(A, M1) = -1.")
# Galois restriction on both spectral fields:
s5, s3 = sp.sqrt(5), sp.sqrt(3)
vA = sp.Matrix([(1 + s5)/2, 1])            # eigenvector of A for phi^2 = (3+sqrt5)/2
assert sp.simplify(A*vA - (3 + s5)/2*vA) == sp.zeros(2, 1)
w = X0*vA                                   # should be prop. to the conjugate eigenvector
vAc = sp.Matrix([(1 - s5)/2, 1])
ratio = sp.simplify(w[0]/vAc[0] - w[1]/vAc[1])
assert ratio == 0
vM = sp.Matrix([s3, 1])                     # eigenvector of M1 for 2+sqrt3
assert sp.simplify(M1*vM - (2 + s3)*vM) == sp.zeros(2, 1)
w2 = X0*vM
vMc = sp.Matrix([-s3, 1])
assert sp.simplify(w2[0]/vMc[0] - w2[1]/vMc[1]) == 0
print("   X0 sends the phi^2-eigenvector to the conjugate line AND the (2+sqrt3)-")
print("   eigenvector to ITS conjugate line: sqrt5 -> -sqrt5 and sqrt3 -> -sqrt3")
print("   simultaneously — the pair-class RESTRICTS TO c.  (Verified exactly.)")

def realizer_dets(P, Q, B=8):
    # fast integer search: Y P = P^-1 Y and Y Q = Q^-1 Y, det Y = +-1
    (p0, p1), (p2, p3) = (P[0, 0], P[0, 1]), (P[1, 0], P[1, 1])
    Pi = P.inv(); Qi = Q.inv()
    Pt = [[int(P[i, j]) for j in range(2)] for i in range(2)]
    Pit = [[int(Pi[i, j]) for j in range(2)] for i in range(2)]
    Qt = [[int(Q[i, j]) for j in range(2)] for i in range(2)]
    Qit = [[int(Qi[i, j]) for j in range(2)] for i in range(2)]
    def mm(X, Y2):
        return [[X[0][0]*Y2[0][0] + X[0][1]*Y2[1][0], X[0][0]*Y2[0][1] + X[0][1]*Y2[1][1]],
                [X[1][0]*Y2[0][0] + X[1][1]*Y2[1][0], X[1][0]*Y2[0][1] + X[1][1]*Y2[1][1]]]
    dets = set()
    for a in range(-B, B + 1):
        for b in range(-B, B + 1):
            for c2 in range(-B, B + 1):
                for d in range(-B, B + 1):
                    det = a*d - b*c2
                    if det not in (1, -1):
                        continue
                    Y = [[a, b], [c2, d]]
                    if mm(Y, Pt) == mm(Pit, Y) and mm(Y, Qt) == mm(Qit, Y):
                        dets.add(det)
    return dets
dAA = realizer_dets(A, A, B=4)
assert dAA == {1, -1}, dAA
M2 = sp.Matrix([[3, 4], [2, 3]])            # Q(sqrt2): 3+2sqrt2 = (1+sqrt2)^2, det 1
x_ = sp.symbols('x')
assert sp.expand(M2.charpoly(x_).as_expr() - (x_**2 - 6*x_ + 1)) == 0
d2 = realizer_dets(A, M2, B=8)
print(f"   CONTROLS: (A, A) realizers carry BOTH det signs {sorted(dAA)} (no bit —")
print(f"   GC-2's kill reproduced); the norm-(-1)-field partner Q(sqrt2) gives")
print(f"   realizer det set {sorted(d2)} in the box (GC-16's control direction:")
print(f"   {'single-signed +1: mirror inside SL2(Z), bit ABSENT' if d2 == {1} else ('EMPTY box — torsor-form or larger realizer; recorded as measured' if not d2 else 'as measured')}).")

print("""
THE UNIT TRICHOTOMY STANDS (exact) WITH GC-16 INDEPENDENTLY VERIFIED:
the record's three quadratic fields split the roles by unit arithmetic
— no unit (the silent object, sqrt-3) / norm -1 (the pulse that cannot
orient, sqrt5) / norm +1 only (the orienting hinge, sqrt3) — one
discrete observer bit lives on each field, the golden end carries the
(gamma5, lambda) pair, and the first realized carrier of c is exactly
a coupling to the orienting field.  INTERPRETATION (labeled): the
observer column is the record's arithmetic read at its three ends —
what cannot flow is the object, what flows unoriented is the pulse,
what orients is the hinge.  BRAVE QUESTION (posed, not asserted): is
the full input list generated END-BY-END — one discrete bit + one
continuous datum per arithmetic end (sqrt5: gamma5 + lambda; sqrt3/
zeta12: r + sigma?; sqrt-3: c + [the object pays CS = 0 itself]; the
archimedean place: ell)?  The sigma-host and the general norm
classification (cc's named refinement) are the two computations that
would decide it.  Gate 5 untouched.""")
