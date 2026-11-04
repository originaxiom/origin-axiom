"""POST HOC (after the density-Higgs note's referee, whose read-only probe P5 tested P-151's tame profile): one charged
density Higgs whose profile in each channel is its own Kronecker kernel (a meromorphic section of the Higgs's bundle
with one simple pole, unique up to scale; P-151, S128/S129), normalised by the frame's small-cut norm
sqrt(2 pi L_max + c_s) (B1654's convention).  Data-free; no measured value; the family's slope refused.  The thresholds
of (b)'s hierarchical fraction (m1/m3 in (1e-12, 0.01), m2/m3 < 0.1 in both quark sectors) are main's filter's, a
disclosed coarse fact of the measured world (B1827; FRAMING_LEDGER section D); they are a read-out, not a test.

The two assignments:
- M3: the field has 6Y = -3 and carries the direction S = DR; its profile in channel s is K_up,s/||K_up,s|| (character
  chi(-3w)K_s).  Up couples to its conjugate (reading S~) and gets exactly the point frame's u_s = R_up,s ||K_up,s||.
  Down and leptons couple to the field (reading S) by the principal value J_X,s = PV int P_X,s K_up,s dA / ||K_up,s||
  (round discs about the puncture).  The reading is (S~, S, S), A05's.
- P3: the mirror.  The field has 6Y = +3 with profile K_down,s/||K_down,s||; down and leptons couple to its conjugate
  (S~) and get R_X,s ||K_down,s||; up couples to the field (S) by PV int P_up,s K_down,s dA / ||K_down,s||.  The reading
  is (S, S~, S~).

(a) The principal value against its closed form.  With K_down,s's character (alpha, beta) and kappa = r - p tau over
    its coset, the double Fourier series gives -Im tau sum_k 1/kappa_k^2, conditionally convergent; summed with r inner
    it is -Im tau sum_{p in alpha + Z} pi^2/sin^2(pi (beta - p tau)).  The round-disc principal value differs from the
    r-inner sum by the constant pi (the G2* correction: K_down K_up is an elliptic function, wp + const, and the
    principal value of wp over the cell carries it).  The constant pi was found by a smoke probe of this script before
    its commit (36 channel-cases, the difference pi to 1e-6 in each).  The closed form tested here:
        PV int K_down,s K_up,s dA = pi - Im tau sum_{p in alpha + Z} pi^2/sin^2(pi (beta - p tau)).
    Polar Gauss-Legendre quadrature (64 x 64 and 96 x 96 nodes per segment; the singular part R/u^2 integrated
    analytically, as the referee's P5 does) against it, per channel, on 20 lines with chi(6w) != 1 at tau = 0.2 + 2.5i
    and 0.45 + 3.1i.
(b) M3 and P3 against the point frame (L_max, (S~, S, S)), on the census lines with chi(6w) != 1, at Re tau = 0.2 and
    0.45 and Im tau = 2, 3, 4, 5, 6: per Re tau and Im tau the median m2/m3 and m1/m3 per sector, the effective
    exponent of the median m2/m3 between consecutive heights, the hierarchical fraction (above), and the within-pair
    weight differences |W_1 - W_i|/|W_1|, |W_j - W_k|/|W_j| (W_s = u_s^2/R_s^2) on M3's principal-value side (down)
    and in the point frame (down).

    python3 kernel_profile_posthoc.py <main checkout>     (main at 88c577896)
"""
import math
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
src = (HERE / "density_higgs_check.py").read_text().split('if __name__ == "__main__":')[0]
exec(compile(src, "density_higgs_check.py", "exec"))

TAU_A = (complex(0.2, 2.5), complex(0.45, 3.1))
RES = (0.2, 0.45)
HTS = (2.0, 3.0, 4.0, 5.0, 6.0)
GL = {64: leggauss(64), 96: leggauss(96)}


