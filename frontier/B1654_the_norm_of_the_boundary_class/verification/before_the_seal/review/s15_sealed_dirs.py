import sys, math; sys.path.insert(0,'.')
import numpy as np, pre
ns = pre.load(); R_A=ns['R_A']; TAUS=ns['TAUS']; Y=ns['Y']; vec=ns['vec']
rng = np.random.default_rng(1654)
def cplx(n): return rng.normal(size=n) + 1j*rng.normal(size=n)
dirs=[cplx(3) for _ in range(3)]
for name in ("omega","i","t1"):
    R=R_A(TAUS[name]); Rv=vec(R)
    near = np.conj(Rv) + 0.1*np.linalg.norm(Rv)*cplx(3)/math.sqrt(6)
    for k,a in enumerate(dirs+[near]):
        s0=np.linalg.svd(Y(a,Rv),compute_uv=False)
        print(f"{name:5s} dir{k}: |a.a|/|a|^2={abs(a@a)/np.vdot(a,a).real:.3f}  |a.R|/(|a||R|)={abs(a@Rv)/np.linalg.norm(a)/np.linalg.norm(Rv):.3f}  sigma2/sigma1={s0[1]/s0[0]:.3f}")
