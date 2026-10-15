"""W92: the per-field twisted units, the dressing, and both readings' pieces for chat1's seal. The rule (W92_RULE.md)
was committed before this script; the construction, the cells and the priors are there.

The construction (the z-form dressing). In the coordinate basis (i, j, k) rho_R's components are the even spin
structures theta2, theta4, theta3. A field of charge q on the line l = (la, lb) of order N (chat1's instrument's
convention, w = (la + lb tau)/N) has every unit dressed component by component:
    U^(q)_c = U_c * D_c,   D_c = [exp(i pi (al^2 tau + 2 al be)) theta_s(be + al tau | tau)]^2 / theta_s(0 | tau)^2,
with (al, be) = (q lb / N, q la / N) and s = (2, 4, 3) on (i, j, k). In characteristics,
    exp(i pi (al^2 tau + 2 al be)) theta_s(be + al tau) = theta[a_s + al, b_s + be](0 | tau) * exp(-2 pi i al b_s),
so the numerator is sum_{n,m} q^{((n+a)^2 + (m+a)^2)/2} exp(2 pi i [(n + m + 2a) b - 2 al b_s]), a = a_s + al,
b = b_s + be, q = e^{2 pi i tau}: exact rational exponents and phases. The denominator's inverse has exact rational
coefficients. R stays neutral; h is dressed by the Higgs's charge.

  V1  the dressing series against direct evaluation (mpmath jtheta), every N, line, q, component, two points, 1e-40
  V2  the multiplier on every L R^n (n <= 3N^2) fixing a primitive line: one scalar exp(2 pi i eps c q^2 / N), 1e-30
  V3  per-field closure of the Y integrands and the K norms on W72's units, SM charges, three threads per N, 1e-25;
      the phase with +q_H^2 misses where c 2 q_H^2 != 0 mod N
  V4  the odd structure's zero: only N = 12, q = 6, one component per primitive line (parity rule)
  V6  the readings compared: theta_s(x+y) theta_s(x-y) theta_s(0)^2 = theta_s(x)^2 theta_s(y)^2 + eps_s theta_1(x)^2
      theta_1(y)^2, eps = (-1, -1, +1), z-form, SM sectors, every primitive line, 1e-40
  V7  THETA2: at q = 0 the Serre derivatives give theta^2 F in span(E4 F, f) (control); for q != 0 they miss by > 1e-3
  V8  chat1's coupling (units_cells.py at 39ffb3928) equals W91's V_s up to one constant, 1e-30
  read-outs: the dressed units' lowest exponents per component for the SM fields; the delivery's size

Delivery: PerFieldSource (a drop-in for chat1's UnitSource), dressing_series / dressing_exact, dressing_at, and
the_per_field_units_delivery.json.gz (exact numerators for every primitive line up to sign and q = 0..N//2 at
N = 9, 11, 12, to exponent 31, with the three inverse thetanull squares).

Run: python3 the_per_field_units.py  ->  the_per_field_units.json and the delivery file beside it.
"""
import gzip
import importlib.util
import itertools
import json
import subprocess
import sys
import tempfile
import time
from fractions import Fraction as Fr
from math import ceil, floor, gcd, sqrt
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
OUT = HERE / "the_per_field_units.json"
DELIVERY = HERE / "the_per_field_units_delivery.json.gz"
CHAT1_COMMIT = "39ffb3928b80ce4aa055fc29f6be0c0eaa95e2a7"
CHAT1_PATH = "relays/chat1_2026-10-15_route/twisted_units/units_cells.py"

COMP = ("i", "j", "k")
S_OF = (2, 4, 3)                                             # theta index per component
CH = {2: (Fr(1, 2), Fr(0)), 4: (Fr(0), Fr(1, 2)), 3: (Fr(0), Fr(0)), 1: (Fr(1, 2), Fr(1, 2))}
CQ = (mp.mpc(-1), mp.mpc(-1), mp.mpc(0, 1))                  # chat1's quat3 constants on (theta2, theta4, theta3)
EPS_RIEMANN = (-1, -1, 1)
B = {"e_i": (1, 0, 0), "v+": (0, 1, -1j), "v-": (0, 1, 1j)}
SM = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
SECTORS = {"up": ("Q", "u", "H"), "down": ("Q", "d", "Hbar"), "lepton": ("L", "e", "Hbar")}
NS = (9, 11, 12)
EMAX = 30
EMAX_DELIVERY = 31


def mpf(x):
    return mp.mpf(x.numerator) / x.denominator


# ------------------------------------------------------------------------------------------- the exact dressing
def char_of(c, q, line, N):
    """(al, be) and the shifted characteristic (a, b) of component c"""
    la, lb = line
    al, be = Fr(q * lb, N), Fr(q * la, N)
    a_s, b_s = CH[S_OF[c]]
    return al, be, a_s + al, b_s + be


