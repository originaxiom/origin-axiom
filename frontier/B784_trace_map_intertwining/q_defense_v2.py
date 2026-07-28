"""Defense v2: the rep-variety vs group-level distinction.

cc's counter-refutation (q_defense_gate relay) accepts Sym2(g)^T != Sym2(g^T)
but raises a deeper objection: Q fails on products (AB -> False), and the
abelian obstruction proves no fixed Q works on the whole group.

THE KEY DISTINCTION: cc conflates two different conditions.

(A) GROUP-LEVEL: Q * rho(w)^T * Q^{-1} = rho(w) for ALL words w.
    This requires the MAP M -> Q M^T Q^{-1} to be the IDENTITY on the
    group image. Impossible for non-abelian groups (abelian obstruction).
    cc's "AB -> False" tests this.

(B) REP-VARIETY: rho_2 is conjugate to rho_1, where
    rho_1(a) = A, rho_1(b) = B,
    rho_2(a) = A^T, rho_2(b) = B^T.
    Requires ONLY Q * A^T * Q^{-1} = A and Q * B^T * Q^{-1} = B.
    This implies Q * rho_2(w) * Q^{-1} = rho_1(w) for ALL words w.

The crucial point: rho_2(ab) = A^T * B^T  (NOT (AB)^T = B^T * A^T).
rho_2 is a legitimate representation of F_2 (free group, no relations).

cc tests condition (A), which fails. Innerness tests condition (B), which works.

Gate 5-Q.
"""
import numpy as np
import sympy as sp

omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
A = sp.Matrix([[1, 1], [0, 1]])
B = sp.Matrix([[1, 0], [-omega, 1]])


def sym2(M):
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([
        [a**2, 2 * a * b, b**2],
        [a * c, a * d + b * c, b * d],
        [c**2, 2 * c * d, d**2],
    ])


Q = sp.Matrix([[0, 0, 1], [0, sp.Rational(1, 2), 0], [1, 0, 0]])

sA = sym2(A)
sB = sym2(B)
sAB = sym2(A * B)
sBA = sym2(B * A)

print("=" * 72)
print("SECTION 1: THE TWO CONDITIONS")
print("=" * 72)
print()
print("Condition (A) — GROUP-LEVEL (cc's test):")
print("  Q * rho(w)^T * Q^{-1} = rho(w) for ALL words w")
print("  Equivalently: Q * Sym2(AB)^T * Q^{-1} = Sym2(AB)?")
print()

cc_AB = sp.simplify(Q * sAB.T * Q.inv() - sAB)
cc_AB_ok = cc_AB.equals(sp.zeros(3, 3))

cc_BA = sp.simplify(Q * sBA.T * Q.inv() - sBA)
cc_BA_ok = cc_BA.equals(sp.zeros(3, 3))

print(f"  Q * Sym2(AB)^T * Q^-1 = Sym2(AB)?  {cc_AB_ok}")
print(f"  Q * Sym2(BA)^T * Q^-1 = Sym2(BA)?  {cc_BA_ok}")
print()

# What does Q actually map Sym2(AB)^T to?
result_AB = sp.simplify(Q * sAB.T * Q.inv())
equals_BA = result_AB.equals(sBA)
print(f"  Q * Sym2(AB)^T * Q^-1 = Sym2(BA)?  {equals_BA}")
print("  (Q reverses the word order — this is the anti-homomorphism at work)")
print()

print("Condition (B) — REP-VARIETY INNERNESS:")
print("  rho_2(a) = Sym2(A)^T, rho_2(b) = Sym2(B)^T")
print("  Q * rho_2(w) * Q^{-1} = rho_1(w) for all words w?")
print()

# On generators (same as before)
gen_A = sp.simplify(Q * sA.T * Q.inv() - sA)
gen_B = sp.simplify(Q * sB.T * Q.inv() - sB)
print(f"  On a:  Q * Sym2(A)^T * Q^-1 = Sym2(A)?  {gen_A.equals(sp.zeros(3, 3))}")
print(f"  On b:  Q * Sym2(B)^T * Q^-1 = Sym2(B)?  {gen_B.equals(sp.zeros(3, 3))}")
print()

# On product ab: rho_2(ab) = Sym2(A)^T * Sym2(B)^T  (NOT Sym2(AB)^T!)
rho2_ab = sA.T * sB.T
rho1_ab = sA * sB  # = Sym2(AB)

inn_AB = sp.simplify(Q * rho2_ab * Q.inv() - rho1_ab)
inn_AB_ok = inn_AB.equals(sp.zeros(3, 3))

