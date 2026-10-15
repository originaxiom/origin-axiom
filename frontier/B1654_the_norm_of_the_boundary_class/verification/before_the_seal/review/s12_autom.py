import sys; sys.path.insert(0,'.')
import numpy as np, pre
ns = pre.load(); S_A=ns['S_A']; W=ns['W']
rng=np.random.default_rng(5)
zs = [0.13+0.07j, -0.21+0.19j, 0.05-0.31j]
def test(tau, zeta, label):
    print(label)
    for r in (2,3,4):
        out=[]
        for s in (2,3,4):
            err=max(abs(zeta*S_A(r,np.array(zeta*z),tau) - S_A(s,np.array(z),tau)) for z in zs)
            out.append((s,err))
        best=min(out,key=lambda t:t[1])
        print(f"   zeta*S_{r}(zeta z) = S_{best[0]}(z) up to {best[1]:.1e}   (all errs: {[f'{e:.1e}' for s,e in out]})")
test(1j, 1j, "tau=i, zeta=i")
test(W, np.exp(2j*np.pi/3), "tau=omega, zeta=omega (order 3)")
test(W, np.exp(1j*np.pi/3), "tau=omega, zeta=exp(i pi/3) (order 6)")
# check the half-period for each S_r: theta_r vanishes at
for r,hp in ((2,0.5),(3,'(1+tau)/2'),(4,'tau/2')): pass
