import numpy as np
np.set_printoptions(precision=4,suppress=True)
phi=(1+5**0.5)/2; sp_=phi**0.5; beta=phi*(1+sp_)
M=np.array([[1,1,1,1],[1,0,1,0],[2,1,1,1],[1,1,1,0]],float)
r=np.array([phi,1,phi*sp_,sp_],float)
w,V=np.linalg.eig(M.T); ell=V[:,int(np.argmax(w.real))].real; ell=ell/(ell@r)

# --- my OWN basis for E_s = ker(ell^T): use QR on a spanning set (independent of their SVD) ---
# columns spanning ker ell^T: ell_i e_0 - ell_0 e_i, i=1,2,3, then orthonormalize
raw=np.column_stack([ell[i]*np.eye(4)[:,0]-ell[0]*np.eye(4)[:,i] for i in (1,2,3)])
B,_=np.linalg.qr(raw)  # 4x3 orthonormal basis of E_s
assert np.allclose(ell@B,0), "B not in ker ell^T"
Abar=B.T@M@B
print("1) M|E_s eigenvalue moduli:", np.abs(np.linalg.eigvals(Abar)), "-> all<1:", np.all(np.abs(np.linalg.eigvals(Abar))<1-1e-9))
print("   (these are |h|,|gamma|,|gamma| = the stable spectrum)")

# --- Lyapunov operator L(S)=S - Abar^T S Abar on Sym(3), as 6x6 ---
def vec(S): return np.array([S[0,0],S[1,1],S[2,2],S[0,1],S[0,2],S[1,2]])
def mat(x): return np.array([[x[0],x[3],x[4]],[x[3],x[1],x[5]],[x[4],x[5],x[2]]])
L6=np.column_stack([vec(mat(e)-Abar.T@mat(e)@Abar) for e in np.eye(6)])
print("\n2) det(L) =", round(np.linalg.det(L6),6), "-> invertible:", abs(np.linalg.det(L6))>1e-9,
      "=> C_metric = L^{-1}(PSD(3)) is a full 6-dim cone")
# check L^{-1}(Q)=sum series matches
Qtest=np.eye(3)
series=sum(np.linalg.matrix_power(Abar.T,n)@Qtest@np.linalg.matrix_power(Abar,n) for n in range(200))
Linv_Q=mat(np.linalg.solve(L6,vec(Qtest)))
print("   L^{-1}(I) matches the series sum:", np.allclose(series,Linv_Q))

# --- KEY: S_aff in the interior? (driver Q_aff PD) ---
A=np.eye(4)-np.outer(r,np.ones(4))/(np.ones(4)@r)
Saff=0.5*A.T@A
Q3=B.T@(Saff-M.T@Saff@M)@B
print("\n3) S_aff driver Q_aff eigenvalues:", np.linalg.eigvalsh(Q3), "-> PD:", np.min(np.linalg.eigvalsh(Q3))>1e-9)
print("   => S_aff IS Stein-compatible, in the INTERIOR of the cone (not an extreme ray).")

# --- RECONCILE with B526: its S_tet should be OUTSIDE the cone (driver indefinite) ---
D=np.diag(r); Stet=np.linalg.inv(D)@(np.eye(4)-np.ones((4,4))/4)@np.linalg.inv(D)
Q3_tet=B.T@(Stet-M.T@Stet@M)@B
evt=np.linalg.eigvalsh(Q3_tet)
print("\n4) B526 S_tet driver eigenvalues on E_s:", evt, "-> signature",
      (int((evt>1e-9).sum()),int((evt<-1e-9).sum())), "(indefinite => S_tet NOT in the cone)")
print("   => CONSISTENT: B526's no-go was specific to a non-Stein metric; S_aff is a Stein one.")
print("   S_aff != S_tet:", not np.allclose(Saff/np.linalg.norm(Saff), Stet/np.linalg.norm(Stet)))

# --- alpha rescaling identity + signature + Stein-positivity of the Lorentzian completion ---
Pt=np.outer(r,ell); Ps=np.eye(4)-Pt
def G(al): return Saff-al*np.outer(ell,ell)
def Tc(c): return Ps+c*Pt
c=1.7
print("\n5) T_c^T G(1) T_c == G(c^2)?  err =", np.linalg.norm(Tc(c).T@G(1)@Tc(c)-G(c*c)))
def sig(X):
    e=np.linalg.eigvalsh((X+X.T)/2); return (int((e>1e-9).sum()),int((e<-1e-9).sum()))
print("   G(1) signature:", sig(G(1)), " Stein G-M^TGM > 0:", np.min(np.linalg.eigvalsh(G(1)-M.T@G(1)@M))>1e-9)

# --- four different null alphas (letters not equivalent null rays) ---
an=np.diag(Saff)/(ell**2)
print("\n6) null alpha_i = S_ii/ell_i^2:", np.round(an,4), "-> all distinct:", len(set(np.round(an,6)))==4)
