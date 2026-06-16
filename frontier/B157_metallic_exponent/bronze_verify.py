"""INDEPENDENT verification of the BRONZE (m=3) k-values (refutation of k=4-m(o-3)).

Independent code path: build the bundle rep from the FULL relations directly
   tAt^-1 = phi(A),  tBt^-1 = phi(B),  with phi(B)=A^m B, phi(A)=A (A^m B)^m,
solve for t given (A,B) AND for B, by Newton on (B,t) using the FULL (un-eliminated) relations.
Then read k in [A,B]=s mu^k, mu=A^-m t. Gate: irreducible (Burnside), non-central longitude, FULL
relations satisfied (not just eliminated). Cross-check m=1 (k=4@o3, k=3@o4), m=2 (k=4@o3,k=2@o4) first.
"""
import numpy as np
from collections import Counter

def phi(A,B,m):
    AmB = np.linalg.matrix_power(A,m) @ B
    return A @ np.linalg.matrix_power(AmB, m), AmB    # phi(A), phi(B)

def full_resid(A,B,t,m):
    phiA, phiB = phi(A,B,m); ti=np.linalg.inv(t)
    return np.concatenate([(t@A@ti - phiA).reshape(-1), (t@B@ti - phiB).reshape(-1)])

def newton_full(A,m,rng,iters=300):
    n=A.shape[0]; x=rng.standard_normal(2*n*n)+1j*rng.standard_normal(2*n*n)
    split=lambda x:(x[:n*n].reshape(n,n),x[n*n:].reshape(n,n))
    for _ in range(iters):
        B,t=split(x)
        if abs(np.linalg.det(t))<1e-9: return None
        g=np.concatenate([full_resid(A,B,t,m),[np.linalg.det(B)-1,np.linalg.det(t)-1]])
        mx=np.max(np.abs(g))
        if mx<1e-12: break
        if mx>1e7: return None
        h=1e-7; J=np.zeros((g.size,2*n*n),complex)
        for k in range(2*n*n):
            xp=x.copy(); xp[k]+=h; Bp,tp=split(xp)
            if abs(np.linalg.det(tp))<1e-12: return None
            gp=np.concatenate([full_resid(A,Bp,tp,m),[np.linalg.det(Bp)-1,np.linalg.det(tp)-1]]); J[:,k]=(gp-g)/h
        try: st,*_=np.linalg.lstsq(J,g,rcond=None)
        except: return None
        x=x-st
    B,t=split(x)
    return (B,t) if (abs(np.linalg.det(t))>1e-6 and np.max(np.abs(full_resid(A,B,t,m)))<1e-9) else None

def irred(A,B,r=6,tol=1e-7):
    n=A.shape[0]; gens=[A,B,np.linalg.inv(A),np.linalg.inv(B)]; allm=[np.eye(n,dtype=complex)]; fr=[np.eye(n,dtype=complex)]
    for _ in range(r): fr=[g@m2 for m2 in fr for g in gens]; allm+=fr
    return np.linalg.matrix_rank(np.array([m2.reshape(-1) for m2 in allm]),tol=tol)==n*n

def kread(A,B,t,m,kmax=12):
    Ai=np.linalg.inv(A); comm=A@B@Ai@np.linalg.inv(B); mu=np.linalg.matrix_power(Ai,m)@t
    best=(None,None,9e9)
    for k in range(1,kmax+1):
        for s in (1,-1):
            e=np.max(np.abs(comm-s*np.linalg.matrix_power(mu,k)))
            if e<best[2]: best=(s,k,e)
    # non-central longitude
    offc=np.max(np.abs(comm-np.trace(comm)/A.shape[0]*np.eye(A.shape[0])))
    return best, offc

w=np.exp(2j*np.pi/3); i_=1j
cases=[(1,3,[1,w,w**2],"k=4"),(1,4,[1,i_,-i_],"k=3"),
       (2,3,[1,w,w**2],"k=4"),(2,4,[1,i_,-i_],"k=2"),
       (3,3,[1,w,w**2],"BRONZE expect k=1"),(3,4,[1,i_,-i_],"BRONZE expect k=3")]
print("INDEPENDENT (full-relation Newton) k in [A,B]=s mu^k, mu=A^-m t, SL(3):")
for m,o,spec,exp in cases:
    sp=np.array(spec,complex); sp=sp/np.prod(sp)**(1/3); A=np.diag(sp)
    cnt=Counter(); reps=0
    for seedbase in (5,77):
        rng=np.random.default_rng(seedbase)
        for s in range(500):
            r=newton_full(A,m,rng)
            if r is None: continue
            B,t=r
            if np.linalg.cond(t)>1e4 or not irred(A,B): continue
            (sg,k,e),offc=kread(A,B,t,m)
            if e<1e-7 and offc>1e-4:
                cnt[(sg,k)]+=1; reps+=1
            if reps>=4: break
        if reps>=4: break
    print(f"  m={m} o={o} [{exp:18s}]: {dict(cnt)}  (reps {reps})")
