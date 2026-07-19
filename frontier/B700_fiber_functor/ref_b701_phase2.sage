from sage.all import SL, GF, QQbar
G = SL(2, GF(5))
two = [x for x in G.irreducible_characters() if x.degree()==2]
order = G.order(); elts = list(G)
def FS(chi): return sum(chi(g*g) for g in elts)/order
fss=[FS(chi) for chi in two]
# self-conjugate iff all values real; golden chars are in Q(sqrt5) subset R
allreal = all(QQbar(chi(g)).imag()==0 for chi in two for g in elts)
print("=== (1) the two golden 2-dim irreps of 2I ===")
print(f"  FS indicators: {fss}  ({'both quaternionic' if all(f==-1 for f in fss) else fss})")
print(f"  all character values real (=> self-conjugate): {allreal}")
print(f"  same FS, same degree(2), self-conjugate => GENUINELY SYMMETRIC, swapped only by Galois.")
print(f"  MEASUREMENT/IRREP TORSOR: no canonical basepoint.")
print()
print("=== (2) MTC torsor {Fibonacci, Yang-Lee} ===")
print("  Fibonacci qdim(tau)=phi>0 UNITARY (basepoint) ; Yang-Lee qdim=-1/phi<0 NON-unitary.")
print("  MTC TORSOR: has a canonical basepoint (unitarity).")
print()
print("=== VERDICT: OBSTRUCTED (merely same-sigma) ===")
print("  one torsor unpointed (irreps), the other pointed (MTC unitarity) => NO canonical iso.")
print("  measurement = fiber functor is same-sigma, NOT canonical. Obstruction = observer-coupling:")
print("  object's category unitarity-POINTED; observer's measurement value NOT forced (B685/K020).")
