"""W87: B1654's section 1 checked against C0 on this seat's own code. The rule (W87_RULE.md) was committed before this
script (3274265c1); the derivations, predictions and priors are there.

  C1  the channel norms: c_r = -2 pi ln((pi/2)|theta_r(0)|^2) (route A, 60 digits), against the Parseval series before
      Euler's and Gauss's identities (route C, 60 digits) and a polar quadrature of the definition (route B, numpy)
  C2  D in closed form through lambda = theta_2^4 / theta_3^4: D = -theta_3^4 h(lambda) / (4 pi eta^6),
      |D|/|R|^2 = pi |h| / (1 + |lambda| + |1 - lambda|); its zeros, tau = i, the cusp with its next order, the grid
  C3  the end conditions as one family u_r = G(2 pi L + c_r) R_r: P4, P4'' and P4'; the shape D for G' != 0; the
      cutoff-free family e^{beta x}
  C4  B1654's item 10: det Y(a; u) = (a.a)(u.u)(a.u), and the limit of L s3/s1 under P4

The thetas are W85's series at 60 digits (`the_b1651_cells_checked.py`), in the pi z convention. B1654's z has periods
1 and tau, so w = pi z, and theta_1'(0) in z is 2 pi eta^3. Units (i, j, k) <-> channels (2, 4, 3), as B1651 and B1654.

Run: python3 the_boundary_class_norms_checked.py  ->  the_boundary_class_norms_checked.json beside it.
"""
import json
import random
from pathlib import Path

import mpmath as mp
import numpy as np

import the_b1651_cells_checked as W85

mp.mp.dps = 60
HERE = Path(__file__).resolve().parent
OUT = HERE / "the_boundary_class_norms_checked.json"
I = mp.mpc(0, 1)
CH = [2, 4, 3]
TIGHT = mp.mpf(10) ** -40
OMEGA = mp.mpc(-0.5, mp.sqrt(3) / 2)
K = 8 * mp.pi * (1 - 4 * mp.log(2))


def fl(x):
    return float(x)


def cx(x):
    return [float(mp.re(x)), float(mp.im(x))]


def fibres():
    rng = random.Random(87)
    out = [("i", mp.mpc(0, 1)), ("omega", OMEGA), ("2i", mp.mpc(0, 2)), ("3i", mp.mpc(0, 3))]
    k = 0
    while len(out) < 12:
        x, y = rng.uniform(-0.5, 0.5), rng.uniform(0.9, 2.5)
        if x * x + y * y >= 1:
            k += 1
            out.append((f"t{k}", mp.mpc(x, y)))
    return out


def consts(t):
    """theta_r(0) for r = 2, 3, 4; eta^3; the residue triplet R (units i, j, k)"""
    th = W85.thetas(mp.mpc(0), t)
    e3 = W85.theta1_prime0(t) / 2
    th0 = {2: th[1], 3: th[2], 4: th[3]}
    R = [-th0[2] ** 2 / (2 * mp.pi * e3), -th0[4] ** 2 / (2 * mp.pi * e3), I * th0[3] ** 2 / (2 * mp.pi * e3)]
    return th0, e3, R


def eta_product(t):
    q = mp.exp(I * mp.pi * t)
    n = int(75 * mp.log(10) / (2 * mp.pi * mp.im(t))) + 5
    p = mp.mpc(1)
    for k in range(1, n + 1):
        p *= 1 - q ** (2 * k)
    return mp.exp(I * mp.pi * t / 12) * p


def route_A(t):
    th0, _, _ = consts(t)
    return {r: -2 * mp.pi * mp.log(mp.pi / 2 * abs(th0[r]) ** 2) for r in (2, 3, 4)}


def route_C(t):
    q = mp.exp(I * mp.pi * t)
    y = mp.im(t)
    m_max = int(75 * mp.log(10) / (mp.pi * y)) + 5
    ms = range(1, m_max + 1)
    s2 = mp.fsum(mp.re((-1) ** m * mp.log(1 - q ** (2 * m))) for m in ms)
    s3 = mp.fsum(mp.re((-1) ** m * mp.log((1 + q ** m) / (1 - q ** m))) for m in ms)
    s4 = mp.fsum(mp.re(mp.log((1 + q ** m) / (1 - q ** m))) for m in ms)
    return {2: -2 * mp.pi * mp.log(2 * mp.pi) + mp.pi ** 2 * y - 4 * mp.pi * s2,
            3: 2 * mp.pi * mp.log(2 / mp.pi) + 4 * mp.pi * s3,
            4: 2 * mp.pi * mp.log(2 / mp.pi) + 4 * mp.pi * s4}


