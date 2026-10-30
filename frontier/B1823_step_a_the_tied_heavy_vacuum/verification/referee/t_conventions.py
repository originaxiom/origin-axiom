"""How far does the decoupling-limit vacuum (tau0* = argmin V0, S0* = Q's lowest eigenvector; the draft's 'physical regime')
move between normalisation conventions for the tie?  Singlets: 'sup' (the draft's primary: max (2y)^w |Y|^2 = 1), 'cusp'
(leading coefficient 1, the source's), 'L2' (int_F (2y)^w |Y|^2 dmu = 1, a Petersson-type norm with the draft's (2y)^w);
triplets: 'N' (F_a / 2^(a/3); DR x 24) or 'cusp'.  Menu Z and H, n = 2, 3, 4, 5; mu^2 = 0.5, m0^2 = 0.005 (analysis_leading's
point); the draft's numpy Model with the cancellation-free F; 12 Nelder-Mead starts for tau0* (Im tau up to 6).
-> t_conventions.json"""
import sys, pathlib, json
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(1, str(HERE / "rerun"))
import numpy as np
from scipy.optimize import minimize
from scipy.integrate import dblquad
import model as M, search as Sr
from t_runaway_stable import stable_F
M.Ffun = stable_F; Sr.Ffun = stable_F
from search import Model, make_copies, SINGLET_LIST, sup_norm
from model import reduce_to_F, form_values, Singlet


def l2_norm(s, p, r):
    S = Singlet(s, p, r)
    def f(y, x):
        th, dth, ddth, E4, E6, ae = form_values(complex(x, y))
        return (2 * y) ** S.w * S.absval(th, E4, E6, ae) ** 2 / y ** 2
    v, err = dblquad(f, -0.5, 0.5, lambda x: np.sqrt(1 - x * x), lambda x: 14.0, epsabs=1e-13, epsrel=1e-9)
    return v

L2 = {spr: l2_norm(*spr) for spr in SINGLET_LIST}


def build(menu, n, sconv, tconv, mu2=0.5, m02=0.005):
    cps = make_copies(n, menu, "N" if tconv == "N" else "cusp", "sup" if sconv == "sup" else "cusp")
    if sconv == "L2":
        for i, c in enumerate(cps):
            for Y, spr in ((c.YL, SINGLET_LIST[2 * i]), (c.YE, SINGLET_LIST[2 * i + 1])):
                Y.c = 1.0 / np.sqrt(L2[spr])
    return Model(cps, mu2, m02, 0.3)


def dec_vacuum(model, rng):
    f = lambda p: model.V0(reduce_to_F(complex(p[0], p[1]), np.ones(3))[0]) if 0.05 < p[1] < 6.0 else 1e30
    best = None
    for _ in range(12):
        x0 = [rng.uniform(-0.5, 0.5), rng.uniform(0.9, 5.5)]
        r = minimize(f, x0, method="Nelder-Mead", options=dict(xatol=1e-12, fatol=1e-16, maxiter=20000))
        if best is None or r.fun < best[0]:
            best = (r.fun, r.x)
    t = reduce_to_F(complex(*best[1]), np.ones(3))[0]
    if t.real < 0:
        t = -t.conjugate()
    Qm = model.Q(t) / model.lv ** 2
    ev, Uv = np.linalg.eigh(Qm)
    A, D, W = model.pieces(t)
    cs = [model.c_coef(a, d) for a, d in zip(A, D)]
    return t, best[0], Uv[:, 0], ev, cs


def hyp(t1, t2):
    return float(np.arccosh(1 + abs(t1 - t2) ** 2 / (2 * t1.imag * t2.imag)))


def fs(S1, S2):
    return float(np.arccos(min(1.0, abs(np.vdot(S1 / np.linalg.norm(S1), S2 / np.linalg.norm(S2))))))


rng = np.random.default_rng(31)
out = dict(L2_norms={str(k): v for k, v in L2.items()}, sup_norms={str(k): sup_norm(*k) for k in SINGLET_LIST}, rows=[])
for menu in ("Z", "H"):
    for n in (2, 3, 4, 5):
        res = {}
        for sconv in ("sup", "cusp", "L2"):
            for tconv in ("N", "cusp"):
                t, V0, S, ev, cs = dec_vacuum(build(menu, n, sconv, tconv), rng)
                res[(sconv, tconv)] = (t, S)
                out["rows"].append(dict(menu=menu, n=n, singlets=sconv, triplets=tconv, tau0=[t.real, t.imag], V0=V0,
                                        Q_eigs=[float(e) for e in ev], c_coefs=[float(c) for c in cs],
                                        all_copies_heavy=bool(min(cs) > 0), S0=[[c.real, c.imag] for c in S]))
                print("%s n=%d singlets %-4s triplets %-4s tau0* = %.4f%+.4fi  c_min %+.4f  Q eigs %s" % (
                    menu, n, sconv, tconv, t.real, t.imag, min(cs), np.round(ev, 5)), flush=True)
        t0, S0 = res[("sup", "N")]
        for k, (t, S) in res.items():
            out["rows"].append(dict(menu=menu, n=n, compare="(%s, %s) vs the draft's (sup, N)" % k,
                                    tau_hyperbolic_distance=hyp(t0, t), direction_FS_distance=fs(S0, S)))
(HERE / "t_conventions.json").write_text(json.dumps(out, indent=1))
for r in out["rows"]:
    if "compare" in r:
        print(r["menu"], r["n"], r["compare"], "d_hyp %.3f  d_FS %.3f" % (r["tau_hyperbolic_distance"], r["direction_FS_distance"]))
