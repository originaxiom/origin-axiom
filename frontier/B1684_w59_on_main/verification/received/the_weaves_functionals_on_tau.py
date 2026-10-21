"""W51 (the rule: W51_RULE.md, committed before this script). What fixes tau? The weave's canonical functionals on the
tau-line, by THE WEAVE rule: the symmetric functions of the three parity sectors' determinants x_p = |theta_p/eta|^2,
T's own norm (W50's N6), the joint norm, and the untwisted sector's y |eta|^4 as the baseline.

  G1  e3 = x_2 x_3 x_4 = 4 on a grid over the fundamental domain, and Jacobi's theta_2 theta_3 theta_4 = 2 eta^3.
  G2  the critical points of e1 and e2 on the half fundamental domain F+ (0 <= x <= 1/2, |tau| >= 1): the interior by a
      grid of gradients refined by minimisation, the three boundary pieces (x = 0, x = 1/2, the arc) by sign changes of
      the tangential derivative; the corners i and rho = 1/2 + i sqrt(3)/2 (omega's point in F+); their types; the
      values against the closed forms; the growth toward the cusp.
  G3  the same for D = y |eta|^4, N_T = y^-1/2 sum_p |theta_p^2 / eta^3|^2 and P_T = prod_p y^-1/2 |theta_p^2/eta^3|^2.
  G4  no candidate has an extremum away from i, rho and the cusp.

  Extra read-outs (no prior): the invariant norms y^k ||Y_k(tau)||^2 of W50's one-dimensional coupling spaces (O+ and
  O- at k = 3, D and O- at k = 5, D at k = 7): their critical points and extrema on F+.

Run: python3 the_weaves_functionals_on_tau.py  ->  the_weaves_functionals_on_tau.json beside it.
"""
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, minimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_parity_grading_at_a_fixed_tau as PG  # noqa: E402  (W50: rho_T in the basis t_p, the coupling pieces, forms)

GM, H = PG.GM, PG.H
OUT = HERE / "the_weaves_functionals_on_tau.json"
RHO = 0.5 + 1j * math.sqrt(3) / 2
I_ = 1j
YMAX = 4.0
ETA_I = math.gamma(0.25) / (2 * math.pi ** 0.75)
ETA_W = 3 ** 0.125 * math.gamma(1 / 3) ** 1.5 / (2 * math.pi)


# ------------------------------------------------------------------------------------------------- theta and eta
def thetas(t, K=16):
    t = np.asarray(t, dtype=complex)
    n = np.arange(-K, K + 1).reshape((-1,) + (1,) * t.ndim)
    e3 = np.exp(1j * np.pi * n ** 2 * t)
    t2 = np.sum(np.exp(1j * np.pi * (n + 0.5) ** 2 * t), axis=0)
    t3 = np.sum(e3, axis=0)
    t4 = np.sum(((-1.0) ** n) * e3, axis=0)
    return t2, t3, t4


def eta(t, M=80):
    t = np.asarray(t, dtype=complex)
    q = np.exp(2j * np.pi * t)
    p = np.ones_like(q)
    for m in range(1, M):
        p = p * (1 - q ** m)
    return np.exp(1j * np.pi * t / 12) * p


def parts(t):
    t2, t3, t4 = thetas(t)
    et = eta(t)
    y = np.imag(np.asarray(t, dtype=complex))
    x = [np.abs(th / et) ** 2 for th in (t2, t3, t4)]
    return t2, t3, t4, et, y, x


def e1(t):
    _, _, _, _, _, x = parts(t)
    return x[0] + x[1] + x[2]


def e2(t):
    _, _, _, _, _, x = parts(t)
    return x[0] * x[1] + x[0] * x[2] + x[1] * x[2]


def e3(t):
    _, _, _, _, _, x = parts(t)
    return x[0] * x[1] * x[2]


def D(t):
    _, _, _, et, y, _ = parts(t)
    return y * np.abs(et) ** 4


def NT(t):
    t2, t3, t4, et, y, _ = parts(t)
    return y ** -0.5 * sum(np.abs(th ** 2 / et ** 3) ** 2 for th in (t2, t3, t4))


def PT(t):
    t2, t3, t4, et, y, _ = parts(t)
    out = np.ones_like(y)
    for th in (t2, t3, t4):
        out = out * y ** -0.5 * np.abs(th ** 2 / et ** 3) ** 2
    return out


CANDIDATES = {"e1": e1, "e2": e2, "D": D, "N_T": NT, "P_T": PT}


