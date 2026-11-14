"""The criterion at the mirror lines (written before the run): near Re tau = 0 and Re tau = 1/2 (mirror lines, where the
two smallest |c_gamma| may tie), L(x) - L(line) grows like |x| for a corner and like x^2 for a smooth (real-analytic)
function. Ratio r = [L(line + 2h) - L(line)] / [L(line + h) - L(line)]: 2 for a corner, 4 for smooth. Also the gap of the two
smallest |c| at the line. Both conventions, h = 0.01 and 0.02, at Im tau = 1.3 and 2.0."""
import json, pathlib, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import smoothness as SM
G = json.loads((HERE / "grid.json").read_text())["grid"]
out = {}
for y in (1.3, 2.0):
    for line, sgn in ((0.0, 1), (0.5, -1)):
        seed = min((p for p in G if "c" in p), key=lambda p: abs(complex(*p["tau"]) - complex(line + sgn * 0.05, y)))
        t0, c0 = complex(*seed["tau"]), complex(*seed["c"])
        vals = {}
        tau, c = t0, c0
        for h in (0.04, 0.02, 0.01, 0.0):
            tgt = complex(line + sgn * h, y)
            c, res = SM.CC.newton_walk(tau, c, tgt); tau = tgt
            vals[h] = SM.ends_and_gap(tau, c)
        for i, name in ((0, "L_max"), (1, "L_2")):
            d1, d2, d4 = (vals[h][i] - vals[0.0][i] for h in (0.01, 0.02, 0.04))
            r1 = d2 / d1 if abs(d1) > 1e-14 else float("nan"); r2 = d4 / d2 if abs(d2) > 1e-14 else float("nan")
            print("Im %.1f, the line Re = %.1f, %s: ratios %.2f (h 0.01 to 0.02), %.2f (0.02 to 0.04); gap of the two smallest |c| at the line %.1e"
                  % (y, line, name, r1, r2, vals[0.0][2]), flush=True)
        out["%s %s" % (y, line)] = {str(h): list(v) for h, v in vals.items()}
(HERE / "mirror_lines.json").write_text(json.dumps(out, indent=1))