def np_thetas(z, t, nt=40):
    q = np.exp(1j * np.pi * t)
    zz = np.pi * np.asarray(z)[..., None]
    n = np.arange(nt)
    m = np.arange(1, nt)
    t1 = 2 * np.sum((-1.0) ** n * q ** ((n + 0.5) ** 2) * np.sin((2 * n + 1) * zz), -1)
    t2 = 2 * np.sum(q ** ((n + 0.5) ** 2) * np.cos((2 * n + 1) * zz), -1)
    t3 = 1 + 2 * np.sum(q ** (m ** 2) * np.cos(2 * m * zz), -1)
    t4 = 1 + 2 * np.sum((-1.0) ** m * q ** (m ** 2) * np.cos(2 * m * zz), -1)
    return t1, t2, t3, t4


def route_B(t):
    """c_r = int dtheta [ln r_max + int_0^r_max (r |S_r|^2 - 1/r) dr] over P, in double precision, own numpy thetas"""
    tc = complex(t)
    y, xr = tc.imag, tc.real
    _, a2, a3, a4 = np_thetas(np.zeros(1), tc)
    n = np.arange(40)
    q = np.exp(1j * np.pi * tc)
    d1 = 2 * np.pi * np.sum((-1.0) ** n * (2 * n + 1) * q ** ((n + 0.5) ** 2))
    zero = {2: a2[0], 3: a3[0], 4: a4[0]}
    corners = [0.5 * sx + 0.5 * st * tc for sx in (-1, 1) for st in (-1, 1)]
    cuts = sorted({0.0, 2 * np.pi} | {float(np.angle(c) % (2 * np.pi)) for c in corners})
    gx, gw = np.polynomial.legendre.leggauss(100)
    rx, rw = np.polynomial.legendre.leggauss(60)
    out = {}
    for r in (2, 3, 4):
        tot = 0.0
        for a0, a1 in zip(cuts[:-1], cuts[1:]):
            th = 0.5 * (a1 - a0) * gx + 0.5 * (a1 + a0)
            wt = 0.5 * (a1 - a0) * gw
            s, c = np.sin(th), np.cos(th)
            with np.errstate(divide="ignore"):
                rm = np.minimum(np.abs(0.5 * y / s), np.abs(0.5 / (c - s * xr / y)))
            rr = 0.5 * rm[:, None] * (rx[None, :] + 1)
            wr = 0.5 * rm[:, None] * rw[None, :]
            z = rr * np.exp(1j * th)[:, None]
            t1, t2, t3, t4 = np_thetas(z, tc)
            num = {2: t2, 3: t3, 4: t4}[r]
            S = num * d1 / (zero[r] * t1)
            f = rr * np.abs(S) ** 2 - 1 / rr
            tot += float(np.sum(wt * (np.log(rm) + np.sum(wr * f, axis=1))))
        out[r] = tot
    return out


def h_of(lam):
    return lam * mp.log(abs(lam)) + (1 - lam) * mp.log(abs(1 - lam))


def closed(t):
    th0, e3, R = consts(t)
    lam = th0[2] ** 4 / th0[3] ** 4
    h = h_of(lam)
    D = -th0[3] ** 4 * h / (4 * mp.pi * e3 ** 2)
    R2 = mp.fsum(abs(x) ** 2 for x in R)
    ratio = mp.pi * abs(h) / (1 + abs(lam) + abs(1 - lam))
    return {"lam": lam, "h": h, "D": D, "R2": R2, "ratio": ratio, "R": R}


def dot(u, v):
    return mp.fsum(a * b for a, b in zip(u, v))


def norm2(u):
    return mp.fsum(abs(a) ** 2 for a in u)