def is_odd(c, q, line, N):
    _, _, a, b = char_of(c, q, line, N)
    return (a - Fr(1, 2)).denominator == 1 and (b - Fr(1, 2)).denominator == 1


def numerator_exact(c, q, line, N, emax):
    """{exponent: {turns: count}} for [z-form theta_s(q w)]^2, exponents <= emax (exact)"""
    al, be, a, b = char_of(c, q, line, N)
    b_s = CH[S_OF[c]][1]
    out = {}
    M = int(ceil(sqrt(2 * emax))) + 3
    n0 = -int(floor(a))
    for n in range(n0 - M, n0 + M + 1):
        for m in range(n0 - M, n0 + M + 1):
            e = ((n + a) ** 2 + (m + a) ** 2) / 2
            if e > emax:
                continue
            t = ((n + m + 2 * a) * b - 2 * al * b_s) % 1
            d = out.setdefault(e, {})
            d[t] = d.get(t, 0) + 1
    return out


_INV = {}


def inverse_thetanull_sq(c, emax):
    """1 / theta_s(0)^2 as {exponent: Fraction}, exponents <= emax (exact)"""
    key = (c, emax)
    if key in _INV:
        return _INV[key]
    a_s, b_s = CH[S_OF[c]]
    den = {}
    M = int(ceil(sqrt(2 * (emax + 2)))) + 3
    for n in range(-M, M + 1):
        for m in range(-M, M + 1):
            e = ((n + a_s) ** 2 + (m + a_s) ** 2) / 2
            if e > emax + 2:
                continue
            sgn = -1 if ((n + m + 2 * a_s) * b_s) % 1 == Fr(1, 2) else 1
            den[e] = den.get(e, 0) + sgn
    den = {e: v for e, v in den.items() if v}
    e0 = min(den)
    h = Fr(1, 2) if a_s == 0 else Fr(1)
    cf = {}
    for e, v in den.items():
        j = (e - e0) / h
        assert j.denominator == 1
        cf[int(j)] = Fr(v)
    J = int((emax + e0) / h) + 1
    inv = [Fr(0)] * (J + 1)
    inv[0] = 1 / cf[0]
    for j in range(1, J + 1):
        inv[j] = -sum(cf[i] * inv[j - i] for i in range(1, j + 1) if i in cf) / cf[0]
    out = {-e0 + j * h: inv[j] for j in range(J + 1) if inv[j] and -e0 + j * h <= emax}
    _INV[key] = out
    return out


def dressing_series(c, q, line, N, emax=EMAX_DELIVERY):
    """D_c as {exponent: mpc}, exponents <= emax; exact data, coefficients at the working precision"""
    if is_odd(c, q, line, N):
        return {}
    shift_max = Fr(1, 4)
    num = numerator_exact(c, q, line, N, emax + shift_max + 1)
    inv = inverse_thetanull_sq(c, emax + 2)
    numv = {e: mp.fsum(k * mp.expjpi(2 * mpf(t)) for t, k in d.items()) for e, d in num.items()}
    out = {}
    for e1, v1 in numv.items():
        for e2, v2 in inv.items():
            e = e1 + e2
            if e <= emax:
                out[e] = out.get(e, 0) + v1 * mpf(v2)
    big = max((abs(v) for v in out.values()), default=0)
    return {e: v for e, v in out.items() if abs(v) > big * mp.mpf(10) ** (-(mp.mp.dps - 5))}


def theta_z(s, al, be, t):
    """exp(i pi (al^2 tau + 2 al be)) theta_s(be + al tau | tau), by mpmath's jtheta (the direct route)"""
    nome = mp.exp(1j * mp.pi * t)
    pref = mp.exp(1j * mp.pi * (mpf(al) ** 2 * t + 2 * mpf(al) * mpf(be)))
    return pref * mp.jtheta(s, mp.pi * (mpf(be) + mpf(al) * t), nome)


def dressing_direct(c, q, line, N, t):
    al, be, _, _ = char_of(c, q, line, N)
    s = S_OF[c]
    return (theta_z(s, al, be, t) / theta_z(s, Fr(0), Fr(0), t)) ** 2


def ev_scalar(ser, t):
    return mp.fsum(v * mp.exp(2j * mp.pi * mpf(e) * t) for e, v in ser.items())


# ------------------------------------------------------------------------------------------- lines and threads
def primitive_lines(N):
    """chat1-convention lines (la, lb), primitive mod N, one per sign class"""
    seen, out = set(), []
    for la, lb in itertools.product(range(N), repeat=2):
        if gcd(gcd(la, lb), N) != 1:
            continue
        if (la, lb) in seen:
            continue
        seen.add((la, lb)); seen.add(((-la) % N, (-lb) % N))
        out.append((la, lb))
    return out


