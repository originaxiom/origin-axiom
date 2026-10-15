"""B1654 -- THE NORM OF THE BOUNDARY CLASS (sealed instrument; one run).

The parity Higgs's only massless mode is the boundary class at the puncture (the SM seat's C0, point 3). In channel r
(an even spin structure, r = 2, 3, 4) its bulk profile is the conjugate Szego kernel, S_r(z) = th_r(z) th_1'(0) /
(th_r(0) th_1(z)) ~ 1/z. Cut at a common end radius eps, its norm is ||S_r||^2 = 2 pi log(1/eps) + c_r(tau) + o(1).
Under the canonical end condition (equal canonically normalised amplitudes) the residue triplet becomes
u_r = sqrt(2 pi L + c_r) R_r, L = log(1/eps), and u.u = 2 pi L (R.R) + D = D, D(tau) = sum_r c_r R_r^2, since R.R = 0.

Route A: polar quadrature about 0 over the period parallelogram P, radial variable s = log r, cut at eps; numpy theta
series.  Route B: product Gauss-Legendre over P in (x, t), z = x + t tau, with 1/|z|^2 and 2 Re(s1 z/zbar) subtracted
and restored analytically; mpmath jtheta.  The two share no quadrature and no theta code.
Cells N0-N6 as sealed in PREREGISTRATION.md.  Writes the_norm_of_the_boundary_class.json and _run.txt.
"""
import json, math, sys, time
import numpy as np
import mpmath as mp
from numpy.polynomial.legendre import leggauss

OUT = {}
LOG = []
def say(*a):
    s = " ".join(str(x) for x in a); LOG.append(s); print(s, flush=True)

# ---------------------------------------------------------------- route A: numpy theta series, polar quadrature
K = 40
def thetas(z, tau):
    q = np.exp(1j*np.pi*tau); n = np.arange(0, K); m = np.arange(1, K)
    z = np.asarray(z, dtype=complex)[..., None]
    t1 = 2*np.sum((-1)**n * q**((n+.5)**2) * np.sin((2*n+1)*np.pi*z), -1)
    t2 = 2*np.sum(q**((n+.5)**2) * np.cos((2*n+1)*np.pi*z), -1)
    t3 = 1 + 2*np.sum(q**(m**2) * np.cos(2*m*np.pi*z), -1)
    t4 = 1 + 2*np.sum((-1)**m * q**(m**2) * np.cos(2*m*np.pi*z), -1)
    return t1, t2, t3, t4
def th1p(tau):
    q = np.exp(1j*np.pi*tau); n = np.arange(0, K)
    return 2*np.pi*np.sum((-1)**n*(2*n+1)*q**((n+.5)**2))           # = 2 pi eta^3
def S_A(r, z, tau, scale=1.0):
    t = thetas(z, tau); t0 = thetas(np.array(0.0), tau)
    return scale*t[r-1]*th1p(tau)/(t0[r-1]*t[0])
def rmax_np(th, tau):
    d = np.exp(1j*th); y1 = d.imag/tau.imag; x1 = d.real - y1*tau.real
    return 0.5/np.maximum(np.abs(x1), np.abs(y1))
def vertex_angles(tau):
    v = [0.5+0.5*tau, -0.5+0.5*tau, -0.5-0.5*tau, 0.5-0.5*tau]
    br = sorted(float(np.mod(np.angle(x), 2*np.pi)) for x in v); return br + [br[0] + 2*np.pi]
def cA(r, tau, eps, scale=1.0, nth=96, ns=64):
    """int_{P minus D_eps} |scale*S_r|^2 dA - 2 pi log(1/eps), polar about 0, s = log r, Gauss-Legendre per segment."""
    br = vertex_angles(tau); xg, wg = leggauss(nth); xs, ws = leggauss(ns); tot = 0.0
    for a, b in zip(br[:-1], br[1:]):
        th = 0.5*(b-a)*xg + 0.5*(b+a); wt = 0.5*(b-a)*wg
        s_hi = np.log(rmax_np(th, tau)); s_lo = math.log(eps)
        s = 0.5*(s_hi - s_lo)[:, None]*xs[None, :] + 0.5*(s_hi + s_lo)[:, None]
        wsr = 0.5*(s_hi - s_lo)[:, None]*ws[None, :]
        rr = np.exp(s); z = rr*np.exp(1j*th)[:, None]
        tot += np.sum(wt[:, None]*wsr*np.abs(S_A(r, z, tau, scale))**2*rr**2)
    return float(tot - 2*np.pi*math.log(1/eps))
