#!/usr/bin/env python3
"""W183 — the kernel's Laurent constant as the Higgs's singlet, RI-1 and main's P-566 Q1 (the rule: W183_RULE.md,
committed and pushed before this script).  It runs once, from the repository root, on four worker processes.

B1656's frame as W178 computes it (W162's point: the Higgs direction DR, L_max, W177's norms in working precision, no
residue cut, the theta-zero rule, the weighted M, W93's coupling; W178's two precisions and status rule), with one
change, the Higgs: in sector X it is S_X = sigma_X 1 + DR.(i, j, k), read alike by every sector.  a0(X) is the Laurent
constant of the identity-channel kernel K_1(z) = e^{2 pi i A z} theta_1(z + ub) theta_1'(0) / (theta_1(ub) theta_1(z))
at ub = (q_L + q_R) w, so a0(X) = 2 pi i A + d/dz log theta_1(z + ub) at z = 0.  The variants:

  tie    sigma = 0 with W178's readings (S~, S, S)                       (O0 only)
  none   sigma = 0
  B      sigma_X = a0(X)                                                 (bare: no free number)
  N      sigma_X = |DR.DR|^(1/2) a0(X)/|a0(X)|                           (natural: P-566's size)
  even   sigma_X = |DR.DR|^(1/2) a0(down)/|a0(down)| in all three sectors
  ph k   sigma_up = e^(2 pi i k/12) |DR.DR|^(1/2), sigma_down = sigma_lepton = -sigma_up, k = 0..11

on the 261 census lines with an identity kernel (theta_1(3w) != 0), at tau = i, and towards the cusp at Re tau 1/8
and 3/8, Im tau 6 and 12 (read-outs).  On the 15 lines where 3w is a half-period (6w in the lattice, 3w not) a0 = 0 by
its oddness; there sigma = 0 under B, N and even (decided from the fractions), and O3-O8 leave those lines out.
The CKM is V = U_up^dagger U_down with U the left singular vectors, lightest first; the corner order is
|V_ub| < |V_td|.

  O0  the tie: with sigma = 0 and W178's readings, the six at tau = i equal W179's stored six within 1e-6
  O1  the parity a0(up) = -a0(down) = -a0(lepton), four channels, and route 2 ((K(h) + K(-h))/2, h = 1e-20)
  O2  none: the joint coarse fact (nature's corner order and |V_ud| > 0.9) at no more than 15% of the decided lines
  O3  even: within 10 points of none (on the lines decided under both)
  O4  N: at least 10 points above none
  O5  N: within the range of the twelve phases' rates (on the lines decided under N and all twelve)
  O6  B: at least 10 points above none
  O7  no line under B or N at tau = i with (r2, r1) within a factor 1.25 of (1/3, 3)
  O8  no line under B or N at tau = i with D in [10.25, 10.91]
  R   read-outs

    python3 -B docs/dossiers/the_weave_2026-10-07/the_laurent_singlet.py

Disclosed: a timing call on this script, after the rule was pushed and before this commit, ran the point function on
line 40 of the 261 ((1/7, 4/7)) at tau = i and at Re tau 3/8, Im tau 12, and printed only the statuses, digits and
seconds (no failure; 145 resolved and 8 zero at working precision, then 153 resolved; 1.0 s and 1.8 s).  No value was
printed or read.
"""
import contextlib
import io
import json
import math
import multiprocessing as mpc
import platform
import statistics
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
    import the_six_at_the_cusp as W178          # noqa: E402  (W178: the frame, its precisions and zero rule)
T8, W93, W162, W177, W58 = W178.T8, W178.W93, W178.W162, W178.W177, W178.W58
mp = W177.mp
OUT = HERE / "the_laurent_singlet.json"
POINTS = ((0.0, 1.0), (0.125, 6.0), (0.125, 12.0), (0.375, 6.0), (0.375, 12.0))
SECS = ("up", "down", "lep")
W178READ = dict(W178.READ)
PHASES = 12
AGREE = 1e-6
DEGEN = 1e-10
NULL = 1e-8
H = mp.mpf("1e-20")
EXTRA = 60
PAR_TOL = mp.mpf("1e-30")
R2_TOL = mp.mpf("1e-20")
JOINT_VUD = 0.9
O2_MAX, O3_BAND, O46_LIFT = 0.15, 0.10, 0.10
FACTOR = 1.25
GJ = (1 / 3, 3.0)
SIGMAS = 3
WORKERS = 4
DOWN2, DOWN1, LEP2, LEP1 = 2, 3, 4, 5
VARIANTS = ["tie", "none", "B", "N", "even"] + [f"ph{k}" for k in range(PHASES)]
FULL = ("tie", "none", "B", "N", "even")
_G = {}


