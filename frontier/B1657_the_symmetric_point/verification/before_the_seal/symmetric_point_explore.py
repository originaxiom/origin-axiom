"""EXPLORATION (main, firewalled, not a seal): the fibre frame at the order-3 point tau = omega.
Y(a; u) = a u^T + u a^T - (a.u) 1 (B1645/B1654).  R = (-th2^2, i th3^2, -th4^2)/th1'(0) in channels (2, 3, 4) (B1654).
Questions: (1) the order-3 move's matrix on the channel triplet; (2) its eigenlines at omega; (3) Y's spectrum with the
Higgs on each eigenline; (4) near omega, the scaling of the light masses."""
import numpy as np
np.set_printoptions(precision=6, suppress=True, linewidth=140)

def th(z, tau, K=30):
    q = np.exp(1j*np.pi*tau); n = np.arange(K); m = np.arange(1, K)
    t1 = 2*np.sum((-1)**n*q**((n+.5)**2)*np.sin((2*n+1)*np.pi*z))
    t2 = 2*np.sum(q**((n+.5)**2)*np.cos((2*n+1)*np.pi*z))
    t3 = 1 + 2*np.sum(q**(m**2)*np.cos(2*m*np.pi*z))
    t4 = 1 + 2*np.sum((-1)**m*q**(m**2)*np.cos(2*m*np.pi*z))
    return t1, t2, t3, t4

def tp(tau, K=30):
    q = np.exp(1j*np.pi*tau); n = np.arange(K)
    return 2*np.pi*np.sum((-1)**n*(2*n+1)*q**((n+.5)**2))

def Rvec(tau):
    _, t2, t3, t4 = th(0.0, tau); p = tp(tau)
    return np.array([-t2**2, 1j*t3**2, -t4**2])/p

def Y(a, u):
    return np.outer(a, u) + np.outer(u, a) - (a @ u)*np.eye(3)

def sv(M):
    return np.linalg.svd(M, compute_uv=False)

w = np.exp(2j*np.pi/3)
# (1) theta^2 triplet transformation under gamma: tau -> -1/(tau+1), which fixes omega.
def T2(tau):
    _, t2, t3, t4 = th(0.0, tau); return np.array([t2**2, t3**2, t4**2])
# Solve M from three generic tau: T2(gamma tau) = (tau+1) * M T2(tau)  (weight one), fit by least squares.
taus = [0.13+1.07j, -0.21+0.93j, 0.33+1.4j, 0.05+0.8j]
A = np.array([T2(t) for t in taus]); B = np.array([T2(-1/(t+1))/(t+1) for t in taus])
M, *_ = np.linalg.lstsq(A, B, rcond=None); M = M.T
print("M (theta^2 basis), T2(gamma tau) = (tau+1) M T2(tau):\n", M)
print("fit residual:", max(np.abs(B[i] - M @ A[i]).max() for i in range(4)))
# in R's basis: R = Dg * T2 / tp, Dg = diag(-1, i, -1).  tp is weight 3/2: tp(gamma tau) = c (tau+1)^{3/2} tp(tau).
Dg = np.diag([-1, 1j, -1])
MR = Dg @ M @ np.linalg.inv(Dg)
print("M in R's basis:\n", MR)
print("M^T M (orthogonal up to scalar?):\n", MR.T @ MR)
print("M^3:\n", np.linalg.matrix_power(MR, 3))
ev, V = np.linalg.eig(MR)
print("eigenvalues:", ev, " args/(2pi/3):", np.angle(ev)/(2*np.pi/3))
Rw = Rvec(w)
print("R(omega) =", Rw, " |R_r| =", np.abs(Rw), " R.R =", Rw @ Rw)
for k in range(3):
    v = V[:, k]; v = v/np.linalg.norm(v)
    ov = abs(np.vdot(v, Rw))/np.linalg.norm(Rw); ovc = abs(np.vdot(v, Rw.conj()))/np.linalg.norm(Rw)
    print(f"eigenline {k}: ev={ev[k]:.6f}  v.v={v@v:.3e}  |<v,R>|={ov:.6f}  |<v,Rbar>|={ovc:.6f}")
# (3) spectra at omega with the Higgs on each eigenline (u = R, P4')
print("\n(3) spectra at omega, u = R:")
for k in range(3):
    a = V[:, k]/np.linalg.norm(V[:, k]); s = sv(Y(a, Rw)); print(f"  a = eigenline {k}: s = {s/s[0]}")
a_rb = Rw.conj()/np.linalg.norm(Rw); print("  a = Rbar:", sv(Y(a_rb, Rw))/sv(Y(a_rb, Rw))[0])
a_r = Rw/np.linalg.norm(Rw); print("  a = R   :", sv(Y(a_r, Rw))/sv(Y(a_r, Rw))[0])
