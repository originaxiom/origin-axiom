#!/usr/bin/env python3
"""B1657 -- THE SYMMETRIC POINT: TWO ISOTROPIC VACUA, TWO LAWS. At tau = omega the order-3 move acts on the channel
triplet as a real signed permutation P whose eigenlines are R, Rbar (isotropic) and n (real). A Higgs on n gives
(1, 1, 0); on R or Rbar, rank one (B1645's cone). Near the CONJUGATE vacuum (a ~ Rbar, v ~ R) the two light masses over
the heavy are the two isotropy defects |d_a|, |d_v| (d_a = a.a/|a|^2, d_v = v.v/|v|^2); near the PARALLEL vacuum
(a ~ R, v ~ R) they are |d_a + d_v|/4 and |d_a d_v|/4, a geometric hierarchy. Under B1654's canonical end condition
(v.v = D), with the Higgs exactly on the line, one generation is exactly massless and L s2/s1 -> |D|/(2 pi |R|^2)
(conjugate) or |D|/(8 pi |R|^2) (parallel). D's covariance D(gamma tau)(tau + 1) = -D(tau) forces D(omega) = 0 and a
cone there, |D| = W87's slope |tau - omega| |R|^2.

Y(a; v) = a v^T + v a^T - (a.v) 1 (B1645, B1654). R = (-th2^2, i th3^2, -th4^2)/th1'(0), channels (2, 3, 4) (B1654).
Cells S0 (plumbing), S1-S5; see the preregistration. Writes the_symmetric_point.json beside itself after every cell."""
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


def save():
    RES["seconds"] = round(time.time() - T0, 1)
    json.dump(RES, open(OUT, "w"), indent=1)


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


# ---------------------------------------------------------------- the cutoff-free D (B1654's N2b route, polar), and W87's closed form
def S_kernel(r, z, tau):
    t = th(z, tau); t0 = th(np.array(0.0), tau)
    return t[r-1]*tp(tau)/(t0[r-1]*t[0])


def D_raw(tau, nth=48, nr=48):
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
    return tot


def R2(tau):
    return float(sum(abs(x)**2 for x in Rvec(tau)))


def D_over_R2(tau):
    return D_raw(tau)/R2(tau)


def D_w87_over_R2(tau):                                                    # the SM seat's W87 closed form, 30 digits
    mp.mp.dps = 30; t = mp.mpc(tau.real, tau.imag); q = mp.exp(1j*mp.pi*t)
    t2, t3, t4 = (mp.jtheta(j, 0, q) for j in (2, 3, 4)); eta = mp.exp(1j*mp.pi*t/12)*mp.qp(mp.exp(2j*mp.pi*t))
    lam = t2**4/t3**4; h = lam*mp.log(abs(lam)) + (1-lam)*mp.log(abs(1-lam))
    D = -t3**4*h/(4*mp.pi*eta**6); Rn = (abs(t2)**4 + abs(t3)**4 + abs(t4)**4)/abs(2*mp.pi*eta**3)**2
    return complex(D/Rn)


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
D54 = json.load(open(B1654))["N5"]["D_over_R2"]
s0["w87_vs_b1654_D_max"] = max(abs(D_w87_over_R2(TAUS[k]) - complex(*D54[k])) for k in ("i", "t1", "t2", "t3"))
s0["void"] = bool(dev > 1e-12 or s0["RR_over_R2_max"] > 1e-13 or s0["b1654_c_omega_spread"] > 1e-9 or s0["w87_vs_b1654_D_max"] > 1e-10)
RES["S0"] = s0; save()

