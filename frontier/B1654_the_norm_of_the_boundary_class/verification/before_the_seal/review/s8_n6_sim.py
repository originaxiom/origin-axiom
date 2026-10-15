import sys, time; sys.path.insert(0,'.')
import numpy as np, math, pre
ns = pre.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']; TAUS=ns['TAUS']; Y=ns['Y']; vec=ns['vec']
# c values at the two non-trivial named points (already seen by main in the exploration)
C = {}
for name in ("i","t1"):
    tau=TAUS[name]; C[name] = {r: cA(r,tau,1e-5) for r in (2,3,4)}
def cplx(rng,n): return rng.normal(size=n)+1j*rng.normal(size=n)
def one_case(a, name):
    tau=TAUS[name]; R=R_A(tau); Rv=vec(R); c=C[name]; cv=np.array([c[2],c[4],c[3]]); D=D_of(c,R)
    s0=np.linalg.svd(Y(a,Rv),compute_uv=False)
    lim=abs(a@a)*abs(D)*abs(a@Rv)/(2*np.pi*s0[0]**2*s0[1])
    rows={}
    for L in (40.,160.,640.,2560.):
        u=np.sqrt(2*np.pi*L+cv)*Rv
        U,s,Vh=np.linalg.svd(Y(a,u)); v3=np.conj(Vh[2])
        ang=math.acos(min(1.0,abs(np.vdot(v3,Rv))/np.linalg.norm(Rv)))
        rows[L]=(s[2]/s[0], s[1]/s[0], ang, ang/math.sqrt(s[2]/s[1]))
    err=abs(L*rows[2560.][0]/lim-1)
    r_ang=rows[2560.][2]*2560/(rows[640.][2]*640)
    r_half=rows[2560.][3]/rows[640.][3]
    return err, r_ang, r_half, rows[2560.][2], s0[1]/s0[0], abs(a@a)/np.vdot(a,a).real
for seed in (11,12,13):
    rng=np.random.default_rng(seed)
    print("seed",seed)
    dirs=[cplx(rng,3) for _ in range(3)]
    for name in ("i","t1"):
        R=R_A(TAUS[name]); Rv=vec(R)
        near=np.conj(Rv)+0.1*np.linalg.norm(Rv)*cplx(rng,3)/math.sqrt(6)
        for k,a in enumerate(dirs+[near]):
            err,r_ang,r_half,ang,sr,iso=one_case(a,name)
            print(f"  {name} dir{k}: |a.a|/|a|^2={iso:.3f} s2/s1(Y(a;R))={sr:.3f} | lim err@2560={err:.2e}  angL ratio={r_ang:.5f}  halving={r_half:.5f}  angle@2560={ang:.2e}")
