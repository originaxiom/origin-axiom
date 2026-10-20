import numpy as np, mpmath as mp
exec(open("v1.py").read().split("# ---- 1.")[0])
gL,gR=W.gL,W.gR
gS=gR@inv(gL)@gR
print("eig gL",np.round(np.linalg.eigvals(gL),4)," eig gS(R L^-1 R)",np.round(np.linalg.eigvals(gS),4))
# modular transformation of Theta2=(th3(2t), -i th2(2t)) numerically
mp.mp.dps=30
def Th(t):
    q=mp.exp(2j*mp.pi*t)
    a=mp.nsum(lambda n:q**(n*n),[-mp.inf,mp.inf]); b=mp.nsum(lambda n:q**((n+mp.mpf(1)/2)**2),[-mp.inf,mp.inf])
    return np.array([complex(a),complex(-1j*b)])
t=0.13+1.1j
print("Theta(t+1)/Theta(t):",Th(t+1)/Th(t))
# S: find 2x2 M with Theta(-1/t)=sqrt(t) M Theta(t) using several taus
rows=[];rhs=[]
ts=[0.1+1.0j,-0.2+0.9j,0.3+1.3j,0.05+0.8j]
A=np.array([Th(x) for x in ts]); B=np.array([Th(-1/x)/np.sqrt(x) for x in ts])
M,res,_,_=np.linalg.lstsq(A,B,rcond=None); M=M.T
print("S-matrix on Theta (fit):\n",np.round(M,6),"resid",res)
print("eig of fitted S-matrix",np.round(np.linalg.eigvals(M),5), " det",np.round(np.linalg.det(M),5))
# fit also with tau=2tau convention: Theta(tau) at 2tau: -1/tau maps 2tau-> -2/tau ; level 2 => not full SL2 but fine
for k in (3,15):
    chiS=np.exp(-1j*k*np.pi/4); chiT=np.exp(1j*k*np.pi/12)
    print("k",k,"chi_T*eig(gL)",np.round(chiT*np.linalg.eigvals(gL),4)," chi_S*eig(gS)",np.round(chiS*np.linalg.eigvals(gS),4))
# check Theta transforms under SL2Z generators actually (weight 1/2, rep of dimension 2, maybe level 4 -> for  full SL2Z need 2-dim irreps of level 4? )
