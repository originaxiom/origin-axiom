"""B1669 -- THE DEDEKIND PHASE (the parameter-free Yukawa sector of the weave's triplet, and the strong CP angle on the
ruled branch): the sealed instrument.

Convention (the paper's, Theorem 9; B1634's hand): rho = chi_eta^21 (x) rho_u on T = span(theta2^2, theta3^2, theta4^2),
f(g tau) = rho(g) (c tau + d)^k f(tau); s: tau -> -1/tau, t: tau -> tau + 1; chi_eta(t) = e^{2 pi i/24}, chi_eta(s) = e^{-i pi/4}.
A coupling L^T Y R with L, R in T is a vector-valued form for rhobar (x) rhobar (weight k odd); with R in Tbar, for
rhobar (x) rho (weight k even). Forms are polynomials in X = theta2^2, Y = theta3^2, Z = theta4^2 modulo Jacobi's
Y^2 = X^2 + Z^2 (B1635's route), with eta^18 (resp. 1) factored out and the cusp condition imposed on the q-series.

Cells (PREREGISTRATION section 3): C0 plumbing; N8a the sum rule and the half floor; N8b the parameter-free sector is
one form per weight; N10a the determinant identities; N10b the phase law; N10c the lowest fittable models' chi^2 floors.
"""
import json, math, os, time, itertools
import numpy as np
from numpy.linalg import svd
import sympy as sp
from scipy.optimize import minimize

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
LOG = open(os.path.join(HERE, "the_dedekind_phase_run.txt"), "w")
def log(s):
    print(s); LOG.write(s + "\n"); LOG.flush()
out = {}

# ---------------------------------------------------------------- the representation
I3 = np.eye(3, dtype=complex)
P24 = np.array([[0,0,1],[0,1,0],[1,0,0]], dtype=complex); P34 = np.array([[1,0,0],[0,0,1],[0,1,0]], dtype=complex)
rho_u_t = np.diag([1j, 1, 1]) @ P34          # theta2^2 -> i theta2^2, theta3^2 <-> theta4^2
rho_u_s = -1j * P24                          # theta_j^2(-1/tau) = -i tau (swapped theta)^2
chi_t, chi_s = np.exp(2j*np.pi/24), np.exp(-1j*np.pi/4)
rho_t, rho_s = chi_t**21 * rho_u_t, chi_s**21 * rho_u_s
def key(Mx): return tuple(np.round(Mx, 8).flatten().view(float))
def generate(gens):
    el = {key(I3): I3}; fr = [I3]
    while fr:
        new = []
        for g in fr:
            for h in gens:
                p = g @ h; k = key(p)
                if k not in el: el[k] = p; new.append(p)
        fr = new
    return list(el.values())
G = generate([rho_s, rho_t]); st = rho_s @ rho_t
expo = sorted(np.round((np.angle(np.linalg.eigvals(rho_t))/(2*np.pi)) % 1, 6))
plumb = dict(order=len(G), braid=bool(np.allclose(rho_s @ rho_s, st @ st @ st)), s4_is_minus_one=bool(np.allclose(np.linalg.matrix_power(rho_s, 4), -I3)), exponents=[float(x) for x in expo])
log(f"rho: image order {plumb['order']}, s^2 = (st)^3 {plumb['braid']}, s^4 = -1 {plumb['s4_is_minus_one']}, exponents of t {plumb['exponents']}")

# ---------------------------------------------------------------- forms as polynomials in X, Y, Z mod Y^2 = X^2 + Z^2
from math import comb
def monomials(K): return [(a, b, K - a - b) for b in (0, 1) for a in range(K - b + 1)]
def reduce_mono(a, b, c):
    out_ = {}; m, r = divmod(b, 2)
    for j in range(m + 1): out_[(a + 2*j, r, c + 2*(m - j))] = out_.get((a + 2*j, r, c + 2*(m - j)), 0) + comb(m, j)
    return out_
