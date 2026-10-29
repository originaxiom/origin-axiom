"""Referee P-406, r1: Theorem B's dichotomy at the forced points, tested at the canonical end (finite L).
Reuses B1691's S164 correction machinery verbatim (B1656's four-channel coupling, b1656_funcs.py, and B1691's
sections), read-only.  Section: a = DR, the unique weight-3/2 covariant section (H-cov; no free coefficient).
Points: tau = i (Theorem A's point), tau = omega, and a control; L at B1667's two canonical horocycles at i
(L_max = 0.688385709056232, L_2 = 2.7192576281085956, from B1667's json) and a sweep."""
import sys, io, contextlib, importlib.util, pathlib, math, json, glob
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[3]
C = pathlib.Path(glob.glob(str(ROOT / 'B1691_*/verification/correction'))[0])
sys.path.insert(0, str(C)); sys.path.insert(0, str(C.parent)); sys.argv = ['x']
import b1656_funcs as B
spec = importlib.util.spec_from_file_location("te", C.parent / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
import mpmath as mp
mp.mp.dps = 40
def ratios(t, L, which=1):
    x, yy = B.sector_twists(0, t, 1, -4)
    R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
    a = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[which]]
    S = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    sv = np.linalg.svd(B.coupling(S, B.weighted_M(u)), compute_uv=False)
    return float(sv[2] / sv[0]), float(sv[1] / sv[0]), [abs(z) for z in a]
out = {}
omega = complex(0.5, math.sqrt(3) / 2)   # B1667's control e^{i pi/3}, PSL(2,Z)-equivalent to omega
pts = {"i": 1j, "e^{i pi/3}": omega, "control 0.25+1.3i": complex(0.25, 1.3)}
Ls = {"L_max(i)": 0.688385709056232, "L_2(i)": 2.7192576281085956, "0.65": 0.65, "10": 10.0, "160": 160.0}
for name, t in pts.items():
    out[name] = {}
    for ln, L in Ls.items():
        m13, m23, a = ratios(t, L)
        out[name][ln] = {"m1/m3": m13, "m2/m3": m23}
        print(f"{name:20s} L={ln:9s} m1/m3={m13:.6e}  m2/m3={m23:.10f}", flush=True)
json.dump(out, open(pathlib.Path(__file__).with_suffix('.json'), 'w'), indent=1)
