"""B1655 -- THE ELECTRON'S ZERO (sealed instrument; one run).

With a flat hypercharge line (charges in units of 6Y: Q 1, u -4, d 2, L -3, e 6, H 3) each sector's four unit pairings
P_s (s = 1, i, j, k) are twisted Szego kernels with a simple pole at the puncture; their residues R_s form a null
quaternion, R_1^2 + R.R = 0 (B1653), with R_s = kappa c_s th_s(ubar) th_s(delta)/th_1'(0), ubar = w_x + w_y = q_H-type
twist, delta = w_x - w_y = (q_L - q_R) w. Under the canonical end condition (B1654's P4, four channels) u_s =
sqrt(2 pi L + c_s) R_s and u.u = D_sector = sum_s c_s R_s^2 (the log cancels because the quaternion is null).
At tau = omega on a line whose Higgs twist 3w is fixed by the order-3 rotation (W59's Higgs lines) the three imaginary
channels have one norm c_perp, so D_sector = (c_1 - c_perp) R_1^2, and R_1 = 0 for the leptons (q_L - q_e = -9, 9w in the
lattice): the electron is massless at this order for every Higgs; the quarks (5, -1) are lifted.

Route A: numpy theta series, polar quadrature about 0 (s = log r), cut at eps. Route B: mpmath (B1653's bilinear), product
Gauss-Legendre over P with 1/|z|^2, 2 Re(a0/zbar) and 2 Re(a1 z/zbar) subtracted and restored. Cells E0-E7 as sealed in
PREREGISTRATION.md. Writes the_electrons_zero.json and _run.txt beside this script, after every cell.
"""
import json, math, pathlib, sys, time
import numpy as np
import mpmath as mp
from numpy.polynomial.legendre import leggauss

HERE = pathlib.Path(__file__).resolve().parent
OUT = {}; LOG = []
def _plain(o):
    if hasattr(o, "item") and getattr(o, "size", 1) == 1: return o.item()
    return str(o)
def dump():
    json.dump(OUT, open(HERE / "the_electrons_zero.json", "w"), indent=1, default=_plain)
    open(HERE / "the_electrons_zero_run.txt", "w").write("\n".join(LOG) + "\n")
def say(*a):
    s = " ".join(str(x) for x in a); LOG.append(s); print(s, flush=True)

QI = np.array([[1j, 0], [0, -1j]]); QJ = np.array([[0, 1], [-1, 0]], dtype=complex); QK = QI @ QJ; EPS = QJ
UNITS = {"1": np.eye(2, dtype=complex), "i": QI, "j": QJ, "k": QK}
BLOCKS = [QJ, QI, QK]                                                        # the generations' blocks (B1644)
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
SECTORS = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
OM = complex(np.exp(2j*np.pi/3)); GEN = 0.13 + 1.07j

# ---------------------------------------------------------------- route A (numpy)
NK = 24
def thc(a, b, u, T):
    n = np.arange(-NK, NK + 1) + a; u = np.asarray(u, dtype=complex)[..., None]
    return np.sum(np.exp(1j*np.pi*T*n*n + 2j*np.pi*n*(u + b)), -1)
def th1(u, t):
    k = np.arange(-NK, NK + 1); h = k + 0.5; u = np.asarray(u, dtype=complex)[..., None]
    return -1j*np.sum((-1.0)**k*np.exp(1j*np.pi*t*h*h + 1j*np.pi*(2*k + 1)*u), -1)
def bil(x, y, u, t):
    (ax, bx), (ay, by) = x, y; T = 2*t; t1 = th1(u, t)
    den = 1j*np.exp(-1j*np.pi*t/2)*np.exp(-1j*np.pi*u)*t1
    X0, X1, Y0, Y1 = thc(ax, bx, u, T), thc(ax, bx, u + t, T), thc(ay, by, u, T), thc(ay, by, u + t, T)
    return np.array([[X0*Y0/t1, np.exp(1j*np.pi*by)*X0*Y1/den], [np.exp(1j*np.pi*bx)*X1*Y0/den, np.exp(1j*np.pi*(bx + by))*X1*Y1/th1(u + t, t)]])
