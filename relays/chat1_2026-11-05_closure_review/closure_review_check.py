"""The web seat, 2026-11-05: cc's asks 1 and 3 (P-699), the checks behind the review of B1841 and B1842. Data-free.

No data file is opened, no held-out quantity is computed, and no inter-sector quantity is computed on a line of the
family's classes (3a = +-1/5 mod 1: the slope 2/5, 3/5 and the four lines the Higgs-twist law ties to them); an assert
guards every line used. Main's instruments are imported unchanged from the checkout given.

(A) B1841's ends at B1839's apexes.
    (A1) All 223 apexes reduced by T^-1 exactly as B1839's census.py does: the range of Im tau and |Re tau|, the values of
         n, and the shortest lattice vector (E2 = ln 2 is the level of the largest disc the cell holds only where it is 1).
    (A2) At six apexes fixed by position only (least, median and greatest Im tau; the first with Re tau = +1/2 and the first
         with Re tau = -1/2; the apex of greatest |Re tau| below 1/2): the accessory parameter continued from the control
         point by B1667's newton_walk (as B1839's accessory_all does), B1667's geometry, the four ends, and E3's
         half-period identity L_max = ln 2 - Re g(1/2), an independent route to L_max (no min|c| search).
(B) B1842's exact end per sector, nu included: two generic tau, five lines off the family's classes (orders 12, 5, 10, 9,
    36), delta 0.3 and 2.0. For each sector its live channels (|R_s| > 1e-12, as the instruments zero them); the norms of
    nu against up and down, up against down and lep against down, where both are live; and each sector's Yukawa from
    yukawas_exact() against the class-cache route (down's norms with the sector's own residues).
(C) The T^-1 reduction.
    (C1) C-T's two input pairs through B1842's reduce(): the reduced (tau, a, b) of each side.
    (C2) What 'mod 1' drops: the twist point moved by a lattice vector, w -> w + 1 and w -> w + tau, per sector: the
         singular-value ratios and the entrywise moduli of Y (scaled by the largest entry) against those at w.
(D) C-MIR at its own two points, delta 0.3, every sector and reading: the moduli test as coded; the full relation
    max|Y2 - P conj(Y1) P| / max|Y2|; and a wrong relation (P Y1 P, no conjugation) under both tests.
(E) The family's slope inside B1842's controls: C-M's lines with a in {2/5, 3/5}, and C-T's points (enumeration only).

    python3 closure_review_check.py <main checkout>      (main at a494173bc)
"""
import contextlib
import importlib.util
import io
import math
import pathlib
import sys
from fractions import Fraction as F

import numpy as np

ROOT = pathlib.Path(sys.argv[1]).resolve()
CHK = ROOT / "frontier" / "B1842_the_closure_instruments" / "verification"
FAMILY_3A = {F(1, 5), F(4, 5)}
UNITS = ("1", "i", "j", "k")


def load(name, path):
    sp = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(sp); sys.modules[name] = m
    with contextlib.redirect_stdout(io.StringIO()):
        sp.loader.exec_module(m)
    return m


X = load("p688_exact_card_instrument", CHK / "exact_card_instrument.py")
with contextlib.redirect_stdout(io.StringIO()):
    MX = X.mods()
ee, B, C = MX["ee"], MX["B"], MX["C"]


def guard(a, b):
    assert (3 * F(a)) % 1 not in FAMILY_3A, ("a line of the family's classes", a, b)


def geo(tau):
    with contextlib.redirect_stdout(io.StringIO()):
        c, res = X.accessory(tau)
        G = ee.geometry(tau, c); rd = ee.higgs(tau)
    return c, res, G, rd


def sector_data(tau, w, sec, G, Lh):
    ql, qr = X.CHARGES[sec]
    x, yy = B.sector_twists(w, tau, ql, qr); R = B.residues(x, yy, tau)
    N, _ = ee.twisted_norms(tau, G["al"], G["be"], Lh, x, yy, R, nth=X.NTH, ns=X.NS)
    return R, N


def yuk(R, N, rd):
    u = {s: (math.sqrt(N[s]) * R[s] if N.get(s) is not None and N[s] > 0 else 0) for s in UNITS}
    Mw = B.weighted_M(u)
    return {rn: B.coupling(H, Mw) for rn, H in rd.items()}


def svr(Y):
    sv = np.linalg.svd(Y, compute_uv=False); return np.array([sv[1] / sv[0], sv[2] / sv[0]])


def mods_scaled(Y):
    A = np.abs(Y); return A / A.max()


