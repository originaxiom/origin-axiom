"""Referee P-406, r4: robustness of r3's tau = i, 2-torsion-line values (DR at the canonical ends) to the
quadrature and residue settings of B1656's functions; and the same at the S-image point -1/tau (= i) via a
nearby point check tau = i*(1+1e-4) for continuity.  Exploratory, read-only reuse."""
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
def ratios(t, L, w, rad=0.01, N=256, eps=1e-5, nth=96, ns=64):
    x, yy = B.sector_twists(w, t, 1, -4)
    R = B.residues(x, yy, t, rad=rad, N=N); c = B.cA(x, yy, t, R, eps=eps, nth=nth, ns=ns)
    a = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    S = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    sv = np.linalg.svd(B.coupling(S, B.weighted_M(u)), compute_uv=False)
    return float(sv[2] / sv[0]), float(sv[1] / sv[0])
out = {}
Lmax, L2 = 0.688385709056232, 2.7192576281085956
for label, kw in [("default", {}), ("rad .02 N 512", {"rad": 0.02, "N": 512}), ("eps 1e-6 nth 144 ns 96", {"eps": 1e-6, "nth": 144, "ns": 96})]:
    for Ln, L in [("L_max", Lmax), ("L_2", L2)]:
        t = 1j; w = B.line_w(0.5, 0.5, t)
        r = ratios(t, L, w, **kw)
        out[f"{label} {Ln}"] = r
        print(f"{label:24s} {Ln}: m1/m3={r[0]:.8e} m2/m3={r[1]:.8f}", flush=True)
t = 1j * (1 + 1e-4); w = B.line_w(0.5, 0.5, t)
r = ratios(t, L2, w); out["near i, L_2"] = r
print(f"tau = i(1+1e-4), L_2: m1/m3={r[0]:.8e} m2/m3={r[1]:.8f}")
json.dump(out, open(pathlib.Path(__file__).with_suffix('.json'), 'w'), indent=1)