def pairs(x, y, u, t):
    M = bil(x, y, u, t); return {s: np.einsum('mn,mn...->...', EPS @ C, M) for s, C in UNITS.items()}
def twist_of(w, t): a = w.imag/t.imag; return (a, 2*(w.real - a*t.real))
def line_w(p1, p2, t): return p1*t - p2                                      # W59's holonomy phases (B1653)
def sector_twists(w, t, ql, qr): return twist_of(ql*w, t), twist_of(qr*w, t)
def residues(x, y, t, rad=0.01, N=256):
    u = rad*np.exp(2j*np.pi*np.arange(N)/N); P = pairs(x, y, u, t); return {s: complex(np.mean(P[s]*u)) for s in UNITS}
def rmax_np(th, t):
    d = np.exp(1j*th); y1 = d.imag/t.imag; x1 = d.real - y1*t.real; return 0.5/np.maximum(abs(x1), abs(y1))
def vangles(t):
    v = [0.5+0.5*t, -0.5+0.5*t, -0.5-0.5*t, 0.5-0.5*t]
    br = sorted(float(np.mod(np.angle(z), 2*np.pi)) for z in v); return br + [br[0] + 2*np.pi]
def cA(x, y, t, R, eps=1e-5, scale=1.0, nth=96, ns=64):
    br = vangles(t); xg, wg = leggauss(nth); xs, ws = leggauss(ns); tot = {s: 0.0 for s in UNITS}
    for a, b in zip(br[:-1], br[1:]):
        th = 0.5*(b-a)*xg + 0.5*(b+a); wt = 0.5*(b-a)*wg
        hi = np.log(rmax_np(th, t)); lo = math.log(eps)
        sg = 0.5*(hi-lo)[:, None]*xs[None, :] + 0.5*(hi+lo)[:, None]; w2 = 0.5*(hi-lo)[:, None]*ws[None, :]
        rr = np.exp(sg); z = rr*np.exp(1j*th)[:, None]; P = pairs(x, y, z, t)
        for s in UNITS:
            if abs(R[s]) > 1e-12: tot[s] += np.sum(wt[:, None]*w2*np.abs(scale*P[s]/R[s])**2*rr**2)
    return {s: (float(tot[s] - 2*np.pi*math.log(1/eps)) if abs(R[s]) > 1e-12 else None) for s in UNITS}
def nR2(R): return sum(abs(R[s])**2 for s in UNITS)
def D_of(c, R): return sum(c[s]*R[s]**2 for s in UNITS if c[s] is not None)

# ---------------------------------------------------------------- route B (mpmath, B1653's bilinear), strip quadrature
mp.mp.dps = 20; I = mp.mpc(0, 1)
def th_mp(n, u, t):
    q = mp.exp(I*mp.pi*t); x = mp.pi*u
    if n == 3: return mp.jtheta(3, x, q)
    if n == 4: return mp.jtheta(4, x, q)
    q4 = mp.exp(I*mp.pi*t/4); s = x + mp.pi*t/2
    if n == 2: return q4*mp.exp(I*x)*mp.jtheta(3, s, q)
    return -I*q4*mp.exp(I*x)*mp.jtheta(4, s, q)
def thc_mp(a, b, u, T): return mp.exp(I*mp.pi*a*a*T + 2*I*mp.pi*a*(u + b))*th_mp(3, u + a*T + b, T)
def bil_mp(x, y, u, t):
    (ax, bx), (ay, by) = x, y; T = 2*t; t1 = th_mp(1, u, t)
    den = I*mp.exp(-I*mp.pi*t/2)*mp.exp(-I*mp.pi*u)*t1
    X0, X1, Y0, Y1 = thc_mp(ax, bx, u, T), thc_mp(ax, bx, u + t, T), thc_mp(ay, by, u, T), thc_mp(ay, by, u + t, T)
    return [[X0*Y0/t1, mp.exp(I*mp.pi*by)*X0*Y1/den], [mp.exp(I*mp.pi*bx)*X1*Y0/den, mp.exp(I*mp.pi*(bx + by))*X1*Y1/th_mp(1, u + t, t)]]
