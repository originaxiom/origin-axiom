import numpy as np, pre2
ns = pre2.load(); S_A=ns['S_A']; W=ns['W']
zs=[0.13+0.07j,-0.21+0.19j,0.05-0.31j]
def test(tau,zeta,label):
    print(label)
    for r in (2,3,4):
        out=[(s,max(abs(zeta*S_A(r,np.array(zeta*z),tau)-S_A(s,np.array(z),tau)) for z in zs)) for s in (2,3,4)]
        best=min(out,key=lambda t:t[1]); print(f"   zeta*S_{r}(zeta z) = S_{best[0]}(z) up to {best[1]:.1e}")
test(1j,1j,"tau=i, zeta=i")
test(W,np.exp(2j*np.pi/3),"tau=omega, zeta=omega (order 3)")
test(W,np.exp(1j*np.pi/3),"tau=omega, zeta=exp(i pi/3) (order 6)")
