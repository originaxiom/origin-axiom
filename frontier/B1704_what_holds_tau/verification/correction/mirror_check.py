"""B1704's correction (2026-10-22), checked on main after the SM seat's relay 197: is Re tau = 1/2 a mirror line of V?  dV/dx at B1704's
Re 1/2 'minima'; the true minima of V for trivial-fermion contents on a 2D grid of the theta group's domain."""
import io, json, contextlib, importlib.util, math, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("hold", A / "hold.py"); H = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(H)
W = H.W
def V(c, t):
    tot = 0.0
    for k, w in c.items():
        if k == ("m",): tot += w * (31 / 1024) * (W.E_cs(t, 3) - W.E_cs(t, 2))
        elif k == (0.0, 0.0): tot += w * W.E_cs(t, 3)
        else: tot += w * W.S_c(t, k)
    return -tot
out = {"mirror_pairs": {}, "dVdx_at_B1704_Re_half": {}, "grid_minima": {}}
c3 = dict(H.CONT["(a)"]); c3[(0.0, 0.0)] = c3.get((0.0, 0.0), 0) - 2 * 3
for x0 in (0.0, 0.5, 1.0):
    out["mirror_pairs"][str(x0)] = max(abs(V(c3, complex(x0 + 0.1, y)) - V(c3, complex(x0 - 0.1, y))) for y in (1.2, 1.6, 2.5))
h = 1e-4
for name, n, y in (("(a)", 3, 1.02), ("(a)", 5, 0.94), ("(c)", 17, 1.05)):
    c = dict(H.CONT[name]); c[(0.0, 0.0)] = c.get((0.0, 0.0), 0) - 2 * n
    t = complex(0.5, y); out["dVdx_at_B1704_Re_half"]["%s+%d y=%.2f" % (name, n, y)] = (V(c, t + h) - V(c, t - h)) / (2 * h)
for name, n in (("(a)", 3), ("(a)", 8), ("(c)", 17), ("(c)", 25)):
    c = dict(H.CONT[name]); c[(0.0, 0.0)] = c.get((0.0, 0.0), 0) - 2 * n
    xs = np.round(np.arange(-0.02, 1.0201, 0.02), 3); ys = np.round(np.arange(0.84, 3.0001, 0.02), 3)
    G = np.full((len(xs), len(ys)), np.nan)
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            if x * x + y * y >= 1 - 1e-9 and (x - 1) ** 2 + y * y >= 1 - 1e-9: G[i, j] = V(c, complex(x, y))
    mins = []
    for i in range(1, len(xs) - 1):
        for j in range(1, len(ys) - 1):
            v = G[i, j]
            nb = G[i - 1:i + 2, j - 1:j + 2]
            if not np.isnan(v) and np.nanmin(nb) == v and np.sum(~np.isnan(nb)) >= 6: mins.append((float(xs[i]), float(ys[j]), float(v)))
    gi = np.nanargmin(G); i, j = np.unravel_index(gi, G.shape)
    out["grid_minima"]["%s+%d" % (name, n)] = {"interior_local_minima": mins, "grid_minimum": [float(xs[i]), float(ys[j]), float(G[i, j])],
                                               "on_the_unit_arc": abs(math.hypot(xs[i], ys[j]) - 1) < 0.03 or abs(math.hypot(xs[i] - 1, ys[j]) - 1) < 0.03}
json.dump(out, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
print(json.dumps(out, indent=1))
