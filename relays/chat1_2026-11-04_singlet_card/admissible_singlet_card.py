"""THE ADMISSIBLE SINGLET OF SIZE |a0|, SCREENED -- the script.  The rule, THE_ADMISSIBLE_SINGLET_RULE.md, was committed
and pushed (3e2d8128e) before this script existed in the tree.  It runs once, on four worker processes:

    python3 admissible_singlet_card.py <main checkout>      (main at eb130f01f)

The frame is B1656's as B1821's module builds it: residues, the channel norms cA, the weighted M, L_max, the coupling;
H = I; c not applied; the Higgs direction DR.  A line (a, b) is w = a tau + b = B.line_w(a, -b, tau).  a0 is
2 pi i Im(u)/Im(tau) + theta_1'(u)/theta_1(u) at u = 3w, and eta^3 comes from its product with q^(1/24) = e^(2 pi i tau/24).

Variants (S = sigma 1 + DR.(i, j, k); adj S = eps S^T eps^T = sigma - DR.(i, j, k); S~ = eps conj(S) eps^T):
  none       sigma = 0                                     up S, down adj S, leptons S
  candidate  sigma = i |a0| e^(i arg eta^3)                up S, down adj S, leptons S
  even       the candidate's sigma                         up S, down S, leptons S
  up-only    the candidate's sigma in up, 0 elsewhere      up S, down S, leptons S          (read-out)
  real       sigma = |a0| e^(i arg eta^3)                  up S, down adj S, leptons S      (read-out)
  SM         the candidate's sigma                         up S~, down S, leptons S         (read-out)
  const      sigma = i rbar (|eta^3|/2) e^(i arg eta^3)    up S, down adj S, leptons S      (read-out; rbar the median
             of 2|a0|/|eta^3| over the card's 1 380 points)

Points: W183's census (own_lines over orders 1-12, each line min((a, b), (-a, -b) mod 1)) without the slope a = 2/5,
3/5 (mod 1), the lines with 3w in the lattice, the half-period lines and the 6 order-4 lines (a read-out): 230 lines, at
Re tau in {0.11, 0.37} and Im tau in {2.2, 2.6, 3.0}, 1 380 points (and 36 order-4 points).

The test: an exact paired sign-flip test on the points filtered under both variants: per line d = J_v - J_ref on those
points, Delta_both = sum d / sum B, p = P(sum s_l d_l >= sum d_l) for independent signs, by convolution (float64).  The
price b = 11.58 bits.  Cells, power and outcomes as the rule fixes them; the script prints each cell's numbers, HOLDS or
FAILS, and the grade.

Smoke test (disclosed): before the rule's push, a draft of this script was exercised outside the tree.  The statistics
ran on synthetic blocks.  point() and k0() ran once at an off-grid point, (1/7, 2/7) at tau = 0.2 + 2.4i, which is not
one of the card's points.  The test printed only the synthetic results, whether the record fields existed, the
instrument's largest change of the six (3e-14) and seconds.  No corner order, |V_ud|, filter or spectrum was printed or
read.  No timing call was made at the card's points.  Before this script's commit, signflip_p was checked against brute
force on 300 random small sign patterns (largest difference 0), and the census counts (266, 236, 230, 6) were printed.

The price: b = 8 + log2 12 = 11.585 bits exactly (the rule's 11.58, whose bar 3.27e-6 is rounded); the script uses the exact
bar, 3.255e-6, and flags a p between the two.
"""
import contextlib
import io
import math
import os
import pathlib
import sys
from fractions import Fraction as Fr
from math import gcd
from multiprocessing import Pool

import numpy as np

sys.dont_write_bytecode = True
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
os.chdir(ROOT)
with contextlib.redirect_stdout(io.StringIO()):
    import cm_zero_line as Z
    B = Z.mods()["B"]

PI = math.pi
SECS = (("up", 1, -4), ("down", 1, 2), ("lep", -3, 6))
SN = ("up", "down", "lep")
FAMILY = (Fr(2, 5), Fr(3, 5))
TAUS = [complex(x, y) for x in (0.11, 0.37) for y in (2.2, 2.6, 3.0)]
VARIANTS = ("none", "candidate", "even", "up-only", "real", "SM", "const")
READS = {"none": ("S", "adj", "S"), "candidate": ("S", "adj", "S"), "even": ("S", "S", "S"), "up-only": ("S", "S", "S"),
         "real": ("S", "adj", "S"), "SM": ("St", "S", "S"), "const": ("S", "adj", "S")}
