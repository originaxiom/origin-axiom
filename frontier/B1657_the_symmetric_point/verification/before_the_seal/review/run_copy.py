#!/usr/bin/env python3
"""B1656 -- THE SYMMETRIC POINT IS RANK ONE: at tau = omega the order-3 move acts on the channel triplet as a real signed
permutation P with eigenlines R, Rbar (isotropic) and n (real); a Higgs on n gives (1, 1, 0), on R or Rbar (1, 0, 0).
Near the isotropic vacuum the two light masses over the heavy are the two isotropy defects -- the Higgs's |a.a|/|a|^2 and
the zero-mode triplet's |v.v|/|v|^2 -- at first order with coefficient one; under B1654's canonical end condition
v.v = D(tau), so in the isotropic vacuum one generation is exactly massless and L s2/s1 -> |D|/(2 pi |R|^2); near omega
D(omega + delta) = kappa delta-bar |R|^2 + O(delta^2), |kappa| the same in every direction.

Y(a; v) = a v^T + v a^T - (a.v) 1 (B1645, B1654). R = (-th2^2, i th3^2, -th4^2)/th1'(0), channels (2, 3, 4) (B1654).
Cells S0 (plumbing), S1-S5; see the preregistration. Writes the_symmetric_point.json beside itself; prints a summary."""
import json, math, os, sys, time
import numpy as np
import mpmath as mp
import sympy as sp
from numpy.polynomial.legendre import leggauss

T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "the_symmetric_point.json")
ROOT = os.environ.get("OA_ROOT") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
B1654 = os.path.join(ROOT, "frontier", "B1654_the_norm_of_the_boundary_class", "verification", "the_norm_of_the_boundary_class.json")
W = np.exp(2j*np.pi/3)
TAUS = {"omega": complex(W), "i": 1j, "t1": 0.13+1.07j, "t2": 0.3+1.6j, "t3": 2.2j, "tstar": complex(0.5, math.sqrt(5)/2)}
RES = {}


# ---------------------------------------------------------------- theta functions (numpy series) and the triplet
def th(z, tau, K=30):
    q = np.exp(1j*np.pi*tau); n = np.arange(K); m = np.arange(1, K); z = np.asarray(z, dtype=complex)[..., None]
    t1 = 2*np.sum((-1)**n*q**((n+.5)**2)*np.sin((2*n+1)*np.pi*z), -1)
    t2 = 2*np.sum(q**((n+.5)**2)*np.cos((2*n+1)*np.pi*z), -1)
    t3 = 1 + 2*np.sum(q**(m**2)*np.cos(2*m*np.pi*z), -1)
    t4 = 1 + 2*np.sum((-1)**m*q**(m**2)*np.cos(2*m*np.pi*z), -1)
    return t1, t2, t3, t4


def tp(tau, K=30):
    q = np.exp(1j*np.pi*tau); n = np.arange(K)
    return 2*np.pi*np.sum((-1)**n*(2*n+1)*q**((n+.5)**2))


def T2(tau):
    _, t2, t3, t4 = th(np.array(0.0), tau); return np.array([t2**2, t3**2, t4**2])


def Rvec(tau):
    return np.array([-1, 1j, -1])*T2(tau)/tp(tau)


def Y(a, v):
    return np.outer(a, v) + np.outer(v, a) - (a @ v)*np.eye(3)


def sv(M):
    return np.linalg.svd(M, compute_uv=False)


# ---------------------------------------------------------------- the cutoff-free D (B1654's N2b route, polar)
def S_kernel(r, z, tau):
    t = th(z, tau); t0 = th(np.array(0.0), tau)
    return t[r-1]*tp(tau)/(t0[r-1]*t[0])


def D_over_R2(tau, nth=48, nr=48):
    R = dict(zip((2, 3, 4), Rvec(tau)))
    v = [0.5+0.5*tau, -0.5+0.5*tau, -0.5-0.5*tau, 0.5-0.5*tau]
    br = sorted(float(np.mod(np.angle(x), 2*np.pi)) for x in v); br += [br[0] + 2*np.pi]
    xg, wg = leggauss(nth); xr, wr = leggauss(nr); tot = 0j
    for a0, b0 in zip(br[:-1], br[1:]):
        thg = 0.5*(b0-a0)*xg + 0.5*(b0+a0); wt = 0.5*(b0-a0)*wg
        d = np.exp(1j*thg); y1 = d.imag/tau.imag; x1 = d.real - y1*tau.real; rm = 0.5/np.maximum(abs(x1), abs(y1))
        rr = 0.5*rm[:, None]*(xr[None, :] + 1); w2 = 0.5*rm[:, None]*wr[None, :]
        z = rr*d[:, None]
        f = sum(R[r]**2*np.abs(S_kernel(r, z, tau))**2 for r in (2, 3, 4))
        tot += np.sum(wt[:, None]*w2*f*rr)
    return tot/sum(abs(x)**2 for x in R.values())