def act_T_mono(a, b, c): return {m: (1j)**a * v for m, v in reduce_mono(a, c, b).items()}
def act_S_mono(a, b, c, K): return {m: (-1j)**K * v for m, v in reduce_mono(c, b, a).items()}
def form_space(R_t, R_s, K):
    d = R_t.shape[0]; monos = monomials(K); n = len(monos); N = d*n; rows = []
    for act, Rm in ((lambda abc: act_T_mono(*abc), R_t), (lambda abc: act_S_mono(*abc, K), R_s)):
        for i in range(d):
            eq = {}
            for mi, abc in enumerate(monos):
                for m, v in act(abc).items(): eq[(m, i*n + mi)] = eq.get((m, i*n + mi), 0) + v
            for j in range(d):
                if abs(Rm[i, j]) > 0:
                    for mi, m in enumerate(monos): eq[(m, j*n + mi)] = eq.get((m, j*n + mi), 0) - Rm[i, j]
            bym = {}
            for (m, col), v in eq.items(): bym.setdefault(m, {})[col] = bym.get(m, {}).get(col, 0) + v
            for m, cols in bym.items():
                row = np.zeros(N, dtype=complex)
                for col, v in cols.items(): row[col] += v
                rows.append(row)
    A = np.array(rows); u, s, vh = svd(A); rank = int(np.sum(s > 1e-9*max(1, s[0])))
    return vh[rank:].conj().T, monos
NP = 90
def theta_series():
    t3 = np.zeros(NP); t4 = np.zeros(NP); s2 = np.zeros(NP)
    for nn in range(-25, 26):
        e = 2*nn*nn
        if e < NP: t3[e] += 1; t4[e] += (-1)**nn
    for nn in range(0, 25):
        e = 2*nn*nn + 2*nn
        if e < NP: s2[e] += 1
    mul = lambda a, b: np.convolve(a, b)[:NP]
    X = np.zeros(NP); X[1:] = 4*mul(s2, s2)[:NP-1]
    return X, mul(t3, t3), mul(t4, t4), mul
X_s, Y_s, Z_s, mul = theta_series()
assert np.abs(mul(Y_s, Y_s) - mul(X_s, X_s) - mul(Z_s, Z_s)).max() == 0, "Jacobi on the q-series"
_pc = {}
def mono_series(a, b, c):
    if (a, b, c) not in _pc:
        def pw(base, e):
            r = np.zeros(NP); r[0] = 1
            for _ in range(e): r = mul(r, base)
            return r
        _pc[(a, b, c)] = mul(mul(pw(X_s, a), pw(Y_s, b)), pw(Z_s, c))
    return _pc[(a, b, c)]
def with_cusp_condition(null, monos, d, min_p_order):
    if null.shape[1] == 0 or min_p_order <= 0: return null
    n = len(monos); rows = []
    for i in range(d):
        for pord in range(min_p_order):
            row = np.zeros(null.shape[1], dtype=complex)
            for col in range(null.shape[1]):
                v = null[:, col]
                row[col] = sum(v[i*n + mi]*mono_series(a, b, c)[pord] for mi, (a, b, c) in enumerate(monos) if abs(v[i*n + mi]) > 1e-12)
            rows.append(row)
    A = np.array(rows)
    if np.abs(A).max() < 1e-12: return null
    u, s, vh = svd(A); rank = int(np.sum(s > 1e-9*max(1, s[0])))
    return null @ vh[rank:].conj().T
Rt_TT, Rs_TT = np.kron(rho_u_t.conj(), rho_u_t.conj()), np.kron(rho_u_s.conj(), rho_u_s.conj())     # rhobar (x) rhobar, eta^18 factored
Rt_TbT, Rs_TbT = np.kron(rho_u_t.conj(), rho_u_t), np.kron(rho_u_s.conj(), rho_u_s)                   # rhobar (x) rho
Pperm = np.zeros((9, 9))
for i in range(3):
    for j in range(3): Pperm[3*i + j, 3*j + i] = 1