K0_LINES = [(Fr(1, 7), Fr(2, 7)), (Fr(3, 8), Fr(1, 8)), (Fr(4, 9), Fr(1, 3)), (Fr(1, 11), Fr(3, 11))]
DEG, ZERO, GAPV, K0TOL = 1e-10, 1e-12, 1e-6, 1e-9
BITS, BITS7, ALPHA, MARGIN, FLOOR = math.log2(12) + 8, 7, 0.01, 0.10, 30     # b = 8 + log2 12 = 11.58
NPOW, LIFT = 500, 0.25


def guard(a):
    if Fr(a) % 1 in FAMILY:
        raise SystemExit("refused: the candidate family's slope")


def eta(tau, n=80):
    q = np.exp(2j * PI * tau)
    return np.exp(2j * PI * tau / 24) * np.prod([1 - q ** k for k in range(1, n)])


def e1star(u, tau, n=40):
    k = np.arange(-n, n); h = k + 0.5
    e = (-1.0) ** k * np.exp(1j * PI * tau * h * h + 2j * PI * h * u)
    return 2j * PI * u.imag / tau.imag + np.sum(2j * PI * h * e) / np.sum(e)


def own_lines(orders):
    seen, out = set(), []
    for N in orders:
        for j in range(N):
            for k in range(N):
                if gcd(gcd(j, k), N) != 1:
                    continue
                a, b = Fr(j, N), Fr(k, N)
                kk = min((a, b), ((-a) % 1, (-b) % 1))
                if kk in seen:
                    continue
                seen.add(kk); out.append(kk)
    return out


def lattice(z):
    return (z[0] % 1, z[1] % 1) == (0, 0)


def order4(l):
    return lattice((4 * l[0], 4 * l[1])) and not lattice((2 * l[0], 2 * l[1]))


CENSUS = own_lines(range(1, 13))
BASE = [l for l in CENSUS if l[0] % 1 not in FAMILY and not lattice((3 * l[0], 3 * l[1])) and not lattice((6 * l[0], 6 * l[1]))]
KEPT = [l for l in BASE if not order4(l)]
ORD4 = [l for l in BASE if order4(l)]


def frame(a, b, tau):
    guard(a)
    L = Z.radii(tau)[0]
    M = {}
    w = B.line_w(float(a), -float(b), tau)
    for sn, ql, qr in SECS:
        x, y = B.sector_twists(w, tau, ql, qr)
        with contextlib.redirect_stdout(io.StringIO()):
            R = B.residues(x, y, tau); c = B.cA(x, y, tau, R)
        u = {k: (math.sqrt(2 * PI * L + c[k]) * R[k] if c[k] is not None and 2 * PI * L + c[k] > 0 else 0) for k in B.UNITS}
        M[sn] = B.weighted_M(u)
    with contextlib.redirect_stdout(io.StringIO()):
        DR = np.array(Z.direction("DR", tau))
    return M, DR, complex(e1star(3 * w, tau)), complex(eta(tau) ** 3)


def sigmas(v, a0, E, rbar):
    ph = E / abs(E)
    s = 1j * abs(a0) * ph
    if v == "none":
        return {"up": 0, "down": 0, "lep": 0}
    if v == "real":
        return {sn: abs(a0) * ph for sn in SN}
    if v == "up-only":
        return {"up": s, "down": 0, "lep": 0}
    if v == "const":
        return {sn: 1j * rbar * abs(E) / 2 * ph for sn in SN}
    return {sn: s for sn in SN}


def read(S, how):
    if how == "S":
        return S
    if how == "adj":
        return B.EPS @ S.T @ B.EPS.T
    return B.EPS @ S.conj() @ B.EPS.T


def yukawas(M, DR, sig, reads):
    T = DR[0] * B.QI + DR[1] * B.QJ + DR[2] * B.QK
    return {sn: B.coupling(read(sig[sn] * np.eye(2) + T, how), M[sn]) for sn, how in zip(SN, reads)}


def spectra(Y):
    out = {}
    for sn in SN:
        uu, s, _ = np.linalg.svd(Y[sn]); o = np.argsort(s)
        out[sn] = (uu[:, o], s[o])
    return out


def degenerate(s):
    return s[2] <= 0 or any((s[k + 1] - s[k]) / s[2] < DEG for k in range(2))


def hier(s):
    return s[2] > 0 and 1e-12 < s[0] / s[2] < 0.01 and s[1] / s[2] < 0.1


