"""P-433 (main's own route; exploratory, audit room; data-free): the near-point exponents at the canonical end radius, computed
with the RECORD'S machinery -- B1656's four-channel coupling as B1691's S164 correction uses it (b1656_funcs: sector_twists at
the zero line, residues, the channel norms cA, coupling) and B1691's own sections (the_exponents.section) -- not B1807's
referee's evaluator.  Slopes of m1/m3 and m2/m3 in eps = |tau - p| between eps = 1e-2, 3e-3, 1e-3, at L = 0.65 and 2.5.
Expected from B1807 (its referee's run): near omega at 23/2 and 11/2 m2/m3 ~ eps (not eps^2), m1/m3 ~ eps^3; 15/2 unchanged
(m2/m3 -> 1, m1/m3 ~ eps^2); near i the k = 3/2 mod 4 class m1/m3 ~ eps; B1806's f2 = 0 rows (15/2, 23/2): m2/m3(i) = O(1/L), not 0.
    python3 near_points_finite_L_main.py      # writes near_points_finite_L_main.json beside itself"""
import contextlib, glob, importlib.util, io, json, math, pathlib, sys
import numpy as np
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
V = pathlib.Path(glob.glob(str(ROOT / "frontier" / "B1691_*" / "verification"))[0]); C = V / "correction"
sys.path.insert(0, str(C)); sys.path.insert(0, str(V)); sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("te", V / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
import b1656_funcs as B

OM = complex(-0.5, math.sqrt(3) / 2); I1 = complex(0, 1)


def masses(sec, tau, L):
    t = complex(tau); x, yy = B.sector_twists(0, t, 1, -4)
    R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
    a = [complex(te.ev(cc, mp.mpc(tau.real, tau.imag))) for cc in sec]
    Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    sv = np.linalg.svd(B.coupling(Sm, B.weighted_M(u)), compute_uv=False)
    return sv[2] / sv[0], sv[1] / sv[0]


EPS = (1e-2, 3e-3, 1e-3); out = {}
cases = [("omega", OM, 6, "23/2"), ("omega", OM, 3, "11/2"), ("omega", OM, 4, "15/2"),
         ("i", I1, 1, "3/2 (DR)"), ("i", I1, 5, "19/2"), ("i", I1, 4, "15/2, f2 = 0"), ("i", I1, 6, "23/2, f2 = 0")]
for pname, p, n, kname in cases:
    with contextlib.redirect_stdout(io.StringIO()):
        sec = te.B[1] if kname == "3/2 (DR)" else (te.section(n, 3, drop=(2,))[0] if "f2 = 0" in kname else te.section(n, 1)[0])
    row = {}
    for L in (0.65, 2.5):
        v = [masses(sec, p + e * complex(math.cos(0.7), math.sin(0.7)), L) for e in EPS]
        sl = lambda j: [round(math.log(v[q][j] / v[q + 1][j]) / math.log(EPS[q] / EPS[q + 1]), 3) for q in range(2)]
        row["L=%g" % L] = {"m1/m3": ["%.4g" % w[0] for w in v], "m2/m3": ["%.4g" % w[1] for w in v],
                           "m1 slopes": sl(0), "m2 slopes": sl(1)}
    out["%s %s" % (pname, kname)] = row
    print(pname, kname, json.dumps(row), flush=True)
(HERE / "near_points_finite_L_main.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