EC = {s: (EPS @ C) for s, C in UNITS.items()}
def pair_mp(M, s): return sum(complex(EC[s][m, n])*M[m][n] for m in range(2) for n in range(2))
def coeffs_mp(x, y, t, s, R, rho=mp.mpf("0.02"), N=64):
    """K_s = P_s/R_s = 1/z + a0 + a1 z + ...: a0, a1 from circle averages"""
    vals = []
    for k in range(N):
        z = rho*mp.expjpi(2*mp.mpf(k)/N); vals.append((z, pair_mp(bil_mp(x, y, z, t), s)/R))
    a0 = mp.fsum(v - 1/z for z, v in vals)/N
    a1 = mp.fsum((v - 1/z - a0)/z for z, v in vals)/N
    return a0, a1
def rmax_mp(th, t):
    d = mp.expj(th); y1 = mp.im(d)/mp.im(t); x1 = mp.re(d) - y1*mp.re(t); return mp.mpf(1)/2/max(abs(x1), abs(y1))
def cB(x, y, t, s, R, n=32):
    t = mp.mpc(t); x = (mp.mpf(x[0]), mp.mpf(x[1])); y = (mp.mpf(y[0]), mp.mpf(y[1])); R = mp.mpc(R)
    a0, a1 = coeffs_mp(x, y, t, s, R)
    xg, wg = leggauss(n); xg = [mp.mpf(float(v)) for v in xg]; wg = [mp.mpf(float(v)) for v in wg]; tot = mp.mpf(0)
    for xa, xb in [(-0.5, 0.0), (0.0, 0.5)]:
        for ta, tb in [(-0.5, 0.0), (0.0, 0.5)]:
            for xi, wi in zip(xg, wg):
                xx = (xb-xa)/2*xi + (xb+xa)/2
                for tj, wj in zip(xg, wg):
                    tt = (tb-ta)/2*tj + (tb+ta)/2; z = xx + tt*t
                    K = pair_mp(bil_mp(x, y, z, t), s)/R
                    f = abs(K)**2 - 1/abs(z)**2 - 2*mp.re(a0/mp.conj(z)) - 2*mp.re(a1*z/mp.conj(z))
                    tot += wi*wj*(xb-xa)/2*(tb-ta)/2*f
    tot *= mp.im(t)
    v = [sx*mp.mpf(1)/2 + sy*t/2 for sx in (1, -1) for sy in (1, -1)]
    br = sorted(mp.arg(z) % (2*mp.pi) for z in v); br.append(br[0] + 2*mp.pi)
    I_log = mp.fsum(mp.quad(lambda th: mp.log(rmax_mp(th, t)), [a, b]) for a, b in zip(br[:-1], br[1:]))
    I_1 = mp.fsum(mp.quad(lambda th: mp.expj(th)*rmax_mp(th, t), [a, b]) for a, b in zip(br[:-1], br[1:]))      # int 1/zbar dA
    I_2 = mp.fsum(mp.quad(lambda th: mp.expj(2*th)*rmax_mp(th, t)**2/2, [a, b]) for a, b in zip(br[:-1], br[1:]))  # int z/zbar dA
    return float(tot + 2*mp.re(a0*I_1) + 2*mp.re(a1*I_2) + I_log)

# ---------------------------------------------------------------- the coupling with channel weights (B1644, B1653)
def dual_basis():
    G = np.array([[np.sum(EC[t]*UNITS[s]) for s in UNITS] for t in UNITS])                 # pair(E_s := C_s, C_t)
    Gi = np.linalg.inv(G); keys = list(UNITS)
    return {keys[a]: sum(Gi[b, a]*UNITS[keys[b]] for b in range(4)) for a in range(4)}
