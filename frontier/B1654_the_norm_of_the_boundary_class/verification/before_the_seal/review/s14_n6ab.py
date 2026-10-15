import sys, math; sys.path.insert(0,'.')
import numpy as np, pre
ns = pre.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']; TAUS=ns['TAUS']; Y=ns['Y']; vec=ns['vec']
C={name:{r:cA(r,TAUS[name],1e-5) for r in (2,3,4)} for name in ("omega","i","t1")}
def cplx(rng,n): return rng.normal(size=n)+1j*rng.normal(size=n)
worst_a=0; worst_b=0
for seed in range(200):
    rng=np.random.default_rng(1000+seed)
    dirs=[cplx(rng,3) for _ in range(3)]
    for name in ("omega","i","t1"):
        R=R_A(TAUS[name]); Rv=vec(R); c=C[name]; cv=np.array([c[2],c[4],c[3]])
        near=np.conj(Rv)+0.1*np.linalg.norm(Rv)*cplx(rng,3)/math.sqrt(6)
        for a in dirs+[near]:
            s=np.linalg.svd(Y(a,Rv),compute_uv=False); worst_b=max(worst_b,s[2]/s[0])
            if name=="omega":
                for L in (40.,160.,640.,2560.):
                    u=np.sqrt(2*np.pi*L+cv)*Rv
                    s=np.linalg.svd(Y(a,u),compute_uv=False); worst_a=max(worst_a,s[2]/s[0])
print("worst N6(a) m1/m3 at omega over 200 seeds:", worst_a)
print("worst N6(b) P4' m1/m3 over omega,i,t1:", worst_b)
