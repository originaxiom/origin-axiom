"""Data-free exploration (labelled; run before the reading test's rule was sealed, disclosed there): at the two
pre-scan points (reading_prescan2_weights.npz, all 266 lines, both horocycles), with reading_prescan2's directions,
under the Standard Model's reading: for the directions with an up hierarchy (m2/m3 <= 0.015, m1/m3 <= 1e-4), the
heaviest left states' bilinear self-products |l3.l3| (0 on a null line, 1 for a real vector) in the up and down sectors,
|V_tb| = |<l3_u, l3_d>|, and the same restricted to the directions where |V_ud| > 0.9."""
import importlib.util, sys, json, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parents[1]
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("p2", HERE / "reading_prescan2.py"); p2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(p2)
W = np.load(HERE / "reading_prescan2_weights.npz")["W"]
HS = p2.HS
acc = {"hier": [], "hier & Vud>0.9": []}
for i in range(W.shape[0]):
    for ih in range(2):
        up, dn = W[i, 0, ih], W[i, 1, ih]
        Uu, su, _ = np.linalg.svd(p2.Ybatch(up, np.conj(HS))); Ud, sd, _ = np.linalg.svd(p2.Ybatch(dn, HS))
        hier = (su[:, 1] / su[:, 0] <= 1.5e-2) & (su[:, 2] / su[:, 0] <= 1e-4)
        if not hier.any():
            continue
        l3u, l3d = Uu[:, :, 0], Ud[:, :, 0]; l1u, l1d = Uu[:, :, 2], Ud[:, :, 2]
        nu = np.abs(np.einsum("ni,ni->n", l3u, l3u)); nd = np.abs(np.einsum("ni,ni->n", l3d, l3d))
        vtb = np.abs(np.einsum("ni,ni->n", np.conj(l3u), l3d)); vud = np.abs(np.einsum("ni,ni->n", np.conj(l1u), l1d))
        for key, m in (("hier", hier), ("hier & Vud>0.9", hier & (vud > 0.9))):
            if m.any():
                acc[key].append([np.median(nu[m]), np.median(nd[m]), np.median(vtb[m]), np.max(vtb[m]), m.sum()])
out = {}
for k, v in acc.items():
    a = np.array(v)
    out[k] = {"rows": len(a), "median over rows of the median |l3_u.l3_u|": float(np.median(a[:, 0])), "... |l3_d.l3_d|": float(np.median(a[:, 1])),
              "... |V_tb|": float(np.median(a[:, 2])), "largest |V_tb| over rows": float(a[:, 3].max()),
              "rows whose median |l3_u.l3_u| < 0.1, and |l3_d.l3_d| < 0.1": [int((a[:, 0] < 0.1).sum()), int((a[:, 1] < 0.1).sum())]}
print(json.dumps(out, indent=1))