Pdiag = np.diag([1 if i == j else 0 for i in range(3) for j in range(3)]).astype(float)
Psym_off = (np.eye(9) + Pperm)/2 - Pdiag; Pasym = (np.eye(9) - Pperm)/2
def piece_dims(nullc, n):
    dims = {}
    for name, P in (("D", Pdiag), ("O+", Psym_off), ("O-", Pasym)):
        if nullc.shape[1] == 0: dims[name] = 0; continue
        cols = [(P @ nullc[:, c].reshape(9, n)).reshape(-1) for c in range(nullc.shape[1])]
        s = svd(np.array(cols).T, compute_uv=False); dims[name] = int(np.sum(s > 1e-9*max(1, s[0])))
    return dims
TT = {}; table_TT = {}
for k in range(1, 12, 2):
    null, monos = form_space(Rt_TT, Rs_TT, k + 9); nullc = with_cusp_condition(null, monos, 9, 3); TT[k] = (nullc, monos)
    table_TT[k] = dict(total=int(nullc.shape[1]), **piece_dims(nullc, len(monos)))
TbT = {}; table_TbT = {}
for k in range(0, 8, 2):
    null, monos = form_space(Rt_TbT, Rs_TbT, k); TbT[k] = (null, monos); table_TbT[k] = dict(total=int(null.shape[1]), **piece_dims(null, len(monos)))
log("dim M_k(rhobar x rhobar) by piece, k odd: " + "; ".join(f"k={k}: D {v['D']}, O+ {v['O+']}, O- {v['O-']} (total {v['total']})" for k, v in table_TT.items()))
log("dim M_k(rhobar x rho), k even: " + "; ".join(f"k={k}: D {v['D']}, O+ {v['O+']}, O- {v['O-']} (total {v['total']})" for k, v in table_TbT.items()))
B1635 = dict(D=[0, 0, 1, 1, 2, 2], Op=[1, 1, 2, 2, 3, 3], Om=[0, 1, 1, 2, 2, 3])
table_ok = all(table_TT[k]['D'] == B1635['D'][i] and table_TT[k]['O+'] == B1635['Op'][i] and table_TT[k]['O-'] == B1635['Om'][i] for i, k in enumerate(range(1, 12, 2)))
log(f"   B1635's table (D 0,0,1,1,2,2; O+ 1,1,2,2,3,3; O- 0,1,1,2,2,3) reproduced: {table_ok}")

# ---------------------------------------------------------------- numerics of the theta constants and eta (|Re tau| <= 1/2)
NN = np.arange(-14, 15)
def XYZ(tau):
    q = np.exp(2j*np.pi*tau)
    t3 = np.sum(q**(NN**2/2.0)); t4 = np.sum((-1.0)**NN * q**(NN**2/2.0))
    t2 = 2*np.exp(1j*np.pi*tau/4)*np.sum(q**(np.arange(0, 14)*(np.arange(0, 14)+1)/2.0))
    return t2**2, t3**2, t4**2
def eta(tau):
    q = np.exp(2j*np.pi*tau); kk = np.arange(1, 80); return np.exp(2j*np.pi*tau/24)*np.prod(1 - q**kk)
def E6(tau):
    q = np.exp(2j*np.pi*tau); kk = np.arange(1, 60); return 1 - 504*np.sum(kk**5*q**kk/(1 - q**kk))
def eval_form(coef, monos, tau, eta_power):
    X, Y, Z = XYZ(tau); ma = np.array(monos); mv = X**ma[:, 0]*Y**ma[:, 1]*Z**ma[:, 2]
    return (coef @ mv).reshape(3, 3)/(eta(tau)**eta_power if eta_power else 1.0)

