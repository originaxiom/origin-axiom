import numpy as np, mpmath as mp
mp.mp.dps=30
def Rv(tau):
    q=mp.exp(1j*mp.pi*mp.mpc(tau))
    t2,t3,t4=[mp.jtheta(j,0,q) for j in (2,3,4)]
    tp=mp.jtheta(1,0,q,1)*mp.pi
    return np.array([complex(-t2**2/tp), complex(1j*t3**2/tp), complex(-t4**2/tp)])
def Y(a,v): return np.outer(a,v)+np.outer(v,a)-(a@v)*np.eye(3)
sv=lambda M: np.linalg.svd(M,compute_uv=False)
P=np.array([[0,1,0],[0,0,-1],[1,0,0.]])
w=np.exp(2j*np.pi/3)
ev,V=np.linalg.eig(P); print("eig P:",ev, np.angle(ev)/np.pi)
R=Rv(w); print("R(w)=",R,"R.R=",R@R)
print("P R / R:", (P@R)/R, " arg/pi:", np.angle((P@R)/R)/np.pi)
n=np.array([1,-1,-1])/np.sqrt(3)
print("n.R=",n@R, "Pn+n:",P@n+n)
print("R.Rbar=",R@R.conj(),"|R|^2=",np.linalg.norm(R)**2, "Re R . Im R =", R.real@R.imag, "|ReR|,|ImR|",np.linalg.norm(R.real),np.linalg.norm(R.imag))
# check n is normal to R's real plane
print("n . Re R, n . Im R:", n@R.real, n@R.imag)
# spectra
Rn=R/np.linalg.norm(R)
for name,a in (("n",n),("R",Rn),("Rbar",Rn.conj())):
    s=sv(Y(a,R)); print(name, s/s[0])
# first-order block: compress dY onto {R,Rbar} (unit R)
rng=np.random.default_rng(5)
Ru=Rn
for t in range(3):
    al=rng.normal(size=3)+1j*rng.normal(size=3); be=rng.normal(size=3)+1j*rng.normal(size=3)
    dY=Y(al,Ru)+Y(Ru.conj(),be)
    basis=[Ru,Ru.conj()]
    C=np.array([[ (e.conj()@dY@x) for x in basis] for e in basis])
    pred=np.array([[0,2*al@Ru.conj()],[2*be@Ru,0]])
    print("compression vs [[0,2 al.Rbar],[2 be.R,0]]:", np.abs(C-pred).max())
# sign of det
a=rng.normal(size=3)+1j*rng.normal(size=3); v=rng.normal(size=3)+1j*rng.normal(size=3)
print("det Y / ((a.v)(a.a)(v.v)):", np.linalg.det(Y(a,v))/((a@v)*(a@a)*(v@v)))