# ================================================================ S0 plumbing (void below threshold)
s0 = {}
mp.mp.dps = 30
dev = 0.0
for k, t in TAUS.items():
    q = mp.exp(1j*mp.pi*mp.mpc(t.real, t.imag))
    ref = [complex(mp.jtheta(j, 0, q)) for j in (2, 3, 4)]
    _, t2, t3, t4 = th(np.array(0.0), t)
    dev = max(dev, max(abs(a-b)/abs(b) for a, b in zip((t2, t3, t4), ref)))
s0["theta_vs_jtheta_max_rel"] = dev
s0["RR_over_R2_max"] = max(abs(Rvec(t) @ Rvec(t))/np.linalg.norm(Rvec(t))**2 for t in TAUS.values())
c = json.load(open(B1654))["N2"]["pairs"]
s0["b1654_c_omega_spread"] = float(np.ptp([c["omega,%d" % r]["A"] for r in (2, 3, 4)]))
s0["void"] = bool(dev > 1e-12 or s0["RR_over_R2_max"] > 1e-13 or s0["b1654_c_omega_spread"] > 1e-9)
RES["S0"] = s0

# ================================================================ S1 the order-3 move at omega
s1 = {}
fit_taus = [0.13+1.07j, -0.21+0.93j, 0.33+1.4j, 0.05+0.8j]
A = np.array([T2(t) for t in fit_taus]); B = np.array([T2(-1/(t+1))/(t+1) for t in fit_taus])
M = np.linalg.lstsq(A, B, rcond=None)[0].T
s1["fit_residual"] = float(max(np.abs(B[i] - M @ A[i]).max() for i in range(4)))
Dg = np.diag([-1, 1j, -1]); MR = Dg @ M @ np.linalg.inv(Dg)
P = np.array([[0, 1, 0], [0, 0, -1], [1, 0, 0]], dtype=float)
s1["MR_minus_P"] = float(np.abs(MR - P).max())
s1["PtP_minus_1"] = float(np.abs(P.T @ P - np.eye(3)).max()); s1["P3_plus_1"] = float(np.abs(np.linalg.matrix_power(P, 3) + np.eye(3)).max())
Rw = Rvec(TAUS["omega"]); n = np.array([1., -1., -1.])/math.sqrt(3)
lam_R = (P @ Rw) @ Rw.conj()/np.linalg.norm(Rw)**2
s1["eig_R"] = [float(np.abs(P @ Rw - lam_R*Rw).max()/np.linalg.norm(Rw)), float(np.angle(lam_R)/np.pi)]
s1["eig_Rbar"] = [float(np.abs(P @ Rw.conj() - np.conj(lam_R)*Rw.conj()).max()/np.linalg.norm(Rw))]
s1["eig_n"] = float(np.abs(P @ n + n).max())
s1["isotropy"] = {"R": float(abs(Rw @ Rw)/np.linalg.norm(Rw)**2), "n.n": float(n @ n)}
rng = np.random.default_rng(1656)
cov = 0.0
for _ in range(20):
    a = rng.normal(size=3)+1j*rng.normal(size=3); v = rng.normal(size=3)+1j*rng.normal(size=3)
    cov = max(cov, np.abs(Y(P @ a, P @ v) - P @ Y(a, v) @ P.T).max())
s1["covariance"] = float(cov)
Rg = Rvec(0.13+1.07j)                                                     # control: not an eigenvector off omega
lam_g = (P @ Rg) @ Rg.conj()/np.linalg.norm(Rg)**2
s1["control_generic_tau_residual"] = float(np.abs(P @ Rg - lam_g*Rg).max()/np.linalg.norm(Rg))
s1["holds"] = bool(s1["fit_residual"] < 1e-12 and s1["MR_minus_P"] < 1e-12 and s1["PtP_minus_1"] == 0 and s1["P3_plus_1"] == 0
                   and s1["eig_R"][0] < 1e-12 and abs(s1["eig_R"][1] + 1/3) < 1e-12 and s1["eig_Rbar"][0] < 1e-12
                   and s1["eig_n"] < 1e-15 and s1["isotropy"]["R"] < 1e-13 and cov < 1e-12
                   and s1["control_generic_tau_residual"] > 0.05)