# ---------------------------------------------------------------- N8: the weight-1 form, the sum rule, the half floor
nullc1, monos1 = TT[1]; c1 = nullc1[:, 0].reshape(9, len(monos1))
def Y1(tau): return eval_form(c1, monos1, tau, 18)
tau0 = -0.17 + 1.23j
Yv = Y1(tau0); X0, Y0, Z0 = XYZ(tau0)
closed = np.array([[0, Z0, Y0], [Z0, 0, X0], [Y0, X0, 0]])
scale = Yv[0, 1]/closed[0, 1]
closed_err = float(np.abs(Yv - scale*closed).max()/np.abs(Yv).max())
log(f"\nN8: the unique weight-1 form equals c * [[0, theta4^2, theta3^2], [theta4^2, 0, theta2^2], [theta3^2, theta2^2, 0]]: relative residual {closed_err:.1e}")
# the sum rule, symbolically: for Y zero-diagonal complex symmetric, s1 = s2 + s3  <=>  e1^2 = 4 e2 for the eigenvalues of Y Y^dagger
a, b, c, a_, b_, c_ = sp.symbols('a b c abar bbar cbar')
Ysym = sp.Matrix([[0, c, b], [c, 0, a], [b, a, 0]]); Ydag = sp.Matrix([[0, c_, b_], [c_, 0, a_], [b_, a_, 0]])
H = Ysym*Ydag
e1 = sp.expand(H.trace()); e2 = sp.expand((H.trace()**2 - (H*H).trace())/2)
sum_rule_residual = sp.expand(e1**2 - 4*e2)
log(f"   the sum rule s1 = s2 + s3 (B1636): e1^2 - 4 e2 for the eigenvalues of Y Y^dagger, symbolically = {sum_rule_residual}  (0 means the identity holds for every complex a, b, c)")
rng = np.random.default_rng(1); worst_sum = 0.0; worst_floor = 1.0
for _ in range(200000):
    aa, bb, cc = rng.normal(size=3) + 1j*rng.normal(size=3)
    s = svd(np.array([[0, cc, bb], [cc, 0, aa], [bb, aa, 0]]), compute_uv=False)
    worst_sum = max(worst_sum, abs(s[0] - s[1] - s[2])/s[0]); worst_floor = min(worst_floor, s[1]/s[0])
log(f"   200000 random complex zero-diagonal symmetric matrices: max |s1 - s2 - s3|/s1 = {worst_sum:.1e}, min s2/s1 = {worst_floor:.6f}")
# the floor over the fundamental domain, and the spectra at i and omega
grid = []
for x in np.linspace(-0.5, 0.5, 81):
    for y in np.linspace(0.86, 6.0, 160):
        if x*x + y*y < 1 - 1e-12: continue
        s = svd(Y1(x + 1j*y), compute_uv=False); grid.append((x, y, s[1]/s[0], s[2]/s[0]))
grid = np.array(grid); imin = np.argmin(grid[:, 2])
s_om = svd(Y1(np.exp(2j*np.pi/3)), compute_uv=False); s_i = svd(Y1(1j), compute_uv=False)
phi = (1 + 5**0.5)/2
log(f"   floor on the fundamental domain (|Im| <= 6): min m2/m1 = {grid[imin, 2]:.6f} at tau = {grid[imin, 0]:.3f} + {grid[imin, 1]:.3f}i; max m2/m1 = {grid[:, 2].max():.6f}")
log(f"   at omega: (m2, m3)/m1 = ({s_om[1]/s_om[0]:.9f}, {s_om[2]/s_om[0]:.9f}); at i: ({s_i[1]/s_i[0]:.9f}, {s_i[2]/s_i[0]:.9f}) vs (1/phi, 1/phi^2) = ({1/phi:.9f}, {1/phi**2:.9f})")
# the parameter-free Dirac form at weight 0 is the identity
null0, monos0 = TbT[0]; Y0f = eval_form(null0[:, 0].reshape(9, len(monos0)), monos0, tau0, 0)
id_err = float(np.abs(Y0f/Y0f[0, 0] - I3).max())
log(f"   dim M_0(rhobar x rho) = {table_TbT[0]['total']}, the form is the identity (residual {id_err:.1e}); dim M_1(rhobar x rhobar) = {table_TT[1]['total']}: one form per parameter-free sector, so M_u is proportional to M_d and V_CKM = 1")
# the Zee reading: theta13 on Re tau = 1/2
def takagi_angles(Mx):
    W, s, Vh = svd(Mx); Dm = W.T @ Mx @ W; U = W @ np.diag(np.exp(-1j*np.angle(np.diag(Dm))/2))
    P = U[:, [1, 0, 2]]; s13 = abs(P[0, 2]); c13 = math.sqrt(1 - s13**2)
    return math.degrees(math.asin(min(1, s13))), math.degrees(math.asin(min(1, abs(P[0, 1])/c13))), math.degrees(math.asin(min(1, abs(P[1, 2])/c13)))