EDUAL = dual_basis()
def weighted_M(u): return sum(u[s]*EDUAL[s] for s in UNITS)
def coupling(S, M): return np.array([[np.sum((Ca.T @ EPS @ S @ Cb)*M) for Cb in BLOCKS] for Ca in BLOCKS])

T0 = time.time()
LINES18 = [(b + i/3, b + j/3) for b in (1/9, 2/9) for i in range(3) for j in range(3)]

# ---------------------------------------------------------------- E0 plumbing
e0 = {}
mp.mp.dps = 30
dd = 0.0
for (p1, p2) in [(1/9, 1/9), (2/9, 5/9)]:
    w = line_w(p1, p2, OM)
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr])
        for z in (0.17+0.11j, -0.22+0.31j):
            Mn = bil(x, y, np.array(z), OM); Mm = bil_mp((mp.mpf(x[0]), mp.mpf(x[1])), (mp.mpf(y[0]), mp.mpf(y[1])), mp.mpc(z), mp.mpc(OM))
            dd = max(dd, max(abs(complex(Mn[m][n]) - complex(Mm[m][n]))/abs(complex(Mm[m][n])) for m in range(2) for n in range(2)))
e0["numpy_vs_B1653_bilinear"] = dd
mp.mp.dps = 20
# the null quaternion and B1653's residue formula R_s = kappa c_s th_s(ubar) th_s(delta)/th1'(0) (ratios R_s/R_i)
CPRED = {"1": -1j, "i": -1, "j": -1, "k": 1j}; THOF = {"1": 1, "i": 2, "j": 4, "k": 3}
def th_any(n, z, t):
    q = np.exp(1j*np.pi*t); m = np.arange(-NK, NK + 1); z = complex(z)
    if n == 1: return complex(-1j*np.sum((-1.0)**m*np.exp(1j*np.pi*t*(m+.5)**2 + 1j*np.pi*(2*m+1)*z)))
    if n == 2: return complex(np.sum(np.exp(1j*np.pi*t*(m+.5)**2 + 1j*np.pi*(2*m+1)*z)))
    if n == 3: return complex(np.sum(np.exp(1j*np.pi*t*m*m + 2j*np.pi*m*z)))
    return complex(np.sum((-1.0)**m*np.exp(1j*np.pi*t*m*m + 2j*np.pi*m*z)))
nullmax = 0.0; formmax = 0.0
for (p1, p2) in LINES18[:4] + [(0.137, 0.291)]:
    for t in (OM, GEN):
        w = line_w(p1, p2, t)
        for sec, (fl, fr) in SECTORS.items():
            x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t)
            nullmax = max(nullmax, abs(sum(R[s]**2 for s in UNITS))/nR2(R))
            ub = SIXY[fl]*w + SIXY[fr]*w; de = SIXY[fl]*w - SIXY[fr]*w
            pred = {s: CPRED[s]*th_any(THOF[s], ub, t)*th_any(THOF[s], de, t) for s in UNITS}
            ref = R["i"]/pred["i"]
            formmax = max(formmax, max(abs(R[s] - ref*pred[s]) for s in UNITS)/math.sqrt(nR2(R)))
e0["null_quaternion_max"] = nullmax; e0["B1653_residue_formula_max"] = formmax
e0["void"] = not (e0["numpy_vs_B1653_bilinear"] < 1e-11 and nullmax < 1e-12 and formmax < 1e-10)
OUT["E0"] = e0; say("E0", e0); dump()
if e0["void"]: OUT["VOID"] = True; dump(); sys.exit(2)

