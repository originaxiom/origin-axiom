"""Referee prep (B1786): load the census through B1786's sealed compare.py (imported, not modified), build the seat-menu
chi2 feature matrices exactly as B1741's chi2_features('seat', False) builds them on ALL 588 lines, tag every row with its
slope class (alpha as stored), and check the per-line minima against comparison.json's read-out."""
import sys, json, pathlib, importlib.util
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
V = ROOT / "frontier/B1786_the_slope_principle_out_of_sample/verification"
OUT = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("b1786_compare", V / "compare.py")
M = importlib.util.module_from_spec(spec); sys.modules["b1786_compare"] = M; spec.loader.exec_module(M)
C = M.C
M._use(cls="all"); A = C.arrays()
rows = M._base(V / "census.jsonl")
alpha_of = {}; b_of = {}
for r in rows:
    alpha_of[r["line"]] = r["alpha"]
F = C.chi2_features("seat", False)
s6, _ = C.sigmas()
lab = A["lab"]
lines = np.array([l[0] for l in lab]); re = np.array([l[1] for l in lab]); im = np.array([l[2] for l in lab])
hor = np.array([0 if l[3] == "L_max" else 1 for l in lab])
classes = sorted(set(alpha_of.values()), key=lambda s: eval(s.replace("/", "/1.0/")) if "/" in s else float(s))
cid = np.array([classes.index(alpha_of[int(l)]) for l in lines])
Xs = np.stack([X for X, f in F])          # (4 configs, rows, 6)
# check the f maps are T/sg for all four
T6 = A["T6"]
for X, f in F: assert np.allclose(f(T6[None, :]), T6[None, :] / s6)
np.savez(OUT / "features.npz", X=Xs, s6=s6, T6=T6, cid=cid, line=lines, re=re, im=im, hor=hor, classes=np.array(classes))
# data: per-line and per-class minima, same expansion as min_chi2
t = T6 / s6
best = np.full(len(lines), np.inf)
for X in Xs:
    best = np.minimum(best, (X ** 2).sum(1) - 2 * X @ t + (t ** 2).sum())
cmp = json.load(open(V / "comparison.json"))
plb = cmp["readout_per_line"]
dev = max(abs(best[lines == int(k)].min() - v["chi2_six_seat"]) for k, v in plb.items())
print("rows", len(lines), "classes", len(classes), "max |per-line min - comparison.json| =", dev)
for i, c in enumerate(classes):
    m = cid == i
    print("%-6s lines %2d  min %.4f" % (c, len(set(lines[m])), best[m].min()))
