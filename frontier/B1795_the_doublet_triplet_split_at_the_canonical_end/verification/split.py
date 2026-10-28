"""B1795 (P-325; L250 (ii)): the doublet-triplet split at B1667's canonical end (no data).  B1656's frame: the vector-like
pairs are the sectors with twists (-2w, 2w) for the colour triplets D D^c (6Y = -2, 2) and (3w, -3w) for the Higgs pair
H_u H_d (6Y = 3, -3), each in both slot orders; their coupling partner is a singlet (6Y = 0) typed as the frame's Higgs
section (B1691's DR, as B1726's compute() builds S).  For every line, at each point: the residues R_s, the regularised
norms c_s, D = sum c_s R_s^2 = 4 det M (B1716; independent of L), normalised as in B1716's Z6, and the coupling's spectrum
Y = coupling(S or S~, M) at both horocycles.  Lines: B1713's 266 (orders 1-12, up to sign) and the twenty slope-2/5 lines
of exact order 60 (B1792).  Points: B1716's two generic tau and the six's strip point (B1792's best row).
    python3 -B split.py [--workers 8]          -> split_rows.jsonl (checkpointed), split.json, split_run.txt
    python3 -B split.py --control              -> control_run.txt (the SM sectors against B1726's compute(); no pair)
Importing computes nothing."""
import sys, io, json, math, contextlib, importlib.util, pathlib, argparse
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
PAIRS = {"D": (-2, 2), "Dc": (2, -2), "H": (3, -3), "Hc": (-3, 3)}
STRIP = (0.730769231, 3.037487672558812)                  # B1792's best row (and B1786's strip point)
POINTS = {"g1": (0.37, 2.2), "g2": (0.11, 1.7), "strip": STRIP}
ZERO = 1e-10                                              # B1716's Z6 threshold scale: exact zeros sit at <= 1e-13
_M = {}


