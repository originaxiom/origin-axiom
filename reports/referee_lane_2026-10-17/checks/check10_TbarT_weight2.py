"""Dirac couplings with L in T and u^c, d^c in Tbar: Y in M_k(rhobar x rho), k even. At k=2 the space is 2-dim.
det Y is then a level-one form of weight 6 (times a constant), so theta-bar = arg det(M_u M_d) = 2 arg E6(tau) + const,
exponentially small at large Im tau. Question: can the quark masses and CKM be fitted there (5 real params: Re tau + two
complex ratios, Im tau >= 4.5 fixed by theta-bar), and what is theta-bar at the best point?"""
import numpy as np, sys, time
from scipy.optimize import minimize
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from check5_yukawa_dims import form_space, rho_u_t, rho_u_s, monomials

Rt = np.kron(rho_u_t.conj(), rho_u_t); Rs = np.kron(rho_u_s.conj(), rho_u_s)
K = 2
null, monos = form_space(Rt, Rs, K)
assert null.shape[1] == 2, null.shape
n = len(monos); mono_arr = np.array(monos)
cA = null[:, 0].reshape(9, n); cB = null[:, 1].reshape(9, n)
NN = np.arange(-12, 13)
def XYZ(tau):
    q = np.exp(2j*np.pi*tau)
    t3 = np.sum(q**(NN**2/2.0)); t4 = np.sum((-1.0)**NN * q**(NN**2/2.0))
    t2 = 2*np.exp(1j*np.pi*tau/4)*np.sum(q**(np.arange(0, 12)*(np.arange(0, 12)+1)/2.0))
    return t2**2, t3**2, t4**2
def E6(tau):
    q = np.exp(2j*np.pi*tau); k = np.arange(1, 40)
    return 1 - 504*np.sum(k**5*q**k/(1 - q**k))
def forms(tau):
    X, Y, Z = XYZ(tau); mv = X**mono_arr[:, 0]*Y**mono_arr[:, 1]*Z**mono_arr[:, 2]
    return (cA @ mv).reshape(3, 3), (cB @ mv).reshape(3, 3)
# show the forms' structure at a sample point and check det ~ E6
tau0 = 0.2 + 1.3j
A, B = forms(tau0)
print("form A at tau0 (rounded):\n", np.round(A, 3)); print("form B at tau0 (rounded):\n", np.round(B, 3))
for t in (0.2+1.3j, -0.4+0.9j, 0.1+2.5j):
    A, B = forms(t); print("tau =", t, " det(A + 0.3i B)/E6 =", np.round(np.linalg.det(A + 0.3j*B)/E6(t), 6))
mu, md, ms, mc, mb, mt = 1.23e-3, 2.67e-3, 53.16e-3, 0.620, 2.839, 168.26
data = dict(mu_mt=mu/mt, mc_mt=mc/mt, md_mb=md/mb, ms_mb=ms/mb, Vus=0.2250, Vcb=0.0410, Vub=0.00382, J=3.08e-5)
err  = dict(mu_mt=0.17, mc_mt=0.03, md_mb=0.07, ms_mb=0.09, Vus=0.01, Vcb=0.03, Vub=0.06, J=0.06)
def observables(tau, ru, rd):
    A, B = forms(tau); Mu = A + ru*B; Md = A + rd*B
    Uu, su, _ = np.linalg.svd(Mu); Ud, sd, _ = np.linalg.svd(Md)
    Uu = Uu[:, ::-1]; su = su[::-1]; Ud = Ud[:, ::-1]; sd = sd[::-1]
    V = Uu.conj().T @ Ud
    J = np.imag(V[0,1]*V[1,2]*np.conj(V[0,2])*np.conj(V[1,1]))
    thetabar = np.angle(np.linalg.det(Mu)*np.linalg.det(Md))
    return dict(mu_mt=su[0]/su[2], mc_mt=su[1]/su[2], md_mb=sd[0]/sd[2], ms_mb=sd[1]/sd[2],
                Vus=abs(V[0,1]), Vcb=abs(V[1,2]), Vub=abs(V[0,2]), J=J), thetabar
def chi2(p, ymin):
    x, y, a, b, c, d = p
    if y < ymin or abs(x) > 0.5 or x*x + y*y < 1.0: return 1e6
    try: o, _ = observables(x + 1j*y, a + 1j*b, c + 1j*d)
    except Exception: return 1e6
    s = 0.0
    for k in data:
        if k == 'J': s += ((o[k] - data[k])/(err[k]*abs(data[k])))**2
        else:
            if not o[k] > 0: return 1e6
            s += (np.log(o[k]/data[k])/err[k])**2
    return s
rng = np.random.default_rng(9)
for ymin, label in ((0.87, "free tau"), (4.5, "Im tau >= 4.5 (theta-bar < 1e-9)")):
    best = (1e9, None); t0 = time.time()
    for s in range(300):
        x = rng.uniform(-0.5, 0.5); y = rng.uniform(max(ymin, 1.0), max(ymin, 1.0) + 3.0)
        r = [rng.normal()*10**rng.uniform(-3, 2) for _ in range(4)]
        res = minimize(chi2, [x, y] + r, args=(ymin,), method='Nelder-Mead', options=dict(maxiter=4000, xatol=1e-9, fatol=1e-10))
        if res.fun < best[0]: best = (res.fun, res.x)
    x, y, a, b, c, d = best[1]; o, tb = observables(x + 1j*y, a + 1j*b, c + 1j*d)
    print(f"\n[{label}] best chi2 = {best[0]:.2f} at tau = {x:.4f}+{y:.4f}i, r_u = {a:.3g}{b:+.3g}i, r_d = {c:.3g}{d:+.3g}i  [{time.time()-t0:.0f}s]")
    print(f"   theta-bar (tree level, real coefficients would remove the coefficient phase) = {tb:+.3e};  2*arg E6 = {2*np.angle(E6(x+1j*y)):+.3e}")
    for k in data: print(f"   {k:6s}: model {o[k]:.3e}  data {data[k]:.3e}  pull {np.log(o[k]/data[k])/err[k] if k!='J' else (o[k]-data[k])/(err[k]*abs(data[k])):+.2f}")
