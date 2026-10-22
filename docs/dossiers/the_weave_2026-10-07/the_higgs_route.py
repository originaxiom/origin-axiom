#!/usr/bin/env python3
"""W123 — the Higgs route to the cusp's unit (the script; `W123_RULE.md` was committed and pushed before it).

- Y0: R = (-th2^2, -th4^2, i th3^2)/(th2 th3 th4) (the 1/pi dropped) as this seat's own exact Laurent series in
  x = q^(1/8); its line orders; the collocation residual of weight -1/2 for rho = (e^{i pi/4} P, e^{i pi/4} L^-1).
- Y1-Y3, Y6: per-line end data m on the eigenlines of rho(T), counted by W45's q-expansion collocation extended to
  per-line bounds (d for weight 3/2, h1 for the dual at weight 1/2), and by W45's formula with shifted exponents;
  the other hand rho_T-bar at weight 1/2 (W45's kept identification).
- Y4: DR = q dR/dq + E2 R / 24 exactly; its line orders and its collocation residual of weight 3/2.
- Y5, Y7: the single-line sections' leading orders; which lines are parity lines.

    python3 -B the_higgs_route.py      # writes the_higgs_route.json and the_higgs_route_run.txt beside itself
"""
import ast
import contextlib
import io
import itertools
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_index_on_the_weaves_surface as W45  # noqa: E402

mp.mp.dps = 30
out, log = {"arc": "W123", "rule": "W123_RULE.md"}, []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    log.append(s)


# ---------------- the representation ----------------
w8 = np.exp(1j * np.pi / 4)
Pm = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=complex)
Linv = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]], dtype=complex)
rS, rT = w8 * Pm, w8 * Linv
LINES = {Fr(1, 8): np.array([1, 0, 0]) + 0j, Fr(3, 8): np.array([0, 1, 1j]) / np.sqrt(2),
         Fr(7, 8): np.array([0, 1, -1j]) / np.sqrt(2)}
EXPS = sorted(LINES)                                    # 1/8, 3/8, 7/8; 7/8 is v+


def rep_checks():
    braid = np.allclose(rS @ rS, np.linalg.matrix_power(rS @ rT, 3), atol=1e-12)
    S2 = np.allclose(rS @ rS, 1j * np.eye(3), atol=1e-12)
    eig = all(np.allclose(rT @ v, np.exp(2j * np.pi * float(e)) * v, atol=1e-12) for e, v in LINES.items())
    return {"rho(S)^2 = (rho(S) rho(T))^3": bool(braid), "rho(S)^2 = i": bool(S2), "the three eigenlines": bool(eig)}


# ---------------- the per-line collocation count (W45's dims, extended) ----------------
def dims_lower(rS, rT, k, lower, N=30, M=160):
    """dim of the forms of weight k for (rS, rT) with order >= lower(lam) on the eigenline of exponent lam;
    returns (null count, (largest small, smallest kept) singular values, null vectors as {exp: coeffs})"""
    rS, rT = np.array(rS, dtype=complex), np.array(rT, dtype=complex)
    d = rS.shape[0]
    w, P = np.linalg.eig(rT)
    P = np.linalg.qr(P)[0] if np.allclose(rT @ rT.conj().T, np.eye(d)) else P
    lam = [Fr(float(np.angle(z) / (2 * np.pi)) % 1.0).limit_denominator(48) for z in w]
    lows = [lower(x) for x in lam]
    assert all((lo - x).denominator == 1 for lo, x in zip(lows, lam))
    cols = [(j, n) for j in range(d) for n in range(N)]
    h0 = np.sqrt(3) / 2

    def phi(j, n, t):
        e = float(lows[j]) + n
        return np.exp(2j * np.pi * e * t) * np.exp(2 * np.pi * e * h0)

    rows = []
    for th in np.linspace(np.pi / 3 + 0.02, 2 * np.pi / 3 - 0.02, M):
        t = np.exp(1j * th)
        ts, tk = -1 / t, np.exp(float(k) * np.log(t))
        block = np.zeros((d, len(cols)), dtype=complex)
        for c, (j, n) in enumerate(cols):
            block[:, c] = P[:, j] * phi(j, n, ts) - tk * (rS @ P[:, j]) * phi(j, n, t)
        rows.append(block)
    A = np.vstack(rows)
    _, s, Vh = np.linalg.svd(A, full_matrices=False)
    s = s / s[0]
    null = int(sum(s < 1e-9))
    gap = [float(s[-null]) if null else None, float(s[len(s) - null - 1]) if null < len(s) else None]
    vecs = []
    for r in range(len(s) - null, len(s)):
        v = Vh[r].conj()
        per = {}
        for j in range(d):
            c = v[j * N:(j + 1) * N]
            big = np.abs(c) > 1e-6 * np.abs(v).max()
            per[str(lam[j])] = {"lower": str(lows[j]),
                                "leading order": str(lows[j] + int(np.argmax(big))) if big.any() else None}
        vecs.append(per)
    return null, gap, vecs


