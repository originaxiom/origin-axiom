"""Referee R8: which draws make the data 'typical' under D1?  The A1 unforced draws at least as isolated as the data
(own nearest distance >= the data's 11.2 sigma): their heights (Im tau > 4: B1667's radii held, not interpolated), their
smallest ratio, and whether they lie near the data at all."""
import json, pathlib, sys
import numpy as np
from scipy.spatial import cKDTree
HERE = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import r3_independent as R
t6, s6, _, _ = R.target(); arms = R.load_census(); cf = R.cfg_seq()
rows = []; X = []
for r, (h, ru, rd, rl) in zip(arms["A1"], cf):
    v = R.six(r, h, ru, rd, rl, 1)
    if v is None or not all(x > 1e-12 for x in v): continue
    rows.append(r); X.append(np.log(v))
X = np.array(X); im = np.array([r["Im_tau"] for r in rows])
d, _ = cKDTree(X / s6).query(X / s6, k=2, p=np.inf); d = d[:, 1]
dd = cKDTree(X / s6).query(t6 / s6, k=1, p=np.inf)[0]
iso = d >= dd; out = {"data d": float(dd), "n draws as isolated as the data": int(iso.sum()), "n": len(X),
      "share of them with Im tau > 4 (radii held)": float(np.mean(im[iso] > 4)), "share of all resolved with Im tau > 4": float(np.mean(im > 4)),
      "share of them with min ratio < 1e-8": float(np.mean(X[iso].min(1) < np.log(1e-8))), "share of them with min ratio < 1e-6 (below the data's least ratio, 7.3e-6)": float(np.mean(X[iso].min(1) < np.log(1e-6))),
      "median Im tau of them": float(np.median(im[iso])), "median Im tau, all": float(np.median(im)),
      "their distance from the data: median, min (sigma)": [float(np.median(np.abs(X[iso] - t6).max(1) / s6.max())), float((np.abs(X[iso] / s6 - t6 / s6)).max(1).min())],
      "data's least ratio": float(np.exp(t6.min()))}
# what the data's nearest unforced world misses, as factors
j = int(np.argmin(np.abs(X / s6 - t6 / s6).max(1))); out["nearest world: model/measured factors"] = np.exp(X[j] - t6).tolist(); out["nearest world Im tau"] = float(im[j])
print(json.dumps(out, indent=1)); (HERE / "r8_out.json").write_text(json.dumps(out, indent=1))
