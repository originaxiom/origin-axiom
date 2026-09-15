#!/usr/bin/env python3
"""B1321's own golden-face test (its functions, executed from its script text up to the sweep) applied to the class members its
raw isomorphisms_to enumeration missed, with the isometries taken on the canonical triangulation."""
import pathlib, sys, json, warnings; warnings.filterwarnings("ignore")
src=pathlib.Path('frontier/B1321_l205_the_siblings_localized_count/verification/b1321_class_search.py').read_text()
head=src.split('t1, t2 = sp.symbols("t1 t2"); out = dict(')[0]
ns={}; exec(head, ns)
sp=ns['sp']; snappy=ns['snappy']
def cusp_rows_canon(N):
    rows=[]
    for iso in N.is_isometric_to(N, return_isometries=True):
        for c,(img,A) in enumerate(zip(iso.cusp_images(), iso.cusp_maps())):
            if img!=c: continue
            a,b,cc,d=int(A[0,0]),int(A[0,1]),int(A[1,0]),int(A[1,1]); rows.append((c,a*d-b*cc,abs((a-1)*(d-1)-b*cc)))
    return rows
t1,t2=sp.symbols("t1 t2"); out=[]
for name in ['m202','s959','v3461','v3551','o9_40999','o9_43931','t10829','t12582','o9_42897']:
    N=snappy.Manifold(name); rows=cusp_rows_canon(N); rows_raw=ns['cusp_rows'](N)
    three=[r for r in rows if r[1]==1 and r[2]==3]; three_raw=[r for r in rows_raw if r[1]==1 and r[2]==3]
    G=N.fundamental_group(); D,how=ns['alexander_two_var'](G,(t1,t2))
    rec=dict(name=name,H1=str(N.homology()),cusps_with_3=sorted({r[0] for r in three}),raw_found_3=bool(three_raw),presentation=how)
    if D is not None:
        nprims,hits=ns['golden_test'](D,(t1,t2)); rec.update(primitive_classes=nprims,golden_hits=hits,delta=str(D)[:160])
    out.append(rec); print(rec, flush=True)
json.dump(out,open('audit/scratch_paper/ob_harvest/golden_new_members.json','w'),indent=1,default=str)
print('golden-face members among the nine:', [r['name'] for r in out if r.get('golden_hits')])
