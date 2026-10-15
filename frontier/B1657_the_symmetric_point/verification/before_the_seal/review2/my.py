import numpy as np, mpmath as mp
mp.mp.dps=30
def th(tau):
    q=mp.exp(1j*mp.pi*tau); return [mp.jtheta(j,0,q) for j in (2,3,4)]
def Rv(tau):
    t2,t3,t4=th(tau); q=mp.exp(1j*mp.pi*tau)
    tp=mp.jtheta(1,0,q,1)  # derivative wrt z of theta1(z)... jtheta(1,z,q,1) = d/dz
    return np.array([complex(x) for x in (-t2**2/tp,1j*t3**2/tp,-t4**2/tp)])
def Y(a,v): return np.outer(a,v)+np.outer(v,a)-(a@v)*np.eye(3)
rng=np.random.default_rng(99)
for tau in (complex(-.5,np.sqrt(3)/2),1j,.13+1.07j):
    R=Rv(tau);R/=np.linalg.norm(R);print(tau,abs(R@R))
    for coef in (1.0,0.5,2.0,1.1,0.9):
        worst=[0,0]
        for _ in range(400):
            ea,ev=10**rng.uniform(-4,-2,2); al=rng.normal(size=3)+1j*rng.normal(size=3);be=rng.normal(size=3)+1j*rng.normal(size=3)
            a=R+ea*al/np.linalg.norm(al); v=R+ev*be/np.linalg.norm(be)
            s=np.linalg.svd(Y(a,v),compute_uv=False); da=a@a/np.linalg.norm(a)**2; dv=v@v/np.linalg.norm(v)**2
            e=max(ea,ev)
            worst[0]=max(worst[0],abs(s[1]/s[0]/(coef*abs(da+dv)/4)-1)/e); worst[1]=max(worst[1],abs(s[2]/s[0]/(coef*abs(da*dv)/4)-1)/e)
        print(coef,worst)
# covariance of D via W87
def D(tau):
    t2,t3,t4=th(tau); lam=t2**4/t3**4; h=lam*mp.log(abs(lam))+(1-lam)*mp.log(abs(1-lam))
    eta=mp.exp(1j*mp.pi*tau/12)*mp.qp(mp.exp(2j*mp.pi*tau)); return -t3**4*h/(4*mp.pi*eta**6)
for t in (.13+1.07j,-.21+.93j,.33+1.4j,.7+.8j):
    t=mp.mpc(t); g=-1/(t+1); print(abs(D(g)*(t+1)+D(t))/abs(D(t)))
w=mp.mpc(-.5,mp.sqrt(3)/2); print(abs(D(w)))
# does covariance force D(w)=0? D(w)*(w+1)=-D(w); w+1=e^{i pi/3}; so (e^{i pi/3}+1)D=0 -> D=0
print(w+1)
# derivative at omega: D(w+d)~ kappa d ; holomorphic-term test: D(g t)(t+1)=-D(t) near w
d=mp.mpf('1e-6'); 
for ph in (0,1,2):
    dd=d*mp.exp(1j*ph); print(abs(D(w+dd))/d)
