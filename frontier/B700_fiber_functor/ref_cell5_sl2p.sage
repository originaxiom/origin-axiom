from sage.all import SL, GF, CyclotomicField, QQ, kronecker_symbol
def pstar(p): return (-1)**((p-1)//2) * p
print(f"{'p':>3} {'p*':>5} {'#(p-1)/2-irreps':>15} {'field deg':>10} {'simply-transitive':>17}")
allok=True
for p in [5,7,11,13]:
    G = SL(2, GF(p)); ct = G.character_table(); D=(p-1)//2
    rows=[i for i in range(ct.nrows()) if ct[i][0]==D]
    K=CyclotomicField(p); z=K.gen()
    if len(rows)!=2: print(f"{p:>3} count {len(rows)} != 2"); allok=False; continue
    rA=[K(ct[rows[0]][j]) for j in range(ct.ncols())]
    rB=[K(ct[rows[1]][j]) for j in range(ct.ncols())]
    gens=[v for v in rA if v not in QQ]; deg=K.subfield(gens[0])[0].degree() if gens else 1
    g=sum(kronecker_symbol(a,p)*z**a for a in range(1,p)); assert g**2==pstar(p)
    n=next(a for a in range(2,p) if kronecker_symbol(a,p)==-1); sig=K.hom([z**n])
    swap=[sig(v) for v in rA]==rB; fixed=[sig(v) for v in rA]==rA
    ok = (deg==2 and swap and not fixed); allok = allok and ok
    print(f"{p:>3} {pstar(p):>5} {len(rows):>15} {deg:>10} {str(swap and not fixed):>17}  {'OK' if ok else 'FAIL'}")
print()
print("ALL PRIMES 5,7,11,13:", "STAGE-UNIFORM TORSOR" if allok else "FAILED")
print("classical ground: the (p+-1)/2-dim exceptional chars of SL(2,p) are Gauss-sum-valued")
print("(Schur/Frobenius) => Galois-conjugate over Q(sqrt p*); the pattern is a theorem, not luck.")
