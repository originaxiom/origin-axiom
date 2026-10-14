"""W65: the second unit. The Higgs's direction in M read as a section of weight -1/2 in rho_R (W64's sections), the
departure from the cone, and what it costs. The rule (W65_RULE.md) was committed before this script.

  H1  the instrument and the generators: E, R' and R by a 40-digit collocation; R against the direct theta series
  H2  the pairings: R.R = R'.R' = 0, R.R' = 2 Phi, E.R = 4 Phi, E.R'/Phi constant, E.E/Phi affine in j
  H3  the special points: omega (one 8-orbit line), i (the plane of P and its two isotropic lines), the cusp
  H4  the second generation at omega: m = 0 for every Higgs section; m > 0 away from omega and tau_0
  H5  the cusp: m ~ e^{-pi y} for alpha R + beta R'; m_E -> 1
  H6  the first generation does not mix under one coupling
  plus the read-outs: the constants, j_0 and tau_0, m_E on two paths, the exponent near omega, the cusp constant, the
  overlap of R and R'

"Relative" in H2 is fixed here, before the run, as relative to |f||g| (the scale of the product f.g), so that the
check is defined at omega, where Phi vanishes.

A failed launch, disclosed: the first launch crashed inside the first collocation solve, before any cell was computed
or any output written. mpmath's qr_solve uses a Householder step that takes its sign from the real part of the
diagonal entry, which is wrong for complex matrices and divides by zero when that real part is 0. The solve now uses
mpmath's complex QR (mp.qr) and a triangular solve, with the residual computed directly. It does not count as the run.

Run: python3 the_second_unit.py  ->  the_second_unit.json beside it.
"""
import itertools
import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_cusp_unit_as_a_vector as CU  # noqa: E402  (W64: K1, the orbits, line_key)
import the_cusp_unit_as_a_vector_posthoc as PH  # noqa: E402  (W64 post hoc: R from the direct theta series)

OUT = HERE / "the_second_unit.json"
mp.mp.dps = 40
I = mp.mpc(0, 1)
H0 = mp.sqrt(3) / 2
OMEGA = mp.mpc(-0.5, H0)
LINES = ("e_i", "v+", "v-")
B = {"e_i": [mp.mpf(1), mp.mpf(0), mp.mpf(0)], "v+": [mp.mpf(0), mp.mpf(1), -I], "v-": [mp.mpf(0), mp.mpf(1), I]}
LAM = {"e_i": mp.mpf(1) / 8, "v+": mp.mpf(7) / 8, "v-": mp.mpf(3) / 8}
P_SWAP = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
L_INV = [[1, 0, 0], [0, 0, 1], [0, -1, 0]]
EPI4 = mp.exp(I * mp.pi / 4)
N_COEF, M_PTS = 30, 120

SAMPLE = [mp.mpc(0, 1), OMEGA, mp.mpc(0, 2), mp.mpc(0, 4),
          mp.mpc(0.13, 1.21), mp.mpc(-0.31, 1.07), mp.mpc(0.42, 1.55), mp.mpc(0.07, 2.3), mp.mpc(-0.22, 0.99),
          mp.mpc(0.35, 0.95), mp.mpc(0, 1.8), mp.mpc(-0.45, 0.92), mp.mpc(0.48, 1.3), mp.mpc(-0.12, 3.1),
          mp.mpc(0.25, 0.98), mp.mpc(-0.4, 1.6), mp.mpc(0.3, 2.7), mp.mpc(0.5, 0.9), mp.mpc(-0.05, 1.02),
          mp.mpc(0.18, 1.4)]
COEF = {"E": mp.mpc(1), "R": mp.mpc(0.7, -0.3), "R'": mp.mpc(-0.4, 0.9)}       # H4's combinations per placement
AB = [(mp.mpc(1), mp.mpc(1)), (mp.mpc(1), mp.mpc(-1)), (mp.mpc(1), I), (mp.mpc(2), mp.mpc(0.5))]   # alpha, beta
TARGETS = [0.004, 0.02, 0.06]


def matvec(Mx, v):
    return [mp.fsum(Mx[r][c] * v[c] for c in range(3)) for r in range(3)]


def dot(f, g):
    return mp.fsum(f[k] * g[k] for k in range(3))