def facts(Y):
    sp = spectra(Y)
    (Uu, su), (Ud, sd) = sp["up"], sp["down"]
    deg = degenerate(su) or degenerate(sd)
    filt = (not deg) and hier(su) and hier(sd) and su[1] / su[2] < sd[1] / sd[2] / 2 and su[0] / su[2] < sd[0] / sd[2]
    V = Uu.conj().T @ Ud
    vub, vtd, vud = abs(V[0, 2]), abs(V[2, 0]), abs(V[0, 0])
    zub, ztd = vub < ZERO, vtd < ZERO
    if zub and ztd:
        corner = False                       # a tie, not nature's order
    elif zub or ztd:
        corner = bool(zub)                   # zero is the smaller
    else:
        corner = bool(vub < vtd)
    return {"deg": bool(deg), "filt": bool(filt), "corner": corner, "vud": bool(vud > 0.9),
            "ratio": float(vub / vtd) if vtd > 0 else float("inf"), "Vud": float(vud)}


def observables(Y):
    sp = spectra(Y)
    six = np.concatenate([sp[sn][1][:2] / sp[sn][1][2] for sn in SN])
    gaps = min(min((sp[sn][1][k + 1] - sp[sn][1][k]) / sp[sn][1][2] for k in range(2)) for sn in ("up", "down"))
    V = sp["up"][0].conj().T @ sp["down"][0]
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    return six, np.abs([V[0, 1], V[1, 2], V[0, 2], V[2, 0]]), J, gaps


def frame_task(task):
    a, b, tau = task
    return (a, b, tau), frame(a, b, tau)


def k0(task):
    a, b, tau = task
    L = {"x": (a, b, tau), "A": (a, b + 1, tau), "P": (a + 1, b, tau), "N": (-a, -b, tau), "T": (a, b - a, tau + 1),
         "M": (a, -b, complex(-tau.real, tau.imag))}
    F = {k: frame(*pt) for k, pt in L.items()}
    out = {}
    for v in ("none", "candidate"):
        o = {k: observables(yukawas(F[k][0], F[k][1], sigmas(v, F[k][2], F[k][3], None), READS[v])) for k in L}
        d = {}
        for k in "APNTM":
            d6 = float(np.max(np.abs(o[k][0] - o["x"][0])))
            if o[k][3] > GAPV and o["x"][3] > GAPV:
                dj = abs(o[k][2] + o["x"][2]) if k == "M" else abs(o[k][2] - o["x"][2])
                dv = float(max(np.max(np.abs(o[k][1] - o["x"][1])), dj))
            else:
                dv = None
            d[k] = (d6, dv)
        out[v] = d
    return out


def signflip_p(d):
    """exact P(sum s_l d_l >= sum d_l) for independent signs, by convolution (float64)"""
    d = [int(x) for x in d]
    t_obs = sum(d)
    mags = [abs(x) for x in d if x != 0]
    tot = sum(mags)
    dist = np.zeros(2 * tot + 1); dist[tot] = 1.0
    for m in mags:
        new = np.zeros_like(dist)
        new[m:] += 0.5 * dist[:len(dist) - m]
        new[:len(dist) - m] += 0.5 * dist[m:]
        dist = new
    return float(dist[t_obs + tot:].sum())


def paired(recs, v, ref, lines):
    """per line on the points filtered under both: B, d = J_v - J_ref; returns (sum B, Delta_both, p, d array, B array, J_ref)"""
    idx = {l: i for i, l in enumerate(lines)}
    Bc = np.zeros(len(lines), dtype=np.int64); dv = np.zeros(len(lines), dtype=np.int64); Jr = np.zeros(len(lines), dtype=np.int64)
    for r in recs:
        if r["line"] not in idx:
            continue
        x, y = r[v], r[ref]
        if x["filt"] and y["filt"]:
            i = idx[r["line"]]
            Bc[i] += 1; jv, jr = int(x["corner"] and x["vud"]), int(y["corner"] and y["vud"])
            dv[i] += jv - jr; Jr[i] += jr
    sB = int(Bc.sum())
    dboth = dv.sum() / sB if sB else float("nan")
    p = signflip_p(dv) if sB else 1.0
    return sB, dboth, p, dv, Bc, Jr


def own_rate(recs, v, lines):
    ls = set(lines)
    f = [r[v] for r in recs if r["line"] in ls and r[v]["filt"]]
    return (sum(x["corner"] and x["vud"] for x in f) / len(f) if f else float("nan")), len(f)


def screen(recs, v, ref, lines):
    rv, nv = own_rate(recs, v, lines); rr, nr = own_rate(recs, ref, lines)
    sB, dboth, p, _, _, _ = paired(recs, v, ref, lines)
    delta = rv - rr
    ok = bool(delta >= MARGIN and dboth >= MARGIN and p * 2 ** BITS < ALPHA and sB >= FLOOR)
    return {"Delta": delta, "Delta_both": dboth, "p": p, "both": sB, "pass": ok, "n_v": nv, "n_ref": nr}