# ---------------------------------------------------------------- E1 the four-channel universal log, and its control
e1 = {"spread": [], "control": []}
for (p1, p2), t in [((1/9, 1/9), OM), ((1/9, 1/9), GEN)]:
    w = line_w(p1, p2, t)
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t)
        cs = [cA(x, y, t, R, eps=e) for e in (1e-3, 1e-4, 1e-5)]
        for s in UNITS:
            if cs[0][s] is not None: e1["spread"].append(max(c[s] for c in cs) - min(c[s] for c in cs))
        c2 = [cA(x, y, t, R, eps=e, scale=2.0) for e in (1e-3, 1e-4)]
        for s in UNITS:
            if c2[0][s] is not None: e1["control"].append((c2[1][s] - c2[0][s])/(6*np.pi*math.log(10)))
e1["spread_max"] = max(e1["spread"]); e1["control_minmax"] = [min(e1["control"]), max(e1["control"])]
e1["holds"] = bool(e1["spread_max"] < 1e-9 and all(abs(v - 1) < 1e-6 for v in e1["control"]))
OUT["E1"] = {k: e1[k] for k in ("spread_max", "control_minmax", "holds")}; say("E1", OUT["E1"]); dump()

# ---------------------------------------------------------------- E2 two routes
e2 = []
for (p1, p2), t, sec in [((1/9, 1/9), OM, "up"), ((1/9, 2/9), OM, "lep"), ((1/9, 1/9), GEN, "down")]:
    w = line_w(p1, p2, t); fl, fr = SECTORS[sec]; x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t)
    ca = cA(x, y, t, R)
    for s in UNITS:
        if ca[s] is None: continue
        cb = cB(x, y, t, s, R[s]); e2.append({"case": f"{p1:.3f},{p2:.3f},{t},{sec},{s}", "A": ca[s], "B": cb, "diff": abs(ca[s] - cb)})
    say("  E2", sec, f"[{time.time()-T0:.0f}s]")
OUT["E2"] = {"pairs": e2, "max_diff": max(v["diff"] for v in e2)}; OUT["E2"]["holds"] = bool(OUT["E2"]["max_diff"] < 1e-7)
say("E2", {"max_diff": OUT["E2"]["max_diff"], "holds": OUT["E2"]["holds"]}); dump()

# ---------------------------------------------------------------- E3, E4 the 18 lines at omega
rec = []; perp_spread = 0.0; gaps = []; split = 0.0
for (p1, p2) in LINES18:
    w = line_w(p1, p2, OM)
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM); c = cA(x, y, OM, R, nth=64, ns=48)
        perp = [c[s] for s in "ijk"]; perp_spread = max(perp_spread, max(perp) - min(perp))
        cp = sum(perp)/3; D = D_of(c, R)
        if c["1"] is not None: gaps.append(c["1"] - cp); split = max(split, abs(D - (c["1"] - cp)*R["1"]**2)/nR2(R))
        rec.append({"line": [p1, p2], "sector": sec, "R1_rel": abs(R["1"])/math.sqrt(nR2(R)), "D_rel": abs(D)/nR2(R)})
e3 = {"perp_spread_max": perp_spread, "gap_minmax": [min(gaps), max(gaps)], "D_equals_gap_R1sq_max": split}
e3["holds"] = bool(perp_spread < 1e-10 and (max(gaps) - min(gaps)) < 1e-9 and abs(min(gaps)) > 1 and split < 1e-10)
OUT["E3"] = e3; say("E3", e3, f"[{time.time()-T0:.0f}s]"); dump()
lep = [r for r in rec if r["sector"] == "lep"]; qk = [r for r in rec if r["sector"] != "lep"]
e4 = {"lep_R1_rel_max": max(r["R1_rel"] for r in lep), "lep_D_rel_max": max(r["D_rel"] for r in lep),
      "quark_R1_rel_min": min(r["R1_rel"] for r in qk), "quark_D_rel_min": min(r["D_rel"] for r in qk),
      "quark_D_values": sorted({round(r["D_rel"], 6) for r in qk})}
e4["holds"] = bool(e4["lep_R1_rel_max"] < 1e-12 and e4["lep_D_rel_max"] < 1e-10 and e4["quark_R1_rel_min"] > 0.1 and e4["quark_D_rel_min"] > 0.5)
OUT["E4"] = e4; OUT["E4_records"] = rec; say("E4", e4); dump()