def C1(fib, cB):
    rows, worst_C, worst_B, worst_eta = {}, mp.mpf(0), 0.0, mp.mpf(0)
    for name, t in fib:
        a, c, b = route_A(t), route_C(t), cB[name]
        _, e3, _ = consts(t)
        de = abs(e3 - eta_product(t) ** 3) / abs(e3)
        worst_eta = max(worst_eta, de)
        dC = max(abs(c[r] - a[r]) for r in a)
        dB = max(abs(b[r] - float(a[r])) for r in a)
        worst_C, worst_B = max(worst_C, dC), max(worst_B, dB)
        rows[name] = {"tau": cx(t), "c_A": {r: fl(a[r]) for r in a}, "C - A": fl(dC), "B - A": dB}
    holds = worst_C < TIGHT and worst_B < 1e-10 and worst_eta < TIGHT
    return {"rows": rows, "worst route C - A": fl(worst_C), "worst route B - A": worst_B,
            "control: worst |eta^3 - product^3| / |eta^3|": fl(worst_eta), "holds": bool(holds)}


def C2(fib, cB):
    out, ok = {"rows": {}}, True
    worst_a, worst_id, worst_inv = 0.0, mp.mpf(0), mp.mpf(0)
    for name, t in fib:
        g = closed(t)
        cA = route_A(t)
        DA = mp.fsum(cA[CH[u]] * g["R"][u] ** 2 for u in range(3))
        DB = sum(cB[name][CH[u]] * complex(g["R"][u]) ** 2 for u in range(3))
        da = abs(DB - complex(g["D"])) / float(g["R2"])
        did = max(abs(DA - g["D"]) / g["R2"], abs(abs(g["D"]) / g["R2"] - g["ratio"]))
        inv = max(abs(closed(-1 / t)["ratio"] - g["ratio"]), abs(closed(t + 1)["ratio"] - g["ratio"]))
        worst_a, worst_id, worst_inv = max(worst_a, da), max(worst_id, did), max(worst_inv, inv)
        out["rows"][name] = {"lambda": cx(g["lam"]), "D": cx(g["D"]), "|D|/|R|^2": fl(g["ratio"]),
                             "route B's D, off": da, "identity, off": fl(did), "invariance, off": fl(inv)}
    out["(a) worst route B's D off the closed form, over |R|^2"] = worst_a
    out["(b) worst identity residual"] = fl(worst_id)
    out["(b) worst invariance residual (-1/tau, tau + 1)"] = fl(worst_inv)
    a_ok = worst_a < 1e-10
    b_ok = worst_id < TIGHT and worst_inv < TIGHT
    ratios = {name: closed(t)["ratio"] for name, t in fib}
    at_i = abs(ratios["i"] - mp.pi / 2 * mp.log(2))
    others = min(ratios[n] for n in ratios if n != "omega")
    c_ok = ratios["omega"] < TIGHT and others > mp.mpf("0.01") and at_i < TIGHT
    out["(c) at omega"] = fl(ratios["omega"])
    out["(c) smallest at the other 11"] = fl(others)
    out["(c) at i, off (pi/2) ln 2"] = fl(at_i)
    cusp, d_ok = {}, True
    for y in (4, 5, 6, 8):
        t = mp.mpc(0, y)
        g = closed(t)
        q = mp.exp(-mp.pi * y)
        val = g["D"] / (q * g["R2"])
        dev = val - 8 * mp.pi ** 2 * y - K
        pred = 64 * mp.pi * q * (4 * mp.log(2) - 1 - mp.pi * y)
        rel = abs(dev - pred) / abs(pred)
        cusp[f"{y}i"] = {"D/(q|R|^2)": cx(val), "deviation": cx(dev), "next order predicted": fl(pred),
                         "relative miss": fl(rel)}
        d_ok = d_ok and rel < mp.mpf("0.01")
        if y == 5:
            d_ok = d_ok and abs(dev) < mp.mpf("0.002")
    out["(d) cusp"] = cusp
    nodes, far, near = 0, [], []
    for i in range(41):
        x = mp.mpf(-0.5) + mp.mpf(i) / 40
        ymin = mp.sqrt(1 - x ** 2)
        for j in range(40):
            y = ymin + j * (2 - ymin) / 39
            t = mp.mpc(x, y)
            rt = closed(t)["ratio"]
            dist = min(abs(t - OMEGA), abs(t - (OMEGA + 1)))
            nodes += 1
            if dist > mp.mpf("0.1"):
                far.append((rt, x, y))
            elif dist > 0:
                near.append(rt / dist)
    fmin = min(far, key=lambda g: g[0])
    e_ok = fmin[0] > mp.mpf("0.05")
    out["(e) grid"] = {"nodes": nodes, "far nodes": len(far), "smallest far value": fl(fmin[0]),
                       "at": [fl(fmin[1]), fl(fmin[2])],
                       "near-corner value / distance, range (read-out)": [fl(min(near)), fl(max(near))]
                       if near else None}
    d = mp.mpf(10) ** -20
    slopes = [closed(OMEGA + d * mp.expj(2 * mp.pi * k / 360))["ratio"] / d for k in range(360)]
    out["read-out: directional slopes of |D|/|R|^2 at omega, min and max"] = [fl(min(slopes)), fl(max(slopes))]
    out["parts"] = {"a": bool(a_ok), "b": bool(b_ok), "c": bool(c_ok), "d": bool(d_ok), "e": bool(e_ok)}
    out["holds"] = bool(a_ok and b_ok and c_ok and d_ok and e_ok)
    return out


