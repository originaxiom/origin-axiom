"""Data-free read of the committed census: V_cb's spread over the null-led directions, restricted to hierarchical rows."""
import json, math, pathlib
import numpy as np
ZF = pathlib.Path(__file__).resolve().parents[2] / "chat1_2026-10-23_zero_free_frame"
I = json.loads((ZF / "zero_free_census_index.json").read_text())
X = np.load(ZF / "zero_free_census.npz")["data"].astype(np.float64)
DIRS = I["dirs"]; fi = {f: i for i, f in enumerate(I["fields"])}
LEAD = {"dR": "St", "F_2": "St", "F_10": "St", "F_18": "St", "F_26": "St", "F_6": "S", "F_14": "S", "F_22": "S"}
im = np.array([t[2] for t in I["tasks"]])
vcb = np.stack([X[:, DIRS.index(d), :, fi[f"Vcb {LEAD[d]}|{LEAD[d]}"]] for d in LEAD], axis=-1)
up2 = np.stack([X[:, DIRS.index(d), :, fi[f"log10 up m2/m3 {LEAD[d]}"]] for d in LEAD], axis=-1)
dn2 = np.stack([X[:, DIRS.index(d), :, fi[f"log10 down m2/m3 {LEAD[d]}"]] for d in LEAD], axis=-1)
hier = (up2.max(-1) < -1.5) & (dn2.max(-1) < -1.0) & (vcb.min(-1) > 1e-3)
sp = np.log(vcb.max(-1) / vcb.min(-1))
for lo, hi in ((2.0, 2.5), (2.5, 3.0), (3.0, 3.5), (3.5, 4.01)):
    m = hier & ((im >= lo) & (im < hi))[:, None]
    print(f"Im tau {lo}-{hi}: hierarchical rows {m.sum():6d} of {(((im >= lo) & (im < hi))[:, None] & np.ones((1, 2), bool)).sum()}; V_cb max/min over 8 null-led Higgs: median {math.exp(np.median(sp[m])):.3f}, 90% {math.exp(np.quantile(sp[m], 0.9)):.3f}, 99% {math.exp(np.quantile(sp[m], 0.99)):.3f}")
# excluding the exactly-null F_2 and DR (the two with e1 admixture)
sub = [i for i, d in enumerate(LEAD) if d not in ("F_2", "dR")]
sp2 = np.log(vcb[..., sub].max(-1) / vcb[..., sub].min(-1))
m = hier & (im >= 2.5)[:, None]
print(f"zero-free a >= 6 only, Im tau >= 2.5: median {math.exp(np.median(sp2[m])):.4f}, 90% {math.exp(np.quantile(sp2[m], 0.9)):.4f}")
