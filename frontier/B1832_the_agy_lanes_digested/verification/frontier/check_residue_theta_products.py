"""All four channel residues of B1656's pairing (main's b1656_funcs) against theta products of the sum and difference twists:
for each channel s, which (a, b) in {1,2,3,4}^2 make |R_s(X, Y)| / [N_a(X+Y) N_b(X-Y)] independent of (X, Y)?  N_a(z) = |theta_a(z|tau)|
exp(-pi (Im z)^2 / Im tau).  Generic complex X, Y; two tau.  (Generalises check_b1761_i_residue.py (a); B1744 has the Y = 0 slice.)"""
import sys, pathlib, json
import numpy as np, mpmath as mp
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _main_frame import B
Bf = B(); rng = np.random.default_rng(17); out = {}
def N(a, z, t):
    q = mp.exp(1j * mp.pi * mp.mpc(t.real, t.imag)); return float(abs(mp.jtheta(a, mp.pi * mp.mpc(z.real, z.imag), q)) * mp.exp(-mp.pi * z.imag ** 2 / t.imag))
for t in (0.137 + 1.31j, -0.271 + 1.83j):
    XY = [(complex(*rng.uniform(-1, 1, 2)), complex(*rng.uniform(-1, 1, 2))) for _ in range(10)]
    Rs = [Bf.residues(Bf.twist_of(X, t), Bf.twist_of(Y, t), t) for X, Y in XY]
    for s in Bf.UNITS:
        best = None
        for a in (1, 2, 3, 4):
            for b in (1, 2, 3, 4):
                r = [abs(R[s]) / (N(a, X + Y, t) * N(b, X - Y, t)) for R, (X, Y) in zip(Rs, XY)]
                sp_ = (max(r) - min(r)) / max(r)
                if best is None or sp_ < best[0]: best = (sp_, a, b, float(np.mean(r)))
        out["%s|%s" % (t, s)] = best
        print("tau=%.3f%+.3fi channel %s: best (a, b) = (%d, %d), rel spread %.1e, constant %.6f" % (t.real, t.imag, s, best[1], best[2], best[0], best[3]))
json.dump({k: list(v) for k, v in out.items()}, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1); print("exit 0")
