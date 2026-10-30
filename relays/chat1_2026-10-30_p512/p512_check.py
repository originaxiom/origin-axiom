#!/usr/bin/env python3
"""P-512, the sealed check of the rule P512_RULE.md (data-free: no Standard Model value is read or compared).

Cells C1-C6 exactly as the rule states them. The instrument is main's code, loaded unchanged from a checkout of main at
5e5e75ac4 (passed as --main), with each module's sha256 asserted. Nothing is written into that checkout.

    python3 -B p512_check.py --main <checkout of main at 5e5e75ac4>

Writes p512_check_out.json beside this script and prints the cells' verdicts. Run once; the output is committed unread.
"""
import argparse, contextlib, hashlib, importlib.util, io, json, math, os, pathlib, subprocess, sys
from fractions import Fraction as F

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
sys.dont_write_bytecode = True
import numpy as np
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
PIN = "5e5e75ac4"
HASHES = {
    "frontier/B1723_the_golden_valley/verification/b1656_funcs.py": "31f09c433c14312d9cee8cfa29a632a72ce13fc46ae838757bf9b22958f22528",
    "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/the_exponents.py": "a8d4ea9bae79dde894b192b7c3645685c1c97890665c96123be20ea6e9073aac",
    "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json": "688152749777970f21a85b3278a39ae33884b9ae99623d5eec541f41de34a774",
    "frontier/B1726_the_two_ingredients_replicated/verification/census.py": "185cf17d8b51c11559bf14650d5ad1dd12745eaa228fc40da0a8b9181d1986bf",
    "frontier/B1817_the_frames_own_lepton_down_factor_at_the_cusp/verification/a1_cusp_map.jsonl": "40aa2ef74c789850a9d7c08a2c789fc42849280f11baeff094c26764a02ee4a9",
}

ap = argparse.ArgumentParser()
ap.add_argument("--main", required=True)
ROOT = pathlib.Path(ap.parse_args().main).resolve()
head = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
assert head.startswith(PIN), "main's checkout is not at the pinned commit"
for rel, h in HASHES.items():
    assert hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() == h, "hash mismatch: " + rel

sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification"))
sys.path.insert(0, str(ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"))  # the_exponents imports qseries from here (launch 1's fix)
_argv = sys.argv; sys.argv = ["x"]
import b1656_funcs as B  # noqa: E402
sys.argv = _argv
_spec = importlib.util.spec_from_file_location("te", ROOT / "frontier/B1691_the_exponents_at_the_two_fixed_points/verification/the_exponents.py")
te = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(te)
_spec = importlib.util.spec_from_file_location("c26", ROOT / "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
C26 = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(C26)
COL = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.loads((ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json").read_text(encoding="utf-8"))["points"] if abs(p["tau"][0] - 0.25) < 1e-9)

QI, QJ, QK, EPS = B.QI, B.QJ, B.QK, B.EPS
SECT = {"down": ("Q", "d"), "lep": ("L", "e")}
OUT = {"pin": head, "cells": {}}
LOG = []


def say(*a):
    s = " ".join(str(x) for x in a)
    LOG.append(s)
    print(s, flush=True)


def S_of(t):
    av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
    S = av[0] * QI + av[1] * QJ + av[2] * QK
    return S, EPS @ np.conj(S) @ EPS.T


def Lval(im_t, h):
    k = 1 if h == "L_max" else 2
    return float(np.interp(im_t, [q[0] for q in COL], [q[k] for q in COL]))


def M_of(t, x, y, L):
    """B1726's compute, step by step, for one sector's twists"""
    R = B.residues(x, y, t)
    c = B.cA(x, y, t, R)
    u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
    return B.weighted_M(u), c


def twists(t, a, b, sec):
    lf, rf = SECT[sec]
    w = float(a) * t + float(b)
    return B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf])


def sv(Y):
    return np.linalg.svd(Y, compute_uv=False)


def Q01(M):
    return 4 * abs(M[0, 0]) ** 2 + 2 * abs(M[0, 1]) ** 2 + 2 * abs(M[1, 0]) ** 2 + abs(M[1, 1]) ** 2


def Q10(M):
    return 4 * abs(M[1, 1]) ** 2 + 2 * abs(M[1, 0]) ** 2 + 2 * abs(M[0, 1]) ** 2 + abs(M[0, 0]) ** 2


# the reduction of D3: config -> (mapped b's, S -> S')
def mapped(b, a, sec):
    if (a, sec) == (F(1, 8), "down"):
        return (2 * b, 4 * b), lambda S: S, None
    if (a, sec) == (F(1, 8), "lep"):
        return (-6 * b, 12 * b), lambda S: EPS.T @ S @ EPS, None
    if (a, sec) == (F(3, 8), "down"):
        return (-2 * b, -4 * b), lambda S: EPS.T @ S, "swap"
    if (a, sec) == (F(3, 8), "lep"):
        return (6 * b, -12 * b), lambda S: S @ EPS, "swap"
    raise ValueError


PERM = {"1": "j", "i": "k", "j": "1", "k": "i"}
CONFIGS = [(F(1, 8), "down"), (F(1, 8), "lep"), (F(3, 8), "down"), (F(3, 8), "lep")]

# ------------------------------------------------------------------ C1: the exact identities
rng = np.random.default_rng(512)
c1 = {"D1_max": 0.0, "D3_sv_max": 0.0, "D3_c_max": 0.0, "points": []}
for k in range(6):
    t = complex(rng.uniform(0.0, 1.0), rng.uniform(1.5, 4.0))
    b = float(rng.uniform(0.0, 1.0))
    # D1 on random characteristics
    ax, bx, ay, by = (float(v) for v in rng.uniform(-1.0, 1.0, 4))
    r = rng.uniform(0.05, 0.3, 8); ph = rng.uniform(0.0, 2 * math.pi, 8); u = r * np.exp(1j * ph)
    base = B.bil((ax, bx), (ay, by), u, t)
    xs = B.bil((ax + 0.5, bx), (ay, by), u, t)
    ys = B.bil((ax, bx), (ay + 0.5, by), u, t)
    ng = B.bil((-ax, -bx), (-ay, -by), u, t)
    neg_ref = -B.bil((ax, bx), (ay, by), -u, t)
    d1 = 0.0
    for n in range(8):
        Bn = base[:, :, n]
        d1 = max(d1, np.max(np.abs(xs[:, :, n] - 1j * EPS @ Bn)) / np.max(np.abs(Bn)))
        d1 = max(d1, np.max(np.abs(ys[:, :, n] - Bn @ (-1j * EPS))) / np.max(np.abs(Bn)))
        d1 = max(d1, np.max(np.abs(ng[:, :, n] - neg_ref[:, :, n])) / np.max(np.abs(neg_ref[:, :, n])))
    c1["D1_max"] = max(c1["D1_max"], float(d1))
    # D3 on the four configurations, both readings, both horocycles
    S, St = S_of(t)
    pt = {"tau": [t.real, t.imag], "b": b, "D1": float(d1)}
    for h in ("L_max", "L_2"):
        L = Lval(t.imag, h)
        for (a, sec) in CONFIGS:
            x, y = twists(t, a, b, sec)
            Mc, cc = M_of(t, x, y, L)
            (bx0, by0), Smap, perm = mapped(b, a, sec)
            M0, c0 = M_of(t, (1 / 8, bx0), (1 / 4, by0), L)
            for rn, SS in (("S", S), ("St", St)):
                s1 = sv(B.coupling(SS, Mc)); s2 = sv(B.coupling(Smap(SS), M0))
                c1["D3_sv_max"] = max(c1["D3_sv_max"], float(np.max(np.abs(s1 - s2) / np.abs(s1))))
            for s in B.UNITS:
                ref = c0[PERM[s]] if perm else c0[s]
                c1["D3_c_max"] = max(c1["D3_c_max"], abs(cc[s] - ref) / max(abs(ref), 1.0))
    c1["points"].append(pt)
c1["pass"] = bool(c1["D1_max"] < 1e-10 and c1["D3_sv_max"] < 1e-8 and c1["D3_c_max"] < 1e-8)
OUT["cells"]["C1"] = c1
say("C1 exact identities: D1 max %.2e (< 1e-10), D3 singular values max %.2e (< 1e-8), c_s max %.2e (< 1e-8) -> %s" % (
    c1["D1_max"], c1["D3_sv_max"], c1["D3_c_max"], "PASS" if c1["pass"] else "FAIL"))

# ------------------------------------------------------------------ C2-C4 at the unseen points
c2 = {"max_dev": 0.0, "rows": []}
c3 = {"max_dev": 0.0, "rows": []}
c4 = {"max_dev": 0.0, "rows": []}
IM = 13.0
for re_t in (0.1, 0.6):
    for b in (0.05, 0.4):
        t = complex(re_t, IM)
        S, St = S_of(t)
        inst = {a: C26.compute(re_t, IM, a, b) for a in (F(1, 8), F(3, 8))}
        for h in ("L_max", "L_2"):
            L = Lval(IM, h)
            f = {}
            cbase = None
            for (a, sec) in CONFIGS:
                x, y = twists(t, a, b, sec)
                Mc, cc = M_of(t, x, y, L)
                if (a, sec) == (F(1, 8), "down"):
                    cbase = cc
                for rn, SS, Q in (("S", S, Q01), ("St", St, Q10)):
                    s = sv(B.coupling(SS, Mc))
                    fi = s[1] / s[0]
                    fi_inst = inst[a]["%s|%s|%s" % (sec, h, rn)][0]
                    assert abs(fi / fi_inst - 1) < 1e-12, "replication differs from B1726's compute"
                    ff = 2 * abs(np.linalg.det(Mc)) / Q(Mc)
                    dev = abs(fi_inst / ff - 1)
                    c2["max_dev"] = max(c2["max_dev"], dev)
                    c2["rows"].append({"Re": re_t, "b": b, "h": h, "alpha": str(a), "sec": sec, "reading": rn, "instrument": fi_inst, "formula": ff, "dev": dev})
                    f[(a, sec, rn)] = fi_inst
            R = {(a, rn): f[(a, "lep", rn)] / f[(a, "down", rn)] for a in (F(1, 8), F(3, 8)) for rn in ("S", "St")}
            q_S = R[(F(1, 8), "S")] / R[(F(3, 8), "S")]
            q_St = R[(F(1, 8), "St")] / R[(F(3, 8), "St")]
            p18 = R[(F(1, 8), "S")] * R[(F(1, 8), "St")]
            p38 = R[(F(3, 8), "S")] * R[(F(3, 8), "St")]
            dev3 = max(abs(q_S / 4 - 1), abs(q_St * 4 - 1), abs(p18 - 1), abs(p38 - 1))
            c3["max_dev"] = max(c3["max_dev"], dev3)
            c3["rows"].append({"Re": re_t, "b": b, "h": h, "R2_1/8": R[(F(1, 8), "S")], "R2_3/8": R[(F(3, 8), "S")],
                               "R2t_1/8": R[(F(1, 8), "St")], "R2t_3/8": R[(F(3, 8), "St")], "ratio_S": q_S, "ratio_St": q_St, "prod_1/8": p18, "prod_3/8": p38})
            xv = (2 * math.pi * L + cbase["1"]) / (2 * math.pi * L + (cbase["j"] + cbase["k"]) / 2)
            p1 = (4 + 2 * xv) / (1 + 2 * xv); p3 = (2 + xv) / (2 + 4 * xv)
            dev4 = max(abs(R[(F(1, 8), "S")] / p1 - 1), abs(R[(F(3, 8), "S")] / p3 - 1))
            c4["max_dev"] = max(c4["max_dev"], dev4)
            c4["rows"].append({"Re": re_t, "b": b, "h": h, "L": L, "c1": cbase["1"], "ci": cbase["i"], "cj": cbase["j"], "ck": cbase["k"],
                               "x": xv, "pred_1/8": p1, "pred_3/8": p3, "R2_1/8": R[(F(1, 8), "S")], "R2_3/8": R[(F(3, 8), "S")], "dev": dev4})
            say("  Re %.1f b %.2f %-5s: R2(1/8) %.7f R2(3/8) %.7f ratio %.7f | St ratio %.7f | x %.7f pred %.7f %.7f" % (
                re_t, b, h, R[(F(1, 8), "S")], R[(F(3, 8), "S")], q_S, q_St, xv, p1, p3))
for cell, thr, name in ((c2, 1e-5, "C2 leading formula"), (c3, 1e-5, "C3 the relation"), (c4, 1e-5, "C4 the constant in closed form")):
    cell["pass"] = bool(cell["max_dev"] < thr)
    say("%s: max deviation %.2e (< %.0e) -> %s" % (name, cell["max_dev"], thr, "PASS" if cell["pass"] else "FAIL"))
OUT["cells"]["C2"] = c2; OUT["cells"]["C3"] = c3; OUT["cells"]["C4"] = c4


# ------------------------------------------------------------------ C5-C6: the slopes (exact arithmetic) and the integer limits
def nn(v):
    v = v % 1
    return min(v, 1 - v)


def charges(nc):
    return {"Q": 1, "u": -(nc + 1), "d": nc - 1, "L": -nc, "e": 2 * nc, "H": nc}


def e2(qL, qR, a):
    return F(1, 2) - (nn(2 * qL * a) + nn(2 * qR * a)) / 2


def slopes(nc):
    q = charges(nc); out = []
    for N in range(1, 31):
        for j in range(0, N // 2 + 1):
            a = F(j, N)
            if a.denominator == N and e2(q["Q"], q["d"], a) == e2(q["L"], q["e"], a):
                out.append(a)
    return out


def blocks_E(qL, qR, a):
    return {(i, j): nn(qL * a + F(i, 2)) ** 2 + nn(qR * a + F(j, 2)) ** 2 for i in (0, 1) for j in (0, 1)}


def dominant(qL, qR, a):
    E = blocks_E(qL, qR, a); m = min(E.values()); arg = [p for p, v in E.items() if v == m]
    return arg


MULT_S = {(0, 0): 4, (0, 1): 2, (1, 0): 2, (1, 1): 1}
MULT_ST = {(1, 1): 4, (0, 1): 2, (1, 0): 2, (0, 0): 1}

ties = []
for a in slopes(3):
    if a in (0, F(1, 2)):
        continue
    q = charges(3)
    if len(dominant(q["Q"], q["d"], a)) > 1 or len(dominant(q["L"], q["e"], a)) > 1:
        ties.append(str(a))
c5 = {"ties": ties, "predicted": ["1/12", "1/8", "1/4", "3/8", "5/12"]}
c5["pass"] = sorted(ties, key=lambda s: F(s)) == sorted(c5["predicted"], key=lambda s: F(s))
OUT["cells"]["C5"] = c5
say("C5 ties among N_c = 3's equal-exponent slopes: %s (predicted %s) -> %s" % (ties, c5["predicted"], "PASS" if c5["pass"] else "FAIL"))

rows = [json.loads(l) for l in (ROOT / "frontier/B1817_the_frames_own_lepton_down_factor_at_the_cusp/verification/a1_cusp_map.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
idx = {}
for r in rows:
    if "error" in r:
        continue
    idx[(r["nc"], r["alpha"], r["b"], r["Im"])] = r
c6 = {"graded": [], "not_graded": []}
for nc in (2, 3, 4, 5):
    q = charges(nc)
    for a in slopes(nc):
        if a in (0, F(1, 2)):
            continue
        dd = dominant(q["Q"], q["d"], a); dl = dominant(q["L"], q["e"], a)
        rec = {"nc": nc, "alpha": str(a), "p_down": [list(p) for p in dd], "p_lep": [list(p) for p in dl],
               "e_down": str(e2(q["Q"], q["d"], a)), "e_lep": str(e2(q["L"], q["e"], a))}
        if len(dd) > 1 or len(dl) > 1:
            rec["why"] = "tie"; c6["not_graded"].append(rec); continue
        if e2(q["Q"], q["d"], a) >= F(1, 2) or e2(q["L"], q["e"], a) >= F(1, 2):
            rec["why"] = "e = 1/2 branch"; c6["not_graded"].append(rec); continue
        pd, pl = dd[0], dl[0]
        pred = {"S": F(MULT_S[pd], MULT_S[pl]), "St": F(MULT_ST[pd], MULT_ST[pl])}
        rec["pred_S"] = str(pred["S"]); rec["pred_St"] = str(pred["St"])
        vals = {}
        ok_data = True
        for bb in (0.137, 0.311):
            for y in (10.0, 12.0):
                r = idx.get((nc, str(a), bb, y))
                if r is None:
                    ok_data = False; continue
                for rn in ("S", "St"):
                    vals[(bb, y, rn)] = r["L_max|%s" % rn]["R2"]
        rec["R2_Im12"] = {"%s|%s" % (bb, rn): vals.get((bb, 12.0, rn)) for bb in (0.137, 0.311) for rn in ("S", "St")}
        if not ok_data or any(v is None or not (v > 0) for v in vals.values()):
            rec["why"] = "missing or non-positive rows"; c6["not_graded"].append(rec); continue
        conv = all(abs(vals[(bb, 12.0, rn)] / vals[(bb, 10.0, rn)] - 1) < 1e-3 for bb in (0.137, 0.311) for rn in ("S", "St"))
        bind = all(abs(vals[(0.137, 12.0, rn)] / vals[(0.311, 12.0, rn)] - 1) < 1e-3 for rn in ("S", "St"))
        if not (conv and bind):
            rec["why"] = "not a converged constant (conv %s, b-independent %s)" % (conv, bind); c6["not_graded"].append(rec); continue
        dev = max(abs(vals[(bb, 12.0, rn)] / float(pred[rn]) - 1) for bb in (0.137, 0.311) for rn in ("S", "St"))
        rec["dev"] = dev; rec["agrees"] = bool(dev < 0.01)
        c6["graded"].append(rec)
c6["pass"] = bool(len(c6["graded"]) > 0 and all(r["agrees"] for r in c6["graded"]))
OUT["cells"]["C6"] = c6
say("C6 integer limits as multiplicity ratios: %d graded slopes, %d agree; %d not graded -> %s" % (
    len(c6["graded"]), sum(r["agrees"] for r in c6["graded"]), len(c6["not_graded"]), "PASS" if c6["pass"] else "FAIL"))
for r in c6["graded"]:
    say("   N_c %d alpha %-6s p_d %s p_l %s pred S %-4s St %-4s R2(12) %s dev %.2e %s" % (
        r["nc"], r["alpha"], r["p_down"][0], r["p_lep"][0], r["pred_S"], r["pred_St"],
        {k: (round(v, 6) if v else v) for k, v in r["R2_Im12"].items()}, r["dev"], "agrees" if r["agrees"] else "DISAGREES"))
for r in c6["not_graded"]:
    say("   not graded: N_c %d alpha %-6s (%s)" % (r["nc"], r["alpha"], r["why"]))

OUT["verdicts"] = {k: v["pass"] for k, v in OUT["cells"].items()}
(HERE / "p512_check_out.json").write_text(json.dumps(OUT, indent=1, default=str), encoding="utf-8")
say("verdicts:", OUT["verdicts"])