def part_a():
    print("(A) B1841's ends at B1839's apexes")
    C39 = load("b1839_census", ROOT / "frontier" / "B1839_the_end_card" / "verification" / "census.py")
    with contextlib.redirect_stdout(io.StringIO()):
        M = C39.mods()
    AP = M["AP"]
    red = [C39.reduce(complex(p["Re_tau"], p["Im_tau"])) for p in AP]
    taus = [t for t, _ in red]

    def shortest(t, n=6):
        return min(abs(a + b * t) for a in range(-n, n + 1) for b in range(-n, n + 1) if (a, b) != (0, 0))
    sv = [shortest(t) for t in taus]
    print("  (A1) %d apexes: Im tau %.4f-%.4f; |Re tau| <= %.4f (at exactly 1/2: %d); n in %s; shortest lattice vector "
          "%.12f-%.12f (below 1 at %d)" % (len(taus), min(t.imag for t in taus), max(t.imag for t in taus),
                                           max(abs(t.real) for t in taus), sum(1 for t in taus if abs(abs(t.real) - 0.5) < 1e-15),
                                           sorted(set(n for _, n in red)), min(sv), max(sv), sum(1 for s in sv if s < 1 - 1e-12)))
    order = sorted(range(len(taus)), key=lambda i: taus[i].imag)
    pick = [order[0], order[len(order) // 2], order[-1]]
    for cond in (lambda t: abs(t.real - 0.5) < 1e-15, lambda t: abs(t.real + 0.5) < 1e-15):
        hit = [i for i in range(len(taus)) if cond(taus[i])]
        if hit and hit[0] not in pick:
            pick.append(hit[0])
    inner = [i for i in range(len(taus)) if abs(abs(taus[i].real) - 0.5) >= 1e-15]
    k = max(inner, key=lambda i: abs(taus[i].real))
    if k not in pick:
        pick.append(k)
    worst_w = worst_4 = 0.0
    for i in pick:
        tau = taus[i]; c, res, G, _ = geo(tau)
        LW = math.log(2) - float(C.g_local(G["al"], G["be"], 0.5).real)
        L4 = G["L_2"] - math.pi / 2; d4f = math.pi * (0.5 - 2 / G["cusp_area"])
        worst_w = max(worst_w, abs(LW - G["L_max"])); worst_4 = max(worst_4, abs((L4 - G["L_max"]) - d4f))
        print("  (A2) apex %3d tau %+.4f%+.4fi (n %d): residual %.1e; L_max %.9f, ln 2 - Re g(1/2) %.9f (diff %.1e); "
              "E1 L_2 %.6f (delta %.4f) | E2 ln 2 (delta %.4f) | E4 %.6f (delta %.4f) | A_cusp %.4f" % (
                  i, tau.real, tau.imag, red[i][1], float(np.max(np.abs(res))), G["L_max"], LW, LW - G["L_max"], G["L_2"],
                  G["L_2"] - G["L_max"], math.log(2) - G["L_max"], L4, L4 - G["L_max"], G["cusp_area"]))
    print("  (A2) largest |L_max - (ln 2 - Re g(1/2))| %.1e; largest |delta_4 - pi(1/2 - 2/A_cusp)| %.1e" % (worst_w, worst_4))


def part_b():
    print("(B) B1842's exact end per sector, nu included")
    lines = [(F(1, 3), F(1, 4)), (F(1, 5), F(0)), (F(1, 10), F(3, 10)), (F(1, 9), F(0)), (F(1, 4), F(2, 9))]
    worst = {"nu~up": 0.0, "nu~down": 0.0, "up~down": 0.0, "lep~down": 0.0, "Y vs cache": 0.0}
    incl = True
    for tau in (complex(0.31, 2.9), complex(-0.12, 3.2)):
        c, res, G, rd = geo(tau)
        for (a, b) in lines:
            guard(a, b); w = float(a) * tau + float(b)
            for d in (0.3, 2.0):
                Lh = G["L_max"] + d; Rs, Ns = {}, {}
                for sec in X.CHARGES:
                    Rs[sec], Ns[sec] = sector_data(tau, w, sec, G, Lh)
                live = {sec: frozenset(s for s in UNITS if abs(Rs[sec][s]) > 1e-12) for sec in X.CHARGES}
                for (p, q) in (("nu", "up"), ("nu", "down"), ("up", "down"), ("lep", "down")):
                    for s in live[p] & live[q]:
                        worst["%s~%s" % (p, q)] = max(worst["%s~%s" % (p, q)], abs(Ns[p][s] / Ns[q][s] - 1))
                incl &= live["nu"] == live["down"] and live["up"] <= live["down"] and live["lep"] <= live["down"]
                Yx, _ = X.yukawas_exact(tau.real, tau.imag, a, b, d)
                for sec in X.CHARGES:
                    Nc = {s: (Ns["down"][s] if s in live[sec] else 0.0) for s in UNITS}
                    Yc = yuk(Rs[sec], Nc, rd)
                    for rn in Yc:
                        worst["Y vs cache"] = max(worst["Y vs cache"], float(np.max(np.abs(Yx[sec][rn] - Yc[rn])) / np.max(np.abs(Yx[sec][rn]))))
                print("  tau %+.2f%+.2fi line (%s, %s) delta %.1f: live channels %s" % (
                    tau.real, tau.imag, a, b, d, {sec: "".join(sorted(live[sec])) for sec in X.CHARGES}))
    print("  (B) norms where both are live, largest relative difference: %s" % {k: "%.1e" % v for k, v in worst.items()})
    print("  (B) nu's live channels = down's, and up's and lep's within down's, at every case: %s" % incl)


def part_c():
    print("(C) the T^-1 reduction")
    for (re_t, im_t, a, b) in ((0.31, 2.9, F(1, 3), F(1, 4)), (-0.2, 3.1, F(2, 5), F(3, 10))):
        r1 = X.reduce(complex(re_t, im_t), a, b); r2 = X.reduce(complex(re_t + 1, im_t), a, (b - a) % 1)
        print("  (C1) C-T's pair at %s: reduced %s and %s; identical: %s" % (
            (re_t, im_t, str(a), str(b)), (r1[0], str(r1[1]), str(r1[2])), (r2[0], str(r2[1]), str(r2[2])),
            r1[0] == r2[0] and r1[1] == r2[1] and r1[2] == r2[2]))
    worst = {"w+1 sv": 0.0, "w+1 |Y|": 0.0, "w+tau sv": 0.0, "w+tau |Y|": 0.0}
    for tau in (complex(0.31, 2.9), complex(-0.12, 3.2)):
        c, res, G, rd = geo(tau); Lh = G["L_max"] + 0.3
        for (a, b) in ((F(1, 3), F(1, 4)), (F(1, 10), F(3, 10))):
            guard(a, b); w = float(a) * tau + float(b)
            for sec in X.CHARGES:
                Y0 = yuk(*sector_data(tau, w, sec, G, Lh), rd)
                for tag, sh in (("w+1", 1.0), ("w+tau", tau)):
                    Y1 = yuk(*sector_data(tau, w + sh, sec, G, Lh), rd)
                    for rn in Y0:
                        worst[tag + " sv"] = max(worst[tag + " sv"], float(np.max(np.abs(svr(Y1[rn]) / svr(Y0[rn]) - 1))))
                        worst[tag + " |Y|"] = max(worst[tag + " |Y|"], float(np.max(np.abs(mods_scaled(Y1[rn]) - mods_scaled(Y0[rn])))))
    print("  (C2) lattice translations of the twist point, every sector and reading, two tau x two lines, delta 0.3: %s" % {
        k: "%.1e" % v for k, v in worst.items()})


def part_d():
    print("(D) C-MIR")
    Pm = np.diag([1, 1, -1]); res = {"moduli": 0.0, "full": 0.0, "wrong, moduli": 0.0, "wrong, full": 0.0}
    for (re_t, im_t, a, b) in ((0.27, 2.95, F(1, 3), F(1, 7)), (0.13, 3.05, F(1, 4), F(2, 9))):
        guard(a, b)
        with contextlib.redirect_stdout(io.StringIO()):
            Y1, _ = X.yukawas_exact(re_t, im_t, a, b, 0.3); Y2, _ = X.yukawas_exact(-re_t, im_t, a, (-b) % 1, 0.3)
        for sec in X.CHARGES:
            for rn in ("S", "St"):
                A = Y2[sec][rn]; Bm = Pm @ np.conj(Y1[sec][rn]) @ Pm; W = Pm @ Y1[sec][rn] @ Pm; s = float(np.max(np.abs(A)))
                res["moduli"] = max(res["moduli"], float(np.max(np.abs(np.abs(A) - np.abs(Bm)))) / s)
                res["full"] = max(res["full"], float(np.max(np.abs(A - Bm))) / s)
                res["wrong, moduli"] = max(res["wrong, moduli"], float(np.max(np.abs(np.abs(A) - np.abs(W)))) / s)
                res["wrong, full"] = max(res["wrong, full"], float(np.max(np.abs(A - W))) / s)
    print("  (D) two points x four sectors x two readings: %s" % {k: "%.1e" % v for k, v in res.items()})


def part_e():
    print("(E) the family's slope inside B1842's controls (enumeration only)")
    def order(a, b): return math.lcm(F(a).denominator, F(b).denominator)
    lines = sorted({(F(p, n), F(q, n)) for n in (2, 3, 4, 5, 6) for p in range(n) for q in range(n) if (p, q) != (0, 0)})
    lines = [l for l in lines if order(*l) in (2, 3, 4, 5, 6)]
    fam = [l for l in lines if l[0] in (F(2, 5), F(3, 5))]
    print("  C-M's lines: %d, of which %d have a in {2/5, 3/5}: %s" % (len(lines), len(fam), [(str(a), str(b)) for a, b in fam]))
    print("  C-T's points: (1/3, 1/4) and (2/5, 3/10); C-MIR's: (1/3, 1/7) and (1/4, 2/9)")


if __name__ == "__main__":
    part_a(); part_b(); part_c(); part_d(); part_e()
    print("closure_review_check exit 0")
