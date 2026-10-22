"""B1703, after Review 67 (its premise audit): is the SM seat's delta-rule (d = e iff N | 8 or 10) the deep-cusp limit of
B1656's coupling?  Down against leptons on lines of order 4, 5, 8, 10 (controls 7, 9) at large L (1e8), Im tau from 2.4
to 14 at Re tau = 0.31; the relative m2/m3 difference per line."""
import sys, json, math, pathlib, io, contextlib, importlib.util
from fractions import Fraction as Fr
from multiprocessing import Pool
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(A)); _argv = sys.argv; sys.argv = ['x']
spec = importlib.util.spec_from_file_location("lc", A / "the_line_census.py"); C = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(C)
sys.argv = _argv
B, te, mp = C.B, C.te, C.mp
YS = [2.4, 4.0, 6.0, 8.0, 10.0, 14.0]
def task(p):
    (a, b, N), y = p
    t = complex(0.31, y); w = float(a) * t + float(b)
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK; r = {}
    for name, (lf, rf) in (("down", ("Q", "d")), ("lep", ("L", "e"))):
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t)
        u = {k: math.sqrt(2 * math.pi * 1e8) * R[k] for k in B.UNITS}
        sv = np.linalg.svd(B.coupling(S, B.weighted_M(u)), compute_uv=False); r[name] = sv[1] / sv[0]
    return {"line": [str(a), str(b)], "N": N, "y": y, "rel": abs(r["down"] - r["lep"]) / r["down"]}
if __name__ == "__main__":
    tasks = []
    for N in (4, 5, 7, 8, 9, 10):
        ls = [(Fr(j, N), Fr(k, N), N) for j in range(N) for k in range(N) if math.gcd(math.gcd(j, k), N) == 1][:6]
        tasks += [(l, y) for l in ls for y in YS]
    with Pool(8) as P: rows = P.map(task, tasks)
    for N in (4, 5, 7, 8, 9, 10):
        print(N, {y: "%.1e..%.1e" % (min(r["rel"] for r in rows if r["N"] == N and r["y"] == y), max(r["rel"] for r in rows if r["N"] == N and r["y"] == y)) for y in YS})
    json.dump(rows, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
