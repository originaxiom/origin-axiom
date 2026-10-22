"""B1704 (P-251; no data): where would a content hold tau?  F(tau) = sum_c W_c S_c(tau, p_c) in B1686's units
(cusp coefficients: trivial 2, (1/2, 0) -31/16, (0, 1/2) 2, (1/2, 1/2) -31/16 zeta(6) per unit weight); the matter by
PH2's verified shape, 90 (31/1024) [E(tau, 3) - E(tau, 2)]; V = -F (a positive cusp coefficient runs to the cusp).
Contents: B1686's (a)-(c) at the line (1/2, 1/2), plus n_f trivial Weyl fermions (W = -2 on (0, 0)) or n_b complex
scalars twisted along the shrinking cycle (W = +2 on (1/2, 0)).  The minima of V on Re tau = 0 and 1/2.  The basis
functions are computed once on the grid; contents are linear combinations."""
import sys, importlib.util, json, pathlib
import numpy as np
P = pathlib.Path(__file__).resolve().parents[3] / "frontier"
f = next(P.glob("B1686_*/verification/main_w62.py"))
sys.path.insert(0, str(f.parent)); spec = importlib.util.spec_from_file_location("w62", f); W = importlib.util.module_from_spec(spec); spec.loader.exec_module(W)
ys = np.round(np.arange(0.9, 8.0001, 0.01), 3)
KEYS = [(0.0, 0.0), (0.5, 0.0), (0.0, 0.5), (0.5, 0.5)]
BAS = {}
for re_t in (0.0, 0.5):
    ts = [complex(re_t, y) for y in ys]
    BAS[re_t] = {"E3": np.array([W.E_cs(t, 3) for t in ts]), "E2": np.array([W.E_cs(t, 2) for t in ts])}
    for p in KEYS[1:]: BAS[re_t][p] = np.array([W.S_c(t, p) for t in ts])
    BAS[re_t][(0.0, 0.0)] = BAS[re_t]["E3"]
KAP = {(0.0, 0.0): 2, (0.5, 0.0): -31 / 16, (0.0, 0.5): 2, (0.5, 0.5): -31 / 16}
def norm(p): return (round(p[0] % 1, 3), round(p[1] % 1, 3))
cps = [norm(c) for c in W.copies((0.5, 0.5))]
base = {("m",): 90} ; [base.__setitem__(c, base.get(c, 0) + 2) for c in cps]
CONT = {"(a)": dict(base), "(b)": {**base, (0.0, 0.0): base.get((0.0, 0.0), 0) + 24}, "(c)": {**base, (0.0, 0.0): base.get((0.0, 0.0), 0) + 28.5}}
def cusp(c): return sum(w * (31 / 1024) * 2 if k == ("m",) else w * KAP[k] for k, w in c.items())
def F(c, re_t):
    b = BAS[re_t]; return sum(w * (31 / 1024) * (b["E3"] - b["E2"]) if k == ("m",) else w * b[k] for k, w in c.items())
out = {"contents": {k: {str(kk): vv for kk, vv in v.items()} for k, v in CONT.items()}, "copies": [list(c) for c in cps], "rows": []}
for name, c0 in CONT.items():
    print(name, "cusp coefficient (zeta6 units) %.4f" % cusp(c0))
    for extra, key, w in (("trivial Weyl fermions", (0.0, 0.0), -2), ("scalars along the shrinking cycle", (0.5, 0.0), 2)):
        shown = 0
        for n in range(1, 80):
            c = dict(c0); c[key] = c.get(key, 0) + w * n
            kc = cusp(c)
            if kc >= 0: continue
            row = {"content": name, "extra": extra, "n": n, "cusp": kc}
            for re_t in (0.0, 0.5):
                v = -F(c, re_t); d = np.diff(v)
                row["minima_y_Re%.1f" % re_t] = [float(ys[i + 1]) for i in range(len(d) - 1) if d[i] < 0 <= d[i + 1]]
            out["rows"].append(row)
            if shown < 12: print("  +%2d %s: cusp %.3f; minima on Re 0: %s; on Re 1/2: %s" % (n, extra, kc, row["minima_y_Re0.0"], row["minima_y_Re0.5"])); shown += 1
json.dump(out, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
