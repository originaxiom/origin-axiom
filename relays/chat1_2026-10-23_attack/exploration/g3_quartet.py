"""Data-free: is the 'quartet' (m2/m3 per sector, V_cb) set by the channel weights alone for any Higgs led by the same
null line?  Compare h0-led Higgs directions at the same (tau, line, horocycle)."""
import contextlib, importlib.util, io, sys, math, pathlib
import numpy as np
ZF = pathlib.Path(__file__).resolve().parents[2] / "chat1_2026-10-23_zero_free_frame"
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("zfc", ZF / "zero_free_census.py")
zfc = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(zfc)
rbs, B, tic = zfc.rbs, zfc.B, zfc.tic
f3 = np.array([0, 1, 1j]) / math.sqrt(2)
def h0_led(d, re_t, im_t):
    v = zfc.direction(d, re_t, im_t)
    if abs(np.vdot(f3, v)) < abs(np.vdot(np.conj(f3), v)):
        v = np.conj(v)
    return v
def null_h0():
    return f3.copy()
def ratios(M, hor, hu, hd):
    Yu = B.coupling(rbs.S_of(hu), M[("up", hor)]); Yd = B.coupling(rbs.S_of(hd), M[("down", hor)]); Ye = B.coupling(rbs.S_of(hd), M[("lep", hor)])
    out = []
    for Y in (Yu, Yd, Ye):
        s = np.linalg.svd(Y, compute_uv=False); out += [s[1] / s[0], s[2] / s[0]]
    return out + tic.ckm_left(Yu, Yd)
pts = [(0.5625, 2.6, 0.4, 0.1, "L_2"), (0.35, 3.05, 0.4, 0.1, "L_max"), (0.35, 2.65, 0.4, 0.5, "L_2"), (0.1, 2.2, 0.4, 0.8, "L_max"), (0.4, 2.0, 1/3, 1/6, "L_2")]
for (re_t, im_t, a, b, hor) in pts:
    M = rbs.channels(re_t, im_t, a, b)
    print(f"tau {re_t}+{im_t}i line ({a:.3f},{b:.3f}) {hor}")
    print("   Higgs (h0-led)   up m2/m3  down m2/m3  lep m2/m3 |  up m1/m3  down m1/m3  lep m1/m3 |  Vus     Vcb     Vub")
    for d in ("null f3", "F_6", "F_22", "F_14", "F_10", "F_2", "dR", "F_-2"):
        h = null_h0() if d == "null f3" else h0_led(d, re_t, im_t)
        r = ratios(M, hor, h, h)
        print(f"   {d:8s}        {r[0]:.3e}  {r[2]:.3e}  {r[4]:.3e} | {r[1]:.2e}  {r[3]:.2e}  {r[5]:.2e} | {r[6]:.4f} {r[7]:.4f} {r[8]:.5f}")
