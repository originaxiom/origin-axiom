"""The web seat's check for its note on the strong angle's counterterm rule (the theta-bar card's first step; data-free;
no measured value is read; no theta_Y is evaluated on the candidate family's slope, a = 2/5 or 3/5).

Notation: a line is (a, b) as in B1726's census, w = a tau + b (main's B.line_w(a, -b, tau)). theta_Y = arg det Y_u +
arg det Y_d, the quark Yukawas built as B1821's module builds them (FR-FIB: residues, channel norms, the two radius
rules, the coupling; c not applied; H = I; h0 = 0).

The relabellings of a point x = (a, b, tau) that the note checks:
  A: (a, b + 1, tau)        w -> w + 1
  P: (a + 1, b, tau)        w -> w + tau
  N: (-a, -b, tau)          w -> -w
  T: (a, b - a, tau + 1)    the same w at tau + 1
  M: (a, -b, -conj(tau))    B1821's mirror
The closed forms the note states (radians, mod 2 pi): A shifts arg det Y_u by 204 pi a and arg det Y_d by 60 pi a, so
theta_Y by 264 pi a = 12 pi a sum(q_L^2 + q_R^2); P and N leave it; T shifts it by -132 pi a^2 - pi/2 in the readings
(S~, S) and (S, S~); M sends it to -theta_Y. The masses, |V| and J are unchanged by A, P, N and T; M keeps the masses and
|V| and sends J to -J.

(1) The relabellings. On 14 lines (orders 1-12 except 4, slopes 2/5 and 3/5 excluded) at tau = 0.13 + 2.2i,
    -0.27 + 2.6i and 0.41 + 1.7i, for the directions DR, a0, F_-10, F_6, F_22 (the null R and t = -5/288 have det Y = 0),
    both radius rules and the four (up, down) readings: the largest departure of each labelling from its closed form
    (wrapped to (-pi, pi]), and of the masses (six normalised singular values), |V_us|, |V_cb|, |V_ub| and J. For T in
    the readings (S, S) and (S~, S~): the constant left after removing -132 pi a^2, per direction, in units of pi.
    For M: whether each reading pair maps to itself or to its swap (the masses compared both ways).
(2) The ambiguity. For every slope a = r/s with s <= 12 and 0 <= a <= 1/2: N_A = the order of 132a in Q/Z (the A
    anomaly), N_T = the order of 66a^2 + 1/4 (the T anomaly), N = lcm(N_A, N_T), the order of the group the two generate.
    theta_Y is a function of the physical point only modulo 2 pi / N. Exact arithmetic.
(3) CP on the mirror's fixed set. A point is fixed by M up to a relabelling when Re tau = -k/2 and 2b = ka (mod 1)
    (M x = T^k A^m x). There the closed forms give theta_Y = 264 pi a b + 132 pi a^2 Re tau - (pi/2) Re tau (mod pi).
    On 12 such points (off the family's slope) at Im tau 2.2 and 2.6, in (S~, S) with DR, a0 and F_6, both radius
    rules: the largest departure from that value mod pi, and the largest |J|.
(4) The counterterm. theta_ct = -264 pi a b + (pi/2 - 132 pi a^2) Re tau. At (1)'s points in (S~, S): the largest
    departure of theta_Y + theta_ct from invariance under A, T and N and from oddness under M; and, for contrast, the
    smallest shift under P (theta_ct is not P-invariant).
(5) The modular route (FPST's condition, P-461). For every slope r/s with s <= 400: whether the T anomaly can vanish
    (66a^2 + 1/4 an integer), and how many slopes have a vanishing A anomaly (132a an integer). Exact arithmetic.

Usage: python3 theta_rule_check.py <main checkout>   (main at 354a4ea4d)
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
QUARKS = (("up", 1, -4), ("down", 1, 2))
DIRS = ("DR", "a0", "F_-10", "F_6", "F_22")
RP = ((1, 0), (0, 1), (0, 0), (1, 1))          # (up, down) readings: 1 = S~, 0 = S
RPN = {(1, 0): "(S~, S)", (0, 1): "(S, S~)", (0, 0): "(S, S)", (1, 1): "(S~, S~)"}
LINES = [(Fr(1, 7), Fr(2, 7)), (Fr(1, 3), Fr(1, 6)), (Fr(3, 8), Fr(1, 8)), (Fr(1, 5), Fr(2, 5)), (Fr(3, 7), Fr(1, 7)),
         (Fr(2, 9), Fr(1, 3)), (Fr(1, 2), Fr(1, 3)), (Fr(1, 9), Fr(4, 9)), (Fr(3, 10), Fr(1, 5)), (Fr(5, 12), Fr(1, 6)),
         (Fr(1, 11), Fr(3, 11)), (Fr(1, 6), Fr(1, 2)), (Fr(0), Fr(1, 5)), (Fr(1, 2), Fr(1, 2))]
TAUS = (complex(0.13, 2.2), complex(-0.27, 2.6), complex(0.41, 1.7))
FAMILY = (Fr(2, 5), Fr(3, 5))


def wrap(x, period=2 * PI):
    return (x + period / 2) % period - period / 2


def guard(a):
    if Fr(a) % 1 in FAMILY:
        raise SystemExit("refused: the candidate family's slope")


_DC = {}


def direction(d, tau):
    if (d, tau) not in _DC:
        with contextlib.redirect_stdout(io.StringIO()):
            _DC[(d, tau)] = Z.direction(d, tau)
    return _DC[(d, tau)]


def ys(a, b, tau):
    """{(sector, radius index, direction, reading): Y} at the point (a, b, tau)."""
    guard(a)
    Ls = Z.radii(tau)
    dirs = {d: direction(d, tau) for d in DIRS}
    out = {}
    for sn, ql, qr in QUARKS:
        w = B.line_w(float(a), -float(b), tau); x, y = B.sector_twists(w, tau, ql, qr)
        with contextlib.redirect_stdout(io.StringIO()):
            R = B.residues(x, y, tau); c = B.cA(x, y, tau, R)
        for ri, L in enumerate(Ls):
            u = {k: (math.sqrt(2 * PI * L + c[k]) * R[k] if c[k] is not None and 2 * PI * L + c[k] > 0 else 0) for k in B.UNITS}
            M = B.weighted_M(u)
            for d, av in dirs.items():
                S0 = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
                out[(sn, ri, d, 0)] = B.coupling(S0, M)
                out[(sn, ri, d, 1)] = B.coupling(B.EPS @ S0.conj() @ B.EPS.T, M)
    return out


def obs(Y, ri, d, ru, rd):
    Yu, Yd = Y[("up", ri, d, ru)], Y[("down", ri, d, rd)]
    au, ad = np.angle(np.linalg.det(Yu)), np.angle(np.linalg.det(Yd))
    uu, su, _ = np.linalg.svd(Yu); ud, sd, _ = np.linalg.svd(Yd)
    ou, od = np.argsort(su), np.argsort(sd)
    masses = np.concatenate([su[ou] / su.max(), sd[od] / sd.max()])
    V = uu[:, ou].conj().T @ ud[:, od]
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    return {"u": au, "d": ad, "th": au + ad, "m": masses, "V": np.abs([V[0, 1], V[1, 2], V[0, 2]]), "J": J}


def theta_ct(a, b, tau):
    return -264 * PI * float(a * b) + (PI / 2 - 132 * PI * float(a * a)) * tau.real


def labellings(a, b, tau):
    return {"x": (a, b, tau), "A": (a, b + 1, tau), "P": (a + 1, b, tau), "N": (-a, -b, tau), "T": (a, b - a, tau + 1),
            "M": (a, -b, complex(-tau.real, tau.imag))}


def work1(task):
    a, b, tau = task
    L = labellings(a, b, tau)
    Ys = {k: ys(*v) for k, v in L.items()}
    rec = []
    for ri in (0, 1):
        for d in DIRS:
            for ru, rd in RP:
                o = {k: obs(Ys[k], ri, d, ru, rd) for k in Ys}
                oswap = obs(Ys["M"], ri, d, rd, ru) if (ru, rd) in ((1, 0), (0, 1)) else None
                rec.append(((a, b, tau), ri, d, (ru, rd), o, oswap))
    return rec


def fixed_points():
    pts = []
    for (a, b, k) in ((Fr(1, 7), Fr(0), 0), (Fr(1, 7), Fr(1, 2), 0), (Fr(3, 8), Fr(1, 2), 0), (Fr(2, 9), Fr(0), 0),
                      (Fr(1, 3), Fr(1, 2), 0), (Fr(1, 3), Fr(1, 3), -1), (Fr(1, 7), Fr(3, 7), -1), (Fr(1, 5), Fr(2, 5), -1),
                      (Fr(3, 7), Fr(2, 7), -1), (Fr(1, 4), Fr(3, 8), -1), (Fr(1, 3), Fr(2, 3), 1), (Fr(1, 3), Fr(1, 6), -2)):
        assert ((2 * b - k * a) % 1) == 0
        for im in (2.2, 2.6):
            pts.append((a, b, complex(-k / 2, im)))
    return pts


def work3(task):
    a, b, tau = task
    return (a, b, tau), ys(a, b, tau)


def order_qz(x):
    return (Fr(x) % 1).denominator


if __name__ == "__main__":
    tasks1 = [(a, b, t) for (a, b) in LINES for t in TAUS]
    with Pool(2) as pool:
        recs = [r for part in pool.map(work1, tasks1, chunksize=1) for r in part]
        fx = dict(pool.map(work3, fixed_points(), chunksize=1))

    print("(1) the relabellings: %d lines x %d tau x %d directions x 2 radius rules x 4 readings = %d rows"
          % (len(LINES), len(TAUS), len(DIRS), len(recs)))
    dev = {k: 0.0 for k in ("A_u", "A_d", "A", "P", "N", "T", "M")}
    phys = {k: 0.0 for k in ("A", "P", "N", "T")}
    physM = 0.0; jM = 0.0
    tconst = {}
    mself = {rp: 0.0 for rp in RP}; mswap = {rp: np.inf for rp in ((1, 0), (0, 1))}
    for (pt, ri, d, rp, o, oswap) in recs:
        a = float(pt[0]); x = o["x"]
        dev["A_u"] = max(dev["A_u"], abs(wrap(o["A"]["u"] - x["u"] - 204 * PI * a)))
        dev["A_d"] = max(dev["A_d"], abs(wrap(o["A"]["d"] - x["d"] - 60 * PI * a)))
        dev["A"] = max(dev["A"], abs(wrap(o["A"]["th"] - x["th"] - 264 * PI * a)))
        dev["P"] = max(dev["P"], abs(wrap(o["P"]["th"] - x["th"])))
        dev["N"] = max(dev["N"], abs(wrap(o["N"]["th"] - x["th"])))
        if rp in ((1, 0), (0, 1)):
            dev["T"] = max(dev["T"], abs(wrap(o["T"]["th"] - x["th"] + 132 * PI * a * a + PI / 2)))
        else:
            tconst.setdefault((rp, d), []).append(wrap(o["T"]["th"] - x["th"] + 132 * PI * a * a) / PI)
        for k in phys:
            phys[k] = max(phys[k], np.max(np.abs(o[k]["m"] - x["m"])), np.max(np.abs(o[k]["V"] - x["V"])), abs(o[k]["J"] - x["J"]))
        dev["M"] = max(dev["M"], abs(wrap(o["M"]["th"] + x["th"])))
        physM = max(physM, np.max(np.abs(o["M"]["m"] - x["m"])), np.max(np.abs(o["M"]["V"] - x["V"])))
        jM = max(jM, abs(o["M"]["J"] + x["J"]))
        mself[rp] = max(mself[rp], np.max(np.abs(o["M"]["m"] - x["m"])))
        if oswap is not None:
            mswap[rp] = min(mswap[rp], np.max(np.abs(oswap["m"] - x["m"])))
    print("    A: arg det Y_u - 204 pi a: %.1e; arg det Y_d - 60 pi a: %.1e; theta_Y - 264 pi a: %.1e" % (dev["A_u"], dev["A_d"], dev["A"]))
    print("    P: %.1e;  N: %.1e;  T in (S~, S) and (S, S~), theta_Y + 132 pi a^2 + pi/2: %.1e;  M, theta_Y(Mx) + theta_Y(x): %.1e"
          % (dev["P"], dev["N"], dev["T"], dev["M"]))
    print("    the masses, |V| and J under A, P, N, T (largest change): %s" % ", ".join("%s %.1e" % kv for kv in phys.items()))
    print("    under M: the masses and |V| change by %.1e; J(Mx) + J(x) %.1e" % (physM, jM))
    print("    M keeps each reading pair (largest mass change with the pair kept): %s" % ", ".join("%s %.1e" % (RPN[k], v) for k, v in mself.items()))
    print("    M with the pair swapped (smallest mass change): %s" % ", ".join("%s %.1e" % (RPN[k], v) for k, v in mswap.items()))
    print("    T in (S, S) and (S~, S~): theta_Y's shift + 132 pi a^2, in units of pi (spread over lines, tau, radii):")
    for (rp, d), v in sorted(tconst.items(), key=lambda kv: (kv[0][0], DIRS.index(kv[0][1]))):
        v = np.array(v); m = float(np.angle(np.mean(np.exp(1j * PI * v))) / PI)
        print("        %-9s %-6s %+.4f (spread %.1e)" % (RPN[rp], d, m, float(np.max(np.abs(wrap(PI * (v - m)))) / PI)))

    print("(2) the ambiguity: theta_Y is a function of the physical point only modulo 2 pi / N")
    print("    slope a  N_A (from A)  N_T (from T)  N")
    for s in range(1, 13):
        for r in range(0, s // 2 + 1):
            if gcd(r, s) != 1:
                continue
            a = Fr(r, s); NA = order_qz(132 * a); NT = order_qz(66 * a * a + Fr(1, 4))
            print("    %-7s  %-12d  %-12d  %d" % (a, NA, NT, NA * NT // gcd(NA, NT)))

    print("(3) CP on the mirror's fixed set, (S~, S), DR / a0 / F_6, both radius rules")
    worst = 0.0; Jmax = 0.0; npt = 0
    for (a, b, tau), Y in fx.items():
        pred = 264 * PI * float(a * b) + 132 * PI * float(a * a) * tau.real - (PI / 2) * tau.real
        for ri in (0, 1):
            for d in ("DR", "a0", "F_6"):
                o = obs(Y, ri, d, 1, 0); npt += 1
                worst = max(worst, abs(wrap(o["th"] - pred, PI))); Jmax = max(Jmax, abs(o["J"]))
    print("    %d rows on 12 fixed points x Im tau 2.2, 2.6: theta_Y - (264 pi a b + 132 pi a^2 Re tau - (pi/2) Re tau) "
          "mod pi, largest %.1e; largest |J| %.1e" % (npt, worst, Jmax))

    print("(4) the counterterm theta_ct = -264 pi a b + (pi/2 - 132 pi a^2) Re tau, (S~, S)")
    inv = {"A": 0.0, "T": 0.0, "N": 0.0, "M (odd)": 0.0}; pbig = ptot = 0
    for (pt, ri, d, rp, o, oswap) in recs:
        if rp != (1, 0):
            continue
        L = labellings(*pt); tb = {k: o[k]["th"] + theta_ct(*L[k]) for k in L}
        for k in ("A", "T", "N"):
            inv[k] = max(inv[k], abs(wrap(tb[k] - tb["x"])))
        inv["M (odd)"] = max(inv["M (odd)"], abs(wrap(tb["M"] + tb["x"])))
        ptot += 1; pbig += abs(wrap(tb["P"] - tb["x"])) > 1e-6
    fxd = 0.0
    for (a, b, tau), Y in fx.items():
        for ri in (0, 1):
            for d in ("DR", "a0", "F_6"):
                fxd = max(fxd, abs(wrap(obs(Y, ri, d, 1, 0)["th"] + theta_ct(a, b, tau), PI)))
    print("    theta_Y + theta_ct: change under A %.1e, T %.1e, N %.1e; under M, theta_bar(Mx) + theta_bar(x) %.1e;"
          " on (3)'s fixed points mod pi %.1e" % (inv["A"], inv["T"], inv["N"], inv["M (odd)"], fxd))
    print("    under P (not a symmetry of theta_ct): theta_Y + theta_ct changes by more than 1e-6 on %d of %d rows" % (pbig, ptot))

    print("(5) the modular route: can theta_Y be invariant under T on any line?")
    zT = [Fr(r, s) for s in range(1, 401) for r in range(0, s) if gcd(r, s) == 1 and (66 * Fr(r, s) ** 2 + Fr(1, 4)).denominator == 1]
    zA = [Fr(r, s) for s in range(1, 401) for r in range(0, s) if gcd(r, s) == 1 and (132 * Fr(r, s)).denominator == 1]
    nsl = sum(1 for s in range(1, 401) for r in range(0, s) if gcd(r, s) == 1)
    print("    slopes r/s in [0, 1), s <= 400: %d; with the T anomaly zero: %d; with the A anomaly zero: %d (s | 132)"
          % (nsl, len(zT), len(zA)))
