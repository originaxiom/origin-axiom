import numpy as np, sympy as sp
from collections import Counter

phi=(1+5**0.5)/2
sub={'a':'abAAB','b':'aAB','A':'abAB','B':'aA'}   # the full object
def grow(seed,n):
    w=seed
    for _ in range(n): w=''.join(sub[c] for c in w)
    return w
w=grow('a',9)
print("=== 1. how big does it get; the golden breath ===")
lens=[len(grow('a',n)) for n in range(1,9)]
print("  lengths:", lens)
print("  ratios ->", [round(lens[i+1]/lens[i],4) for i in range(len(lens)-1)], " (beta = phi(1+sqrt phi) = 3.6762)")

print("\n=== 2. the four letters' proportions (who the object mostly is) ===")
c=Counter(w); tot=len(w)
for L in 'abAB': print(f"  {L}: {c[L]/tot:.4f}")
# Perron frequencies (right eigenvector normalized)
M=np.array([[w2.count(L) for w2 in [sub[x] for x in 'abAB']] for L in 'abAB'],float)
val,vec=np.linalg.eig(M); r=np.abs(vec[:,np.argmax(val.real)]); r=r/r.sum()
print("  exact Perron freq (phi,1,phi*sqrt phi,sqrt phi)/sum:", np.round(r,4))

print("\n=== 3. the conversation: which letter follows which (the object's grammar) ===")
big=Counter(zip(w,w[1:]))
letters='abAB'
print("     ->a   ->b   ->A   ->B")
for x in letters:
    row=[big.get((x,y),0) for y in letters]
    s=sum(row) or 1
    print(f"  {x}: "+"  ".join(f"{v/s:.2f}" for v in row))
present=set((x,y) for (x,y),v in big.items() if v>0)
forbidden=[x+y for x in letters for y in letters if (x,y) not in present]
print("  FORBIDDEN adjacencies (pairs the object never says):", forbidden)

print("\n=== 4. is the object reversible in its letters? (a<->A, b<->B swap = the residue) ===")
swap={'a':'A','A':'a','b':'B','B':'b'}
wsw=''.join(swap[c] for c in w)
print("  letter-swapped word == reverse?", wsw==w[::-1], " | == itself?", wsw==w)
# palindrome / mirror content
print("  freq(a)+freq(A) (scattering) vs freq(b)+freq(B) (transparent):",
      round((c['a']+c['A'])/tot,4), round((c['b']+c['B'])/tot,4))
