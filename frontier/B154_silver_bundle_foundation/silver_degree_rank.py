"""Silver degree=rank with the DERIVED metallic meridian mu = A^-m t (m=2 for silver).
phi_silver([A,B]) = A^2 [A,B] A^-2  =>  mu=A^-2 t commutes with [A,B] (the cusp meridian).
Test the MATRIX identity [A,B] = +- mu^k across all irreducible silver reps, at SL(3) {1,w,w^2},{1,i,-i}
and SL(4) {1,1,w,w^2}. Report: commuting, the sub-locus count, exactness, conditioning, the exponent k.
"""
import numpy as np

def silver_resid(A,B,t):
    Ai=np.linalg.inv(A)
    return np.concatenate([(t@B@B - Ai@t@A).reshape(-1),(t@B - A@A@B@t).reshape(-1)])
def newton_BT(A,rng,iters=700):
    n=A.shape[0]; x=rng.standard_normal(2*n*n)+1j*rng.standard_normal(2*n*n)
    sp=lambda x:(x[:n*n].reshape(n,n),x[n*n:].reshape(n,n))
    for _ in range(iters):
        B,t=sp(x); g=np.concatenate([silver_resid(A,B,t),[np.linalg.det(B)-1,np.linalg.det(t)-1]])
        if np.max(np.abs(g))<1e-12: break
        h=1e-7; J=np.zeros((g.size,2*n*n),complex)
        for k in range(2*n*n):
            xp=x.copy(); xp[k]+=h; Bp,tp=sp(xp)
            gp=np.concatenate([silver_resid(A,Bp,tp),[np.linalg.det(Bp)-1,np.linalg.det(tp)-1]])
            J[:,k]=(gp-g)/h
        st,*_=np.linalg.lstsq(J,g,rcond=None); x=x-st
    B,t=sp(x); return B,t,np.max(np.abs(silver_resid(A,B,t)))
def is_irred(A,B,rounds=6,tol=1e-7):
    n=A.shape[0]; gens=[A,B,np.linalg.inv(A),np.linalg.inv(B)]
    allm=[np.eye(n,dtype=complex)]; fr=[np.eye(n,dtype=complex)]
    for _ in range(rounds): fr=[g@m for m in fr for g in gens]; allm+=fr
    return np.linalg.matrix_rank(np.array([m.reshape(-1) for m in allm]),tol=tol)==n*n

w=np.exp(2j*np.pi/3)
cases={"SL3 {1,w,w^2}":[1,w,w**2], "SL3 {1,i,-i}":[1,1j,-1j], "SL4 {1,1,w,w^2}":[1,1,w,w**2]}
for name,sp in cases.items():
    A=np.diag(np.array(sp,dtype=complex)); n=A.shape[0]
    rng=np.random.default_rng(7); nirr=0; hits={}; commerrs=[]; idconds=[]; iderrs=[]
    nseed=200 if n==4 else 160
    for s in range(nseed):
        B,t,res=newton_BT(A,rng)
        if res<1e-9 and abs(np.linalg.det(t))>1e-3 and np.linalg.cond(t)<1e4 and is_irred(A,B):
            nirr+=1
            lam=A@B@np.linalg.inv(A)@np.linalg.inv(B); mu=np.linalg.inv(A@A)@t
            commerrs.append(np.max(np.abs(mu@lam-lam@mu)))
            for k in range(1,12):
                for sgn in (1,-1):
                    err=np.max(np.abs(lam - sgn*np.linalg.matrix_power(mu,k)))
                    if err<1e-7:
                        hits[(sgn,k)]=hits.get((sgn,k),0)+1
                        idconds.append(np.linalg.cond(t)); iderrs.append(err)
    commmax=max(commerrs) if commerrs else float('nan')
    print(f"{name}: irreducible {nirr}; mu=A^-2 t commutes with [A,B] (max ||[.,.]||={commmax:.1e})")
    print(f"   MATRIX [A,B]=s*mu^k holds (count by (s,k)): {dict(sorted(hits.items()))}")
    if iderrs: print(f"   on-identity reps: max err {max(iderrs):.1e}, cond(t) median {np.median(idconds):.1f}")