def R_A(tau):
    t0 = thetas(np.array(0.0), tau); d = th1p(tau)
    return {2: -t0[1]**2/d, 4: -t0[3]**2/d, 3: 1j*t0[2]**2/d}         # R_i (th2), R_j (th4), R_k (th3): B1644
def D_of(c, R): return sum(c[r]*R[r]**2 for r in (2, 3, 4))
def nR2(R): return sum(abs(R[r])**2 for r in (2, 3, 4))

# ---------------------------------------------------------------- route B: mpmath jtheta, strip quadrature
mp.mp.dps = 20
def make_B(tau):
    q = mp.exp(1j*mp.pi*tau); tp = mp.jtheta(1, 0, q, 1)*mp.pi
    t0 = {r: mp.jtheta(r, 0, q) for r in (2, 3, 4)}
    return (lambda r, z: mp.jtheta(r, mp.pi*z, q)*tp/(t0[r]*mp.jtheta(1, mp.pi*z, q)))
def s1_B(S, r):
    rho = mp.mpf('0.02'); N = 64
    return mp.fsum(S(r, rho*mp.expjpi(2*mp.mpf(k)/N))*mp.expjpi(-2*mp.mpf(k)/N) for k in range(N))/(N*rho)
def rmax_mp(th, tau):
    d = mp.expj(th); y1 = mp.im(d)/mp.im(tau); x1 = mp.re(d) - y1*mp.re(tau)
    return mp.mpf(1)/2/max(abs(x1), abs(y1))
def cB(r, tau, n=40):
    tau = mp.mpc(tau); S = make_B(tau); s1 = s1_B(S, r)
    xg, wg = leggauss(n); xg = [mp.mpf(float(v)) for v in xg]; wg = [mp.mpf(float(v)) for v in wg]
    tot = mp.mpf(0)
    for xa, xb in [(-0.5, 0.0), (0.0, 0.5)]:
        for ta, tb in [(-0.5, 0.0), (0.0, 0.5)]:
            for xi, wi in zip(xg, wg):
                x = (xb-xa)/2*xi + (xb+xa)/2
                for tj, wj in zip(xg, wg):
                    t = (tb-ta)/2*tj + (tb+ta)/2; z = x + t*tau
                    f = abs(S(r, z))**2 - 1/abs(z)**2 - 2*mp.re(s1*z/mp.conj(z))
                    tot += wi*wj*(xb-xa)/2*(tb-ta)/2*f
    tot *= mp.im(tau)
    v = [sx*mp.mpf(1)/2 + sy*tau/2 for sx in (1, -1) for sy in (1, -1)]
    br = sorted(mp.arg(x) % (2*mp.pi) for x in v); br.append(br[0] + 2*mp.pi)
    I_log = mp.fsum(mp.quad(lambda th: mp.log(rmax_mp(th, tau)), [a, b]) for a, b in zip(br[:-1], br[1:]))
    I_e2 = mp.fsum(mp.quad(lambda th: mp.expj(2*th)*rmax_mp(th, tau)**2/2, [a, b]) for a, b in zip(br[:-1], br[1:]))
    return float(tot + 2*mp.re(s1*I_e2) + I_log)

# ---------------------------------------------------------------- the Yukawa of a Higgs in M (B1644, B1645)
def Y(a, u): return np.outer(a, u) + np.outer(u, a) - (a @ u)*np.eye(3)
def vec(R): return np.array([R[2], R[4], R[3]])                       # units i, j, k

W = complex(np.exp(2j*np.pi/3)); WP = W + 1                              # the two corners of the fundamental domain
TAUS = {"omega": W, "i": 1j, "t1": 0.13+1.07j, "t2": 0.3+1.6j, "t3": 2.2j, "t4": 3.0j}
T0 = time.time()

# ---------------------------------------------------------------- N0 plumbing (void below 1e-25 / 1e-12)
mp.mp.dps = 40
pl = {}
qq = lambda tau: mp.exp(1j*mp.pi*mp.mpc(tau))
pl["th_series_vs_jtheta"] = max(float(abs(complex(mp.jtheta(r, mp.pi*mp.mpc(z), qq(tau))) - complex(thetas(np.array(z), tau)[r-1])))
                                for tau in (W, 1j, 0.13+1.07j) for z in (0.1+0.07j, -0.23+0.31j) for r in (1, 2, 3, 4))
