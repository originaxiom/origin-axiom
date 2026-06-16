# Silver A-free spectrum-rigidity (B153-style): with A,B,t ALL free, is the {1,w,w^2} spectrum RIGID on
# the silver degree=rank component (=> genuine component, like fig n=3) or does tr A move (=> slice, fig n=4)?
# Silver variety: F1 = t B^2 - A^-1 t A,  F2 = t B - A^2 B t.  Exact differential (A,B,t free); SVD tangent.
import numpy as np
n=3; w=np.exp(2j*np.pi/3)
# get a degree=rank component rep at A=diag{1,w,w^2} (fixed-A solver), then do the A-FREE tangent there.
A0=np.diag([1,w,w**2]).astype(complex); Ai0=np.linalg.inv(A0); A20=A0@A0
def resid_fixedA(B,t): return np.concatenate([(t@B@B-Ai0@t@A0).reshape(-1),(t@B-A20@B@t).reshape(-1)])
def newton_fixedA(rng,it=250):
    x=rng.standard_normal(2*n*n)+1j*rng.standard_normal(2*n*n); sp=lambda x:(x[:n*n].reshape(n,n),x[n*n:].reshape(n,n))
    for _ in range(it):
        B,t=sp(x); g=np.concatenate([resid_fixedA(B,t),[np.linalg.det(B)-1,np.linalg.det(t)-1]])
        if np.max(np.abs(g))<1e-13: break
        if np.max(np.abs(g))>1e6: return None
        h=1e-7; J=np.zeros((g.size,2*n*n),complex)
        for k in range(2*n*n):
            xp=x.copy(); xp[k]+=h; Bp,tp=sp(xp); gp=np.concatenate([resid_fixedA(Bp,tp),[np.linalg.det(Bp)-1,np.linalg.det(tp)-1]]); J[:,k]=(gp-g)/h
        try: st,*_=np.linalg.lstsq(J,g,rcond=None)
        except: return None
        x=x-st
    B,t=sp(x); return (B,t) if np.max(np.abs(resid_fixedA(B,t)))<1e-9 else None
def irred(A,B,r=5,tol=1e-7):
    gens=[A,B,np.linalg.inv(A),np.linalg.inv(B)]; allm=[np.eye(n,dtype=complex)]; fr=[np.eye(n,dtype=complex)]
    for _ in range(r): fr=[g@m for m in fr for g in gens]; allm+=fr
    return np.linalg.matrix_rank(np.array([m.reshape(-1) for m in allm]),tol=tol)==n*n
def afree_tangent(A,B,t):
    # exact differential of (F1,F2) wrt (A,B,t) all free
    Ai=np.linalg.inv(A); Bi=np.linalg.inv(B); ti=np.linalg.inv(t); A2=A@A
    cols=[]
    Z=np.zeros((n,n),complex)
    for which in range(3):       # 0=dA,1=dB,2=dt
        for i in range(n):
            for j in range(n):
                E=np.zeros((n,n),complex); E[i,j]=1
                dA=E if which==0 else Z; dB=E if which==1 else Z; dt=E if which==2 else Z
                dAi=-Ai@dA@Ai
                dF1=dt@B@B + t@dB@B + t@B@dB - (dAi@t@A + Ai@dt@A + Ai@t@dA)
                dF2=dt@B + t@dB - ((dA@A+A@dA)@B@t + A2@dB@t + A2@B@dt)
                cols.append(np.concatenate([dF1.reshape(-1),dF2.reshape(-1)]))
    J=np.array(cols).T           # (2n^2) x (3n^2)
    s=np.linalg.svd(J,compute_uv=False); tol=1e-7*s[0]; rk=int(np.sum(s>tol))
    ker=3*n*n-rk
    # does tr A move within SL x SL x SL? kernel directions; functionals d(detA),d(detB),d(dett),d(trA)
    Vh=np.linalg.svd(J)[2]; K=Vh[rk:].conj().T   # kernel basis, cols, in (dA|dB|dt) coords (27)
    N=n*n
    def dtrA(v): return sum(v[k*n+k] for k in range(n))                       # dA diag
    def ddet(v,off,M): return sum(np.linalg.inv(M)[b,a]*v[off+a*n+b] for a in range(n) for b in range(n))
    rows2=[]; rows3=[]
    for c in range(K.shape[1]):
        v=K[:,c]
        dA_=ddet(v,0,A); dB_=ddet(v,N,B); dt_=ddet(v,2*N,t); trA_=dtrA(v)
        rows2.append([dA_,dB_,dt_]); rows3.append([dA_,dB_,dt_,trA_])
    r2=np.linalg.matrix_rank(np.array(rows2),tol=1e-7) if rows2 else 0
    r3=np.linalg.matrix_rank(np.array(rows3),tol=1e-7) if rows3 else 0
    return ker, bool(r3>r2)
rng=np.random.default_rng(7); done=0
for s in range(160):
    r=newton_fixedA(rng)
    if r is None: continue
    B,t=r
    if np.linalg.cond(B)>1e3 or np.linalg.cond(t)>1e3 or not irred(A0,B): continue
    lam=A0@B@Ai0@np.linalg.inv(B); mu=Ai0@Ai0@t
    if np.max(np.abs(lam-np.linalg.matrix_power(mu,4)))>1e-6: continue   # on the degree=rank component
    ker,moves=afree_tangent(A0,B,t)
    done+=1
    print(f"deg=rank rep {done}: A-free tangent dim = {ker}; tr A moves in SLxSLxSL: {moves}  => {'SLICE (spectrum deforms)' if moves else 'RIGID component (spectrum fixed)'}", flush=True)
    if done>=4: break
