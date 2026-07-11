from itertools import combinations
sub={'a':'abAAB','b':'aAB','A':'abAB','B':'aA'}
def grow(n,seed='a'):
    w=seed
    for _ in range(n): w=''.join(sub[c] for c in w)
    return w
w=grow(9)

print("=== two graphs on the four letters ===")
# 1) the CONVERSATION: undirected adjacency actually occurring in the word
adj=set()
for x,y in zip(w,w[1:]): adj.add(frozenset((x,y)) if x!=y else frozenset((x,)))
pairs=[frozenset(p) for p in combinations('abAB',2)]
present=[p for p in pairs if p in adj]
absent =[p for p in pairs if p not in adj]
print("  the 6 possible letter-pairs; which ever appear ADJACENT in the word:")
for p in pairs: print(f"    {''.join(sorted(p))}: {'appears' if p in adj else 'NEVER adjacent'}")
print("  => the conversation graph = K4 minus", [''.join(sorted(p)) for p in absent])

print("\n=== the swap s (a<->A, b<->B) acting on the six kappa(x,y) = tr[x,y] ===")
swap={'a':'A','A':'a','b':'B','B':'b'}
def sk(p): return frozenset(swap[x] for x in p)
orbits=[]; seen=set()
for p in pairs:
    if p in seen: continue
    q=sk(p); 
    if q==p: orbits.append(('FIXED', ''.join(sorted(p)))); seen.add(p)
    else: orbits.append(('pair', ''.join(sorted(p)),''.join(sorted(q)))); seen|={p,q}
for o in orbits: print("   ", o)

print("\n=== the connection (threads 1+4) ===")
print("  swap-FIXED kappas: kappa(a,A) and kappa(b,B)  -- the same-role couplings")
print("  these are EXACTLY the symplectic pairs from Movement II (D pairs a<->A and b<->B).")
print("  and kappa(b,B): the couriers -- is bB the missing conversation edge?",
      frozenset(('b','B')) in absent)
print("  => the ONE pair the object never says aloud (bB) is a swap-fixed, symplectic-paired")
print("     interaction: the couriers touch only through the character variety, never in the word.")
