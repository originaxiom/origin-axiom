import sympy as sp

print("=== HANDOFF CHECK 1: the stated substitution phi on F4 — is it an automorphism? ===")
# phi: a->abAB, b->aA, A->abaAB, B->aA   (generators a,b,A,B)
# abelianization exponent-sum matrix: columns = images, rows = (a,b,A,B) counts
# a->abAB : a1 b1 A1 B1
# b->aA   : a1 b0 A1 B0
# A->abaAB: a2 b1 A1 B1
# B->aA   : a1 b0 A1 B0
M = sp.Matrix([
    [1, 1, 2, 1],   # a-row
    [1, 0, 1, 0],   # b-row
    [1, 1, 1, 1],   # A-row
    [1, 0, 1, 0],   # B-row
])
print("abelianization matrix M =")
sp.pprint(M)
print("det(M) =", M.det(), "   (handoff claims -1 => automorphism)")
print("phi(b) == phi(B)?  b->aA, B->aA  =>", "YES, identical => phi NON-INJECTIVE => NOT an automorphism")
print("columns for b-image and B-image identical:", M[:,1]==M[:,3])

print("\n=== HANDOFF CHECK 2: |gamma| = 1/sqrt(phi) exactly ===")
phi = (1+sp.sqrt(5))/2
# gamma = -1/phi + i*sqrt(sqrt5 - 2)
re = -1/phi; im2 = sp.sqrt(5)-2
mod2 = sp.simplify(re**2 + im2)
print("|gamma|^2 = 1/phi^2 + (sqrt5-2) =", sp.simplify(mod2), " ; 1/phi =", sp.simplify(1/phi))
print("|gamma|^2 == 1/phi ?", sp.simplify(mod2 - 1/phi)==0, " => |gamma| = 1/sqrt(phi):", sp.simplify(mod2-1/phi)==0)

print("\n=== HANDOFF CHECK 3: direct-product F2xF2 has no irreducible cross-coupled SL2 rep ===")
print("Schur: if rho|_{first F2} is irreducible, its commutant = scalars; the second F2 commutes")
print("=> second F2 is scalar (+-1) => any 2-dim irrep of GxH is (2-dim of G) (x) (1-dim of H).")
print("=> genuinely cross-coupled (kappa(a,A)!=2) irreducible reps do NOT exist for the DIRECT product.")
print("   => the obstruction the handoff names is REAL (this part is correct).")
