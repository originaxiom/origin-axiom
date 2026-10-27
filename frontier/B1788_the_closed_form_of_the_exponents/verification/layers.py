"""Closed-form check, layers B-C (data-free): per (line, sector, height) the residues R_s, the regularised norms c_s, the
channel weights u_s = sqrt(2 pi L + c_s) R_s, the M entries, and the singular-value ratios, with B1726's compute() pieces
(L_max at Re tau = 1/3, heights 4, 5, 6 -- B1785's setting).  Writes layers_<tag>.json.
    python3 -B layers.py <tag> <alpha/b list as a/b:c/d,...>"""
import sys, math, json, pathlib
from fractions import Fraction as Fr
import numpy as np
import blocks as K
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
B = K.B
HERE = pathlib.Path(__file__).resolve().parent
COL = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.loads(open(ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json").read())["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
H = (4.0, 5.0, 6.0)


def S_at(t):
    import io, contextlib, importlib.util, mpmath as mp
    if "te" not in globals():
        P = (ROOT / "frontier/B1691_the_exponents_at_the_two_fixed_points/verification"); sys.path.insert(0, str(P))
        spec = importlib.util.spec_from_file_location("te", P / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
        globals()["te"] = te
    te = globals()["te"]
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    return av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK


def one(a, b, sec, y):
    lf, rf = B.SECTORS[sec]; t = complex(1 / 3, y); w = float(a) * t + float(b)
    x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
    L = float(np.interp(y, [q[0] for q in COL], [q[1] for q in COL]))
    u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
    Mw = B.weighted_M(u); S = S_at(t); out = {"R": {s: [R[s].real, R[s].imag] for s in R}, "c": c, "u": {s: [complex(u[s]).real, complex(u[s]).imag] for s in u},
                                             "M": [[[complex(Mw[i, j]).real, complex(Mw[i, j]).imag] for j in range(2)] for i in range(2)]}
    for rn, SS in (("S", S), ("St", B.EPS @ np.conj(S) @ B.EPS.T)):
        sv = np.linalg.svd(B.coupling(SS, Mw), compute_uv=False); out[rn] = [float(sv[1] / sv[0]), float(sv[2] / sv[0])]
    return out


if __name__ == "__main__":
    tag = sys.argv[1]; L = [tuple(Fr(z) for z in p.split(":")) for p in sys.argv[2].split(",")]
    res = []
    for (a, b) in L:
        for sec in ("up", "down", "lep"):
            res.append({"alpha": str(a), "b": str(b), "sec": sec, "h": {str(y): one(a, b, sec, y) for y in H}})
        print(a, b, flush=True)
    json.dump(res, open(HERE / ("layers_%s.json" % tag), "w"))
    print("layers exit 0")
