"""POST HOC 2 (after the density note's second referee, whose read-only probe changed the principal value's constant):
how much the tame-profile frames M3 and P3 (kernel_profile_posthoc.py) lean on A07, the small-cut convention.
Data-free; no measured value; no threshold of nature; the family's slope refused; within-sector values only.

The principal value on the principal-value side (down and leptons in M3, up in P3) is, per channel (the note's § 2),
    PV(eps) = int_{cell minus the round disc of radius eps} K_down,s K_up,s dA = pi - Im tau S_s - C_s pi eps^2,
with S_s = sum_{p in alpha + Z} pi^2/sin^2(pi(beta - p tau)) ((alpha, beta) down's character in channel s) and
C_s = G2(tau) - S_s = -wp(v_s), the product's constant term.  The eps^2 term is exact for a round disc on which the
Laurent series of wp converges: every other term of wp(u) - wp(v) - 1/u^2 integrates to zero over the circle.  A07's
small-cut form drops it (eps -> 0), which is what f271abe66 computed by quadrature.

The variants (the norms stay in A07's small-cut form sqrt(2 pi L_max + c_s) throughout; their own eps^2 correction is
the first term of a series that is not small at the frame's radius, so no consistent eps^2 convention is attempted):
- "A07": eps -> 0 (constant pi), the control; at Im tau 2-6 it must reproduce f271abe66's M3 and P3 medians;
- "half": eps = exp(-L_max)/2, a disc inside the cell;
- "frame": eps = exp(-L_max), the frame's own radius; that disc slightly exceeds the cell, as in A07's own form;
- "c=0": the constant pi removed (PV - pi = -Im tau S_s, the r-inner summation of the double series).
M3 (field at -3, reading (S~,S,S)): up = the point frame's weights; down and leptons R_X,s PV/||K_up,s||.
P3 (field at +3, reading (S,S~,S~)): down and leptons = the point frame's weights; up R_up,s PV/||K_down,s||.
The point frame (L_max, (S~,S,S)) alongside.  Grid: the census lines with chi(6w) != 1, Re tau = 0.2,
Im tau = 2, 3, 4, 5, 6, 7, 8.  Printed per variant: the median constant |PV(eps)| over channel-points, the median
m2/m3 and m1/m3 per sector, the effective exponent of the median m2/m3 between consecutive heights, and the median
within-pair differences |W_1 - W_i|/|W_1|, |W_j - W_k|/|W_j| (W_s = u_s^2/R_s^2) on M3's principal-value side (down).

    python3 cut_sensitivity_posthoc.py <main checkout>     (main at 88c577896)
"""
import math
import pathlib
import sys

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
src = (HERE / "density_higgs_check.py").read_text().split('if __name__ == "__main__":')[0]
exec(compile(src, "density_higgs_check.py", "exec"))

HTS = (2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0)
RE = 0.2
VARIANTS = ("A07", "half", "frame", "c=0")
FRAMES = ["M3 (S~,S,S)", "P3 (S,S~,S~)"]


def g2(tau, n=60):
    q = np.exp(2j * PI * tau)
    s = sum(sum(d for d in range(1, k + 1) if k % d == 0) * q ** k for k in range(1, n))
    return PI ** 2 / 3 * (1 - 24 * s)


def ssum(alpha, beta, tau, n=8):
    ps = alpha + np.arange(-n, n + 1)
    return complex(np.sum(PI ** 2 / np.sin(PI * (beta - ps * tau)) ** 2))


def pv(alpha, beta, tau, L, variant):
    S = ssum(alpha, beta, tau)
    base = PI - tau.imag * S
    if variant == "A07":
        return base
    if variant == "c=0":
        return base - PI
    eps = math.exp(-L) / (2 if variant == "half" else 1)
    return base - (g2(tau) - S) * PI * eps ** 2


def norms(d, L):
    c = d["c"]
    return {s: (math.sqrt(2 * PI * L + c[s]) if c[s] is not None and 2 * PI * L + c[s] > 0 else None) for s in CH}