def S40(r, z, tau):
    q = qq(tau); tp = mp.jtheta(1, 0, q, 1)*mp.pi
    return mp.jtheta(r, mp.pi*z, q)*tp/(mp.jtheta(r, 0, q)*mp.jtheta(1, mp.pi*z, q))
const = []
for tau in (W, 1j, 0.13+1.07j):
    for (r, s) in ((2, 3), (3, 4)):
        vals = [S40(r, mp.mpc(z), tau)**2 - S40(s, mp.mpc(z), tau)**2 for z in (0.11+0.05j, -0.21+0.33j, 0.37-0.19j)]
        const.append(float(max(abs(vals[0]-vals[1]), abs(vals[0]-vals[2]))))
pl["S_r2_minus_S_s2_constant"] = max(const)                               # S_r^2 - S_s^2 = e_s - e_r
pl["th1p_vs_2pi_eta3"] = max(float(abs(mp.jtheta(1, 0, qq(tau), 1)*mp.pi - 2*mp.pi*mp.exp(1j*mp.pi*mp.mpc(tau)/4)**1 *
                              mp.qp(qq(tau)**2)**3)) for tau in (W, 1j, 0.13+1.07j))
def RR40(tau):
    q = qq(tau); t2, t3, t4 = (mp.jtheta(r, 0, q) for r in (2, 3, 4))
    return abs(t2**4 + t4**4 - t3**4)/(abs(t2)**4 + abs(t3)**4 + abs(t4)**4)
pl["R_dot_R_isotropic"] = max(float(RR40(tau)) for tau in (W, 1j, 0.13+1.07j, 2.2j))
pl["numpy_RR_isotropic"] = max(abs(sum(R_A(t)[r]**2 for r in (2, 3, 4)))/nR2(R_A(t)) for t in TAUS.values())
pl["void"] = not (pl["th_series_vs_jtheta"] < 1e-12 and pl["S_r2_minus_S_s2_constant"] < 1e-25
                  and pl["th1p_vs_2pi_eta3"] < 1e-25 and pl["R_dot_R_isotropic"] < 1e-25 and pl["numpy_RR_isotropic"] < 1e-14)
OUT["N0"] = pl; say("N0", pl)
mp.mp.dps = 20
if pl["void"]: OUT["VOID"] = True; json.dump(OUT, open("the_norm_of_the_boundary_class.json", "w"), indent=1, default=str); sys.exit(2)

# ---------------------------------------------------------------- N1 the universal log, and its control
n1 = {"spread": {}, "control_drift": {}}
for name in ("omega", "i", "t1", "t3"):
    tau = TAUS[name]
    for r in (2, 3, 4):
        v = [cA(r, tau, e) for e in (1e-3, 1e-4, 1e-5)]
        n1["spread"][f"{name},{r}"] = max(v) - min(v)
        w2 = [cA(r, tau, e, scale=2.0) for e in (1e-3, 1e-4)]                # residue 2: coefficient 8 pi, not 2 pi
        n1["control_drift"][f"{name},{r}"] = (w2[1] - w2[0])/math.log(10)    # predicted 6 pi
n1["spread_max"] = max(n1["spread"].values())
n1["control_drift_over_6pi_minmax"] = [min(v/(6*np.pi) for v in n1["control_drift"].values()),
                                       max(v/(6*np.pi) for v in n1["control_drift"].values())]
n1["holds"] = n1["spread_max"] < 1e-9 and all(abs(v/(6*np.pi) - 1) < 1e-6 for v in n1["control_drift"].values())
OUT["N1"] = n1; say("N1", {k: n1[k] for k in ("spread_max", "control_drift_over_6pi_minmax", "holds")})

# ---------------------------------------------------------------- N2 two routes
C = {}; n2 = {}
for name, tau in TAUS.items():
    C[name] = {r: cA(r, tau, 1e-5) for r in (2, 3, 4)}
    for r in (2, 3, 4):
        b = cB(r, tau, 40); n2[f"{name},{r}"] = {"A": C[name][r], "B": b, "diff": abs(b - C[name][r])}
    say("  N2", name, {r: round(C[name][r], 10) for r in (2, 3, 4)}, f"[{time.time()-T0:.0f}s]")
OUT["N2"] = {"pairs": n2, "max_diff": max(v["diff"] for v in n2.values())}
OUT["N2"]["holds"] = OUT["N2"]["max_diff"] < 1e-8
say("N2", {"max_diff": OUT["N2"]["max_diff"], "holds": OUT["N2"]["holds"]})