def power(recs, lines):
    sB, _, _, _, Bc, Jr = paired(recs, "candidate", "none", lines)
    r_both = Jr.sum() / sB
    q = min(1.0, r_both + LIFT)
    hits = 0
    for s in range(1, NPOW + 1):
        rng = np.random.default_rng(s)
        Jc = np.where(rng.random(len(Bc)) < q, Bc, 0)
        d = Jc - Jr
        dboth = d.sum() / sB
        p = signflip_p(d)
        hits += int(dboth >= MARGIN and p * 2 ** BITS < ALPHA)
    return hits / NPOW, q


def summary(recs, v, lines=None):
    ls = set(lines) if lines is not None else None
    f = [r[v] for r in recs if ls is None or r["line"] in ls]
    filt = [x for x in f if x["filt"]]
    n = len(filt)
    return {"points": len(f), "degenerate": sum(x["deg"] for x in f), "filtered": n,
            "joint": sum(x["corner"] and x["vud"] for x in filt),
            "rate": (sum(x["corner"] and x["vud"] for x in filt) / n if n else float("nan")),
            "corner": (sum(x["corner"] for x in filt) / n if n else float("nan")),
            "vud": (sum(x["vud"] for x in filt) / n if n else float("nan")),
            "q": (np.quantile([x["ratio"] for x in filt], [0.25, 0.5, 0.75]).tolist() if n else []),
            "Vud": (float(np.median([x["Vud"] for x in filt])) if n else float("nan"))}


