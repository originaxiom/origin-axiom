# E1 exactly as sealed (a copy of its loop; not the instrument file), then three candidate fixes
import numpy as np, math, sys, time
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("cA","pairs","residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","np"): globals()[k] = ns[k]
def a0_of(x, y, t, R, s, rho=0.05, N=128):
    u = rho*np.exp(2j*np.pi*np.arange(N)/N); K = pairs(x, y, u, t)[s]/R[s]; return np.mean(K - 1/u)
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
print("E1 AS SEALED: spread_max %.3e (thr 1e-9); control min/max" % max(e1["spread"]), min(e1["control"]), max(e1["control"]), "(thr |v-1|<1e-6)")
print("   holds =", bool(max(e1["spread"]) < 1e-9 and all(abs(v - 1) < 1e-6 for v in e1["control"])))
print("   n_spread_entries", len(e1["spread"]), " number of entries exceeding 1e-9:", sum(1 for v in e1["spread"] if v > 1e-9), " control entries failing:", sum(1 for v in e1["control"] if abs(v-1) >= 1e-6))
# Fix A: smaller eps grid
def run(eps_list, eps_ctrl, correct=False):
    sp = []; ct = []
    for (p1, p2), t in [((1/9, 1/9), OM), ((1/9, 1/9), GEN), ((2/9, 5/9), OM)]:
        w = line_w(p1, p2, t)
        for sec, (fl, fr) in SECTORS.items():
            x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t)
            cs = [cA(x, y, t, R, eps=e) for e in eps_list]
            c2 = [cA(x, y, t, R, eps=e, scale=2.0) for e in eps_ctrl]
            for s in UNITS:
                if cs[0][s] is None: continue
                a0 = a0_of(x, y, t, R, s)
                vals = [c[s] + (math.pi*e*e*abs(a0)**2 if correct else 0.0) for c, e in zip(cs, eps_list)]
                sp.append(max(vals) - min(vals))
                v2 = [c2[k][s] + (4*math.pi*eps_ctrl[k]**2*abs(a0)**2 if correct else 0.0) for k in range(2)]
                ct.append((v2[1] - v2[0])/(6*np.pi*math.log(eps_ctrl[0]/eps_ctrl[1])))
    return max(sp), max(abs(v - 1) for v in ct)
for name, (el, ec, cor) in {"A: eps=(1e-5,1e-6,1e-7), ctrl (1e-5,1e-6), no correction": ((1e-5, 1e-6, 1e-7), (1e-5, 1e-6), False),
                            "B: sealed eps grid + analytic pi*eps^2*|a0|^2 correction": ((1e-3, 1e-4, 1e-5), (1e-3, 1e-4), True),
                            "C: eps=(1e-4,1e-5,1e-6) + correction": ((1e-4, 1e-5, 1e-6), (1e-4, 1e-5), True)}.items():
    s, c = run(el, ec, cor); print(name, "-> spread max %.2e  control max|v-1| %.2e" % (s, c))