print(f"  On ab: Q * rho_2(ab) * Q^-1 = rho_1(ab)?  {inn_AB_ok}")
print(f"         where rho_2(ab) = Sym2(A)^T * Sym2(B)^T")
print(f"         and   rho_1(ab) = Sym2(A) * Sym2(B) = Sym2(AB)")
print()

# Show the key: rho_2(ab) != rho_1(ab)^T
rho1_ab_T = rho1_ab.T  # = Sym2(AB)^T = (Sym2(A)*Sym2(B))^T = Sym2(B)^T*Sym2(A)^T
diff = sp.simplify(rho2_ab - rho1_ab_T)
diff_ok = diff.equals(sp.zeros(3, 3))
print(f"  CRUCIAL: rho_2(ab) = Sym2(A)^T * Sym2(B)^T")
print(f"           rho_1(ab)^T = Sym2(AB)^T = Sym2(B)^T * Sym2(A)^T")
print(f"           rho_2(ab) == rho_1(ab)^T?  {diff_ok}")
print(f"           (Different order! A^T*B^T != B^T*A^T)")
print()

# ================================================================
print("=" * 72)
print("SECTION 2: INNERNESS HOLDS ON ALL WORDS (ALGEBRAIC PROOF)")
print("=" * 72)
print()
print("If Q * A^T * Q^-1 = A and Q * B^T * Q^-1 = B, then for any word w:")
print("  Q * rho_2(w) * Q^-1 = rho_1(w)")
print()
print("Proof: rho_2 is a HOMOMORPHISM (F_2 is free, any pair defines a rep).")
print("  rho_2(ab) = rho_2(a) * rho_2(b) = A^T * B^T")
print("  Q * rho_2(ab) * Q^-1 = Q * A^T * B^T * Q^-1")
print("                       = (Q*A^T*Q^-1) * (Q*B^T*Q^-1)")
print("                       = A * B = rho_1(ab)")
print()
print("For an arbitrary word w = a^{e1} b^{e2} a^{e3} ...:")
print("  Q * rho_2(w) * Q^-1 = Q * (A^T)^{e1} * (B^T)^{e2} * ... * Q^-1")
print("                      = A^{e1} * B^{e2} * ... = rho_1(w)")
print()
print("The abelian obstruction does NOT apply because:")
print("  - It proves: no Q with Q*M^T*Q^-1 = M for all M in a non-abelian group")
print("  - Innerness asks: Q*rho_2(w)*Q^-1 = rho_1(w) for all w in F_2")
print("  - These are different: rho_2(ab) = A^T*B^T  !=  (AB)^T = B^T*A^T")
print()

# ================================================================
print("=" * 72)
print("SECTION 3: EXHAUSTIVE WORD-LEVEL VERIFICATION")
print("=" * 72)
print()

words = [
    ("a", A, sA),
    ("b", B, sB),
    ("ab", A * B, sA * sB),
    ("ba", B * A, sB * sA),
    ("a^-1", A.inv(), sA.inv()),
    ("b^-1", B.inv(), sB.inv()),
    ("a^-1*b", A.inv() * B, sA.inv() * sB),
    ("a*b^-1", A * B.inv(), sA * sB.inv()),
    ("aba", A * B * A, sA * sB * sA),
    ("bab", B * A * B, sB * sA * sB),
    ("abab", A * B * A * B, sA * sB * sA * sB),
    ("a^2*b", A * A * B, sA * sA * sB),
]

all_cc_ok = True
all_inn_ok = True