zee = {f"{x}+{y}i": takagi_angles(Y1(x + 1j*y)) for x, y in ((0.5, 2.5), (0.5, 3.5), (0.25, 3.5), (0.0, 3.0))}
log("   as a Majorana texture (charged leptons diagonal): (theta13, theta12, theta23) in degrees: " + "; ".join(f"{k}: ({v[0]:.2e}, {v[1]:.1f}, {v[2]:.1f})" for k, v in zee.items()))

# ---------------------------------------------------------------- N10: the determinants and the phase law
taus = [0.13 + 1.21j, -0.31 + 0.95j, 0.45 + 2.0j, 0.07 + 3.1j, -0.22 + 1.6j]
r1 = [np.linalg.det(Y1(t))/eta(t)**6 for t in taus]
spread1 = float(np.abs(np.array(r1)/r1[0] - 1).max())
nullc3, monos3 = TT[3]
cs = Psym_off @ nullc3[:, 0].reshape(9, len(monos3)); ca = Pasym @ nullc3[:, 0].reshape(9, len(monos3))
if np.abs(ca).max() < 1e-9: ca = Pasym @ nullc3[:, 1].reshape(9, len(monos3))
if np.abs(cs).max() < 1e-9: cs = Psym_off @ nullc3[:, 1].reshape(9, len(monos3))
cs /= np.abs(cs).max(); ca /= np.abs(ca).max()
def Y3(tau, r): return eval_form(cs, monos3, tau, 18) + r*eval_form(ca, monos3, tau, 18)
spread3 = max(float(np.abs(np.array([np.linalg.det(Y3(t, r))/(eta(t)**6*E6(t)) for t in taus])/ (np.linalg.det(Y3(taus[0], r))/(eta(taus[0])**6*E6(taus[0]))) - 1).max()) for r in (0.7 + 0.2j, -1.3j, 2.0))
null2, monos2 = TbT[2]; cA = null2[:, 0].reshape(9, len(monos2)); cB = null2[:, 1].reshape(9, len(monos2))
def Y2(tau, r): return eval_form(cA, monos2, tau, 0) + r*eval_form(cB, monos2, tau, 0)
spread2 = max(float(np.abs(np.array([np.linalg.det(Y2(t, r))/E6(t) for t in taus])/(np.linalg.det(Y2(taus[0], r))/E6(taus[0])) - 1).max()) for r in (0.3j, 1.1 - 0.4j, -2.0))
log(f"\nN10: det Y_1 / eta^6 constant over five tau (relative spread {spread1:.1e}); det(Y_s + r Y_a) / (eta^6 E_6) constant (spread {spread3:.1e}, three r); weight-2 Dirac: det(A + r B) / E_6 constant (spread {spread2:.1e})")
phase_dev = 0.0
for x in np.linspace(-0.5, 0.5, 21):
    for y in (2.5, 3.0, 4.0):
        d = (12*np.angle(eta(x + 1j*y)) - np.pi*x + np.pi) % (2*np.pi) - np.pi
        phase_dev = max(phase_dev, abs(d))
dE6 = max(abs(np.angle(E6(x + 1j*y))) for x in np.linspace(-0.5, 0.5, 21) for y in (4.5, 5.0))
log(f"   the phase law: max |12 arg eta(x + iy) - pi x| over x in [-1/2, 1/2], y in {{2.5, 3, 4}} = {phase_dev:.2e};  max |arg E_6| at y >= 4.5: {dE6:.2e}")