def census(rS, rT, k, exps, box=(-1, 0, 1, 2)):
    chi0 = W45.chi(Fr(k), rS, rT)[0]
    dual = (np.conj(rS), np.conj(rT))
    table, law, formula = {}, True, True
    for m in itertools.product(box, repeat=3):
        mm = dict(zip(exps, m))
        d, gd, vd = dims_lower(rS, rT, k, lambda x: x - mm[x])
        h, gh, _ = dims_lower(*dual, 2 - k, lambda y: y + mm[(1 - y) % 1] if y != 0 else 1 + mm[Fr(0)])
        chi_f = chi0 + sum(m)
        table[str(m)] = {"d": d, "h1": h, "d - h1": d - h, "sum m": sum(m), "formula chi": round(chi_f, 9),
                         "gaps": [gd, gh], "four-dimensional count -chi": -sum(m),
                         "leading orders": vd if sum(1 for x in m if x > 0) == 1 and max(m) == 1
                         and min(m) == 0 else None}
        law &= (d - h == sum(m))
        formula &= abs(chi_f - sum(m)) < 1e-9
    return table, law, formula, chi0


# ---------------- exact Laurent series in x = q^(1/8) ----------------
NT = 420


class L:
    """sum c[i] x^(v + i), i < NT, Fraction coefficients"""

    def __init__(self, v, c):
        k = 0
        while k < len(c) and c[k] == 0:
            k += 1
        self.v, self.c = v + k, (list(c[k:]) + [Fr(0)] * NT)[:NT]

    def __mul__(self, o):
        c = [Fr(0)] * NT
        for i, a in enumerate(self.c):
            if a:
                for j in range(NT - i):
                    if o.c[j]:
                        c[i + j] += a * o.c[j]
        return L(self.v + o.v, c)

    def __add__(self, o):
        v = min(self.v, o.v)
        c = [Fr(0)] * NT
        for s in (self, o):
            for i, a in enumerate(s.c):
                if i + s.v - v < NT:
                    c[i + s.v - v] += a
        return L(v, c)

    def neg(self):
        return L(self.v, [-a for a in self.c])

    def inv(self):
        a0 = self.c[0]
        b = [Fr(0)] * NT
        b[0] = 1 / a0
        for n in range(1, NT):
            b[n] = -sum(self.c[i] * b[n - i] for i in range(1, n + 1)) / a0
        return L(-self.v, b)

    def qdq(self):                                           # q d/dq x^n = (n/8) x^n
        return L(self.v, [a * Fr(self.v + i, 8) for i, a in enumerate(self.c)])

    def scale(self, r):
        return L(self.v, [a * r for a in self.c])

    def ev(self, tau):
        x = mp.exp(2j * mp.pi * tau / 8)
        return mp.fsum(mp.mpf(a.numerator) / a.denominator * x ** (self.v + i) for i, a in enumerate(self.c) if a)


def theta2():
    c = [Fr(0)] * NT
    n = 0
    while (2 * n + 1) ** 2 - 1 < NT:
        c[(2 * n + 1) ** 2 - 1] = Fr(2)
        n += 1
    return L(1, c)


def theta34(sign):
    c = [Fr(0)] * NT
    n = 0
    while 4 * n * n < NT:
        c[4 * n * n] += Fr(1) if n == 0 else Fr(2) * (sign ** n)
        n += 1
    return L(0, c)