def _init(root_str):
    W178._init(root_str)
    _G["lines"] = [l for l in W178._G["lines"] if not W178.theta_zero(1, l, 3)]


def order(line):
    return math.lcm(line[0].denominator, line[1].denominator)


def half_period(line):
    """3w is a half-period: 6w in the lattice and 3w not (exact), where a0 = 0 by its oddness"""
    inl = lambda n: (n * line[0]) % 1 == 0 and (n * line[1]) % 1 == 0
    return inl(6) and not inl(3)


# ============================================================================================ the kernel's constant
def a0_closed(s, ub, t):
    """route 1: a0 = 2 pi i A + pi theta_s'(pi ub) / theta_s(pi ub), ub reduced to the centred cell (W177's kernels)"""
    ubr = W177.reduce(ub, t)
    A = mp.im(ubr) / mp.im(t)
    q = W177.q_of(t)
    return 2j * mp.pi * A + mp.pi * mp.jtheta(s, mp.pi * ubr, q, 1) / mp.jtheta(s, mp.pi * ubr, q)


def a0_numeric(s, ub, t, p):
    """route 2: (K(h) + K(-h)) / 2 with W177's K_direct, h = 1e-20, at p + 60 digits"""
    with mp.workdps(p + EXTRA):
        return (W177.K_direct(s, H, ub, t) + W177.K_direct(s, -H, ub, t)) / 2


# ============================================================================================ one point, one precision
def svd_sorted(Y):
    """left singular vectors and singular values, lightest first"""
    U, S, _V = mp.svd_c(Y, compute_uv=True)
    sv = [abs(S[i]) for i in range(3)]
    idx = sorted(range(3), key=lambda i: sv[i])
    Us = mp.matrix(3, 3)
    for c, i in enumerate(idx):
        for r in range(3):
            Us[r, c] = U[r, i]
    return Us, [sv[i] for i in idx]


def lnv(v):
    return float(mp.log(v)) if v > 0 else -math.inf


def l10(v):
    return float(mp.log10(v)) if v > 0 else -math.inf


def degenerate(sv):
    return any(abs(sv[i + 1] - sv[i]) <= DEGEN * max(sv[i + 1], sv[i]) for i in range(2))


