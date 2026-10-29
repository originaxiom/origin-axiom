"""Main's own check of the reader's claim (audit/drafts/t2/WP_AT_SOURCE.md): B1667's accessory parameter c(tau) (its sealed
instrument, imported unchanged) is a primitive of the Weil-Petersson form: with C = 2c, dC/d(tau-bar) = i h_WP, where
h_WP = (1/2)|d(l, t)/d(Re tau, Im tau)| from the Fenchel-Nielsen coordinates of the a-curve (l = 2 arccosh(x/2), x = |tr A_a|;
t = 2 arcsinh((2z - x y)/(2x)), y = |tr A_b|, z = |tr A_a A_b|).  Central differences, step h, at four points off Re tau = 0
(where the instrument's Newton is degenerate); warm starts from the centre.  Reported: Re and Im of dC/d(tau-bar), the FN
Jacobian route, their ratio, the predicted cusp form (pi^2/2)/(y + 4 ln2/pi)^3, the hyperbolic (pi/4)/y^2, and c itself."""
import importlib.util, json, math, pathlib, numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sp = importlib.util.spec_from_file_location("cc", ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.py")
cc = importlib.util.module_from_spec(sp); sp.loader.exec_module(cc)
def solve(tau, c0):
    c, f = cc.solve_accessory(tau, c0=c0); assert np.max(np.abs(f)) < 1e-9, (tau, f); return c
def fn(tau, c):
    _, _, Aa, Ab = cc.monodromy(tau, c); x, y, z = (abs(v) for v in cc.traces(Aa, Ab))
    return 2 * math.acosh(x / 2), 2 * math.asinh((2 * z - x * y) / (2 * x))
out = {}
delta = 4 * math.log(2) / math.pi
STORED = [((q["tau"][0], q["tau"][1]), complex(*q["c"])) for q in json.loads((ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json").read_text())["points"]]
def warm(tau):
    """the true root (B1667's continuation and uniformisation check), by continuation from B1667's nearest stored point"""
    (x0, y0), c = min(STORED, key=lambda s: abs(complex(*s[0]) - tau))
    start = complex(x0, y0); n = max(1, int(abs(tau - start) / 0.05))
    for k in range(1, n + 1): c = solve(start + (tau - start) * k / n, c)
    return c
for tau in (0.25 + 1.2j, 0.25 + 2.0j, 0.15 + 3.0j, 0.3 + 5.0j):
    h = 1e-4 * tau.imag
    c0 = warm(tau)
    pts = {k: tau + d for k, d in (("xp", h), ("xm", -h), ("yp", 1j * h), ("ym", -1j * h))}
    cs = {k: solve(v, c0) for k, v in pts.items()}
    C = {k: 2 * v for k, v in cs.items()}
    dCdx = (C["xp"] - C["xm"]) / (2 * h); dCdy = (C["yp"] - C["ym"]) / (2 * h)
    dCdtb = 0.5 * (dCdx + 1j * dCdy)
    F = {k: fn(pts[k], cs[k]) for k in pts}
    J = np.array([[(F["xp"][0] - F["xm"][0]) / (2 * h), (F["yp"][0] - F["ym"][0]) / (2 * h)],
                  [(F["xp"][1] - F["xm"][1]) / (2 * h), (F["yp"][1] - F["ym"][1]) / (2 * h)]])
    hfn = 0.5 * abs(np.linalg.det(J)); y = tau.imag
    out[str(tau)] = {"c": [c0.real, c0.imag], "dC/dtaubar": [dCdtb.real, dCdtb.imag], "Im dC/dtaubar / FN route": dCdtb.imag / hfn,
                     "|Re| / |dC/dtaubar|": abs(dCdtb.real) / abs(dCdtb), "h_WP (FN route)": hfn,
                     "cusp form (pi^2/2)/(y+delta)^3": (math.pi ** 2 / 2) / (y + delta) ** 3, "hyperbolic (pi/4)/y^2": (math.pi / 4) / y ** 2}
    print(str(tau), json.dumps(out[str(tau)]), flush=True)
out["pi^2/12 (the predicted cusp limit of c)"] = math.pi ** 2 / 12
# control: Newton from c = 0 (no continuation) lands on another real-holonomy root at 0.15 + 3i; the same two routes there
tau = 0.15 + 3.0j; h = 1e-4 * tau.imag; c0 = solve(tau, 0j)
pts = {k: tau + d for k, d in (("xp", h), ("xm", -h), ("yp", 1j * h), ("ym", -1j * h))}
cs = {k: solve(v, c0) for k, v in pts.items()}; C = {k: 2 * v for k, v in cs.items()}
dCdtb = 0.5 * ((C["xp"] - C["xm"]) / (2 * h) + 1j * (C["yp"] - C["ym"]) / (2 * h))
F = {k: fn(pts[k], cs[k]) for k in pts}
J = np.array([[(F["xp"][0] - F["xm"][0]) / (2 * h), (F["yp"][0] - F["ym"][0]) / (2 * h)],
              [(F["xp"][1] - F["xm"][1]) / (2 * h), (F["yp"][1] - F["ym"][1]) / (2 * h)]])
hfn = 0.5 * abs(np.linalg.det(J))
out["control: root from c = 0 at 0.15+3j (not the uniformisation)"] = {"c": [c0.real, c0.imag], "Im dC/dtaubar / FN route": dCdtb.imag / hfn,
    "|Re| / |dC/dtaubar|": abs(dCdtb.real) / abs(dCdtb), "h (FN route of this root's holonomy)": hfn, "true root's h_WP": out["(0.15+3j)"]["h_WP (FN route)"]}
print("control", json.dumps(out["control: root from c = 0 at 0.15+3j (not the uniformisation)"]), flush=True)
(pathlib.Path(__file__).with_suffix(".json")).write_text(json.dumps(out, indent=1))
