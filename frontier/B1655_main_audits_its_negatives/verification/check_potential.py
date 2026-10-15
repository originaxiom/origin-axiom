# Does B1646's "never between" survive (a) one octic invariant, (b) the zero-modes' own one-loop term?
# D4 of B1646 used V = -A + A^2 + lam2*|a.a|^2 (quartic only) -> linear in y=|a.a|^2 at fixed A=|a|^2.
import numpy as np, math
from scipy.optimize import minimize
rng = np.random.default_rng(11)
def thetas(t, K=40):
    n = np.arange(-K, K+1); q = lambda x: np.exp(1j*np.pi*t*x)
    return np.sum(q((n+0.5)**2)), np.sum(q(n*n)), np.sum((-1.0)**n*q(n*n))
def Rtheta(t):
    th2, th3, th4 = thetas(t); den = np.pi*th2*th3*th4
    return np.array([-th2**2/den, -th4**2/den, 1j*th3**2/den])
def Y(a, R): return np.outer(a, R) + np.outer(R, a) - (a@R)*np.eye(3)
def mratio(a, R):
    s = np.linalg.svd(Y(a, R), compute_uv=False); return s[1]/s[0]
R = Rtheta(1j)
print("|R.R| =", abs(R@R))
def run(lam2, kappa=0.0, g=0.0, nstart=40):
    def V(p):
        a = p[:3]+1j*p[3:]; A = np.vdot(a, a).real; y = abs(a@a)**2
        v = -A + A*A + lam2*y + kappa*y*y
        if g != 0.0:
            s = np.linalg.svd(Y(a, R), compute_uv=False); s = s[s > 1e-300]
            v += g*np.sum(s**4*np.log(s**2))
        return v
    ms = []; ds = []
    for _ in range(nstart):
        res = minimize(V, rng.normal(size=6), method="BFGS", options={"gtol": 1e-12, "maxiter": 20000})
        a = res.x[:3]+1j*res.x[3:]; A = np.vdot(a, a).real
        ms.append(mratio(a, R)); ds.append(abs(a@a)/A)
    return np.array(ms), np.array(ds)
print("--- (a) add an octic invariant kappa*|a.a|^4 (kappa>0) with lam2<0 (tree-level, SO(3)xU(1) symmetric, NOT quartic):")
for lam2, kappa in ((-0.05, 0.5), (-0.2, 0.5), (-0.5, 0.5), (-1.0, 0.5)):
    ms, ds = run(lam2, kappa)
    print(f" lam2={lam2:5} kappa={kappa}: defect |a.a|/|a|^2 in [{ds.min():.3g},{ds.max():.3g}]  m in [{ms.min():.3g},{ms.max():.3g}]  #minima with 1e-3<m<0.45: {int(np.sum((ms>1e-3)&(ms<0.45)))}/{len(ms)}")
print("--- (b) quartic potential plus the zero-modes' own CW term g*sum s^4 ln s^2 (tau=i):")
for lam2, g in ((0.05, -0.2), (0.05, -0.05), (0.02, -0.1), (-0.02, 0.1), (0.0, -0.1), (0.1, -0.5)):
    ms, ds = run(lam2, 0.0, g)
    print(f" lam2={lam2:5} g={g:5}: defect in [{ds.min():.3g},{ds.max():.3g}]  m in [{ms.min():.3g},{ms.max():.3g}]  #minima with 1e-3<m<0.45: {int(np.sum((ms>1e-3)&(ms<0.45)))}/{len(ms)}")
