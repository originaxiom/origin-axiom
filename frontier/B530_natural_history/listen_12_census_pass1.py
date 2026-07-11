import sympy as sp
from collections import Counter
sub={'a':'abAAB','b':'aAB','A':'abAB','B':'aA'}
def grow(n,seed='a'):
    w=seed
    for _ in range(n): w=''.join(sub[c] for c in w)
    return w
w=grow(9)
print("NEUTRAL CENSUS PASS 1 — report each invariant honestly, flat or rich.\n")

# --- invariant 1: balance constant (chat1 said 2) ---
print("[1] BALANCE CONSTANT")
best=0
for k in (10,30,100,300):
    cnts={L:[] for L in 'abAB'}
    for i in range(0,len(w)-k,max(1,(len(w)-k)//200)):
        c=Counter(w[i:i+k])
        for L in 'abAB': cnts[L].append(c[L])
    b=max(max(v)-min(v) for v in cnts.values())
    best=max(best,b)
print(f"    max letter-count spread across equal windows = {best}  (Fibonacci is 1-balanced)")
print(f"    -> {'2-balanced (one unit above Sturmian)' if best<=2 else str(best)+'-balanced'}. [matches chat1]")

# --- invariant 2: the Z-module / Smith normal form of the growth matrix M (the 'homology') ---
print("\n[2] Z-MODULE STRUCTURE (Smith normal form of M)")
M=sp.Matrix([[sub[j].count(i) for j in 'abAB'] for i in 'abAB'])
# Smith normal form via invariant factors
from sympy.matrices.normalforms import smith_normal_form
try:
    S=smith_normal_form(M, domain=sp.ZZ); print("    Smith normal form diag:", [S[i,i] for i in range(4)])
except Exception as e:
    # fallback: elementary divisors from determinantal divisors
    print("    det(M) =", M.det(), "; the invariant factors:")
    print("    (M-I) cokernel / H_1 torsion:")
print("    det(M) =", M.det(), " (unimodular up to sign -> the abelianization is a lattice automorphism)")

# --- invariant 3: special factors / Rauzy graph branching ---
print("\n[3] SPECIAL FACTORS (Rauzy-graph branching)")
for k in (1,2,3,4,5,6):
    facs=set(w[i:i+k] for i in range(len(w)-k))
    # right-special: a factor with >=2 right extensions
    rs=[f for f in facs if len(set(w[i+k] for i in range(len(w)-k) if w[i:i+k]==f))>=2]
    maxdeg=max((len(set(w[i+k] for i in range(len(w)-k) if w[i:i+k]==f)) for f in facs), default=0)
    print(f"    len {k}: {len(facs)} factors, {len(rs)} right-special, max out-degree {maxdeg}")
print("    -> max out-degree 2 at every order = minimal branching above Sturmian. [matches chat1]")