def pv(xP, yP, RP, xK, yK, RK, tau, n=64):
    """{s: PV int P(xP, yP)_s K(xK, yK)_s dA}, K_s = P(xK, yK)_s / RK_s; R_P/u^2 integrated analytically"""
    xt, wt = GL[n]; xr, wr = GL[n]
    br = B.vangles(tau); out = {s: 0j for s in CH}
    for t0, t1 in zip(br[:-1], br[1:]):
        th = 0.5 * (t1 - t0) * xt + 0.5 * (t1 + t0); wth = 0.5 * (t1 - t0) * wt
        rm = B.rmax_np(th, tau)
        rr = 0.5 * rm[:, None] * (xr[None, :] + 1); wrr = 0.5 * rm[:, None] * wr[None, :]
        u = rr * np.exp(1j * th)[:, None]
        PP = B.pairs(xP, yP, u, tau); PK = B.pairs(xK, yK, u, tau)
        for s in CH:
            if abs(RK[s]) <= CUT:
                continue
            f = PP[s] * PK[s] / RK[s] - RP[s] / u ** 2
            out[s] += np.sum(wth[:, None] * wrr * f * rr) + RP[s] * np.sum(wth * np.exp(-2j * th) * np.log(rm))
    return out


def closed(alpha, beta, tau, n=12):
    ps = alpha + np.arange(-n, n + 1)
    return PI - tau.imag * complex(np.sum(PI ** 2 / np.sin(PI * (beta - ps * tau)) ** 2))


def norms(d, L):
    c = d["c"]
    return {s: (math.sqrt(2 * PI * L + c[s]) if c[s] is not None and 2 * PI * L + c[s] > 0 else None) for s in CH}


def work_a(task):
    a, b, tau = task
    guard(a)
    D = {sn: sector(a, b, tau, ql, qr) for sn, ql, qr in SECS if sn != "lep"}
    out = []
    for n in (64, 96):
        J = pv(D["down"]["x"], D["down"]["y"], D["down"]["R"], D["up"]["x"], D["up"]["y"], D["up"]["R"], tau, n)
        for s in CH:
            ch = D["down"]["ch"][s]
            if ch is None or abs(D["down"]["R"][s]) <= CUT or abs(D["up"]["R"][s]) <= CUT:
                continue
            cf = closed(ch[0], ch[1], tau)
            val = J[s] / D["down"]["R"][s]
            out.append((n, abs(val - cf) / abs(cf)))
    return out


def work_b(task):
    a, b, tau = task
    guard(a)
    D = {sn: sector(a, b, tau, ql, qr, need_c=(sn != "lep")) for sn, ql, qr in SECS}
    if order2(D["up"]["ch"]):
        return None
    L = Z.radii(tau)[0]; S0, _ = higgs(tau)
    N = {X: norms(D[X], L) for X in ("up", "down")}
    res, W = {}, {}
    # M3
    u = {"up": {s: (N["up"][s] * D["up"]["R"][s] if N["up"][s] and abs(D["up"]["R"][s]) > CUT else 0) for s in CH}}
    for X in ("down", "lep"):
        J = pv(D[X]["x"], D[X]["y"], D[X]["R"], D["up"]["x"], D["up"]["y"], D["up"]["R"], tau)
        u[X] = {s: (J[s] / N["up"][s] if N["up"][s] else 0) for s in CH}
    res["M3 (S~,S,S)"] = spectra({sn: yuk(S0, u[sn], r) for sn, r in zip(SN, (1, 0, 0))})[0]
    W["M3 down"] = {s: (u["down"][s] / D["down"]["R"][s]) ** 2 if abs(D["down"]["R"][s]) > CUT else None for s in CH}
    # P3
    J = pv(D["up"]["x"], D["up"]["y"], D["up"]["R"], D["down"]["x"], D["down"]["y"], D["down"]["R"], tau)
    u = {"up": {s: (J[s] / N["down"][s] if N["down"][s] else 0) for s in CH},
         "down": {s: (N["down"][s] * D["down"]["R"][s] if N["down"][s] and abs(D["down"]["R"][s]) > CUT else 0) for s in CH},
         "lep": {s: (N["down"][s] * D["lep"]["R"][s] if N["down"][s] and abs(D["lep"]["R"][s]) > CUT else 0) for s in CH}}
    res["P3 (S,S~,S~)"] = spectra({sn: yuk(S0, u[sn], r) for sn, r in zip(SN, (0, 1, 1))})[0]
    # the point frame (leptons' kernel is down's: the same summed twist, so the same norms)
    up_ = {s: (N["up"][s] * D["up"]["R"][s] if N["up"][s] and abs(D["up"]["R"][s]) > CUT else 0) for s in CH}
    res["point (S~,S,S)"] = spectra({"up": yuk(S0, up_, 1), "down": yuk(S0, u["down"], 0), "lep": yuk(S0, u["lep"], 0)})[0]
    W["point down"] = {s: (N["down"][s] ** 2 if N["down"][s] else None) for s in CH}
    pair = {}
    for k, Ws in W.items():
        if all(Ws[s] is not None for s in CH) and abs(Ws["1"]) > 0 and abs(Ws["j"]) > 0:
            pair[k] = (abs(Ws["1"] - Ws["i"]) / abs(Ws["1"]), abs(Ws["j"] - Ws["k"]) / abs(Ws["j"]))
    return (a, b, tau), res, pair


