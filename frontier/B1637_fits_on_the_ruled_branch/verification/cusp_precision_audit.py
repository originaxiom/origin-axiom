"""B1637 audit (2026-10-14, S125; not a seal): the growth of B1637's basis forms far up the tau line, confirming the SM seat's W79.  A holomorphic form tends to a constant;
a cusp-violating residual delta in the coefficients grows like delta |eta|^-18, slope 3 pi/2 per unit y in ln
(2.047 in log10).  Fit log10 |form| - log10 |form(y0)| at y = 8.5 ... 11."""
import pathlib, json
import numpy as np
path = pathlib.Path(__file__).resolve().parents[2] / "B1637_fits_on_the_ruled_branch" / "verification" / "fits_on_the_ruled_branch.py"
src = open(path).read().split("def task(args):")[0]
ns = {"__file__": str(path), "__name__": "audit"}; exec(compile(src, "defs", "exec"), ns)
out = {}
for k in (3, 5, 7):
    hol, mons = ns["forms"](k)
    ys = [3.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0]; norms = []
    for y in ys:
        u, eta = ns["theta_eta"](complex(0.36, y))
        vals = np.array([u[0] ** m[0] * u[1] ** m[1] * u[2] ** m[2] for m in mons])
        norms.append([float(np.linalg.norm((bb @ vals) / eta ** 18)) for bb in hol])
    norms = np.array(norms)
    excess = np.log10(np.abs(norms[1:] - norms[0]) + 1e-300)          # growth over the y = 3 value
    slopes = [float(np.polyfit(ys[1:], excess[:, j], 1)[0]) for j in range(norms.shape[1])]
    # the implied residual delta at y: |form(y) - form(3)| / |eta|^-18
    deltas = [float(np.median(np.abs(norms[1:, j] - norms[0, j]) / np.array([abs(ns["theta_eta"](complex(0.36, y))[1]) ** -18 for y in ys[1:]]))) for j in range(norms.shape[1])]
    implied_at_6p8 = [d * abs(ns["theta_eta"](complex(0.36, 6.8))[1]) ** -18 / float(norms[0, j]) for j, d in enumerate(deltas)]
    out[k] = {"slopes_log10_per_unit_y": [round(s, 3) for s in slopes], "implied_relative_error_at_Im_tau_6.8": [float("%.2g" % x) for x in implied_at_6p8],
              "implied_relative_error_at_Im_tau_3.4": [float("%.2g" % (d * abs(ns["theta_eta"](complex(0.36, 3.4))[1]) ** -18 / float(norms[0, j]))) for j, d in enumerate(deltas)]}
out["expected_slope_log10_per_unit_y"] = round(float(1.5 * np.pi * np.log10(np.e)), 3)
print(json.dumps(out, indent=1))