RES["S1"] = s1

# ================================================================ S2 the symmetric vacua at omega
s2 = {}
Rn = Rw/np.linalg.norm(Rw)
spec = {}
for name, a in (("n", n), ("R", Rn), ("Rbar", Rn.conj())):
    s = sv(Y(a, Rw)); spec[name] = [float(x) for x in s/s[0]]
cw = [c["omega,%d" % r]["A"] for r in (2, 3, 4)]
p4 = {}
for L in (10.0, 100.0):
    u = np.sqrt(2*np.pi*L + np.array(cw))*Rw
    for name, a in (("n", n), ("Rbar", Rn.conj())):
        s = sv(Y(a, u)); p4["%s,L=%g" % (name, L)] = [float(x) for x in s/s[0]]
rng = np.random.default_rng(2)
ctrl = []
for _ in range(50):
    a = rng.normal(size=3); s = sv(Y(a, Rw)); ctrl.append(s[1]/s[0])
s2.update(spectra=spec, P4=p4, control_real_m=[float(min(ctrl)), float(max(ctrl))])
s2["holds"] = bool(abs(spec["n"][1] - 1) < 1e-12 and spec["n"][2] < 1e-12
                   and max(spec["R"][1:] + spec["Rbar"][1:]) < 1e-12
                   and all(abs(v[1] - 1) < 1e-9 and v[2] < 1e-9 for k, v in p4.items() if k.startswith("n"))
                   and all(max(v[1:]) < 1e-9 for k, v in p4.items() if k.startswith("Rbar"))
                   and min(ctrl) > 0.5 - 1e-9)
RES["S2"] = s2

# ================================================================ S3 the two-defect law
s3 = {}
a_, v_ = sp.symbols("a1:4"), sp.symbols("v1:4")
av, vv = sp.Matrix(a_), sp.Matrix(v_)
Ys = av*vv.T + vv*av.T - (av.dot(vv))*sp.eye(3)
s3["symbolic_det_minus_formula"] = str(sp.expand(Ys.det() - av.dot(vv)*av.dot(av)*vv.dot(vv)))   # det Y = +(a.v)(a.a)(v.v)
s3["symbolic_symmetric_in_a_v"] = bool(sp.simplify(Ys - (vv*av.T + av*vv.T - (vv.dot(av))*sp.eye(3))) == sp.zeros(3, 3))
worst = {}; ctrl_unnorm = 0.0
for seed in (11, 12):
    rng = np.random.default_rng(seed)
    for k in ("omega", "i", "t1", "tstar"):
        R = Rvec(TAUS[k]); R = R/np.linalg.norm(R); wk = 0.0
        for _ in range(200):
            ea, ev = 10**rng.uniform(-6, -2), 10**rng.uniform(-6, -2)
            al = rng.normal(size=3)+1j*rng.normal(size=3); be = rng.normal(size=3)+1j*rng.normal(size=3)
            a = 2.0*(R.conj() + ea*al/np.linalg.norm(al)); v = 3.0*(R + ev*be/np.linalg.norm(be))
            s = sv(Y(a, v)); got = s[1:]/s[0]
            da = abs(a @ a)/np.linalg.norm(a)**2; dv = abs(v @ v)/np.linalg.norm(v)**2
            wk = max(wk, float(np.abs(got/np.sort([da, dv])[::-1] - 1).max()/max(ea, ev)))
            un = np.sort([abs(a @ a), abs(v @ v)])[::-1]                    # control: unnormalised defects
            ctrl_unnorm = max(ctrl_unnorm, float(np.abs(got/un - 1).min()))
        worst["%s,seed%d" % (k, seed)] = wk
s3["first_order_worst"] = worst
s3["control_unnormalised_min_deviation"] = ctrl_unnorm
rng = np.random.default_rng(3); dets = 0.0
for _ in range(100):
    a = rng.normal(size=3)+1j*rng.normal(size=3); v = rng.normal(size=3)+1j*rng.normal(size=3)
    dets = max(dets, abs(abs(np.linalg.det(Y(a, v))) - abs(a @ v)*abs(a @ a)*abs(v @ v))/(abs(a @ v)*abs(a @ a)*abs(v @ v)))