# ---------------------------------------------------------------- N3 symmetry
cw, ci, c1 = C["omega"], C["i"], C["t1"]
n3 = {"omega_spread": max(cw.values()) - min(cw.values()), "i_pair_2_4": abs(ci[2] - ci[4]), "i_third": abs(ci[3] - ci[2]),
      "t1_min_pairwise": min(abs(c1[2]-c1[3]), abs(c1[3]-c1[4]), abs(c1[2]-c1[4]))}
n3["holds"] = n3["omega_spread"] < 1e-10 and n3["i_pair_2_4"] < 1e-10 and n3["i_third"] > 1 and n3["t1_min_pairwise"] > 0.1
OUT["N3"] = n3; say("N3", n3)

# ---------------------------------------------------------------- N4 the cancellation, and its two controls
n4 = {}
for name, tau in TAUS.items():
    R = R_A(tau); c = C[name]; D = D_of(c, R)
    uu = [sum((2*np.pi*L + c[r])*R[r]**2 for r in (2, 3, 4)) for L in (5.0, 20.0, 80.0)]
    lam = {2: 1.0, 3: 2.0, 4: 4.0}                                            # channel-dependent cutoffs eps_r = eps*lam_r
    uu_c = [sum((2*np.pi*(L - math.log(lam[r])) + c[r])*R[r]**2 for r in (2, 3, 4)) for L in (5.0, 20.0)]
    t0 = thetas(np.array(0.0), tau); d = th1p(tau)
    Rp = {2: t0[1]**2/d, 4: 1j*t0[3]**2/d, 3: t0[2]**2/d}                     # another phase assignment: R'.R' != 0
    upup = [sum((2*np.pi*L + c[r])*Rp[r]**2 for r in (2, 3, 4)) for L in (5.0, 20.0)]
    n4[name] = {"uu_L_spread_rel": max(abs(x - uu[0]) for x in uu)/(nR2(R)*80*2*np.pi),
                "uu_minus_D_rel": abs(uu[0] - D)/(nR2(R)*5*2*np.pi),
                "cutoff_control_shift": abs(uu_c[0] - D), "cutoff_control_pred": abs(-2*np.pi*sum(math.log(lam[r])*R[r]**2 for r in (2, 3, 4))),
                "Rprime_slope_over_2piRpRp": abs((upup[1] - upup[0])/15.0)/abs(2*np.pi*sum(Rp[r]**2 for r in (2, 3, 4)))}
n4["holds"] = all(v["uu_L_spread_rel"] < 1e-12 and v["uu_minus_D_rel"] < 1e-12 and v["cutoff_control_shift"] > 1e-3*nR2(R_A(TAUS[k]))
                  and abs(v["cutoff_control_shift"]/v["cutoff_control_pred"] - 1) < 1e-9 and abs(v["Rprime_slope_over_2piRpRp"] - 1) < 1e-9
                  for k, v in n4.items() if k != "holds")
OUT["N4"] = n4; say("N4", {k: (v if k == "holds" else {kk: float(f"{vv:.3e}") for kk, vv in v.items()}) for k, v in n4.items()})

# ---------------------------------------------------------------- N5 D's zero at omega, the grid, the cusp
n5 = {}
Dn = {name: D_of(C[name], R_A(t))/nR2(R_A(t)) for name, t in TAUS.items()}
n5["D_over_R2"] = {k: [v.real, v.imag] for k, v in Dn.items()}
n5["omega_abs"] = abs(Dn["omega"])
n5["away_min_named"] = min(abs(Dn[k]) for k in ("i", "t1", "t2"))
grid = []
for x in np.round(np.linspace(-0.5, 0.5, 21), 4):
    for y in np.round(np.arange(0.86, 2.0001, 0.06), 4):
        tau = complex(x, y)
        if abs(tau) < 1 - 1e-9: continue
        R = R_A(tau); c = {r: cA(r, tau, 1e-5, nth=64, ns=48) for r in (2, 3, 4)}
        grid.append((float(x), float(y), float(abs(D_of(c, R))/nR2(R)), float(min(abs(tau - W), abs(tau - WP)))))
far = [g for g in grid if g[3] > 0.1]
n5["grid_points"] = len(grid); n5["grid_far_points"] = len(far)
n5["grid_far_min"] = min(g[2] for g in far); n5["grid_far_argmin"] = min(far, key=lambda g: g[2])[:2]
n5["grid_global_argmin"] = min(grid, key=lambda g: g[2])[:2]
cusp = {}
for y in (4.0, 5.0):
    tau = complex(0, y); R = R_A(tau); c = {r: cA(r, tau, 1e-5, nth=160, ns=96) for r in (2, 3, 4)}
    q = math.exp(-math.pi*y); cusp[y] = float((D_of(c, R)/nR2(R)).real/q)