def norm(f):
    return mp.sqrt(mp.fsum(abs(x) ** 2 for x in f))


def cross(f, g):
    return [f[1] * g[2] - f[2] * g[1], f[2] * g[0] - f[0] * g[2], f[0] * g[1] - f[1] * g[0]]


def sine(f, g):
    """the sine of the Hermitian angle between the lines of f and g: |f x g| / (|f||g|)"""
    return norm(cross(f, g)) / (norm(f) * norm(g))


def qp(e, t):
    return mp.exp(2 * mp.pi * I * e * t)


RS = [[EPI4 * P_SWAP[r][c] for c in range(3)] for r in range(3)]
RT = [[EPI4 * L_INV[r][c] for c in range(3)] for r in range(3)]


# ----------------------------------------------------------------------------------------------------------- H1
def check_basis():
    """the basis vectors are rho(T)'s eigenvectors with eigenvalues e^{2 pi i lambda}"""
    worst = 0
    for l in LINES:
        w = matvec(RT, B[l])
        worst = max(worst, max(abs(w[k] - mp.exp(2 * mp.pi * I * LAM[l]) * B[l][k]) for k in range(3)))
    return worst


def solve_section(units, lead):
    """the section of weight -1/2 with end data `units` on (e_i, v+, v-), normalized by its leading coefficient 1 on
    `lead` at exponent lambda - 1: f(-1/t) = t^{-1/2} rho(S) f(t) on the arc |t| = 1"""
    u = dict(zip(LINES, units))
    cols = [(l, n) for l in LINES for n in range(-u[l], N_COEF) if not (l == lead and n == -1)]
    thetas = [mp.pi / 3 + mp.mpf("0.02") + k * (mp.pi / 3 - mp.mpf("0.04")) / (M_PTS - 1) for k in range(M_PTS)]
    A = mp.matrix(3 * M_PTS, len(cols))
    b = mp.matrix(3 * M_PTS, 1)
    for r, th in enumerate(thetas):
        t = mp.exp(I * th)
        ts, tk = -1 / t, mp.power(t, mp.mpf(-1) / 2)
        for c, (l, n) in enumerate(cols):
            e = n + LAM[l]
            sc = mp.exp(2 * mp.pi * e * H0)
            v2 = matvec(RS, B[l])
            for k in range(3):
                A[3 * r + k, c] = (B[l][k] * qp(e, ts) - tk * v2[k] * qp(e, t)) * sc
        e = LAM[lead] - 1
        v2 = matvec(RS, B[lead])
        for k in range(3):
            b[3 * r + k] = -(B[lead][k] * qp(e, ts) - tk * v2[k] * qp(e, t))
    Q, Rm = mp.qr(A, mode="skinny")                   # mpmath's complex QR (qr_solve's householder is real-only)
    x = mp.lu_solve(Rm, Q.H * b)
    res = mp.norm(A * x - b)                           # the residual computed directly
    terms = [(lead, LAM[lead] - 1, mp.mpf(1))] + [
        (l, n + LAM[l], x[c] * mp.exp(2 * mp.pi * (n + LAM[l]) * H0)) for c, (l, n) in enumerate(cols)]
    return terms, float(res / mp.norm(b))


def evaluate(terms, t):
    out = [mp.mpc(0)] * 3
    for l, e, a in terms:
        z = a * qp(e, t)
        out = [out[k] + z * B[l][k] for k in range(3)]
    return out


def R_main(t):
    v = PH.Rdirect(t)
    return [v[0], v[1], v[2]]


def H1(sec):
    worst = 0
    for t in SAMPLE:
        a, b = sec["R"](t), R_main(t)
        worst = max(worst, max(abs(a[k] + 2 * mp.pi * b[k]) for k in range(3)) / norm(a))
    res = {k: sec["residual"][k] for k in ("E", "R'", "R")}
    holds = max(res.values()) < 1e-20 and worst < 1e-20
    return {"the basis is rho(T)'s eigenbasis (largest error)": float(check_basis()),
            "collocation residuals (relative)": res,
            "R by collocation against -2 pi R (direct series), largest relative difference": float(worst),
            "holds": bool(holds)}


# ----------------------------------------------------------------------------------------------------------- forms
def sigma3(n):
    return sum(d ** 3 for d in range(1, n + 1) if n % d == 0)


