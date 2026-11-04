"""The web seat's check for its note on the Higgs singlet's law (RI-1, P-591, P-566; data-free; no measured value is read;
nothing is computed on the candidate family's slope, a = 2/5 or 3/5; no D, no corner order, no theta-bar).

Notation: a line is (a, b), w = a tau + b (main's B.line_w(a, -b, tau)). The frame is FR-FIB as B1821's module builds it
(B1656's residues, channel norms and coupling; the radius rule L_max; c not applied; H = I) with the record's Higgs
triplet DR (the Serre derivative of R). A singlet sigma_X is added in sector X: S_X = sigma_X 1 + DR.(i, j, k). Readings:
"eq" = every sector reads S_X (W183's); "SM" = up reads eps conj(S_up) eps^T, down and leptons read S_X. a0(X) is the
Laurent constant of the identity-channel kernel at the sector's summed twist u_X = (q_L + q_R) w, in closed form
2 pi i Im(u_X)/Im(tau) + theta_1'(u_X)/theta_1(u_X) (W183's route 1). eta^3 is summed from its product with
q^(1/24) = e^(2 pi i tau/24), so no branch is taken.

The relabellings of a point x = (a, b, tau) (theta_rule_check.py's; all in B1790's list of maps on record):
  A: (a, b + 1, tau)   P: (a + 1, b, tau)   N: (-a, -b, tau), the elliptic involution w -> -w
  T: (a, b - a, tau + 1)   M: (a, -b, -conj(tau)), B1821's mirror
Observables compared: the six (m1/m3, m2/m3 in each sector), |V_us|, |V_cb|, |V_ub|, |V_td| and J, with V = U_up^dag
U_down from the left singular vectors, lightest first. |V| and J are compared only where neither quark sector has two
singular values within 1e-6 of each other (rows skipped are counted).

(0) The instrument, on LINES x TAUS: main's a0_of['1'] against the closed form (where main's identity residue is not
    below its 1e-12 cut; the rows where it is are counted); DR.DR against eta^6/4; DR's T law e^(i pi/4)(DR_1, DR_3, -DR_2)
    and M law (conj DR_1, conj DR_2, -conj DR_3); eta^3's T law e^(i pi/4) and M law conj; and, with no singlet, the
    largest change of the observables under A, P, N, T, and under M with J -> -J.
(1) The law. At each point a random complex singlet c_X per sector (seeded) is kept at x and multiplied at the relabelled
    point by a candidate multiplier: T by e^(i pi k/4), k = 0..7; A, P, N by +1 and -1; M by conj(.) times +1, -1, i, -i.
    For each candidate: the largest and the smallest departure over the points, in both readings. Then the whole Higgs:
    a random triplet h (in place of DR) and a random singlet, carried by the law found (T: sigma -> e^(i pi/4) sigma,
    h -> e^(i pi/4)(h_1, h_3, -h_2); A, P, N: unchanged; M: sigma -> -conj sigma, h -> (conj h_1, conj h_2, -conj h_3)).
(2) The singlet candidates' own laws: a0(Lx)/a0(x) for L = A, P, N, T and a0(Mx)/conj a0(x); the same for eta^3.
(3) RI-1 as W183 typed it, at tau = i on W183's census (the SM seat's own_lines over orders 1-12, each line taken as
    min((a, b), (-a, -b) mod 1), 266 lines), without the family's slope, the lines with 3w in the lattice (no identity
    kernel) and the half-period lines (a0 = 0), in the reading "eq". Variants: B (sigma_X = a0(X)), N (sigma_X =
    |DR.DR|^(1/2) a0(X)/|a0(X)|), B_eta (B times e^(i arg eta^3), which carries the T law), even (N's phase from down in
    every sector), and the twelve phases ph k (sigma_up = e^(2 pi i k/12)|DR.DR|^(1/2), sigma_down = sigma_lep = -sigma_up).
    For each variant and for N (the census's other representative), T (the same line at tau = 1 + i, (a, b - a)) and, for
    the phases, M (the mirror line (a, -b) at tau = i, J -> -J): how many lines change by more than 1e-6 and by more than
    1e-2, the largest and the median change; and the largest change of the six on W183's O8 lines (4/9, 1/3), (4/9, 2/3),
    (4/9, 4/9), (4/9, 5/9) under N. No D is computed.
(4) The admissible family, on LINES x TAUS: sigma = i r eta^3/2 (one sigma in every sector, "uni") and eps_X i r eta^3/2
    (eps_up = +1, eps_down = eps_lep = -1, "sgn"), r = 1/2, 1, 2; eps_X i |a0(X)| eta^3/|eta^3| ("sgn |a0|"); controls on
    the real axis, r eta^3/2 ("uni") and eps_X r eta^3/2 ("sgn"), r = 1: the largest change under A, P, N, T, M in both
    readings. det S_X against (1 - r^2) eta^6/4. In the reading "SM", the up sector's singlet over its triplet's root
    (conj eta^3/2) divided by down's singlet over eta^3/2, for "uni" (admissible and control). On the mirror's fixed set
    (b = 0 or 1/2 at Re tau = 0; tau = i and 1.7i): the largest |J| with and without an admissible singlet.

Usage: python3 singlet_law_check.py <main checkout>   (main at eb130f01f)
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
LINES = [(Fr(1, 7), Fr(2, 7)), (Fr(1, 3), Fr(1, 6)), (Fr(3, 8), Fr(1, 8)), (Fr(1, 5), Fr(2, 5)), (Fr(3, 7), Fr(1, 7)),
         (Fr(2, 9), Fr(1, 3)), (Fr(1, 2), Fr(1, 3)), (Fr(1, 9), Fr(4, 9)), (Fr(3, 10), Fr(1, 5)), (Fr(5, 12), Fr(1, 6)),
         (Fr(1, 11), Fr(3, 11)), (Fr(1, 6), Fr(1, 2)), (Fr(0), Fr(1, 5)), (Fr(4, 9), Fr(1, 3))]
TAUS = (complex(0, 1), complex(0.13, 2.2), complex(-0.27, 2.6))
FIXED = [(Fr(1, 7), Fr(0)), (Fr(3, 8), Fr(0)), (Fr(2, 9), Fr(1, 2)), (Fr(1, 5), Fr(1, 2)), (Fr(3, 10), Fr(0)),
         (Fr(1, 11), Fr(1, 2))]
FIXED_TAUS = (complex(0, 1), complex(0, 1.7))
O8 = [(Fr(4, 9), Fr(1, 3)), (Fr(4, 9), Fr(2, 3)), (Fr(4, 9), Fr(4, 9)), (Fr(4, 9), Fr(5, 9))]
TOL, BIG, GAP = 1e-6, 1e-2, 1e-6
ROT_T = lambda v: np.exp(1j * PI / 4) * np.array([v[0], v[2], -v[1]])
CONJ_M = lambda v: np.array([np.conj(v[0]), np.conj(v[1]), -np.conj(v[2])])


def guard(a):
    if Fr(a) % 1 in FAMILY:
        raise SystemExit("refused: the candidate family's slope")


def eta(tau, n=80):
    q = np.exp(2j * PI * tau)
    return np.exp(2j * PI * tau / 24) * np.prod([1 - q ** k for k in range(1, n)])


def e1star(u, tau, n=40):
    """2 pi i Im(u)/Im(tau) + theta_1'(u)/theta_1(u); theta_1's constant factor cancels in the ratio."""
    k = np.arange(-n, n); h = k + 0.5
    e = (-1.0) ** k * np.exp(1j * PI * tau * h * h + 2j * PI * h * u)
    return 2j * PI * u.imag / tau.imag + np.sum(2j * PI * h * e) / np.sum(e)


def frame(a, b, tau):
    """{sector: (M, a0 closed, main's a0_of['1'] or None)}, DR"""
    guard(a)
    L = Z.radii(tau)[0]
    out = {}
    for sn, ql, qr in SECS:
        w = B.line_w(float(a), -float(b), tau); x, y = B.sector_twists(w, tau, ql, qr)
        with contextlib.redirect_stdout(io.StringIO()):
            R = B.residues(x, y, tau); c = B.cA(x, y, tau, R); A0 = B.a0_of(x, y, tau, R)
        u = {k: (math.sqrt(2 * PI * L + c[k]) * R[k] if c[k] is not None and 2 * PI * L + c[k] > 0 else 0) for k in B.UNITS}
        out[sn] = (B.weighted_M(u), e1star((ql + qr) * w, tau), A0["1"])
    with contextlib.redirect_stdout(io.StringIO()):
        DR = np.array(Z.direction("DR", tau))
    return out, DR


def labellings(a, b, tau):
    return {"x": (a, b, tau), "A": (a, b + 1, tau), "P": (a + 1, b, tau), "N": (-a, -b, tau), "T": (a, b - a, tau + 1),
            "M": (a, -b, complex(-tau.real, tau.imag))}


def yuk(F, h, sig, reading):
    S0 = h[0] * B.QI + h[1] * B.QJ + h[2] * B.QK
    Ys = {}
    for sn in SN:
        S = S0 + sig[sn] * np.eye(2)
        if reading == "SM" and sn == "up":
            S = B.EPS @ S.conj() @ B.EPS.T
        Ys[sn] = B.coupling(S, F[sn][0])
    return Ys


def obs(Ys):
    six, U, gap = [], {}, np.inf
    for sn in SN:
        uu, s, _ = np.linalg.svd(Ys[sn]); o = np.argsort(s); sv = s[o] / s.max()
        six += [sv[0], sv[1]]; U[sn] = uu[:, o]
        if sn != "lep":
            gap = min(gap, sv[1] - sv[0], sv[2] - sv[1])
    V = U["up"].conj().T @ U["down"]
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    return np.array(six), np.abs([V[0, 1], V[1, 2], V[0, 2], V[2, 0]]), J, gap > GAP


def change(o0, o1, flipJ=False):
    """(largest change of the six; of |V| and J, or None where a quark spectrum is degenerate)"""
    d6 = float(np.max(np.abs(o1[0] - o0[0])))
    if not (o0[3] and o1[3]):
        return d6, None
    dj = abs(o1[2] + o0[2]) if flipJ else abs(o1[2] - o0[2])
    return d6, float(max(np.max(np.abs(o1[1] - o0[1])), dj))


def worst(c):
    return c[0] if c[1] is None else max(c)


# ---------------------------------------------------------------------------------------------- (0), (1), (2), (4)
def work_a(task):
    a, b, tau, seed = task
    rng = np.random.default_rng(seed)
    L = labellings(a, b, tau)
    D = {k: frame(*v) for k, v in L.items()}
    Fx, DRx = D["x"]
    rec = {"pt": (a, b, tau)}
    # (0)
    rec["a0_main"] = [abs(Fx_[1] - Fx_[2]) / (1 + abs(Fx_[1])) for k in D for Fx_ in D[k][0].values() if Fx_[2] is not None]
    rec["a0_none"] = sum(1 for k in D for Fx_ in D[k][0].values() if Fx_[2] is None)
    e3 = {k: eta(v[2]) ** 3 for k, v in L.items()}
    rec["hh"] = abs(DRx @ DRx - e3["x"] ** 2 / 4) / abs(DRx @ DRx)
    rec["DR_T"] = np.linalg.norm(D["T"][1] - ROT_T(DRx)) / np.linalg.norm(DRx)
    rec["DR_M"] = np.linalg.norm(D["M"][1] - CONJ_M(DRx)) / np.linalg.norm(DRx)
    rec["e3_T"] = abs(e3["T"] - np.exp(1j * PI / 4) * e3["x"]) / abs(e3["x"])
    rec["e3_M"] = abs(e3["M"] - np.conj(e3["x"])) / abs(e3["x"])
    zero = {sn: 0 for sn in SN}
    for rd in ("eq", "SM"):
        o = {k: obs(yuk(D[k][0], D[k][1], zero, rd)) for k in D}
        rec[("none", rd)] = {k: change(o["x"], o[k], k == "M") for k in "APNTM"}
    # (1) the law, random singlets
    nd = np.linalg.norm(DRx)
    c = {sn: complex(*rng.normal(size=2)) * nd for sn in SN}
    for rd in ("eq", "SM"):
        o0 = obs(yuk(Fx, DRx, c, rd)); r = {}
        for k in range(8):
            mu = np.exp(1j * PI * k / 4)
            r["T x e^(i pi %d/4)" % k] = change(o0, obs(yuk(D["T"][0], D["T"][1], {s: mu * c[s] for s in SN}, rd)))
        for lab in "APN":
            for s_ in (1, -1):
                r["%s x %+d" % (lab, s_)] = change(o0, obs(yuk(D[lab][0], D[lab][1], {s: s_ * c[s] for s in SN}, rd)))
        for mu, nm in ((1, "+1"), (-1, "-1"), (1j, "+i"), (-1j, "-i")):
            r["M conj x %s" % nm] = change(o0, obs(yuk(D["M"][0], D["M"][1], {s: mu * np.conj(c[s]) for s in SN}, rd)), True)
        rec[("law", rd)] = r
        # the whole Higgs: a random triplet and a random singlet carried by the law
        h = (rng.normal(size=3) + 1j * rng.normal(size=3)) * nd / math.sqrt(3)
        cc = {sn: complex(*rng.normal(size=2)) * nd for sn in SN}
        o0 = obs(yuk(Fx, h, cc, rd)); g = {}
        g["T"] = change(o0, obs(yuk(D["T"][0], ROT_T(h), {s: np.exp(1j * PI / 4) * cc[s] for s in SN}, rd)))
        for lab in "APN":
            g[lab] = change(o0, obs(yuk(D[lab][0], h, cc, rd)))
        g["M"] = change(o0, obs(yuk(D["M"][0], CONJ_M(h), {s: -np.conj(cc[s]) for s in SN}, rd)), True)
        rec[("whole", rd)] = g
    # (2) the candidates' own laws
    a0 = {k: {sn: D[k][0][sn][1] for sn in SN} for k in D}
    rec["a0_law"] = {k: [a0[k][sn] / (np.conj(a0["x"][sn]) if k == "M" else a0["x"][sn]) for sn in SN if abs(a0["x"][sn]) > 1e-9]
                     for k in "APNTM"}
    rec["e3_law"] = {k: (e3[k] / (np.conj(e3["x"]) if k == "M" else e3["x"])) for k in "APNTM"}
    # (4) the admissible family and controls
    def fam(name, k):
        F_, DR_ = D[k]; E = e3[k]; a0k = a0[k]
        eps = {"up": 1, "down": -1, "lep": -1}
        if name.startswith("uni i r="):
            r_ = float(name.split("=")[1]); return {s: 1j * r_ * E / 2 for s in SN}
        if name.startswith("sgn i r="):
            r_ = float(name.split("=")[1]); return {s: eps[s] * 1j * r_ * E / 2 for s in SN}
        if name == "sgn i |a0|":
            return {s: eps[s] * 1j * abs(a0k[s]) * E / abs(E) for s in SN}
        if name == "uni real r=1":
            return {s: E / 2 for s in SN}
        if name == "sgn real r=1":
            return {s: eps[s] * E / 2 for s in SN}
    names = ["uni i r=0.5", "uni i r=1", "uni i r=2", "sgn i r=0.5", "sgn i r=1", "sgn i r=2", "sgn i |a0|",
             "uni real r=1", "sgn real r=1"]
    for rd in ("eq", "SM"):
        for nm in names:
            o = {k: obs(yuk(D[k][0], D[k][1], fam(nm, k), rd)) for k in D}
            rec[("fam", rd, nm)] = {k: change(o["x"], o[k], k == "M") for k in "APNTM"}
    dets = []
    for r_ in (0.5, 1.0, 2.0):
        S = (1j * r_ * e3["x"] / 2) * np.eye(2) + DRx[0] * B.QI + DRx[1] * B.QJ + DRx[2] * B.QK
        dets.append(abs(np.linalg.det(S) - (1 - r_ ** 2) * e3["x"] ** 2 / 4) / abs(e3["x"] ** 2 / 4))
    rec["det"] = max(dets)
    # the SM reading: up's singlet over conj(eta^3)/2, divided by down's over eta^3/2
    rat = {}
    for nm in ("uni i r=1", "uni real r=1"):
        s_ = fam(nm, "x")
        Sup = B.EPS @ ((s_["up"]) * np.eye(2) + DRx[0] * B.QI + DRx[1] * B.QJ + DRx[2] * B.QK).conj() @ B.EPS.T
        sig_up = (Sup[0, 0] + Sup[1, 1]) / 2
        rat[nm] = (sig_up / (np.conj(e3["x"]) / 2)) / (s_["down"] / (e3["x"] / 2))
    rec["sm_ratio"] = rat
    return rec


def work_fixed(task):
    a, b, tau = task
    F, DR = frame(a, b, tau); E = eta(tau) ** 3
    out = {}
    for rd in ("eq", "SM"):
        for nm, sig in (("none", {s: 0 for s in SN}), ("uni i r=2", {s: 1j * E for s in SN}),
                        ("sgn i r=2", {"up": 1j * E, "down": -1j * E, "lep": -1j * E}),
                        ("uni real r=2", {s: E for s in SN}), ("sgn real r=2", {"up": E, "down": -E, "lep": -E})):
            o = obs(yuk(F, DR, sig, rd))
            out[(rd, nm)] = abs(o[2]) if o[3] else None
    return (a, b, tau), out


# ---------------------------------------------------------------------------------------------- (3)
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


def variants(F, DR, tau, phases=True):
    hh = DR @ DR; nat = math.sqrt(abs(hh)); E = eta(tau) ** 3
    a0 = {s: F[s][1] for s in SN}
    v = {"B": dict(a0), "N": {s: nat * a0[s] / abs(a0[s]) for s in SN},
         "B_eta": {s: a0[s] * E / abs(E) for s in SN},
         "even": {s: nat * a0["down"] / abs(a0["down"]) for s in SN}}
    if phases:
        for k in range(12):
            c = np.exp(2j * PI * k / 12) * nat
            v["ph %d" % k] = {"up": c, "down": -c, "lep": -c}
    return v


def work_c(line):
    a, b = line
    tau = complex(0, 1)
    pts = {"x": (a, b, tau), "N": ((-a) % 1, (-b) % 1, tau), "T": (a, b - a, tau + 1), "M": (a, (-b) % 1, tau)}
    D = {k: frame(*v) for k, v in pts.items()}
    V = {k: variants(D[k][0], D[k][1], pts[k][2]) for k in D}
    res = {}
    for vn in V["x"]:
        o = {k: obs(yuk(D[k][0], D[k][1], V[k][vn], "eq")) for k in D}
        res[vn] = {k: change(o["x"], o[k], k == "M") for k in ("N", "T", "M")}
    return line, res


if __name__ == "__main__":
    tasks = [(a, b, t, 20261104 + 97 * i) for i, ((a, b), t) in enumerate([(l, t) for l in LINES for t in TAUS])]
    census = own_lines(range(1, 13))
    keep = [l for l in census if l[0] % 1 not in FAMILY and not lattice((3 * l[0], 3 * l[1]))
            and not lattice((6 * l[0], 6 * l[1]))]
    with Pool(4) as pool:
        RA = pool.map(work_a, tasks, chunksize=1)
        RF = dict(pool.map(work_fixed, [(a, b, t) for (a, b) in FIXED for t in FIXED_TAUS], chunksize=1))
        RC = dict(pool.map(work_c, keep, chunksize=1))

    print("(0) the instrument (%d points: %d lines x %d tau, each with its five relabellings)" % (len(RA), len(LINES), len(TAUS)))
    am = [v for r in RA for v in r["a0_main"]]
    print("    main's a0_of['1'] against the closed form: largest |difference|/(1 + |a0|) %.1e on %d sector-points; "
          "main's identity residue below its cut on %d sector-points (closed form used there, as W183)"
          % (max(am), len(am), sum(r["a0_none"] for r in RA)))
    print("    DR.DR against eta^6/4: %.1e;  DR's T law %.1e, M law %.1e;  eta^3's T law %.1e, M law %.1e"
          % (max(r["hh"] for r in RA), max(r["DR_T"] for r in RA), max(r["DR_M"] for r in RA),
             max(r["e3_T"] for r in RA), max(r["e3_M"] for r in RA)))
    for rd in ("eq", "SM"):
        print("    no singlet, reading %s: largest change (six; |V| and J, M with J -> -J): %s" % (rd, "  ".join(
            "%s %.1e; %s" % (k, max(r[("none", rd)][k][0] for r in RA),
                             "%.1e" % max((r[("none", rd)][k][1] for r in RA if r[("none", rd)][k][1] is not None), default=float("nan")))
            for k in "APNTM")))
    deg = sum(1 for r in RA for rd in ("eq", "SM") for k in "APNTM" if r[("none", rd)][k][1] is None)
    print("    rows with a degenerate quark spectrum (|V|, J not compared), no singlet: %d of %d" % (deg, len(RA) * 10))

    print("(1) the law: a random singlet at x, multiplied at the relabelled point (largest / smallest departure over %d points)" % len(RA))
    for rd in ("eq", "SM"):
        print("    reading %s" % rd)
        for k in RA[0][("law", rd)]:
            vals = [worst(r[("law", rd)][k]) for r in RA]
            print("        %-22s largest %.1e  smallest %.1e" % (k, max(vals), min(vals)))
        print("        the whole Higgs carried by the law (random triplet and singlet): %s" % "  ".join(
            "%s %.1e" % (k, max(worst(r[("whole", rd)][k]) for r in RA)) for k in "APNTM"))

    print("(2) the candidates' own laws (largest departure from the value shown)")
    for k, want in (("A", 1), ("P", 1), ("N", -1), ("T", 1), ("M", -1)):
        v = [x for r in RA for x in r["a0_law"][k]]
        print("    a0(%sx)/%s = %+d: %.1e" % (k, "conj a0(x)" if k == "M" else "a0(x)", want, max(abs(x - want) for x in v)))
    for k, want in (("A", 1), ("P", 1), ("N", 1), ("T", np.exp(1j * PI / 4)), ("M", 1)):
        v = [r["e3_law"][k] for r in RA]
        print("    eta^3(%sx)/%s = %s: %.1e" % (k, "conj eta^3(x)" if k == "M" else "eta^3(x)",
                                              "e^(i pi/4)" if k == "T" else "1", max(abs(x - want) for x in v)))

    print("(3) RI-1 as W183 typed it, reading eq, at tau = i on W183's census: %d lines; %d kept (the family's slope, 3w in the "
          "lattice and the half-period lines left out)" % (len(census), len(keep)))
    print("    variant  relabelling  changed > 1e-6  > 1e-2  largest  median   (|V| and J compared on n lines)")
    for vn in RC[keep[0]]:
        for k in (("N", "T", "M") if vn.startswith("ph") else ("N", "T")):
            ch = [worst(RC[l][vn][k]) for l in keep]
            nv = sum(1 for l in keep if RC[l][vn][k][1] is not None)
            print("    %-8s %-12s %4d of %d     %4d    %.2e  %.2e  (%d)" % (vn, k, sum(c > TOL for c in ch), len(ch),
                                                                       sum(c > BIG for c in ch), max(ch), float(np.median(ch)), nv))
    print("    W183's O8 lines under N (the census's other representative), B: the six's largest change %s"
          % ", ".join("%s/%s %.2e" % (l[0], l[1], RC[min(l, ((-l[0]) % 1, (-l[1]) % 1))]["B"]["N"][0]) for l in O8))

    print("(4) the admissible family: largest change under each relabelling (M with J -> -J)")
    for rd in ("eq", "SM"):
        print("    reading %s" % rd)
        for nm in [k[2] for k in RA[0] if isinstance(k, tuple) and k[0] == "fam" and k[1] == rd]:
            print("        %-14s %s" % (nm, "  ".join("%s %.1e" % (k, max(worst(r[("fam", rd, nm)][k]) for r in RA)) for k in "APNTM")))
    print("    det S against (1 - r^2) eta^6/4, r = 1/2, 1, 2: %.1e" % max(r["det"] for r in RA))
    for nm in ("uni i r=1", "uni real r=1"):
        v = [r["sm_ratio"][nm] for r in RA]
        print("    reading SM, %s: up's singlet over conj(eta^3)/2, divided by down's over eta^3/2: from %s to %s"
              % (nm, np.round(min(v, key=lambda z: z.real), 12), np.round(max(v, key=lambda z: z.real), 12)))
    print("    the mirror's fixed set (%d points): largest |J| (None where a quark spectrum is degenerate)" % len(RF))
    for key in RF[next(iter(RF))]:
        js = [RF[p][key] for p in RF]
        good = [j for j in js if j is not None]
        print("        %-3s %-13s %s on %d of %d" % (key[0], key[1], "%.1e" % max(good) if good else "-", len(good), len(js)))
