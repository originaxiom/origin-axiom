"""B1703 (P-250): the SM seat's question (relay 195) -- is the difference between its residue rule (d = e iff N | 8 or 10,
the point coupling, the large-L limit) and the canonical-end census (d = e iff N | 4 or 5) the frame?  Down against
leptons on lines of order 4, 5, 7, 8, 9, 10 at tau = 0.31 + 2.4i and omega, for L from the canonical end to 1e8."""
import sys, json, math, pathlib
from fractions import Fraction as Fr
from multiprocessing import Pool
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); _argv = sys.argv; sys.argv = ['x']
import the_line_census as C
sys.argv = _argv
B, te, mp = C.B, C.te, C.mp
LS = ["canon", 10.0, 1e2, 1e4, 1e8]
def task(p):
    (a, b, N), t = p
    w = float(a) * t + float(b)
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    out = {"line": [str(a), str(b)], "N": N, "tau": [t.real, t.imag]}
    sec = {}
    for name, (lf, rf) in (("down", ("Q", "d")), ("lep", ("L", "e"))):
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R); sec[name] = (R, c)
    for L in LS:
        LL = C.L_of(t.imag) if L == "canon" else L; r = {}
        for name, (R, c) in sec.items():
            u = {k: (math.sqrt(2 * math.pi * LL + c[k]) * R[k] if c[k] is not None and 2 * math.pi * LL + c[k] > 0 else 0) for k in B.UNITS}
            sv = np.linalg.svd(B.coupling(S, B.weighted_M(u)), compute_uv=False); r[name] = sv[1] / sv[0]
        out[str(L)] = abs(r["down"] - r["lep"]) / r["down"]
    return out
if __name__ == "__main__":
    tasks = []
    for N in (4, 5, 7, 8, 9, 10):
        ls = [(Fr(j, N), Fr(k, N), N) for j in range(N) for k in range(N) if math.gcd(math.gcd(j, k), N) == 1][:6]
        for t in (complex(0.31, 2.4), complex(-0.5, math.sqrt(3) / 2)): tasks += [(l, t) for l in ls]
    with Pool(8) as P: rows = P.map(task, tasks)
    for N in (4, 5, 7, 8, 9, 10):
        rs = [r for r in rows if r["N"] == N]
        print(N, {L: "%.1e" % max(r[str(L)] for r in rs) for L in LS})
    json.dump(rows, open(HERE / "large_L.json", "w"), indent=1)
