#!/usr/bin/env python3
"""(a) |det(A-I)|=3 class search over the FULL OrientableCuspedCensus (61911), isometries on the canonical triangulation
(B1321 used isomorphisms_to on the triangulation as given). (b) chirality of the covers of m004 to degree 10 by canonical
isometries (B1324 claims 66 of 87 chiral) and B1295's isometry/cusp-fixing counts."""
import json, time, snappy
t0=time.time()
def det2(m): return m[0][0]*m[1][1]-m[0][1]*m[1][0]
def cm(iso,i):
    c=iso.cusp_maps()[i]; return [[int(c[0][0]),int(c[0][1])],[int(c[1][0]),int(c[1][1])]]
def canon_isos(M): return M.is_isometric_to(M,return_isometries=True)
res={}
three=[]; n=0; errs=[]
for M in snappy.OrientableCuspedCensus():
    n+=1
    try: L=canon_isos(M)
    except Exception: errs.append(M.name()); continue
    vals=set()
    for iso in L:
        for i in range(M.num_cusps()):
            if iso.cusp_images()[i]!=i: continue
            A=cm(iso,i)
            if det2(A)!=1: continue
            vals.add(abs(det2([[A[0][0]-1,A[0][1]],[A[1][0],A[1][1]-1]])))
    if 3 in vals: three.append(M.name())
res['full_census']={'N':n,'errors':errs,'attain_3':three,'seconds':round(time.time()-t0)}
print(res['full_census'],flush=True)
# covers of m004 to degree 10
t0=time.time(); M=snappy.Manifold('m004'); rows=[]; n_iso=0; pairs=0; mult={}
for d in range(2,11):
    for C in M.covers(d):
        L=canon_isos(C); Lraw=C.isomorphisms_to(C)
        amph=any(det2(cm(iso,0))==-1 for iso in L)
        amph_raw=any(det2(cm(iso,0))==-1 for iso in Lraw)
        n_iso+=len(L)
        for iso in L:
            for i in range(C.num_cusps()):
                if iso.cusp_images()[i]!=i: continue
                A=cm(iso,i)
                if det2(A)!=1: continue
                pairs+=1; v=abs(det2([[A[0][0]-1,A[0][1]],[A[1][0],A[1][1]-1]])); mult[v]=mult.get(v,0)+1
        rows.append({'deg':d,'type':C.cover_info()['type'],'cusps':C.num_cusps(),'iso_canon':len(L),'iso_raw':len(Lraw),'amph_canon':amph,'amph_raw':amph_raw})
res['covers_to_10']={'n':len(rows),'chiral_canon':sum(not r['amph_canon'] for r in rows),'chiral_raw':sum(not r['amph_raw'] for r in rows),
  'raw_undercounts':sum(r['iso_raw']<r['iso_canon'] for r in rows),'disagree_chirality':[r for r in rows if r['amph_canon']!=r['amph_raw']],
  'isometries_total_canon':n_iso,'cusp_fixing_pairs_canon':pairs,'det_multiset_canon':{str(k):v for k,v in sorted(mult.items())},'seconds':round(time.time()-t0)}
print(res['covers_to_10'])
json.dump(res,open('canon_full.json','w'),indent=1)
