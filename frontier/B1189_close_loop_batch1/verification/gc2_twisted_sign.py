#!/usr/bin/env python3
"""GC-2: THE SIGN — the relational bit on the TWISTED double.

All arithmetic exact (sympy over ZZ). Three parts:
 (1) homological detection of the twist (plain vs twisted double H1);
 (2) the mirror-parity of the twist datum: solve X A X^-1 = A^-1 over GL2(Z),
     compute the FULL centralizer and the full conjugator coset, with determinants;
 (3) two-sided control: a hyperbolic matrix in Z[sqrt(3)] (norm-(+1)-only unit
     group) where the instrument WOULD report a surviving chirality bit.
"""
import sympy as sp
from sympy import Matrix, eye, symbols
from sympy.matrices.normalforms import smith_normal_form

A = Matrix([[2, 1], [1, 1]])
I2 = eye(2)

print("=" * 72)
print("PART 1 — homological detection of the twist (exact SNF)")
print("=" * 72)
# H1(torus bundle with monodromy C) = Z (+) Z^2/(C-I)Z^2
for name, C in [("plain  A-bundle  (monodromy  A)", A),
                ("twisted -A-bundle (monodromy -A)", -A)]:
    M = C - I2
    d = M.det()
    snf = smith_normal_form(M, domain=sp.ZZ)
    tor = [abs(snf[i, i]) for i in range(2) if abs(snf[i, i]) != 1]
    print(f"  {name}: det(C-I) = {d}, SNF diag = "
          f"{[snf[0,0], snf[1,1]]}, H1 = Z"
          + "".join(f" + Z/{t}" for t in tor if t != 0))
assert (A - I2).det() == -1        # unit -> coker trivial -> H1 = Z
assert (-A - I2).det() == 5        # -> coker = Z/5 -> H1 = Z + Z/5
print("  => twist class is homologically detected: Z/5 torsion present iff twisted.")
print("  => it is a datum of the PAIR (the gluing), not of either copy: each copy")
print("     is the same once-punctured-torus/figure-eight object (B462/B131).")

print()
print("=" * 72)
print("PART 2 — mirror parity: conjugators X A X^-1 = A^-1 over GL2(Z)")
print("=" * 72)
Ainv = A.inv()
Ainv = Ainv.applyfunc(sp.nsimplify)
print(f"  A^-1 = {Ainv.tolist()}  (integral, det A = {A.det()})")

# --- 2a. the commutant of A in M2(Z), exactly ---
x, y = symbols('x y', integer=True)
B = Matrix([[1, 1], [1, 0]])           # candidate: B^2 = A, det B = -1
assert B * B == A, "B^2 != A"
assert B.det() == -1
assert A * B == B * A
print(f"  B = {B.tolist()}: B^2 = A (verified), det B = {B.det()}, commutes with A.")

# A is non-derogatory (distinct eigenvalues, char poly t^2-3t+1 irreducible /Q),
# so the commutant of A in M2(Q) is Q[A] = Q[B].  General element x*I + y*B:
G = x * I2 + y * B
print(f"  general commutant element xI + yB = {G.tolist()}")
# integrality of xI+yB  <=>  x,y in Z  (entries are x+y, y, y, x)
detG = sp.expand(G.det())
print(f"  det(xI + yB) = {detG}   <- the norm form of Z[phi], disc 5")
assert detG == x**2 + x*y - y**2
# unit solutions: x^2+xy-y^2 = +1 at (1,0); = -1 at (0,1) i.e. B itself
assert detG.subs({x: 1, y: 0}) == 1 and detG.subs({x: 0, y: 1}) == -1
print("  norm form represents +1 (x,y)=(1,0) AND -1 (x,y)=(0,1):")
print("  => Cent_GL2(Z)(A) = { +/- B^n : n in Z }  contains det = -1 elements")
print("     (B = the fundamental unit phi of Z[phi], N(phi) = -1).")
# exhaustive cross-check of the centralizer over a box
cent = []
for a_ in range(-6, 7):
    for b_ in range(-6, 7):
        for c_ in range(-6, 7):
            for d_ in range(-6, 7):
                M = Matrix([[a_, b_], [c_, d_]])
                if M.det() in (1, -1) and M * A == A * M:
                    cent.append(M)
powersB = set()
P = eye(2)
for n in range(0, 9):
    for s in (1, -1):
        powersB.add(tuple((s * P).tolist()[0] + (s * P).tolist()[1]))
    P = P * B
Pinv = eye(2)
Binv = B.inv().applyfunc(sp.nsimplify)
for n in range(1, 9):
    Pinv = Pinv * Binv
    for s in (1, -1):
        powersB.add(tuple((s * Pinv).tolist()[0] + (s * Pinv).tolist()[1]))
box_cent = {tuple(M.tolist()[0] + M.tolist()[1]) for M in cent}
assert box_cent <= powersB, "centralizer element outside {+/-B^n} found!"
print(f"  exhaustive box check |entries|<=6: {len(cent)} centralizer elements, "
      f"ALL of form +/-B^n (verified).")

# --- 2b. one explicit conjugator and the full coset ---
X = Matrix([[0, 1], [-1, 0]])
assert X * A * X.inv().applyfunc(sp.nsimplify) == Ainv
print(f"  X = {X.tolist()}: X A X^-1 = A^-1 (verified), det X = {X.det()}")
# solution set = X * Cent(A): verify both directions
XB = X * B
assert XB * A * XB.inv().applyfunc(sp.nsimplify) == Ainv
print(f"  X*B = {XB.tolist()}: also conjugates A -> A^-1 (verified), det = {XB.det()}")
print("  coset determinants: det(+/- X B^n) = det(X)*det(B)^n = (+1)*(-1)^n")
print("  => BOTH determinant signs occur among conjugators. In particular a")
print(f"     det = -1 conjugator EXISTS: {XB.tolist()}.")
# exhaustive box check of conjugators
conj = []
for a_ in range(-6, 7):
    for b_ in range(-6, 7):
        for c_ in range(-6, 7):
            for d_ in range(-6, 7):
                M = Matrix([[a_, b_], [c_, d_]])
                dd = M.det()
                if dd in (1, -1):
                    if M * A == Ainv * M:      # M A M^-1 = A^-1
                        conj.append((M, dd))
