#!/usr/bin/env python3
"""One sweep, two base rates (memo 231 cells 1 and 3), own code:
 - orientation-aware amphichirality over the one-cusped orientable census (cell 1: 181/203123)
 - |det(A-I)| over orientation-preserving cusp-fixing isometries, first 4000 of OrientableCuspedCensus, all cusp numbers (cell 3: 2/4000 attain 3; 3595/4000 max 4)
Writes JSON incrementally."""
import json, sys, time, snappy, pathlib
OUT=pathlib.Path(__file__).with_suffix('.json')
mode=sys.argv[1]
def isos(M):
    try: return M.isomorphisms_to(M)
    except Exception as e: return None
def det2(m): return m[0][0]*m[1][1]-m[0][1]*m[1][0]
def cusp_map(iso,i):
    cm=iso.cusp_maps()[i]; return [[int(cm[0][0]),int(cm[0][1])],[int(cm[1][0]),int(cm[1][1])]]
t0=time.time()
if mode=='det':
    N=int(sys.argv[2]) if len(sys.argv)>2 else 4000
    rows=[]; attain={}; maxv={}; rejected_rev=0; 
    for k,M in enumerate(snappy.OrientableCuspedCensus()):
        if k>=N: break
        L=isos(M); vals=[]; 
        if L is None: rows.append((M.name(),None)); continue
        for iso in L:
            imgs=iso.cusp_images()
            for i in range(M.num_cusps()):
                if imgs[i]!=i: continue
                A=cusp_map(iso,i); d=det2(A)
                if d!=1: rejected_rev+=1; continue
                vals.append(abs(det2([[A[0][0]-1,A[0][1]],[A[1][0],A[1][1]-1]])))
        rows.append((M.name(),sorted(vals)))
        for v in set(vals): attain[v]=attain.get(v,0)+1
        mv=max(vals) if vals else None; maxv[mv]=maxv.get(mv,0)+1
        if k%500==0: print(k, M.name(), round(time.time()-t0), flush=True)
    three=[r[0] for r in rows if r[1] and 3 in r[1]]
    res={'N':len(rows),'attain':{str(k):v for k,v in attain.items()},'max':{str(k):v for k,v in maxv.items()},'attain_3':three,'rejected_orientation_reversing_rows':rejected_rev,
         'm004':[r[1] for r in rows if r[0]=='m004'],'seconds':round(time.time()-t0)}
    json.dump(res,open(OUT.with_name('det_sweep.json'),'w'),indent=1); print(json.dumps({k:v for k,v in res.items()},indent=1))
elif mode=='chir':
    N=int(sys.argv[2]) if len(sys.argv)>2 else None
    amph=[]; n=0; errs=[]
    for k,M in enumerate(snappy.OrientableCuspedCensus(cusps=1)):
        if N and k>=N: break
        n+=1
        L=isos(M)
        if L is None: errs.append(M.name()); continue
        if any(det2(cusp_map(iso,0))==-1 for iso in L): amph.append(M.name())
        if k%5000==0:
            print(k, M.name(), len(amph), round(time.time()-t0), flush=True)
            json.dump({'swept':n,'amphichiral':len(amph),'errors':errs,'partial':True},open(OUT.with_name('chir_sweep.json'),'w'))
    res={'swept':n,'amphichiral':len(amph),'chiral':n-len(amph),'errors':errs,'amphichiral_names_first_40':amph[:40],'m004_in':'m004' in amph,'seconds':round(time.time()-t0)}
    json.dump(res,open(OUT.with_name('chir_sweep.json'),'w'),indent=1); print(json.dumps(res,indent=1))
