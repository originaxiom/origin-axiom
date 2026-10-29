#!/usr/bin/env python3
"""W180 — the cusp limits on the integer-lambda lines (the rule: W180_RULE.md, committed and pushed before this script).
It runs once, from the repository root, on four worker processes.

On the 49 resolved census lines with an integer-lambda kernel (a in {0, 1/6, 1/3, 1/2}), W177's norm splits as
c_s = c_inf + B_s Im tau + rho_s, with B_s = 4 pi^2 / |1 - W_s Q^{-l0}|^2 for an integer lambda_s = l0 (0 otherwise)
and rho_s exponentially small.  W178's frame, unchanged in every other piece (residues, kappa, DR, L, coupling,
readings, no cut, the theta-zero rule, its two precisions and status rule), is read in two forms:
  the frozen frame  F(y, Y): each norm replaced by c_inf + B_s Y, at Im tau y in {48, 64}, Y in the ladder
  the limit frame   F_inf:   weight sqrt(B_s) on the integer channels and no other channel, at Im tau 48 and 64
on both Re tau, 16 points per pair, 98 pairs.

  H0  the tie: F(48, 48) agrees with W178's stored six at Im tau 48 within 1e-6 (ln), every feature resolved in both
  H1  frozen exponents e(Y) = -[f(64, Y) - f(48, Y)] / (2 pi 16) agree over the seven Y within 1e-6
  H2  each such exponent lies within 1e-6 of a fraction with denominator at most 60
  H3  the interchange: ln D of F(64, Y), Y = 64, 96, 128, against W179 post hoc 1's true ln D, within 1e-6
  H4  on agreeing pairs: F_inf's exponents equal the frozen ones, its ln D agrees at 48 and 64, and
      |ln D(64, Y) - ln D_inf| does not increase along Y = 128, 256, 1024, 4096 (1e-12 allowed)
  H5  no pair's D_inf in the data's 3-sigma window
  H6  D_inf on (1/2, 1/5) and (1/2, 3/10) in [6.5, 7.7] at both Re tau
  H7  the agreeing pairs are exactly W179's finite pairs on integer-lambda lines
  R   read-outs

    python3 -B docs/dossiers/the_weave_2026-10-07/the_integer_lambda_limits.py

Disclosed: a timing call on this script's draft, after the rule was pushed and before this commit, ran four points
((1/2, 1/5) frozen at Im tau 48 with Y = 4096 and the limit frame at 64; (0, 0) limit frame at 48; (0, 1/11) frozen at
64 with Y = 48) and printed only the statuses, digits and seconds (all resolved; 2.8 to 4.7 s; no failure).  No value
was printed or read.
"""
import contextlib
import io
import json
import math
import multiprocessing as mpc
import platform
import sys
import time
import traceback
import warnings
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_six_at_the_cusp as W178          # noqa: E402  (W178: the frame in working precision, its output)
T8, W93, W162, W177 = W178.T8, W178.W93, W178.W162, W178.W177
mp = W177.mp
OUT = HERE / "the_integer_lambda_limits.json"
XS = W178.XS
HEIGHTS = (48.0, 64.0)
YS = (48.0, 64.0, 96.0, 128.0, 256.0, 1024.0, 4096.0)
TOL = 1e-6
FLAT = 1e-12
DEN = 60
SIGMAS = 3
BOX = (6.5, 7.7)
G2_LINES = (("1/2", "1/5"), ("1/2", "3/10"))
WORKERS = 4
DOWN2, DOWN1, LEP2, LEP1 = 2, 3, 4, 5
AGREE_Y = 1024.0


# ============================================================================================ the frozen and limit frames
def split(s, ub, t):
    """(c_inf, B_s) of W177's series for theta_s at ub: B_s > 0 exactly when lambda_s is an integer"""
    lam, w = W177.lam_w(s, ub, t)
    base = -2 * mp.pi * mp.log(2 * mp.pi) - 2 * mp.pi * mp.euler
    if abs(lam - mp.nint(lam)) < mp.mpf(10) ** -30:
        l0 = int(mp.nint(lam))
        W, Q = mp.exp(2j * mp.pi * w), mp.exp(2j * mp.pi * t)
        return base - 2 * mp.pi * mp.digamma(1), 4 * mp.pi ** 2 / abs(1 - W * Q ** (-l0)) ** 2
    lp = lam - mp.floor(lam)
    return base - mp.pi * (mp.digamma(lp) + mp.digamma(1 - lp)), mp.mpf(0)


