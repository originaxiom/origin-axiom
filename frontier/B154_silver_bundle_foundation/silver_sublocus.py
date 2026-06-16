# Cleaner sub-locus tangent: add cond(B) filter, report SVD gaps, confirm codim(S in V)=0 (component).
import numpy as np
n=3; w=np.exp(2j*np.pi/3); A=np.diag([1,w,w**2]).astype(complex); Ai=np.linalg.inv(A); A2=A@A
def resid(B,t): return np.concatenate([(t@B@B-Ai@t@A).reshape(-1),(t@B-A2@B@t).reshape(-1)])
def newton(rng,it=250):
    x=rng.standard_normal(2*n*n)+1j*rng.standard_normal(2*n*n); sp=lambda x:(x[:n*n].reshape(n,n),x[n*n:].reshape(n,n))
    for _ in range(it):
        B,t=sp(x); g=np.concatenate([resid(B,t),[np.linalg.det(B)-1,np.linalg.det(t)-1]])
        if np.max(np.abs(g))<1e-13: break
        if np.max(np.abs(g))>1e6: return None
        h=1e-7; J=np.zeros((g.size,2*n*n),complex)
        for k in range(2*n*n):
            xp=x.copy(); xp[k]+=h; Bp,tp=sp(xp); gp=np.concatenate([resid(Bp,tp),[np.linalg.det(Bp)-1,np.linalg.det(tp)-1]]); J[:,k]=(gp-g)/h
        try: st,*_=np.linalg.lstsq(J,g,rcond=None)
        except: return None
        x=x-st
    B,t=sp(x); return (B,t) if np.max(np.abs(resid(B,t)))<1e-9 else None
def irred(B,t,r=5,tol=1e-7):
    gens=[A,B,np.linalg.inv(A),np.linalg.inv(B)]; allm=[np.eye(n,dtype=complex)]; fr=[np.eye(n,dtype=complex)]
    for _ in range(r): fr=[g@m for m in fr for g in gens]; allm+=fr
    return np.linalg.matrix_rank(np.array([m.reshape(-1) for m in allm]),tol=tol)==n*n
def jacs(B,t):
    Bi=np.linalg.inv(B); ti=np.linalg.inv(t); mu=Ai@Ai@t; colsF=[]; colsR=[]
    for which in range(2):
        for i in range(n):
            for j in range(n):
                E=np.zeros((n,n),complex); E[i,j]=1
                dB=E if which==0 else 0*E; dt=E if which==1 else 0*E
                dF1=dt@B@B+t@dB@B+t@B@dB-Ai@dt@A; dF2=dt@B+t@dB-A2@dB@t-A2@B@dt
                dlam=A@dB@Ai@Bi-A@B@Ai@Bi@dB@Bi; dmu=Ai@Ai@dt
                dmu4=dmu@mu@mu@mu+mu@dmu@mu@mu+mu@mu@dmu@mu+mu@mu@mu@dmu
                colsF.append(np.concatenate([dF1.reshape(-1),dF2.reshape(-1),[np.trace(Bi@dB),np.trace(ti@dt)]]))
                colsR.append((dlam-dmu4).reshape(-1))
    return np.array(colsF).T, np.array(colsR).T
rng=np.random.default_rng(7); shown_on=0; offtan=[]
for s in range(200):
    r=newton(rng)
    if r is None: continue
    B,t=r
    if np.linalg.cond(t)>1e3 or np.linalg.cond(B)>1e3 or not irred(B,t): continue
    lam=A@B@Ai@np.linalg.inv(B); mu=Ai@Ai@t; on=np.max(np.abs(lam-np.linalg.matrix_power(mu,4)))<1e-6
    JF,JR=jacs(B,t); JS=np.vstack([JF,JR])
    try:
        sF=np.linalg.svd(JF,compute_uv=False); sS=np.linalg.svd(JS,compute_uv=False)
    except np.linalg.LinAlgError:
        continue
    rkF=int(np.sum(sF>1e-7*sF[0])); rkS=int(np.sum(sS>1e-7*sS[0]))
    tanV=2*n*n-rkF; tanS=2*n*n-rkS
    if on and shown_on<3:
        shown_on+=1
        print(f"ON  rep{shown_on}: cond(B)={np.linalg.cond(B):.0f} cond(t)={np.linalg.cond(t):.0f} | rk(JF)={rkF} (gap sF[{rkF-1}]={sF[rkF-1]:.1e}/sF[{rkF}]={sF[rkF] if rkF<len(sF) else 0:.1e}) tanV={tanV}; rk(JS)={rkS} tanS={tanS}; relation adds rank {rkS-rkF}")
    if not on:
        offtan.append(tanV)
print(f"\nOFF sub-locus tangents (well-conditioned, cond(B),cond(t)<1e3): {offtan[:12]}")
print(f"gauge dim (Z(A)=SL diag) = {n-1}; if tanV==tanS on-locus => codim 0 => the degree=rank locus is a COMPONENT")
