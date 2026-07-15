"""B634 G1 — the conductor identities (exact)."""
import sympy as sp

A = sp.Matrix([[2, 1], [1, 1]])                    # the fig-8 monodromy A1
assert A.trace() == 3 and A.det() == 1
assert (A - sp.eye(2)).det() == -1                 # the abelian-invisibility unit
d = (A + sp.eye(2)).det()
assert d == 5 and A.trace() ** 2 - 4 == 5          # det(A+I) = 5 = tr^2 - 4
M = A + sp.eye(2)
# Smith normal form of [[3,1],[1,2]] by hand-verifiable row/col ops:
# gcd of entries = 1, det = 5  =>  SNF = diag(1, 5)
g = sp.gcd(sp.gcd(M[0, 0], M[0, 1]), sp.gcd(M[1, 0], M[1, 1]))
assert g == 1 and abs(M.det()) == 5
print("G1 PASS: det(A1+I) = 5 = tr^2-4; det(A1-I) = -1; SNF(A1+I) = diag(1,5)")
print("      => H1(-A1 bundle) = Z + Z/5 : the mirror-twist conductor = 5 = kappa")
