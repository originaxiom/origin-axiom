"""STEP A v2 -- the free numbers in the decoupling limit lambda v / M -> 0 (data-free):
    python3 -I analysis_leading.py -> analysis_leading.json

In the limit the vacuum is (tau0*, S*): tau0* = argmin V0 (the singlets alone; depends on mu^2/M^2, m0^2/mu^2) and S* the
lowest eigenvector of Q(tau0*) (the heavy threshold's 3x3 mass matrix of the Higgs copies; its weights c_i depend on the
same two numbers).  lambda v drops out of both.  Here: the speeds of (tau0*, S*) per unit log mu^2 and log m0^2 (tau in
hyperbolic units, S in Fubini-Study), and the gap of Q (isolation of S*), for both menus, n = 1..8.
"""
import sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import numpy as np
from scipy.optimize import minimize
from model import reduce_to_F, unit
from search import Model, make_copies, fs_dist

DMAT = np.diag([1.0, 1.0, -1.0])
NSTART = 8                                    # 2-D starts for argmin V0 (checked against section D's exact n = 2 vacua)
PART = sys.argv[1] if len(sys.argv) > 1 else "all"     # "Z", "H", "scan" or "all"; parts write analysis_leading_<part>.json


def tau0_star(model, start=None, rng=None):
    f = lambda p: model.V0(reduce_to_F(complex(p[0], p[1]), np.ones(3))[0]) if p[1] > 0.05 else 1e30
    starts = [start] if start is not None else [(rng.uniform(-0.5, 0.5), rng.uniform(0.9, 3.5)) for _ in range(NSTART)]
    best = None
    for s in starts:
        r = minimize(f, s, method="Nelder-Mead", options=dict(xatol=1e-13, fatol=1e-17, maxiter=20000))
        if best is None or r.fun < best[0]:
            best = (r.fun, r.x)
    t = reduce_to_F(complex(*best[1]), np.ones(3))[0]
    if t.real < 0:
        t = -t.conjugate()
    return t, best[0]


def S_star(model, t):
    Qm = model.Q(t) / model.lv ** 2
    ev, U = np.linalg.eigh(Qm)
    return U[:, 0], ev


def fs_small(S0, S1):
    """Fubini-Study distance, stable for small distances: 2 arcsin(|e^{i phi} S1 - S0| / 2) with the optimal phase"""
    S0 = unit(S0); S1 = unit(S1); ov = np.vdot(S0, S1)
    if abs(ov) > 0:
        S1 = S1 * (abs(ov) / ov)
    return float(2 * np.arcsin(min(1.0, np.linalg.norm(S1 - S0) / 2)))


def align(S, Sref):
    """the representative of S's line closest to Sref (phase) -- for differences"""
    ph = np.vdot(S, Sref); return S * (ph / abs(ph)) if abs(ph) > 0 else S


out = {}
rng = np.random.default_rng({"Z": 31, "H": 32, "scan": 33}.get(PART, 31))
for menu in [m for m in ("Z", "H") if PART in (m, "all")]:
    rows = {}
    for n in range(1, 9):
        mu2, m02 = 0.5, 0.005
        base = Model(make_copies(n, menu), mu2, m02, 0.3)
        t0, v0 = tau0_star(base, rng=rng)
        S0, ev = S_star(base, t0)
        speeds = {}
        for name, dmu, dm in (("log mu2", 1e-4, 0.0), ("log m02", 0.0, 1e-4)):
            pts = []
            for sgn in (1, -1):
                m = Model(make_copies(n, menu), mu2 * np.exp(sgn * dmu), m02 * np.exp(sgn * dm), 0.3)
                t, _ = tau0_star(m, start=(t0.real, t0.imag))
                # keep the same mirror image as t0
                if abs(t - t0) > abs(-t.conjugate() - t0):
                    t = -t.conjugate()
                S, _ = S_star(m, t)
                pts.append((t, align(S, S0)))
            d = 2 * (dmu + dm)
            dtau = abs(pts[0][0] - pts[1][0]) / d / t0.imag
            dS = fs_small(pts[0][1], pts[1][1]) / d
            speeds[name] = dict(tau_hyperbolic=float(dtau), S_fubini_study=float(dS))
        rows[n] = dict(tau0=[t0.real, t0.imag], V0=float(v0), Q_eigs_over_lv2=[float(e) for e in ev],
                       S_star_degenerate=bool(abs(ev[1] - ev[0]) < 1e-9 * max(abs(ev[2]), 1e-300)),
                       Q_gap_ratio=float((ev[1] - ev[0]) / max(abs(ev[2]), 1e-300)),
                       S_star=[[c.real, c.imag] for c in S0], speeds=speeds)
        print("%s n=%d tau0*=%.6f+%.6fi  Q eigs %s  speeds mu2 (tau %.3g, S %.3g)  m02 (tau %.3g, S %.3g)" % (
            menu, n, t0.real, t0.imag, np.round(ev, 5), speeds["log mu2"]["tau_hyperbolic"], speeds["log mu2"]["S_fubini_study"],
            speeds["log m02"]["tau_hyperbolic"], speeds["log m02"]["S_fubini_study"]), flush=True)
    out["menu_" + menu] = rows
# the n = 2 vacuum along the one free number: exact at zero mixing (tau* = argmin V0, S* = Y1 x Y2 at tau*)
scan = []
for mu2 in ([round(0.20 + 0.05 * k, 2) for k in range(16)] if PART in ("scan", "all") else []):
    m = Model(make_copies(2, "Z"), mu2, 0.01 * mu2, 0.3)
    t, v = tau0_star(m, rng=rng)
    A, D, W = m.pieces(t)
    cr = np.cross(W[0], W[1]); cr = cr / np.linalg.norm(cr)
    k = int(np.argmax(np.abs(cr))); cr = cr * (abs(cr[k]) / cr[k])
    line_ = ("Re tau = 0" if abs(t.real) < 1e-6 else "Re tau = 1/2" if abs(abs(t.real) - 0.5) < 1e-6 else
             "|tau| = 1" if abs(abs(t) - 1) < 1e-6 else None)
    cs = [float(m.c_coef(a, d)) for a, d in zip(A, D)]
    scan.append(dict(mu2=mu2, tau=[t.real, t.imag], V0=float(v), mirror_line=line_, c_coefs=cs,
                     S_star=[[c.real, c.imag] for c in cr]))
    print("n=2 scan mu2=%.2f tau*=%.6f%+.6fi line=%s c=%s S*=%s" % (mu2, t.real, t.imag, line_, np.round(cs, 4),
          np.round(cr, 4)), flush=True)
if scan:
    out["n2_scan_menu_Z"] = scan

out["reading"] = ("lambda v drops out of the decoupling-limit vacuum for every n; S* is isolated when Q's lowest eigenvalue is "
                  "simple (n >= 2; n = 1 has a double zero: a CP^1); the vacuum moves with mu^2/M^2 at leading order and with "
                  "m0^2/mu^2 at sub-leading order")
(HERE / ("analysis_leading.json" if PART == "all" else "analysis_leading_%s.json" % PART)).write_text(json.dumps(out, indent=1),
                                                                                                encoding="utf-8")