dets = sorted({dd for _, dd in conj})
n_plus = sum(1 for _, dd in conj if dd == 1)
n_minus = sum(1 for _, dd in conj if dd == -1)
print(f"  exhaustive box |entries|<=6: {len(conj)} conjugators, dets found = {dets} "
      f"({n_plus} with +1, {n_minus} with -1)")
# every boxed conjugator lies in X*Cent: X^-1 * M must commute with A
for M, _ in conj:
    W = X.inv().applyfunc(sp.nsimplify) * M
    assert W * A == A * W
print("  every boxed conjugator verified to lie in the single coset X*Cent(A).")

# same statements for the TWISTED monodromy -A (the actual carrier):
mA = -A
mAinv = mA.inv().applyfunc(sp.nsimplify)
assert X * mA * X.inv().applyfunc(sp.nsimplify) == mAinv
assert XB * mA * XB.inv().applyfunc(sp.nsimplify) == mAinv
assert B * mA == mA * B
print("  same conjugators/centralizer work verbatim for -A (twisted carrier).")

# --- 2c. orientation bookkeeping (affine mapping classes of a Sol bundle) ---
print()
print("  Orientation bookkeeping for the mapping torus M_C, C = -A (Sol, |tr|=3>2):")
print("   fiber map P, base FIXED:    needs PC=CP;        or.-effect = sign(det P)")
print("   fiber map P, base REVERSED: needs PCP^-1=C^-1;  or.-effect = -sign(det P)")
print("  Orientation-REVERSING self-homeo exists iff:")
print("   (i)  some P in Cent(C) with det P = -1   -> P = B qualifies (det -1), OR")
print("   (ii) some P with PCP^-1=C^-1, det P = +1 -> P = X qualifies (det +1).")
print("  BOTH exist => the twisted double M_{-A} is MIRROR-SELF-EQUIVALENT")
print("  (amphichiral), two independent ways.")

print()
print("=" * 72)
print("PART 3 — TWO-SIDED CONTROL: the instrument can exclude")
print("=" * 72)
# positive side already recovered: Part 1 reproduces B591's H1 table row (golden).
# exclusion side: disc-12 hyperbolic A' (unit group of Z[sqrt3] has NO norm -1)
Ap = Matrix([[2, 1], [3, 2]])          # tr 4, det 1, eigenvalues 2 +/- sqrt(3)
Apinv = Ap.inv().applyfunc(sp.nsimplify)
Cm = Matrix([[0, 1], [3, 0]])          # Cm^2 = 3I ; commutant = {aI + bCm}
assert Cm * Cm == 3 * I2 and Ap == 2 * I2 + Cm
detGp = sp.expand((x * I2 + y * Cm).det())
print(f"  control A' = {Ap.tolist()} (disc 12);  det(xI+yCm) = {detGp}")
assert detGp == x**2 - 3 * y**2
print("  x^2 - 3y^2 = -1 impossible mod 3 (x^2 = -1 mod 3 insoluble)")
print("  => Cent(A') has ONLY det +1 elements.")
Xp = Matrix([[1, 0], [0, -1]])
assert Xp * Ap * Xp.inv().applyfunc(sp.nsimplify) == Apinv
print(f"  X' = {Xp.tolist()} conjugates A'->A'^-1, det X' = {Xp.det()}")
print("  coset dets = det(X')*det(Cent) = -1 ONLY  => no route (i) and no route (ii):")
print("   (i) needs det -1 in Cent(A'): impossible;  (ii) needs det +1 conjugator: impossible.")
# exhaustive corroboration
conj_p = [Matrix([[a_, b_], [c_, d_]])
          for a_ in range(-6, 7) for b_ in range(-6, 7)
          for c_ in range(-6, 7) for d_ in range(-6, 7)
          if abs(a_ * d_ - b_ * c_) == 1
          and Matrix([[a_, b_], [c_, d_]]) * Ap == Apinv * Matrix([[a_, b_], [c_, d_]])]
dets_p = sorted({M.det() for M in conj_p})
cent_p_dets = sorted({M.det() for a_ in range(-6, 7) for b_ in range(-6, 7)
                      for c_ in range(-6, 7) for d_ in range(-6, 7)
                      for M in [Matrix([[a_, b_], [c_, d_]])]
                      if abs(M.det()) == 1 and M * Ap == Ap * M})
print(f"  exhaustive box |entries|<=6: conjugator dets = {dets_p}, "
      f"centralizer dets = {cent_p_dets}")
assert dets_p == [-1] and cent_p_dets == [1]
print("  => for the disc-12 control the twisted double WOULD be chiral: the Z/2")
print("     survives there. The instrument distinguishes; the golden kill is real.")

print()
print("=" * 72)
print("VERDICT (against B1168's law: accepted only if mirror-ODD + dimensionless)")
print("=" * 72)
print("  The twist class IS a relational (pair-only), dimensionless, homologically")
print("  detected Z/2 datum (Part 1). But it is mirror-EVEN: the twisted double is")
print("  its own mirror (Part 2), because Z[phi] has a norm -1 unit (B, det -1,")
print("  B^2 = A). It therefore CANNOT carry c. NEGATIVE.")
