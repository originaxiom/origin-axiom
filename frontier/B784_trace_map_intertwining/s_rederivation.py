"""Re-derivation of S = diag(1,-1,1) for N8 — cc's open ask.

cc's critique: "S = diag(1,-1,1) does NOT intertwine Sym^2(g) with
Sym^2(g)^{-T} for generic g."  CORRECT — but that tests the CONTRAGREDIENT,
not INVERSION.  My S implements inversion; cc's J implements the contragredient.
These are different operations.

The standard self-duality matrix is J = [[0,1],[-1,0]], det=1:
  J M J^{-1} = M^{-T}  for all M in SL(2)

My conjugation matrix is P = diag(1,-1), det=-1:
  P M^{-1} P^{-1} = M  for all Riley M = [[1,t],[0,1]] or [[1,0],[-u,1]]

P works because Riley matrices are UNIPOTENT with a single off-diagonal entry.
Inverting negates that entry, and P = diag(1,-1) also negates off-diagonal
entries.  So P*M^{-1}*P^{-1} = M for the entire Riley family (all u).

S = Sym^2(P) = diag(1,-1,1) lifts this to V0.  The identity
S*Sym^2(w^{-1})*S^{-1} = Sym^2(w^R) holds for ALL words w, not just
at the geometric point.

MISLABEL CORRECTED: P is the "Riley off-diagonal negation," NOT the
"SL(2) self-duality matrix."  The conclusion (iota gauge on V0) is unaffected.

Gate 5-Q.
"""
import sympy as sp

omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
u = sp.Symbol('u')


def sym2(M):
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([
        [a**2, 2 * a * b, b**2],
        [a * c, a * d + b * c, b * d],
        [c**2, 2 * c * d, d**2],
    ])


P = sp.Matrix([[1, 0], [0, -1]])
J = sp.Matrix([[0, 1], [-1, 0]])
S = sym2(P)
SJ = sym2(J)

print("=" * 72)
print("SECTION 1: P vs J — INVERSION vs CONTRAGREDIENT")
print("=" * 72)
print()

# --- Generic SL(2) ---
a, b, c, d = sp.symbols('a b c d')
g = sp.Matrix([[a, b], [c, d]])
gi = sp.Matrix([[d, -b], [-c, a]])  # g^{-1} for det=1
giT = gi.T  # g^{-T} = contragredient

# J implements contragredient
JgJ = sp.simplify(J * g * J.inv())
print("J * g * J^{-1} for generic g =")
sp.pprint(sp.simplify(JgJ))
print()
print("g^{-T} =")
sp.pprint(giT)
print()
diff_J = sp.simplify(JgJ - giT)
print(f"J*g*J^{{-1}} = g^{{-T}} for generic g?  {diff_J.equals(sp.zeros(2, 2))}")
print()

# P does NOT implement contragredient
PgP = sp.simplify(P * g * P.inv())
print("P * g * P^{-1} for generic g =")
sp.pprint(PgP)
print()
print("g^{-T} =")
sp.pprint(giT)
print()
diff_P_generic = sp.simplify(PgP - giT)
print(f"P*g*P^{{-1}} = g^{{-T}} for generic g?  {diff_P_generic.equals(sp.zeros(2, 2))}")
print()

print("-" * 72)
print("KEY: J implements g -> g^{-T} (contragredient) for all SL(2).")
print("     P implements M^{-1} -> M (inversion) for Riley family only.")
print("     Different operations, different matrices, both correct.")
print("-" * 72)
print()

print("=" * 72)
print("SECTION 2: P WORKS FOR THE ENTIRE RILEY FAMILY")
print("=" * 72)
print()

A_u = sp.Matrix([[1, 1], [0, 1]])
B_u = sp.Matrix([[1, 0], [-u, 1]])