def six_frozen(line, x, y, p, mode, Yn):
    """W178's six_at (no cut) with the norms frozen at c_inf + B_s Yn ('frozen') or the limit weights ('limit')"""
    a, b = line
    with mp.workdps(p):
        CM, EPSM, _BLK, EM = W93.units("mp")
        t = mp.mpc(mp.mpf(x), mp.mpf(y))
        dr = W178.DR_mp(t, p)
        S = dr[0] * CM["i"] + dr[1] * CM["j"] + dr[2] * CM["k"]
        reads = {"S": S, "St": EPSM * W178.mat_conj(S) * EPSM.T}
        Lv = mp.mpf(W162.L_of(W178._G["col"], y, "L_max"))
        lnr = []
        for sec, rd in W178.READ:
            qL, qR = T8.charges(W93, sec)
            R = W93.residues((a, -b), sec, t)
            k = T8.kappa(qL, qR, a, b, t)
            ub = (qL + qR) * (mp.mpf(a.numerator) / a.denominator * t + mp.mpf(b.numerator) / b.denominator)
            M = mp.zeros(2, 2)
            for s in T8.UNITS:
                th = W178.W89TH[s]
                if W178.theta_zero(th, line, qL + qR):
                    continue
                cinf, B = split(th, ub, t)
                if mode == "frozen":
                    w = 2 * mp.pi * Lv + cinf + B * mp.mpf(Yn)
                elif B > 0:
                    w = B
                else:
                    continue
                if w > 0:
                    M += mp.sqrt(w) * k * R[s] * EM[s]
            Yc = W93.coupling_mp(reads[rd], M)
            sv = sorted((abs(v) for v in mp.svd_c(Yc, compute_uv=False)), reverse=True)
            for j in (1, 2):
                lnr.append(sv[j] / sv[0] if sv[0] > 0 else mp.mpf(0))
        return ([float(mp.log(r)) if r > 0 else -math.inf for r in lnr],
                [float(mp.log10(r)) if r > 0 else -math.inf for r in lnr])


def point(task):
    """(k, x, y, mode, Yn) -> the six by W178's two precisions and status rule (doubled once if needed)"""
    k, x, y, mode, Yn = task
    line = W178._G["lines"][k]
    t0 = time.time()
    try:
        p1, p2 = W178.precisions(y)
        status = None
        for attempt in (1, 2):
            f1, l1 = six_frozen(line, x, y, p1, mode, Yn)
            f2, l2 = six_frozen(line, x, y, p2, mode, Yn)
            status = []
            for i in range(6):
                if math.isfinite(f1[i]) and math.isfinite(f2[i]) and abs(f1[i] - f2[i]) <= W178.AGREE:
                    status.append("resolved")
                elif l1[i] <= -(p1 - 30) and l2[i] <= -(p2 - 30):
                    status.append("zero at working precision")
                else:
                    status.append("unresolved")
            if all(s != "unresolved" for s in status) or attempt == 2:
                break
            p1, p2 = 2 * p1, 2 * p2
        six = [f2[i] if status[i] == "resolved" else None for i in range(6)]
        spread = max((abs(f1[i] - f2[i]) for i in range(6) if status[i] == "resolved"), default=0.0)
        return {"k": k, "x": x, "y": y, "mode": mode, "Y": Yn, "six": six, "status": status, "digits": [p1, p2],
                "two-precision spread": spread, "seconds": round(time.time() - t0, 2)}
    except Exception:  # noqa: BLE001  (a failed task is kept and disclosed)
        return {"k": k, "x": x, "y": y, "mode": mode, "Y": Yn,
                "failed": W178.sanitize(traceback.format_exc()[-1500:])}


