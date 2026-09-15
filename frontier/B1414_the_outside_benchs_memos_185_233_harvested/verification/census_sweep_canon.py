#!/usr/bin/env python3
"""Same two sweeps as census_sweep.py but with the isometries taken on the CANONICAL triangulation
(M.is_isometric_to(M, return_isometries=True) canonizes), not on the census triangulation as given."""
import json, sys, time, snappy, pathlib
mode=sys.argv[1]; t0=time.time()
def det2(m): return m[0][0]*m[1][1]-m[0][1]*m[1][0]
def cusp_map(iso,i):
    cm=iso.cusp_maps()[i]; return [[int(cm[0][0]),int(cm[0][1])],[int(cm[1][0]),int(cm[1][1])]]
def isos(M):
    try: return M.is_isometric_to(M, return_isometries=True)
    except Exception as e: return None
if mode=='det':
    N=int(sys.argv[2]); rows=[]; attain={}; maxv={}; rej=0; errs=[]
    for k,M in enumerate(snappy.OrientableCuspedCensus()):
        if k>=N: break
        L=isos(M)
        if L is None: errs.append(M.name()); continue
        vals=[]
        for iso in L:
            imgs=iso.cusp_images()
            for i in range(M.num_cusps()):
                if imgs[i]!=i: continue
                A=cusp_map(iso,i)
                if det2(A)!=1: rej+=1; continue
                vals.append(abs(det2([[A[0][0]-1,A[0][1]],[A[1][0],A[1][1]-1]])))
        rows.append((M.name(),sorted(vals)))
        for v in set(vals): attain[v]=attain.get(v,0)+1
        mv=max(vals) if vals else None; maxv[str(mv)]=maxv.get(str(mv),0)+1
    res={'N':len(rows),'errors':errs,'attain':{str(k):v for k,v in sorted(attain.items())},'max':maxv,'attain_3':[r[0] for r in rows if 3 in r[1]],'attain_1_2':[(r[0],r[1]) for r in rows if 1 in r[1] or 2 in r[1]],
         'rejected_orientation_reversing_rows':rej,'m004':[r[1] for r in rows if r[0]=='m004'],'seconds':round(time.time()-t0)}
    json.dump(res,open('det_sweep_canon.json','w'),indent=1); print(json.dumps(res,indent=1))
else:
    amph=[]; n=0; errs=[]; sym_disagree=[]
    for k,M in enumerate(snappy.OrientableCuspedCensus(cusps=1)):
        n+=1; L=isos(M)
        if L is None: errs.append(M.name()); continue
        a=any(det2(cusp_map(iso,0))==-1 for iso in L)
        if a: amph.append(M.name())
        if k%20000==0:
            print(k,M.name(),len(amph),round(time.time()-t0),flush=True)
            json.dump({'swept':n,'amphichiral':len(amph),'partial':True},open('chir_sweep_canon.json','w'))
    res={'swept':n,'amphichiral':len(amph),'chiral':n-len(amph),'errors':errs,'names':amph,'seconds':round(time.time()-t0)}
    json.dump(res,open('chir_sweep_canon.json','w'),indent=1); print(json.dumps({k:v for k,v in res.items() if k!='names'},indent=1))