for name, word_sl2, word_sym2 in words:
    sym2_word = sym2(word_sl2)

    # cc's test: Q * Sym2(word)^T * Q^-1 = Sym2(word)?
    cc_result = sp.simplify(Q * sym2_word.T * Q.inv() - sym2_word)
    cc_ok = cc_result.equals(sp.zeros(3, 3))

    # Innerness test: Q * rho_2(word) * Q^-1 = Sym2(word)?
    # rho_2(word) = product of transposed generators in word order
    rho2_word = word_sym2.T  # Wait...

    # Actually, rho_2 transposes the GENERATORS, so rho_2(a) = Sym2(A)^T.
    # For a product: rho_2(ab) = rho_2(a) * rho_2(b) = Sym2(A)^T * Sym2(B)^T.
    # This is NOT Sym2(AB)^T. It IS the product in GL(3) of the transposed generators.
    # But word_sym2 already computes this correctly if we transpose the FACTORS.

    # Let me compute rho_2(word) from scratch using transposed Sym2 generators.
    sA_T = sA.T
    sB_T = sB.T
    sAi_T = sA.inv().T
    sBi_T = sB.inv().T

    # Build rho_2(word) by substituting transposed generators
    rho2_map = {
        "a": sA_T,
        "b": sB_T,
        "ab": sA_T * sB_T,
        "ba": sB_T * sA_T,
        "a^-1": sAi_T,
        "b^-1": sBi_T,
        "a^-1*b": sAi_T * sB_T,
        "a*b^-1": sA_T * sBi_T,
        "aba": sA_T * sB_T * sA_T,
        "bab": sB_T * sA_T * sB_T,
        "abab": sA_T * sB_T * sA_T * sB_T,
        "a^2*b": sA_T * sA_T * sB_T,
    }

    rho2_w = rho2_map[name]
    inn_result = sp.simplify(Q * rho2_w * Q.inv() - sym2_word)
    inn_ok = inn_result.equals(sp.zeros(3, 3))

    all_cc_ok = all_cc_ok and cc_ok
    all_inn_ok = all_inn_ok and inn_ok
    tag = ""
    if not cc_ok and inn_ok:
        tag = " <-- cc fails, innerness works"
    elif not cc_ok and not inn_ok:
        tag = " <-- BOTH fail (BUG)"
    print(f"  w={name:10s}: cc's test={cc_ok:5}, innerness={inn_ok:5}{tag}")

print()
print(f"cc's condition (A) passes on all words: {all_cc_ok}")
print(f"Innerness condition (B) passes on all words: {all_inn_ok}")
print()

# ================================================================
print("=" * 72)
print("SECTION 4: THE ABELIAN OBSTRUCTION EXPLAINED")
print("=" * 72)
print()
print("cc's argument: if Q*M^T*Q^-1 = M for all M in group G,")
print("then Q*(MN)^T*Q^-1 = MN. But (MN)^T = N^T*M^T, so")
print("Q*N^T*M^T*Q^-1 = (Q*N^T*Q^-1)(Q*M^T*Q^-1) = N*M = MN.")
print("So N*M = M*N for all M,N => G abelian. Contradiction.")
print()
print("THIS IS CORRECT but addresses condition (A), not (B).")
print()
print("Condition (B) does NOT require Q*Sym2(AB)^T*Q^-1 = Sym2(AB).")
print("It requires Q*rho_2(ab)*Q^-1 = Sym2(AB), where")
print("rho_2(ab) = Sym2(A)^T * Sym2(B)^T  (product of transposed GENERATORS).")
print()
print("Verify:")

rho2_ab_check = sA.T * sB.T
result = sp.simplify(Q * rho2_ab_check * Q.inv())
equals_AB = result.equals(sA * sB)
print(f"  Q * (Sym2(A)^T * Sym2(B)^T) * Q^-1 = Sym2(A)*Sym2(B)?  {equals_AB}")

rho1_ab_T_check = (sA * sB).T  # = Sym2(B)^T * Sym2(A)^T (reversed order)
result2 = sp.simplify(Q * rho1_ab_T_check * Q.inv())
equals_AB2 = result2.equals(sA * sB)
equals_BA = result2.equals(sB * sA)
print(f"  Q * Sym2(AB)^T * Q^-1 = Sym2(AB)?  {equals_AB2}  (cc's test)")
print(f"  Q * Sym2(AB)^T * Q^-1 = Sym2(BA)?  {equals_BA}  (Q reverses)")
print()
print("Q * (A^T*B^T) * Q^-1 = AB  (innerness: rho_2 conjugate to rho_1)")
print("Q * (AB)^T * Q^-1 = BA  (word reversal, not identity)")
print()
print("The abelian obstruction kills the group-level question.")
print("The rep-variety innerness question has no abelian obstruction")
print("because rho_2(ab) = A^T*B^T has the SAME multiplication order")
print("as rho_1(ab) = A*B after conjugation by Q.")
print()

# ================================================================
print("=" * 72)
print("SUMMARY")
print("=" * 72)
print()
print("cc's q_defense_gate confuses two questions:")
print()
print("  (A) Is M -> Q*M^T*Q^-1 the identity on Sym2(SL(2))?")
print("      NO (abelian obstruction). cc's 'AB -> False' confirms this.")
print()
print("  (B) Are (A,B) and (A^T,B^T) conjugate on the rep variety?")
print("      YES. Q*A^T*Q^-1 = A, Q*B^T*Q^-1 = B (verified, Riley family).")
print("      This implies Q*rho_2(w)*Q^-1 = rho_1(w) for ALL words w.")
print()
print("theta_T innerness on V0 is condition (B), not (A).")
print("Q = [[0,0,1],[0,1/2,0],[1,0,0]] is the correct intertwiner.")
