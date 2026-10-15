import numpy as np
rng=np.random.default_rng(5)
EPS=np.array([[0,1],[-1,0]],complex);EI=np.linalg.inv(EPS)
QI=np.array([[1j,0],[0,-1j]]);QJ=EPS;QK=QI@QJ;BL=[QJ,QI,QK]
def Y(S,M): return np.array([[np.sum((a.T@EPS@S@b)*M) for b in BL] for a in BL])
def r(): return rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
S=r();Z=Y(S,S@EI)
sv=np.linalg.svd(Z,compute_uv=False);print("sv",sv,sv[0]*sv[2]/sv[1]**2)
Z2=Z@Z;print("Z^2",np.round(Z2/ Z2[0,0],3)); print("Zsym",np.abs(Z-Z.T).max())
print("Z@conj",np.round(Z@Z.conj().T,3))
# B1657
def Y57(a,v): return np.outer(a,v)+np.outer(v,a)-(a@v)*np.eye(3)
v=rng.normal(size=3)+1j*rng.normal(size=3);Yv=Y57(v,v);sv=np.linalg.svd(Yv,compute_uv=False);print("57 sv",sv,sv[0]*sv[2]/sv[1]**2, np.abs(Yv@Yv-(v@v)**2*np.eye(3)).max())
# is Z linearly Y57-like? Z^2 prop 1?
# m2=0 case: det S=0 and both? rank
Sn=np.outer(rng.normal(size=2)+0j,rng.normal(size=2)+0j);Mn=np.outer(rng.normal(size=2)+0j,rng.normal(size=2)+0j)
print("null both sv",np.linalg.svd(Y(Sn,Mn),compute_uv=False))
# m2 = 0 with det Y !=0? impossible. tr=0, both nonnull
S=r();M=S  # ell=0
print("ell0 sv",np.linalg.svd(Y(S,M),compute_uv=False))
