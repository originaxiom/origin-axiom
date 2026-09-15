import snappy, json
C = snappy.OrientableCuspedCensus
rows=[]; N=len(C); print("census size", N, flush=True)
for i,M in enumerate(C):
    try:
        G=M.symmetry_group()
        if not G.is_amphicheiral(): continue
        cs=float(M.chern_simons())%0.5
        cls = 0 if min(cs,0.5-cs)<1e-8 else (1 if abs(cs-0.25)<1e-8 else 9)
        isos=G.isometries()
        def det(g):
            m=g.cusp_maps()[0]; return int(m[0,0]*m[1,1]-m[0,1]*m[1,0])
        rev=[k for k,g in enumerate(isos) if det(g)==-1]
        def order(k):
            cur=k; n=1
            for _ in range(40):
                cur=G.multiply_elements(cur,k); n+=1
                if cur==0: return n
            return None
        orders={order(k) for k in rev}-{None}
        rows.append((M.name(), cls, str(M.homology()), G.order(), sorted(orders), 2 in orders))
    except Exception: pass
    if (i+1)%2000==0: print(f"  {i+1}/{N} amph={len(rows)}", flush=True)
json.dump(rows, open('wide.json','w'))
z=[r for r in rows if r[1]==0]; q=[r for r in rows if r[1]==1]; o=[r for r in rows if r[1]==9]
print(f"\namphichiral total {len(rows)}   class0={len(z)} class1/4={len(q)} OTHER={len(o)}")
print(f"  class 0   with orientation-reversing involution: {sum(1 for r in z if r[5])}/{len(z)}")
print(f"  class 1/4 with orientation-reversing involution: {sum(1 for r in q if r[5])}/{len(q)}")
bad=[r for r in q if r[5]]
print(f"  COUNTEREXAMPLES to 'involution => class 0': {len(bad)}  {bad[:6]}")