# ---------------------------------------------------------------- E5 controls
def lepD(w, t, ql=SIXY["L"], qr=SIXY["e"]):
    x, y = sector_twists(w, t, ql, qr); R = residues(x, y, t); c = cA(x, y, t, R, nth=64, ns=48)
    return abs(D_of(c, R))/nR2(R), abs(R["1"])/math.sqrt(nR2(R))
e5 = {"a_generic_tau": [lepD(line_w(p1, p2, GEN), GEN)[0] for (p1, p2) in LINES18[:3]],
      "b_nonfixed_lines": [lepD(line_w(p1, p2, OM), OM) for (p1, p2) in [(1/9, 2/9), (1/9, 0.0), (2/9, 1/9)]],
      "c_fictitious_charges": [lepD(line_w(p1, p2, OM), OM, -3, 5)[0] for (p1, p2) in LINES18[:3]]}
e5["holds"] = bool(min(e5["a_generic_tau"]) > 0.1 and min(v[0] for v in e5["b_nonfixed_lines"]) > 0.1
                   and max(v[1] for v in e5["b_nonfixed_lines"]) < 1e-12 and min(e5["c_fictitious_charges"]) > 0.1)
OUT["E5"] = e5; say("E5", e5, f"[{time.time()-T0:.0f}s]"); dump()

# ---------------------------------------------------------------- E6 the masses
rng = np.random.default_rng(1655)
def rndS(): return rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
SS = [rndS() for _ in range(5)]
e6 = {"lep_rank_ratio_max": 0.0, "quark_L_ratio_rel_err": [], "quark_m1m3_at_40": []}
for (p1, p2) in LINES18[:3]:
    w = line_w(p1, p2, OM)
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM); c = cA(x, y, OM, R, nth=64, ns=48)
        for S in SS:
            vals = {}
            for L in (40.0, 640.0, 2560.0):
                u = {s: (math.sqrt(2*np.pi*L + c[s])*R[s] if c[s] is not None else 0j) for s in UNITS}
                sv = np.linalg.svd(coupling(S, weighted_M(u)), compute_uv=False); vals[L] = sv[2]/sv[0]
            if sec == "lep": e6["lep_rank_ratio_max"] = max(e6["lep_rank_ratio_max"], max(vals.values()))
            else:
                e6["quark_L_ratio_rel_err"].append(abs(2560*vals[2560]/(640*vals[640]) - 1)); e6["quark_m1m3_at_40"].append(vals[40.0])
e6["quark_L_ratio_rel_err_max"] = max(e6["quark_L_ratio_rel_err"]); e6["quark_m1m3_at_40_minmax"] = [min(e6["quark_m1m3_at_40"]), max(e6["quark_m1m3_at_40"])]
e6["holds"] = bool(e6["lep_rank_ratio_max"] < 1e-12 and e6["quark_L_ratio_rel_err_max"] < 0.02 and min(e6["quark_m1m3_at_40"]) > 1e-6)
OUT["E6"] = {k: e6[k] for k in ("lep_rank_ratio_max", "quark_L_ratio_rel_err_max", "quark_m1m3_at_40_minmax", "holds")}
say("E6", OUT["E6"]); dump()

# ---------------------------------------------------------------- E7 read-outs
w = line_w(1/9, 1/9, OM); ro = {}
for sec, (fl, fr) in SECTORS.items():
    x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM); c = cA(x, y, OM, R)
    ro[sec] = {"c": {s: c[s] for s in UNITS}, "R1_rel": abs(R["1"])/math.sqrt(nR2(R)), "D_rel": abs(D_of(c, R))/nR2(R)}
OUT["E7"] = ro; OUT["seconds"] = time.time() - T0
say("E7", {k: (round(v["D_rel"], 6), round(v["R1_rel"], 6)) for k, v in ro.items()})
say(f"RUN_EXIT 0 ({OUT['seconds']:.0f} s)"); dump()
