"""B1691's correction (2026-10-21): the first generation of a section without a D2R component (here DR) under B1656's
four-channel canonical end at finite L, with no line: m1/m3 falls like 1/L^2, not to zero at finite L; m2/m3 tends to
B1691's large-L value.  B1656's functions copied verbatim (b1656_funcs.py)."""
import sys, io, contextlib, importlib.util, pathlib, math, json
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent))
sys.argv = ['x']
import b1656_funcs as B
spec = importlib.util.spec_from_file_location("te", HERE.parent / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
import mpmath as mp
out = {}
for y in (1.5, 2.0, 2.5):
    t = complex(0, y); x, yy = B.sector_twists(0, t, 1, -4)
    R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
    a = [complex(te.ev(cc, mp.mpc(0, y))) for cc in te.B[1]]
    S = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    row = {}
    for L in (0.65, 2.5, 10, 40, 160, 640):
        u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
        sv = np.linalg.svd(B.coupling(S, B.weighted_M(u)), compute_uv=False)
        row[str(L)] = {"m1/m3": float(sv[2] / sv[0]), "m2/m3": float(sv[1] / sv[0])}
    out[str(y)] = row
if __name__ == "__main__":
    json.dump(out, open(HERE / "the_lift_at_finite_L.json", "w"), indent=1); print(json.dumps(out, indent=1)[:1500])
