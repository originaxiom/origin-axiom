#!/usr/bin/env python3
"""W181 — the cusp limits on the integer-lambda lines in the exact norms (the rule: W181_RULE.md, committed and pushed
before this script).  It runs once, from the repository root, on four worker processes.

The shifted frame F(y, Y) is W178's frame at Im tau = y (its residues, kappa, DR, L, coupling and readings, no cut, the
theta-zero rule), with each norm replaced by c_s(y) + B_s (Y - y): c_s(y) W177's exact series at Im tau y, B_s W180's
split coefficient (4 pi^2 / |1 - W_s Q^{-l0}|^2 on an integer channel, 0 otherwise).  F(y, y) is the true frame.  On
the 49 resolved census lines with an integer-lambda kernel, at Re tau 1/8 and 3/8 (98 pairs), it is read at
Im tau 48, 64, 96 and 128 and at Y = 48 ... 262144, the frame's pieces computed once per pair and height.

  K0  the tie: F(48, 48) against W178's stored six at Im tau 48 within 1e-6 (ln), every feature resolved in both
  K1  the truth on the G2 lines: ln D of F(y, y), y = 64, 96, 128, at Re tau 1/8, against W179 post hoc 1, 1e-6
  K2  the G2 control: ln D of F(64, Y) against W180's frozen ln D at Im tau 64, Y = 48 ... 4096, both Re tau, 1e-6
  K3  the y-limit: on every agreeing pair, |ln D(128, Y) - ln D(96, Y)| <= 1e-8 at every Y
  K4  the Y-limit: on every agreeing pair, Neville's extrapolation of ln D(128, Y) in u = Y^{-1/2} to u = 0 over the
      six Y = 256 ... 262144 (N6) and over the top five (N5) agree within 1e-6
  K5  the agreeing pairs are exactly W179's finite pairs on integer-lambda lines
  K6  the twelve ties: |ln D| <= 1e-12 at every height and Y on W179's settled integer-lambda pairs
  K7  no accepted D_inf in the data's 3-sigma window
  K8  D_inf on (1/2, 1/5) and (1/2, 3/10) accepted and in [6.0, 6.6] at both Re tau
  R   read-outs

    python3 -B docs/dossiers/the_weave_2026-10-07/the_exact_norm_limits.py

Disclosed: a timing call on this script, after the rule was pushed and before this commit, ran two tasks at Re tau 1/8
((0, 0) at Im tau 128 and (0, 1/11) at Im tau 48, each with its ten Y) and printed only the statuses, digits and
seconds (all resolved; 57.5 s and 5.1 s; no failure).  No value was printed or read.
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
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_integer_lambda_limits as W180    # noqa: E402  (W180: the split's B_s; through it W178, W177, W93, T8)
W178, T8, W93, W162, W177 = W180.W178, W180.T8, W180.W93, W180.W162, W180.W177
mp = W177.mp
OUT = HERE / "the_exact_norm_limits.json"
XS = W178.XS
HEIGHTS = (48.0, 64.0, 96.0, 128.0)
YS = (48.0, 64.0, 96.0, 128.0, 256.0, 1024.0, 4096.0, 16384.0, 65536.0, 262144.0)
EXT = (256.0, 1024.0, 4096.0, 16384.0, 65536.0, 262144.0)
K2_YS = (48.0, 64.0, 96.0, 128.0, 256.0, 1024.0, 4096.0)
LO_H, HI_H = 96.0, 128.0
AGREE_Y = 1024.0
PAD = 40
TOL = 1e-6
YTOL = 1e-8
TIE = 1e-12
SIGMAS = 3
BOX = (6.0, 6.6)
G2_LINES = (("1/2", "1/5"), ("1/2", "3/10"))
WORKERS = 4
DOWN2, DOWN1, LEP2, LEP1 = 2, 3, 4, 5


# ============================================================================================ the shifted frame
def precisions(y):
    """W178's two precisions at Im tau y, each with PAD more digits (for the powers of Y)"""
    p1, p2 = W178.precisions(y)
    return p1 + PAD, p2 + PAD


