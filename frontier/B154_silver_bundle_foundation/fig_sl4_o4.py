# Fast figure-eight solver (analytic star Jacobian) to reach the o=4/SL(4) corner: {1,1,i,-i}@n4.
# Tests order-vs-rank AND the formula k=4-m(o-3): o=4,m=1 => predicts k=3 (order); rank would give k=4.
# Control: {1,1,w,w2}@n4 (o=3) => k=4.
import numpy as np
def Bfrom(A,t): return np.linalg.inv(A@A)@t@A@np.linalg.inv(t)
def star(A,t):
    Ai=np.linalg.inv(A); A2i=np.linalg.inv(A@A); return t@A2i@t@A - Ai@t@A@t
def newton(A,rng,iters=200):
    n=A.shape[0]; Ai=np.linalg.inv(A); A2i=np.linalg.inv(A@A)
    t=rng.standard_normal((n,n))+1j*rng.standard_normal((n,n))
    for _ in range(iters):
        s=star(A,t); dts=np.linalg.det(t)-1
        g=np.concatenate([s.reshape(-1),[dts]]); 
        if np.max(np.abs(g))<1e-12: break
        if np.max(np.abs(g))>1e7: return None
        # analytic Jacobian of star wrt t (A fixed): dstar = dt A2i t A + t A2i dt A - Ai dt A t - Ai t A dt
        cols=[]; ti=np.linalg.inv(t)
        for i in range(n):
            for j in range(n):
                E=np.zeros((n,n),complex); E[i,j]=1
                ds=E@A2i@t@A + t@A2i@E@A - Ai@E@A@t - Ai@t@A@E
                cols.append(np.concatenate([ds.reshape(-1),[np.trace(ti@E)]]))  # d det t = det(t) tr(t^-1 dt)~tr(t^-1 dt) near det=1
        J=np.array(cols).T
        try: st,*_=np.linalg.lstsq(J,g,rcond=None)
        except: return None
        t=t-st.reshape(n,n)
    return t if np.max(np.abs(star(A,t)))<1e-9 else None
def irred(A,B,rounds=4,tol=1e-7):
    n=A.shape[0]; gens=[A,B,np.linalg.inv(A),np.linalg.inv(B)]
    allm=[np.eye(n,dtype=complex)]; fr=[np.eye(n,dtype=complex)]
    for _ in range(rounds): fr=[g@m for m in fr for g in gens]; allm+=fr
    return np.linalg.matrix_rank(np.array([m.reshape(-1) for m in allm]),tol=tol)==n*n
def expo(A,t):
    B=Bfrom(A,t); lam=A@B@np.linalg.inv(A)@np.linalg.inv(B); mu=np.linalg.inv(A)@t
    for k in range(1,13):
        for sg in (1,-1):
            if np.max(np.abs(lam-sg*np.linalg.matrix_power(mu,k)))<1e-6: return (sg,k)
    return None
w=np.exp(2j*np.pi/3); i_=1j
for name,sp,pred in [("{1,1,w,w2} o3 (ctrl, k=4)",[1,1,w,w**2],4),
                     ("{1,1,i,-i} o4 (k=3=>order/formula, k=4=>rank)",[1,1,i_,-i_],3)]:
    sp=np.array(sp,dtype=complex); sp=sp/(np.prod(sp))**0.25; A=np.diag(sp)
    rng=np.random.default_rng(0); exps={}; tot=0
    for s in range(400):
        t=newton(A,rng)
        if t is None or abs(np.linalg.det(t))<1e-3 or np.linalg.cond(t)>1e4: continue
        B=Bfrom(A,t)
        if not irred(A,B): continue
        e=expo(A,t)
        if e: exps[e]=exps.get(e,0)+1; tot+=1
        if tot>=3: break
    print(f"FIG n=4 {name}: exponents {dict(sorted(exps.items()))} (formula predicts k={pred})", flush=True)
