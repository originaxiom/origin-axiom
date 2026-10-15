import time, math, numpy as np, sys
sys.path.insert(0,'.'); import b1654_routeA as B
from numpy.polynomial import chebyshev as Ch
X0,X1,Y0,Y1=-0.5,0.5,0.86,4.5
def ctil(tau): return np.array([B.cA(r,tau,1e-5)-math.pi*math.log(tau.imag) for r in (2,4,3)])  # order: units i(th2), j(th4), k(th3)
def nodes(n,a,b): k=np.arange(n); x=np.cos(np.pi*(k+0.5)/n); return 0.5*(b-a)*x+0.5*(b+a), x
def build(nx,ny):
    xs,ux=nodes(nx,X0,X1); ys,uy=nodes(ny,Y0,Y1)
    V=np.zeros((nx,ny,3))
    for i,x in enumerate(xs):
        for j,y in enumerate(ys): V[i,j]=ctil(complex(x,y))
    # 2D Chebyshev coefficients via separable fit
    Tx=Ch.chebvander(ux,nx-1); Ty=Ch.chebvander(uy,ny-1)
    Cf=np.einsum('ia,jb,ijc->abc',np.linalg.inv(Tx).T.T if False else np.linalg.inv(Tx),np.linalg.inv(Ty),V) if False else None
    A=np.linalg.solve(Tx, V.reshape(nx,-1)).reshape(nx,ny,3)        # coefficients along x
    Cf=np.linalg.solve(Ty, A.transpose(1,0,2).reshape(ny,-1)).reshape(ny,nx,3).transpose(1,0,2)
    return Cf
def ev(Cf,tau):
    ux=(2*tau.real-(X1+X0))/(X1-X0); uy=(2*tau.imag-(Y1+Y0))/(Y1-Y0)
    tx=Ch.chebvander(np.array([ux]),Cf.shape[0]-1)[0]; ty=Ch.chebvander(np.array([uy]),Cf.shape[1]-1)[0]
    return np.einsum('a,b,abc->c',tx,ty,Cf)
t0=time.time(); Cf=build(14,22); print('built',time.time()-t0)
rng=np.random.default_rng(5); worst=0
for _ in range(12):
    x=rng.uniform(-0.5,0.5); y=rng.uniform(math.sqrt(1-x*x),4.4); tau=complex(x,y)
    d=ctil(tau); e=ev(Cf,tau); worst=max(worst,np.max(np.abs(d-e))); 
print('worst abs err', worst, time.time()-t0)
