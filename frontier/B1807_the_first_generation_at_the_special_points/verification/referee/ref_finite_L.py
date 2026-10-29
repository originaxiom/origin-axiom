"""Attack 2: does the draft's exponent survive at finite L?  B1654's canonical end condition (P4): the coupling is
Y(a, u) = a u^T + u a^T - (a.u) 1 with u_r = sqrt(2 pi L + c_r(tau)) R_r (B1654 N6; B1691's S164 correction uses the
same u through B1656's machinery).  m1/m3 = s3/s1, m2/m3 = s2/s1 of Y(a, u), exact SVD; c_r from this referee's own
quadrature (ref_cr.py, validated against B1654's banked values); sections from refkit (own theta sums).
Also checks the exact identity  s1 s2 s3 = |a.a| |D| |a.u|  (det Y(a,u) = (a.a)(u.u)(a.u), u.u = D exactly since R.R = 0),
and compares with the draft's large-L formula m1/m3 = |D||a.R| / (2 pi L |R|^2 s1)  [s1 of Y(a, R)].
Near i and (for B1691's omega column, which the draft says it explains) near omega.
    python3 ref_finite_L.py  -> ref_finite_L.json
"""
import json, pathlib, math
import mpmath as mp
import numpy as np
from refkit import basis, dot, nrm2
from ref_cr import c_vec
from ref_near_i import make_section, mono

HERE = pathlib.Path(__file__).resolve().parent
mp.mp.dps = 30
I = mp.mpc(0, 1); W = mp.exp(2j * mp.pi / 3)
CC = {}


def cpt(tau):
    key = (round(float(tau.real), 15), round(float(tau.imag), 15))
    if key not in CC: CC[key] = [mp.mpf(float(x)) for x in c_vec(complex(tau))]
    return CC[key]


def svd3(a, u):
    au = dot(a, u); Y = mp.matrix(3, 3)
    for r in range(3):
        for c in range(3): Y[r, c] = a[r] * u[c] + u[r] * a[c] - (au if r == c else 0)
    return sorted([abs(x) for x in mp.svd_c(Y, compute_uv=False)], reverse=True)


def point(fs, tau, Ls):
    R, dR, d2R, eta6, e2, e4, e6 = basis(tau)
    f = fs(e4, e6); a = [f[0] * R[i] + f[1] * dR[i] + f[2] * d2R[i] for i in range(3)]
    R = [x / mp.pi for x in R]; a = [x / mp.pi for x in a]           # B1654's normalisation (ratios unaffected)
    c = cpt(tau); D = sum(c[k] * R[k] ** 2 for k in range(3))
    s0 = svd3(a, R)
    lim = abs(D) * abs(dot(a, R)) / (2 * mp.pi * nrm2(R) * s0[0])     # draft's m1/m3 times L
    res = {"m2/m3 at L=inf": s0[1] / s0[0], "L*m1/m3 large-L formula": lim}
    for L in Ls:
        u = [mp.sqrt(2 * mp.pi * L + c[k]) * R[k] for k in range(3)]
        s = svd3(a, u)
        ident = abs(s[0] * s[1] * s[2] - abs(dot(a, a)) * abs(dot(u, u)) * abs(dot(a, u))) / (s[0] * s[1] * s[2] + mp.mpf(10) ** -60)
        uu_vs_D = abs(dot(u, u) - D) / abs(D)
        res[L] = {"m1/m3": s[2] / s[0], "m2/m3": s[1] / s[0], "det identity rel": ident, "|u.u - D|/|D|": uu_vs_D}
    return res


def slope(v1, v2, e1, e2):
    if v1 <= 0 or v2 <= 0: return None
    return round(float(mp.log(v1 / v2) / mp.log(mp.mpf(e1) / e2)), 3)


if __name__ == "__main__":
    Ls = [0.65, 2.5, 40.0, 2560.0]
    EPS = [mp.mpf("0.1"), mp.mpf("0.03"), mp.mpf("0.01"), mp.mpf("0.003"), mp.mpf("0.001"), mp.mpf("0.0001")]
    cases_i = [("3/2 (dR; f2 = 0): draft 'm1 = 0 on all of H'", 1, None), ("11/2 generic (f2 = 0)", 3, None),
               ("19/2 generic (nu_i(f2) = 1)", 5, None), ("43/2 f2 = E6^3 (draft exponent 3)", 11, mono(0, 3)),
               ("31/2 f2 = E6^2 (draft: m2/m3 ~ eps^2, m1/m3 ~ eps^2)", 8, mono(0, 2)), ("31/2 generic (exponent 0)", 8, None)]
    cases_w = [("omega 19/2 generic (B1691: eps, eps)", 5, None), ("omega 15/2 generic (B1691: m2/m3 -> 1; m1/m3 eps^2)", 4, None),
               ("omega 23/2 generic (B1691: eps^2, eps^3)", 6, None), ("omega 11/2 generic (B1691: m1 = 0)", 3, None)]
    out = {"note": "values: m1/m3, m2/m3 of Y(a,u) at finite L; local slopes between consecutive eps", "i": {}, "omega": {}}
    for label, p0, cases in (("i", I, cases_i), ("omega", W, cases_w)):
        for name, n, f2 in cases:
            fs = make_section(n, 1, f2)
            rec = {}
            for phi in (0.3, 1.9):
                pts = [point(fs, p0 + e * mp.exp(1j * phi), Ls) for e in EPS]
                row = {"eps": [mp.nstr(e, 2) for e in EPS],
                       "L=inf m2/m3": [mp.nstr(p["m2/m3 at L=inf"], 4) for p in pts],
                       "large-L L*m1/m3": [mp.nstr(p["L*m1/m3 large-L formula"], 4) for p in pts]}
                for L in Ls:
                    m1 = [p[L]["m1/m3"] for p in pts]; m2 = [p[L]["m2/m3"] for p in pts]
                    row["L=%g" % L] = {"m1/m3": [mp.nstr(x, 4) for x in m1], "m2/m3": [mp.nstr(x, 4) for x in m2],
                                       "m1 slopes": [slope(m1[k], m1[k + 1], EPS[k], EPS[k + 1]) for k in range(len(EPS) - 1)],
                                       "m2 slopes": [slope(m2[k], m2[k + 1], EPS[k], EPS[k + 1]) for k in range(len(EPS) - 1)],
                                       "max det-identity rel": mp.nstr(max(p[L]["det identity rel"] for p in pts), 3),
                                       "max |u.u-D|/|D|": mp.nstr(max(p[L]["|u.u - D|/|D|"] for p in pts), 3)}
                rec["phi=%g" % phi] = row
            out[label][name] = rec
            r = rec["phi=0.3"]
            print(label, name, flush=True)
            for L in Ls: print("   L=%-7g m1 slopes %s   m2 slopes %s" % (L, r["L=%g" % L]["m1 slopes"], r["L=%g" % L]["m2 slopes"]), flush=True)
    # exactly at the points: m1/m3 and m2/m3 at finite L
    at = {}
    for label, p0, cases in (("i", I, cases_i), ("omega", W, cases_w)):
        for name, n, f2 in cases:
            p = point(make_section(n, 1, f2), p0, Ls)
            at[label + ": " + name] = {("L=%g" % L): {"m1/m3": mp.nstr(p[L]["m1/m3"], 4), "m2/m3": mp.nstr(p[L]["m2/m3"], 4)} for L in Ls}
            at[label + ": " + name]["L=inf m2/m3"] = mp.nstr(p["m2/m3 at L=inf"], 4)
    out["exactly at the point"] = at
    (HERE / "ref_finite_L.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(at, indent=1))
