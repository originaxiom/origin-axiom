"""Referee P-406, r6: Theorem B's dichotomy inside its own scope (zero line, H-cov, F1).  The weight-7/2 section with no
end data is unique, a0 = D2R - E4 R/48 (B1697, W68 G1).  B1806's closed form at k = 7/2 (a = alpha E4 R + gamma D2R,
t = alpha/gamma): m2/m3(i) = min(x, 1/x), x = 3/(2|288 t + 5|).  At t = -1/48: x = 3/2, so m2/m3(i) = 2/3 -- a definite,
parameter-free, non-degenerate value at a forced point.  Checked here by the exact SVD of Y(a) = a R^T + R a^T - (a.R) 1
(B1645/B1646) from B1691's own q-series, and the control DR (weight 3/2: m2/m3(i) = 1).  Then the first generation at the
canonical end (B1656's four-channel coupling, B1691's S164 machinery, zero line) for a0 at i: m1/m3(i)."""
import sys, io, contextlib, importlib.util, pathlib, math, json, glob
from fractions import Fraction as F
import numpy as np
import mpmath as mp
ROOT = pathlib.Path(__file__).resolve().parents[3]
V = pathlib.Path(glob.glob(str(ROOT / 'B1691_*/verification'))[0]); C = V / 'correction'
sys.path.insert(0, str(C)); sys.path.insert(0, str(V)); sys.argv = ['x']
spec = importlib.util.spec_from_file_location("te", V / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
import b1656_funcs as B
mp.mp.dps = 40
S = te.S
a0 = [te.B[2][j] + S.c(F(-1, 48)) * te.e4 * te.B[0][j] for j in range(3)]
def svd_ratio(sec, tau):
    a = mp.matrix([te.ev(c, tau) for c in sec]); R = mp.matrix([te.ev(c, tau) for c in te.R])
    aR = sum(a[j] * R[j] for j in range(3))
    Y = a * R.T + R * a.T - aR * mp.eye(3)
    s = sorted([abs(v) for v in mp.svd_c(Y, compute_uv=False)], reverse=True)
    return s
out = {}
for name, sec in (("DR (k=3/2)", te.B[1]), ("a0 = D2R - E4 R/48 (k=7/2)", a0)):
    for tn, tau in (("i", mp.mpc(0, 1)), ("i + 1e-3", mp.mpc(0, 1) + mp.mpf('1e-3')), ("2i", mp.mpc(0, 2))):
        s = svd_ratio(sec, tau)
        out[f"{name} @ {tn}"] = {"s": [mp.nstr(v, 12) for v in s], "m2/m3 = s2/s1": mp.nstr(s[1] / s[0], 15)}
        print(f"{name:28s} tau={tn:9s} s = {[mp.nstr(v, 8) for v in s]}  s2/s1 = {mp.nstr(s[1] / s[0], 15)}", flush=True)
# the first generation at the canonical end, zero line, tau = i
for L, Ln in ((0.688385709056232, "L_max(i)"), (2.7192576281085956, "L_2(i)")):
    t = 1j; x, yy = B.sector_twists(0, t, 1, -4)
    R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
    a = [complex(te.ev(cc, mp.mpc(0, 1))) for cc in a0]
    Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    sv = np.linalg.svd(B.coupling(Sm, B.weighted_M(u)), compute_uv=False)
    out[f"a0 four-channel @ i, {Ln}"] = {"m1/m3": float(sv[2] / sv[0]), "m2/m3": float(sv[1] / sv[0])}
    print(f"a0 four-channel coupling at tau=i, {Ln}: m1/m3 = {sv[2]/sv[0]:.8e}, m2/m3 = {sv[1]/sv[0]:.10f}")
json.dump(out, open(pathlib.Path(__file__).with_suffix('.json'), 'w'), indent=1)
