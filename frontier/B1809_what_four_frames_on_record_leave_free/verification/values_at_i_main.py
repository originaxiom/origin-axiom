"""P-432, first entries (main's own driver of the record's machinery; exploratory, audit room; data-free): the outputs of
B1656's four-channel coupling at the configuration-fixed point tau = i, zero line, for the record's parameter-free Higgs
directions, at B1667's canonical end radii L_max(i) = 0.688385709056232 and L_2(i) = 2.7192576281085956 (as r6 takes them),
and at L = 2560 (the large-L side).  Checks the P-406 census referee's c1 by a separate code path.
    python3 values_at_i_main.py      # writes values_at_i_main.json beside itself"""
import contextlib, glob, importlib.util, io, json, math, pathlib, sys
from fractions import Fraction as F
import numpy as np
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
V = pathlib.Path(glob.glob(str(ROOT / "frontier" / "B1691_*" / "verification"))[0]); C = V / "correction"
sys.path.insert(0, str(C)); sys.path.insert(0, str(V)); sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("te", V / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
import b1656_funcs as B

S = te.S


def masses(sec, tau, L):
    t = complex(tau); x, yy = B.sector_twists(0, t, 1, -4)
    R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
    a = [complex(te.ev(cc, mp.mpc(tau.real, tau.imag))) for cc in sec]
    Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    sv = np.linalg.svd(B.coupling(Sm, B.weighted_M(u)), compute_uv=False)
    return float(sv[2] / sv[0]), float(sv[1] / sv[0])


secs = {"DR (k = 3/2)": te.B[1],
        "a0 = D2R - E4 R/48 (k = 7/2)": [te.B[2][j] + S.c(F(-1, 48)) * te.e4 * te.B[0][j] for j in range(3)],
        "R (k = -1/2)": te.B[0],
        "t = -5/288: E4 R (-5/288) + D2R (k = 7/2; a.a = 0)": [te.B[2][j] + S.c(F(-5, 288)) * te.e4 * te.B[0][j] for j in range(3)]}
out = {}
for name, sec in secs.items():
    row = {}
    for Ln, L in (("L_max(i)", 0.688385709056232), ("L_2(i)", 2.7192576281085956), ("L = 2560", 2560.0)):
        m1, m2 = masses(sec, complex(0, 1), L)
        row[Ln] = {"m1/m3": "%.5g" % m1, "m2/m3": "%.5g" % m2}
    out[name] = row
    print(name, json.dumps(row), flush=True)
(HERE / "values_at_i_main.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
