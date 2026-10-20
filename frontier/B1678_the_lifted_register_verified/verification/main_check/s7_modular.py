import mpmath as mp, numpy as np
mp.mp.dps=30
def th(k,z,tau):
    N=40
    if k==3: return sum(mp.exp(1j*mp.pi*n*n*tau+2j*mp.pi*n*z) for n in range(-N,N+1))
    if k==2: return sum(mp.exp(1j*mp.pi*(n+mp.mpf(1)/2)**2*tau+2j*mp.pi*(n+mp.mpf(1)/2)*z) for n in range(-N,N))
    if k==1: return -1j*sum((-1)**n*mp.exp(1j*mp.pi*(n+mp.mpf(1)/2)**2*tau+2j*mp.pi*(n+mp.mpf(1)/2)*z) for n in range(-N,N))

def F(z,tau): return mp.matrix([1j*th(2,z,2*tau),th(3,z,2*tau)])/mp.sqrt(th(1,z,tau))
def const_matrix(fun,tau,zs):
    # find G with fun(z)=G F(z): solve with two z points, verify on third
    A=mp.matrix(2,2);B=mp.matrix(2,2)
    for j,z in enumerate(zs[:2]):
        f=F(z,tau);g=fun(z)
        for i in range(2): A[i,j]=f[i];B[i,j]=g[i]
    G=B*mp.inverse(A)
    z=zs[2];res=mp.norm(G*F(z,tau)-fun(z))
    return G,res
qi=np.array([[1j,0],[0,-1j]]);qj=np.array([[0,1],[-1,0]],dtype=complex)
gL=(np.eye(2)+qi)/np.sqrt(2);gR=(np.eye(2)-qj)/np.sqrt(2)
tau=mp.mpc('0.21','0.93')
zs=[mp.mpc('0.07','0.03'),mp.mpc('0.11','-0.05'),mp.mpc('0.05','0.02')]
G,res=const_matrix(lambda z:F(z,tau+1),tau,zs)
print("F(z,tau+1)=G F(z,tau), residual",mp.nstr(res,3))
Gn=np.array(G.tolist(),dtype=complex)
k=np.exp(1j*np.pi/8)
print(" G/e^{i pi/8} =",np.round(Gn/k,5).tolist()," vs gL =",np.round(gL,5).tolist())
# S: z -> z/tau, tau -> -1/tau
G2,res2=const_matrix(lambda z:F(z/tau,-1/tau),tau,zs)
print("F(z/tau,-1/tau)=G2 F(z,tau), residual",mp.nstr(res2,3))
G2n=np.array(G2.tolist(),dtype=complex)
t=complex(tau)
for name,c in [("tau^{1/4}",t**0.25)]:
    M=G2n/c/np.exp(-3j*np.pi/8)
    print(" G2/(tau^{1/4} e^{-3 pi i/8}) =",np.round(M,5).tolist())
gi=np.linalg.inv
cands={"gS=gR gL^-1 gR":gR@gi(gL)@gR,"gL^-1 gR gL^-1 (Delta^-1)":gi(gL)@gR@gi(gL),"gDelta=gL gR^-1 gL":gL@gi(gR)@gL}
for n,c in cands.items():
    print("  cand",n,"det",np.round(np.linalg.det(c),4),"match up to scalar?",[np.round(np.vdot(c.flatten(),M.flatten())/np.vdot(c.flatten(),c.flatten()),4)], "resid", np.round(np.abs(M-np.vdot(c.flatten(),M.flatten())/np.vdot(c.flatten(),c.flatten())*c).max(),5))