def work(task):
    a, b, tau = task
    guard(a)
    D = {sn: sector(a, b, tau, ql, qr, need_c=(sn != "lep")) for sn, ql, qr in SECS}
    if order2(D["up"]["ch"]):
        return None
    L = Z.radii(tau)[0]; S0, _ = higgs(tau)
    N = {X: norms(D[X], L) for X in ("up", "down")}
    ch = D["down"]["ch"]
    point = {X: {s: (N[Y][s] * D[X]["R"][s] if N[Y][s] and abs(D[X]["R"][s]) > CUT else 0) for s in CH}
             for X, Y in (("up", "up"), ("down", "down"), ("lep", "down"))}
    res = {"point (S~,S,S)": spectra({sn: yuk(S0, point[sn], r) for sn, r in zip(SN, (1, 0, 0))})[0]}
    consts, pair = {}, {}
    for v in VARIANTS:
        P = {s: (pv(ch[s][0], ch[s][1], tau, L, v) if ch[s] is not None else 0) for s in CH}
        consts[v] = [abs(P[s]) for s in CH if ch[s] is not None]
        live = {s: abs(D["up"]["R"][s]) > CUT and abs(D["down"]["R"][s]) > CUT for s in CH}
        u = {"up": point["up"]}
        for X in ("down", "lep"):
            u[X] = {s: (D[X]["R"][s] * P[s] / N["up"][s] if N["up"][s] and live[s] and abs(D[X]["R"][s]) > CUT else 0) for s in CH}
        res[(v, "M3 (S~,S,S)")] = spectra({sn: yuk(S0, u[sn], r) for sn, r in zip(SN, (1, 0, 0))})[0]
        W = {s: ((u["down"][s] / D["down"]["R"][s]) ** 2 if abs(D["down"]["R"][s]) > CUT else None) for s in CH}
        if all(W[s] is not None for s in CH) and abs(W["1"]) > 0 and abs(W["j"]) > 0:
            pair[v] = (abs(W["1"] - W["i"]) / abs(W["1"]), abs(W["j"] - W["k"]) / abs(W["j"]))
        u = {"down": point["down"], "lep": point["lep"],
             "up": {s: (D["up"]["R"][s] * P[s] / N["down"][s] if N["down"][s] and live[s] else 0) for s in CH}}
        res[(v, "P3 (S,S~,S~)")] = spectra({sn: yuk(S0, u[sn], r) for sn, r in zip(SN, (0, 1, 1))})[0]
    Wp = {s: (N["down"][s] ** 2 if N["down"][s] else None) for s in CH}
    if all(Wp[s] is not None for s in CH):
        pair["point"] = (abs(Wp["1"] - Wp["i"]) / abs(Wp["1"]), abs(Wp["j"] - Wp["k"]) / abs(Wp["j"]))
    return (a, b, tau), res, consts, pair


def med(rows, key, sn, i):
    return float(np.median([r[1][key][sn][i] for r in rows]))


if __name__ == "__main__":
    census = own_lines(range(1, 13))
    keep = [l for l in census if l[0] % 1 not in FAMILY]
    gen = [l for l in keep if not ((6 * l[0]).denominator == 1 and (6 * l[1]).denominator == 1)]
    with Pool(4) as pool:
        RB = pool.map(work, [(a, b, complex(RE, y)) for (a, b) in gen for y in HTS], chunksize=2)
    rb = [r for r in RB if r is not None]
    print("POST HOC 2: %d points (%d lines with chi(6w) != 1 x Im tau %s at Re tau %.2f)" % (len(rb), len(gen), HTS, RE))
    at = {y: [r for r in rb if abs(r[0][2].imag - y) < 1e-9] for y in HTS}
    keys = [("point (S~,S,S)", "point")] + [((v, f), "%s %s" % (v, f.split()[0])) for v in VARIANTS for f in FRAMES]
    for v in VARIANTS:
        print("  constant |PV(eps)|, %-6s median over channel-points: %s" % (v, "; ".join(
            "Im %.0f %.3g" % (y, float(np.median([c for r in at[y] for c in r[2][v]]))) for y in HTS)))
    for key, name in keys:
        m = {y: {sn: (med(at[y], key, sn, 1), med(at[y], key, sn, 0)) for sn in SN} for y in HTS}
        print("  %-9s median m2/m3 up/down/leptons: %s" % (name, "; ".join(
            "Im %.0f %.3g/%.3g/%.3g" % (y, m[y]["up"][0], m[y]["down"][0], m[y]["lep"][0]) for y in HTS)))
        print("  %-9s median m1/m3 up/down/leptons: %s" % (name, "; ".join(
            "Im %.0f %.2g/%.2g/%.2g" % (y, m[y]["up"][1], m[y]["down"][1], m[y]["lep"][1]) for y in HTS)))
        print("  %-9s effective exponent of the median m2/m3 up/down/leptons: %s" % (name, "; ".join(
            "%.0f-%.0f %.3f/%.3f/%.3f" % (y0, y1, *[-(math.log(m[y1][sn][0]) - math.log(m[y0][sn][0])) / (2 * PI * (y1 - y0)) for sn in SN])
            for y0, y1 in zip(HTS[:-1], HTS[1:]))))
    for k in ("point",) + VARIANTS:
        print("  within-pair weight differences, %-6s (down): %s" % (k, "; ".join(
            "Im %.0f %.3g, %.3g" % (y, float(np.median([r[3][k][0] for r in at[y] if k in r[3]])),
                                    float(np.median([r[3][k][1] for r in at[y] if k in r[3]]))) for y in HTS)))