def at(line, x, y, p):
    a, b = line
    with mp.workdps(p):
        CM, EPSM, _BLK, EM = W93.units("mp")
        t = mp.mpc(mp.mpf(x), mp.mpf(y))
        dr = W178.DR_mp(t, p)
        S0 = dr[0] * CM["i"] + dr[1] * CM["j"] + dr[2] * CM["k"]
        St = EPSM * W178.mat_conj(S0) * EPSM.T
        I2 = mp.eye(2)
        hh = dr[0] ** 2 + dr[1] ** 2 + dr[2] ** 2
        nat = mp.sqrt(abs(hh))
        drn = mp.sqrt(sum(abs(v) ** 2 for v in dr))
        Lv = mp.mpf(W162.L_of(W178._G["col"], y, "L_max"))
        M, a0, a0n = {}, {}, {}
        for sec in SECS:
            qL, qR = T8.charges(W93, sec)
            R = W93.residues((a, -b), sec, t)
            k = T8.kappa(qL, qR, a, b, t)
            ub = (qL + qR) * (mp.mpf(a.numerator) / a.denominator * t + mp.mpf(b.numerator) / b.denominator)
            Mx = mp.zeros(2, 2)
            for s in T8.UNITS:
                if W178.theta_zero(W178.W89TH[s], line, qL + qR):
                    continue
                w = 2 * mp.pi * Lv + W177.c_series(W178.W89TH[s], ub, t)
                if w > 0:
                    Mx += mp.sqrt(w) * k * R[s] * EM[s]
            M[sec] = Mx
            a0[sec], a0n[sec] = {}, {}
            for s in (1, 2, 3, 4):
                if W178.theta_zero(s, line, qL + qR):
                    continue
                a0[sec][s] = a0_closed(s, ub, t)
                a0n[sec][s] = a0_numeric(s, ub, t, p)
        sig = {}
        sig["tie"] = None
        sig["none"] = {X: mp.mpf(0) for X in SECS}
        if half_period(line):
            for v in ("B", "N", "even"):
                sig[v] = {X: mp.mpf(0) for X in SECS}
        else:
            sig["B"] = {X: a0[X][1] for X in SECS}
            sig["N"] = {X: nat * a0[X][1] / abs(a0[X][1]) for X in SECS}
            ev = nat * a0["down"][1] / abs(a0["down"][1])
            sig["even"] = {X: ev for X in SECS}
        for kk in range(PHASES):
            c = mp.expjpi(mp.mpf(2 * kk) / PHASES) * nat
            sig[f"ph{kk}"] = {"up": c, "down": -c, "lep": -c}
        res = {}
        for v in VARIANTS:
            Sx = ({X: (St if W178READ[X] == "St" else S0) for X in SECS} if v == "tie"
                  else {X: S0 + sig[v][X] * I2 for X in SECS})
            Us, svs, nullx = {}, {}, {}
            for X in SECS:
                Y = W93.coupling_mp(Sx[X], M[X])
                if X == "lep":
                    svs[X] = sorted(abs(u) for u in mp.svd_c(Y, compute_uv=False))
                else:
                    Us[X], svs[X] = svd_sorted(Y)
                detS = Sx[X][0, 0] * Sx[X][1, 1] - Sx[X][0, 1] * Sx[X][1, 0]
                nullx[X] = bool(abs(detS) <= NULL * abs(hh))
            six, six10 = [], []
            for X in SECS:
                s = svs[X]
                for j in (1, 0):            # W178's order: sigma_2nd / sigma_max, then sigma_min / sigma_max
                    r = s[j] / s[2] if s[2] > 0 else mp.mpf(0)
                    six.append(lnv(r))
                    six10.append(l10(r))
            V = Us["up"].H * Us["down"]
            el = {"ud": abs(V[0, 0]), "ub": abs(V[0, 2]), "td": abs(V[2, 0])}
            res[v] = {"six": six, "six10": six10, "ln": {e: lnv(z) for e, z in el.items()},
                      "l10": {e: l10(z) for e, z in el.items()}, "vud": float(el["ud"]),
                      "degenerate": bool(degenerate(svs["up"]) or degenerate(svs["down"])), "null": nullx,
                      "hier": [[float(s[1] / s[2]) if s[2] > 0 else 0.0, float(s[0] / s[2]) if s[2] > 0 else 0.0]
                               for s in (svs["up"], svs["down"])]}
        par = {"max |a0(up) + a0(down)| / (1 + |a0(down)|)": 0.0, "max |a0(lep) - a0(down)| / (1 + |a0(down)|)": 0.0,
               "max route 2 / (1 + |a0|)": 0.0, "channels compared": 0}
        for s in (1, 2, 3, 4):
            if s in a0["down"] and s in a0["up"]:
                d = 1 + abs(a0["down"][s])
                par["max |a0(up) + a0(down)| / (1 + |a0(down)|)"] = max(
                    par["max |a0(up) + a0(down)| / (1 + |a0(down)|)"], abs(a0["up"][s] + a0["down"][s]) / d)
                par["max |a0(lep) - a0(down)| / (1 + |a0(down)|)"] = max(
                    par["max |a0(lep) - a0(down)| / (1 + |a0(down)|)"], abs(a0["lep"][s] - a0["down"][s]) / d)
                par["channels compared"] += 1
            for X in SECS:
                if s in a0[X]:
                    par["max route 2 / (1 + |a0|)"] = max(par["max route 2 / (1 + |a0|)"],
                                                          abs(a0n[X][s] - a0[X][s]) / (1 + abs(a0[X][s])))
        par = {k_: (float(v_) if k_ != "channels compared" else v_) for k_, v_ in par.items()}
        par["log10 of the maxima"] = {k_: (float(mp.log10(v_)) if v_ > 0 else None)
                                      for k_, v_ in par.items() if k_ != "channels compared"}
        extra = {"a0(down), identity channel": [float(mp.re(a0["down"][1])), float(mp.im(a0["down"][1]))],
                 "|a0|/|DR|": float(abs(a0["down"][1]) / drn), "|DR.DR|^(1/2)/|DR|": float(nat / drn)}
        return res, par, extra