def fixed_lines(n, N):
    """lines fixed up to sign by L R^n = (1, n, 1, n+1), with eps and c (chat1's pairing on (a, b) = (lb, la))"""
    A, Bm, C, D = 1, n, 1, n + 1
    out = []
    for la, lb in primitive_lines(N):
        a, b = lb, la
        wg = ((a * A + b * C) % N, (a * Bm + b * D) % N)
        if wg == (a % N, b % N):
            eps = 1
        elif wg == ((-a) % N, (-b) % N):
            eps = -1
        else:
            continue
        pair = a * (a * Bm + b * D) - b * (a * A + b * C)
        assert pair % N == 0
        out.append({"line": (la, lb), "eps": eps, "c": (pair // N) % N})
    return out


def mob(g, t):
    A, Bm, C, D = g
    return (A * t + Bm) / (C * t + D)


# ------------------------------------------------------------------------------------------- V1
def V1():
    mp.mp.dps = 60
    pts = (mp.mpc("0.13", "1.1"), mp.mpc("-0.4", "2.3"))
    worst, zeros, n, bad_zero = mp.mpf(0), 0, 0, 0
    sizes = []
    for N in NS:
        for line in primitive_lines(N):
            for q in range(1, N // 2 + 1):
                for c in range(3):
                    ser = dressing_series(c, q, line, N, EMAX)
                    sizes.append(len(ser))
                    for t in pts:
                        d = dressing_direct(c, q, line, N, t)
                        if is_odd(c, q, line, N):
                            zeros += 1
                            if abs(d) >= mp.mpf(10) ** -40 or ser:
                                bad_zero += 1
                            continue
                        err = abs(ev_scalar(ser, t) - d) / abs(d)
                        worst = max(worst, err)
                        n += 1
    return {"cases (series, point)": n, "identically zero (series, point)": zeros,
            "zero cases not zero on both routes": bad_zero, "worst relative": float(worst),
            "holds": bool(worst < mp.mpf(10) ** -40 and bad_zero == 0),
            "terms per series (min, max)": [min(sizes), max(sizes)]}


# ------------------------------------------------------------------------------------------- V2
def sigma_at(g, pts):
    C, D = g[2], g[3]
    out = {}
    for c in range(3):
        best = None
        for c2 in range(3):
            r = [theta_z(S_OF[c], Fr(0), Fr(0), mob(g, t)) ** 2
                 / ((C * t + D) * theta_z(S_OF[c2], Fr(0), Fr(0), t) ** 2) for t in pts]
            sp = abs(r[0] - r[1])
            if best is None or sp < best[0]:
                best = (sp, c2)
        out[c] = best[1]
    return out


def V2():
    mp.mp.dps = 45
    tally = {}
    worst_cov, worst_law, cases, skipped = mp.mpf(0), mp.mpf(0), 0, 0
    misses = []
    for N in NS:
        threads = 0
        for n in range(1, 3 * N * N + 1):
            fl = fixed_lines(n, N)
            if not fl:
                continue
            threads += 1
            g = (1, n, 1, n + 1)
            pts = [mp.mpc(-(n + 1), y0) for y0 in (mp.mpf(1), mp.mpf("0.8"))]
            sg = sigma_at(g, pts)
            for f in fl:
                for q in range(1, N // 2 + 1):
                    ratios = []
                    for c in range(3):
                        if is_odd(c, q, f["line"], N) or is_odd(sg[c], q, f["line"], N):
                            skipped += 1
                            continue
                        ratios.append([dressing_direct(c, q, f["line"], N, mob(g, t))
                                       / dressing_direct(sg[c], q, f["line"], N, t) for t in pts])
                    if not ratios:
                        continue
                    ref = ratios[0][0]
                    cov = max(abs(x - ref) for r in ratios for x in r)
                    law = mp.expjpi(2 * mp.mpf(f["eps"] * f["c"] * q * q) / N)
                    err = abs(ref - law)
                    worst_cov, worst_law = max(worst_cov, cov), max(worst_law, err)
                    cases += 1
                    key = f"N={N} eps={f['eps']:+d}"
                    tally[key] = tally.get(key, 0) + 1
                    if (cov > 1e-30 or err > 1e-30) and len(misses) < 10:
                        misses.append({"N": N, "n": n, "line": f["line"], "q": q, "cov": float(cov), "law": float(err)})
        tally[f"N={N} threads"] = threads
    return {"cases (thread, line, q)": cases, "tally": tally, "components skipped (odd)": skipped,
            "worst covariance spread": float(worst_cov), "worst |chi - exp(2 pi i eps c q^2 / N)|": float(worst_law),
            "misses (first 10)": misses, "holds": bool(worst_cov < 1e-30 and worst_law < 1e-30)}


# ------------------------------------------------------------------------------------------- the units (W72's)
def build_units():
    """W72's untwisted units, as chat1's build_forms.py builds them from this seat's code (forms part only)"""
    sys.path.insert(0, str(HERE))
    import the_surface_yukawa as SY
    RC = SY.RC
    mp.mp.dps = 40
    K32, K72, KM12 = Fr(3, 2), Fr(7, 2), Fr(-1, 2)
    resid = {}
    F32, FM12 = [], []
    for name, u in SY.MATTER:
        terms, r, _ = SY.best_section(u, K32); F32.append(SY.to_series(terms, SY.E8)); resid[f"{name} 3/2"] = r
        terms, r, _ = SY.best_section(u, KM12); FM12.append(SY.to_series(terms, SY.E8)); resid[f"{name} -1/2"] = r
    fbest = None
    for line in SY.LINES:
        terms, r = RC.solve((0, 0, 0), K72, line)
        if fbest is None or r < fbest[1]:
            fbest = (terms, r, line)
    fser = SY.to_series(fbest[0], SY.E8); resid["f 7/2"] = fbest[1]
    hb5 = hb9 = None
    for line in ("v+", "e_i", "v-"):
        terms, r = SY.solve_twisted(Fr(5, 2), line)
        if hb5 is None or r < hb5[1]:
            hb5 = (terms, r, line)
        terms, r = SY.solve_twisted(Fr(9, 2), line)
        if hb9 is None or r < hb9[1]:
            hb9 = (terms, r, line)
    h5, h9 = SY.to_series(hb5[0], SY.E8P), SY.to_series(hb9[0], SY.E8P)
    resid["h 5/2"], resid["h 9/2"] = hb5[1], hb9[1]
    CAP = SY.CAP8 // 8
    sig = lambda m, p: sum(d ** p for d in range(1, m + 1) if m % d == 0)
    E4 = {0: mp.mpf(1)}
    E4.update({8 * m: mp.mpf(240 * sig(m, 3)) for m in range(1, CAP + 1)})
    E4F = [SY.scal_vec(E4, F) for F in FM12]
    return {"F32": F32, "FM12": FM12, "E4F": E4F, "fser": fser, "h5": h5, "h9": h9, "resid": resid}


def to_comp(ser):
    """{(line, n8): a} -> {Fraction exponent: [a_i, a_j, a_k]}"""
    out = {}
    for (l, n8), a in ser.items():
        v = out.setdefault(Fr(n8, 8), [mp.mpc(0)] * 3)
        for k in range(3):
            if B[l][k] != 0:
                v[k] += a * mp.mpc(B[l][k])
    return out


def ev_comp(ser, t):
    out = [mp.mpc(0)] * 3
    for e, v in ser.items():
        z = mp.exp(2j * mp.pi * mpf(e) * t)
        out = [out[k] + v[k] * z for k in range(3)]
    return out


def dot(X, Y):
    return X[0] * Y[0] + X[1] * Y[1] + X[2] * Y[2]


def Gp(X, Y, v):
    a, b, c = dot(v, Y), dot(v, X), dot(X, Y)
    return [a * X[i] + b * Y[i] - c * v[i] for i in range(3)]


def neutral_R(t):
    """chat1's coupling at zero charge: -2 pi c_s theta_s(0)^2 / theta_1'(0), theta_1'(0) = 2 pi eta^3"""
    q = mp.exp(2j * mp.pi * t)
    d1 = 2 * mp.pi * (mp.exp(2j * mp.pi * t / 24) * mp.qp(q)) ** 3
    return [-2 * mp.pi * CQ[c] * theta_z(S_OF[c], Fr(0), Fr(0), t) ** 2 / d1 for c in range(3)]


def integrands(U, t, qs, line, N):
    """chat1's seven integrands for one sector at one point, the units dressed per field (factored evaluation)"""
    qL, qR, qH = qs
    y = t.imag
    Dd = {qq: [mp.mpc(0) if is_odd(c, qq, line, N) else dressing_direct(c, qq, line, N, t) for c in range(3)]
          for qq in set(qs)}
    dress = lambda vec, qq: [vec[c] * Dd[qq][c] for c in range(3)]
    L32 = [dress(ev_comp(F, t), qL) for F in U["F32c"]]
    R32 = [dress(ev_comp(F, t), qR) for F in U["F32c"]]
    LM = [dress(ev_comp(F, t), qL) for F in U["FM12c"]]
    R72 = [dress(ev_comp(F, t), qR) for F in U["E4Fc"] + [U["fc"]]]
    h5 = [x.conjugate() for x in dress(ev_comp(U["h5c"], t), qH)]
    h9 = [x.conjugate() for x in dress(ev_comp(U["h9c"], t), qH)]
    v = neutral_R(t)
    cj = lambda X: [x.conjugate() for x in X]
    return {
        "KL32": [[dot(L32[i], cj(L32[k])) * y ** 1.5 for k in range(3)] for i in range(3)],
        "KR32": [[dot(R32[i], cj(R32[k])) * y ** 1.5 for k in range(3)] for i in range(3)],
        "KLM12": [[dot(LM[i], cj(LM[k])) * y ** -0.5 for k in range(3)] for i in range(3)],
        "KR72": [[dot(R72[i], cj(R72[k])) * y ** 3.5 for k in range(4)] for i in range(4)],
        "Y1": [[dot(Gp(L32[i], R32[k], v), h5) * y ** 2.5 for k in range(3)] for i in range(3)],
        "Y2x": [[dot(Gp(L32[i], R72[k], v), h9) * y ** 4.5 for k in range(4)] for i in range(3)],
        "Y3x": [[dot(Gp(LM[i], R72[k], v), h5) * y ** 2.5 for k in range(4)] for i in range(3)]}


def V3(U):
    mp.mp.dps = 50
    rows, worst_law, worst_K, plus_ok = [], mp.mpf(0), mp.mpf(0), True
    for N in NS:
        found, n = 0, 0
        while found < 3:
            n += 1
            fl = fixed_lines(n, N)
            if not fl:
                continue
            found += 1
            g = (1, n, 1, n + 1)
            tr = n + 2
            rho = mp.sqrt(tr * tr - 4) / 2
            x0 = mp.mpf(1 - (n + 1)) / 2
            P = 2 * mp.acosh(mp.mpf(tr) / 2)
            t0 = x0 + rho * mp.mpc(mp.tanh(-P / 2), 1 / mp.cosh(P / 2))
            t1 = mob(g, t0)
            axis_end = x0 + rho * mp.mpc(mp.tanh(P / 2), 1 / mp.cosh(P / 2))
            for f in fl:
                for sec, (fl_, fr_, hh) in SECTORS.items():
                    qL, qR = SM[fl_], SM[fr_]
                    qH = SM["H"] if hh == "H" else -SM["H"]
                    I0 = integrands(U, t0, (qL, qR, qH), f["line"], N)
                    I1 = integrands(U, t1, (qL, qR, qH), f["line"], N)
                    chi = mp.expjpi(2 * mp.mpf(f["eps"] * f["c"] * (qL ** 2 + qR ** 2 - qH ** 2)) / N)
                    chi_plus = mp.expjpi(2 * mp.mpf(f["eps"] * f["c"] * (qL ** 2 + qR ** 2 + qH ** 2)) / N)
                    row = {"N": N, "n": n, "line": f["line"], "eps": f["eps"], "c": f["c"], "sector": sec,
                           "|g tau0 - tau(P/2)|": float(abs(t1 - axis_end)), "Im tau0": float(t0.imag)}
                    for key in I0:
                        A0, A1 = I0[key], I1[key]
                        den = max(abs(x) for r in A0 for x in r)
                        if den == 0:
                            row[key] = None
                            continue
                        target = 1 if key.startswith("K") else chi
                        err = max(abs(A1[i][k] - target * A0[i][k]) for i in range(len(A0)) for k in range(len(A0[0])))
                        err = err / den
                        row[key] = float(err)
                        if key.startswith("K"):
                            worst_K = max(worst_K, err)
                        else:
                            worst_law = max(worst_law, err)
                            errp = max(abs(A1[i][k] - chi_plus * A0[i][k])
                                       for i in range(len(A0)) for k in range(len(A0[0]))) / den
                            differs = (f["c"] * 2 * qH * qH) % N != 0
                            row[key + " (+q_H^2 law)"] = float(errp)
                            if differs and errp <= 1e-3:
                                plus_ok = False
                    row["closes"] = bool((f["c"] * (qL ** 2 + qR ** 2 - qH ** 2)) % N == 0)
                    rows.append(row)
    return {"rows": rows, "worst Y vs the per-field law": float(worst_law), "worst K": float(worst_K),
            "the +q_H^2 law misses wherever it differs": plus_ok,
            "holds": bool(worst_law < 1e-25 and worst_K < 1e-25 and plus_ok)}


# ------------------------------------------------------------------------------------------- V4
def V4():
    found = []
    for N in NS:
        for line in primitive_lines(N):
            for q in range(1, N // 2 + 1):
                for c in range(3):
                    if is_odd(c, q, line, N):
                        found.append((N, line, q, COMP[c]))
    predicted = []
    for line in primitive_lines(12):
        la, lb = line
        comp = "i" if (la % 2, lb % 2) == (1, 0) else ("j" if (la % 2, lb % 2) == (0, 1) else "k")
        predicted.append((12, line, 6, comp))
    return {"zero components (N, line, q, component)": len(found), "as predicted": sorted(found) == sorted(predicted),
            "N with zeros": sorted({x[0] for x in found}), "q with zeros": sorted({x[2] for x in found}),
            "holds": sorted(found) == sorted(predicted)}


# ------------------------------------------------------------------------------------------- V6
def V6():
    mp.mp.dps = 50
    t = mp.mpc("0.17", "1.3")
    worst, n = mp.mpf(0), 0
    for N in NS:
        for line in primitive_lines(N):
            la, lb = line
            ch = lambda k: (Fr(k * lb, N), Fr(k * la, N))
            for sec, (fl_, fr_, _) in SECTORS.items():
                qL, qR = SM[fl_], SM[fr_]
                for c in range(3):
                    s = S_OF[c]
                    T = lambda k, ss=s: theta_z(ss, *ch(k), t)
                    lhs = T(qL + qR) * T(qL - qR) * T(0) ** 2
                    odd = theta_z(1, *ch(qL), t) ** 2 * theta_z(1, *ch(qR), t) ** 2
                    rhs = T(qL) ** 2 * T(qR) ** 2 + EPS_RIEMANN[c] * odd
                    scale = max(abs(lhs), abs(T(qL) ** 2 * T(qR) ** 2))
                    worst = max(worst, abs(lhs - rhs) / scale)
                    n += 1
    return {"cases": n, "worst relative": float(worst), "eps on (i, j, k)": list(EPS_RIEMANN),
            "holds": bool(worst < mp.mpf(10) ** -40)}


# ------------------------------------------------------------------------------------------- V7
def mul_comp_scalar(X, D, emax):
    out = {}
    for e1, v in X.items():
        for e2, d in D.items():
            e = e1 + e2
            if e <= emax:
                w = out.setdefault(e, [mp.mpc(0)] * 3)
                for k in range(3):
                    w[k] += v[k] * d
    return out


def dress_series(Xc, q, line, N, emax=EMAX):
    """the product series of a component-form unit and its dressing, exponents <= emax"""
    out = {}
    for c in range(3):
        D = dressing_series(c, q, line, N, emax + 1)
        for e1, v in Xc.items():
            if v[c] == 0:
                continue
            for e2, d in D.items():
                e = e1 + e2
                if e <= emax:
                    w = out.setdefault(e, [mp.mpc(0)] * 3)
                    w[c] += v[c] * d
    return out


def serre_comp(X, k, emax):
    sig = lambda m: sum(d for d in range(1, m + 1) if m % d == 0)
    E2 = {Fr(0): mp.mpf(1)}
    E2.update({Fr(m): mp.mpf(-24 * sig(m)) for m in range(1, int(emax) + 2)})
    D = {e: [mpf(e) * x for x in v] for e, v in X.items()}
    E2X = mul_comp_scalar(X, E2, emax)
    out = {}
    for e in set(D) | set(E2X):
        a = D.get(e, [0, 0, 0]); b = E2X.get(e, [0, 0, 0])
        out[e] = [a[i] - mpf(k) / 12 * b[i] for i in range(3)]
    return out


def V7(U):
    mp.mp.dps = 50
    pts = (mp.mpc("0.1", "1.2"), mp.mpc("-0.3", "1.0"), mp.mpc("0.25", "1.6"))
    E4ser = {Fr(0): mp.mpf(1)}
    sig3 = lambda m: sum(d ** 3 for d in range(1, m + 1) if m % d == 0)
    E4ser.update({Fr(m): mp.mpf(240 * sig3(m)) for m in range(1, EMAX + 2)})
    rows, worst_control, min_twisted = [], None, None
    cases = [(9, 0, (0, 1))]
    for N in NS:
        qs = sorted({min(abs(x) % N, N - abs(x) % N) for x in SM.values()} - {0})
        for line in ((0, 1), (1, 1)):
            for q in qs:
                cases.append((N, q, line))
    for N, q, line in cases:
        worst_j = 0.0
        fq = dress_series(U["fc"], q, line, N) if q else U["fc"]
        for j in range(3):
            F = U["FM12c"][j]
            Fq = dress_series(F, q, line, N) if q else F
            th2 = serre_comp(serre_comp(Fq, Fr(-1, 2), EMAX), Fr(3, 2), EMAX)
            E4Fq = mul_comp_scalar(Fq, E4ser, EMAX)
            A, bvec = [], []
            for t in pts:
                lhs = ev_comp(th2, t); x1 = ev_comp(E4Fq, t); x2 = ev_comp(fq, t)
                for k in range(3):
                    A.append([x1[k], x2[k]]); bvec.append(lhs[k])
            Am, bm = mp.matrix(A), mp.matrix(bvec)
            Q, Rm = mp.qr(Am, mode="skinny")
            sol = mp.lu_solve(Rm, Q.H * bm)
            res = mp.norm(Am * sol - bm) / mp.norm(bm)
            worst_j = max(worst_j, float(res))
        rows.append({"N": N, "q": q, "line": line, "relative residual (worst unit)": worst_j})
        if q == 0:
            worst_control = worst_j
        else:
            min_twisted = worst_j if min_twisted is None else min(min_twisted, worst_j)
    return {"rows": rows, "control (q = 0)": worst_control, "smallest twisted residual": min_twisted,
            "holds": bool(worst_control < 1e-25 and min_twisted > 1e-3)}


# ------------------------------------------------------------------------------------------- V8
def load_chat1():
    src = subprocess.run(["git", "-C", str(REPO), "show", f"{CHAT1_COMMIT}:{CHAT1_PATH}"], check=True,
                         capture_output=True, text=True).stdout
    tmp = Path(tempfile.mkdtemp(prefix="w92_chat1_"))
    (tmp / "units_cells.py").write_text(src)
    spec = importlib.util.spec_from_file_location("units_cells_chat1", tmp / "units_cells.py")
    UC = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(UC)
    return UC


def V8(UC):
    import flint
    from flint import arb, acb
    flint.ctx.prec = 400
    sys.path.insert(0, str(HERE))
    import the_twisted_coupling_vector as W91                   # sets mp.mp.dps = 60 on import
    mp.mp.dps = 60
    pts = (mp.mpc("0.11", "1.05"), mp.mpc("-0.35", "1.7"))
    worst_spread, worst_closed, n = mp.mpf(0), mp.mpf(0), 0
    for N in NS:
        for line in primitive_lines(N):
            la, lb = line
            for sec, (fl_, fr_, _) in SECTORS.items():
                qL, qR = SM[fl_], SM[fr_]
                ku, kd = qL + qR, qL - qR
                psi = (Fr(lb, N), Fr(-la, N))
                consts = []
                for t in pts:
                    ta = acb(arb(mp.nstr(t.real, 60)), arb(mp.nstr(t.imag, 60)))
                    ub = (arb(ku * lb) / N, arb(ku * la) / N)
                    de = (arb(kd * lb) / N, arb(kd * la) / N)
                    vals = [-2 * acb.pi() * x for x in UC.quat3(ta, ub, de, UC.th1p(ta))]
                    vals = [mp.mpc(mp.mpf(x.real.mid().str(55, radius=False)),
                                   mp.mpf(x.imag.mid().str(55, radius=False))) for x in vals]
                    V = W91.V_direct(ku, kd, psi, t)
                    consts += [vals[c] / V[COMP[c]] for c in range(3)]
                ref = consts[0]
                worst_spread = max(worst_spread, max(abs(x - ref) / abs(ref) for x in consts))
                closed = -2 * mp.pi * mp.expjpi(-2 * mp.mpf((ku * ku + kd * kd) * lb * (-la)) / (N * N))
                worst_closed = max(worst_closed, abs(ref - closed) / abs(closed))
                n += 1
    return {"cases (line, sector)": n, "worst spread of the constant": float(worst_spread),
            "the constant vs -2 pi exp(-2 pi i (ku^2 + kd^2) psi1 psi2) (read-out)": float(worst_closed),
            "holds": bool(worst_spread < 1e-30)}


# ------------------------------------------------------------------------------------------- the source for chat1
class PerFieldSource:
    """A drop-in for chat1's UnitSource (units_cells.py): the per-field reading. Pass chat1's forms dict P and its
    module UC. units and higgs return dressed series in UC's prepared form; coupling returns the neutral R;
    completion_beta returns None (THETA2 does not apply to dressed units, W92's V7). The charge is used as given:
    D(-q) = D(q) exactly, and D(q + N) = exp(4 pi i q lb la / N) D(q), one phase on every component, which no
    singular value or norm depends on."""

    def __init__(self, P, UC, round53=False):
        self.UC, self.round53, self.cache = UC, round53, {}
        e8 = lambda ser: {(l, n8): a for (l, n8), a in ser.items()}
        self.raw = {"3/2": [to_comp(e8(s)) for s in P["F32"]], "-1/2": [to_comp(e8(s)) for s in P["FM12"]],
                    "7/2": [to_comp(e8(s)) for s in P["E4F"] + [P["fser"]]],
                    "5/2": [to_comp(e8(P["h5"]))], "9/2": [to_comp(e8(P["h9"]))]}

    def _prep(self, ser):
        UC = self.UC
        out = {}
        for e, v in ser.items():
            out[e] = [UC.to_acb(complex(x) if self.round53 else x, self.round53) for x in v]
        return out

    def _dressed(self, weight, charge, line, N):
        q = charge                       # as given: q + N changes D by exp(4 pi i q lb la / N) on every component
        key = (weight, q, tuple(line), N)
        if key not in self.cache:
            mp.mp.dps = 50
            sers = [dress_series(X, q, line, N) if q else X for X in self.raw[weight]]
            self.cache[key] = [self._prep(s) for s in sers]
        return self.cache[key]

    def units(self, field, weight, charge, line, N):
        return self._dressed(weight, charge, line, N)

    def higgs(self, weight, charge, line, N):
        return self._dressed(weight, charge, line, N)[0]

    def coupling(self, tau, qL, qR, line, N, d1):
        UC = self.UC
        z = (UC.arb(0), UC.arb(0))
        return [-2 * UC.acb.pi() * x for x in UC.quat3(tau, z, z, d1)]

    def completion_beta(self, field, charge, line, N):
        return None


def dressing_at(tau, charge, line, N, UC):
    """the dressing's three components at an acb point, by chat1's own Tc and theta (factored evaluation)"""
    la, lb = line
    al, be = UC.arb(charge * lb) / N, UC.arb(charge * la) / N
    return [(UC.Tc(s, al, be, tau) / UC.theta(s, UC.acb(0), tau)) ** 2 for s in S_OF]


# ------------------------------------------------------------------------------------------- delivery and read-outs
def delivery():
    conv = ("chat1's line (la, lb), w = (la + lb tau)/N; (al, be) = (q lb/N, q la/N); components (i, j, k) <-> "
            "theta (2, 4, 3); numerator [z-form theta_s(q w)]^2 = sum count * exp(2 pi i turns) q^exponent; "
            "D_c = numerator * inverse_thetanull_sq[c]; q = e^{2 pi i tau}; D(-q) = D(q); "
            "D(q + N) = exp(4 pi i q lb la / N) D(q) on every component")
    inv = {COMP[c]: [[str(e), str(v)] for e, v in sorted(inverse_thetanull_sq(c, EMAX_DELIVERY + 2).items())]
           for c in range(3)}
    data = {"convention": conv, "emax": EMAX_DELIVERY, "inverse_thetanull_sq": inv,
            "numerators": {}}
    for N in NS:
        dN = data["numerators"][str(N)] = {}
        for line in primitive_lines(N):
            dl = dN[f"{line[0]},{line[1]}"] = {}
            for q in range(0, N // 2 + 1):
                dq = dl[str(q)] = {}
                for c in range(3):
                    if is_odd(c, q, line, N):
                        dq[COMP[c]] = "zero (odd characteristic)"
                        continue
                    num = numerator_exact(c, q, line, N, EMAX_DELIVERY + Fr(5, 4))
                    dq[COMP[c]] = [[str(e), str(t), k] for e, d in sorted(num.items()) for t, k in sorted(d.items())]
    with gzip.open(DELIVERY, "wt", encoding="utf-8") as fh:
        json.dump(data, fh)
    return {"file": DELIVERY.name, "bytes": DELIVERY.stat().st_size}


def readouts(U):
    mp.mp.dps = 50
    out = {}
    for N in NS:
        for field, q in SM.items():
            line = (0, 1)
            row = {}
            for name, X in (("F 3/2", U["F32c"]), ("F -1/2", U["FM12c"])):
                lows = []
                for j, F in enumerate(X):
                    ser = dress_series(F, q, line, N)
                    lows.append([str(min((e for e, v in ser.items() if abs(v[c]) > 1e-30), default="none"))
                                 for c in range(3)])
                row[name] = lows
            out[f"N={N} {field} (q={q})"] = row
    return out


def main():
    t0 = time.time()
    out = {"rule": "W92_RULE.md", "status": "one run"}
    out["V1"] = V1(); print("V1", out["V1"]["holds"], round(time.time() - t0, 1), flush=True)
    out["V4"] = V4(); print("V4", out["V4"]["holds"], round(time.time() - t0, 1), flush=True)
    out["V6"] = V6(); print("V6", out["V6"]["holds"], round(time.time() - t0, 1), flush=True)
    UC = load_chat1()
    out["V8"] = V8(UC); print("V8", out["V8"]["holds"], round(time.time() - t0, 1), flush=True)
    out["V2"] = V2(); print("V2", out["V2"]["holds"], round(time.time() - t0, 1), flush=True)
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    U = build_units()
    out["units' collocation residuals"] = U["resid"]
    U.update({"F32c": [to_comp(s) for s in U["F32"]], "FM12c": [to_comp(s) for s in U["FM12"]],
              "E4Fc": [to_comp(s) for s in U["E4F"]], "fc": to_comp(U["fser"]), "h5c": to_comp(U["h5"]),
              "h9c": to_comp(U["h9"])})
    print("units built", round(time.time() - t0, 1), flush=True)
    out["V3"] = V3(U); print("V3", out["V3"]["holds"], round(time.time() - t0, 1), flush=True)
    out["V7"] = V7(U); print("V7", out["V7"]["holds"], round(time.time() - t0, 1), flush=True)
    out["read-out: lowest exponents of the dressed units, line (0, 1)"] = readouts(U)
    out["delivery"] = delivery()
    out["seconds"] = round(time.time() - t0, 1)
    out["all cells hold"] = all(out[k]["holds"] for k in ("V1", "V2", "V3", "V4", "V6", "V7", "V8"))
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    print("all cells hold", out["all cells hold"], "seconds", out["seconds"], flush=True)


if __name__ == "__main__":
    main()