s3["numeric_det_rel"] = float(dets)
s3["holds"] = bool(s3["symbolic_det_minus_formula"] == "0" and s3["symbolic_symmetric_in_a_v"] and dets < 1e-12
                   and max(worst.values()) < 0.05 and ctrl_unnorm > 0.5)
RES["S3"] = s3

# ================================================================ S4 the canonical end condition, isotropic vacuum a ~ Rbar(tau)
s4 = {}
D54 = json.load(open(B1654))["N5"]["D_over_R2"]
rows = {}
for k in ("omega", "i", "t1", "t2", "t3"):
    t = TAUS[k]; R = Rvec(t); cr = np.array([c["%s,%d" % (k, r)]["A"] for r in (2, 3, 4)])
    a = R.conj()/np.linalg.norm(R); Dk = complex(*D54[k]); lim = abs(Dk)/(2*np.pi)
    row = {}
    for L in (40.0, 160.0, 640.0, 2560.0):
        u = np.sqrt(2*np.pi*L + cr)*R; s = sv(Y(a, u))
        row["%g" % L] = [float(s[2]/s[0]), float(L*s[1]/s[0])]
    rows[k] = {"rows": row, "limit_abs_D_over_2pi": lim}
s4["rows"] = rows
s4["massless_max"] = max(r["rows"][L][0] for r in rows.values() for L in r["rows"])
s4["rel_err_at_2560"] = {k: (abs(r["rows"]["2560"][1]/r["limit_abs_D_over_2pi"] - 1) if r["limit_abs_D_over_2pi"] > 1e-9 else None)
                         for k, r in rows.items()}
s4["omega_L_s2_max"] = max(r[1] for r in rows["omega"]["rows"].values())
s4["holds"] = bool(s4["massless_max"] < 1e-12 and s4["omega_L_s2_max"] < 1e-8
                   and all(v < 0.01 for k, v in s4["rel_err_at_2560"].items() if v is not None))
RES["S4"] = s4

# ================================================================ S5 D near omega: linear and antiholomorphic
s5 = {}
grid = {}
for d in (1e-3, 2.5e-4):
    for j in range(6):
        phi = j*np.pi/3 + np.pi/7
        Dv = D_over_R2(complex(W + d*np.exp(1j*phi)))
        grid["%g,%d" % (d, j)] = [float(abs(Dv)/d), float(np.angle(Dv*np.exp(1j*phi))/np.pi)]
mods = {d: [grid["%g,%d" % (d, j)][0] for j in range(6)] for d in (1e-3, 2.5e-4)}
args = {d: [grid["%g,%d" % (d, j)][1] for j in range(6)] for d in (1e-3, 2.5e-4)}
s5["grid"] = grid
s5["kappa_abs_spread"] = {"%g" % d: float(np.ptp(m)/np.mean(m)) for d, m in mods.items()}
s5["kappa_arg_over_pi_spread"] = {"%g" % d: float(np.ptp(np.unwrap(np.array(a)*np.pi))/np.pi) for d, a in args.items()}
s5["kappa_abs_at_2.5e-4"] = float(np.mean(mods[2.5e-4])); s5["kappa_arg_over_pi"] = float(np.mean(args[2.5e-4]))
mp.mp.dps = 30
s5["w87_slope"] = float(mp.pi**2*mp.sqrt(3)/6*abs(mp.jtheta(3, 0, mp.exp(1j*mp.pi*mp.mpc(W.real, W.imag))))**4)
s5["kappa_vs_w87_rel"] = float(abs(s5["kappa_abs_at_2.5e-4"]/s5["w87_slope"] - 1))
s5["holds"] = bool(s5["kappa_abs_spread"]["0.00025"] < s5["kappa_abs_spread"]["0.001"] and s5["kappa_abs_spread"]["0.00025"] < 2e-3
                   and s5["kappa_arg_over_pi_spread"]["0.00025"] < 2e-3 and abs(s5["kappa_arg_over_pi"] - 0.25) < 2e-3
                   and s5["kappa_vs_w87_rel"] < 1e-3)
RES["S5"] = s5

RES["seconds"] = round(time.time() - T0, 1)
json.dump(RES, open(OUT, "w"), indent=1)
for k in ("S0", "S1", "S2", "S3", "S4", "S5"):
    print(k, "void" if k == "S0" and RES[k]["void"] else ("HOLDS" if RES[k].get("holds", not RES[k].get("void")) else "FAILS"))
print("seconds", RES["seconds"])