# ---------------------------------------------------------------- N10c: the lowest fittable models against the quark data
mu, md, ms, mc, mb, mt = 1.23e-3, 2.67e-3, 53.16e-3, 0.620, 2.839, 168.26          # Huang-Zhou 2021 at M_Z (as in the referee's draft)
data = dict(mu_mt=mu/mt, mc_mt=mc/mt, md_mb=md/mb, ms_mb=ms/mb, Vus=0.22501, Vcb=0.04183, Vub=0.003732, J=3.12e-5)
err = dict(mu_mt=0.17, mc_mt=0.03, md_mb=0.07, ms_mb=0.09, Vus=0.01, Vcb=0.03, Vub=0.06, J=0.06)
def observables(Mu, Md):
    Uu, su, _ = svd(Mu); Ud, sd, _ = svd(Md); Uu, su, Ud, sd = Uu[:, ::-1], su[::-1], Ud[:, ::-1], sd[::-1]
    V = Uu.conj().T @ Ud; J = np.imag(V[0, 1]*V[1, 2]*np.conj(V[0, 2])*np.conj(V[1, 1]))
    return dict(mu_mt=su[0]/su[2], mc_mt=su[1]/su[2], md_mb=sd[0]/sd[2], ms_mb=sd[1]/sd[2], Vus=abs(V[0, 1]), Vcb=abs(V[1, 2]), Vub=abs(V[0, 2]), J=J)
def chi2_of(o):
    s = 0.0
    for k in data:
        if k == 'J': s += ((o[k] - data[k])/(err[k]*abs(data[k])))**2
        else:
            if not o[k] > 0: return 1e6
            s += (math.log(o[k]/data[k])/err[k])**2
    return s
def make_chi2(model, ymin):
    def chi2(p):
        x, y, a1, b1, a2, b2 = p
        if y < ymin or abs(x) > 0.5 or x*x + y*y < 1.0: return 1e6
        try:
            if model == 'TT': o = observables(Y3(x + 1j*y, a1 + 1j*b1), Y3(x + 1j*y, a2 + 1j*b2))
            else: o = observables(Y2(x + 1j*y, a1 + 1j*b1), Y2(x + 1j*y, a2 + 1j*b2))
        except Exception: return 1e6
        return chi2_of(o)
    return chi2
fits = {}
for label, model, ymin in (("TT_weight3", 'TT', 0.87), ("TbT_weight2", 'TbT', 0.87), ("TbT_weight2_Im_tau_ge_4.5", 'TbT', 4.5)):
    f = make_chi2(model, ymin); rng = np.random.default_rng(5); best = (1e9, None); t1 = time.time()
    for sidx in range(100):
        x = rng.uniform(-0.5, 0.5); y = rng.uniform(max(ymin, 1.0), max(ymin, 1.0) + 3.0)
        p0 = [x, y] + [rng.normal()*10**rng.uniform(-2, 1.5) for _ in range(4)]
        res = minimize(f, p0, method='Nelder-Mead', options=dict(maxiter=3000, xatol=1e-8, fatol=1e-10))
        if res.fun < best[0]: best = (float(res.fun), [float(v) for v in res.x])
    fits[label] = dict(chi2_min=best[0], params=best[1], starts=100, seconds=time.time() - t1)
    log(f"   fit {label}: chi2_min = {best[0]:.1f} at tau = {best[1][0]:.3f} + {best[1][1]:.3f}i  [{time.time() - t1:.0f}s]")

# ---------------------------------------------------------------- cells
cells = {}
cells['C0'] = dict(holds=plumb['order'] == 96 and plumb['braid'] and plumb['s4_is_minus_one'] and plumb['exponents'] == [0.125, 0.375, 0.875] and table_ok
                   and abs(s_i[1]/s_i[0] - 1/phi) < 1e-9 and abs(s_i[2]/s_i[0] - 1/phi**2) < 1e-9, predicted="order 96, braid, s^4 = -1, exponents 1/8 3/8 7/8; B1635's table by piece; B1636's golden spectrum at i")
