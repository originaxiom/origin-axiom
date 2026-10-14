"""W72: the surface frame's Yukawa (main's S122 relay, section 2). B1644's coupling between the surface frame's three
chiral modes (weight 3/2 in rho_R, one unit each at the cusp), its multipliers, the Higgs's unique surface mode h of
weight 5/2 in rho' = rho_R (x) chi_i, the Petersson pairing Y_ab = <G_ab, h> and its rank, and the modes' norms. The
rule (W72_RULE.md) was committed before this script.

  X1  the multipliers, exact: the eigenlines' pairing table and the exponent classes of f_ab(a) and G_ab
  X2  the multipliers, numerically on the record's sections at five sample points (T and S laws)
  X3  the Higgs's surface mode: chi_{5/2}(rho') by W45's formula, the collocation's null count, the 40-digit solve
  X4  the Yukawa's rank: Y_ab in two settings (Y0, nodes), their agreement, the singular values
  X5  the modes' norms: a non-zero coefficient at a negative exponent in each matter mode
  X6  the verdict
  plus the read-outs: the singular values (basis-dependent), h's first coefficients, the parts above and below Y0

Run: python3 the_surface_yukawa.py  ->  the_surface_yukawa.json beside it.
"""
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_second_unit as SU  # noqa: E402  (W65: the basis, the exponents, rho_R, the evaluation)
import the_residual_charges_at_omega as RC  # noqa: E402  (W68: the collocation at any weight)
import the_index_on_the_weaves_surface as IW  # noqa: E402  (W45: chi and the null count)

OUT = HERE / "the_surface_yukawa.json"
mp.mp.dps = 40
I = mp.mpc(0, 1)
LINES = SU.LINES
E8 = {"e_i": 1, "v+": 7, "v-": 3}                       # rho_R's exponents, in eighths
E8P = {"e_i": 3, "v+": 1, "v-": 5}                      # rho' = rho_R (x) chi_i
BB = {("e_i", "e_i"): 1, ("v+", "v-"): 2, ("v-", "v+"): 2}
WNORM = {"e_i": 1, "v+": 2, "v-": 2}                    # B[l] . conj(B[l])
E3PI4 = mp.exp(3 * I * mp.pi / 4)
RS2 = [[E3PI4 * SU.P_SWAP[r][c] for c in range(3)] for r in range(3)]
RT2 = [[E3PI4 * SU.L_INV[r][c] for c in range(3)] for r in range(3)]
MATTER = [("F_i", (1, 0, 0)), ("F+", (0, 1, 0)), ("F-", (0, 0, 1))]
HIGGS = [("E", (1, 0, 0)), ("R", (0, 1, 0)), ("R'", (0, 0, 1))]
PAIRS = list(itertools.combinations_with_replacement(range(3), 2))
CAP8 = 8 * 30                                           # keep product exponents up to 30


def best_section(units, k):
    order = [l for l, on in zip(LINES, units) if on] + [l for l, on in zip(LINES, units) if not on]
    best = None
    for line in order:
        terms, res = RC.solve(units, k, line)
        if best is None or res < best[1]:
            best = (terms, res, line)
        if res < 1e-20:
            break
    return best


def to_series(terms, classes):
    """{(line, exponent in eighths): coefficient}, checking each exponent lies in its line's class"""
    out = {}
    for l, e, a in terms:
        n8 = int(mp.nint(e * 8))
        assert abs(e * 8 - n8) < mp.mpf("1e-25") and (n8 - classes[l]) % 8 == 0, (l, e)
        out[(l, n8)] = out.get((l, n8), 0) + a
    return out


def dot_series(X, Y):
    s = {}
    for (l1, n1), a in X.items():
        for (l2, n2), b in Y.items():
            w = BB.get((l1, l2))
            if w and n1 + n2 <= CAP8:
                s[n1 + n2] = s.get(n1 + n2, 0) + w * a * b
    return s


def scal_vec(s, X):
    out = {}
    for n, a in s.items():
        for (l, m), b in X.items():
            if n + m <= CAP8:
                out[(l, n + m)] = out.get((l, n + m), 0) + a * b
    return out


def add(*parts):
    out = {}
    for sign, X in parts:
        for key, a in X.items():
            out[key] = out.get(key, 0) + sign * a
    return out


def G_series(Fa, Fb, R):
    return add((1, scal_vec(dot_series(R, Fb), Fa)), (1, scal_vec(dot_series(R, Fa), Fb)),
               (-1, scal_vec(dot_series(Fa, Fb), R)))


def nonzero(series, rel=mp.mpf("1e-25")):
    big = max(abs(v) for v in series.values())
    return {k: v for k, v in series.items() if abs(v) > rel * big}


def ev_vec(series, t):
    out = [mp.mpc(0)] * 3
    for (l, n8), a in series.items():
        z = a * mp.exp(2 * mp.pi * I * mp.mpf(n8) / 8 * t)
        out = [out[k] + z * SU.B[l][k] for k in range(3)]
    return out


