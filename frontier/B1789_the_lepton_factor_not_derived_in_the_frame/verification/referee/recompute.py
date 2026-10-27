"""Referee recomputation (S226 lepton factor note): own pipeline from b1656_funcs primitives (not B1726's compute()).
R2 = (m2/m3)_lep/(m2/m3)_down, R1 = (m1/m3)_down/(m1/m3)_lep, Dframe = R2*R1, reading S both sectors.
Logs channels dropped by the sqrt(2 pi L + c_s) > 0 guard, and tests L-sensitivity (L_max column vs fixed L)."""
import os, sys, io, json, math, contextlib, importlib.util, pathlib
from fractions import Fraction as Fr
from multiprocessing import Pool
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
OUT = pathlib.Path(__file__).resolve().parent


def mods():
    sys.path.insert(0, str(ROOT / "frontier/B1723_the_golden_valley/verification")); argv = sys.argv; sys.argv = ["x"]
    import b1656_funcs as B
    sys.argv = argv
    P = ROOT / "frontier/B1691_the_exponents_at_the_two_fixed_points/verification"; sys.path.insert(0, str(P))
    spec = importlib.util.spec_from_file_location("te", P / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
    col = sorted((p["tau"][1], p["L_max"]) for p in json.loads((ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json").read_text())["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
    return B, te, col


def one(task):
    import mpmath as mp
    B, te, col = mods()
    re_t, im_t, a, b, Lmode = task
    t = complex(re_t, im_t)
    w = float(Fr(a)) * t + float(Fr(b))
    hv = [complex(te.ev(c, mp.mpc(t.real, t.imag))) for c in te.B[1]]
    S = hv[0] * B.QI + hv[1] * B.QJ + hv[2] * B.QK
    L = float(np.interp(im_t, [q[0] for q in col], [q[1] for q in col])) if Lmode == "col" else float(Lmode)
    res = {}; dropped = []
    for sec, (lf, rf) in (("down", ("Q", "d")), ("lep", ("L", "e"))):
        x, y = B.twist_of(B.SIXY[lf] * w, t), B.twist_of(B.SIXY[rf] * w, t)
        R = B.residues(x, y, t); c = B.cA(x, y, t, R)
        u = {}
        for s in B.UNITS:
            if c[s] is None: u[s] = 0; continue
            arg = 2 * math.pi * L + c[s]
            if arg <= 0: dropped.append((sec, s, round(c[s], 3))); u[s] = 0
            else: u[s] = math.sqrt(arg) * R[s]
        Y = B.coupling(S, B.weighted_M(u)); sv = np.linalg.svd(Y, compute_uv=False)
        res[sec] = (sv[1] / sv[0], sv[2] / sv[0])
    R2 = res["lep"][0] / res["down"][0]; R1 = res["down"][1] / res["lep"][1]
    return dict(re=re_t, im=im_t, a=a, b=b, L=Lmode, R2=R2, R1=R1, D=R2 * R1, qi=abs(hv[0]) / max(abs(hv[1]), abs(hv[2])), dropped=dropped)


if __name__ == "__main__":
    tasks = []
    # item 3: slope 2/5 on three lines (one order 10 k odd, one order 25, one order 30), two heights, two L modes
    for b in ("1/10", "4/25", "23/30"):
        for y in (3.0, 6.0):
            for Lm in ("col", "2.0"):
                tasks.append((0.3, y, "2/5", b, Lm))
    # item 4: slope 1/10 on two offsets, two heights
    for b in ("1/6", "1/2"):
        for y in (2.9, 8.0):
            tasks.append((0.3, y, "1/10", b, "col"))
    # control: B1786's best row from its census (2/5, 23/30) at 0.269230769 + 3.037487672558812i (census: R2 0.9987, R1 0.9413)
    tasks.append((0.269230769, 3.037487672558812, "2/5", "23/30", "col"))
    with Pool(4) as P:
        rs = P.map(one, tasks)
    for r in rs:
        print("a %-4s b %-5s tau %.3f+%.3fi L %-4s  R2 %.4f  R1 %.4f  D %.4f  9D %.3f  |QI|/max %.2e  dropped %s" % (
            r["a"], r["b"], r["re"], r["im"], r["L"], r["R2"], r["R1"], r["D"], 9 * r["D"], r["qi"], r["dropped"]))
    json.dump(rs, open(OUT / "recompute.json", "w"), indent=1, default=str)
