"""Count-of-three under two readings of 'orientation-preserving cusp-fixing isometry'."""
import snappy, warnings, time; warnings.filterwarnings("ignore")
cen=snappy.OrientableCuspedCensus()
t0=time.time(); strictHits=[]; relaxHits=[]; errs=[]
for i,M in enumerate(cen):
    try:
        isos=M.is_isometric_to(M,return_isometries=True)
    except Exception:
        try:
            M=snappy.Manifold(M.name()); M.canonize(); isos=M.is_isometric_to(M,return_isometries=True)
        except Exception as e:
            errs.append(M.name()); continue
    nc=M.num_cusps(); s=set(); r=set()
    for iso in isos:
        try:
            cm=iso.cusp_maps(); ci=iso.cusp_images()
        except Exception: continue
        dets=[m[0,0]*m[1,1]-m[0,1]*m[1,0] for m in cm]
        if set(dets)!={1}: continue                       # orientation-preserving
        for k in range(nc):
            if ci[k]!=k: continue
            m=cm[k]; a=abs((m[0,0]-1)*(m[1,1]-1)-m[0,1]*m[1,0])
            r.add(a)
            if all(ci[j]==j for j in range(nc)): s.add(a)
    if 3 in s: strictHits.append((M.name(),nc))
    if 3 in r: relaxHits.append((M.name(),nc))
    if (i+1)%50000==0: print(f"  {i+1} ({time.time()-t0:.0f}s) strict={len(strictHits)} relaxed={len(relaxHits)} errs={len(errs)}",flush=True)
print("STRICT (isometry fixes every cusp):",len(strictHits))
print("RELAXED (isometry fixes the cusp in question):",len(relaxHits))
print("errors:",errs)
print("relaxed hits:",relaxHits)
print("cusp numbers among relaxed hits:",sorted({n for _,n in relaxHits}))
# first-4000 control
s4=[h for h in strictHits]; 
names4=set(M.name() for M in list(cen)[:4000])
print("strict hits inside the first 4000:",[h for h in strictHits if h[0] in names4])
print("relaxed hits inside the first 4000:",[h for h in relaxHits if h[0] in names4])
