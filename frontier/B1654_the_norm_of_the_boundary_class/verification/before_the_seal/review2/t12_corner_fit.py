# Local structure of D near omega (non-grid points on small circles): D ~ alpha*d + beta*conj(d); range of |D|/(|R|^2 |d|) over directions
import math, numpy as np, pre2
ns = pre2.load(); cA=ns['cA']; R_A=ns['R_A']; D_of=ns['D_of']; nR2=ns['nR2']; W=ns['W']
def Dn(tau):
    R=R_A(tau); c={r:cA(r,tau,1e-5,nth=96,ns=64) for r in (2,3,4)}
    return D_of(c,R)/nR2(R)
for rad in (0.01,0.03,0.054,0.0736):
    vals=[]
    for k in range(16):
        ph=2*math.pi*k/16
        d=rad*complex(math.cos(ph),math.sin(ph))
        tau=W+d
        # skip points that leave the fundamental domain region only for reporting (the formula is valid anywhere)
        vals.append((abs(Dn(tau))/rad, ph))
    v=[x[0] for x in vals]
    print(f"radius {rad}: |D|/(|R|^2 |d|) over 16 directions: min {min(v):.4f} max {max(v):.4f};  at phi=90deg: {vals[4][0]:.4f}")
# fit alpha, beta from radius 0.003
rad=0.003
ph=[2*math.pi*k/8 for k in range(8)]
A=[];b=[]
for p in ph:
    d=rad*complex(math.cos(p),math.sin(p)); D=Dn(W+d)
    A.append([d,np.conj(d)]); b.append(D)
sol,res,rk,sv=np.linalg.lstsq(np.array(A),np.array(b),rcond=None)
print("alpha, beta =",sol, " |alpha|,|beta| =",abs(sol[0]),abs(sol[1]), " range of |D|/(|R|^2|d|): [",abs(abs(sol[0])-abs(sol[1])),",",abs(sol[0])+abs(sol[1]),"]")
