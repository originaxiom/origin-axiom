import numpy as np
np.set_printoptions(precision=4, suppress=True)
phi=(1+5**0.5)/2; sp_=phi**0.5
M=np.array([[1,1,1,1],[1,0,1,0],[2,1,1,1],[1,1,1,0]],float)
r=np.array([phi,1,phi*sp_,sp_])
beta=phi*(1+sp_)
print("M r = beta r?", np.allclose(M@r, beta*r), " beta=",round(beta,6))
# left Perron ell: ell^T M = beta ell^T, normalized ell^T r =1
w,V=np.linalg.eig(M.T); i=np.argmax(w.real); ell=V[:,i].real; ell=ell/(ell@r)
print("ell^T M = beta ell^T?", np.allclose(ell@M, beta*ell), " ell^T r=",round(ell@r,6))

D=np.diag(r); C=np.eye(4)-np.ones((4,4))/4
S=np.linalg.inv(D)@C@np.linalg.inv(D)
print("\nS_tet rank:", np.linalg.matrix_rank(S), " S_tet r ~0?", np.allclose(S@r,0))
# weighted Gram of d_i = r_i e_i
d=[r[i]*np.eye(4)[:,i] for i in range(4)]
G=np.array([[d[a]@S@d[b] for b in range(4)] for a in range(4)])
print("weighted Gram (should be 3/4 diag, -1/4 off):\n", G)
print("tetrahedron Gram correct?", np.allclose(G, C))

Giso=S-np.outer(ell,ell)
def sig(A):
    ev=np.linalg.eigvalsh((A+A.T)/2); return (int((ev>1e-9).sum()), int((ev<-1e-9).sum()), int((abs(ev)<=1e-9).sum()))
print("\n--- INDEPENDENT signatures via eigenvalues (not leading minors) ---")
print("G_iso signature (pos,neg,null):", sig(Giso), " G_iso(r,r)=",round(r@Giso@r,4),"(r timelike)")
Wiso=Giso-M.T@Giso@M
print("W_iso signature:", sig(Wiso), " -> positive definite?", sig(Wiso)[1]==0, "(no-go: NOT pos-def)")
# W_stable = S - M^T S M restricted to E_s = ker(ell^T)
B=np.column_stack([ell[i]*np.eye(4)[:,0]-ell[0]*np.eye(4)[:,i] for i in (1,2,3)])
Wst=B.T@(S-M.T@S@M)@B
print("W_stable signature:", sig(Wst), " det<0?", np.linalg.det(Wst)<0)

print("\n--- ADVERSARIAL: is the no-go just 'beta>1'? test the expanding vs contracting story ---")
# along expanding r (timelike): W(r,r) should be POSITIVE (so negativity is NOT from beta>1)
print("W_iso(r,r) =", round(r@Wiso@r,4), "(>0 => the expanding dir is fine; negativity is elsewhere)")
# M restricted to E_s has all |eig|<1 (contracting) yet W_stable is indefinite => NON-NORMAL growth
evEs=np.linalg.eigvals(np.linalg.pinv(B)@M@B)
print("eig(M|E_s) moduli:", [round(abs(e),3) for e in evEs], "(all<1: contracting)")
print("=> W_stable indefinite despite spectral contraction => NON-NORMALITY, not beta>1. No-go is real.")

print("\n--- RG exponents (independent) ---")
h=phi*(1-sp_); gam=-1/phi+1j*(5**0.5-2)**0.5
print("omega_h =", round(-np.log(abs(h))/np.log(beta),16))
print("omega_gamma =", round(-np.log(abs(gam))/np.log(beta),16))
Om=np.angle(gam)/np.log(beta)
print("Omega =", round(Om,15), " exp(2pi/Omega) =", round(np.exp(2*np.pi/Om),14))