SIG3 = [0] + [sigma3(n) for n in range(1, 80)]


def E4(t):
    q = qp(1, t)
    return 1 + 240 * mp.fsum(SIG3[n] * q ** n for n in range(1, 80))


def eta(t):
    q = qp(1, t)
    p = mp.mpf(1)
    for n in range(1, 120):
        p *= (1 - q ** n)
    return qp(mp.mpf(1) / 24, t) * p


def kleinj(t):
    return E4(t) ** 3 / eta(t) ** 24


def Phi(t):
    return E4(t) ** 2 / eta(t) ** 18


# ----------------------------------------------------------------------------------------------------------- H2
def H2(sec):
    rows = {}
    fit_pts = (mp.mpc(0, 2), mp.mpc(0.13, 1.21))
    ph = [Phi(t) for t in fit_pts]
    jj = [kleinj(t) for t in fit_pts]
    ee = [dot(sec["E"](t), sec["E"](t)) / p for t, p in zip(fit_pts, ph)]
    a = (ee[0] - ee[1]) / (jj[0] - jj[1])
    b0 = ee[0] - a * jj[0]
    c2 = dot(sec["E"](fit_pts[0]), sec["R'"](fit_pts[0])) / ph[0]
    worst = {"R.R": 0, "R'.R'": 0, "R.R' - 2 Phi": 0, "E.R - 4 Phi": 0, "E.R' - c2 Phi": 0, "E.E - (a j + b) Phi": 0}
    for t in SAMPLE:
        E, R, Rp = sec["E"](t), sec["R"](t), sec["R'"](t)
        p, j = Phi(t), kleinj(t)
        nE, nR, nRp = norm(E), norm(R), norm(Rp)
        vals = {"R.R": abs(dot(R, R)) / nR ** 2, "R'.R'": abs(dot(Rp, Rp)) / nRp ** 2,
                "R.R' - 2 Phi": abs(dot(R, Rp) - 2 * p) / (nR * nRp),
                "E.R - 4 Phi": abs(dot(E, R) - 4 * p) / (nE * nR),
                "E.R' - c2 Phi": abs(dot(E, Rp) - c2 * p) / (nE * nRp)}
        if t not in fit_pts:
            vals["E.E - (a j + b) Phi"] = abs(dot(E, E) - (a * j + b0) * p) / nE ** 2
        for k, v in vals.items():
            worst[k] = max(worst[k], float(v))
    rows["largest relative error over the sample (relative to |f||g|)"] = worst
    rows["E.R'/Phi (fitted at 2i)"] = [float(mp.re(c2)), float(mp.im(c2))]
    rows["E.E/Phi = a j + b: a"] = [float(mp.re(a)), float(mp.im(a))]
    rows["E.E/Phi = a j + b: b"] = [float(mp.re(b0)), float(mp.im(b0))]
    rows["holds"] = bool(max(worst.values()) < 1e-15)
    return rows, a, b0, c2


# ----------------------------------------------------------------------------------------------------------- H3
def orbit_size_of(v, orbit_of):
    key = CU.line_key(np.array([complex(x) for x in v]))
    return orbit_of.get(key)


