# N6(a): s3/s1 at omega per unit |D|/|R|^2, for the sealed directions, at L=40 (the limit-law factor); compares to the 1e-12 threshold when |D|/|R|^2 = 1e-10 (N5(a)'s allowance)
import math, numpy as np, pre2
ns = pre2.load(); R_A=ns['R_A']; nR2=ns['nR2']; TAUS=ns['TAUS']; Y=ns['Y']; vec=ns['vec']
rng=np.random.default_rng(1654)
def cplx(n): return rng.normal(size=n)+1j*rng.normal(size=n)
dirs=[cplx(3) for _ in range(3)]
tau=TAUS['omega']; R=R_A(tau); Rv=vec(R)
near=np.conj(Rv)+0.1*np.linalg.norm(Rv)*cplx(3)/math.sqrt(6)
for k,a in enumerate(dirs+[near]):
    s0=np.linalg.svd(Y(a,Rv),compute_uv=False)
    fac=abs(a@a)*abs(a@Rv)*nR2(R)/(2*math.pi*40*s0[0]**2*s0[1])   # s3/s1 = fac * |D|/|R|^2 at L=40
    print(f"dir{k}: s3/s1 at L=40 = {fac:.3e} x (|D|/|R|^2)   -> for |D|/|R|^2 = 1e-10 (N5(a) allowance): {fac*1e-10:.2e}  vs N6(a) threshold 1e-12")