def ev_scal(series, t):
    return mp.fsum(a * mp.exp(2 * mp.pi * I * mp.mpf(n8) / 8 * t) for n8, a in series.items())


def solve_twisted(k, norm_line, N=30, M=120):
    """weight-k holomorphic forms for rho' with no units, the lowest coefficient on norm_line set to 1"""
    lam = {l: mp.mpf(E8P[l]) / 8 for l in LINES}
    cols = [(l, n) for l in LINES for n in range(0, N) if not (l == norm_line and n == 0)]
    thetas = [mp.pi / 3 + mp.mpf("0.02") + j * (mp.pi / 3 - mp.mpf("0.04")) / (M - 1) for j in range(M)]
    A = mp.matrix(3 * M, len(cols))
    b = mp.matrix(3 * M, 1)
    kk = mp.mpf(k.numerator) / k.denominator
    for r, th in enumerate(thetas):
        t = mp.exp(I * th)
        ts, tk = -1 / t, mp.power(t, kk)
        for c, (l, n) in enumerate(cols):
            e = n + lam[l]
            sc = mp.exp(2 * mp.pi * e * SU.H0)
            v2 = SU.matvec(RS2, SU.B[l])
            for q in range(3):
                A[3 * r + q, c] = (SU.B[l][q] * SU.qp(e, ts) - tk * v2[q] * SU.qp(e, t)) * sc
        e = lam[norm_line]
        v2 = SU.matvec(RS2, SU.B[norm_line])
        for q in range(3):
            b[3 * r + q] = -(SU.B[norm_line][q] * SU.qp(e, ts) - tk * v2[q] * SU.qp(e, t))
    Q, Rm = mp.qr(A, mode="skinny")
    x = mp.lu_solve(Rm, Q.H * b)
    res = mp.norm(A * x - b) / mp.norm(b)
    terms = [(norm_line, lam[norm_line], mp.mpf(1))] + [
        (l, n + lam[l], x[c] * mp.exp(2 * mp.pi * (n + lam[l]) * SU.H0)) for c, (l, n) in enumerate(cols)]
    return terms, float(res)


def np_eval(series):
    keys = list(series)
    vec = np.array([[complex(series[k] * SU.B[k[0]][c]) for c in range(3)] for k in keys])
    ex = np.array([k[1] / 8 for k in keys])
    return lambda T: np.exp(2j * np.pi * np.outer(T, ex)) @ vec           # (len(T), 3)


def pairing(Gs, hs, Gnp, hnp, Y0, nodes):
    up = mp.mpc(0)
    for (l, n8), g in Gs.items():
        if n8 > 0 and (l, n8) in hs:
            E = mp.mpf(n8) / 8
            up += WNORM[l] * g * mp.conj(hs[(l, n8)]) * mp.gammainc(mp.mpf(3) / 2, 4 * mp.pi * E * Y0) / (
                4 * mp.pi * E) ** (mp.mpf(3) / 2)
    xs, wx = np.polynomial.legendre.leggauss(nodes)
    xs, wx = xs / 2, wx / 2                                                    # on [-1/2, 1/2]
    us, wu = np.polynomial.legendre.leggauss(nodes)
    low = 0j
    for x, w in zip(xs, wx):
        y0 = np.sqrt(1 - x * x)
        ys = y0 + (us + 1) / 2 * (Y0 - y0)
        wy = wu / 2 * (Y0 - y0)
        T = x + 1j * ys
        vals = np.sum(Gnp(T) * np.conj(hnp(T)), axis=1) * np.sqrt(ys)
        low += w * np.sum(wy * vals)
    return complex(up), low