# ============================================================================================ the analysis
def doubles(six):
    if six is None or any(six[i] is None for i in (DOWN2, DOWN1, LEP2, LEP1)):
        return None
    l2, l1 = six[DOWN2] - six[LEP2], six[DOWN1] - six[LEP1]
    return [l2, l1, l1 - l2]


def expo(lo, hi):
    """per feature: -(f(64) - f(48)) / (2 pi 16), or None"""
    if lo is None or hi is None:
        return [None] * 6
    return [None if (u is None or v is None) else -(v - u) / (2 * math.pi * (HEIGHTS[1] - HEIGHTS[0]))
            for u, v in zip(lo, hi)]


def near_fraction(e):
    f = Fr(e).limit_denominator(DEN)
    return f, abs(e - float(f))


def half_power(p):
    h = round(2 * p) / 2
    return h, abs(p - h)


def run(out, pool):
    w178 = json.loads((HERE / "the_six_at_the_cusp.json").read_text(encoding="utf-8"))
    w179 = json.loads((HERE / "the_down_lepton_factor.json").read_text(encoding="utf-8"))
    post = json.loads((HERE / "the_down_lepton_factor_posthoc.json").read_text(encoding="utf-8"))
    lines = W178._G["lines"]
    ks = [k for k, e in enumerate(w178["per line"])
          if e["slowest kernel min(l+, l-)"] == 0.0 and not any(p.get("zero channel") for p in e["per Re tau"])]
    out["pairs"] = {"lines": len(ks), "pairs": 2 * len(ks)}
    tasks = [(k, x, y, "frozen", Yn) for k in ks for x in XS for y in HEIGHTS for Yn in YS]
    tasks += [(k, x, y, "limit", None) for k in ks for x in XS for y in HEIGHTS]
    out["tasks"] = len(tasks)
    t0 = time.time()
    res, n = {}, 0
    for r in pool.imap_unordered(point, tasks, chunksize=1):
        res[(r["k"], r["x"], r["y"], r["mode"], r["Y"])] = r
        n += 1
        if n % 200 == 1:
            print(f"point {n}/{len(tasks)} at {round(time.time() - t0)} s", flush=True)
    out["compute seconds"] = round(time.time() - t0, 1)
    failed = [[r["k"], r["x"], r["y"], r["mode"], r["Y"], r["failed"]] for r in res.values() if "failed" in r]
    out["failed tasks"] = failed
    out["doubled-precision tasks"] = sum(1 for r in res.values() if "digits" in r
                                         and r["digits"][0] > W178.precisions(r["y"])[0])
    ahs = json.loads((HERE / "received" / "AHS2026_double_ratio.json").read_text(encoding="utf-8"))["the double ratio"]
    data = {"D": float(ahs["value"]), "sigma D": float(ahs["sigma"])}
    data["ln D"] = math.log(data["D"])
    out["the data (read once)"] = data
    lo, hi = data["D"] - SIGMAS * data["sigma D"], data["D"] + SIGMAS * data["sigma D"]
    w179_finite = {(tuple(e["line"]), r["x"]) for e in w179["per line"] for r in e["cusp"] if r["status"] == "finite"}
    post_lnD = {tuple(e["line"]): {r[0]: math.log(r[1]) for r in e["D per height"] if r[1] is not None}
                for e in post["per line"]}
    six = lambda k, x, y, mode, Yn: (res[(k, x, y, mode, Yn)].get("six") if (k, x, y, mode, Yn) in res else None)
    per, h0_bad, h1_bad, h2_bad, h3_rows, h4_bad, h5_hits, h6_rows = [], [], [], [], [], [], [], []
    agreeing, h0_n, h1_n = set(), 0, 0
    for k in ks:
        line = lines[k]
        key = (str(line[0]), str(line[1]))
        e178 = w178["per line"][k]
        assert e178["line"] == list(key)
        for xi, x in enumerate(XS):
            p178 = e178["per Re tau"][xi]
            assert p178["x"] == x
            row = {"line": list(key), "x": x}
            # H0: the tie
            mine, stored = six(k, x, 48.0, "frozen", 48.0), p178["six per height"]["48.0"]
            if mine is not None:
                d = [abs(u - v) for u, v in zip(mine, stored) if u is not None and v is not None]
                h0_n += len(d)
                row["H0 worst"] = max(d) if d else None
                if d and max(d) > TOL:
                    h0_bad.append([list(key), x, max(d)])
            # exponents per Y
            ex = {Yn: expo(six(k, x, 48.0, "frozen", Yn), six(k, x, 64.0, "frozen", Yn)) for Yn in YS}
            row["frozen exponents at Y = 1024"] = ex[AGREE_Y]
            spreads, fracs = [], []
            for i in range(6):
                vals = [ex[Yn][i] for Yn in YS]
                if any(v is None for v in vals):
                    continue
                h1_n += 1
                spreads.append(max(vals) - min(vals))
                if spreads[-1] > TOL:
                    h1_bad.append([list(key), x, i, spreads[-1]])
                f, dev = near_fraction(ex[AGREE_Y][i])
                fracs.append([i, str(f), dev])
                if dev > TOL:
                    h2_bad.append([list(key), x, i, ex[AGREE_Y][i], str(f), dev])
            row["exponent spread over Y"] = spreads
            row["nearest fractions"] = fracs
            # powers of Y at Im tau 64
            fa, fb = six(k, x, 64.0, "frozen", 1024.0), six(k, x, 64.0, "frozen", 4096.0)
            if fa is not None and fb is not None:
                row["power of Y per feature (1024 to 4096)"] = [
                    None if (u is None or v is None) else [(v - u) / math.log(4), *half_power((v - u) / math.log(4))]
                    for u, v in zip(fa, fb)]
            # agreement and D
            e = ex[AGREE_Y]
            ok = all(e[i] is not None for i in (DOWN2, DOWN1, LEP2, LEP1))
            agree = ok and abs(e[DOWN2] - e[LEP2]) <= TOL and abs(e[DOWN1] - e[LEP1]) <= TOL
            row["exponents agree"] = bool(agree) if ok else None
            lnD = {}
            for Yn in YS:
                v = doubles(six(k, x, 64.0, "frozen", Yn))
                lnD[Yn] = v
            row["ln (r2, r1, D) at Im tau 64 per Y"] = {str(Yn): v for Yn, v in lnD.items()}
            if key in G2_LINES and x == XS[0]:
                for Yn in (64.0, 96.0, 128.0):
                    truth = post_lnD[key].get(Yn)
                    got = lnD[Yn][2] if lnD[Yn] is not None else None
                    h3_rows.append([list(key), x, Yn, got, truth,
                                    None if (got is None or truth is None) else abs(got - truth)])
            if agree:
                agreeing.add((key, x))
                inf48, inf64 = six(k, x, 48.0, "limit", None), six(k, x, 64.0, "limit", None)
                einf = expo(inf48, inf64)
                dinf48, dinf64 = doubles(inf48), doubles(inf64)
                why = []
                if any(einf[i] is None or abs(einf[i] - e[i]) > TOL for i in (DOWN2, DOWN1, LEP2, LEP1)):
                    why.append("limit-frame exponents differ")
                if dinf48 is None or dinf64 is None or abs(dinf64[2] - dinf48[2]) > TOL:
                    why.append("limit-frame ln D not settled")
                if dinf64 is not None and all(lnD[Yn] is not None for Yn in YS):
                    dist = [abs(lnD[Yn][2] - dinf64[2]) for Yn in (128.0, 256.0, 1024.0, 4096.0)]
                    row["|ln D(64, Y) - ln D_inf|, Y = 128, 256, 1024, 4096"] = dist
                    if any(b > a + FLAT for a, b in zip(dist, dist[1:])):
                        why.append("approach not monotone")
                else:
                    why.append("ladder incomplete")
                row["limit frame exponents"] = einf
                if not why:
                    row["H4"] = "holds"
                    row["D_inf"] = math.exp(dinf64[2])
                    row["r2_inf, r1_inf"] = [math.exp(dinf64[0]), math.exp(dinf64[1])]
                    value, flag = row["D_inf"], False
                else:
                    row["H4"] = why
                    h4_bad.append([list(key), x, why])
                    value = math.exp(lnD[4096.0][2]) if lnD[4096.0] is not None else None
                    row["D at Y = 4096 (flagged)"] = value
                    flag = True
                if value is not None and lo <= value <= hi:
                    h5_hits.append([list(key), x, value, "flagged" if flag else "D_inf"])
                if key in G2_LINES:
                    h6_rows.append([list(key), x, value, flag])
            # W178's local cusp exponent against the frozen one and the power of Y
            pw = row.get("power of Y per feature (1024 to 4096)")
            if pw is not None:
                row["W178 e(32,48) minus frozen e, beside -p ln(3/2)/(2 pi 16)"] = [
                    None if (e[i] is None or pw[i] is None) else
                    [p178["cusp pattern e(32,48)"][i] - e[i], -pw[i][0] * math.log(1.5) / (2 * math.pi * 16)]
                    for i in range(6)]
            per.append(row)
    out["per pair"] = per
    out["H0"] = {"features compared": h0_n, "misses": h0_bad, "holds": bool(h0_n and not h0_bad)}
    out["H1"] = {"features": h1_n, "misses": h1_bad, "holds": bool(h1_n and not h1_bad)}
    out["H2"] = {"features": h1_n, "misses": h2_bad, "holds": bool(h1_n and not h2_bad)}
    out["H3"] = {"rows (line, x, Y, ln D frozen, ln D true, |difference|)": h3_rows,
                 "holds": bool(len(h3_rows) == 6 and all(r[5] is not None and r[5] <= TOL for r in h3_rows))}
    out["H4"] = {"agreeing pairs": len(agreeing), "misses": h4_bad, "holds": bool(agreeing and not h4_bad)}
    out["H5"] = {"window": [lo, hi], "hits": h5_hits, "holds": bool(not h5_hits)}
    out["H6"] = {"box": list(BOX), "rows (line, x, value, flagged)": h6_rows,
                 "holds": bool(len(h6_rows) == 4 and all(r[2] is not None and not r[3] and BOX[0] <= r[2] <= BOX[1]
                                                         for r in h6_rows))}
    ilam = {(tuple(e["line"]), x) for e in w178["per line"] if e["slowest kernel min(l+, l-)"] == 0.0 for x in XS}
    w179_int = {q for q in w179_finite if q in ilam}
    out["H7"] = {"agreeing pairs": len(agreeing), "W179 finite pairs on integer-lambda lines": len(w179_int),
                 "agreeing, not finite in W179": sorted([list(q[0]), q[1]] for q in agreeing - w179_int),
                 "finite in W179, not agreeing": sorted([list(q[0]), q[1]] for q in w179_int - agreeing),
                 "holds": bool(agreeing == w179_int)}
    vals = [(r["line"], r["x"], r["D_inf"]) for r in per if "D_inf" in r]
    out["R: distinct D_inf (to 1e-6)"] = sorted({round(v, 6) for _l, _x, v in vals})
    out["R: ten nearest to the data's D"] = sorted(vals, key=lambda q: abs(math.log(q[2]) - data["ln D"]))[:10]
    out["R: agreeing pairs with D_inf = 1 (|ln D_inf| <= 1e-12)"] = sum(1 for _l, _x, v in vals
                                                                      if abs(math.log(v)) <= FLAT)
    out["cells"] = {c: out[c]["holds"] for c in ("H0", "H1", "H2", "H3", "H4", "H5", "H6", "H7")}


def main():
    t0 = time.time()
    out = {"arc": "W180", "rule": "W180_RULE.md", "python": platform.python_version(), "workers": WORKERS,
           "frame": "W178's (the_six_at_the_cusp.py), its norms frozen or at the limit weights"}
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            with mpc.get_context("fork").Pool(WORKERS, initializer=W178._init, initargs=(str(ROOT),)) as pool:
                W178._init(str(ROOT))
                run(out, pool)
        except Exception:  # noqa: BLE001  (a failed run still writes what it has)
            out["run_failed"] = W178.sanitize(traceback.format_exc()[-3000:])
    out["warnings"] = sorted({f"{w.category.__name__}: {w.message}" for w in caught})
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name, "in", out["seconds"], "s;", len(out["warnings"]), "distinct warnings")


if __name__ == "__main__":
    main()