# ------------------------------------------------------------------------------------------------- the census
def grad(f, x, y, h=1e-5):
    fx = (f(x + h + 1j * y) - f(x - h + 1j * y)) / (2 * h)
    fy = (f(x + 1j * (y + h)) - f(x + 1j * (y - h))) / (2 * h)
    return fx, fy


def boundary_pieces():
    return {"x = 0": (lambda s: 1j * s, 1.0, 6.0),
            "x = 1/2": (lambda s: 0.5 + 1j * s, math.sqrt(3) / 2, 6.0),
            "the arc": (lambda s: np.exp(1j * s), math.pi / 3, math.pi / 2)}


def boundary_critical(f, n=3001, h=1e-6):
    out = {}
    for name, (path, a, b) in boundary_pieces().items():
        s = np.linspace(a, b, n)
        df = lambda u: float(np.real(f(path(u + h)) - f(path(u - h))) / (2 * h))
        d = np.array([df(u) for u in s[1:-1]])
        roots = []
        for i in range(len(d) - 1):
            if d[i] == 0 or d[i] * d[i + 1] < 0:
                try:
                    r = brentq(df, s[1 + i], s[2 + i], xtol=1e-13)
                except ValueError:
                    continue
                if min(abs(r - a), abs(r - b)) > 1e-4:
                    roots.append(round(r, 8))
        out[name] = sorted(set(roots))
    return out


def interior_critical(f, nx=60, ny=100):
    xs = np.linspace(0.0, 0.5, nx + 2)[1:-1]
    found = []
    for x in xs:
        y0 = math.sqrt(1 - x * x)
        ys = np.linspace(y0, YMAX, ny + 2)[1:-1]
        g = [np.hypot(*grad(f, x, y)) for y in ys]
        for j in range(1, len(ys) - 1):
            if g[j] <= g[j - 1] and g[j] <= g[j + 1]:
                found.append((x, ys[j], g[j]))
    pts = []
    for x, y, _ in found:
        res = minimize(lambda v: float(np.hypot(*grad(f, v[0], v[1])) ** 2), [x, y], method="Nelder-Mead",
                       options={"xatol": 1e-12, "fatol": 1e-24, "maxiter": 4000})
        vx, vy = res.x
        inside = 1e-3 < vx < 0.5 - 1e-3 and vx * vx + vy * vy > 1 + 2e-3 and vy < YMAX - 1e-3
        if inside and math.sqrt(res.fun) < 1e-7:
            if not any(abs(vx - a) + abs(vy - b) < 1e-5 for a, b in pts):
                pts.append((round(float(vx), 8), round(float(vy), 8)))
    return pts


def corner_type(f, z, kind, r=1e-3):
    """the sign of f - f(z) on a small circle around z inside F+ (min: all positive; max: all negative)"""
    f0 = float(np.real(f(z)))
    angles = {"i": np.linspace(0.05, np.pi / 2 - 0.05, 40), "rho": np.linspace(np.pi / 3 + 0.05, 5 * np.pi / 6 - 0.05, 40)}
    # inside F+: at i the quarter between the axis x = 0 (up) and the arc (to the right); at rho between the arc and x = 1/2
    if kind == "i":
        vals = [float(np.real(f(z + r * np.exp(1j * a)))) - f0 for a in angles["i"]]
    else:
        vals = [float(np.real(f(z + r * np.exp(1j * a)))) - f0 for a in angles["rho"]]
    up = float(np.real(f(z + 1j * r))) - f0 if kind == "i" else None
    along = None
    if kind == "i":
        along = float(np.real(f(np.exp(1j * (np.pi / 2 - r))))) - f0
    if all(v > 0 for v in vals):
        return "minimum", f0
    if all(v < 0 for v in vals):
        return "maximum", f0
    if kind == "i" and up is not None and along is not None and up * along < 0:
        return "saddle", f0
    return "saddle", f0


def grid_extrema(f, nx=101, ny=301):
    best_min, best_max = None, None
    for x in np.linspace(0, 0.5, nx):
        y0 = math.sqrt(1 - x * x)
        for y in np.linspace(y0, YMAX, ny):
            v = float(np.real(f(x + 1j * y)))
            if best_min is None or v < best_min[0]:
                best_min = (v, x, y)
            if best_max is None or v > best_max[0]:
                best_max = (v, x, y)
    return best_min, best_max


