"""B1304 Q2 -- B915's crossing solver, adjudicated (DESIGN sealed 866bd71e). B915's curve_point solves g1(MU) = g2(MU) for sin^2 theta_W with
alpha_s HELD at 0.118, then solves g2(MU) = g3(MU) for alpha_s without re-solving the first equation; at two loops the running of g1, g2
depends on g3 through the off-diagonal beta matrix. Here: B915's own definitions are exec'd WITHOUT its output-overwriting scan; at every
archived two-loop curve point (B915's results.json) the FIRST UV equation's residual |x1 - x2|(MU) is re-evaluated with the archived final
alpha_s; the first-stage guess is varied (0.09, 0.15) at the archived d_min point; and a simultaneous two-equation solve gives the corrected
point. Predictions: max residual ~ 0.0268 (the audit seat's 0.02683971597), well above 1e-6; the guess moves the answer by > 1e-4."""
import json, math, os, sys
import numpy as np
from scipy.optimize import fsolve, brentq
HERE = os.path.dirname(os.path.abspath(__file__)); B915 = os.path.join(HERE, "..", "..", "B915_the_crossing")
src = open(os.path.join(B915, "crossing.py")).read()
defs = src.split("MUs = np.logspace")[0]                      # definitions only; the scan and the JSON write are not executed
g = {"__name__": "b915_defs", "__file__": os.path.join(B915, "crossing.py")}; exec(compile(defs, "crossing_defs", "exec"), g)
run, alphas_from, curve_point, MZ = g["run"], g["alphas_from"], g["curve_point"], g["MZ"]
res = json.load(open(os.path.join(B915, "results.json")))
MUs = res["curve_samples"]["MU"]; C2 = res["curve_samples"]["two_loop"]
fails = []
def check(label, ok):
    print(("  [PASS] " if ok else "  [FAIL] ") + label)
    if not ok: fails.append(label)
def residuals(MU, sw2, als):
    t = math.log(MU / MZ); x = run(alphas_from(sw2, als), t, True).y[:, -1]
    return float(x[0] - x[1]), float(x[1] - x[2])
r1s = []; r2s = []
for MU, (sw2, als) in zip(MUs, C2):
    if any(math.isnan(v) for v in (sw2, als)): continue
    r1, r2 = residuals(MU, sw2, als); r1s.append(abs(r1)); r2s.append(abs(r2))
print(f"  archived two-loop points: {len(r1s)}; max |x1 - x2| (the first UV equation, NOT re-solved) = {max(r1s):.11f}; max |x2 - x3| (the solved one) = {max(r2s):.2e}")
check("(a) the first UV equation is violated at the archived points: max residual in [0.02, 0.035] inverse-coupling units (the seat's 0.02683971597) and > 1e-6", 0.02 <= max(r1s) <= 0.035 and max(r2s) < 1e-6)
# the leak: vary the first-stage guess at the archived d_min point
MU0 = res["curve_2loop_at_dmin"]["MU_GeV"]; t0 = math.log(MU0 / MZ)
def curve_point_with_guess(MU, guess):
    t = math.log(MU / MZ)
    f_sw = lambda sw2: (lambda x: x[0] - x[1])(run(alphas_from(sw2, guess), t, True).y[:, -1])
    sw2 = brentq(f_sw, 0.18, 0.30, xtol=1e-12)
    f_as = lambda als: (lambda x: x[1] - x[2])(run(alphas_from(sw2, als), t, True).y[:, -1])
    return sw2, brentq(f_as, 0.06, 0.30, xtol=1e-12)
pts = {gs: curve_point_with_guess(MU0, gs) for gs in (0.118, 0.09, 0.15)}
print(f"  at MU = {MU0:.3e} GeV: (sw2, alpha_s) with first-stage guess 0.118 = {pts[0.118]}, 0.09 = {pts[0.09]}, 0.15 = {pts[0.15]}")
shift = max(max(abs(pts[gs][0] - pts[0.118][0]), abs(pts[gs][1] - pts[0.118][1])) for gs in (0.09, 0.15))
check("(b) the answer depends on the first-stage guess (max shift > 1e-4): the 0.118 is not an inert initial guess", shift > 1e-4)
# the corrected point: both UV equations simultaneously
def both(v):
    return residuals(MU0, v[0], v[1])
sol = fsolve(both, x0=list(pts[0.118]), xtol=1e-12); rr = both(sol)
print(f"  simultaneous solve at the same MU: (sw2, alpha_s) = ({sol[0]:.6f}, {sol[1]:.6f}); residuals {rr[0]:.2e}, {rr[1]:.2e}; B915's archived point ({res['curve_2loop_at_dmin']['sw2']:.6f}, {res['curve_2loop_at_dmin']['alpha_s']:.6f})")
check("(c) the simultaneous solve satisfies both equations to 1e-8 and differs from B915's archived point", max(abs(rr[0]), abs(rr[1])) < 1e-8 and (abs(sol[0] - res['curve_2loop_at_dmin']['sw2']) > 1e-5 or abs(sol[1] - res['curve_2loop_at_dmin']['alpha_s']) > 1e-5))
json.dump(dict(n_points=len(r1s), max_r1=max(r1s), max_r2=max(r2s), MU_dmin=MU0, points_by_guess={str(k): list(v) for k, v in pts.items()}, corrected=[float(sol[0]), float(sol[1])], corrected_residuals=list(rr), archived=res["curve_2loop_at_dmin"], fails=fails), open("b1304_b915_residual.json", "w"), indent=1)
print("Q2:", "PASS" if not fails else f"FAIL ({len(fails)})"); sys.exit(0 if not fails else 1)
