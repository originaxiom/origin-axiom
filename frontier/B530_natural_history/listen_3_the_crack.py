import numpy as np, sympy as sp
sub={'a':'abAAB','b':'aAB','A':'abAB','B':'aA'}
letters='abAB'
# abelianization M (rows/cols a,b,A,B): M[i,j] = count of letter i in image of letter j
M=sp.Matrix([[sub[j].count(i) for j in letters] for i in letters])
print("M (the object's growth), rows/cols a,b,A,B:"); sp.pprint(M)

# the swap s: a<->A, b<->B  as a permutation matrix P (swap indices 0<->2, 1<->3)
P=sp.Matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]])
sMs=P*M*P
print("\ns M s (M seen through the swap):"); sp.pprint(sMs)
D=sp.simplify(M-sMs)
print("\nM - sMs  (where the swap symmetry breaks):"); sp.pprint(D)
nz=[(letters[i],letters[j],D[i,j]) for i in range(4) for j in range(4) if D[i,j]!=0]
print("nonzero differences:", nz)

print("\n=== read: is the break localized, and does it sit on A? ===")
print("total |asymmetry| =", sum(abs(D[i,j]) for i in range(4) for j in range(4)),
      " of", sum(abs(M[i,j]) for i in range(4) for j in range(4)), "total weight")

print("\n=== the two ends live in M's spectrum -- does the swap exchange them? ===")
Mn=np.array(M.tolist(),float)
w,V=np.linalg.eig(Mn); 
print("eigenvalues:", np.round(sorted(w,key=lambda z:-abs(z)),4))
# the program's two ends: product RL (trace 3, sqrt5) and ratio -RL^-1 (trace -1, sqrt-3)
print("beta (Perron) =", round(max(abs(w)),4), " = phi(1+sqrt phi); the growth axis is swap-broken (the A-self-loop feeds it)")

print("\n=== is the swap even an automorphism of the object's dynamics? phi.s vs s.phi ===")
def word_swap(w): return ''.join({'a':'A','A':'a','b':'B','B':'b'}[c] for c in w)
for L in letters:
    lhs=word_swap(sub[L])                 # s(phi(L))
    rhs=sub[word_swap(L)]                 # phi(s(L))
    print(f"  s(phi({L}))={lhs:6s}  phi(s({L}))={rhs:6s}  equal:{lhs==rhs}  reverse-equal:{lhs==rhs[::-1]}")