def H3(sec, orbit_of):
    out = {}
    at_w = {k: sec[k](OMEGA) for k in ("E", "R", "R'")}
    norms_w = {k: float(norm(v)) for k, v in at_w.items()}
    par_w = max(float(sine(at_w["E"], at_w["R"])), float(sine(at_w["R'"], at_w["R"])))
    iso_w = float(abs(dot(at_w["R"], at_w["R"])) / norm(at_w["R"]) ** 2)
    orb_w = orbit_size_of(at_w["R"], orbit_of)
    out["omega"] = {"norms": norms_w, "largest sine of the angle to R(omega)": par_w, "R(omega) isotropy": iso_w,
                    "R(omega)'s orbit size": orb_w}
    ok_w = min(norms_w.values()) > 1e-10 and par_w < 1e-15 and orb_w == 8
    ti = mp.mpc(0, 1)
    at_i = {k: sec[k](ti) for k in ("E", "R", "R'")}
    off_plane = max(float(abs(v[0] - v[1]) / (mp.sqrt(2) * norm(v))) for v in at_i.values())
    l1, l2 = [mp.mpf(1), mp.mpf(1), -I * mp.sqrt(2)], [mp.mpf(1), mp.mpf(1), I * mp.sqrt(2)]
    sR = [float(sine(at_i["R"], l)) for l in (l1, l2)]
    sRp = [float(sine(at_i["R'"], l)) for l in (l1, l2)]
    one_each = (min(sR) < 1e-15 and min(sRp) < 1e-15 and int(np.argmin(sR)) != int(np.argmin(sRp)))
    orb_i = [orbit_size_of(l1, orbit_of), orbit_size_of(l2, orbit_of)]
    E_iso = float(abs(dot(at_i["E"], at_i["E"])) / norm(at_i["E"]) ** 2)
    out["i"] = {"largest component off the plane (e_i - e_j part)": off_plane,
                "R(i): sines to (1, 1, -i sqrt 2) and (1, 1, i sqrt 2)": sR,
                "R'(i): sines to the same two lines": sRp, "the two lines' orbit sizes": orb_i,
                "|E.E|/|E|^2 at i": E_iso}
    ok_i = off_plane < 1e-15 and one_each and orb_i == [12, 12] and E_iso > 1e-6
    t8 = mp.mpc(0, 8)
    s8 = {"E to e_i": float(sine(sec["E"](t8), B["e_i"])), "R to v+": float(sine(sec["R"](t8), B["v+"])),
          "R' to v-": float(sine(sec["R'"](t8), B["v-"]))}
    out["y = 8"] = s8
    ok_c = max(s8.values()) < 1e-4
    out["holds"] = bool(ok_w and ok_i and ok_c)
    return out


# ----------------------------------------------------------------------------------------------------------- masses
def Yuk(a, R):
    s = dot(a, R)
    return mp.matrix([[a[r] * R[c] + R[r] * a[c] - (s if r == c else 0) for c in range(3)] for r in range(3)])


def m_of(a, R):
    S = mp.svd_c(Yuk(a, R), compute_uv=False)
    return S[1] / S[0]


def combo(sec, t, weights):
    vals = {k: sec[k](t) for k in weights}
    return [mp.fsum(weights[k] * vals[k][c] for k in weights) for c in range(3)]


def placements():
    out = {}
    for u in itertools.product((0, 1), repeat=3):
        if sum(u) == 0:
            continue
        out[str(u)] = {k: COEF[k] for k, on in zip(("E", "R", "R'"), u) if on}
    return out


def H4(sec, tau0):
    at_w = {}
    Rw = R_main(OMEGA)
    for name, w in placements().items():
        at_w[name] = float(m_of(combo(sec, OMEGA, w), Rw))
    at_w["E"] = float(m_of(sec["E"](OMEGA), Rw))
    at_w["R'"] = float(m_of(sec["R'"](OMEGA), Rw))
    smallest = {}
    for t in SAMPLE:
        if abs(t - OMEGA) < 0.05 or abs(t - tau0) < 0.05:
            continue
        Rt = R_main(t)
        vals = [m_of(sec["E"](t), Rt)] + [m_of(combo(sec, t, {"R": al, "R'": be}), Rt) for al, be in AB]
        smallest[mp.nstr(t, 4)] = float(min(vals))
    holds = max(at_w.values()) < 1e-12 and min(smallest.values()) > 1e-9
    return {"m at omega (every placement's combination, E, R')": at_w,
            "smallest m over E and the four alpha R + beta R' at each sample point away from omega and tau_0": smallest,
            "holds": bool(holds)}


def H5(sec):
    rows = {}
    ok = True
    for al, be in AB:
        ms = {}
        for y in (5, 6):
            t = mp.mpc(0, y)
            ms[y] = m_of(combo(sec, t, {"R": al, "R'": be}), R_main(t))
        slope = mp.log(ms[6]) - mp.log(ms[5])
        rel = abs(slope + mp.pi) / mp.pi
        rows[f"alpha = {mp.nstr(al, 3)}, beta = {mp.nstr(be, 3)}"] = {
            "m at 5i": float(ms[5]), "m at 6i": float(ms[6]), "slope": float(slope), "relative to -pi": float(rel)}
        ok &= rel < 0.01
    t8 = mp.mpc(0, 8)
    mE8 = m_of(sec["E"](t8), R_main(t8))
    rows["m_E at 8i"] = float(mE8)
    ok &= (1 - mE8) < 1e-3
    rows["holds"] = bool(ok)
    return rows


