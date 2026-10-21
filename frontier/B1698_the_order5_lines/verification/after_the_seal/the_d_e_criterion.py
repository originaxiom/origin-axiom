"""B1698, after the seal (labelled; not part of the sealed test): why the down quarks and the leptons coincide on the
order-5 lines, and which lines can split them.  6Y mod 5 is constant on SU(5)'s multiplets (Q, u, e = 1; d, L = 2;
H = 3), so on a line with 5w in the lattice the lepton pair's twists (L, e) are the down pair's (Q, d) swapped: the
lepton coupling is the down coupling transposed (minimal SU(5)'s Y_e = Y_d^T), with the same singular values.  By the
same count the pairs' twists coincide unswapped when 4w is in the lattice (6Y mod 4 is constant on Pati-Salam's SU(4)
multiplets: Y_e = Y_d).  The prediction, printed before the loop:
the down and lepton ratios coincide exactly when the line's order divides 4 or 5, and differ otherwise.  Lines
(1/N, 0), (0, 1/N), (1/N, 1/N) for N = 2..12 at tau = 1/2 + 2.5i and 2i; the end-data Higgs DR; L_max.  No data.
Coincide means m2/m3 agrees to 1e-10 relatively and m1/m3 to 1e-12 absolutely.  Disclosed: the comparison was rewritten
twice after seeing output, the computation and the prediction unchanged -- the first runs compared both ratios
relatively and flagged the order-4 lines, where m1/m3 is a numerical zero (~1e-15) in both sectors and m2/m3 agrees to
1e-15.
    python3 -B the_d_e_criterion.py [--workers 8]      # writes the_d_e_criterion.json beside itself"""
import sys, io, json, math, contextlib, importlib.util, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); _argv = sys.argv; sys.argv = ['x']
spec = importlib.util.spec_from_file_location("o5", HERE.parent / "the_order5_lines.py"); o5 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(o5)
sys.argv = _argv
B, te, mp = o5.B, o5.te, o5.mp
def order(a, b): return math.lcm(Fr(a).denominator, Fr(b).denominator)
def point(task):
    a, b, re_t, y = task
    t = complex(re_t, y); w = float(a) * t + float(b)
    av = [complex(te.ev(cc, mp.mpc(re_t, y))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    L = o5.L_of(y, "L_max"); res = {"line": [str(a), str(b)], "order": order(a, b), "tau": [re_t, y]}
    for sec, (lf, rf) in (("down", ("Q", "d")), ("lep", ("L", "e"))):
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
        sv = np.linalg.svd(B.coupling(S, B.weighted_M(u)), compute_uv=False)
        res[sec] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
    res["m2_rel_diff"] = abs(res["down"][0] - res["lep"][0]) / res["down"][0]
    res["m1_abs_diff"] = abs(res["down"][1] - res["lep"][1])
    res["coincide"] = res["m2_rel_diff"] < 1e-10 and res["m1_abs_diff"] < 1e-12
    return res
if __name__ == "__main__":
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    print("prediction: down and leptons coincide exactly when the line's order divides 4 or 5")
    lines = [(Fr(1, N), Fr(0)) for N in range(2, 13)] + [(Fr(0), Fr(1, N)) for N in range(2, 13)] + [(Fr(1, N), Fr(1, N)) for N in range(2, 13)]
    tasks = [(a, b, r, y) for a, b in lines for r, y in ((0.5, 2.5), (0.0, 2.0))]
    with Pool(nw) as P: out = P.map(point, tasks)
    ok = all(r["coincide"] == (4 % r["order"] == 0 or 5 % r["order"] == 0) for r in out)
    for r in out: print(r["line"], r["order"], r["tau"], "m2/m3 %.1e  m1/m3 %.1e  m1/m3 down %.1e" % (r["m2_rel_diff"], r["m1_abs_diff"], r["down"][1]), "coincide" if r["coincide"] else "split")
    print("criterion holds on every line and tau:", ok)
    json.dump({"rows": out, "criterion_holds": ok}, open(HERE / "the_d_e_criterion.json", "w"), indent=1)