def main():
    out = {"status": "W72: the surface frame's Yukawa (the rule W72_RULE.md first; one run)"}
    sec, res = {}, {}
    for name, u in MATTER:
        terms, r, line = best_section(u, Fraction(3, 2))
        sec[name], res[name] = to_series(terms, E8), (r, line)
    for name, u in HIGGS:
        terms, r, line = best_section(u, Fraction(-1, 2))
        sec[name], res[name] = to_series(terms, E8), (r, line)
    F = [sec[n] for n, _ in MATTER]
    R = sec["R"]
    G = {(a, b): G_series(F[a], F[b], R) for a, b in PAIRS}
    fab = {(a, b, hn): dot_series(sec[hn], G[(a, b)]) for a, b in PAIRS for hn, _ in HIGGS}
    # X1
    table = {f"{l1}.{l2}": str(BB.get((l1, l2), 0)) for l1 in LINES for l2 in LINES}
    classes_ok = all(((E8[l1] + E8[l2]) % 8 == 2) for (l1, l2) in BB)
    f_ok = all(n8 % 8 == 4 for s in fab.values() for n8 in nonzero(s))
    G_ok = all((n8 - E8P[l]) % 8 == 0 for s in G.values() for (l, n8) in nonzero(s))
    out["X1"] = {"pairing table": table, "pair exponent sums are 1/4 mod 1": classes_ok,
                 "every f exponent in 1/2 + Z": f_ok, "G exponents in rho' classes": G_ok,
                 "holds": bool(classes_ok and f_ok and G_ok)}
    # X2
    worst = 0.0
    for t in SU.SAMPLE[:5]:
        for a, b in PAIRS:
            Gt, G1, Gs_ = ev_vec(G[(a, b)], t), ev_vec(G[(a, b)], t + 1), ev_vec(G[(a, b)], -1 / t)
            want1 = SU.matvec(RT2, Gt)
            wantS = [mp.power(t, mp.mpf(5) / 2) * z for z in SU.matvec(RS2, Gt)]
            nG = max(abs(z) for z in Gt)
            worst = max(worst, float(max(abs(G1[k] - want1[k]) for k in range(3)) / nG),
                        float(max(abs(Gs_[k] - wantS[k]) for k in range(3)) / max(abs(z) for z in wantS)))
            for hn, _ in HIGGS:
                s = fab[(a, b, hn)]
                f0, f1, fS = ev_scal(s, t), ev_scal(s, t + 1), ev_scal(s, -1 / t)
                worst = max(worst, float(abs(f1 + f0) / abs(f0)), float(abs(fS + t * t * f0) / abs(t * t * f0)))
    out["X2"] = {"largest relative deviation": worst, "holds": bool(worst < 1e-10)}
    # X3
    rS2 = np.array([[complex(x) for x in row] for row in RS2])
    rT2 = np.array([[complex(x) for x in row] for row in RT2])
    chi, lam = IW.chi(Fraction(5, 2), rS2, rT2)
    null, gap = IW.dims(rS2, rT2, Fraction(5, 2))
    hbest = None
    for line in ("v+", "e_i", "v-"):
        terms, r = solve_twisted(Fraction(5, 2), line)
        if hbest is None or r < hbest[1]:
            hbest = (terms, r, line)
    hs = to_series(hbest[0], E8P)
    out["X3"] = {"chi_5/2(rho')": chi, "exponents": lam, "null count": null, "gap": gap,
                 "40-digit residual": hbest[1], "normalised on": hbest[2],
                 "holds": bool(abs(chi - 1) < 1e-9 and null == 1 and gap[0] is not None and gap[0] > 1e-6
                               and gap[1] < 1e-9 and hbest[1] < 1e-20)}
    # X4
    hnp = np_eval(hs)
    Ymat, parts = {}, {}
    for Y0, nodes in ((1.25, 64), (2.0, 96)):
        M_ = np.zeros((3, 3), dtype=complex)
        for a, b in PAIRS:
            up, low = pairing(G[(a, b)], hs, np_eval(G[(a, b)]), hnp, mp.mpf(Y0), nodes)
            M_[a, b] = M_[b, a] = up + low
            parts[f"{Y0}:{a}{b}"] = {"above": [up.real, up.imag], "below": [low.real, low.imag]}
        Ymat[Y0] = M_
    A1, A2 = Ymat[1.25], Ymat[2.0]
    agree = float(np.max(np.abs(A1 - A2)) / np.max(np.abs(A2)))
    sv = np.linalg.svd(A2, compute_uv=False)
    out["X4"] = {"agreement of the two settings": agree, "singular values (basis F_i, F+, F-)": sv.tolist(),
                 "smallest over largest": float(sv[-1] / sv[0]),
                 "Y (Y0 = 2.0)": [[[z.real, z.imag] for z in row] for row in A2],
                 "holds": bool(agree < 1e-8 and sv[-1] / sv[0] > 1e-6)}
    # X5
    neg = {name: sorted(str(Fraction(n8, 8)) for (l, n8), a in nonzero(sec[name]).items() if n8 < 0)
           for name, _ in MATTER}
    out["X5"] = {"negative exponents with non-zero coefficient": neg,
                 "holds": bool(neg["F_i"] == ["-7/8"] and neg["F+"] == ["-1/8"] and neg["F-"] == ["-5/8"])}
    out["X6"] = {"rank 3 and the modes not normalisable": bool(out["X4"]["holds"] and out["X5"]["holds"]),
                 "holds": bool(out["X3"]["holds"] and out["X4"]["holds"] and out["X5"]["holds"])}
    out["cells"] = {k: out[k]["holds"] for k in ("X1", "X2", "X3", "X4", "X5", "X6")}
    out["read-outs"] = {
        "section residuals and lines": {k: [v[0], v[1]] for k, v in res.items()},
        "h's first coefficients": {f"{l}:{Fraction(n8, 8)}": [float(mp.re(a)), float(mp.im(a))]
                                   for (l, n8), a in sorted(hs.items(), key=lambda kv: kv[0][1]) if n8 < 8 * 3},
        "the parts above and below Y0": parts,
        "f's lowest exponent per pair and Higgs": {f"{a}{b}:{hn}": str(Fraction(min(nonzero(s)), 8))
                                                   for (a, b, hn), s in fab.items()}}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main()
