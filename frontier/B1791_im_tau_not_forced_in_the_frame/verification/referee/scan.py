"""Referee scan (read-only on the record): B1656's frame via B1726's census._modules(), compute()'s exact path, keeping the
full singular values per (sector, horocycle, reading), the channel norms c_s, |S| (Frobenius of the Higgs matrix) and |eta|.
Grid: 4 slope-2/5 lines (the note's three + the mirror (2/5, 1/2)), Re tau in 7 values, Im tau 1.0-8.0 (53 values).
    python3 -B scan.py --workers 6"""
import sys, json, math, pathlib, importlib.util
from fractions import Fraction as Fr
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()); HERE = pathlib.Path(__file__).resolve().parent
LINES = [(Fr(2, 5), Fr(1, 10)), (Fr(2, 5), Fr(23, 30)), (Fr(2, 5), Fr(4, 25)), (Fr(2, 5), Fr(1, 2))]
RES = (0.0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9)
IMS = tuple([round(1.0 + 0.05 * k, 3) for k in range(10)] + [round(1.5 + 0.1 * k, 3) for k in range(26)]
            + [round(4.25 + 0.25 * k, 3) for k in range(16)])
_C = {}


def census():
    if not _C:
        spec = importlib.util.spec_from_file_location("c26", ROOT / "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); _C["m"] = m
    return _C["m"]


def eta_abs(t):
    import mpmath as mp
    q = mp.exp(2j * mp.pi * mp.mpc(t.real, t.imag))
    p = mp.mpf(1)
    for n in range(1, 200):
        p *= (1 - q ** n)
        if abs(q) ** n < 1e-30: break
    return float(abs(mp.exp(2j * mp.pi * mp.mpc(t.real, t.imag) / 24) * p))


def point(task):
    import mpmath as mp
    (a, b), re_t, im_t = task
    C = census(); M_ = C._modules(); B, te, col = M_["B"], M_["te"], M_["col"]
    t = complex(re_t, im_t); w = float(a) * t + float(b)
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    reading = {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T}
    Ls = {"L_max": float(np.interp(im_t, [q[0] for q in col], [q[1] for q in col])),
          "L_2": float(np.interp(im_t, [q[0] for q in col], [q[2] for q in col]))}
    out = {"line": "%s,%s" % (a, b), "re": re_t, "im": im_t, "S_frob": float(np.linalg.norm(S)), "eta": eta_abs(t)}
    for sec, (lf, rf) in C.SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
        out[sec + "|c"] = {s: c[s] for s in B.UNITS}
        out[sec + "|absR"] = {s: abs(R[s]) for s in B.UNITS}
        for h in ("L_max", "L_2"):
            L = Ls[h]
            u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
            Mw = B.weighted_M(u)
            out[sec + "|" + h + "|detM"] = float(abs(np.linalg.det(Mw)))
            for rn in ("S", "St"):
                Y = B.coupling(reading[rn], Mw); sv = np.linalg.svd(Y, compute_uv=False)
                out["%s|%s|%s" % (sec, h, rn)] = [float(v) for v in sv]
    return out


if __name__ == "__main__":
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    tasks = [(ln, r, y) for ln in LINES for r in RES for y in IMS]
    print(len(tasks), "points", flush=True)
    import multiprocessing as mpp
    with mpp.Pool(nw) as P, open(HERE / "scan.jsonl", "w") as f:
        for k, r in enumerate(P.imap_unordered(point, tasks, chunksize=4)):
            f.write(json.dumps(r) + "\n"); f.flush()
            if k % 100 == 0: print(k, flush=True)
    print("scan exit 0")
