import sympy as sp
from collections import Counter
sub={'a':'abAAB','b':'aAB','A':'abAB','B':'aA'}
def grow(n,seed='a'):
    w=seed
    for _ in range(n): w=''.join(sub[c] for c in w)
    return w
w=grow(11)

# positions of a; return words = blocks starting at each a up to (not incl) next a
pos=[i for i,c in enumerate(w) if c=='a']
gaps=[pos[i+1]-pos[i] for i in range(len(pos)-1)]
retwords=[w[pos[i]:pos[i+1]] for i in range(len(pos)-1)]
print("=== the pulse: gaps between consecutive a's ===")
gc=Counter(gaps)
print("  distinct return-gaps and their counts:", dict(sorted(gc.items())))
print("  => the object returns to a in only", len(gc), "distinct rhythms")

print("\n=== the return words (the blocks between a's) ===")
rc=Counter(retwords)
for word,cnt in sorted(rc.items(), key=lambda x:-x[1]):
    print(f"  {word:8s} x{cnt}  (len {len(word)})")

print("\n=== is the pulse golden? ratio of the two gap-frequencies ===")
counts=sorted(gc.values(),reverse=True)
if len(counts)>=2:
    print(f"  gap-frequency ratio = {counts[0]/counts[1]:.5f}")
    phi=(1+5**0.5)/2
    for name,val in [('phi',phi),('phi^2',phi**2),('sqrt phi',phi**0.5),('beta',phi*(1+phi**0.5))]:
        if abs(counts[0]/counts[1]-val)<1e-2: print(f"    ~ {name} = {val:.5f}")

print("\n=== is the SEQUENCE of return-words itself self-similar? (Durand: derived seq is substitutive) ===")
alph=sorted(rc, key=lambda x:-rc[x]); code={rw:chr(ord('x')+i) for i,rw in enumerate(alph)}
derived=''.join(code[rw] for rw in retwords)
print("  return-words coded as", {v:k for k,v in code.items()})
print("  derived sequence (first 40):", derived[:40])
dc=Counter(zip(derived,derived[1:]))
print("  derived-alphabet size:", len(alph), " ; derived bigrams present:", sorted(set(dc)))