def direction(u, k):
    n = mp.sqrt(norm2(u))
    ph = u[k] / abs(u[k])
    return [a / (n * ph) for a in u]


def C3(fib):
    worst_a = mp.mpf(0)
    for _, t in fib:
        _, e3, R = consts(t)
        th0 = W85.thetas(mp.mpc(0), t)
        for lab in W85.LABELS[1:]:
            w = W85.point(lab, t)
            v = W85.triplet_at(w, t)
            thz = W85.thetas(w, t)
            S = [thz[CH[u] - 1] * 2 * mp.pi * e3 / (th0[CH[u] - 1] * thz[0]) for u in range(3)]
            mine = [R[u] * S[u] for u in range(3)]
            worst_a = max(worst_a, max(abs(v[u] - mine[u]) for u in range(3)) / mp.sqrt(norm2(v)))
    a_ok = worst_a < TIGHT
    worst_b = mp.mpf(0)
    worst_c = mp.mpf(0)
    worst_d_dir = mp.mpf(0)
    smallest_lift, at_omega = mp.inf, mp.mpf(0)
    control = mp.inf
    xs = [2 * mp.pi * L for L in (5, 20, 80)]
    for name, t in fib:
        cA = route_A(t)
        _, _, R = consts(t)
        c = [cA[CH[u]] for u in range(3)]
        DA = mp.fsum(c[u] * R[u] ** 2 for u in range(3))
        for X in xs:
            u4 = [mp.sqrt(X + c[k]) * R[k] for k in range(3)]
            u44 = [(X + c[k]) * R[k] for k in range(3)]
            r4 = abs(dot(u4, u4) - DA) / norm2(u4)
            r44 = abs(dot(u44, u44) - (2 * X * DA + mp.fsum(c[k] ** 2 * R[k] ** 2 for k in range(3)))) / norm2(u44)
            r41 = abs(dot(R, R)) / norm2(R)
            worst_b = max(worst_b, r4, r44, r41)
        if name != "omega":
            X = 2 * mp.pi * 10 ** 4
            for p in (mp.mpf(1) / 4, mp.mpf(1) / 2, mp.mpf(1), mp.mpf(2)):
                u = [(X + c[k]) ** p * R[k] for k in range(3)]
                lead = 2 * X ** p * p * X ** (p - 1) * DA
                worst_c = max(worst_c, abs(dot(u, u) / lead - 1))
        for beta in (mp.mpf("-0.1"), mp.mpf("0.05"), mp.mpf("0.2")):
            us = [[mp.exp(beta * (X + c[k])) * R[k] for k in range(3)] for X in xs]
            k0 = max(range(3), key=lambda k: abs(us[0][k]))
            dirs = [direction(u, k0) for u in us]
            for dd in dirs[1:]:
                worst_d_dir = max(worst_d_dir, max(abs(dd[k] - dirs[0][k]) for k in range(3)))
            lift = abs(dot(us[0], us[0])) / norm2(us[0])
            if name == "omega":
                at_omega = max(at_omega, lift)
            else:
                smallest_lift = min(smallest_lift, lift)
        ua = [mp.sqrt(xs[0] + c[k]) * R[k] for k in range(3)]
        ub = [mp.sqrt(xs[2] + c[k]) * R[k] for k in range(3)]
        k0 = max(range(3), key=lambda k: abs(ua[k]))
        da_, db_ = direction(ua, k0), direction(ub, k0)
        if name != "omega":
            control = min(control, max(abs(da_[k] - db_[k]) for k in range(3)))
    b_ok = worst_b < TIGHT
    c_ok = worst_c < mp.mpf("0.01")
    d_ok = worst_d_dir < TIGHT and smallest_lift > mp.mpf(10) ** -5 and at_omega < TIGHT and control > mp.mpf(10) ** -6
    return {"(a) worst |W85's triplet - R_r S_r| / |v|": fl(worst_a),
            "(b) worst residual of P4, P4'' and P4' (relative to |u|^2)": fl(worst_b),
            "(c) worst |u.u / (2 G G' D) - 1| at L = 10^4 (p = 1/4, 1/2, 1, 2)": fl(worst_c),
            "(d) worst direction change under e^{beta x}": fl(worst_d_dir),
            "(d) smallest |u.u|/|u|^2 under e^{beta x} off omega": fl(smallest_lift),
            "(d) largest |u.u|/|u|^2 under e^{beta x} at omega": fl(at_omega),
            "(d) control: smallest direction change under sqrt(x), L = 5 to 80, off omega": fl(control),
            "parts": {"a": bool(a_ok), "b": bool(b_ok), "c": bool(c_ok), "d": bool(d_ok)},
            "holds": bool(a_ok and b_ok and c_ok and d_ok)}


