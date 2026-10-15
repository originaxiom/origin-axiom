import numpy as np, math
rng=np.random.default_rng(0)
def dot(X,Y): return np.sum(X*Y,axis=1)
def Gp(X,Y,v): return dot(v,Y)[:,None]*X + dot(v,X)[:,None]*Y - dot(X,Y)[:,None]*v
def inv_sqrt(K):
    e,U=np.linalg.eigh(K); return U@np.diag(e**-0.5)@U.conj().T
N=200
def crand(*s): return rng.normal(size=s)+1j*rng.normal(size=s)
# isotropic R(tau): R = a*(1, i cos t, i sin t)-type: pick random complex a, angle
def iso(n):
    a=crand(n); th=rng.normal(size=n)+0.3j*rng.normal(size=n)
    return a[:,None]*np.stack([np.ones(n), 1j*np.cos(th), 1j*np.sin(th)],1)
R=iso(N); print('R.R/|R|^2', np.max(np.abs(dot(R,R))/np.sum(abs(R)**2,1)))
h=crand(N,3); c=rng.normal(size=(N,3))*2
L=[R, crand(N,3), crand(N,3)]          # left modes, first is R  (C3-like: zero row)
Rt=[crand(N,3), crand(N,3), crand(N,3)]
KL=np.array([[np.sum(dot(L[i],np.conj(L[j]))) for j in range(3)] for i in range(3)])
KR=np.array([[np.sum(dot(Rt[i],np.conj(Rt[j]))) for j in range(3)] for i in range(3)])
A,B=inv_sqrt(KL),inv_sqrt(KR)
def Ymat(v): return np.array([[np.sum(dot(Gp(L[a],Rt[b],v),np.conj(h))) for b in range(3)] for a in range(3)])
YR=Ymat(R); MR=A@YR@B.T
U,s,Vh=np.linalg.svd(MR); o=np.argsort(s); s3=s[o[2]]
print('m1/m3', s[o[0]]/s3, 'm2/m3', s[o[1]]/s3, ' zero row of YR:', np.abs(YR[0]).max()/np.abs(YR).max())
u0,v0=U[:,o[0]],Vh[o[0],:].conj()
print('null check |MR v0|, |u0^H MR|', np.linalg.norm(MR@v0), np.linalg.norm(u0.conj()@MR))
def kap(delta): return abs(u0.conj()@(A@Ymat(delta)@B.T)@v0)/s3
k0=kap(c*R); print('kappa', k0)
ktau=rng.normal(size=N)*5
print('kappa with tau-dependent common shift', kap((c+ktau[:,None])*R), ' rel diff', abs(kap((c+ktau[:,None])*R)-k0)/k0)
# exact: v = sqrt(1+c/(2 pi L)) R, compare 4 pi L m1/m3 with kappa
for Lv in (10,100,1000,1e4,1e5):
    sl=np.sort(np.linalg.svd(A@Ymat(np.sqrt(1+c/(2*math.pi*Lv))*R)@B.T,compute_uv=False))
    print(f'L={Lv:g}: 4piL m1/m3 / kappa = {4*math.pi*Lv*sl[0]/sl[2]/k0:.6f}')