def H6(sec, tau0):
    worst = 0
    count = 0
    for t in SAMPLE:
        if abs(t - OMEGA) < 0.05 or abs(t - tau0) < 0.05:
            continue
        Rt = R_main(t)
        higgs = [sec["E"](t)] + [combo(sec, t, {"R": al, "R'": be}) for al, be in AB]
        Us = []
        for a in higgs:
            U, S, V = mp.svd_c(Yuk(a, Rt))
            order = sorted(range(3), key=lambda k: S[k])                 # ascending: the massless state first
            Us.append(mp.matrix([[U[r, k] for k in order] for r in range(3)]))
        for U1, U2 in itertools.product(Us, repeat=2):
            V = U1.H * U2
            dev = max(abs(1 - abs(V[0, 0])), abs(V[0, 1]), abs(V[0, 2]), abs(V[1, 0]), abs(V[2, 0]))
            worst = max(worst, float(dev))
            count += 1
    return {"pairs checked": count, "largest deviation of the massless row and column from (1, 0, 0)": worst,
            "holds": bool(worst < 1e-12)}


# ----------------------------------------------------------------------------------------------------------- tau_0
def reduce_to_fd(t):
    for _ in range(200):
        t = t - mp.nint(mp.re(t))
        if abs(t) < 1:
            t = -1 / t
        else:
            break
    return t


def find_tau0(j0):
    ymax = max(mp.mpf(2), mp.log(abs(j0) + 1) / (2 * mp.pi) + 1)
    best = None
    for xr in range(-50, 51):
        for yk in range(0, 60):
            t = mp.mpc(xr / mp.mpf(100), H0 + (ymax - H0) * yk / 59)
            if abs(t) < 1:
                continue
            d = abs(kleinj(t) - j0)
            if best is None or d < best[0]:
                best = (d, t)
    t0 = mp.findroot(lambda t: kleinj(t) - j0, best[1], verify=False)     # its error is reported, not asserted
    t0 = reduce_to_fd(t0)
    return t0, float(abs(kleinj(t0) - j0) / max(abs(j0), 1))


# ----------------------------------------------------------------------------------------------------------- read-outs
def crossings(path, values, label):
    out = {}
    for target in TARGETS:
        hits = []
        for k in range(len(values) - 1):
            a, b = values[k] - target, values[k + 1] - target
            if a == 0 or (a < 0) != (b < 0):
                hits.append(path(k, a, b))
        out[str(target)] = hits
    return out


