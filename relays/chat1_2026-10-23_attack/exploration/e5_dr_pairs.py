"""POST HOC exploration, labelled: aligned pairs with DR (read so that it is h0-led) in one or both sectors."""
import contextlib, importlib.util, io, json, math, sys, pathlib, subprocess
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[3]; ZF = ROOT / "relays/chat1_2026-10-23_zero_free_frame"
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("zfc", ZF / "zero_free_census.py"); zfc = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(zfc)
rbs, B, tic = zfc.rbs, zfc.B, zfc.tic
exec(open(pathlib.Path(__file__).resolve().parent / "e_common.py").read())
I = json.loads((ZF / "zero_free_census_index.json").read_text())
X = np.load(ZF / "zero_free_census.npz")["data"].astype(np.float64)
DIRS = I["dirs"]; fi = {f: i for i, f in enumerate(I["fields"])}
LEAD = {"dR": "St", "F_2": "St", "F_10": "St", "F_18": "St", "F_26": "St", "F_6": "S", "F_14": "S", "F_22": "S"}
NULLED = [d for d in LEAD if d != "F_2"]
vcb = np.stack([X[:, DIRS.index(d), :, fi[f"Vcb {LEAD[d]}|{LEAD[d]}"]] for d in LEAD], axis=-1)
vch = np.exp(np.median(np.log(vcb), axis=-1))
cands = []
for du in NULLED:
    for dd in NULLED:
        if "dR" not in (du, dd):
            continue
        u2 = X[:, DIRS.index(du), :, fi[f"log10 up m2/m3 {LEAD[du]}"]]; u1 = X[:, DIRS.index(du), :, fi[f"log10 up m1/m3 {LEAD[du]}"]]
        g = lambda sec, r: X[:, DIRS.index(dd), :, fi[f"log10 {sec} {r} {LEAD[dd]}"]]
        L6 = np.stack([u2, u1, g("down", "m2/m3"), g("down", "m1/m3"), g("lep", "m2/m3") + math.log10(3), g("lep", "m1/m3") - math.log10(3)], axis=-1) * math.log(10)
        chi = np.sum(((L6 - T6) / SIG[:6]) ** 2, axis=-1) + ((np.log(vch) - T9[7]) / SIG[7]) ** 2
        for k in np.argsort(chi, axis=None)[:10]:
            p, h = np.unravel_index(int(k), chi.shape); cands.append((float(chi[p, h]), du, dd, p, h))
cands.sort()
res = []
for (chi7, du, dd, p, h) in cands[:70]:
    k, re_t, im_t = I["tasks"][p]; a, b, _ = zfc.LINES[k]; hor = I["hors"][h]
    M = rbs.channels(re_t, im_t, a, b)
    hu = zfc.direction(du, re_t, im_t); hd = zfc.direction(dd, re_t, im_t)
    if LEAD[du] == "St": hu = np.conj(hu)
    if LEAD[dd] == "St": hd = np.conj(hd)
    res.append({"up": du, "down": dd, "line": I["lines"][k], "tau": [re_t, im_t], "hor": hor, "chi2_7": round(chi7, 2), **nine_of(M, hor, hu, hd)})
res.sort(key=lambda r: r["chi2_nine"])
for r in res[:14]:
    print(json.dumps(r))
