"""Referee B1799, check 1(c): is 'det M != 0 for both Majorana pairings' an argument from B1716's law, or an observation?
B1716's converse is numerical and has a known second family on Re tau = 0 (P-292: up and down D = 0 on the order-12 lines
with 12 alpha odd).  None of B1799's three points is on Re tau = 0.  Here: reproduce P-292 (control), then the Majorana
pairings nucnuc (0, 0) and LL (-3, -3) on Re tau = 0 and Re tau = 1/2, on every line of order 1-12 (B1713's 266), Dn as
B1795's sector().  Read-only."""
import pathlib as _pl; _ROOT = str(next(q for q in _pl.Path(__file__).resolve().parents if (q / 'frontier').is_dir() and (q / 'GENESIS.md').is_file()))
import sys, math, pathlib, importlib.util, json
from fractions import Fraction as Fr
import numpy as np
ROOT = pathlib.Path(_ROOT + "")
spec = importlib.util.spec_from_file_location("split", ROOT / "frontier/B1795_the_doublet_triplet_split_at_the_canonical_end/verification/split.py")
SP = importlib.util.module_from_spec(spec); spec.loader.exec_module(SP)
B = SP._modules()["B"]
LINES = SP.lines()[:266]
HERE = pathlib.Path(__file__).resolve().parent


def Dn(t, a, b, ql, qr):
    w = float(a) * t + float(b); x, y = B.sector_twists(w, t, ql, qr); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
    vals = [abs(v) for v in c.values() if v is not None]
    if not vals or B.nR2(R) < 1e-28: return float("nan")
    D = sum(c[s] * R[s] ** 2 for s in B.UNITS if c[s] is not None)
    return abs(D) / (max(vals) * B.nR2(R))


def task(job):
    re_t, im_t, k = job; a, b = LINES[k]; t = complex(re_t, im_t)
    return {"re": re_t, "im": im_t, "line": k, "a": str(a), "b": str(b),
            "up": Dn(t, a, b, 1, -4), "down": Dn(t, a, b, 1, 2), "LL": Dn(t, a, b, -3, -3), "Lnuc": Dn(t, a, b, -3, 0),
            "nucnuc": Dn(t, a, b, 0, 0) if k == 0 else None}


if __name__ == "__main__":
    import multiprocessing as mpc
    jobs = [(re_t, im_t, k) for (re_t, im_t) in ((0.0, 2.2), (0.0, 1.7), (0.5, 2.2), (0.0, 3.037487672558812)) for k in range(266)]
    with mpc.get_context("fork").Pool(6) as pool: rows = pool.map(task, jobs, chunksize=4)
    (HERE / "r3_cp_line_rows.json").write_text(json.dumps(rows))
    for (re_t, im_t) in sorted({(r["re"], r["im"]) for r in rows}):
        rs = [r for r in rows if r["re"] == re_t and r["im"] == im_t]
        nn = [r["nucnuc"] for r in rs if r["nucnuc"] is not None][0]
        out = "tau = %.3f + %.4fi: nucnuc Dn %.2e;" % (re_t, im_t, nn)
        for s in ("up", "down", "LL", "Lnuc"):
            z = [(r["a"], r["b"]) for r in rs if not math.isnan(r[s]) and r[s] < 1e-10]
            out += "  %s zeros %d (min nonzero %.1e)" % (s, len(z), min(r[s] for r in rs if not math.isnan(r[s]) and r[s] >= 1e-10))
        print(out)
        zl = [(r["a"], r["b"], "%.1e" % r["LL"]) for r in rs if not math.isnan(r["LL"]) and r["LL"] < 1e-10]
        print("   LL zero lines:", zl[:20], "..." if len(zl) > 20 else "")
        order = lambda q, a, b: math.lcm(((q * Fr(a)) % 1).denominator, ((q * Fr(b)) % 1).denominator)
        extra = [(r["a"], r["b"]) for r in rs if not math.isnan(r["Lnuc"]) and (r["Lnuc"] < 1e-10) != (order(-3, r["a"], r["b"]) == 4)]
        print("   Lnuc rows off B1716's law:", len(extra), extra[:12])
    print("r3 exit 0")