check_A = sp.simplify(P * A_u.inv() * P.inv() - A_u)
check_B = sp.simplify(P * B_u.inv() * P.inv() - B_u)
print(f"P * A(u)^{{-1}} * P^{{-1}} = A(u)?  {check_A.equals(sp.zeros(2, 2))}  (all u)")
print(f"P * B(u)^{{-1}} * P^{{-1}} = B(u)?  {check_B.equals(sp.zeros(2, 2))}  (all u)")
print()

print("WHY: A = [[1,1],[0,1]], A^{-1} = [[1,-1],[0,1]].  Inversion negates")
print("the off-diagonal entry.  P = diag(1,-1) also negates off-diagonal")
print("entries (conjugation: [[a,-b],[-c,d]]).  So P*A^{-1}*P^{-1} = A.")
print("Same for B = [[1,0],[-u,1]], B^{-1} = [[1,0],[u,1]].")
print()

# Verify: J does NOT implement inversion at the geometric point
A_geo = sp.Matrix([[1, 1], [0, 1]])
B_geo = sp.Matrix([[1, 0], [-omega, 1]])
print("Does J implement inversion at the geometric point?")
JA = sp.simplify(J * A_geo.inv() * J.inv())
print(f"  J * A^{{-1}} * J^{{-1}} = {JA.tolist()}")
print(f"  A =                  {A_geo.tolist()}")
print(f"  Equal?  {JA.equals(A_geo)}  (NO — J gives the contragredient, not inversion)")
print()

print("=" * 72)
print("SECTION 3: THE CORRECT GENERAL STATEMENT")
print("=" * 72)
print()

print("For SL(2): g^{-1} = J * g^T * J^{-1}  (standard identity).")
print("Therefore: M^{-1} = J * M^T * J^{-1}.")
print()
print("At the Riley parametrization: P * M^{-1} * P^{-1} = M  for all (A(u), B(u)).")
print("Combining: P * J * M^T * J^{-1} * P^{-1} = M.")
print("So: (PJ) * M^T * (PJ)^{-1} = M  for Riley matrices.")
print()

PJ = P * J
print(f"P * J = {PJ.tolist()},  det = {PJ.det()}")
print()

# Verify: PJ conjugates M^T to M for Riley
check_A_PJ = sp.simplify(PJ * A_u.T * PJ.inv() - A_u)
check_B_PJ = sp.simplify(PJ * B_u.T * PJ.inv() - B_u)
print(f"(PJ) * A(u)^T * (PJ)^{{-1}} = A(u)?  {check_A_PJ.equals(sp.zeros(2, 2))}")
print(f"(PJ) * B(u)^T * (PJ)^{{-1}} = B(u)?  {check_B_PJ.equals(sp.zeros(2, 2))}")
print()

print("So the inversion/contragredient relationship at Riley is:")
print("  inversion P = contragredient J composed with transpose conjugator.")
print("  P = (PJ) * (J^{-1}),  where PJ implements transpose-to-identity")
print("  and J implements identity-to-contragredient.")
print()

print("=" * 72)
print("SECTION 4: Sym^2 LIFT — S vs Sym^2(J)")
print("=" * 72)
print()

print(f"S = Sym^2(P) = Sym^2(diag(1,-1)) =")
sp.pprint(S)
print()
print(f"Sym^2(J) =")
sp.pprint(SJ)
print()

# cc's test: Sym^2(J) intertwines contragredient
# Sym^2(J) * Sym^2(g) * Sym^2(J)^{-1} = Sym^2(g^{-T}) = Sym^2(g)^{-T}
g2 = sp.Matrix([[1, 2], [3, -5]])  # det = -5-6 = -11, normalize
g2_sl2 = sp.Matrix([[3, 1], [2, 1]])  # det = 3-2 = 1
g2i = g2_sl2.inv()
g2iT = g2i.T

lhs_SJ = sp.simplify(SJ * sym2(g2_sl2) * SJ.inv())
rhs_SJ = sym2(g2iT)  # = Sym^2(g)^{-T}? No, Sym^2(g^{-T}).
print("cc's test with Sym^2(J) at g = [[3,1],[2,1]] (det=1):")
print(f"  Sym^2(J) * Sym^2(g) * Sym^2(J)^{{-1}} = Sym^2(g^{{-T}})?  "
      f"{sp.simplify(lhs_SJ - rhs_SJ).equals(sp.zeros(3, 3))}")