def census(f):
    gi = grad(f, 0.0, 1.0)
    gr = grad(f, 0.5, math.sqrt(3) / 2)
    ti, vi = corner_type(f, I_, "i")
    tr, vr = corner_type(f, RHO, "rho")
    bmin, bmax = grid_extrema(f)
    cusp = [float(np.real(f(1j * y))) for y in (4.0, 6.0, 8.0)]
    return {"the gradient at i and at rho": [abs(complex(*gi)), abs(complex(*gr))],
            "i": {"type": ti, "value": vi}, "rho": {"type": tr, "value": vr},
            "critical points on the boundary pieces (corners excluded)": boundary_critical(f),
            "critical points in the interior": interior_critical(f),
            "the grid's minimum (value, x, y)": [round(v, 10) for v in bmin],
            "the grid's maximum (value, x, y)": [round(v, 10) for v in bmax],
            "along x = 0 at y = 4, 6, 8": cusp}


# ------------------------------------------------------------------------------------------------- G1
def G1():
    worst, jac = 0.0, 0.0
    for x in np.linspace(-0.5, 0.5, 41):
        y0 = math.sqrt(1 - x * x)
        for y in np.linspace(y0, YMAX, 61):
            t = x + 1j * y
            worst = max(worst, abs(float(e3(t)) - 4.0))
            t2, t3, t4 = thetas(t)
            et = eta(t)
            jac = max(jac, abs(complex(t2 * t3 * t4 - 2 * et ** 3)) / abs(complex(2 * et ** 3)))
    return {"max |e3 - 4| on the grid": worst, "max relative |theta_2 theta_3 theta_4 - 2 eta^3|": jac}


def closed_forms():
    Di, Dw = ETA_I ** 4, (math.sqrt(3) / 2) * ETA_W ** 4
    return {"e1": (2 + 2 * math.sqrt(2), 3 * 2 ** (2 / 3)), "e2": (2 + 4 * math.sqrt(2), 3 * 2 ** (4 / 3)),
            "D": (Di, Dw), "N_T": (8 / math.sqrt(Di), 3 * 2 ** (4 / 3) / math.sqrt(Dw)),
            "P_T": (16 / Di ** 1.5, 16 / Dw ** 1.5)}


# ------------------------------------------------------------------------------------------------- extra: the couplings
def forms_vec(rS, rT, k, N=24, M=120):
    """W50's forms, with a vectorised evaluator (the same construction, step for step)"""
    rS, rT = np.array(rS, dtype=complex), np.array(rT, dtype=complex)
    d = rS.shape[0]
    w, P = np.linalg.eig(rT)
    P = np.linalg.qr(P)[0] if np.allclose(rT @ rT.conj().T, np.eye(d)) else P
    lam = [float(np.angle(z) / (2 * np.pi)) % 1.0 for z in w]
    lam = [0.0 if abs(x - 1) < 1e-9 or abs(x) < 1e-9 else x for x in lam]
    cols = [(j, n) for j in range(d) for n in range(N)]
    null, gap, Z, ev = PG.forms(rS, rT, k, N, M)
    h0 = np.sqrt(3) / 2
    e = np.array([n + lam[j] for j, n in cols])
    scale = np.exp(2 * np.pi * e * h0)
    Pc = np.array([P[:, j] for j, _ in cols]).T

    def evaluate(c, t):
        t = np.atleast_1d(np.asarray(t, dtype=complex))
        E = np.exp(2j * np.pi * np.outer(e, t)) * scale[:, None]
        return (Pc * c[None, :]) @ E

    return null, Z, evaluate, ev


