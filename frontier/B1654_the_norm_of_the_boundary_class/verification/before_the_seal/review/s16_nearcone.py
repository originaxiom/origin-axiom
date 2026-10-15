import sys, math; sys.path.insert(0,'.')
import numpy as np, pre
ns = pre.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']; TAUS=ns['TAUS']; Y=ns['Y']; vec=ns['vec']
C={name:{r:cA(r,TAUS[name],1e-5) for r in (2,3,4)} for name in ("i","t1")}
def cplx(rng,n): return rng.normal(size=n)+1j*rng.normal(size=n)
def metrics(a,name):
    tau=TAUS[name]; R=R_A(tau); Rv=vec(R); c=C[name]; cv=np.array([c[2],c[4],c[3]]); D=D_of(c,R)
    s0=np.linalg.svd(Y(a,Rv),compute_uv=False)
    lim=abs(a@a)*abs(D)*abs(a@Rv)/(2*np.pi*s0[0]**2*s0[1])
    rows={}
    for L in (640.,2560.):
        u=np.sqrt(2*np.pi*L+cv)*Rv
        U,s,Vh=np.linalg.svd(Y(a,u)); v3=np.conj(Vh[2])
        ov=abs(np.vdot(v3,Rv))/np.linalg.norm(Rv)
        ang_acos=math.acos(min(1.0,ov))
        perp=v3-np.vdot(Rv/np.linalg.norm(Rv),v3)*Rv/np.linalg.norm(Rv)   # robust small angle
        ang_robust=math.atan2(np.linalg.norm(perp),ov)
        rows[L]=(s[2]/s[0],ang_acos,ang_robust,s[1])
        last=(s[2]/s[0],)
    errL=abs(2560*rows[2560.][0]/lim-1)
    r_ang=rows[2560.][1]*2560/(rows[640.][1]*640)
    r_ang_rob=rows[2560.][2]*2560/(rows[640.][2]*640)
    half=(rows[2560.][1]/math.sqrt(rows[2560.][0]*rows[2560.][3]/rows[2560.][3]) if False else None)
    return errL,r_ang,r_ang_rob,rows[2560.][1],rows[2560.][2], s0[1]/s0[0]
for eta in (0.1,0.03,0.01,0.003,0.001):
    worst=[0,0,0,1e9,0]
    for seed in range(100):
        rng=np.random.default_rng(seed)
        for name in ("i","t1"):
            Rv=vec(R_A(TAUS[name]))
            a=np.conj(Rv)+eta*np.linalg.norm(Rv)*cplx(rng,3)/math.sqrt(6)
            errL,r_ang,r_rob,ang,angr,sr=metrics(a,name)
            worst[0]=max(worst[0],errL); worst[1]=max(worst[1],abs(r_ang-1)); worst[2]=max(worst[2],abs(r_rob-1)); worst[3]=min(worst[3],ang); worst[4]=max(worst[4],sr)
    print(f"eta={eta}: max lim err={worst[0]:.2e}, max |angL ratio-1| (acos)={worst[1]:.2e}, (robust atan2)={worst[2]:.2e}, min angle@2560={worst[3]:.2e}, max sigma2/sigma1={worst[4]:.3f}")