# ================================================================ S1 the order-3 move at omega
s1 = {}
fit_taus = [0.13+1.07j, -0.21+0.93j, 0.33+1.4j, 0.05+0.8j]
A = np.array([T2(t) for t in fit_taus]); B = np.array([T2(-1/(t+1))/(t+1) for t in fit_taus])
M = np.linalg.lstsq(A, B, rcond=None)[0].T
s1["fit_residual"] = float(max(np.abs(B[i] - M @ A[i]).max() for i in range(4)))
Dg = np.diag([-1, 1j, -1]); MR = Dg @ M @ np.linalg.inv(Dg)
P = np.array([[0, 1, 0], [0, 0, -1], [1, 0, 0]], dtype=float)
s1["MR_minus_P"] = float(np.abs(MR - P).max())
s1["PtP_is_1"] = bool(np.array_equal(P.T @ P, np.eye(3))); s1["P3_is_minus_1"] = bool(np.array_equal(np.linalg.matrix_power(P, 3), -np.eye(3)))
Rw = Rvec(TAUS["omega"]); n = np.array([1., -1., -1.])/math.sqrt(3)
lam_R = (P @ Rw) @ Rw.conj()/np.linalg.norm(Rw)**2
s1["eig_R"] = [float(np.abs(P @ Rw - lam_R*Rw).max()/np.linalg.norm(Rw)), float(np.angle(lam_R)/np.pi)]
s1["eig_Rbar"] = float(np.abs(P @ Rw.conj() - np.conj(lam_R)*Rw.conj()).max()/np.linalg.norm(Rw))
s1["eig_n"] = float(np.abs(P @ n + n).max()); s1["n.n"] = float(n @ n)
rng = np.random.default_rng(1657)
cov = 0.0
for _ in range(20):
    a = rng.normal(size=3)+1j*rng.normal(size=3); v = rng.normal(size=3)+1j*rng.normal(size=3)
    cov = max(cov, np.abs(Y(P @ a, P @ v) - P @ Y(a, v) @ P.T).max())
s1["covariance"] = float(cov)
Rg = Rvec(0.13+1.07j); lam_g = (P @ Rg) @ Rg.conj()/np.linalg.norm(Rg)**2
s1["control_generic_tau_residual"] = float(np.abs(P @ Rg - lam_g*Rg).max()/np.linalg.norm(Rg))
grad = []
for d in (1e-1, 1e-2, 1e-3, 1e-4):                                        # graded control: off omega R leaves the eigenline linearly
    Rd = Rvec(complex(W + d*np.exp(0.7j))); ld = (P @ Rd) @ Rd.conj()/np.linalg.norm(Rd)**2
    grad.append(float(np.abs(P @ Rd - ld*Rd).max()/np.linalg.norm(Rd)))
s1["graded_control"] = grad
s1["graded_ratios"] = [grad[i]/grad[i+1] for i in range(3)]
s1["holds"] = bool(s1["fit_residual"] < 1e-12 and s1["MR_minus_P"] < 1e-12 and s1["PtP_is_1"] and s1["P3_is_minus_1"]
                   and s1["eig_R"][0] < 1e-12 and abs(s1["eig_R"][1] + 1/3) < 1e-12 and s1["eig_Rbar"] < 1e-12
                   and s1["eig_n"] < 1e-15 and abs(s1["n.n"] - 1) < 1e-15 and cov < 1e-12
                   and s1["control_generic_tau_residual"] > 0.05 and all(9 < r < 11 for r in s1["graded_ratios"][1:]))
RES["S1"] = s1; save()

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
    for name, a in (("n", n), ("R", Rn), ("Rbar", Rn.conj())):
        s = sv(Y(a, u)); p4["%s,L=%g" % (name, L)] = [float(x) for x in s/s[0]]
rng = np.random.default_rng(2)
ctrl = []
for _ in range(50):
    a = rng.normal(size=3); s = sv(Y(a, Rw)); ctrl.append(s[1]/s[0])
s2.update(spectra=spec, P4=p4, control_real_m=[float(min(ctrl)), float(max(ctrl))])
s2["holds"] = bool(abs(spec["n"][1] - 1) < 1e-12 and spec["n"][2] < 1e-12
                   and max(spec["R"][1:] + spec["Rbar"][1:]) < 1e-12
                   and all(abs(v[1] - 1) < 1e-9 and v[2] < 1e-9 for k, v in p4.items() if k.startswith("n,"))
                   and all(max(v[1:]) < 1e-9 for k, v in p4.items() if not k.startswith("n,"))
                   and min(ctrl) > 0.5 - 1e-9)
RES["S2"] = s2; save()

