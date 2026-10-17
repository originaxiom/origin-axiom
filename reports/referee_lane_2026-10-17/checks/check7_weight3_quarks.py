"""The first fittable model of the grammar's triplet: quarks with L_q, u^c, d^c all in T, Higgs singlets, Yukawa weight 3.
M_k(rhobar x rhobar) at k=3 is two-dimensional: one symmetric form Ys and one antisymmetric form Ya.
M_u = Y_s + r_u Y_a,  M_d = Y_s + r_d Y_a  (overall scales free), tau shared: 6 real parameters for 8 observables
(m_u/m_t, m_c/m_t, m_d/m_b, m_s/m_b, |V_us|, |V_cb|, |V_ub|, J)."""
import numpy as np, sys, time
from scipy.optimize import minimize
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from check5_yukawa_dims import form_space, with_cusp_condition, rho_u_t, rho_u_s, monomials

Rt = np.kron(rho_u_t.conj(), rho_u_t.conj()); Rs = np.kron(rho_u_s.conj(), rho_u_s.conj())
K = 12
null, monos = form_space(Rt, Rs, K)
nullc = with_cusp_condition(null, monos, 9, 3)
assert nullc.shape[1] == 2, nullc.shape
n = len(monos)
# split into symmetric and antisymmetric parts
Pperm = np.zeros((9, 9))
for i in range(3):
    for j in range(3): Pperm[3*i + j, 3*j + i] = 1
def sym_part(v): c = v.reshape(9, n); return ((np.eye(9) + Pperm)/2 @ c)
def asym_part(v): c = v.reshape(9, n); return ((np.eye(9) - Pperm)/2 @ c)
cands = [sym_part(nullc[:, j]) for j in range(2)] + [asym_part(nullc[:, j]) for j in range(2)]
# pick the nonzero symmetric and antisymmetric representatives
cs = max(cands[:2], key=lambda c: np.abs(c).max()); ca = max(cands[2:], key=lambda c: np.abs(c).max())
cs /= np.abs(cs).max(); ca /= np.abs(ca).max()
print("weight-3 forms found: |sym| =", np.abs(cs).max(), " |asym| =", np.abs(ca).max())

# fast theta^2 evaluation (q = e^{2 pi i tau}); valid for |Re tau| <= 1/2 (principal branch of q^{1/4} fine)
NN = np.arange(-12, 13)
def XYZ(tau):
    q = np.exp(2j*np.pi*tau)
    t3 = np.sum(q**(NN**2/2.0)); t4 = np.sum((-1.0)**NN * q**(NN**2/2.0))
    t2 = 2*np.exp(1j*np.pi*tau/4)*np.sum(q**(np.arange(0, 12)*(np.arange(0, 12)+1)/2.0))
    return t2**2, t3**2, t4**2
def eta18(tau):
    q = np.exp(2j*np.pi*tau); k = np.arange(1, 60)
    return (np.exp(2j*np.pi*tau/24)*np.prod(1 - q**k))**18
mono_arr = np.array(monos)  # (n,3)
def forms(tau):
    X, Y, Z = XYZ(tau)
    mv = X**mono_arr[:, 0] * Y**mono_arr[:, 1] * Z**mono_arr[:, 2]
    e = eta18(tau)
    return (cs @ mv).reshape(3, 3)/e, (ca @ mv).reshape(3, 3)/e

# data at M_Z (Huang-Zhou 2021 masses; CKM from PDG)
mu, md, ms, mc, mb, mt = 1.23e-3, 2.67e-3, 53.16e-3, 0.620, 2.839, 168.26
data = dict(mu_mt=mu/mt, mc_mt=mc/mt, md_mb=md/mb, ms_mb=ms/mb, Vus=0.2250, Vcb=0.0410, Vub=0.00382, J=3.08e-5)
err  = dict(mu_mt=0.17, mc_mt=0.03, md_mb=0.07, ms_mb=0.09, Vus=0.01, Vcb=0.03, Vub=0.06, J=0.06)   # relative (log) errors
def observables(tau, ru, rd):
    Ys, Ya = forms(tau)
    Mu = Ys + ru*Ya; Md = Ys + rd*Ya
    Uu, su, _ = np.linalg.svd(Mu); Ud, sd, _ = np.linalg.svd(Md)   # columns of U = left singular vectors, descending
    # reorder ascending (u, c, t)
    Uu = Uu[:, ::-1]; su = su[::-1]; Ud = Ud[:, ::-1]; sd = sd[::-1]
    V = Uu.conj().T @ Ud
    J = np.imag(V[0,1]*V[1,2]*np.conj(V[0,2])*np.conj(V[1,1]))
    return dict(mu_mt=su[0]/su[2], mc_mt=su[1]/su[2], md_mb=sd[0]/sd[2], ms_mb=sd[1]/sd[2],
                Vus=abs(V[0,1]), Vcb=abs(V[1,2]), Vub=abs(V[0,2]), J=J)
def chi2(p):
    x, y, ru_r, ru_i, rd_r, rd_i = p
    if y < 0.5 or abs(x) > 0.5 or x*x + y*y < 1.0: return 1e6
    try:
        o = observables(x + 1j*y, ru_r + 1j*ru_i, rd_r + 1j*rd_i)
    except Exception: return 1e6
    c = 0.0
    for k in data:
        if k == 'J': c += ((o[k] - data[k])/(err[k]*abs(data[k])))**2
        else:
            if o[k] <= 0: return 1e6
            c += (np.log(o[k]/data[k])/err[k])**2
    return c
rng = np.random.default_rng(5)
best = (1e9, None); t0 = time.time()
NSTART = 400
for s in range(NSTART):
    x = rng.uniform(-0.5, 0.5); y = rng.uniform(0.9, 4.0)
    if x*x + y*y < 1: y = 1.1
    r = [rng.normal()*10**rng.uniform(-2, 1.5) for _ in range(4)]
    res = minimize(chi2, [x, y] + r, method='Nelder-Mead', options=dict(maxiter=4000, xatol=1e-8, fatol=1e-10))
    if res.fun < best[0]: best = (res.fun, res.x); print(f"  start {s}: chi2 = {res.fun:.3f} at tau = {res.x[0]:.3f}+{res.x[1]:.3f}i  [{time.time()-t0:.0f}s]")
print("\nbest chi2 =", best[0])
x, y, a, b, c, d = best[1]
o = observables(x + 1j*y, a + 1j*b, c + 1j*d)
print(f"tau = {x:.4f} + {y:.4f}i,  r_u = {a:.4f}{b:+.4f}i,  r_d = {c:.4f}{d:+.4f}i")
for k in data: print(f"  {k:6s}: model {o[k]:.4e}   data {data[k]:.4e}   pull {np.log(o[k]/data[k])/err[k] if k!='J' else (o[k]-data[k])/(err[k]*abs(data[k])):+.2f}")