def E2():
    c = [Fr(0)] * NT
    c[0] = Fr(1)
    for n in range(1, NT // 8 + 1):
        if 8 * n < NT:
            c[8 * n] = Fr(-24 * sum(dd for dd in range(1, n + 1) if n % dd == 0))
    return L(0, c)


def the_R_series():
    t2, t3, t4 = theta2(), theta34(1), theta34(-1)
    A = t2 * (t3 * t4).inv()                 # th2/(th3 th4)
    B = t4 * (t2 * t3).inv()                 # th4/(th2 th3)
    C = t3 * (t2 * t4).inv()                 # th3/(th2 th4)
    comps = {"i": (A.neg(), 1), "j": (B.neg(), 1), "k": (C, 1j)}      # R = (-A, -B, iC)
    lines = {Fr(1, 8): A.neg(), Fr(7, 8): B.neg() + C.neg(), Fr(3, 8): B.neg() + C}   # e_i, e_j + i e_k, e_j - i e_k
    e2 = E2()
    serre = lambda s: s.qdq() + (e2 * s).scale(Fr(1, 24))
    dcomps = {key: (serre(s), f) for key, (s, f) in comps.items()}
    dlines = {e: serre(s) for e, s in lines.items()}
    return comps, lines, dcomps, dlines


def residual(comps, k, npts=9):
    """max |f(-1/tau) - tau^k rho(S) f(tau)| / |f| on the arc"""
    worst = mp.mpf(0)
    S = mp.matrix([[0, mp.exp(1j * mp.pi / 4), 0], [mp.exp(1j * mp.pi / 4), 0, 0], [0, 0, mp.exp(1j * mp.pi / 4)]])
    for th in mp.linspace(mp.pi / 3 + mp.mpf("0.05"), 2 * mp.pi / 3 - mp.mpf("0.05"), npts):
        t = mp.exp(1j * th)
        f = mp.matrix([comps[key][0].ev(t) * comps[key][1] for key in "ijk"])
        g = mp.matrix([comps[key][0].ev(-1 / t) * comps[key][1] for key in "ijk"])
        rhs = mp.exp(k * mp.log(t)) * (S * f)
        worst = max(worst, mp.norm(g - rhs) / mp.norm(f))
    return float(worst)


def main():
    out["representation"] = rep_checks()
    say("representation", out["representation"])

    # Y0 and Y4: the exact series
    comps, lines, dcomps, dlines = the_R_series()
    ordR = {str(e): str(Fr(s.v, 8)) for e, s in lines.items()}
    ordD = {str(e): str(Fr(s.v, 8)) for e, s in dlines.items()}
    resR, resD = residual(comps, mp.mpf(-1) / 2), residual(dcomps, mp.mpf(3) / 2)
    want = {"1/8": "1/8", "3/8": "3/8", "7/8": "-1/8"}
    Y0 = {"R line orders (in q)": ordR, "residual weight -1/2": resR,
          "holds": ordR == want and resR < 1e-10 and all(out["representation"].values())}
    say("Y0 R line orders", ordR, "| residual %.2e" % resR, "->", Y0["holds"])

    # the census for rho at weight 3/2
    table, law, formula, chi0 = census(rS, rT, Fr(3, 2), EXPS)
    Y1_cases = {m: v["d"] for m, v in table.items() if max(ast.literal_eval(m)) <= 0}
    Y1 = {"d(m) for every m <= 0": Y1_cases, "holds": all(v == 0 for v in Y1_cases.values())}
    Y2 = {"chi_{3/2} at m = 0 (formula)": round(chi0, 9), "d - h1 = sum m for all 64": bool(law),
          "formula agrees for all 64": bool(formula), "holds": bool(law and formula)}
    singles = {}
    for e in EXPS:
        m = tuple(1 if x == e else 0 for x in EXPS)
        row = table[str(m)]
        singles[str(e)] = {"m": list(m), "d": row["d"], "h1": row["h1"], "leading orders": row["leading orders"]}
    Y3 = {"single-line units": singles, "holds": all(v["d"] == 1 and v["h1"] == 0 for v in singles.values())}
    vplus = singles["7/8"]["leading orders"][0] if singles["7/8"]["d"] == 1 else None
    Y4 = {"DR line orders (in q)": ordD, "residual weight 3/2": resD,
          "the (0,0,1) space's section has DR's orders": vplus is not None and all(
              vplus[e]["leading order"] == ordD[e] for e in ordD),
          "holds": ordD == want and resD < 1e-10 and Y3["holds"]}   # the orders' match is a read-out
    poles = {}
    for e in EXPS:
        lo = singles[str(e)]["leading orders"][0][str(e)]["leading order"] if singles[str(e)]["d"] == 1 else None
        poles[str(e)] = lo
    least = max((Fr(v), k) for k, v in poles.items())[1] if all(poles.values()) else None   # the pole nearest 0
    Y5 = {"leading order on the unit's line": poles, "least pole on": least,
          "holds": poles == {"1/8": "-7/8", "3/8": "-5/8", "7/8": "-1/8"} and least == "7/8" and Y4["holds"]}
    say("Y1 no unit, no Higgs:", Y1["holds"], "| Y2 index law:", Y2)
    say("Y3 single-line units:", {k: (v["d"], v["h1"]) for k, v in singles.items()}, "->", Y3["holds"])
    say("Y4 DR line orders", ordD, "| residual %.2e" % resD, "| matches the v+ section:",
        Y4["the (0,0,1) space's section has DR's orders"], "->", Y4["holds"])
    say("Y5 leading pole orders", poles, "| least on", least, "->", Y5["holds"])

    # Y6: the other hand
    with contextlib.redirect_stdout(io.StringIO()):
        _, kept = W45.E3()
    bS, bT = (np.array(x, dtype=complex) for x in kept["S <-> S~^-1, T <-> L"])
    wb = np.linalg.eigvals(bT)
    bexps = sorted(Fr(float(np.angle(z) / (2 * np.pi)) % 1.0).limit_denominator(48) for z in wb)
    btable, blaw, bformula, bchi0 = census(bS, bT, Fr(1, 2), bexps)
    bY1 = all(v["d"] == 0 for m, v in btable.items() if max(ast.literal_eval(m)) <= 0)
    bsingles = {}
    for e in bexps:
        m = tuple(1 if x == e else 0 for x in bexps)
        row = btable[str(m)]
        lo = (row["leading orders"][0][str(e)]["leading order"] if row["d"] == 1 and row["leading orders"] else None)
        bsingles[str(e)] = {"d": row["d"], "h1": row["h1"], "leading order on the unit's line": lo}
    bleast = (max((Fr(v["leading order on the unit's line"]), k) for k, v in bsingles.items())[1]
              if all(v["leading order on the unit's line"] for v in bsingles.values()) else None)
    Y6 = {"exponents": [str(e) for e in bexps], "chi_{1/2} at m = 0": round(bchi0, 9), "Y1": bool(bY1),
          "Y2 law": bool(blaw), "Y2 formula": bool(bformula), "single-line units": bsingles, "least pole on": bleast,
          "holds": bool(bY1 and blaw and bformula and all(v["d"] == 1 and v["h1"] == 0 for v in bsingles.values())
                        and bleast == "7/8")}
    say("Y6 the other hand: exponents", Y6["exponents"], "| Y1", bY1, "| law", blaw, "| formula", bformula,
        "| singles", {k: (v["d"], v["h1"], v["leading order on the unit's line"]) for k, v in bsingles.items()},
        "| least pole on", bleast, "->", Y6["holds"])

    # Y7: read-out
    parity = {str(e): bool(np.count_nonzero(np.abs(v) > 1e-12) == 1) for e, v in LINES.items()}
    Y7 = {"d and h1 for rho": {m: [v["d"], v["h1"]] for m, v in table.items()},
          "d and h1 for rho_T-bar": {m: [v["d"], v["h1"]] for m, v in btable.items()},
          "single-line units diagonal in the parity basis": parity,
          "four-dimensional count for a single-line unit": -1, "for the uniform unit": -3,
          "uniform unit (1,1,1): d, h1": [table["(1, 1, 1)"]["d"], table["(1, 1, 1)"]["h1"]]}
    say("Y7 parity lines", parity, "| uniform unit d, h1", Y7["uniform unit (1,1,1): d, h1"])

    out.update({"Y0": Y0, "Y1": Y1, "Y2": Y2, "Y3": Y3, "Y4": Y4, "Y5": Y5, "Y6": Y6, "Y7": Y7,
                "census rho": table, "census rho_T-bar": btable})
    out["verdict"] = {c: out[c]["holds"] for c in ("Y0", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6")}
    say("verdict", out["verdict"])
    (HERE / "the_higgs_route.json").write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    (HERE / "the_higgs_route_run.txt").write_text("\n".join(log) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
