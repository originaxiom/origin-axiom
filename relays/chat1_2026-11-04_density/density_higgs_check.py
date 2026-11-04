"""The web seat's check for its note on the density-type Higgs (data-free; no measured value is read; nothing is computed
on the candidate family's slope, a = 2/5 or 3/5; no D, no theta-bar, no inter-sector value, no comparison with any
coarse fact of nature).

The design.  A Higgs of charge q (6Y units) is a density on the fibre E_tau whose channel components carry the inverse
of the matter pairing's characters; sector X couples by Y_{X,s} = int_E P_{X,s}(u) psi_s(u) dA (B1651's Szego addendum:
"a density-type Higgs couples by int v(z) phi(z)").  The integrand must be periodic, so the profile psi_s must carry the
inverse of P_{X,s}'s character.  The ground-state profile of a channel is the plane wave of smallest |kappa| in that
coset; for a plane wave e_{p,r}(u) = exp(2 pi i (p x + r y)), u = x + y tau, with the multipliers of P_{X,s}:
    int_E P_{X,s}(u) conj(e_{p,r}(u)) dA = -R_{X,s} Im(tau) / kappa,   kappa = r - p tau
(integration by parts against dbar(1/u) = pi delta; P's only pole in the cell is the simple one at u = 0, residue R).

Notation: a line is (a, b), w = a tau + b (main's B.line_w(a, -b, tau)); the frame is B1656's as B1821's module builds it,
at main 88c577896; channels 1, i, j, k; the Higgs direction DR; readings written (up, down, leptons).

(0) The instrument: the point frame rebuilt here (u_s = sqrt(2 pi L_max + c_s) R_s, as cm_zero_line) against
    cm_zero_line.rows_at for DR, L_max, reading S~SS, at two (line, tau); DR.DR against eta^6/4.
(1) The characters: on W183's census (orders 1-12, the family's slope refused) at tau = 0.2 + 2.5i and 0.45 + 3.1i, per
    sector and channel, the multipliers m1 = P(u + 1)/P(u), m2 = P(u + tau)/P(u) at four points: constancy and unit
    modulus; (alpha, beta) = arg/(2 pi) mod 1; the channels' shifts against channel 1; up's character times down's
    (expected trivial), leptons' against down's (expected equal); the lines where up's characters all have order <= 2
    (chi(6w) = 1), where a Higgs of charge +3 and its conjugate carry the same characters and charge selection fails.
(2) The closed form: by polar Gauss-Legendre quadrature over the cell centred at the pole (the frame's own vangles and
    rmax_np), int P_s conj(e_k) dA against -R_s Im tau/kappa_k for the three smallest |kappa| in each channel's coset,
    on 30 census lines at the two tau of (1).
(3) The ground state: per channel, |kappa_2|/|kappa_1| - 1 (0 = a tied ground state, the profile not fixed), on the
    census at the two tau, split by chi(6w) = 1 or not; a trivial character (kappa = 0 in the coset: the constant mode,
    no pole allowed) is counted apart and given weight 0.
(4) The density frame against the point frame, on the census lines with chi(6w) != 1 at Re tau = 0.2, Im tau = 2.0, 2.5,
    3.0, 3.5, 4.0, 5.0, 6.0 (the point frame's L_max is B1667's column, held at its last value above it, as np.interp
    does): the density weights w_s = -Im tau/kappa_min,s (u_s = w_s R_s) with the readings (S, S~, S~) (S the flavour
    part of the +3 field) and (S~, S, S); the point frame with (S~, S, S) (A05).  Per Im tau: the median m2/m3 and m1/m3
    per sector; the fraction of points hierarchical in both quark sectors (main's thresholds m1/m3 < 0.01,
    m2/m3 < 0.1); the within-pair weight differences |W_1 - W_i|/|W_1| and |W_j - W_k|/|W_j| (W_s = w_s^2 for the
    density, 2 pi L + c_s for the point frame); and the effective exponent of the median m2/m3,
    -d ln(median)/d(2 pi Im tau), between consecutive heights.
(5) The density frame's covariance under the record's relabellings A (a, b + 1, tau), P (a + 1, b, tau), N (-a, -b, tau),
    T (a, b - a, tau + 1), M (a, -b, -conj tau) with J -> -J: the largest change of the six, |V| and J, both readings,
    on 10 lines with chi(6w) != 1 (where the ground state is not tied) at the two tau of (1).

Usage: python3 density_higgs_check.py <main checkout>   (main at 88c577896)
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
from numpy.polynomial.legendre import leggauss

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
CH = ("1", "i", "j", "k")
FAMILY = (Fr(2, 5), Fr(3, 5))
TAU_C = (complex(0.2, 2.5), complex(0.45, 3.1))
IMS = (2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0)
TAU_B = tuple(complex(0.2, y) for y in IMS)
CUT = 1e-12
SAMPLE = np.array([0.11 + 0.07j, -0.19 + 0.13j, 0.07 - 0.21j, 0.23 + 0.31j])
GLT = leggauss(48)
GLR = leggauss(48)
READ = {"S,S~,S~": (0, 1, 1), "S~,S,S": (1, 0, 0)}


def guard(a):
    if Fr(a) % 1 in FAMILY:
        raise SystemExit("refused: the candidate family's slope")


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


def eta(tau, n=80):
    q = np.exp(2j * PI * tau)
    return np.exp(2j * PI * tau / 24) * np.prod([1 - q ** k for k in range(1, n)])


def twists(a, b, tau, ql, qr):
    w = B.line_w(float(a), -float(b), tau)
    return B.sector_twists(w, tau, ql, qr)


def characters(x, y, tau):
    """{channel: (alpha, beta, spread, unit) or None where the channel's pairing vanishes at every sample point}"""
    P0 = B.pairs(x, y, SAMPLE, tau); P1 = B.pairs(x, y, SAMPLE + 1, tau); P2 = B.pairs(x, y, SAMPLE + tau, tau)
    scale = max(float(np.max(np.abs(P0[s]))) for s in CH)
    out = {}
    for s in CH:
        ok = np.abs(P0[s]) > 1e-9 * scale
        if not ok.any():
            out[s] = None
            continue
        m1 = P1[s][ok] / P0[s][ok]; m2 = P2[s][ok] / P0[s][ok]
        spread = float(max(np.max(np.abs(m1 - m1.mean())), np.max(np.abs(m2 - m2.mean()))))
        unit = float(max(np.max(np.abs(np.abs(m1) - 1)), np.max(np.abs(np.abs(m2) - 1))))
        out[s] = ((np.angle(m1.mean()) / (2 * PI)) % 1, (np.angle(m2.mean()) / (2 * PI)) % 1, spread, unit)
    return out


def d01(v):
    v = v % 1
    return min(v, 1 - v)


def half(v):
    return d01(2 * v) < 1e-7


def kappas(alpha, beta, tau, n=6):
    ps = alpha + np.arange(-n, n + 1); rs = beta + np.arange(-n, n + 1)
    P, R = np.meshgrid(ps, rs, indexing="ij")
    K = (R - P * tau).ravel(); o = np.argsort(np.abs(K))
    return K[o], P.ravel()[o], R.ravel()[o]


def order2(ch):
    """every non-vanishing channel's character has order <= 2 (2 alpha, 2 beta integers)"""
    live = [s for s in CH if ch[s] is not None]
    return bool(live) and all(half(ch[s][0]) and half(ch[s][1]) for s in live)


def sector(a, b, tau, ql, qr, need_c=False):
    x, y = twists(a, b, tau, ql, qr)
    with contextlib.redirect_stdout(io.StringIO()):
        R = B.residues(x, y, tau)
        c = B.cA(x, y, tau, R) if need_c else None
    ch = characters(x, y, tau)
    w = {}; tie = {}
    for s in CH:
        if ch[s] is None:
            w[s] = 0; tie[s] = None
            continue
        K, _, _ = kappas(ch[s][0], ch[s][1], tau)
        if abs(K[0]) < 1e-12:
            w[s] = 0; tie[s] = "trivial"
            continue
        w[s] = -tau.imag / K[0]; tie[s] = abs(K[1]) / abs(K[0]) - 1
    return dict(x=x, y=y, R=R, c=c, ch=ch, w=w, tie=tie)


def higgs(tau):
    with contextlib.redirect_stdout(io.StringIO()):
        a = Z.direction("DR", tau)
    return a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK, np.array(a)


def yuk(S0, u, conj):
    S = B.EPS @ S0.conj() @ B.EPS.T if conj else S0
    return B.coupling(S, B.weighted_M(u))


def u_density(d):
    return {s: (d["w"][s] * d["R"][s] if abs(d["R"][s]) > CUT else 0) for s in CH}


def u_point(d, L):
    c = d["c"]
    return {s: (math.sqrt(2 * PI * L + c[s]) * d["R"][s] if c[s] is not None and 2 * PI * L + c[s] > 0 else 0) for s in CH}


def spectra(Ys):
    out, U = {}, {}
    for sn in SN:
        uu, s, _ = np.linalg.svd(Ys[sn]); o = np.argsort(s); s = s[o]; U[sn] = uu[:, o]
        out[sn] = (float(s[0] / s[2]), float(s[1] / s[2]), float(min(s[1] - s[0], s[2] - s[1]) / s[2]))
    V = U["up"].conj().T @ U["down"]
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    return out, np.abs([V[0, 1], V[1, 2], V[0, 2], V[2, 0]]), J


# ---------------------------------------------------------------------------------------------- (1), (3)
def work_chars(task):
    a, b, tau = task
    guard(a)
    D = {sn: sector(a, b, tau, ql, qr) for sn, ql, qr in SECS}
    return (a, b, tau), {sn: (D[sn]["ch"], D[sn]["tie"]) for sn in SN}


# ---------------------------------------------------------------------------------------------- (2)
def work_fourier(task):
    a, b, tau = task
    guard(a)
    out = []
    br = B.vangles(tau)
    xt, wt = GLT; xr, wr = GLR
    for sn, ql, qr in SECS:
        x, y = twists(a, b, tau, ql, qr)
        with contextlib.redirect_stdout(io.StringIO()):
            R = B.residues(x, y, tau)
        ch = characters(x, y, tau)
        live = [s for s in CH if ch[s] is not None and abs(R[s]) > CUT]
        ks = {s: kappas(ch[s][0], ch[s][1], tau) for s in live}
        live = [s for s in live if abs(ks[s][0][0]) > 1e-12]
        acc = {s: np.zeros(3, complex) for s in live}
        for t0, t1 in zip(br[:-1], br[1:]):
            th = 0.5 * (t1 - t0) * xt + 0.5 * (t1 + t0); wth = 0.5 * (t1 - t0) * wt
            rm = B.rmax_np(th, tau)
            rr = 0.5 * rm[:, None] * (xr[None, :] + 1); wrr = 0.5 * rm[:, None] * wr[None, :]
            u = rr * np.exp(1j * th)[:, None]
            P = B.pairs(x, y, u, tau)
            yy = u.imag / tau.imag; xx = u.real - yy * tau.real
            for s in live:
                K, Pp, Rr = ks[s]
                for j in range(3):
                    eb = np.exp(-2j * PI * (Pp[j] * xx + Rr[j] * yy))
                    acc[s][j] += np.sum(wth[:, None] * wrr * P[s] * eb * rr)
        for s in live:
            K = ks[s][0]
            for j in range(3):
                pred = -R[s] * tau.imag / K[j]
                out.append(abs(acc[s][j] - pred) / abs(pred))
    return out


# ---------------------------------------------------------------------------------------------- (4)
def work_band(task):
    a, b, tau = task
    guard(a)
    D = {sn: sector(a, b, tau, ql, qr, need_c=True) for sn, ql, qr in SECS}
    if order2(D["up"]["ch"]):
        return None
    L = Z.radii(tau)[0]
    S0, _ = higgs(tau)
    res = {}
    for nm, rd in READ.items():
        Ys = {sn: yuk(S0, u_density(D[sn]), r) for sn, r in zip(SN, rd)}
        res["density " + nm] = spectra(Ys)[0]
    Ys = {sn: yuk(S0, u_point(D[sn], L), r) for sn, r in zip(SN, (1, 0, 0))}
    res["point S~,S,S"] = spectra(Ys)[0]
    pair = {}
    for sn in SN:
        Wd = {s: D[sn]["w"][s] ** 2 for s in CH}
        c = D[sn]["c"]
        if all(c[s] is not None for s in CH):
            Wp = {s: 2 * PI * L + c[s] for s in CH}
            pair[sn] = (abs(Wd["1"] - Wd["i"]) / abs(Wd["1"]), abs(Wd["j"] - Wd["k"]) / abs(Wd["j"]),
                        abs(Wp["1"] - Wp["i"]) / abs(Wp["1"]), abs(Wp["j"] - Wp["k"]) / abs(Wp["j"]))
    return (a, b, tau), res, pair


# ---------------------------------------------------------------------------------------------- (5)
def work_cov(task):
    a, b, tau = task
    guard(a)
    pts = {"x": (a, b, tau), "A": (a, b + 1, tau), "P": (a + 1, b, tau), "N": (-a, -b, tau), "T": (a, b - a, tau + 1),
           "M": (a, -b, complex(-tau.real, tau.imag))}
    obs = {}
    for k, (aa, bb, tt) in pts.items():
        D = {sn: sector(aa, bb, tt, ql, qr) for sn, ql, qr in SECS}
        S0, _ = higgs(tt)
        obs[k] = {nm: spectra({sn: yuk(S0, u_density(D[sn]), r) for sn, r in zip(SN, rd)}) for nm, rd in READ.items()}
    out = {}
    for nm in READ:
        o0 = obs["x"][nm]
        for k in "APNTM":
            o1 = obs[k][nm]
            six = max(abs(o1[0][sn][i] - o0[0][sn][i]) for sn in SN for i in (0, 1))
            deg = min(o0[0]["up"][2], o0[0]["down"][2], o1[0]["up"][2], o1[0]["down"][2]) < 1e-6
            vj = None if deg else max(float(np.max(np.abs(o1[1] - o0[1]))), abs(o1[2] + o0[2]) if k == "M" else abs(o1[2] - o0[2]))
            out[(nm, k)] = (six, vj)
    return out


def instrument():
    out = []
    for (a, b), tau in (((Fr(1, 7), Fr(2, 7)), complex(0.2, 2.5)), ((Fr(3, 8), Fr(1, 8)), complex(0.45, 3.1))):
        with contextlib.redirect_stdout(io.StringIO()):
            rows = Z.rows_at(tau, (float(a), -float(b)))
        ref = next(r for r in rows if r["direction"] == "DR" and r["radius"] == "L_max" and r["reading"] == "S~SS")
        D = {sn: sector(a, b, tau, ql, qr, need_c=True) for sn, ql, qr in SECS}
        L = Z.radii(tau)[0]; S0, h = higgs(tau)
        sp = spectra({sn: yuk(S0, u_point(D[sn], L), r) for sn, r in zip(SN, (1, 0, 0))})[0]
        dev = max(abs(sp[sn][i] - ref[key][i]) / abs(ref[key][i]) for sn, key in zip(SN, ("up", "down", "lepton")) for i in (0, 1))
        hh = abs(h @ h - eta(tau) ** 6 / 4) / abs(h @ h)
        out.append(((a, b, tau), dev, hh))
    return out


if __name__ == "__main__":
    census = own_lines(range(1, 13))
    keep = [l for l in census if l[0] % 1 not in FAMILY]
    with Pool(4) as pool:
        RC = pool.map(work_chars, [(a, b, t) for (a, b) in keep for t in TAU_C], chunksize=4)
        o2set = {(pt[0], pt[1]) for pt, r in RC if order2(r["up"][0])}
        generic = [l for l in keep if l not in o2set]
        RF = pool.map(work_fourier, [(a, b, t) for (a, b) in keep[::8][:30] for t in TAU_C], chunksize=1)
        RB = pool.map(work_band, [(a, b, t) for (a, b) in keep for t in TAU_B], chunksize=2)
        RV = pool.map(work_cov, [(a, b, t) for (a, b) in generic[5::23][:10] for t in TAU_C], chunksize=1)

    print("(0) the instrument")
    for pt, dev, hh in instrument():
        print("    %s at tau %s: the point frame rebuilt against rows_at (DR, L_max, S~SS): largest relative difference %.1e; "
              "DR.DR against eta^6/4: %.1e" % ((str(pt[0]), str(pt[1])), pt[2], dev, hh))

    print("(1) the characters: %d census lines (of %d; the family's slope refused) x %d tau" % (len(keep), len(census), len(TAU_C)))
    live = [(r[sn][0][s]) for _, r in RC for sn in SN for s in CH if r[sn][0][s] is not None]
    nnone = sum(1 for _, r in RC for sn in SN for s in CH if r[sn][0][s] is None)
    print("    multipliers: largest spread over the four sample points %.1e; largest ||m| - 1| %.1e; channel-points whose "
          "pairing vanishes at every sample point: %d" % (max(v[2] for v in live), max(v[3] for v in live), nnone))
    shifts = {}
    for _, r in RC:
        for sn in SN:
            ch = r[sn][0]
            if ch["1"] is None:
                continue
            for s in CH[1:]:
                if ch[s] is None:
                    continue
                da, db = (ch[s][0] - ch["1"][0]) % 1, (ch[s][1] - ch["1"][1]) % 1
                d = ((round(2 * da) / 2) % 1, (round(2 * db) / 2) % 1)
                err = max(d01(da - d[0]), d01(db - d[1]))
                shifts.setdefault(s, {}).setdefault(d, [0, 0.0])
                shifts[s][d][0] += 1; shifts[s][d][1] = max(shifts[s][d][1], err)
    for s in CH[1:]:
        print("    channel %s against channel 1, (alpha, beta) shift: %s" % (s, "; ".join("%s on %d (largest off %.1e)" % (d, n, e) for d, (n, e) in sorted(shifts[s].items()))))
    pairs_ud = [(r["up"][0][s], r["down"][0][s], r["lep"][0][s]) for _, r in RC for s in CH
                if r["up"][0][s] is not None and r["down"][0][s] is not None and r["lep"][0][s] is not None]
    inv = max(d01(u[i] + d[i]) for u, d, _ in pairs_ud for i in (0, 1))
    eq = max(d01(l[i] - d[i]) for _, d, l in pairs_ud for i in (0, 1))
    print("    up's character times down's, distance from trivial: largest %.1e;  leptons' against down's: largest %.1e (%d channel-points)"
          % (inv, eq, len(pairs_ud)))
    o2 = sorted({(pt[0], pt[1]) for pt, r in RC if order2(r["up"][0])})
    print("    lines where up's four characters all have order <= 2 (chi(6w) = 1; charge selection fails): %d: %s"
          % (len(o2), ", ".join("(%s, %s)" % l for l in o2)))
    o2tau = {}
    for pt, r in RC:
        o2tau.setdefault((pt[0], pt[1]), set()).add(order2(r["up"][0]))
    print("    the order-2 lines are the same at both tau: %s" % all(len(v) == 1 for v in o2tau.values()))

    rf = [v for r in RF for v in r]
    print("(2) the closed form int P_s conj(e_k) dA = -R_s Im tau/kappa_k: %d (line, tau, sector, channel, k) cases on %d lines x %d tau; "
          "largest relative difference %.1e, median %.1e" % (len(rf), len(RF) // len(TAU_C), len(TAU_C), max(rf), float(np.median(rf))))

    ties_o2, ties_g, triv = [], [], {True: 0, False: 0}
    for pt, r in RC:
        o = order2(r["up"][0])
        for sn in SN:
            for s in CH:
                t = r[sn][1][s]
                if t == "trivial":
                    triv[o] += 1
                elif t is not None:
                    (ties_o2 if o else ties_g).append(t)
    print("(3) the ground state: |kappa_2|/|kappa_1| - 1 per channel (a trivial character, kappa = 0 in the coset, counted apart)")
    print("    on the chi(6w) = 1 lines: %d channel-points, tied (< 1e-9) %d, largest gap %.2g; trivial characters %d"
          % (len(ties_o2), sum(t < 1e-9 for t in ties_o2), max(ties_o2), triv[True]))
    print("    on the other lines: %d channel-points, tied (< 1e-9) %d; smallest gap %.2g, median %.3g; trivial characters %d"
          % (len(ties_g), sum(t < 1e-9 for t in ties_g), min(ties_g), float(np.median(ties_g)), triv[False]))

    rb = [r for r in RB if r is not None]
    print("(4) the density frame against the point frame: %d points (%d lines with chi(6w) != 1 x %d Im tau at Re tau 0.2)"
          % (len(rb), len(rb) // len(IMS), len(IMS)))
    frames = ["density S,S~,S~", "density S~,S,S", "point S~,S,S"]
    med = {}
    for fr in frames:
        for y in IMS:
            rows = [r[1][fr] for r in rb if abs(r[0][2].imag - y) < 1e-9]
            m = {sn: (float(np.median([x[sn][1] for x in rows])), float(np.median([x[sn][0] for x in rows]))) for sn in SN}
            hb = sum(1 for x in rows if all(x[sn][1] < 0.1 and 1e-12 < x[sn][0] < 0.01 for sn in ("up", "down"))) / len(rows)
            med[(fr, y)] = m
            print("    %-16s Im tau %.1f: median m2/m3 up %.3g, down %.3g, leptons %.3g; median m1/m3 up %.3g, down %.3g, leptons %.3g; "
                  "hierarchical in both quark sectors %.3f" % (fr, y, m["up"][0], m["down"][0], m["lep"][0], m["up"][1], m["down"][1], m["lep"][1], hb))
    for fr in frames:
        for y0, y1 in zip(IMS[:-1], IMS[1:]):
            ex = {sn: -(math.log(med[(fr, y1)][sn][0]) - math.log(med[(fr, y0)][sn][0])) / (2 * PI * (y1 - y0)) for sn in SN}
            print("    %-16s the median m2/m3's effective exponent between Im tau %.1f and %.1f: up %.3f, down %.3f, leptons %.3f"
                  % (fr, y0, y1, ex["up"], ex["down"], ex["lep"]))
    for y in IMS:
        pr = [p for r in rb if abs(r[0][2].imag - y) < 1e-9 for p in r[2].values()]
        print("    within-pair weight differences at Im tau %.1f (median over %d sector-points): density |W1 - Wi|/|W1| %.3g, |Wj - Wk|/|Wj| %.3g; "
              "point |W1 - Wi|/|W1| %.3g, |Wj - Wk|/|Wj| %.3g" % (y, len(pr), float(np.median([p[0] for p in pr])), float(np.median([p[1] for p in pr])),
                                                                 float(np.median([p[2] for p in pr])), float(np.median([p[3] for p in pr]))))

    print("(5) the density frame's covariance (largest change: the six; |V| and J, M with J -> -J), %d points" % len(RV))
    for nm in READ:
        print("    %-9s %s" % (nm, "  ".join("%s %.1e; %s" % (k, max(r[(nm, k)][0] for r in RV),
                                                         ("%.1e" % max(r[(nm, k)][1] for r in RV if r[(nm, k)][1] is not None))
                                                         if any(r[(nm, k)][1] is not None for r in RV) else "-") for k in "APNTM")))
