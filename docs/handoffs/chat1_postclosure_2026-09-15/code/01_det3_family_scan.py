#!/usr/bin/env python3
"""det(A-I)=3 family scan. CORRECTED instrument (cusp-fixing filter).
Result: family GROWS with scan size -- 2@4k, 4@6k, 6@20k. Not finite, not selected."""
import snappy
HEX=complex(0.5,0.8660254037844386)
def dets_fixing(M):
    G=M.symmetry_group(); out=set(); ident=tuple(range(M.num_cusps()))
    for I in G.isometries():
        try:
            if tuple(I.cusp_images())!=ident: continue
        except Exception: continue
        for m in I.cusp_maps():
            if int(m[0,0]*m[1,1]-m[0,1]*m[1,0])==1: out.add(2-int(m[0,0]+m[1,1]))
    return out
def scan(N):
    hits=[]
    for k,M in enumerate(snappy.OrientableCuspedCensus):
        if k>=N: break
        try:
            if M.num_cusps()!=2: continue
            sh=[complex(s) for s in M.cusp_info('shape')]
            if not all(min(abs(s-HEX),abs(s-HEX.conjugate()))<1e-8 for s in sh): continue
            if 3 in dets_fixing(M):
                v=float(M.volume())
                hits.append((str(M).split('(')[0], v, v/0.169156934, str(M.homology()), str(M.symmetry_group())))
        except Exception: pass
    return hits
if __name__=="__main__":
    for N in (4000,6000,20000):
        h=scan(N); print(f"N={N:6d}: {len(h)} members  {[x[0] for x in h]}")
    for nm,v,idx,hh,sym in scan(20000):
        print(f"  {nm:8s} vol {v:12.9f} idx {idx:8.3f} integral {abs(idx-round(idx))<1e-3} H1 {hh:18s} {sym}")
