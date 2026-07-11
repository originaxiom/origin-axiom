import sympy as sp
import numpy as np

# corrected substitution phi on F4 = <a,b,A,B> (A,B are GENERATORS, positive letters):
#   a -> abAAB,  b -> aAB,  A -> abAB,  B -> aA
imgs = {'a':'abAAB', 'b':'aAB', 'A':'abAB', 'B':'aA'}
gens = ['a','b','A','B']

print("=== injectivity sanity: are the images distinct (the prior bug was phi(b)=phi(B))? ===")
print("  phi(b) =", imgs['b'], " phi(B) =", imgs['B'], " distinct:", imgs['b']!=imgs['B'])
print("  all images distinct:", len(set(imgs.values()))==4)

# abelianization matrix M[i][j] = count of gen_i in phi(gen_j)
M = sp.zeros(4,4)
for j,g in enumerate(gens):
    for i,gi in enumerate(gens):
        M[i,j] = imgs[g].count(gi)
print("\nabelianization matrix M (rows/cols a,b,A,B):"); sp.pprint(M)
x = sp.symbols('x')
cp = sp.expand(M.charpoly(x).as_expr())
print("\ncharpoly =", cp)
print("== bootstrap minpoly x^4-2x^3-5x^2-4x-1 ?", sp.expand(cp - (x**4-2*x**3-5*x**2-4*x-1))==0)
print("det(M) =", M.det(), " (=-1 => necessary for automorphism)")
print("charpoly irreducible/Q:", sp.Poly(cp,x).is_irreducible)

# Perron / primitivity
Mn = np.array(M.tolist(), float)
print("\n=== primitivity (Perron-Frobenius): is (I+M)^3 entrywise > 0 ? ===")
P = np.linalg.matrix_power(np.eye(4)+Mn, 3)
print("  (I+M)^3 all-positive:", bool(np.all(P>0)))
w = np.linalg.eigvals(Mn)
beta = max(abs(w))
print("  Perron beta =", round(beta,4), " (bootstrap beta = phi(1+sqrt phi) ~ 3.676):", abs(beta-3.6756)<1e-2)
print("  other |eig| all < beta:", bool(np.all(np.abs(w) < beta-1e-9) | (np.abs(np.abs(w)-beta)<1e-9)))

print("\n=== what the 5 tests DO and DON'T establish ===")
print("  established: M primitive + charpoly irreducible + Perron => a TRAIN-TRACK map on the rose")
print("              with primitive transition matrix (NECESSARY for iwip).")
print("  NOT established by these tests: (a) phi in Aut(F4) [det=-1 necessary, NOT sufficient for")
print("              free groups -> needs Whitehead]; (b) iwip [needs Bestvina-Handel: NO periodic")
print("              Nielsen paths -> not checked]. word-hyperbolic/atoroidal FOLLOW ONLY IF iwip holds.")
