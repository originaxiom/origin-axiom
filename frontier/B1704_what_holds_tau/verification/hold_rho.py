"""B1704 (P-251): the third family -- B1686's contents (a)-(c) plus n complex scalars in the matter's representation
(W = +2 each in PH2's shape, the sign opposite to the matter's Weyl fermions), n up to 1499.  Minima of V = -F on
Re tau = 0 and 1/2; the n that put a minimum in the band 2.1 <= y <= 3.2; for representative band cases, the 2D kind of
the critical point (the curvatures in Re tau and Im tau).  No data.
    python3 -B hold_rho.py      # writes hold_rho.json beside itself"""
import io, json, contextlib, importlib.util, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("hold", HERE / "hold.py"); H = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(H)
W = H.W
def V(c, t):
    tot = 0.0
    for k, w in c.items():
        if k == ("m",): tot += w * (31 / 1024) * (W.E_cs(t, 3) - W.E_cs(t, 2))
        elif k == (0.0, 0.0): tot += w * W.E_cs(t, 3)
        else: tot += w * W.S_c(t, k)
    return -tot
out = {}
for name, c0 in H.CONT.items():
    rows, flip = [], None
    for n in range(1, 1500):
        c = dict(c0); c[("m",)] = c[("m",)] - 2 * n
        if flip is None and H.cusp(c) < 0: flip = n
        mins = {}
        for re_t in (0.0, 0.5):
            v = -H.F(c, re_t); d = np.diff(v)
            mins[re_t] = [float(H.ys[i + 1]) for i in range(len(d) - 1) if d[i] < 0 <= d[i + 1]]
        if any(2.1 <= y <= 3.2 for m in mins.values() for y in m):
            rows.append({"n": n, "cusp": H.cusp(c), "minima_Re0": mins[0.0], "minima_Re1/2": mins[0.5]})
    kinds = []
    for r in (rows[0], rows[len(rows) // 2], rows[-1]) if rows else ():
        c = dict(c0); c[("m",)] -= 2 * r["n"]
        for re0, key in ((0.0, "minima_Re0"), (0.5, "minima_Re1/2")):
            for y in r[key]:
                t = complex(re0, y); h = 0.03
                vx = (V(c, t + h) + V(c, t - h) - 2 * V(c, t)) / h ** 2; vy = (V(c, t + 1j * h) + V(c, t - 1j * h) - 2 * V(c, t)) / h ** 2
                kinds.append({"n": r["n"], "Re": re0, "y": y, "d2V_dx2": vx, "d2V_dy2": vy, "minimum": bool(vx > 0 and vy > 0)})
    out[name] = {"cusp_flips_at_n": flip, "band_rows": rows, "kinds": kinds}
    print(name, "flip at", flip, "; band n", (rows[0]["n"], rows[-1]["n"]) if rows else None, "; kinds", [(k["n"], k["Re"], k["y"], k["minimum"]) for k in kinds])
json.dump(out, open(HERE / "hold_rho.json", "w"), indent=1)