if __name__ == "__main__":
    assert len(CENSUS) == 266 and len(BASE) == 236 and len(KEPT) == 230 and len(ORD4) == 6, (len(CENSUS), len(BASE), len(KEPT), len(ORD4))
    assert all(l in KEPT for l in K0_LINES)
    St = 0.3 * np.eye(2) + 0.2 * B.QI - 0.7 * B.QJ + 0.4 * B.QK
    assert np.allclose(read(St, "adj"), 0.3 * np.eye(2) - 0.2 * B.QI + 0.7 * B.QJ - 0.4 * B.QK)
    assert abs(BITS - 11.585) < 1e-3
    tasks = [(a, b, t) for (a, b) in KEPT + ORD4 for t in TAUS]
    with Pool(4) as pool:
        K0 = pool.map(k0, [(a, b, t) for (a, b) in K0_LINES for t in TAUS], chunksize=1)
        FR = dict(pool.map(frame_task, tasks, chunksize=4))

    kept_pts = [(a, b, t) for (a, b) in KEPT for t in TAUS]
    rbar = float(np.median([2 * abs(FR[p][2]) / abs(FR[p][3]) for p in kept_pts]))
    RECS = []
    for (a, b, t), (M, DR, a0, E) in FR.items():
        rec = {"line": (a, b), "tau": t, "r": float(2 * abs(a0) / abs(E)), "a0/DR": float(abs(a0) / np.linalg.norm(DR))}
        for v in VARIANTS:
            rec[v] = facts(yukawas(M, DR, sigmas(v, a0, E, rbar), READS[v]))
        RECS.append(rec)
    MAIN = [r for r in RECS if r["line"] in set(KEPT)]

    print("THE ADMISSIBLE SINGLET OF SIZE |a0|, SCREENED: %d census lines, %d kept (%d order-4 as a read-out), %d tau, %d points"
          % (len(CENSUS), len(KEPT), len(ORD4), len(TAUS), len(MAIN)))
    print("K0 the instrument (24 points; the six's largest change; |V| and J where both gaps exceed 1e-6, with the count; M with J -> -J):")
    k0_ok = True
    for v in ("none", "candidate"):
        parts = []
        for k in "APNTM":
            d6 = max(x[v][k][0] for x in K0); dv = [x[v][k][1] for x in K0 if x[v][k][1] is not None]
            k0_ok = k0_ok and d6 <= K0TOL and all(t <= K0TOL for t in dv)
            parts.append("%s %.1e/%s (%d)" % (k, d6, "%.1e" % max(dv) if dv else "-", len(dv)))
        print("    %-10s %s" % (v, "  ".join(parts)))
    print("    K0 %s" % ("HOLDS" if k0_ok else "FAILS"))

    print("the variants on the 230 lines, each on its own filtered points (rbar = %.4g):" % rbar)
    for v in VARIANTS:
        s = summary(MAIN, v)
        print("    %-10s points %d  degenerate %d  filtered %d  joint %d  rate %.4f  corner alone %.4f  |V_ud|>0.9 alone %.4f"
              "  |V_ub|/|V_td| quartiles %s  median |V_ud| %.4f" % (v, s["points"], s["degenerate"], s["filtered"], s["joint"],
              s["rate"], s["corner"], s["vud"], ", ".join("%.3g" % q for q in s["q"]), s["Vud"]))

    rn, nn = own_rate(MAIN, "none", KEPT)
    K1 = rn <= 0.10
    print("K1 none's rate %.4f (on %d filtered points) <= 0.10: %s" % (rn, nn, "HOLDS" if K1 else "FAILS"))
    T = {v: screen(MAIN, v, "none", KEPT) for v in VARIANTS if v != "none"}
    for v, t in T.items():
        print("    %-10s vs none: Delta %+.4f, Delta_both %+.4f on %d common points, p %.3e, p*2^7 %.3e, p*2^11.58 %.3e, passes K2's test: %s"
              % (v, t["Delta"], t["Delta_both"], t["both"], t["p"], t["p"] * 2 ** BITS7, t["p"] * 2 ** BITS, t["pass"]))
    K2 = T["candidate"]["pass"]
    if ALPHA / 2 ** BITS <= T["candidate"]["p"] < 0.01 / 2 ** 11.58:
        print("    note: the candidate's p lies between the exact bar and the rule's rounded one")
    K3 = not T["even"]["pass"]
    nc, nn2 = own_rate(MAIN, "candidate", KEPT)[1], own_rate(MAIN, "none", KEPT)[1]
    K4 = nc >= 0.25 * nn2
    print("K2 the screen (the candidate against none): %s" % ("HOLDS" if K2 else "FAILS"))
    print("K3 even does not pass K2's whole test: %s" % ("HOLDS" if K3 else "FAILS"))
    print("K4 the candidate's filtered count %d >= a quarter of none's %d: %s" % (nc, nn2, "HOLDS" if K4 else "FAILS"))

    pw = q = None
    if not k0_ok:
        grade = "VOID (K0 fails)"
    elif K2:
        sg = screen(MAIN, "candidate", "even", KEPT)
        credit = sg["p"] < 0.01 and sg["Delta_both"] > 0
        print("the sign: the candidate against even, paired: Delta_both %+.4f on %d common points, p %.3e: %s"
              % (sg["Delta_both"], sg["both"], sg["p"], "credited" if credit else "not credited"))
        grade = "CANDIDATE (level 1)" + ("" if credit else "; the sign not credited: 'a singlet of size |a0|'")
        if T["up-only"]["pass"]:
            grade += "; up-only passes: 'a sector-different singlet of size |a0|'"
        if not K4:
            grade += "; K4 fails: scoped to the lines that keep their hierarchy"
    else:
        sB = T["candidate"]["both"]
        if sB >= FLOOR:
            pw, q = power(MAIN, KEPT)
        grade = "NOT FOUND within the reach" if (sB >= FLOOR and pw is not None and pw >= 0.80) else "UNDECIDED"
    print("power (500 sets, full line clustering, q = r_both + 0.25 = %s): %s" % ("-" if q is None else "%.4f" % q, "-" if pw is None else "%.3f" % pw))
    print("GRADE: %s" % grade)

    print("read-outs:")
    for t in TAUS:
        sub = [r for r in MAIN if r["tau"] == t]
        print("    tau %s  %s" % (t, "  ".join("%s %d/%d" % (v, summary(sub, v)["filtered"], summary(sub, v)["joint"]) for v in VARIANTS)))
    o4 = [r for r in RECS if r["line"] in set(ORD4)]
    print("    the order-4 lines (%d points): %s" % (len(o4), "  ".join("%s %d/%d" % (v, summary(o4, v)["filtered"], summary(o4, v)["joint"]) for v in VARIANTS)))
    a16 = [r for r in MAIN if r["line"][0] in (Fr(1, 6), Fr(1, 2), Fr(5, 6))]
    print("    the lines with a in {1/6, 1/2} (%d points): %s" % (len(a16), "  ".join("%s %d/%d" % (v, summary(a16, v)["filtered"], summary(a16, v)["joint"]) for v in VARIANTS)))
    for key, nm in (("r", "2|a0|/|eta^3|"), ("a0/DR", "|a0|/|DR|")):
        vals = np.array([r[key] for r in MAIN])
        print("    %s: min %.3g, quartiles %s, max %.3g" % (nm, vals.min(), ", ".join("%.3g" % qq for qq in np.quantile(vals, [0.25, 0.5, 0.75])), vals.max()))
