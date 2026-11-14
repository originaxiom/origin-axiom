"""T-check with the channel residues from B1906's closed form (theta constants at 30 digits) in place of the frame's
numpy contour residues; SVDs in double precision first, then (option --mp) the coupling's SVDs at 50 digits too."""
import sys, pathlib, time
import numpy as np, mpmath as mp
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
EB = next((ROOT / "frontier").glob("B1932_*")) / "verification"
sys.path.insert(0, str(EB)); _a = sys.argv; sys.argv = ["x"]
import fiber_grid_t90 as G
sys.argv = _a
B = G.Bm
mp.mp.dps = 30
I = mp.mpc(0, 1); H = mp.mpf(1) / 2
def residues_closed(x, yy, t):
    tt = mp.mpc(t.real, t.imag)
    x0, x1 = mp.mpf(x[0]), mp.mpf(x[1]); y0, y1 = mp.mpf(yy[0]), mp.mpf(yy[1])
    ap, am = x0 + y0, x0 - y0; bp, bm = (x1 + y1) / 2, (x1 - y1) / 2
    e = mp.exp(-2 * I * mp.pi * x0)
    kap = {"1": -I * e, "i": mp.mpf(-1), "j": -e, "k": I}
    cs = {"1": (ap + H, bp + H), "i": (ap + H, bp), "j": (ap, bp + H), "k": (ap, bp)}
    ds = {"1": (am + H, bm + H), "i": (am + H, bm), "j": (am, bm + H), "k": (am, bm)}
    eta = mp.exp(I * mp.pi * tt / 12) * mp.qp(mp.exp(2 * I * mp.pi * tt))
    t1p = 2 * mp.pi * eta ** 3
    return {s: complex(kap[s] * B.thc_mp(*cs[s], 0, tt) * B.thc_mp(*ds[s], 0, tt) / t1p) for s in B.UNITS}
# check against the contour at a modest height first
xx, yy = B.sector_twists(0.4 * complex(0.13, 1.5) + 0.8, complex(0.13, 1.5), B.SIXY["Q"] if "Q" in B.SIXY else 1, B.SIXY.get("u", -4))
Rn = B.residues(xx, yy, complex(0.13, 1.5)); Rc = residues_closed(xx, yy, complex(0.13, 1.5))
print("closed vs contour at y = 1.5:", max(abs(Rn[s] - Rc[s]) for s in B.UNITS) / max(abs(Rn[s]) for s in B.UNITS), flush=True)
B.residues = residues_closed
if "--mp" in sys.argv:
    exec(open(str(pathlib.Path(__file__).resolve().parent / "svd_alone_does_not_repair.py")).read().split("KW = ")[0].split("mp.mp.dps = 50")[1].replace("COV = G.C", ""))
KW = ["up|L_2|St", "down|L_2|S", "ckm|L_2|St|S"]
for y in [6, 9, 12, 15, 20, 30, 45]:
    t0 = time.time(); rows = []
    for x in (0.13, 1.13, -0.31):
        f = G.fbar_t90(complex(x, y)); rows.append(np.concatenate([np.array(f[k]) for k in KW]))
    rows = np.array(rows)
    td = np.max(np.abs(rows[0] - rows[1]) / np.maximum(np.abs(rows[0]), 1e-300)); xd = np.max(np.abs(rows[0] - rows[2]) / np.maximum(np.abs(rows[0]), 1e-300))
    print("y %5.1f  T-check %.1e  x-variation %.1e  W- seven: %s  (%.0f s)" % (y, td, xd, " ".join("%.4g" % v for v in rows[0]), time.time() - t0), flush=True)
