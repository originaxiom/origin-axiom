"""EXPLORATION (unsealed, excluded orders only): the twisted thread-frame cells on deep threads, in ball arithmetic.

The minimal reading (B1656's twisted coupling vector in place of R; matter and Higgs modes untwisted), in W72's and
THETA2's cells, as twisted_explore.py computes them, but:
  - every form is evaluated at the UNREDUCED point of the thread's period (the q-series converge there: on the period
    centred at the top of the axis, Im tau >= rho sech(P/2) ~ 2 rho / tr), so no reduction or transport is needed;
  - arithmetic is arb/acb (python-flint) at a working precision set by the top of the arc, so the cancellation that
    broke double precision at y ~ 13 is carried with rigorous error radii.
Questions: (1) does Y stay polynomial in the height while K grows as W84's law (the cusp criterion: a term
q^p conj(q^p') grows only if p < 0 and p' < 0; h5 and h9 have no negative exponent)? (2) are the light/heavy ratios'
exponents the same in every sector? Orders 3, 5 and 7 only (each excluded: up = down at 3, down = leptons at 5,
up = leptons at 7). No N = 9, 11 or 12 quantity is computed.

Usage: python3 deep_cusp.py <forms.pkl> <theta2_completion.json> [mode]
"""
import json, math, pickle, sys, time
import flint
from flint import arb, acb
import mpmath as mp

t0 = time.time()
P = pickle.load(open(sys.argv[1], "rb"))
T2 = json.loads(open(sys.argv[2]).read())["per thread"]
MODE = sys.argv[3] if len(sys.argv) > 3 else "all"

B = {"e_i": (1, 0, 0), "v+": (0, 1, -1j), "v-": (0, 1, 1j)}


def to_acb(z):
    z = mp.mpc(z)
    return acb(arb(mp.nstr(z.real, 60)), arb(mp.nstr(z.imag, 60)))


def prep(series):
    """{n8: [c0, c1, c2]} with the line vectors folded in"""
    out = {}
    for (l, n8), a in series.items():
        v = out.setdefault(n8, [acb(0), acb(0), acb(0)])
        for c in range(3):
            if B[l][c] != 0:
                v[c] += to_acb(a) * acb(B[l][c].real, B[l][c].imag)
    return out


def setup_forms():
    S = {}
    S["F32"] = [prep(s) for s in P["F32"]]
    S["FM12"] = [prep(s) for s in P["FM12"]]
    S["RB"] = [prep(s) for s in P["E4F"] + [P["fser"]]]
    S["R"], S["h5"], S["h9"] = prep(P["Rser"]), prep(P["h5"]), prep(P["h9"])
    return S


def ev(ser, pw):
    v = [acb(0), acb(0), acb(0)]
    for n8, c in ser.items():
        p = pw[n8]
        v[0] += c[0] * p; v[1] += c[1] * p; v[2] += c[2] * p
    return v


KMAX = 40
def E(x):
    return (acb.pi() * acb(0, 1) * x).exp()


def theta(n, z, tau):
    s = acb(0)
    for k in range(-KMAX, KMAX + 1):
        if n == 3:
            s += E(k * k * tau + 2 * k * z)
        elif n == 4:
            s += (-1) ** (k % 2) * E(k * k * tau + 2 * k * z)
        else:
            h = arb(k) + arb(0.5)
            t = E(h * h * tau + 2 * h * z)
            s += t if n == 2 else acb(0, -1) * (-1) ** (k % 2) * t
    return s


def th1p(tau):
    s = acb(0)
    for k in range(-KMAX, KMAX + 1):
        h = arb(k) + arb(0.5)
        s += 2 * acb.pi() * (-1) ** (k % 2) * h * E(h * h * tau)
    return s


def Tc(n, al, be, tau):
    return E(al * al * tau + 2 * al * be) * theta(n, be + al * tau, tau)


CHS = [(2, acb(-1)), (4, acb(-1)), (3, acb(0, 1))]   # channels i, j, k


def quat3(tau, ub, de, d):
    return [c * Tc(n, ub[0], ub[1], tau) * Tc(n, de[0], de[1], tau) / d for n, c in CHS]


def dot(X, Y):
    return X[0] * Y[0] + X[1] * Y[1] + X[2] * Y[2]


def Gp(X, Y, v):
    a, b, c = dot(v, Y), dot(v, X), dot(X, Y)
    return [a * X[i] + b * Y[i] - c * v[i] for i in range(3)]