def readouts(sec, a, b0, c2, j0, tau0):
    ro = {"E.R'/Phi": [float(mp.re(c2)), float(mp.im(c2))],
          "j_0 = -b/a": [float(mp.re(j0)), float(mp.im(j0))],
          "j_0 is real (|Im|/|j_0|)": float(abs(mp.im(j0)) / abs(j0)),
          "tau_0 (E on the cone)": [float(mp.re(tau0)), float(mp.im(tau0))]}
    t0 = tau0
    ro["at tau_0: |E.E|/|E|^2 and m_E"] = [float(abs(dot(sec["E"](t0), sec["E"](t0))) / norm(sec["E"](t0)) ** 2),
                                           float(m_of(sec["E"](t0), R_main(t0)))]
    ys = [1 + k * mp.mpf("0.25") for k in range(29)]
    mE_axis = [float(m_of(sec["E"](mp.mpc(0, y)), R_main(mp.mpc(0, y)))) for y in ys]
    ro["m_E along tau = iy, y = 1 to 8 by 0.25"] = mE_axis
    ths = [mp.pi / 2 + k * (mp.pi / 6) / 40 for k in range(41)]
    arc = [mp.exp(I * th) for th in ths]
    mE_arc = [float(m_of(sec["E"](t), R_main(t))) for t in arc]
    ro["m_E along the arc from i to omega (41 points)"] = mE_arc

    def on_axis(k, fa, fb):
        y = ys[k] + (ys[k + 1] - ys[k]) * fa / (fa - fb)
        return float(y)

    def on_arc(k, fa, fb):
        th = ths[k] + (ths[k + 1] - ths[k]) * fa / (fa - fb)
        return [float(mp.cos(th)), float(mp.sin(th))]

    ro["where m_E equals 0.004, 0.02, 0.06 on the axis (y, linear interpolation)"] = crossings(on_axis, mE_axis, "y")
    ro["where m_E equals 0.004, 0.02, 0.06 on the arc (tau)"] = crossings(on_arc, mE_arc, "arc")
    near = {}
    for name, w in (("E", {"E": mp.mpc(1)}), ("R + R'", {"R": mp.mpc(1), "R'": mp.mpc(1)})):
        ms = {}
        for d in (mp.mpf("1e-3"), mp.mpf("1e-2")):
            t = OMEGA + I * d
            ms[d] = m_of(combo(sec, t, w), R_main(t))
        near[name] = {"m at delta = 1e-3": float(ms[mp.mpf("1e-3")]), "m at delta = 1e-2": float(ms[mp.mpf("1e-2")]),
                      "slope of log m against log delta": float(mp.log(ms[mp.mpf("1e-2")] / ms[mp.mpf("1e-3")])
                                                                / mp.log(10))}
    ro["near omega (tau = omega + i delta)"] = near
    cusp = {}
    for al, be in AB:
        t = mp.mpc(0, 6)
        mm = m_of(combo(sec, t, {"R": al, "R'": be}), R_main(t))
        cusp[f"alpha = {mp.nstr(al, 3)}, beta = {mp.nstr(be, 3)}"] = float(mm * mp.exp(6 * mp.pi) / abs(al / be))
    ro["m e^{pi y} / |alpha/beta| at y = 6"] = cusp

    def overlap(t):
        R, Rp = sec["R"](t), sec["R'"](t)
        return float(abs(mp.fsum(mp.conj(R[k]) * Rp[k] for k in range(3))) / (norm(R) * norm(Rp)))
    ro["|<R, R'>|/(|R||R'|) along tau = iy, y = 1 to 8 by 0.25"] = [overlap(mp.mpc(0, y)) for y in ys]
    ro["|<R, R'>|/(|R||R'|) along the arc from i to omega"] = [overlap(t) for t in arc]
    uni = {"E": COEF["E"], "R": COEF["R"], "R'": COEF["R'"]}
    ro["m for the uniform placement's combination along tau = iy"] = [
        float(m_of(combo(sec, mp.mpc(0, y), uni), R_main(mp.mpc(0, y)))) for y in ys]
    return ro


# ----------------------------------------------------------------------------------------------------------- main
def main():
    _, _, _, _, orbits, _ = CU.K1()
    orbit_of = {k: len(o) for o in orbits for k in o}
    sec = {"residual": {}}
    for name, units, lead in (("E", (1, 0, 0), "e_i"), ("R'", (0, 0, 1), "v-"), ("R", (0, 1, 0), "v+")):
        terms, res = solve_section(units, lead)
        sec["residual"][name] = res
        sec[name] = (lambda tm: (lambda t: evaluate(tm, t)))(terms)
    h1 = H1(sec)
    h2, a, b0, c2 = H2(sec)
    j0 = -b0 / a
    tau0, tau0_err = find_tau0(j0)
    h3 = H3(sec, orbit_of)
    h4 = H4(sec, tau0)
    h5 = H5(sec)
    h6 = H6(sec, tau0)
    out = {"status": "W65: the second unit (the rule W65_RULE.md first; one run)",
           "H1": h1, "H2": h2, "H3": h3, "H4": h4, "H5": h5, "H6": h6}
    out["cells"] = {k: out[k]["holds"] for k in ("H1", "H2", "H3", "H4", "H5", "H6")}
    out["every cell holds"] = all(out["cells"].values())
    out["tau_0's solve: |j(tau_0) - j_0| / max(|j_0|, 1)"] = tau0_err
    out["read-outs"] = readouts(sec, a, b0, c2, j0, tau0)
    OUT.write_text(json.dumps(out, indent=1, default=lambda x: float(x) if isinstance(x, mp.mpf) else str(x)) + "\n",
                   encoding="utf-8")
    print(json.dumps(out["cells"], indent=1), "\nevery cell holds:", out["every cell holds"])


if __name__ == "__main__":
    main()
