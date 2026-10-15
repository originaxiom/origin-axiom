import numpy as np, mpmath as mp, math
mp.mp.dps=30
def Rv(tau):
    q=mp.exp(1j*mp.pi*mp.mpc(tau))
    t2,t3,t4=[mp.jtheta(j,0,q) for j in (2,3,4)]
    tp=mp.jtheta(1,0,q,1)*mp.pi
    return np.array([complex(-t2**2/tp), complex(1j*t3**2/tp), complex(-t4**2/tp)])
def Y(a,v): return np.outer(a,v)+np.outer(v,a)-(a@v)*np.eye(3)
sv=lambda M: np.linalg.svd(M,compute_uv=False)
TAUS={"omega":complex(np.exp(2j*np.pi/3)),"i":1j,"t1":0.13+1.07j,"tstar":complex(.5,math.sqrt(5)/2)}
Rs={k:Rv(t)/np.linalg.norm(Rv(t)) for k,t in TAUS.items()}
# the instrument's statistic, many seeds
allw=[]
for seed in range(100,300):
    rng=np.random.default_rng(seed)
    for k,R in Rs.items():
        wk=0
        for _ in range(200):
            ea,ev=10**rng.uniform(-6,-2),10**rng.uniform(-6,-2)
            al=rng.normal(size=3)+1j*rng.normal(size=3); be=rng.normal(size=3)+1j*rng.normal(size=3)
            a=2*(R.conj()+ea*al/np.linalg.norm(al)); v=3*(R+ev*be/np.linalg.norm(be))
            s=sv(Y(a,v)); got=s[1:]/s[0]
            da=abs(a@a)/np.linalg.norm(a)**2; dv=abs(v@v)/np.linalg.norm(v)**2
            wk=max(wk,np.abs(got/np.sort([da,dv])[::-1]-1).max()/max(ea,ev))
        allw.append(wk)
allw=np.array(allw); print("statistic over 800 (seed,tau) blocks: max %.4f  99%% %.4f  median %.4f ; frac>0.05: %.4f"%(allw.max(),np.quantile(allw,.99),np.median(allw),(allw>0.05).mean()))
# adversarial: alpha nearly bilinear-orthogonal to Rbar (a.a ~ second order), and da ~ dv
rng=np.random.default_rng(1)
worst=0
for k,R in Rs.items():
    for _ in range(4000):
        ea=10**rng.uniform(-6,-2); ev=ea*(1+1e-3*rng.normal())
        al=rng.normal(size=3)+1j*rng.normal(size=3); be=rng.normal(size=3)+1j*rng.normal(size=3)
        # make al.Rbar small
        al=al-(al@R)*R.conj()*0.0
        al=al/np.linalg.norm(al); be=be/np.linalg.norm(be)
        a=2*(R.conj()+ea*al); v=3*(R+ev*be)
        s=sv(Y(a,v)); got=s[1:]/s[0]
        da=abs(a@a)/np.linalg.norm(a)**2; dv=abs(v@v)/np.linalg.norm(v)**2
        worst=max(worst,np.abs(got/np.sort([da,dv])[::-1]-1).max()/max(ea,ev))
print("near-equal eps worst:",worst)
worst=0;wx=None
for k,R in Rs.items():
    for _ in range(20000):
        ea=10**rng.uniform(-6,-2); ev=10**rng.uniform(-6,-2)
        al=rng.normal(size=3)+1j*rng.normal(size=3); be=rng.normal(size=3)+1j*rng.normal(size=3)
        al/=np.linalg.norm(al); be/=np.linalg.norm(be)
        a=2*(R.conj()+ea*al); v=3*(R+ev*be)
        x=abs(al@R.conj())
        s=sv(Y(a,v)); got=s[1:]/s[0]
        da=abs(a@a)/np.linalg.norm(a)**2; dv=abs(v@v)/np.linalg.norm(v)**2
        r=np.abs(got/np.sort([da,dv])[::-1]-1).max()/max(ea,ev)
        if r>worst: worst=r;wx=(k,ea,ev,x,abs(be@R))
print("20000x4 draws worst:",worst,wx)
