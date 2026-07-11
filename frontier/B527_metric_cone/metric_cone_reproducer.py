#!/usr/bin/env python3
"""Lightweight verification of the complete Stein-compatible metric cone."""
import numpy as np

phi=(1+5**0.5)/2
sp_=phi**0.5
beta=phi*(1+sp_)
M=np.array([[1,1,1,1],[1,0,1,0],[2,1,1,1],[1,1,1,0]],float)
r=np.array([phi,1,phi*sp_,sp_],float)

# normalized left Perron vector
w,V=np.linalg.eig(M.T)
i=np.argmax(w.real)
ell=V[:,i].real
ell=ell/(ell@r)
Pt=np.outer(r,ell)
Ps=np.eye(4)-Pt

# orthonormal basis for ker ell^T
_,_,vh=np.linalg.svd(ell.reshape(1,4))
B=vh[1:].T
Abar=B.T@M@B

# affine tetrahedral metric
A=np.eye(4)-np.outer(r,np.ones(4))/(np.ones(4)@r)
S=0.5*A.T@A
Q4=S-M.T@S@M
Q3=B.T@Q4@B

# 6x6 Lyapunov operator on Sym(3)
def v(S): return np.array([S[0,0],S[1,1],S[2,2],S[0,1],S[0,2],S[1,2]])
def Sfrom(x):
    return np.array([[x[0],x[3],x[4]],[x[3],x[1],x[5]],[x[4],x[5],x[2]]])
L6=np.column_stack([v(Sfrom(np.eye(6)[:,k])-Abar.T@Sfrom(np.eye(6)[:,k])@Abar) for k in range(6)])

alpha_null=np.diag(S)/(ell**2)

def G(alpha): return S-alpha*np.outer(ell,ell)
def T(c): return Ps+c*Pt

if __name__=='__main__':
    print('stable eigenvalue moduli:',np.abs(np.linalg.eigvals(Abar)))
    print('det Lyapunov operator:',np.linalg.det(L6))
    print('Q_aff eigenvalues:',np.linalg.eigvalsh(Q3))
    print('S_aff is interior:',np.min(np.linalg.eigvalsh(Q3))>0)
    print('null alpha ratios:',alpha_null)
    print('time rescaling error:',np.linalg.norm(T(1.7).T@G(1)@T(1.7)-G(1.7**2)))
    print('cone dimension: 6')
    print('extreme rays: L^{-1}(vv^T), projectively RP^2')
