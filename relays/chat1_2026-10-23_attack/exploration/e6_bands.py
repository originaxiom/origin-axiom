"""POST HOC exploration, labelled: the stored diagonal aligned rows (each direction in its null-led reading in every
sector) by Im tau band: the best chi2_nine, its parts, and V_us there."""
import json, math, pathlib, subprocess
import numpy as np
exec(open(pathlib.Path(__file__).resolve().parent / "e_common.py").read().split("def nine_of")[0])
ZF = ROOT / "relays/chat1_2026-10-23_zero_free_frame"
I = json.loads((ZF / "zero_free_census_index.json").read_text())
X = np.load(ZF / "zero_free_census.npz")["data"].astype(np.float64)
DIRS = I["dirs"]; fi = {f: i for i, f in enumerate(I["fields"])}
LEAD = {"dR": "St", "F_10": "St", "F_18": "St", "F_26": "St", "F_6": "S", "F_14": "S", "F_22": "S"}
im = np.array([t[2] for t in I["tasks"]])
for d, rd in LEAD.items():
    g = lambda f: X[:, DIRS.index(d), :, fi[f]]
    L9 = np.stack([g(f"log10 up m2/m3 {rd}"), g(f"log10 up m1/m3 {rd}"), g(f"log10 down m2/m3 {rd}"), g(f"log10 down m1/m3 {rd}"),
                   g(f"log10 lep m2/m3 {rd}") + math.log10(3), g(f"log10 lep m1/m3 {rd}") - math.log10(3)], axis=-1) * math.log(10)
    V = np.stack([g(f"Vus {rd}|{rd}"), g(f"Vcb {rd}|{rd}"), g(f"Vub {rd}|{rd}")], axis=-1)
    L9 = np.concatenate([L9, np.log(np.maximum(V, 1e-300))], axis=-1)
    chi9 = np.sum(((L9 - T9) / SIG) ** 2, axis=-1); chi6 = np.sum(((L9[..., :6] - T6) / SIG[:6]) ** 2, axis=-1)
    line = f"{d:5s}"
    for lo, hi in ((1.5, 2.0), (2.0, 2.3), (2.3, 2.6), (2.6, 3.0), (3.0, 3.6)):
        msk = (im >= lo) & (im < hi)
        c = np.where(msk[:, None], chi9, np.inf); p, h = np.unravel_index(int(np.argmin(c)), c.shape)
        r = np.exp(L9[p, h] - T9)
        line += f" | {lo}-{hi}: nine {chi9[p,h]:6.1f} six {chi6[p,h]:5.1f} Vus {r[6]:.2f} Vcb {r[7]:.2f} Vub {r[8]:.2f}"
    print(line)
