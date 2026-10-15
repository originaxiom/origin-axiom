import numpy as np, itertools
from scipy.optimize import least_squares
I=1j
qi=np.array([[I,0],[0,-I]]);qj=np.array([[0,1],[-1,0]],dtype=complex);qk=qi@qj
C=[qj,qi,qk];E=qj
def Y(S,M): return np.array([[np.sum((a.T@E@S@b)*M) for b in C] for a in C])
def Y57(a,v): return np.outer(a,v)+np.outer(v,a)-(a@v)*np.eye(3)
rng=np.random.default_rng(0)
def rc(*s): return rng.normal(size=s)+1j*rng.normal(size=s)
# check ell = -polar_det(S, M eps)
S=rc(2,2);M=rc(2,2)
pol=lambda A,B: np.linalg.det(A+B)-np.linalg.det(A)-np.linalg.det(B)
print("ell vs polar:",np.trace(E@S@M.T), pol(S,M@E), pol(S,M@np.linalg.inv(E)))
# fit Y(L a, L' v) ~ T1 Y57(a,v) T2 ; unknown complex L(4x3),L'(4x3),T1,T2 ; use samples
N=60
As=[rc(3) for _ in range(N)];Vs=[rc(3) for _ in range(N)]
def unpack(x):
    z=x[:len(x)//2]+1j*x[len(x)//2:]
    L=z[:12].reshape(4,3);Lp=z[12:24].reshape(4,3);T1=z[24:33].reshape(3,3);T2=z[33:42].reshape(3,3);return L,Lp,T1,T2
def res(x):
    L,Lp,T1,T2=unpack(x);r=[]
    for a,v in zip(As,Vs):
        r.append((Y((L@a).reshape(2,2),(Lp@v).reshape(2,2))-T1@Y57(a,v)@T2).ravel())
    r=np.concatenate(r);return np.concatenate([r.real,r.imag])
best=9
for t in range(12):
    x0=rng.normal(size=84)*0.7
    s=least_squares(res,x0,method='lm',max_nfev=3000)
    rel=np.linalg.norm(s.fun)/np.sqrt(sum(np.linalg.norm(Y57(a,v))**2 for a,v in zip(As,Vs)))
    L,Lp,T1,T2=unpack(s.x); print(t,rel,np.linalg.norm(T1@T2)); best=min(best,rel)
print("best rel residual",best)
# also with Y(S,M) as function of (S, M eps^-1) full 4-dim symmetric check
def Z(S,N): return Y(S,N@np.linalg.inv(E))
S=rc(2,2);N_=rc(2,2)
# is Z(S,N) = T Z(N,S) T' ? linear solve on 3x3 matrices T,T' by least squares over samples (bilinear -> alternate)
samples=[(rc(2,2),rc(2,2)) for _ in range(40)]
def r2(x):
    z=x[:18]+1j*x[18:];T=z[:9].reshape(3,3);Tp=z[9:].reshape(3,3);r=[]
    for S,N_ in samples: r.append((Z(S,N_)-T@Z(N_,S)@Tp).ravel())
    r=np.concatenate(r);return np.concatenate([r.real,r.imag])
b=9
for t in range(8):
    s=least_squares(r2,rng.normal(size=36),method='lm');b=min(b,np.linalg.norm(s.fun))
print("sym fit residual",b)