def _modules():
    if not _M:
        spec = importlib.util.spec_from_file_location("c1726", ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification" / "census.py")
        c1726 = importlib.util.module_from_spec(spec); spec.loader.exec_module(c1726)
        M = c1726._modules(); _M.update(B=M["B"], te=M["te"], col=M["col"], c1726=c1726)
    return _M


def lines():
    """B1713's 266 lines, then the twenty slope-2/5 lines of exact order 60 (b = k/60, gcd(k, 6) = 1)"""
    base = list(_modules()["c1726"].lines())
    o60 = [(Fr(2, 5), Fr(k, 60)) for k in range(60) if math.gcd(k, 6) == 1]
    return base + o60


def order(a, b): return math.lcm(Fr(a).denominator, Fr(b).denominator)


def higgs(t):
    import mpmath as mp
    M = _modules(); B, te = M["B"], M["te"]
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
    return {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T}


def Ls_at(im_t):
    col = _modules()["col"]
    return {"L_max": float(np.interp(im_t, [q[0] for q in col], [q[1] for q in col])), "L_2": float(np.interp(im_t, [q[0] for q in col], [q[2] for q in col]))}


def sector(t, w, ql, qr, S, Ls):
    B = _modules()["B"]
    x, y = B.sector_twists(w, t, ql, qr); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
    cmax = max(abs(v) for v in c.values() if v is not None) if any(v is not None for v in c.values()) else float("nan")
    D = sum(c[s] * R[s] ** 2 for s in B.UNITS if c[s] is not None)
    Dn = abs(D) / (cmax * B.nR2(R)) if B.nR2(R) > 1e-28 else 0.0          # every residue zero: M = 0, det M = 0
    out = {"R": {s: [R[s].real, R[s].imag] for s in B.UNITS}, "c": {s: c[s] for s in B.UNITS}, "D": [D.real, D.imag], "Dn": Dn,
           "R1_rel": abs(R["1"]) / math.sqrt(B.nR2(R)) if B.nR2(R) > 1e-28 else 0.0}
    for h, L in Ls.items():
        u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
        Mw = B.weighted_M(u)
        for rn, Sx in S.items():
            sv = np.linalg.svd(B.coupling(Sx, Mw), compute_uv=False)
            out["sv|%s|%s" % (h, rn)] = [float(v) for v in sv]
            out["tr|%s|%s" % (h, rn)] = abs(complex(np.trace(B.EPS @ Sx @ Mw.T)))
        out["detM|%s" % h] = abs(complex(np.linalg.det(Mw)))
    return out


def task(job):
    k, pk = job
    a, b = lines()[k]; re_t, im_t = POINTS[pk]; t = complex(re_t, im_t); w = float(a) * t + float(b)
    S = higgs(t); Ls = Ls_at(im_t)
    r = {"line": k, "a": str(a), "b": str(b), "order": order(a, b), "point": pk}
    for name, (ql, qr) in PAIRS.items():
        r[name] = sector(t, w, ql, qr, S, Ls)
    return r


def control():
    """the SM sectors through this file's path against B1726's compute() at the strip point on (2/5, 49/60)"""
    B = _modules()["B"]; c1726 = _modules()["c1726"]
    a, b = Fr(2, 5), Fr(49, 60); re_t, im_t = STRIP; t = complex(re_t, im_t); w = float(a) * t + float(b)
    ref = c1726.compute(re_t, im_t, a, b); S = higgs(t); Ls = Ls_at(im_t); dev = 0.0
    for sec, (lf, rf) in c1726.SECT.items():
        r = sector(t, w, B.SIXY[lf], B.SIXY[rf], S, Ls)
        for h in Ls:
            for rn in S:
                sv = r["sv|%s|%s" % (h, rn)]; mine = [sv[1] / sv[0], sv[2] / sv[0]]
                dev = max(dev, max(abs(p - q) for p, q in zip(mine, ref["%s|%s|%s" % (sec, h, rn)])))
    return dev


CARRIERS = {("2/5", "11/12"), ("2/5", "29/60"), ("2/5", "41/60"), ("2/5", "47/60"), ("2/5", "49/60"), ("2/5", "7/60")}   # B1792's six


def cells_of(rows, d):
    """the cells and read-outs, as sealed, from the rows (pure: no frame value is computed here)"""
    def zero(r, p): return (not math.isnan(r[p]["Dn"])) and r[p]["Dn"] < ZERO
    def name(r): return "%s,%s" % (r["a"], r["b"])
    by_line = {}
    for r in rows: by_line.setdefault(name(r), []).append(r)
    exactH = sorted(k for k, rs in by_line.items() if all(zero(r, "H") or zero(r, "Hc") for r in rs))
    exactD = sorted(k for k, rs in by_line.items() if all(zero(r, "D") or zero(r, "Dc") for r in rs))
    split = sorted(k for k in exactH if k not in exactD)
    o5 = [r for r in rows if r["order"] in (1, 5) and not math.isnan(r["D"]["Dn"])]
    ident = max((abs(r["D"]["Dn"] - r["H"]["Dn"]) / max(r["D"]["Dn"], r["H"]["Dn"], 1e-300) for r in o5), default=float("nan"))
    def lightest(r, ps): return min(r[p]["sv|%s|%s" % (h, rn)][2] / r[p]["sv|%s|%s" % (h, rn)][0] for p in ps for h in ("L_max", "L_2") for rn in ("S", "St"))
    strip = [r for r in rows if r["point"] == "strip" and (r["a"], r["b"]) in CARRIERS]
    strip_H = min((lightest(r, ("H", "Hc")) for r in strip), default=float("nan"))
    strip_D = min((lightest(r, ("D", "Dc")) for r in strip), default=float("nan"))
    cells = {"C1_control_dev_le_1e-9": d <= 1e-9, "C2_order5_identity_le_1e-9": ident <= 1e-9,
             "S1_DECISIVE_no_line_with_exact_detM_H_zero": not exactH, "S1p_no_line_with_exact_detM_D_zero": not exactD,
             "S2_split_some_line_detM_H_zero_detM_D_not": bool(split),
             "S3_DECISIVE_no_light_Higgs_pair_at_the_strip_ge_1e-3": strip_H >= 1e-3}
    readouts = {"exact_H_lines": exactH, "exact_D_lines": exactD, "split_lines": split, "order5_identity_max_rel": ident,
                "strip_carriers_rows": len(strip), "strip_carriers_min_sv3_over_sv1_H": strip_H, "strip_carriers_min_sv3_over_sv1_D": strip_D,
                "min_Dn_H": min(min(r["H"]["Dn"], r["Hc"]["Dn"]) for r in rows), "min_Dn_D": min(min(r["D"]["Dn"], r["Dc"]["Dn"]) for r in rows),
                "max_R1_rel_leading_order": max(max(r[p]["R1_rel"] for p in PAIRS) for r in rows)}
    return cells, readouts


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--workers", type=int, default=1); ap.add_argument("--control", action="store_true")
    args = ap.parse_args()
    if args.control:
        d = control(); txt = "control: SM sectors through split.py's path vs B1726 compute() at (2/5, 49/60), strip point: max dev %.3e\ncontrol exit 0\n" % d
        (HERE / "control_run.txt").write_text(txt, encoding="utf-8"); print(txt, end=""); return
    RJ = HERE / "split_rows.jsonl"                        # checkpoint: each row appended as it completes; a rerun skips them
    done = set()
    if RJ.exists():
        for l in RJ.read_text(encoding="utf-8").splitlines():
            if l.strip(): r = json.loads(l); done.add((r["line"], r["point"]))
    jobs = [(k, pk) for k in range(len(lines())) for pk in POINTS if (k, pk) not in done]
    with open(RJ, "a", encoding="utf-8") as fh:
        if args.workers > 1:
            import multiprocessing as mpc
            with mpc.get_context("fork").Pool(args.workers) as pool:
                for r in pool.imap_unordered(task, jobs, chunksize=2): fh.write(json.dumps(r, default=str) + "\n"); fh.flush()
        else:
            for j in jobs: fh.write(json.dumps(task(j), default=str) + "\n"); fh.flush()
    rows = sorted((json.loads(l) for l in RJ.read_text(encoding="utf-8").splitlines() if l.strip()), key=lambda r: (r["line"], r["point"]))
    assert len(rows) == len(lines()) * len(POINTS), len(rows)
    d = control()
    cells, readouts = cells_of(rows, d)
    out = {"lines": len(lines()), "points": POINTS, "pairs": PAIRS, "control_dev": d, "cells": cells, "readouts": readouts}
    (HERE / "split.json").write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    txt = ["B1795 split.py: %d lines x %d points x 4 pair orientations (rows in split_rows.jsonl)" % (len(lines()), len(POINTS))]
    for k, v in cells.items(): txt.append("cell %s: %s" % (k, v))
    for k, v in readouts.items(): txt.append("readout %s: %s" % (k, v))
    txt.append("split exit 0")
    (HERE / "split_run.txt").write_text("\n".join(txt) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