# ============================================================================================ two precisions
def status_of(v1, v2, l1, l2, p1, p2):
    if math.isfinite(v1) and math.isfinite(v2) and abs(v1 - v2) <= AGREE:
        return "resolved"
    if l1 <= -(p1 - 30) and l2 <= -(p2 - 30):
        return "zero at working precision"
    return "unresolved"


def point(task):
    k, x, y = task
    line = _G["lines"][k]
    t0 = time.time()
    try:
        p1, p2 = W178.precisions(y)
        for attempt in (1, 2):
            r1, par1, ex1 = at(line, x, y, p1)
            r2, par2, ex2 = at(line, x, y, p2)
            out, unresolved = {}, 0
            for v in VARIANTS:
                a, b = r1[v], r2[v]
                st6 = [status_of(a["six"][i], b["six"][i], a["six10"][i], b["six10"][i], p1, p2) for i in range(6)]
                stv = {e: status_of(a["ln"][e], b["ln"][e], a["l10"][e], b["l10"][e], p1, p2) for e in a["ln"]}
                unresolved += st6.count("unresolved") + list(stv.values()).count("unresolved")
                out[v] = {"six": [b["six"][i] if st6[i] == "resolved" else None for i in range(6)], "six status": st6,
                          "ln V": {e: (b["ln"][e] if stv[e] == "resolved" else None) for e in stv},
                          "V status": stv, "vud": b["vud"], "vud agree": abs(a["vud"] - b["vud"]) <= AGREE,
                          "sep": [(c["ln"]["ub"] - c["ln"]["td"]) if math.isfinite(c["ln"]["ub"])
                                  and math.isfinite(c["ln"]["td"]) else None for c in (a, b)],
                          "degenerate": a["degenerate"] or b["degenerate"], "null": b["null"], "hier": b["hier"]}
            if unresolved == 0 or attempt == 2:
                break
            p1, p2 = 2 * p1, 2 * p2
        return {"k": k, "x": x, "y": y, "digits": [p1, p2], "variants": out, "parity": [par1, par2],
                "extra": ex2, "seconds": round(time.time() - t0, 2)}
    except Exception:  # noqa: BLE001  (a failed task is kept and disclosed)
        return {"k": k, "x": x, "y": y, "failed": W178.sanitize(traceback.format_exc()[-1500:])}


# ============================================================================================ the verdicts per point
def verdict(r):
    """(decided, nature's corner order, joint) for one variant's record"""
    if r["degenerate"] or not r["vud agree"]:
        return False, None, None
    su, st = r["V status"]["ub"], r["V status"]["td"]
    zu, zt = su == "zero at working precision", st == "zero at working precision"
    if su == "resolved" and st == "resolved":
        if None in r["sep"] or min(abs(r["sep"][0]), abs(r["sep"][1])) <= AGREE or \
                (r["sep"][0] < 0) != (r["sep"][1] < 0):
            return False, None, None
        nat = r["sep"][1] < 0
    elif zu and st == "resolved":
        nat = True
    elif zt and su == "resolved":
        nat = False
    elif zu and zt:
        nat = False
    else:
        return False, None, None
    return True, nat, bool(nat and r["vud"] > JOINT_VUD)


def hier_ok(r):
    """main's scan's filter: both sectors 1e-12 < m1/m3 < 0.01 and m2/m3 < 0.1, and up steeper than down"""
    (u2, u1), (d2, d1) = r["hier"]
    return (1e-12 < u1 < 0.01 and u2 < 0.1 and 1e-12 < d1 < 0.01 and d2 < 0.1 and u2 < d2 / 2 and u1 < d1)