cells['N8a'] = dict(holds=sum_rule_residual == 0 and worst_sum < 1e-12 and worst_floor >= 0.5 - 1e-9 and grid[imin, 2] >= 0.5 - 1e-9 and abs(s_om[1]/s_om[0] - 0.5) < 1e-9 and abs(s_om[2]/s_om[0] - 0.5) < 1e-9 and closed_err < 1e-10,
                    value=dict(sum_rule_symbolic=str(sum_rule_residual), random_floor=worst_floor, grid_floor=float(grid[imin, 2]), omega=[float(s_om[1]/s_om[0]), float(s_om[2]/s_om[0])], closed_form_residual=closed_err),
                    predicted="e1^2 - 4e2 = 0 symbolically; s2/s1 >= 1/2 on 200000 random matrices and on the grid; (1/2, 1/2) at omega; the closed form to 1e-10")
cells['N8b'] = dict(holds=table_TT[1]['total'] == 1 and table_TbT[0]['total'] == 1 and id_err < 1e-10, value=dict(dim_M1_TT=table_TT[1]['total'], dim_M0_TbT=table_TbT[0]['total'], identity_residual=id_err), predicted="one form at weight 1 (T x T) and one at weight 0 (Tbar x T), the latter the identity")
cells['N10a'] = dict(holds=spread1 < 1e-7 and spread3 < 1e-7 and spread2 < 1e-7, value=dict(weight1=spread1, weight3=spread3, Dirac_weight2=spread2), predicted="det Y_1/eta^6, det Y_3/(eta^6 E_6) and det Y_2^Dirac/E_6 constant in tau to 1e-7")
cells['N10b'] = dict(holds=phase_dev < 1e-4 and dE6 < 1e-9, value=dict(phase_dev=phase_dev, argE6_max=dE6), predicted="|12 arg eta - pi x| < 1e-4 for Im tau >= 2.5; |arg E_6| < 1e-9 for Im tau >= 4.5")
cells['N10c'] = dict(holds=all(v['chi2_min'] > 500 for v in fits.values()), value={k: v['chi2_min'] for k, v in fits.items()}, predicted="chi^2_min > 500 for each of the three lowest fittable models (100 starts each)")
all_hold = all(c['holds'] for c in cells.values())
log("\nCELLS")
for k, c in cells.items(): log(f"   {k}: {'HOLDS' if c['holds'] else 'FAILS'}  {json.dumps(c.get('value'), default=float)[:220]}")
log(f"all_hold {all_hold}  [{time.time() - T0:.0f}s]")
json.dump(dict(plumbing=plumb, table_TT=table_TT, table_TbT=table_TbT, B1635_reproduced=table_ok, N8=dict(closed_form_residual=closed_err, sum_rule_symbolic=str(sum_rule_residual), random=dict(max_sum_rule_dev=worst_sum, min_floor=worst_floor), grid_floor=dict(value=float(grid[imin, 2]), tau=[float(grid[imin, 0]), float(grid[imin, 1])], max=float(grid[:, 2].max())), omega=[float(s_om[1]/s_om[0]), float(s_om[2]/s_om[0])], i=[float(s_i[1]/s_i[0]), float(s_i[2]/s_i[0])], zee_angles=zee, identity_residual=id_err),
               N10=dict(spread_weight1=spread1, spread_weight3=spread3, spread_Dirac2=spread2, phase_dev=phase_dev, argE6_max=dE6), fits=fits, cells=cells, all_hold=all_hold, seconds=time.time() - T0),
          open(os.path.join(HERE, "the_dedekind_phase.json"), "w"), indent=1, default=lambda o: float(o) if isinstance(o, (np.floating, np.integer)) else str(o))
LOG.close()