def six_shifted(line, x, y, p):
    """W178's six_at (no cut) with each norm c_s(y) + B_s (Y - y), for every Y in YS: {Y: (ln list, log10 list)}"""
    a, b = line
    with mp.workdps(p):
        CM, EPSM, _BLK, EM = W93.units("mp")
        t = mp.mpc(mp.mpf(x), mp.mpf(y))
        dr = W178.DR_mp(t, p)
        S = dr[0] * CM["i"] + dr[1] * CM["j"] + dr[2] * CM["k"]
        reads = {"S": S, "St": EPSM * W178.mat_conj(S) * EPSM.T}
        Lv = mp.mpf(W162.L_of(W178._G["col"], y, "L_max"))
        pieces = []
        for sec, rd in W178.READ:
            qL, qR = T8.charges(W93, sec)
            R = W93.residues((a, -b), sec, t)
            k = T8.kappa(qL, qR, a, b, t)
            ub = (qL + qR) * (mp.mpf(a.numerator) / a.denominator * t + mp.mpf(b.numerator) / b.denominator)
            chans = []
            for s in T8.UNITS:
                th = W178.W89TH[s]
                if W178.theta_zero(th, line, qL + qR):
                    continue
                w0 = 2 * mp.pi * Lv + W177.c_series(th, ub, t)
                _cinf, B = W180.split(th, ub, t)
                chans.append((w0, B, k * R[s], EM[s]))
            pieces.append((rd, chans))
        out = {}
        for Yn in YS:
            shift = mp.mpf(Yn) - mp.mpf(y)
            lnr = []
            for rd, chans in pieces:
                M = mp.zeros(2, 2)
                for w0, B, Rs, Es in chans:
                    w = w0 + B * shift
                    if w > 0:
                        M += mp.sqrt(w) * Rs * Es
                Yc = W93.coupling_mp(reads[rd], M)
                sv = sorted((abs(v) for v in mp.svd_c(Yc, compute_uv=False)), reverse=True)
                for j in (1, 2):
                    lnr.append(sv[j] / sv[0] if sv[0] > 0 else mp.mpf(0))
            out[Yn] = ([float(mp.log(r)) if r > 0 else -math.inf for r in lnr],
                       [float(mp.log10(r)) if r > 0 else -math.inf for r in lnr])
        return out


def point(task):
    """(k, x, y) -> the six at every Y by W178's two precisions (padded) and status rule (doubled once if needed)"""
    k, x, y = task
    line = W178._G["lines"][k]
    t0 = time.time()
    try:
        p1, p2 = precisions(y)
        status = None
        for attempt in (1, 2):
            r1 = six_shifted(line, x, y, p1)
            r2 = six_shifted(line, x, y, p2)
            status = {}
            for Yn in YS:
                (f1, l1), (f2, l2) = r1[Yn], r2[Yn]
                st = []
                for i in range(6):
                    if math.isfinite(f1[i]) and math.isfinite(f2[i]) and abs(f1[i] - f2[i]) <= W178.AGREE:
                        st.append("resolved")
                    elif l1[i] <= -(p1 - 30) and l2[i] <= -(p2 - 30):
                        st.append("zero at working precision")
                    else:
                        st.append("unresolved")
                status[Yn] = st
            if all(s != "unresolved" for st in status.values() for s in st) or attempt == 2:
                break
            p1, p2 = 2 * p1, 2 * p2
        six = {Yn: [r2[Yn][0][i] if status[Yn][i] == "resolved" else None for i in range(6)] for Yn in YS}
        spread = max((abs(r1[Yn][0][i] - r2[Yn][0][i]) for Yn in YS for i in range(6)
                      if status[Yn][i] == "resolved"), default=0.0)
        return {"k": k, "x": x, "y": y, "six": six, "status": status, "digits": [p1, p2],
                "two-precision spread": spread, "seconds": round(time.time() - t0, 2)}
    except Exception:  # noqa: BLE001  (a failed task is kept and disclosed)
        return {"k": k, "x": x, "y": y, "failed": W178.sanitize(traceback.format_exc()[-1500:])}


# ============================================================================================ the analysis
def doubles(six):
    if six is None or any(six[i] is None for i in (DOWN2, DOWN1, LEP2, LEP1)):
        return None
    l2, l1 = six[DOWN2] - six[LEP2], six[DOWN1] - six[LEP1]
    return [l2, l1, l1 - l2]


def expo(lo, hi):
    """per feature: -(f(128) - f(96)) / (2 pi 32), or None"""
    if lo is None or hi is None:
        return [None] * 6
    return [None if (u is None or v is None) else -(v - u) / (2 * math.pi * (HI_H - LO_H)) for u, v in zip(lo, hi)]


def neville(xs, ys, x0=0.0):
    """the value at x0 of the polynomial through (xs, ys), by Neville's recursion"""
    P = list(ys)
    n = len(xs)
    for m in range(1, n):
        for i in range(n - m):
            P[i] = ((x0 - xs[i + m]) * P[i] + (xs[i] - x0) * P[i + 1]) / (xs[i] - xs[i + m])
    return P[0]