print()

# My test: S intertwines inversion at Riley
AB = A_geo * B_geo
BA = B_geo * A_geo
ABi = AB.inv()
lhs_S = sp.simplify(S * sym2(ABi) * S.inv())
rhs_S = sym2(BA)
print("My test with S at w=AB (geometric point):")
print(f"  S * Sym^2((AB)^{{-1}}) * S^{{-1}} = Sym^2(BA)?  "
      f"{sp.simplify(lhs_S - rhs_S).equals(sp.zeros(3, 3))}")
print()

# Cross-test: cc's S on my identity
lhs_SJ_mine = sp.simplify(SJ * sym2(ABi) * SJ.inv())
print("Cross-test: Sym^2(J) on my inversion identity at w=AB:")
print(f"  Sym^2(J) * Sym^2((AB)^{{-1}}) * Sym^2(J)^{{-1}} = Sym^2(BA)?  "
      f"{sp.simplify(lhs_SJ_mine - rhs_S).equals(sp.zeros(3, 3))}")
print()

# My S on cc's identity
lhs_S_cc = sp.simplify(S * sym2(g2_sl2) * S.inv())
rhs_S_cc = sym2(g2iT)
print("Cross-test: S on cc's contragredient identity at g=[[3,1],[2,1]]:")
print(f"  S * Sym^2(g) * S^{{-1}} = Sym^2(g^{{-T}})?  "
      f"{sp.simplify(lhs_S_cc - rhs_S_cc).equals(sp.zeros(3, 3))}")
print()

print("-" * 72)
print("RESULT: Each matrix passes ITS OWN identity, fails the OTHER's.")
print("  S = diag(1,-1,1): inversion at Riley (P*M^{-1}*P^{-1} = M)")
print("  Sym^2(J) = [[0,0,1],[0,-1,0],[1,0,0]]: contragredient (generic)")
print("-" * 72)
print()

print("=" * 72)
print("SECTION 5: BOTH PROVE THE SAME CONCLUSION — RANK 3 ON V0")
print("=" * 72)
print()

print("Via P (inversion route):")
print("  P*A^{-1}*P^{-1} = A, P*B^{-1}*P^{-1} = B  =>  (A,B) ~ (A^{-1},B^{-1})")
print("  => iota is trivial on character variety  =>  rank 3 on V0")
print()
print("Via J (contragredient route):")
print("  Sym^2 is self-dual:  Sym^2(M)^{-T} = Sym^2(J) Sym^2(M) Sym^2(J)^{-1}")
print("  Self-dual representations have tr(M) = tr(M^{-1})  (same character)")
print("  => iota is trivial on V0 traces  =>  rank 3 on V0")
print()
print("Same conclusion by different paths.  cc's contragredient route is the")
print("standard proof.  My Riley-P route is concrete and parametrization-aware.")
print("The mislabel 'self-duality matrix' conflated the two.")
print()

print("=" * 72)
print("CORRECTION SUMMARY")
print("=" * 72)
print()
print("WRONG: 'S = diag(1,-1,1) = Sym^2 of the SL(2) self-duality matrix'")
print("RIGHT: 'S = diag(1,-1,1) = Sym^2(P), where P = diag(1,-1) is the")
print("        Riley off-diagonal negation.  P implements iota as theta")
print("        for the Riley family: P*M^{-1}*P^{-1} = M for all (A(u),B(u)).'")
print()
print("The standard SL(2) self-duality matrix is J = [[0,1],[-1,0]],")
print("which implements the contragredient M -> M^{-T}, not inversion")
print("M -> M^{-1}.  cc tested the contragredient identity on my S;")
print("that test correctly fails because S implements a different operation.")
print()
print("The rank-3 conclusion is UNAFFECTED by this relabeling.")