def conjv(X):
    return [x.conjugate() for x in X]


def matrix(word):
    M = [[1, 0], [0, 1]]
    for ch in word:
        G = [[1, 0], [1, 1]] if ch == "L" else [[1, 1], [0, 1]]
        M = [[M[0][0] * G[0][0] + M[0][1] * G[1][0], M[0][0] * G[0][1] + M[0][1] * G[1][1]],
             [M[1][0] * G[0][0] + M[1][1] * G[1][0], M[1][0] * G[0][1] + M[1][1] * G[1][1]]]
    return M


SECTORS = {"zero": (0, 0), "up": (1, -4), "down": (1, 2), "lepton": (-3, 6)}


def run(word, Npts, line, Nord, sectors, S):
    best = None
    for k in range(len(word)):
        rot = word[k:] + word[:k]; M = matrix(rot)
        if best is None or abs(M[1][0]) < abs(best[1][1][0]):
            best = (rot, M)
    rot, M = best
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]; tr = a + d
    rho = math.sqrt(tr * tr - 4) / (2 * abs(c))
    bits = int(2 * math.pi * 2.0 * rho / math.log(2)) + 260
    flint.ctx.prec = bits
    x0 = arb(a - d) / (2 * c); rhoA = (arb(tr * tr - 4)).sqrt() / (2 * abs(c))
    PlA = 2 * (arb(tr) / 2).acosh()
    la, lb = line
    chars = {}
    for sec in sectors:
        qL, qR = SECTORS[sec]
        chars[sec] = ((arb((qL + qR) * lb) / Nord, arb((qL + qR) * la) / Nord),
                      (arb((qL - qR) * lb) / Nord, arb((qL - qR) * la) / Nord))
    acc = {sec: {} for sec in sectors}
    nmin = min(min(s) for grp in ("F32", "FM12", "RB") for s in S[grp])
    nmax = max(max(s) for grp in ("F32", "FM12", "RB") for s in S[grp])
    nmax = max(nmax, max(S["h5"]), max(S["h9"]), max(S["R"]))
    rcheck = arb(0)
    ymin = None
    first = {}
    for j in range(Npts):
        s = -PlA / 2 + PlA * j / Npts
        tau = x0 + rhoA * acb(s.tanh(), 1 / s.cosh())
        y = tau.imag
        ymin = y if ymin is None or y < ymin else ymin
        q8 = (2 * acb.pi() * acb(0, 1) * tau / 8).exp(); q8i = 1 / q8
        pw = {0: acb(1)}
        for n in range(1, nmax + 1): pw[n] = pw[n - 1] * q8
        for n in range(1, -nmin + 1): pw[-n] = pw[-n + 1] * q8i
        a32 = [ev(f, pw) for f in S["F32"]]; am = [ev(f, pw) for f in S["FM12"]]; ar = [ev(f, pw) for f in S["RB"]]
        h5c, h9c = conjv(ev(S["h5"], pw)), conjv(ev(S["h9"], pw))
        y15, ym05, y35, y25, y45 = y ** 1.5, y ** -0.5, y ** 3.5, y ** 2.5, y ** 4.5
        d1 = th1p(tau)
        base = {}
        base["K32"] = [[dot(a32[i], conjv(a32[k])) * y15 for k in range(3)] for i in range(3)]
        base["KM12"] = [[dot(am[i], conjv(am[k])) * ym05 for k in range(3)] for i in range(3)]
        base["K72"] = [[dot(ar[i], conjv(ar[k])) * y35 for k in range(4)] for i in range(4)]
        if j % max(1, Npts // 8) == 0:
            Rv = ev(S["R"], pw); u0 = quat3(tau, (0, 0), (0, 0), d1)
            for cch in range(3):
                rr = abs(-2 * acb.pi() * u0[cch] - Rv[cch]) / (abs(Rv[0]) + abs(Rv[1]) + abs(Rv[2]))
                rcheck = rr if rr > rcheck else rcheck
        for sec in sectors:
            ub, de = chars[sec]
            v = [-2 * acb.pi() * x for x in quat3(tau, ub, de, d1)]
            A = acc[sec]
            vals = dict(base)
            vals["Y1"] = [[dot(Gp(a32[i], a32[k], v), h5c) * y25 for k in range(3)] for i in range(3)]
            vals["Y2x"] = [[dot(Gp(a32[i], ar[k], v), h9c) * y45 for k in range(4)] for i in range(3)]
            vals["Y3x"] = [[dot(Gp(am[i], ar[k], v), h5c) * y25 for k in range(4)] for i in range(3)]
            if j == 0:
                first[sec] = vals["Y1"]
            for key, Mv in vals.items():
                if key not in A:
                    A[key] = [[acb(0)] * len(Mv[0]) for _ in Mv]
                for i in range(len(Mv)):
                    for k in range(len(Mv[0])):
                        A[key][i][k] += Mv[i][k]
    # closure: the integrand at s = +P/2 (one period on) against s = -P/2 (the first node)
    s = PlA / 2
    tau = x0 + rhoA * acb(s.tanh(), 1 / s.cosh()); y = tau.imag
    q8 = (2 * acb.pi() * acb(0, 1) * tau / 8).exp(); q8i = 1 / q8
    pw = {0: acb(1)}
    for n in range(1, nmax + 1): pw[n] = pw[n - 1] * q8
    for n in range(1, -nmin + 1): pw[-n] = pw[-n + 1] * q8i
    a32 = [ev(f, pw) for f in S["F32"]]; h5c = conjv(ev(S["h5"], pw)); d1 = th1p(tau)
    clos = {}
    for sec in sectors:
        ub, de = chars[sec]
        v = [-2 * acb.pi() * x for x in quat3(tau, ub, de, d1)]
        endv = [[dot(Gp(a32[i], a32[k], v), h5c) * y ** 2.5 for k in range(3)] for i in range(3)]
        st = first[sec]
        num = max(float(abs(endv[i][k] - st[i][k]).mid()) for i in range(3) for k in range(3))
        den = max(float(abs(st[i][k]).mid()) for i in range(3) for k in range(3))
        clos[sec] = num / den
    w = PlA / Npts
    for sec in sectors:
        for key in acc[sec]:
            acc[sec][key] = [[x * w for x in row] for row in acc[sec][key]]
    return {"rot": rot, "rho": rho, "bits": bits, "ymin": float(ymin.mid()), "rcheck": float(rcheck.mid()),
            "closure": clos, "acc": acc}


def to_mp(Mx):
    nd = mp.mp.dps + 10
    return mp.matrix([[mp.mpc(mp.mpf(x.real.mid().str(nd, radius=False)), mp.mpf(x.imag.mid().str(nd, radius=False)))
                       for x in row] for row in Mx])


def maxrad(Mx):
    return max(float(x.real.rad()) + float(x.imag.rad()) for row in Mx for x in row)


def inv_sqrt(K):
    E_, U = mp.eighe(K)
    ev_ = [E_[i] for i in range(E_.rows)]
    if min(ev_) <= 0: return None
    D = mp.diag([e ** -0.5 for e in ev_])
    return U * D * U.transpose_conj()


def cells(acc, beta):
    res = {}
    for cell, comp in [("C1", None), ("C2", "E4"), ("C2", "THETA2"), ("C2", "ORTH"), ("C3", "E4"), ("C3", "THETA2"),
                       ("C3", "ORTH")]:
        name = cell if comp is None else f"{cell}/{comp}"
        if cell == "C1":
            KL, Y, KR = to_mp(acc["K32"]), to_mp(acc["Y1"]), to_mp(acc["K32"])
        else:
            Kx = to_mp(acc["K72"])
            if comp == "E4": cc = [0, 0, 0]
            elif comp == "THETA2": cc = [mp.mpc(b_) for b_ in beta]
            else: cc = [-Kx[i, 3] / Kx[3, 3] for i in range(3)]
            P3 = mp.matrix(3, 4)
            for i in range(3): P3[i, i] = 1; P3[i, 3] = cc[i]
            KR = P3 * Kx * P3.transpose_conj()
            if cell == "C2": KL, Y = to_mp(acc["K32"]), to_mp(acc["Y2x"]) * P3.T
            else: KL, Y = to_mp(acc["KM12"]), to_mp(acc["Y3x"]) * P3.T
        A_, B_ = inv_sqrt(KL), inv_sqrt(KR)
        if A_ is None or B_ is None:
            res[name] = None; continue
        Mx = A_ * Y * B_.T
        Sv = mp.svd_c(Mx, compute_uv=False)
        sv = sorted([abs(Sv[i]) for i in range(Sv.rows)], reverse=True)
        res[name] = {"s": sv, "Ymax": max(abs(Y[i, k]) for i in range(Y.rows) for k in range(Y.cols)),
                     "Kdiag": [KL[i, i] for i in range(KL.rows)]}
    return res


if __name__ == "__main__":
    flint.ctx.prec = 800          # parse the solve's coefficients at full precision (not the 53-bit default)
    S = setup_forms()
    beta = P["beta"]
    print("forms prepared", round(time.time() - t0, 1), flush=True)
    jobs = []
    if MODE in ("all", "validate"):
        jobs += [("L" + "R" * n, 256, (0, 1), 5, ["zero"]) for n in range(1, 8)]
    if MODE in ("all", "deep"):
        jobs += [("L" + "R" * 9, 0, (0, 1), 3, list(SECTORS)), ("L" + "R" * 18, 0, (0, 1), 3, list(SECTORS)),
                 ("L" + "R" * 27, 0, (0, 1), 3, list(SECTORS)), ("L" + "R" * 25, 0, (0, 1), 5, list(SECTORS)),
                 ("L" + "R" * 50, 0, (0, 1), 5, list(SECTORS)), ("L" + "R" * 49, 0, (0, 1), 7, list(SECTORS))]
    if MODE == "conv":
        jobs += [("L" + "R" * 25, -1, (0, 1), 5, ["up", "zero"])]
    report = {}
    for word, Npts, line, Nord, secs in jobs:
        tr = word.count("R") + 2
        rho = math.sqrt(tr * tr - 4) / 2
        if Npts == 0:
            Npts = int(2 * math.acosh(tr / 2) * (2 * math.pi * 1.0 * rho + 60)) // 4 * 4
        runs = [Npts, int(Npts * 1.25) // 4 * 4] if Npts > 0 else [600, 800]
        if Npts == -1: runs = [400, 600, 800]
        outs = []
        for npt in runs:
            r = run(word, npt, line, Nord, secs, S)
            outs.append((npt, r))
            print(f"{word[:4]}..(n={word.count('R')}) N={Nord} Npts={npt} bits={r['bits']} rho={r['rho']:.3f} "
                  f"ymin={r['ymin']:.3f} Rcheck={r['rcheck']:.1e}  t={time.time() - t0:.0f}s", flush=True)
        npt, r = outs[-1]
        rprev = outs[-2][1]
        mp.mp.dps = r["bits"] // 3
        key = f"{word} N={Nord}"
        report[key] = {"rho": r["rho"], "Npts": [o[0] for o in outs]}
        for sec in secs:
            cs, csp = cells(r["acc"][sec], beta), cells(rprev["acc"][sec], beta)
            rad = max(maxrad(r["acc"][sec][k]) for k in r["acc"][sec])
            line_out = {}
            for name in cs:
                if cs[name] is None:
                    line_out[name] = None; continue
                s, sp = cs[name]["s"], csp[name]["s"]
                conv = float(max(abs(mp.log(s[i] / sp[i])) for i in range(len(s)) if s[i] > 0 and sp[i] > 0))
                line_out[name] = {"ln s2/s1": float(mp.log(s[1] / s[0])), "ln s3/s1": float(mp.log(s[2] / s[0])),
                                  "ln max|Y|": float(mp.log(cs[name]["Ymax"])),
                                  "ln K diag": [float(mp.log(abs(x))) for x in cs[name]["Kdiag"]],
                                  "conv (ln, Npts vs 0.8 Npts)": conv}
            report[key][sec] = {"max ball radius": rad, "cells": line_out}
            report[key][sec]["closure (Y1 integrand, one period on)"] = r["closure"][sec]
            if word in T2 and sec == "zero":
                for name, k2 in (("C2/E4", "H-E4 C2"), ("C3/E4", "H-E4 C3"), ("C3/THETA2", "H-THETA2 C3"),
                                 ("C2/THETA2", "H-THETA2 C2")):
                    s = cs[name]["s"]
                    report[key][sec].setdefault("vs THETA2 m2/m3", {})[name] = (float(s[1] / s[0]), T2[word][k2]["m2/m3"])
            print(json.dumps({key + " " + sec: report[key][sec]}, default=float)[:3000], flush=True)
    json.dump(report, open("deep_cusp_" + MODE + ".json", "w"), indent=1, default=float)
    print("seconds", round(time.time() - t0, 1))