def Ymat(a, u):
    au = dot(a, u)
    return mp.matrix([[a[i] * u[j] + u[i] * a[j] - (au if i == j else 0) for j in range(3)] for i in range(3)])


def svals(M):
    s = mp.svd_c(M, compute_uv=False)
    return sorted([abs(s[i]) for i in range(3)], reverse=True)


def C4(fib):
    rng = random.Random(87)

    def rvec():
        return [mp.mpc(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(3)]

    worst_a = mp.mpf(0)
    for _ in range(5):
        a, u = rvec(), rvec()
        lhs = mp.det(Ymat(a, u))
        rhs = dot(a, a) * dot(u, u) * dot(a, u)
        worst_a = max(worst_a, abs(lhs - rhs) / (mp.sqrt(norm2(a)) * mp.sqrt(norm2(u))) ** 3)
    dirs = [rvec() for _ in range(3)]
    use = dict(fib)
    rows, b_ok = [], True
    for name in ("i", "t1", "t2"):
        t = use[name]
        cA = route_A(t)
        _, _, R = consts(t)
        c = [cA[CH[k]] for k in range(3)]
        DA = mp.fsum(c[k] * R[k] ** 2 for k in range(3))
        for a in dirs:
            sg = svals(Ymat(a, R))
            limit = abs(dot(a, a)) * abs(DA) * abs(dot(a, R)) / (2 * mp.pi * sg[0] ** 2 * sg[1])
            errs = []
            for L in (10 ** 3, 10 ** 4):
                u = [mp.sqrt(2 * mp.pi * L + c[k]) * R[k] for k in range(3)]
                s = svals(Ymat(a, u))
                errs.append(abs(L * s[2] / s[0] / limit - 1))
            fall = errs[0] / errs[1]
            ok = errs[1] < mp.mpf("0.01") and 5 <= fall <= 20
            b_ok = b_ok and ok
            rows.append({"fibre": name, "limit": fl(limit), "error at 10^3": fl(errs[0]),
                         "error at 10^4": fl(errs[1]), "fall": fl(fall), "holds": bool(ok)})
    a_ok = worst_a < TIGHT
    return {"(a) worst det identity residual": fl(worst_a), "(b)": rows,
            "parts": {"a": bool(a_ok), "b": bool(b_ok)}, "holds": bool(a_ok and b_ok)}


def main():
    fib = fibres()
    out = {"status": "W87: B1654's section 1 checked against C0 on this seat's own code "
                     "(script committed before its one run)",
           "dps": mp.mp.dps, "fibres": {n: cx(t) for n, t in fib}}
    cB = {name: route_B(t) for name, t in fib}
    out["C1"] = C1(fib, cB)
    out["C2"] = C2(fib, cB)
    out["C3"] = C3(fib)
    out["C4"] = C4(fib)
    out["cells"] = {k: out[k]["holds"] for k in ("C1", "C2", "C3", "C4")}
    out["every cell holds"] = all(out["cells"].values())
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)
    print(json.dumps(out["cells"], indent=1))


if __name__ == "__main__":
    main()