n5["cusp_D_over_qR2"] = cusp; n5["cusp_slope_over_8pi2"] = (cusp[5.0] - cusp[4.0])/(8*np.pi**2)
n5["holds"] = (n5["omega_abs"] < 1e-10 and n5["away_min_named"] > 0.1 and n5["grid_far_min"] > 0.05
               and abs(n5["cusp_slope_over_8pi2"] - 1) < 5e-3)
OUT["N5"] = n5; say("N5", {k: n5[k] for k in n5 if k != "D_over_R2"}, f"[{time.time()-T0:.0f}s]")

# ---------------------------------------------------------------- N6 the masses
rng = np.random.default_rng(1654)
def cplx(n): return rng.normal(size=n) + 1j*rng.normal(size=n)
n6 = {}
dirs = [cplx(3) for _ in range(3)]
for name in ("omega", "i", "t1"):
    tau = TAUS[name]; R = R_A(tau); Rv = vec(R); c = C[name]; cv = np.array([c[2], c[4], c[3]])
    D = D_of(c, R); recs = []
    near = np.conj(Rv) + 0.1*np.linalg.norm(Rv)*cplx(3)/math.sqrt(6)        # near the cone, about R-bar
    for a in dirs + [near]:
        s0 = np.linalg.svd(Y(a, Rv), compute_uv=False)                        # sigma1 >= sigma2 > sigma3 = 0
        lim = abs(a @ a)*abs(D)*abs(a @ Rv)/(2*np.pi*s0[0]**2*s0[1])
        rows = []
        for L in (40.0, 160.0, 640.0, 2560.0):
            u = np.sqrt(2*np.pi*L + cv)*Rv
            U, s, Vh = np.linalg.svd(Y(a, u)); v3 = np.conj(Vh[2])
            ang = math.acos(min(1.0, abs(np.vdot(v3, Rv))/np.linalg.norm(Rv)))
            rows.append({"L": L, "m1_m3": s[2]/s[0], "m2_m3": s[1]/s[0], "L_m1_m3": L*s[2]/s[0], "angle": ang,
                         "angle_over_sqrt_m1_m2": ang/math.sqrt(s[2]/s[1]) if s[2] > 0 else None})
        u_eq = Rv; m1_eq = np.linalg.svd(Y(a, u_eq), compute_uv=False)        # P4': equal framed data
        recs.append({"limit": lim, "rows": rows, "P4prime_m1_m3": m1_eq[2]/m1_eq[0]})
    n6[name] = recs
om = n6["omega"]; others = n6["i"] + n6["t1"]
n6["omega_m1_m3_max"] = max(r["m1_m3"] for rec in om for r in rec["rows"])
n6["P4prime_m1_m3_max"] = max(rec["P4prime_m1_m3"] for rec in om + others)
n6["limit_rel_err_at_2560_max"] = max(abs(rec["rows"][-1]["L_m1_m3"]/rec["limit"] - 1) for rec in others)
n6["angle_L_ratio_640_2560"] = [rec["rows"][3]["angle"]*2560/(rec["rows"][2]["angle"]*640) for rec in others]
n6["ratio_halving_640_2560"] = [rec["rows"][3]["angle_over_sqrt_m1_m2"]/rec["rows"][2]["angle_over_sqrt_m1_m2"] for rec in others]
n6["holds"] = (n6["omega_m1_m3_max"] < 1e-12 and n6["P4prime_m1_m3_max"] < 1e-12 and n6["limit_rel_err_at_2560_max"] < 0.02
               and all(abs(x - 1) < 0.03 for x in n6["angle_L_ratio_640_2560"]) and all(abs(x - 0.5) < 0.05 for x in n6["ratio_halving_640_2560"]))
OUT["N6"] = n6; say("N6", {k: n6[k] for k in n6 if k not in ("omega", "i", "t1")})

OUT["seconds"] = time.time() - T0
json.dump(OUT, open("the_norm_of_the_boundary_class.json", "w"), indent=1, default=lambda o: str(o))
open("the_norm_of_the_boundary_class_run.txt", "w").write("\n".join(LOG) + f"\nRUN_EXIT 0 ({OUT['seconds']:.0f} s)\n")
say("RUN_EXIT 0")
