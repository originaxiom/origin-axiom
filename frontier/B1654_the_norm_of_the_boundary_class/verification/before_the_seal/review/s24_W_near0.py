import sys; sys.path.insert(0,'.')
import numpy as np, pre
ns = pre.load(); R_A=ns['R_A']; S_A=ns['S_A']; nR2=ns['nR2']
tau=0.13+1.07j; R=R_A(tau)
for rho in (1e-1,1e-2,1e-3):
    vals=[]
    for th in np.linspace(0,2*np.pi,7)[:-1]:
        z=np.array(rho*np.exp(1j*th))
        W=sum(R[r]**2*abs(S_A(r,z,tau))**2 for r in (2,3,4))
        vals.append(W)
    print(f"|z|={rho:g}: max|W|/|R|^2 = {max(abs(w) for w in vals)/nR2(R):.3e};  max|W|/(|z|^2 |R|^2) = {max(abs(w) for w in vals)/rho**2/nR2(R):.3f}")
# e_r from S_r^2 = wp - e_r: s1_r = -e_r/2 ; check sum R_r^2 s1_r = 0
for r in (2,3,4):
    rho=0.03; N=64
    z=rho*np.exp(2j*np.pi*np.arange(N)/N)
    s1=np.mean(S_A(r,z,tau)/z)
    print("r",r,"s1 =",s1)
s1={r: np.mean(S_A(r,0.03*np.exp(2j*np.pi*np.arange(64)/64),tau)/(0.03*np.exp(2j*np.pi*np.arange(64)/64))) for r in (2,3,4)}
print("sum R_r^2 s1_r / |R|^2 =", abs(sum(R[r]**2*s1[r] for r in (2,3,4)))/nR2(R))