def compact_status(st):
    code = {"resolved": "r", "zero at working precision": "z", "unresolved": "u"}
    return "".join(code[s] for s in st)


def run(out, pool):
    w178 = json.loads((HERE / "the_six_at_the_cusp.json").read_text(encoding="utf-8"))
    w179 = json.loads((HERE / "the_down_lepton_factor.json").read_text(encoding="utf-8"))
    post = json.loads((HERE / "the_down_lepton_factor_posthoc.json").read_text(encoding="utf-8"))
    w180 = json.loads((HERE / "the_integer_lambda_limits.json").read_text(encoding="utf-8"))
    lines = W178._G["lines"]
    ks = [k for k, e in enumerate(w178["per line"])
          if e["slowest kernel min(l+, l-)"] == 0.0 and not any(p.get("zero channel") for p in e["per Re tau"])]
    out["pairs"] = {"lines": len(ks), "pairs": 2 * len(ks)}
    tasks = sorted(((k, x, y) for k in ks for x in XS for y in HEIGHTS), key=lambda q: -q[2])
    out["tasks"] = len(tasks)
    t0 = time.time()
    res, n = {}, 0
    for r in pool.imap_unordered(point, tasks, chunksize=1):
        res[(r["k"], r["x"], r["y"])] = r
        n += 1
        if n % 20 == 1:
            print(f"task {n}/{len(tasks)} at {round(time.time() - t0)} s", flush=True)
    out["compute seconds"] = round(time.time() - t0, 1)
    out["failed tasks"] = [[r["k"], r["x"], r["y"], r["failed"]] for r in res.values() if "failed" in r]
    out["doubled-precision tasks"] = sum(1 for r in res.values() if "digits" in r
                                         and r["digits"][0] > precisions(r["y"])[0])
    ahs = json.loads((HERE / "received" / "AHS2026_double_ratio.json").read_text(encoding="utf-8"))["the double ratio"]
    data = {"D": float(ahs["value"]), "sigma D": float(ahs["sigma"])}
    data["ln D"] = math.log(data["D"])
    out["the data (read once)"] = data
    lo, hi = data["D"] - SIGMAS * data["sigma D"], data["D"] + SIGMAS * data["sigma D"]
    # W179's subsets of the 98 pairs
    g0 = {(tuple(r[0]), r[1]) for r in w179["G0"]["not settled"]}
    finite = {(tuple(e["line"]), r["x"]) for e in w179["per line"] for r in e["cusp"] if r["status"] == "finite"}
    ilam = {(tuple(w178["per line"][k]["line"]), x) for k in ks for x in XS}
    w179_int = finite & ilam
    settled = w179_int - g0
    out["subsets (W179)"] = {"unsettled (G0)": len(g0 & ilam), "settled": len(settled),
                             "finite on integer-lambda lines": len(w179_int), "running": len(ilam - finite)}
    post_lnD = {tuple(e["line"]): {r[0]: math.log(r[1]) for r in e["D per height"] if r[1] is not None}
                for e in post["per line"]}
    w180_lnD = {(tuple(r["line"]), r["x"]): r["ln (r2, r1, D) at Im tau 64 per Y"] for r in w180["per pair"]}

    def six(k, x, y, Yn):
        r = res.get((k, x, y))
        return None if r is None or "six" not in r else r["six"][Yn]

    per, k0_bad, k1_rows, k2_rows, k3_bad, k4_bad, k6_bad, k7_hits, k8_rows, crossings = ([] for _ in range(10))
    agreeing, accepted, k0_n = set(), [], 0
    for k in ks:
        line = lines[k]
        key = (str(line[0]), str(line[1]))
        e178 = w178["per line"][k]
        assert e178["line"] == list(key)
        for xi, x in enumerate(XS):
            p178 = e178["per Re tau"][xi]
            assert p178["x"] == x
            q = (key, x)
            row = {"line": list(key), "x": x,
                   "W179 subset": ("unsettled" if q in g0 else "settled" if q in settled else
                                   "finite" if q in finite else "running")}
            row["points"] = {str(y): {"digits": res[(k, x, y)].get("digits"), "seconds": res[(k, x, y)].get("seconds"),
                                      "two-precision spread": res[(k, x, y)].get("two-precision spread"),
                                      "status per Y": {str(Yn): compact_status(res[(k, x, y)]["status"][Yn])
                                                       for Yn in YS} if "status" in res[(k, x, y)] else None,
                                      "six per Y": {str(Yn): six(k, x, y, Yn) for Yn in YS}}
                             for y in HEIGHTS}
            # K0: the tie at Im tau 48
            mine, stored = six(k, x, 48.0, 48.0), p178["six per height"]["48.0"]
            if mine is not None:
                d = [abs(u - v) for u, v in zip(mine, stored) if u is not None and v is not None]
                k0_n += len(d)
                row["K0 worst"] = max(d) if d else None
                if d and max(d) > TOL:
                    k0_bad.append([list(key), x, max(d)])
            else:
                k0_bad.append([list(key), x, "no six"])
            # ln (r2, r1, D) at every height and Y
            lnD = {y: {Yn: doubles(six(k, x, y, Yn)) for Yn in YS} for y in HEIGHTS}
            row["ln (r2, r1, D) per height and Y"] = {str(y): {str(Yn): lnD[y][Yn] for Yn in YS} for y in HEIGHTS}
            # exponents and agreement
            ex = {Yn: expo(six(k, x, LO_H, Yn), six(k, x, HI_H, Yn)) for Yn in YS}
            row["exponents per Y (Im tau 96 to 128)"] = {str(Yn): ex[Yn] for Yn in YS}
            e = ex[AGREE_Y]
            ok = all(e[i] is not None for i in (DOWN2, DOWN1, LEP2, LEP1))
            agree = ok and abs(e[DOWN2] - e[LEP2]) <= TOL and abs(e[DOWN1] - e[LEP1]) <= TOL
            row["exponents agree"] = bool(agree) if ok else None
            # the y-limit at every Y
            ydiff = {}
            for Yn in YS:
                a_, b_ = lnD[LO_H][Yn], lnD[HI_H][Yn]
                ydiff[Yn] = None if (a_ is None or b_ is None) else abs(b_[2] - a_[2])
            row["|ln D(128, Y) - ln D(96, Y)|"] = {str(Yn): ydiff[Yn] for Yn in YS}
            ypass = {Yn: ydiff[Yn] is not None and ydiff[Yn] <= YTOL for Yn in YS}
            # K1 and K2 on the G2 lines
            if key in G2_LINES and x == XS[0]:
                for y in (64.0, 96.0, 128.0):
                    got = lnD[y][y][2] if lnD[y][y] is not None else None
                    truth = post_lnD[key].get(y)
                    k1_rows.append([list(key), x, y, got, truth,
                                    None if (got is None or truth is None) else abs(got - truth)])
            if key in G2_LINES:
                ref = w180_lnD[q]
                for Yn in K2_YS:
                    got = lnD[64.0][Yn][2] if lnD[64.0][Yn] is not None else None
                    want = ref[str(Yn)][2] if ref.get(str(Yn)) is not None else None
                    k2_rows.append([list(key), x, Yn, got, want,
                                    None if (got is None or want is None) else abs(got - want)])
            # K6 on the settled ties
            if q in settled:
                vals = [lnD[y][Yn] for y in HEIGHTS for Yn in YS]
                worst = None if any(v is None for v in vals) else max(abs(v[2]) for v in vals)
                row["K6 max |ln D|"] = worst
                if worst is None or worst > TIE:
                    k6_bad.append([list(key), x, worst])
            # the diagonal (the true frame)
            st48 = doubles(stored)
            diag = [[48.0, None if st48 is None else math.exp(st48[2]), "stored (W178)"]]
            diag += [[y, None if lnD[y][y] is None else math.exp(lnD[y][y][2]), "computed"] for y in HEIGHTS[1:]]
            row["true D on the diagonal"] = diag
            # the Y-limit on agreeing pairs
            value = None
            if agree:
                agreeing.add(q)
                bad_y = [Yn for Yn in YS if not ypass[Yn]]
                if bad_y:
                    k3_bad.append([list(key), x, bad_y])
                us = [Yn ** -0.5 for Yn in EXT]
                top = [lnD[HI_H][Yn] for Yn in EXT]
                if all(v is not None for v in top):
                    n6 = [neville(us, [v[j] for v in top]) for j in range(3)]
                    n5 = [neville(us[1:], [v[j] for v in top[1:]]) for j in range(3)]
                    row["N6 (ln r2, ln r1, ln D)"], row["N5 (ln r2, ln r1, ln D)"] = n6, n5
                    row["|N6 - N5| (ln r2, ln r1, ln D)"] = [abs(a_ - b_) for a_, b_ in zip(n6, n5)]
                    row["q, D's power of Y (65536 to 262144)"] = (top[-1][2] - top[-2][2]) / math.log(4)
                    k4_ok = abs(n6[2] - n5[2]) <= TOL
                    if not k4_ok:
                        k4_bad.append([list(key), x, abs(n6[2] - n5[2])])
                    why = [] if k4_ok else ["N6 and N5 differ"]
                    if any(not ypass[Yn] for Yn in EXT):
                        why.append("y-limit not reached at an extrapolation Y")
                else:
                    k4_bad.append([list(key), x, "a feature unresolved at Im tau 128"])
                    why = ["a feature unresolved at Im tau 128"]
                if not why:
                    value = math.exp(row["N6 (ln r2, ln r1, ln D)"][2])
                    row["D_inf"] = value
                    row["r2_inf, r1_inf (read-out)"] = [math.exp(v) for v in row["N6 (ln r2, ln r1, ln D)"][:2]]
                    accepted.append((list(key), x, value))
                    if lo <= value <= hi:
                        k7_hits.append([list(key), x, value])
                else:
                    row["D_inf withheld"] = why
                if key in G2_LINES:
                    k8_rows.append([list(key), x, value])
            seq = [v for _y, v, _s in diag if v is not None] + ([value] if value is not None else [])
            if any(lo <= v <= hi for v in seq) or any(min(u, v) < lo and max(u, v) > hi for u, v in zip(seq, seq[1:])):
                crossings.append([list(key), x, row["W179 subset"], seq])
            per.append(row)
    out["per pair"] = per
    out["K0"] = {"features compared": k0_n, "misses": k0_bad, "holds": bool(k0_n and not k0_bad)}
    out["K1"] = {"rows (line, x, Im tau, ln D here, ln D post hoc 1, |difference|)": k1_rows,
                 "holds": bool(len(k1_rows) == 6 and all(r[5] is not None and r[5] <= TOL for r in k1_rows))}
    out["K2"] = {"rows (line, x, Y, ln D here at Im tau 64, ln D W180 frozen, |difference|)": k2_rows,
                 "holds": bool(len(k2_rows) == 4 * len(K2_YS)
                               and all(r[5] is not None and r[5] <= TOL for r in k2_rows))}
    out["K3"] = {"agreeing pairs": len(agreeing), "misses (line, x, Y failing)": k3_bad,
                 "holds": bool(agreeing and not k3_bad)}
    out["K4"] = {"agreeing pairs": len(agreeing), "misses": k4_bad, "holds": bool(agreeing and not k4_bad)}
    out["K5"] = {"agreeing pairs": len(agreeing), "W179 finite pairs on integer-lambda lines": len(w179_int),
                 "agreeing, not finite in W179": sorted([list(q[0]), q[1]] for q in agreeing - w179_int),
                 "finite in W179, not agreeing": sorted([list(q[0]), q[1]] for q in w179_int - agreeing),
                 "holds": bool(agreeing == w179_int)}
    out["K6"] = {"settled pairs": len(settled), "misses": k6_bad, "holds": bool(settled and not k6_bad)}
    out["K7"] = {"window": [lo, hi], "accepted D_inf": len(accepted), "hits": k7_hits, "holds": bool(not k7_hits)}
    out["K8"] = {"box": list(BOX), "rows (line, x, D_inf or None)": k8_rows,
                 "holds": bool(len(k8_rows) == 4 and all(r[2] is not None and BOX[0] <= r[2] <= BOX[1]
                                                         for r in k8_rows))}
    out["R: distinct accepted D_inf (to 1e-6)"] = sorted({round(v, 6) for _l, _x, v in accepted})
    out["R: ten nearest to the data's D"] = sorted(accepted, key=lambda r: abs(math.log(r[2]) - data["ln D"]))[:10]
    out["R: accepted D_inf = 1 (|ln D_inf| <= 1e-12)"] = sum(1 for _l, _x, v in accepted if abs(math.log(v)) <= TIE)
    out["R: pairs whose diagonal (or its limit) crosses the window"] = crossings
    out["cells"] = {c: out[c]["holds"] for c in ("K0", "K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8")}


def main():
    t0 = time.time()
    out = {"arc": "W181", "rule": "W181_RULE.md", "python": platform.python_version(), "workers": WORKERS,
           "frame": "W178's (the_six_at_the_cusp.py), each norm c_s(Im tau) + B_s (Y - Im tau)"}
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
