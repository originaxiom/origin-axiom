#!/usr/bin/env python3
"""B476 addendum reproducer: the metallic pair's Weil-rep decomposition per level.
level 3 -> 1+2, level 5 -> 2+3, level 15 -> 2+3+4+6 (CRT tensor of the two). This is
the classical Weil reducibility (p+-1)/2, NOT SU(5) branching (see S058)."""
import numpy as np
np.seterr(all='ignore'); mp=np.linalg.matrix_power
def weil(N):
    z=np.exp(2j*np.pi/N)
    D=np.diag([z**((j*(j-1)//2)%N) for j in range(N)])
    F=np.array([[z**((i*j)%N) for j in range(N)] for i in range(N)])/np.sqrt(N)
    WR=(F@D@F.conj().T).conj().T
    return mp(WR,1)@mp(D,1), mp(WR,2)@mp(D,2)
def commutant_blocks(mats,n):
    rows=[np.kron(np.eye(n),W)-np.kron(W.T,np.eye(n)) for W in mats]
    U,s,Vh=np.linalg.svd(np.vstack(rows)); tol=1e-8*s[0]
    ns=[Vh[i].conj().reshape(n,n) for i in range(Vh.shape[0]) if i>=len(s) or s[i]<tol]
    X=sum((k+1.7)*M for k,M in enumerate(ns)); ev=np.linalg.eigvals(X); g={}
    for e in ev:
        key=tuple(np.round([e.real,e.imag],4)); g[key]=g.get(key,0)+1
    return len(ns), sorted(g.values())
for N in (3,5,15):
    cd,bl=commutant_blocks(list(weil(N)),N)
    print(f"level {N}: commutant dim={cd}, blocks={bl}")
