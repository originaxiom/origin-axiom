import sys, math; sys.path.insert(0,'.')
import numpy as np, pre
ns = pre.load(); R_A=ns['R_A']; TAUS=ns['TAUS']; Y=ns['Y']; vec=ns['vec']
rng=np.random.default_rng(3)
a=rng.normal(size=3)+1j*rng.normal(size=3)
Rv=vec(R_A(TAUS['t1']))
M=Y(a,Rv)
U,s,Vh=np.linalg.svd(M)
v3=np.conj(Vh[2]); u3=U[:,2]
print("Y R =", np.linalg.norm(M@Rv)/np.linalg.norm(Rv), " sigma =", s)
print("overlap |<v3,R>|/|R| (vdot, as coded):", abs(np.vdot(v3,Rv))/np.linalg.norm(Rv))
print("wrong convention overlap |<Vh[2],R>|:", abs(np.vdot(Vh[2],Rv))/np.linalg.norm(Rv))
print("||Y v3|| =", np.linalg.norm(M@v3), " ||Y^H u3|| =", np.linalg.norm(M.conj().T@u3), " u3 vs conj(v3) phase-free overlap:", abs(np.vdot(u3,np.conj(v3))))