def rate(vals):
    return (sum(vals) / len(vals)) if vals else None


def doubles(six):
    if six is None or any(six[i] is None for i in (DOWN2, DOWN1, LEP2, LEP1)):
        return None
    l2, l1 = six[DOWN2] - six[LEP2], six[DOWN1] - six[LEP1]
    return [l2, l1, l1 - l2]


def run(out, pool):
    lines = _G["lines"]
    keep = {k for k, l in enumerate(lines) if not half_period(l)}
    out["lines"] = {"census": len(W178._G["lines"]), "with an identity kernel": len(lines),
                    "a0 = 0 (3w a half-period), left out of O3-O8": [[str(l[0]), str(l[1])] for l in lines
                                                                       if half_period(l)],
                    "lines in O3-O8": len(keep),
                    "excluded (3w in the lattice)": [[str(l[0]), str(l[1])] for l in W178._G["lines"]
                                                     if W178.theta_zero(1, l, 3)]}
    tasks = [(k, x, y) for k in range(len(lines)) for x, y in POINTS]
    tasks.sort(key=lambda q: -q[2])
    out["tasks"] = len(tasks)
    t0 = time.time()
    pts, n = {}, 0
    for r in pool.imap_unordered(point, tasks, chunksize=1):
        pts[(r["k"], r["x"], r["y"])] = r
        n += 1
        if n % 100 == 1:
            print(f"task {n}/{len(tasks)} at {round(time.time() - t0)} s", flush=True)
    out["compute seconds"] = round(time.time() - t0, 1)
    out["failed tasks"] = [[str(k), r["failed"]] for k, r in pts.items() if "failed" in r]
    out["doubled-precision tasks"] = sum(1 for r in pts.values() if "digits" in r
                                         and r["digits"][0] > W178.precisions(r["y"])[0])
    ok = {key: r for key, r in pts.items() if "failed" not in r}
    # ---- O1, the parity
    worst = {}
    for r in ok.values():
        for par in r["parity"]:
            for k_, v_ in par["log10 of the maxima"].items():
                worst[k_] = max(worst.get(k_, -1000.0), v_ if v_ is not None else -1000.0)
    lim = float(mp.log10(PAR_TOL))
    out["O1"] = {"log10 of the worst relative residuals": worst, "parity limit (log10)": lim,
                 "route 2 limit (log10)": float(mp.log10(R2_TOL)),
                 "holds": bool(worst and worst["max |a0(up) + a0(down)| / (1 + |a0(down)|)"] <= lim
                               and worst["max |a0(lep) - a0(down)| / (1 + |a0(down)|)"] <= lim
                               and worst["max route 2 / (1 + |a0|)"] <= float(mp.log10(R2_TOL))
                               and len(ok) == len(pts))}
    # ---- O0, the tie at i
    w179 = json.loads((HERE / "the_down_lepton_factor.json").read_text(encoding="utf-8"))
    s179 = {tuple(e["line"]): e for e in w179["per line"]}
    o0_n, o0_bad, o0_missing = 0, [], 0
    for k, line in enumerate(lines):
        key = (str(line[0]), str(line[1]))
        r = ok.get((k, 0.0, 1.0))
        stored = s179[key]["at i"].get("six")
        if r is None:
            o0_missing += 1
            continue
        if stored is None:
            continue
        mine = r["variants"]["tie"]["six"]
        for i in range(6):
            if mine[i] is not None and stored[i] is not None:
                o0_n += 1
                if abs(mine[i] - stored[i]) > AGREE:
                    o0_bad.append([list(key), i, mine[i], stored[i]])
    out["O0"] = {"features compared": o0_n, "disagreements": o0_bad, "lines without a point": o0_missing,
                 "holds": bool(o0_n > 0 and not o0_bad and o0_missing == 0)}
    # ---- the verdicts at tau = i
    V = {v: {} for v in VARIANTS}
    for k in range(len(lines)):
        r = ok.get((k, 0.0, 1.0))
        if r is None:
            continue
        for v in VARIANTS:
            V[v][k] = verdict(r["variants"][v]) + (hier_ok(r["variants"][v]),)
    counts = {}
    for v in VARIANTS:
        rs = [ok[(k, 0.0, 1.0)]["variants"][v] for k in V[v]]
        dec = [k for k, q in V[v].items() if q[0]]
        joint = [V[v][k][2] for k in dec]
        ratios = sorted(ok[(k, 0.0, 1.0)]["variants"][v]["sep"][1] for k in dec
                        if ok[(k, 0.0, 1.0)]["variants"][v]["V status"]["ub"] == "resolved"
                        and ok[(k, 0.0, 1.0)]["variants"][v]["V status"]["td"] == "resolved")
        hdec = [k for k in dec if V[v][k][3]]
        counts[v] = {"points": len(rs), "decided": len(dec), "degenerate": sum(1 for q in rs if q["degenerate"]),
                     "nature's corner order": sum(1 for k in dec if V[v][k][1]), "joint": sum(joint),
                     "rate": rate(joint),
                     "corner ratio |V_ub|/|V_td| quartiles": ([math.exp(q) for q in statistics.quantiles(ratios, n=4)]
                                                             if len(ratios) >= 4 else None),
                     "|V_ud| median": (statistics.median([ok[(k, 0.0, 1.0)]["variants"][v]["vud"] for k in dec])
                                       if dec else None),
                     "hierarchical subset": {"decided": len(hdec), "joint": sum(V[v][k][2] for k in hdec),
                                             "rate": rate([V[v][k][2] for k in hdec])},
                     "null points (any sector)": sum(1 for q in rs if any(q["null"].values()))}
    out["R: per variant at tau = i"] = counts

    def common_rate(v, w):
        both = [k for k in V[v] if k in keep and V[v][k][0] and V[w].get(k, (False,))[0]]
        return len(both), rate([V[v][k][2] for k in both]), rate([V[w][k][2] for k in both])

    n0 = counts["none"]
    out["O2"] = {"rate none": n0["rate"], "decided": n0["decided"], "max": O2_MAX,
                 "holds": bool(n0["rate"] is not None and n0["rate"] <= O2_MAX)}
    nb, re_, rn = common_rate("even", "none")
    out["O3"] = {"common lines": nb, "rate even": re_, "rate none": rn,
                 "holds": bool(re_ is not None and abs(re_ - rn) <= O3_BAND)}
    nb, rN, rn = common_rate("N", "none")
    out["O4"] = {"common lines": nb, "rate N": rN, "rate none": rn,
                 "holds": bool(rN is not None and rN - rn >= O46_LIFT)}
    phs = [f"ph{k}" for k in range(PHASES)]
    allk = [k for k in V["N"] if k in keep and V["N"][k][0] and all(V[p].get(k, (False,))[0] for p in phs)]
    rN5 = rate([V["N"][k][2] for k in allk])
    rph = [rate([V[p][k][2] for k in allk]) for p in phs]
    out["O5"] = {"common lines": len(allk), "rate N": rN5, "twelve-phase rates": rph,
                 "holds": bool(rN5 is not None and None not in rph and min(rph) <= rN5 <= max(rph))}
    nb, rB, rn = common_rate("B", "none")
    out["O6"] = {"common lines": nb, "rate B": rB, "rate none": rn,
                 "holds": bool(rB is not None and rB - rn >= O46_LIFT)}
    # ---- O7, O8: the six under B and N at tau = i (the look)
    files = {p: T8.git_bytes(ROOT, W58.REV, p) for p in W58.FILES}
    t6 = T8.targets(files)[0]
    ahs = json.loads((HERE / "received" / "AHS2026_double_ratio.json").read_text(encoding="utf-8"))["the double ratio"]
    data = {"ln r2": float(t6[DOWN2] - t6[LEP2]), "ln r1": float(t6[DOWN1] - t6[LEP1]),
            "D": float(ahs["value"]), "sigma D": float(ahs["sigma"])}
    out["the data (read once)"] = data
    lo, hi = data["D"] - SIGMAS * data["sigma D"], data["D"] + SIGMAS * data["sigma D"]
    o7, o8, dvals, order5 = [], [], {"B": [], "N": []}, []
    for k, line in enumerate(lines):
        r = ok.get((k, 0.0, 1.0))
        if r is None or k not in keep:
            continue
        key = [str(line[0]), str(line[1])]
        for v in ("B", "N"):
            d = doubles(r["variants"][v]["six"])
            if d is None:
                continue
            dvals[v].append(math.exp(d[2]))
            if abs(d[0] - math.log(GJ[0])) <= math.log(FACTOR) and abs(d[1] - math.log(GJ[1])) <= math.log(FACTOR):
                o7.append([key, v, math.exp(d[0]), math.exp(d[1])])
            if lo <= math.exp(d[2]) <= hi:
                o8.append([key, v, math.exp(d[2])])
            if order(line) == 5:
                order5.append([key, v, math.exp(d[2])])
    out["O7"] = {"factor": FACTOR, "hits": o7, "holds": bool(not o7)}
    out["O8"] = {"window": [lo, hi], "hits": o8, "holds": bool(not o8)}
    out["R: D at tau = i under B and N (range, count)"] = {
        v: ([min(x), max(x), len(x)] if x else None) for v, x in dvals.items()}
    out["R: D on the order-5 lines under B and N"] = order5
    # ---- read-outs per line at i, and towards the cusp
    per = []
    for k, line in enumerate(lines):
        r = ok.get((k, 0.0, 1.0))
        e = {"line": [str(line[0]), str(line[1])], "order": order(line), "a0 = 0": half_period(line)}
        if r is not None:
            e.update(r["extra"])
            e["at i"] = {v: {"decided, nature, joint": list(V[v][k][:3]),
                             "ln |V_ud|, |V_ub|, |V_td|": [r["variants"][v]["ln V"][z] for z in ("ud", "ub", "td")],
                             **({"six": r["variants"][v]["six"]} if v in FULL else {})} for v in VARIANTS}
        cusp = {}
        for x in (0.125, 0.375):
            for y in (6.0, 12.0):
                rc = ok.get((k, x, y))
                if rc is not None:
                    cusp[f"{x},{y}"] = {v: list(verdict(rc["variants"][v])) for v in FULL[1:]}
        e["towards the cusp"] = cusp
        per.append(e)
    out["per line"] = per
    stab = {}
    for v in FULL[1:]:
        same, tot = 0, 0
        for k in range(len(lines)):
            for x in (0.125, 0.375):
                a, b = ok.get((k, x, 6.0)), ok.get((k, x, 12.0))
                if a is None or b is None:
                    continue
                va, vb = verdict(a["variants"][v]), verdict(b["variants"][v])
                if va[0] and vb[0]:
                    tot += 1
                    same += va[2] == vb[2]
        rates12 = [verdict(ok[(k, x, 12.0)]["variants"][v])[2] for k in range(len(lines)) for x in (0.125, 0.375)
                   if (k, x, 12.0) in ok and verdict(ok[(k, x, 12.0)]["variants"][v])[0]]
        stab[v] = {"pairs decided at 6 and 12": tot, "same joint verdict": same, "rate at Im tau 12": rate(rates12)}
    out["R: towards the cusp"] = stab
    out["cells"] = {c: out[c]["holds"] for c in ("O0", "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8")}


def main():
    t0 = time.time()
    out = {"arc": "W183", "rule": "W183_RULE.md", "python": platform.python_version(), "workers": WORKERS,
           "frame": "W178's (the_six_at_the_cusp.py) with the Higgs S_X = sigma_X 1 + DR.(i, j, k), read alike"}
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            with mpc.get_context("fork").Pool(WORKERS, initializer=_init, initargs=(str(ROOT),)) as pool:
                _init(str(ROOT))
                run(out, pool)
        except Exception:  # noqa: BLE001  (a failed run still writes what it has)
            out["run_failed"] = W178.sanitize(traceback.format_exc()[-3000:])
    out["warnings"] = sorted({f"{w.category.__name__}: {w.message}" for w in caught})
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name, "in", out["seconds"], "s;", len(out["warnings"]), "distinct warnings")


if __name__ == "__main__":
    main()
