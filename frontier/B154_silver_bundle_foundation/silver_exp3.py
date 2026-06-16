import numpy as np
def resid(A,B,t):
    Ai=np.linalg.inv(A); return np.concatenate([(t@B@B-Ai@t@A).reshape(-1),(t@B-A@A@B@t).reshape(-1)])
def newton(A,rng,iters=120):
    n=A.shape[0]; x=rng.standard_normal(2*n*n)+1j*rng.standard_normal(2*n*n)
    sp=lambda x:(x[:n*n].reshape(n,n),x[n*n:].reshape(n,n)); prev=9
    for _ in range(iters):
        B,t=sp(x); g=np.concatenate([resid(A,B,t),[np.linalg.det(B)-1,np.linalg.det(t)-1]])
        m=np.max(np.abs(g))
        if m<1e-12: break
        if m>1e6: return None,None,9          # diverged, bail early
        h=1e-7; J=np.zeros((g.size,2*n*n),complex)
        for k in range(2*n*n):
            xp=x.copy(); xp[k]+=h; Bp,tp=sp(xp)
            gp=np.concatenate([resid(A,Bp,tp),[np.linalg.det(Bp)-1,np.linalg.det(tp)-1]])
            J[:,k]=(gp-g)/h
        try: st,*_=np.linalg.lstsq(J,g,rcond=None)
        except np.linalg.LinAlgError: return None,None,9
        x=x-st
    B,t=sp(x); return B,t,np.max(np.abs(resid(A,B,t)))
def irred(A,B,rounds=4,tol=1e-7):
    n=A.shape[0]; gens=[A,B,np.linalg.inv(A),np.linalg.inv(B)]
    allm=[np.eye(n,dtype=complex)]; fr=[np.eye(n,dtype=complex)]
    for _ in range(rounds): fr=[g@m for m in fr for g in gens]; allm+=fr
    return np.linalg.matrix_rank(np.array([m.reshape(-1) for m in allm]),tol=tol)==n*n
def expo(A,B,t):
    lam=A@B@np.linalg.inv(A)@np.linalg.inv(B); mu=np.linalg.inv(A@A)@t
    for k in range(1,13):
        for s in (1,-1):
            if np.max(np.abs(lam-s*np.linalg.matrix_power(mu,k)))<1e-6: return (s,k)
    return None
w=np.exp(2j*np.pi/3); i_=1j
for n,name,sp in [(3,"o3 {1,w,w2}",[1,w,w**2]),(3,"o4 {1,i,-i}",[1,i_,-i_]),
                  (4,"o3 {1,1,w,w2}",[1,1,w,w**2]),(4,"o4 {1,1,i,-i}",[1,1,i_,-i_])]:
    sp=np.array(sp,dtype=complex); sp=sp/(np.prod(sp))**(1.0/n); A=np.diag(sp)
    rng=np.random.default_rng(0); exps={}; tot=0
    for s in range(150):
        B,t,r=newton(A,rng)
        if B is None or r>1e-9 or abs(np.linalg.det(t))<1e-3 or np.linalg.cond(t)>1e4: continue
        if not irred(A,B): continue
        e=expo(A,B,t)
        if e: exps[e]=exps.get(e,0)+1; tot+=1
        if tot>=3: break
    print(f"n={n} {name:14s}: exponents {dict(sorted(exps.items()))}", flush=True)
