"""B1692's correction (2026-10-21): the cross-sector spread of m2/m3 at B1695's best point (alpha = 37/96, Im tau = 3.15,
Re tau = 0; the up quarks through the conjugate Higgs) under B1656's four-channel coupling, against L: B1692's bound of four
is the large-L (point-coupling) limit; at the canonical L of order one the spread exceeds it."""
import sys, io, json, math, contextlib, importlib.util, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
V = HERE
sys.path.insert(0, str(V)); sys.argv = ['x']
import b1656_funcs as B
P1691 = ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
sys.path.insert(0, str(P1691))
spec = importlib.util.spec_from_file_location("te", P1691 / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
import mpmath as mp
def at(j, y, re_t, Ls):
    t = complex(re_t, y); w = (j / 96.0) * t
    a = [complex(te.ev(cc, mp.mpc(re_t, y))) for cc in te.B[1]]
    S = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK; St = B.EPS @ np.conj(S) @ B.EPS.T
    out = {}
    for L in Ls:
        r = {}
        for sec, (lf, rf), SS in (("up", ("Q", "u"), St), ("down", ("Q", "d"), S), ("lep", ("L", "e"), S)):
            x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
            u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
            sv = np.linalg.svd(B.coupling(SS, B.weighted_M(u)), compute_uv=False); r[sec] = sv[1] / sv[0]
        out[L] = (r, max(r.values()) / min(r.values()))
    return out
res = at(37, 3.15, 0.0, (0.648, 2.5, 10, 40, 160, 640, 2560))
out = {str(L): {'m2/m3': {k: float(v) for k, v in r.items()}, 'spread': float(sp)} for L, (r, sp) in res.items()}
if __name__ == '__main__':
    json.dump(out, open(HERE / 'the_bound_at_finite_L.json', 'w'), indent=1)
    for L, (r, sp) in res.items(): print('L %7.3f  up %.4g down %.4g lep %.4g  spread %.2f' % (L, r['up'], r['down'], r['lep'], sp))