# ================================================================ S3 the two laws
s3 = {}
a_, v_ = sp.symbols("a1:4"), sp.symbols("v1:4")
av, vv = sp.Matrix(a_), sp.Matrix(v_)
Ys = av*vv.T + vv*av.T - (av.dot(vv))*sp.eye(3)
s3["symbolic_det_minus_formula"] = str(sp.expand(Ys.det() - av.dot(vv)*av.dot(av)*vv.dot(vv)))   # det Y = +(a.v)(a.a)(v.v)
s3["symbolic_symmetric_in_a_v"] = bool(sp.simplify(Ys - (vv*av.T + av*vv.T - (vv.dot(av))*sp.eye(3))) == sp.zeros(3, 3))
rng = np.random.default_rng(3); dets = 0.0
for _ in range(100):
    a = rng.normal(size=3)+1j*rng.normal(size=3); v = rng.normal(size=3)+1j*rng.normal(size=3)
    dets = max(dets, abs(abs(np.linalg.det(Y(a, v))) - abs(a @ v)*abs(a @ a)*abs(v @ v))/(abs(a @ v)*abs(a @ a)*abs(v @ v)))
s3["numeric_det_rel"] = float(dets)


def law_stats(vac, seeds, lo, hi, n_draw=200):
    """max over draws of |light/law - 1| / max(eps), for both laws, in the given vacuum; plus the normalisation control"""
    out = {"conj_law": 0.0, "par_m2": 0.0, "par_m1": 0.0, "norm_ctrl_min": 1e9}
    for seed in seeds:
        rng = np.random.default_rng(seed)
        for k in ("omega", "i", "t1", "tstar"):
            R = Rvec(TAUS[k]); R = R/np.linalg.norm(R); A0 = R.conj() if vac == "conjugate" else R
            for _ in range(n_draw):
                ea, ev = 10**rng.uniform(lo, hi), 10**rng.uniform(lo, hi)
                al = rng.normal(size=3)+1j*rng.normal(size=3); be = rng.normal(size=3)+1j*rng.normal(size=3)
                a = 2.0*(A0 + ea*al/np.linalg.norm(al)); v = 3.0*(R + ev*be/np.linalg.norm(be))
                s = sv(Y(a, v)); got = s[1:]/s[0]; e = max(ea, ev)
                da = (a @ a)/np.linalg.norm(a)**2; dv = (v @ v)/np.linalg.norm(v)**2
                conj = np.sort([abs(da), abs(dv)])[::-1]
                out["conj_law"] = max(out["conj_law"], float(np.abs(got/conj - 1).max()/e))
                out["par_m2"] = max(out["par_m2"], float(abs(got[0]/(abs(da+dv)/4) - 1)/e))
                out["par_m1"] = max(out["par_m1"], float(abs(got[1]/(abs(da*dv)/4) - 1)/e))
                un = np.sort([abs(a @ a), abs(v @ v)])[::-1]
                out["norm_ctrl_min"] = min(out["norm_ctrl_min"], float(np.abs(got/un - 1).min()))
    return out


s3["conjugate_vacuum"] = law_stats("conjugate", (11, 12), -6, -2)
s3["parallel_vacuum"] = law_stats("parallel", (21, 22), -4, -2)
cv, pv = s3["conjugate_vacuum"], s3["parallel_vacuum"]
s3["holds"] = bool(s3["symbolic_det_minus_formula"] == "0" and s3["symbolic_symmetric_in_a_v"] and dets < 1e-12
                   and cv["conj_law"] < 0.05 and pv["par_m2"] < 100 and pv["par_m1"] < 100
                   and pv["conj_law"] > 100 and cv["par_m2"] > 100
                   and cv["norm_ctrl_min"] > 0.5)
RES["S3"] = s3; save()

# ================================================================ S4 the canonical end condition, the Higgs exactly on an isotropic line
s4 = {}
rows = {}
for k in ("omega", "i", "t1", "t2", "t3"):
    t = TAUS[k]; R = Rvec(t); cr = np.array([c["%s,%d" % (k, r)]["A"] for r in (2, 3, 4)])
    Dk = D_w87_over_R2(t) if k != "omega" else 0.0
    row = {}
    for vac, a, fac in (("conjugate", R.conj()/np.linalg.norm(R), 2*np.pi), ("parallel", R/np.linalg.norm(R), 8*np.pi)):
        rr = {}
        for L in (40.0, 160.0, 640.0, 2560.0):
            u = np.sqrt(2*np.pi*L + cr)*R; s = sv(Y(a, u))
            rr["%g" % L] = [float(s[2]/s[0]), float(L*s[1]/s[0])]
        row[vac] = {"rows": rr, "limit": float(abs(Dk)/fac)}
    rows[k] = row
