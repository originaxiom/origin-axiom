"""B1694 (P-242): the parameter-free curve. The weight-3/2 section DR (unique; B1691) as the Higgs in M, no line, at the
canonical end (B1667's two horocycles, L_max(Im tau) and L_2(Im tau) interpolated from B1667's stored column Re tau = 0.25;
L's Re tau dependence is below 1e-3 there), with B1656's four-channel coupling (u_s = sqrt(2 pi L + c_s) R_s; functions
copied verbatim): m2/m3 and m1/m3 as functions of tau on the CP lines Re tau = 0 and 1/2.  Mathematics only; no data.
    python3 -B the_curve.py      # writes the_curve.json beside itself"""
import sys, io, json, math, contextlib, importlib.util, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(HERE)); sys.argv = ['x']
import b1656_funcs as B
P1691 = ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
sys.path.insert(0, str(P1691))
spec = importlib.util.spec_from_file_location("te", P1691 / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
import mpmath as mp
col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.load(open(ROOT / "frontier" / "B1667_the_canonical_cusp" / "verification" / "the_canonical_cusp.json"))["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
Y, LM, L2 = [c[0] for c in col], [c[1] for c in col], [c[2] for c in col]
def L_of(y, which):
    arr = LM if which == "L_max" else L2
    return float(np.interp(y, Y, arr)) if y <= Y[-1] else arr[-1]
def masses(tau, L):
    t = complex(tau); x, yy = B.sector_twists(0, t, 1, -4)
    R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
    a = [complex(te.ev(cc, mp.mpc(tau.real, tau.imag))) for cc in te.B[1]]
    S = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    sv = np.linalg.svd(B.coupling(S, B.weighted_M(u)), compute_uv=False)
    return float(sv[1] / sv[0]), float(sv[2] / sv[0])
out = {"L_column_Re_tau_0.25": col, "curves": {}}
ys = [round(1.2 + 0.1 * k, 2) for k in range(25)]
for re_t in (0.0, 0.5):
    for which in ("L_max", "L_2"):
        pts = []
        for y in ys:
            r2, r1 = masses(complex(re_t, y), L_of(y, which)); pts.append({"Im_tau": y, "L": L_of(y, which), "m2/m3": r2, "m1/m3": r1})
        out["curves"]["Re%.1f_%s" % (re_t, which)] = pts
        print(re_t, which, [(p["Im_tau"], "%.3g" % p["m2/m3"], "%.3g" % p["m1/m3"]) for p in pts[::6]], flush=True)
if __name__ == "__main__":
    json.dump(out, open(HERE / "the_curve.json", "w"), indent=1)