def coupling_norms():
    names, U = GM.units()
    named, _ = H.triplets()
    C = named["T"]
    _, _, xs, ell, lhat, _, _ = GM.M1(C, U)
    Ct = GM.t_basis(C, xs, ell, lhat)
    A, Tm = PG.rho_T(Ct)
    rS9, rT9 = np.kron(A.conj(), A.conj()), np.kron(Tm.conj(), Tm.conj())
    pcs = PG.pieces()
    out, funcs, agree = {}, {}, True
    for name, k in (("O+", 3), ("O-", 3), ("D", 5), ("O-", 5), ("D", 7)):
        B = pcs[name]
        rS, rT = B.conj().T @ rS9 @ B, B.conj().T @ rT9 @ B
        null, Z, evv, ev = forms_vec(rS, rT, k)
        if null != 1:
            out["%s at k = %d" % (name, k)] = {"dimension": null}
            continue
        c = Z[:, 0]
        t_test = 0.13 + 1.21j
        agree &= bool(np.allclose(evv(c, t_test)[:, 0], ev(c, t_test), atol=1e-12))

        def norm(t, c=c, evv=evv, k=k):
            t = np.asarray(t, dtype=complex)
            vals = evv(c, t.ravel())
            return (np.imag(t.ravel()) ** k * np.sum(np.abs(vals) ** 2, axis=0)).reshape(t.shape)

        funcs["%s at k = %d" % (name, k)] = norm
    for nm, f in funcs.items():
        ti, vi = corner_type(f, I_, "i")
        tr, vr = corner_type(f, RHO, "rho")
        bmin, bmax = grid_extrema(f, nx=41, ny=121)
        out[nm] = {"i": {"type": ti, "value": vi}, "rho": {"type": tr, "value": vr},
                   "critical points on the boundary pieces (corners excluded)": boundary_critical(f, n=801),
                   "critical points in the interior": interior_critical(f, nx=24, ny=40),
                   "the grid's minimum (value, x, y)": [round(v, 10) for v in bmin],
                   "the grid's maximum (value, x, y)": [round(v, 10) for v in bmax],
                   "along x = 0 at y = 4, 6, 8": [float(np.real(f(1j * y))) for y in (4.0, 6.0, 8.0)]}
    return out, bool(agree)


def main():
    g1 = G1()
    cf = closed_forms()
    cen = {n: census(f) for n, f in CANDIDATES.items()}
    values_ok = {n: bool(abs(cen[n]["i"]["value"] - cf[n][0]) < 1e-8 * max(1, cf[n][0])
                         and abs(cen[n]["rho"]["value"] - cf[n][1]) < 1e-8 * max(1, cf[n][1])) for n in cen}

    def only_corners(n):
        c = cen[n]
        return (not c["critical points in the interior"]
                and all(not v for v in c["critical points on the boundary pieces (corners excluded)"].values())
                and max(c["the gradient at i and at rho"]) < 1e-6)

    def grows(n):
        a = cen[n]["along x = 0 at y = 4, 6, 8"]
        return a[0] < a[1] < a[2] and a[2] > 4 * a[0]

    def decays(n):
        a = cen[n]["along x = 0 at y = 4, 6, 8"]
        return a[0] > a[1] > a[2] > 0 and a[2] < a[0] / 4

    def at_rho(n, kind):
        c = cen[n]
        v = c["the grid's minimum (value, x, y)"] if kind == "minimum" else c["the grid's maximum (value, x, y)"]
        return abs(v[1] - 0.5) < 1e-9 and abs(v[2] - math.sqrt(3) / 2) < 1e-9

    checks = {
        "G1: e3 = 4 to 1e-10 and Jacobi's identity on the grid": bool(
            g1["max |e3 - 4| on the grid"] < 1e-10 and g1["max relative |theta_2 theta_3 theta_4 - 2 eta^3|"] < 1e-10),
        "G2: e1 and e2: only i (saddle) and rho (the global minimum), the closed-form values, growth to the cusp": all(
            only_corners(n) and cen[n]["i"]["type"] == "saddle" and cen[n]["rho"]["type"] == "minimum"
            and at_rho(n, "minimum") and values_ok[n] and grows(n) for n in ("e1", "e2")),
        "G3: D (rho the maximum), N_T and P_T (rho the minimum); i a saddle; the closed-form values": bool(
            only_corners("D") and cen["D"]["i"]["type"] == "saddle" and cen["D"]["rho"]["type"] == "maximum"
            and at_rho("D", "maximum") and values_ok["D"] and decays("D")
            and all(only_corners(n) and cen[n]["i"]["type"] == "saddle" and cen[n]["rho"]["type"] == "minimum"
                    and at_rho(n, "minimum") and values_ok[n] and grows(n) for n in ("N_T", "P_T"))),
        "G4: no candidate has an extremum away from i, rho and the cusp": all(only_corners(n) for n in CANDIDATES),
    }
    extra, agree = coupling_norms()
    out = {"status": "W51: what fixes tau? the weave's canonical functionals (the rule first)",
           "G1": g1, "the closed forms (at i, at rho)": {n: list(v) for n, v in cf.items()},
           "the census, by candidate": cen, "the values match the closed forms": values_ok,
           "extra read-outs (not predicted)": {"the coupling norms": extra,
                                               "the vectorised evaluator agrees with W50's": agree},
           "checks": {k: bool(v) for k, v in checks.items()}, "every check holds": bool(all(checks.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["checks"], indent=1))
    print("every check holds:", out["every check holds"])


if __name__ == "__main__":
    main()
