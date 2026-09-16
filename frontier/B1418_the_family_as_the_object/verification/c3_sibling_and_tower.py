#!/usr/bin/env python3
"""B1418 cell 3 -- THE SIBLING AND THE TOWER: m202 and s959 (the count-of-three members) against the class: symmetry groups
(canonical), covering relations to every one-cusped class member of smaller volume (degree <= 5), and the seven covers of
m004 in the family (degree, cusps, chirality, door, three) -- pre-registered: none of the covers attains the three."""
import json, pathlib, snappy
HERE=pathlib.Path(__file__).resolve().parent; ROOT=HERE.parents[2]
fam=json.load(open(ROOT/'frontier/B1186_family_is_112/verification/family_census.json')); A=fam['members_A']; B=fam['members_B']
def det2(m): return m[0][0]*m[1][1]-m[0][1]*m[1][0]
def cm(iso,i):
    c=iso.cusp_maps()[i]; return [[int(c[0][0]),int(c[0][1])],[int(c[1][0]),int(c[1][1])]]
def facts(M):
    L=M.is_isometric_to(M,return_isometries=True); vals=set()
    for iso in L:
        for i in range(M.num_cusps()):
            if iso.cusp_images()[i]!=i: continue
            X=cm(iso,i)
            if det2(X)!=1: continue
            vals.add(abs(det2([[X[0][0]-1,X[0][1]],[X[1][0],X[1][1]-1]])))
    return {'sym':len(L),'chiral':not any(det2(cm(iso,0))==-1 for iso in L),'det_values':sorted(vals),'three':3 in vals,'cusps':M.num_cusps(),'vol':float(M.volume()),'H1':str(M.homology())}
v0=float(snappy.Manifold('m004').volume()); out={}
one=[n for n in B if snappy.Manifold(n).num_cusps()==1]
for name in ('m202','s959'):
    M=snappy.Manifold(name); f=facts(M); f['vol/m004']=round(f['vol']/v0,6); f['in_A']=name in A; f['covers_of']=[]
    for base in one:
        Nb=snappy.Manifold(base); r=f['vol']/float(Nb.volume()); d=round(r)
        if abs(r-d)<1e-6 and 2<=d<=5:
            if any(M.is_isometric_to(C) for C in Nb.covers(d)): f['covers_of'].append((base,d))
    out[name]=f; print(name,f,flush=True)
covers={'m206':2,'s961':3,'t12839':4,'t12840':4,'o10_150685':5,'o10_150696':5,'o10_150703':5}
tab={}
for n,d in covers.items():
    M=snappy.Manifold(n); f=facts(M); f['degree']=d; tab[n]=f; print(n,f,flush=True)
print('pre-registered: none of the covers attains the three ->', all(not f['three'] for f in tab.values()))
print('class-level statement (A): the count of three occurs only on two-cusped members that are not covers of m004 ->', all(out[n]['cusps']==2 and not out[n]['covers_of'] for n in out))
json.dump({'siblings':out,'covers':tab},open(HERE/'c3_sibling_and_tower.json','w'),indent=1,default=str)