s4["rows"] = rows
s4["massless_max"] = max(v["rows"][L][0] for r in rows.values() for v in r.values() for L in v["rows"])
s4["rel_err_at_2560"] = {"%s,%s" % (k, vac): abs(r[vac]["rows"]["2560"][1]/r[vac]["limit"] - 1)
                         for k, r in rows.items() if k != "omega" for vac in r}
s4["omega_L_s2_max"] = max(v["rows"][L][1] for v in rows["omega"].values() for L in v["rows"])
others = []                                                               # genuine cone points at t1: a(s) = Rbar + s n_t - (s^2/2) R
R = Rvec(TAUS["t1"]); cr = np.array([c["t1,%d" % r]["A"] for r in (2, 3, 4)]); u = np.sqrt(2*np.pi*2560 + cr)*R
e1 = R.conj()/np.linalg.norm(R); e2 = R/np.linalg.norm(R); nt = np.cross(R, R.conj()); nt = nt/np.sqrt(nt @ nt)
for s_ in (0.3, 0.7, 1.2):
    a = e1 + s_*nt - 0.5*s_**2*e2; s = sv(Y(a, u))
    others.append([float(abs(a @ a)/np.linalg.norm(a)**2), float(2560*s[1]/s[0]), float(s[2]/s[0])])
s4["other_cone_points_t1"] = others
s4["holds"] = bool(s4["massless_max"] < 1e-12 and s4["omega_L_s2_max"] < 1e-8 and max(s4["rel_err_at_2560"].values()) < 1e-3)
RES["S4"] = s4; save()

# ================================================================ S5 D near omega: covariance, the cone, and controls
s5 = {}
cov5 = []
for t in (0.13+1.07j, -0.21+0.93j, 0.33+1.4j):
    cov5.append(float(abs(D_raw(-1/(t+1))*(t+1) + D_raw(t))/abs(D_raw(t))))
s5["covariance_rel"] = cov5
w87 = float(mp.pi**2*mp.sqrt(3)/6*abs(mp.jtheta(3, 0, mp.exp(1j*mp.pi*mp.mpc(W.real, W.imag))))**4)
s5["w87_slope"] = w87
grid = {}
for d in (1e-3, 2.5e-4):
    for j in range(6):
        phi = j*np.pi/3 + np.pi/7
        Dv = D_over_R2(complex(W + d*np.exp(1j*phi)))
        grid["%g,%d" % (d, j)] = [float(abs(Dv)/d), float(np.angle(Dv*np.exp(1j*phi))/np.pi)]
mods = {d: [grid["%g,%d" % (d, j)][0] for j in range(6)] for d in (1e-3, 2.5e-4)}
s5["grid"] = grid
s5["kappa_abs_spread"] = {"%g" % d: float(np.ptp(m)/np.mean(m)) for d, m in mods.items()}
s5["kappa_abs_mean_vs_w87_rel"] = float(abs(np.mean(mods[2.5e-4])/w87 - 1))
s5["kappa_arg_readout_convention_dependent"] = float(np.mean([grid["0.00025,%d" % j][1] for j in range(6)]))
negc = {}
for k in ("i", "t1"):
    t0 = TAUS[k]; D0 = D_over_R2(t0)
    vals = [abs(D_over_R2(complex(t0 + 1e-3*np.exp(1j*(j*np.pi/3 + np.pi/7)))) - D0)/1e-3 for j in range(6)]
    negc[k] = float(np.ptp(vals)/np.mean(vals))
s5["negative_isotropy_control"] = negc
s5["holds"] = bool(max(cov5) < 1e-10 and s5["kappa_abs_spread"]["0.00025"] < s5["kappa_abs_spread"]["0.001"]
                   and s5["kappa_abs_spread"]["0.00025"] < 2e-3 and s5["kappa_abs_mean_vs_w87_rel"] < 1e-5
                   and min(negc.values()) > 0.1)
RES["S5"] = s5; save()

for k in ("S0", "S1", "S2", "S3", "S4", "S5"):
    print(k, "void" if k == "S0" and RES[k]["void"] else ("HOLDS" if RES[k].get("holds", not RES[k].get("void")) else "FAILS"))
print("seconds", RES["seconds"])