if __name__ == "__main__":
    census = own_lines(range(1, 13))
    keep = [l for l in census if l[0] % 1 not in FAMILY]
    gen = [l for l in keep if not ((6 * l[0]).denominator == 1 and (6 * l[1]).denominator == 1)]
    with Pool(4) as pool:
        RA = pool.map(work_a, [(a, b, t) for (a, b) in gen[3::11][:20] for t in TAU_A], chunksize=1)
        RB = pool.map(work_b, [(a, b, complex(x, y)) for (a, b) in gen for x in RES for y in HTS], chunksize=2)

    ra = [v for r in RA for v in r]
    print("POST HOC (a): PV int K_down,s K_up,s dA against pi - Im tau sum_p pi^2/sin^2(pi(beta - p tau)), %d lines x %d tau" % (len(RA) // len(TAU_A), len(TAU_A)))
    for n in (64, 96):
        v = [e for m, e in ra if m == n]
        print("    %d x %d nodes per segment: %d channel-cases; largest relative difference %.1e, median %.1e" % (n, n, len(v), max(v), float(np.median(v))))

    rb = [r for r in RB if r is not None]
    print("POST HOC (b): %d points (%d lines with chi(6w) != 1 x %d Re tau x %d Im tau)" % (len(rb), len(gen), len(RES), len(HTS)))
    frames = ["M3 (S~,S,S)", "P3 (S,S~,S~)", "point (S~,S,S)"]
    for x in RES:
        print("  Re tau %.2f" % x)
        for fr in frames:
            med = {}
            for y in HTS:
                rows = [r[1][fr] for r in rb if abs(r[0][2].real - x) < 1e-9 and abs(r[0][2].imag - y) < 1e-9]
                m = {sn: (float(np.median([q[sn][1] for q in rows])), float(np.median([q[sn][0] for q in rows]))) for sn in SN}
                hb = sum(1 for q in rows if all(q[sn][1] < 0.1 and 1e-12 < q[sn][0] < 0.01 for sn in ("up", "down"))) / len(rows)
                med[y] = m
                print("    %-15s Im tau %.0f: median m2/m3 up %.3g, down %.3g, leptons %.3g; median m1/m3 up %.2g, down %.2g, leptons %.2g; "
                      "hierarchical fraction %.3f" % (fr, y, m["up"][0], m["down"][0], m["lep"][0], m["up"][1], m["down"][1], m["lep"][1], hb))
            print("    %-15s effective exponent of the median m2/m3: %s" % (fr, "; ".join(
                "%.0f-%.0f up %.3f, down %.3f, leptons %.3f" % (y0, y1, *[-(math.log(med[y1][sn][0]) - math.log(med[y0][sn][0])) / (2 * PI * (y1 - y0)) for sn in SN])
                for y0, y1 in zip(HTS[:-1], HTS[1:]))))
        for k in ("M3 down", "point down"):
            print("    within-pair weight differences, %-10s: %s" % (k, "; ".join(
                "Im %.0f: |W1 - Wi|/|W1| %.3g, |Wj - Wk|/|Wj| %.3g" % (y, float(np.median([r[2][k][0] for r in rb if k in r[2] and abs(r[0][2].real - x) < 1e-9 and abs(r[0][2].imag - y) < 1e-9])),
                                                                    float(np.median([r[2][k][1] for r in rb if k in r[2] and abs(r[0][2].real - x) < 1e-9 and abs(r[0][2].imag - y) < 1e-9])))
                for y in HTS)))
