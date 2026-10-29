"""Referee P-406, r3: tau = i with the 2-torsion lines (S permutes or fixes them) and tau = e^{i pi/3} with 3-torsion
lines; DR at L_2(i).  Same machinery as r1/r2.  Exploratory: Theorem B's scope (B1645/B1646: zero Wilson line)."""
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
def ratios(t, L, w, ql=1, qr=-4):
    x, yy = B.sector_twists(w, t, ql, qr)
    R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
    a = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    S = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    sv = np.linalg.svd(B.coupling(S, B.weighted_M(u)), compute_uv=False)
    return float(sv[2] / sv[0]), float(sv[1] / sv[0])
out = {}
L = 2.7192576281085956
for t, nm in [(1j, "i"), (complex(0.5, math.sqrt(3)/2), "e^{i pi/3}")]:
    for p in [(0.5, 0.5), (0.5, 0.0), (0.0, 0.5), (1/3, 1/3), (1/3, 2/3), (0.1, 0.3)]:
        w = B.line_w(p[0], p[1], t)
        try:
            m13, m23 = ratios(t, L, w)
        except Exception as e:
            print(nm, p, "error", e); continue
        out[f"{nm} {p}"] = {"m1/m3": m13, "m2/m3": m23}
        print(f"tau={nm:10s} line={tuple(round(v,4) for v in p)}: m1/m3={m13:.6e} m2/m3={m23:.8f}", flush=True)
json.dump(out, open(pathlib.Path(__file__).with_suffix('.json'), 'w'), indent=1)
