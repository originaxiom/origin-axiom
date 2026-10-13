#!/usr/bin/env python3
"""Normalized inhomogeneous finite-group cochains over F3; Q8 and C3 control.
No classification of Spin-Q8 anomalies is attempted.
"""
from itertools import product
from pathlib import Path
import json
import numpy as np

OUT=Path(__file__).resolve().parent

def qmul(a,b):
    sa,ia=((-1,a-4) if a>=4 else (1,a))
    sb,ib=((-1,b-4) if b>=4 else (1,b))
    if ia==0:s,k=1,ib
    elif ib==0:s,k=1,ia
    elif ia==ib:s,k=-1,0
    else:s,k=(1 if (ia,ib) in [(1,2),(2,3),(3,1)] else -1),6-ia-ib
    return k+(4 if sa*sb*s==-1 else 0)

def coboundary(size,mul,n,p=3):
    cols=list(product(range(1,size),repeat=n));index={x:i for i,x in enumerate(cols)}
    rows=list(product(range(1,size),repeat=n+1))
    D=np.zeros((len(rows),len(cols)),dtype=np.int16)
    for r,g in enumerate(rows):
        terms=[(1,g[1:])]
        for j in range(n):
            terms.append(((-1)**(j+1),g[:j]+(mul(g[j],g[j+1]),)+g[j+2:]))
        terms.append(((-1)**(n+1),g[:-1]))
        for sign,t in terms:
            if 0 not in t:D[r,index[t]]+=sign
    return D%p

def rank_mod(A,p=3):
    M=A.copy()%p;r=0
    for j in range(M.shape[1]):
        cand=np.flatnonzero(M[r:,j])
        if not len(cand):continue
        k=r+int(cand[0]);M[[r,k]]=M[[k,r]]
        M[r]=(M[r]*pow(int(M[r,j]),-1,p))%p
        ids=np.flatnonzero(M[r+1:,j])+r+1
        # coefficients are at most p-1; int16 safe for this elementwise operation.
        if len(ids):M[ids]=(M[ids]-M[ids,j,None]*M[r,None,:])%p
        r+=1
        if r==M.shape[0]:break
    return r

res={};checks={}
for name,size,mul in [('Q8',8,qmul),('C3',3,lambda a,b:(a+b)%3)]:
    Ds=[coboundary(size,mul,n) for n in [1,2,3]]
    ranks=[rank_mod(D) for D in Ds]
    # product uses wider integer accumulation than cochain storage.
    squares=[not np.any((Ds[i+1].astype(np.int64)@Ds[i].astype(np.int64))%3) for i in [0,1]]
    checks[name+'_d_squared_zero']=all(squares)
    h2=Ds[1].shape[1]-ranks[1]-ranks[0]
    h3=Ds[2].shape[1]-ranks[2]-ranks[1]
    checks[name+'_expected_h2_h3']=(h2,h3)==((0,0) if name=='Q8' else (1,1))
    res[name]={'cochain_matrix_shapes':[list(D.shape) for D in Ds],'differential_ranks':ranks,'H2_F3_dimension':h2,'H3_F3_dimension':h3}
checks['Q8_lagrange_order_invertible_mod3']=(8%3)!=0
assert all(checks.values())
out={'checks':checks,'passed':sum(checks.values()),'cohomology':res,'scope':'Ordinary Q8 cohomology with trivial F3 coefficients, not full spin-Q8 bordism or defect-junction classification.'}
(OUT/'cocycle_results.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
