"""The decisive form of the criterion (written before the run): along the bottom arc |tau| = 1 the two smallest |c_gamma|
tie (their gap above the arc is proportional to the distance). The invariant end L~ = L + 1/2 log Im tau - (gamma + log pi)
is symmetric under the inversion r -> 1/r across the arc (S composed with the mirror). It is smooth across the arc only if
its radial slope there is zero: L~(r) - L~(1) ~ (r - 1)^2 (ratio 4 between r - 1 = 0.02 and 0.01) for a smooth end, ~ |r - 1|
(ratio 2) for a corner. EXPECTATION: L_max has the corner (ratio near 2) and L_2 does not (ratio near 4)."""
import json, math, pathlib, sys
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import smoothness as SM
C = 0.5772156649015329 + math.log(math.pi)
G = json.loads((HERE / "grid.json").read_text())["grid"]
out = {}
for theta_deg in (80.0, 70.0):
    th = math.radians(theta_deg)
    pts = {dr: complex((1 + dr) * math.cos(th), (1 + dr) * math.sin(th)) for dr in (0.04, 0.02, 0.01, 0.0)}
    seed = min((p for p in G if "c" in p), key=lambda p: abs(complex(*p["tau"]) - pts[0.04]))
    tau, c = complex(*seed["tau"]), complex(*seed["c"])
    vals = {}
    for dr in (0.04, 0.02, 0.01, 0.0):
        c, res = SM.CC.newton_walk(tau, c, pts[dr]); tau = pts[dr]
        lm, l2, gap = SM.ends_and_gap(tau, c)
        vals[dr] = (lm + 0.5 * math.log(tau.imag) - C, l2 + 0.5 * math.log(tau.imag) - C, gap)
    for i, name in ((0, "L_max"), (1, "L_2")):
        d1, d2, d4 = (vals[d][i] - vals[0.0][i] for d in (0.01, 0.02, 0.04))
        print("theta %.0f deg, %s: ratios %.2f (0.01 to 0.02), %.2f (0.02 to 0.04); gap on the arc %.1e"
              % (theta_deg, name, d2 / d1, d4 / d2, vals[0.0][2]), flush=True)
    out[str(theta_deg)] = {str(k): list(v) for k, v in vals.items()}
(HERE / "arc_corner.json").write_text(json.dumps(out, indent=1))
