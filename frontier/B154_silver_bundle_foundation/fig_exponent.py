# Figure-eight exponent test: is k determined by spectrum ORDER or by rank n?
# Figure-eight construction: B = A^-2 t A t^-1, relation (*) star=0; meridian mu=A^-1 t.
# Test off-principal spectra to separate k=n (rank) from k=f(order).
import numpy as np
def Bfrom(A,t): return np.linalg.inv(A@A)@t@A@np.linalg.inv(t)
def star(A,t):
    Ai=np.linalg.inv(A); A2i=np.linalg.inv(A@A); return t@A2i@t@A - Ai@t@A@t
def newton_t(A,rng,iters=300):
    n=A.shape[0]; t=rng.standard_normal((n,n))+1j*rng.standard_normal((n,n))
    for _ in range(iters):
        g=np.concatenate([star(A,t).reshape(-1),[np.linalg.det(t)-1]])
        if np.max(np.abs(g))<1e-12: break
        h=1e-7; tf=t.reshape(-1); J=np.zeros((g.size,n*n),complex)
        for k in range(n*n):
            tp=tf.copy(); tp[k]+=h
            gp=np.concatenate([star(A,tp.reshape(n,n)).reshape(-1),[np.linalg.det(tp.reshape(n,n))-1]])
            J[:,k]=(gp-g)/h
        try: st,*_=np.linalg.lstsq(J,g,rcond=None)
        except np.linalg.LinAlgError: return None,9
        t=(tf-st).reshape(n,n)
    return t,np.max(np.abs(star(A,t)))
def irred(A,B,rounds=4,tol=1e-7):
    n=A.shape[0]; gens=[A,B,np.linalg.inv(A),np.linalg.inv(B)]
    allm=[np.eye(n,dtype=complex)]; fr=[np.eye(n,dtype=complex)]
    for _ in range(rounds): fr=[g@m for m in fr for g in gens]; allm+=fr
    return np.linalg.matrix_rank(np.array([m.reshape(-1) for m in allm]),tol=tol)==n*n
def expo(A,t):
    B=Bfrom(A,t); lam=A@B@np.linalg.inv(A)@np.linalg.inv(B); mu=np.linalg.inv(A)@t
    for k in range(1,13):
        for s in (1,-1):
            if np.max(np.abs(lam-s*np.linalg.matrix_power(mu,k)))<1e-6: return (s,k)
    return None
w=np.exp(2j*np.pi/3); i_=1j
# (n, name, spectrum): principal controls + OFF-principal tests
cases=[(3,"o4 {1,i,-i} (PRINCIPAL, expect k=3)",[1,i_,-i_]),
       (3,"o3 {1,w,w2} (OFF-principal: k=4=>order, k=3=>rank)",[1,w,w**2]),
       (4,"o3 {1,1,w,w2} (PRINCIPAL, expect k=4)",[1,1,w,w**2]),
       (4,"o4 {1,1,i,-i} (OFF-principal: k=2=>order, k=4=>rank)",[1,1,i_,-i_])]
for n,name,sp in cases:
    sp=np.array(sp,dtype=complex); sp=sp/(np.prod(sp))**(1.0/n); A=np.diag(sp)
    rng=np.random.default_rng(0); exps={}; tot=0
    for s in range(150):
        t,r=newton_t(A,rng)
        if t is None or r>1e-9 or abs(np.linalg.det(t))<1e-3 or np.linalg.cond(t)>1e4: continue
        B=Bfrom(A,t)
        if not irred(A,B): continue
        e=expo(A,t)
        if e: exps[e]=exps.get(e,0)+1; tot+=1
        if tot>=3: break
    print(f"FIG n={n} {name}: exponents {dict(sorted(exps.items()))}", flush=True)
