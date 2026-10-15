"""C1 exploration (main, unsealed, labelled): the boundary-class Higgs normalised by its Szegő norm cut at a common radius.
||S_r||^2 over P minus D_eps = 2 pi log(1/eps) + c_r(tau). With u_r = sqrt(2 pi L + c_r) R_r, u.u = sum c_r R_r^2 =: D(tau)
because R.R = 0 (Jacobi). Checks: c_r independent of the split radius rho; c_2 = c_3 = c_4 at omega; c_2 = c_4 at i."""
import numpy as np
from numpy.polynomial.legendre import leggauss
K = 30
def thetas(z, tau):
    q = np.exp(1j*np.pi*tau); n = np.arange(0, K)
    z = np.asarray(z)[..., None]
    t1 = 2*np.sum((-1)**n * q**((n+.5)**2) * np.sin((2*n+1)*np.pi*z), -1)
    t2 = 2*np.sum(q**((n+.5)**2) * np.cos((2*n+1)*np.pi*z), -1)
    m = np.arange(1, K)
    t3 = 1 + 2*np.sum(q**(m**2) * np.cos(2*m*np.pi*z), -1)
    t4 = 1 + 2*np.sum((-1)**m * q**(m**2) * np.cos(2*m*np.pi*z), -1)
    return t1, t2, t3, t4
def th1p(tau):
    q = np.exp(1j*np.pi*tau); n = np.arange(0, K)
    return 2*np.pi*np.sum((-1)**n*(2*n+1)*q**((n+.5)**2))
def S(r, z, tau):
    t = thetas(z, tau); t0 = thetas(np.array(0.0), tau)
    return t[r-1]*th1p(tau)/(t0[r-1]*t[0])
def rmax(th, tau):
    d = np.exp(1j*th); y1 = d.imag/tau.imag; x1 = d.real - y1*tau.real
    return 0.5/np.maximum(np.abs(x1), np.abs(y1))
def laurent(r, tau, n, rho=0.05, N=256):
    t = 2*np.pi*np.arange(N)/N; z = rho*np.exp(1j*t)
    return np.mean(S(r, z, tau)*z**(-n))          # coefficient of z^(n-1)... see below
def c_r(r, tau, rho, Nth=1600, Nr=120):
    # vertex directions of P = {x + y tau : |x|,|y| <= 1/2} as breakpoints
    verts = [0.5+0.5*tau, -0.5+0.5*tau, -0.5-0.5*tau, 0.5-0.5*tau]
    br = sorted(np.mod(np.angle(verts), 2*np.pi)); br = br + [br[0]+2*np.pi]
    xg, wg = leggauss(Nth//4); xr, wr = leggauss(Nr); tot = 0.0
    for a, b in zip(br[:-1], br[1:]):
        th = 0.5*(b-a)*xg + 0.5*(b+a); wt = 0.5*(b-a)*wg
        R = rmax(th, tau)
        rr = 0.5*(R-rho)[:, None]*xr[None, :] + 0.5*(R+rho)[:, None]; wr2 = 0.5*(R-rho)[:, None]*wr[None, :]
        z = rr*np.exp(1j*th)[:, None]
        tot += np.sum(wt[:, None]*wr2*np.abs(S(r, z, tau))**2*rr)
    # inner disc rho: S = 1/z + s1 z + s3 z^3 + ... ; int_{eps<|z|<rho} |S|^2 = 2 pi log(rho/eps) + sum_n |s_n|^2 pi rho^(2n+2)/(n+1)
    s1 = laurent(r, tau, 2); s3 = laurent(r, tau, 4)   # mean(S z^-n) on |z|=rho gives coeff of z^n... (S = sum a_k z^k => mean(S z^-n) = a_n)
    return tot + 2*np.pi*np.log(rho) + abs(s1)**2*np.pi*rho**4/2 + abs(s3)**2*np.pi*rho**8/4, s1
def eta3_2pi(tau): return th1p(tau)               # theta1'(0) = 2 pi eta^3
def R_triplet(tau):
    t0 = thetas(np.array(0.0), tau); d = eta3_2pi(tau)
    return {2: -t0[1]**2/d, 4: -t0[3]**2/d, 3: 1j*t0[2]**2/d}      # R_i (th2), R_j (th4), R_k (th3), B1644
if __name__ == "__main__":
    w = np.exp(2j*np.pi/3)
    for name, tau in [("omega", w), ("i", 1j), ("0.13+1.07i", 0.13+1.07j), ("0.3+1.6i", 0.3+1.6j), ("2.2i", 2.2j), ("3.0i", 3.0j)]:
        tau = complex(tau); Rt = R_triplet(tau)
        cs = {}
        for r in (2, 3, 4):
            ca, s1 = c_r(r, tau, 0.05); cb, _ = c_r(r, tau, 0.09)
            cs[r] = ca
            print(f"  tau={name} r={r}: c_r(rho=.05)={ca:.10f}  c_r(rho=.09)={cb:.10f}  diff={abs(ca-cb):.1e}  s1={s1:.4f}")
        RR = sum(Rt[r]**2 for r in (2, 3, 4)); nR2 = sum(abs(Rt[r])**2 for r in (2, 3, 4))
        D = sum(cs[r]*Rt[r]**2 for r in (2, 3, 4))
        print(f"tau={name}: R.R/|R|^2={abs(RR)/nR2:.1e}  D/|R|^2 = {D/nR2:.6e}  |D|/|R|^2 = {abs(D)/nR2:.6e}   |q|={abs(np.exp(1j*np.pi*tau)):.3e}")
