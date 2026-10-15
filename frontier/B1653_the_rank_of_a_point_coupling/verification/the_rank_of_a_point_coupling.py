#!/usr/bin/env python3
"""B1653 -- THE RANK OF A POINT COUPLING (sealed before this runs; PREREGISTRATION.md).

The record's zero mode (W21; B1642): F = (f(u), f(u + tau)), f(u) = th3(u; 2 tau)/sqrt(th1(u; tau)), PERIOD-1
convention, rho_Q: a -> QI, b -> QJ; generations C_p F with BLOCKS (QJ, QI, QK); B1644's coupling
Y_ab = sum_mn (C_a^T eps S C_b)_mn M_mn for a 2x2 bilinear M (the residue Res F~_x F~_y^T, a value F~_x(u0) F~_y(u0)^T,
or a spread integral).  A flat line: th3(u; 2 tau) -> th[a, b](u; 2 tau), record frame F~ = (f, e^{i pi b} f(u + tau)),
line point w = a tau + b/2; a field of hypercharge Y on the line (holonomy phases psi_1 along 1, psi_2 along tau) sees
6Y * w with w = psi_1 tau - psi_2.  Every bilinear uses B1642's fixed branch sqrt(th1(u) th1(u + tau)) :=
i e^{-i pi tau/2} e^{-i pi u} th1(u).  Thetas from mpmath's jtheta (argument pi u; th1 and th2 from th4 and th3 with the
nome root q^(1/4) = e^{i pi tau/4} explicit), characteristics by the shift formula.  All linear algebra in mpmath.

  U0 the frame and its control; U1 the form (c = (-i, -1, -1, i)); U2 the residue is rank one (the null quaternion);
  U3 rank <= 2 at the puncture (pairs, every line, every sector) and the two-point control; U4 the shared null state
  and V's trivial row and column, with the different-left-field control; U5 a regular point; U6 profiles: a radially
  symmetric one about a regular point acts as the point, a tilted, an elliptic and one radial about the puncture lift;
  U7 read-outs.  Plumbing on known cases, each < 1e-30 or the run is void.

    python3 -B the_rank_of_a_point_coupling.py      # writes the_rank_of_a_point_coupling.json beside itself
"""
import itertools, json, pathlib
import mpmath as mp
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
mp.mp.dps = 40
I = mp.mpc(0, 1)
QI = mp.matrix([[I, 0], [0, -I]]); QJ = mp.matrix([[0, 1], [-1, 0]]); QK = QI * QJ; ONE = mp.eye(2); EPS = QJ
UNITS = {"1": ONE, "i": QI, "j": QJ, "k": QK}
TH_OF = {"1": 1, "i": 2, "j": 4, "k": 3}
C_PRED = {"1": -I, "i": mp.mpf(-1), "j": mp.mpf(-1), "k": I}
BLOCKS = [QJ, QI, QK]
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
SECTORS = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
OUT = {}


# ---------------------------------------------------------------- thetas (period-1), by jtheta
def th(n, u, t):
    q = mp.exp(I * mp.pi * t); x = mp.pi * u
    if n == 3: return mp.jtheta(3, x, q)
    if n == 4: return mp.jtheta(4, x, q)
    q4 = mp.exp(I * mp.pi * t / 4); s = x + mp.pi * t / 2
    if n == 2: return q4 * mp.exp(I * x) * mp.jtheta(3, s, q)
    return -I * q4 * mp.exp(I * x) * mp.jtheta(4, s, q)


def thc(a, b, u, T):
    return mp.exp(I * mp.pi * a * a * T + 2 * I * mp.pi * a * (u + b)) * th(3, u + a * T + b, T)


def th_series(n, u, t, N=30):
    e = lambda x: mp.exp(I * mp.pi * x); K = range(-N, N + 1); h = mp.mpf(1) / 2
    if n == 1: return -I * mp.fsum((-1) ** k * e(t * (k + h) ** 2 + (2 * k + 1) * u) for k in K)
    if n == 2: return mp.fsum(e(t * (k + h) ** 2 + (2 * k + 1) * u) for k in K)
    if n == 3: return mp.fsum(e(t * k * k + 2 * k * u) for k in K)
    return mp.fsum((-1) ** k * e(t * k * k + 2 * k * u) for k in K)


def eta(t): return mp.exp(I * mp.pi * t / 12) * mp.qp(mp.exp(2 * I * mp.pi * t))
def d1(t): return mp.diff(lambda u: th(1, u, t), 0)


# ---------------------------------------------------------------- bilinears, pairings, couplings
def bil(x, y, u, t, frame="record"):
    (ax, bx), (ay, by) = x, y
    T = 2 * t; t1 = th(1, u, t)
    den = I * mp.exp(-I * mp.pi * t / 2) * mp.exp(-I * mp.pi * u) * t1
    X0, X1 = thc(ax, bx, u, T), thc(ax, bx, u + t, T)
    Y0, Y1 = thc(ay, by, u, T), thc(ay, by, u + t, T)
    if frame == "record":
        p01, p10 = mp.exp(I * mp.pi * by), mp.exp(I * mp.pi * bx)
    else:                                                    # the control: the symmetric phase on both off-diagonals
        p01 = p10 = mp.exp(I * mp.pi * (bx + by) / 2)
    p11 = mp.exp(I * mp.pi * (bx + by))
    return mp.matrix([[X0 * Y0 / t1, p01 * X0 * Y1 / den], [p10 * X1 * Y0 / den, p11 * X1 * Y1 / th(1, u + t, t)]])


def pair_from(M, C):
    K = EPS * C
    return sum(K[m, n] * M[m, n] for m in range(2) for n in range(2))


def res_bil(x, y, t, rad=mp.mpf("0.02"), N=96):
    acc = mp.matrix(2, 2)
    for m in range(N):
        u = rad * mp.exp(2 * I * mp.pi * m / N); acc += bil(x, y, u, t) * u
    return acc / N


def coupling(S, M):
    Y = mp.matrix(3, 3)
    for a, Ca in enumerate(BLOCKS):
        for b, Cb in enumerate(BLOCKS):
            K = Ca.T * EPS * S * Cb
            Y[a, b] = sum(K[m, n] * M[m, n] for m in range(2) for n in range(2))
    return Y


def sv(Y):
    return sorted([abs(s) for s in mp.svd_c(Y, compute_uv=False)], reverse=True)


def left_null(Y):
    U, S, V = mp.svd_c(Y)
    k = min(range(3), key=lambda i: abs(S[i]))
    v = [U[r, k] for r in range(3)]; n = mp.sqrt(sum(abs(z) ** 2 for z in v))
    return [z / n for z in v], [abs(S[i]) for i in range(3)], U


def det2(M): return M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
def mx(M): return max(abs(M[m, n]) for m in range(M.rows) for n in range(M.cols))
def wpt(x, t): return x[0] * t + x[1] / 2
def twist_of(w, t):
    a = mp.im(w) / mp.im(t); return (a, 2 * (mp.re(w) - a * mp.re(t)))


def line_w(psi1, psi2, t): return psi1 * t - psi2             # W59's holonomy phases (the reviewer's finding 4)


def field(wline, f, t): return twist_of(SIXY[f] * wline, t)


rng = np.random.default_rng(16531)
def rnd_twist(): return (mp.mpf(rng.uniform(-0.5, 0.5)), mp.mpf(rng.uniform(-1, 1)))
def rnd_S():
    z = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    return mp.matrix([[mp.mpc(z[0, 0]), mp.mpc(z[0, 1])], [mp.mpc(z[1, 0]), mp.mpc(z[1, 1])]])


OMEGA = mp.exp(2 * I * mp.pi / 3)
TAUS = [mp.mpc(0.13, 1.07), mp.mpc(-0.31, 0.88), OMEGA]
PTS = [mp.mpc(0.21, 0.17), mp.mpc(0.33, -0.12), mp.mpc(-0.4, 0.29)]
PAIRS = [(rnd_twist(), rnd_twist()) for _ in range(5)]
SS = [rnd_S() for _ in range(20)]

# ---------------------------------------------------------------- plumbing (known cases)
pl = {}
pl["jtheta_vs_series"] = float(max(abs(th(n, u, t) / th_series(n, u, t) - 1) for n in (1, 2, 3, 4) for u in PTS for t in (TAUS[0], OMEGA)))
pl["th1p_vs_2pi_eta3"] = float(max(abs(d1(t) / (2 * mp.pi * eta(t) ** 3) - 1) for t in TAUS))
pl["thc_vs_series"] = float(max(abs(thc(a, b, u, 2 * TAUS[0]) / mp.fsum(mp.exp(I * mp.pi * 2 * TAUS[0] * (n + a) ** 2 + 2 * I * mp.pi * (n + a) * (u + b)) for n in range(-30, 31)) - 1)
                                for (a, b) in [(mp.mpf("0.1"), mp.mpf("0.3")), (mp.mpf("-0.27"), mp.mpf("0.6"))] for u in PTS))


def omega_fixed(z):
    """is omega*z - z in the lattice Z + omega Z?"""
    d = OMEGA * z - z; n = mp.im(d) / mp.im(OMEGA); m = mp.re(d) - n * mp.re(OMEGA)
    return float(max(abs(n - mp.nint(n)), abs(m - mp.nint(m))))


pl["w59_minimum_3w_omega_fixed"] = max(omega_fixed(3 * line_w(base + i_ / mp.mpf(3), base + j_ / mp.mpf(3), OMEGA))
                                       for base in (mp.mpf(1) / 9, mp.mpf(2) / 9) for i_ in range(3) for j_ in range(3))
# the half-period shift of one field acts on the four pairings as a signed permutation (design v1's U3; frame algebra)
def four(x, y, t, u): M = bil(x, y, u, t); return [pair_from(M, UNITS[s]) for s in "1ijk"]
def signed_perm_err(v, w):
    best = 1e9
    for p in itertools.permutations(range(4)):
        vp = [v[k] for k in p]; k0 = max(range(4), key=lambda k: abs(vp[k])); lam = w[k0] / vp[k0]
        best = min(best, max(min(abs(w[k] - lam * vp[k]), abs(w[k] + lam * vp[k])) for k in range(4)) / max(abs(z) for z in w))
    return float(best)
pl["half_period_signed_perm_max"] = max(signed_perm_err(four(x, y, TAUS[0], PTS[0]), four((x[0] + sh[0], x[1] + sh[1]), y, TAUS[0], PTS[0]))
                                        for (x, y) in PAIRS[:3] for sh in [(0, 1), (mp.mpf(1) / 2, 0), (mp.mpf(1) / 2, 1)])
pl["all_below_1e-30"] = all(v < 1e-30 for k, v in pl.items())
OUT["plumbing"] = pl                       # a plumbing failure voids the run as an instrument failure (PREREGISTRATION §4)

# ---------------------------------------------------------------- U0, the frame
def holonomy_err(x, y, u, t):
    (ax, bx), (ay, by) = x, y
    B0 = bil(x, y, u, t); B1 = bil(x, y, u + 1, t); Bt = bil(x, y, u + t, t)
    Ea = B1 - mp.exp(2 * I * mp.pi * (ax + ay)) * QI * B0 * QI.T
    Eb = Bt - mp.exp(-I * mp.pi * (bx + by)) * QJ * B0 * QJ.T
    return float(max(mx(Ea), mx(Eb)) / mx(B0))


def form_spread(x, y, t, s, frame="record", pts=PTS):
    A = x[0] + y[0]; ub = wpt(x, t) + wpt(y, t)
    vals = [pair_from(bil(x, y, u, t, frame), UNITS[s]) * th(1, u, t) * mp.exp(-2 * I * mp.pi * A * u) / th(TH_OF[s], u + ub, t) for u in pts]
    return vals[0], float(max(abs(v / vals[0] - 1) for v in vals[1:]))


u0a = max(holonomy_err(x, y, u, t) for t in TAUS for (x, y) in PAIRS for u in PTS)
u0b = min(max(form_spread(x, y, t, s, frame="control")[1] for s in "1i") for t in TAUS for (x, y) in PAIRS)
OUT["U0"] = {"a_holonomy_max": u0a, "b_control_min_spread": u0b, "holds": u0a < 1e-25 and u0b > 1e-3}

# ---------------------------------------------------------------- U1, the form
u1a = 0.0; u1b = 0.0; c_read = {}
for t in TAUS:
    for (x, y) in PAIRS:
        de = wpt(x, t) - wpt(y, t); N = {}
        for s in "1ijk":
            N[s], spread = form_spread(x, y, t, s); u1a = max(u1a, spread)
        rat = {s: N[s] / (C_PRED[s] * th(TH_OF[s], de, t)) for s in "1ijk"}
        u1b = max(u1b, float(max(abs(rat[s] / rat["i"] - 1) for s in "1ijk")))
        c_read.setdefault("c1_over_ci", []).append(mp.nstr((N["1"] / th(1, de, t)) / (N["i"] / th(2, de, t)) * C_PRED["i"], 12))
        c_read.setdefault("kappa", []).append(mp.nstr(rat["i"], 12))
stored = json.loads((ROOT / "frontier/B1642_the_golden_coupling_as_the_zero_modes_residue/verification/residue_coupling.json").read_text())["R2"]
u1c = 0.0
for t in TAUS[:2]:
    for s in "ijk":
        Ns, _ = form_spread((0, 0), (0, 0), t, s)
        c_here = Ns / th(TH_OF[s], 0, t)
        c_store = complex(*stored[s]["c_values"][0])
        u1c = max(u1c, float(abs(c_here - c_store)))
OUT["U1"] = {"a_const_max": u1a, "b_common_ratio_max": u1b, "c_vs_B1642_stored_c_max": u1c,
             "holds": u1a < 1e-25 and u1b < 1e-25 and u1c < 1e-25}

# ---------------------------------------------------------------- U2, the residue is rank one
u2a = 0.0; u2b = 0.0; u2c = 0.0; u2d = 1.0; RES = {}
for ti, t in enumerate(TAUS):
    for pi_, (x, y) in enumerate(PAIRS):
        Rb = res_bil(x, y, t); RES[(ti, pi_)] = Rb
        R = {s: pair_from(Rb, UNITS[s]) for s in "1ijk"}
        u2a = max(u2a, float(abs(det2(Rb)) / mx(Rb) ** 2))
        u2b = max(u2b, float(abs(sum(R[s] ** 2 for s in "1ijk")) / sum(abs(R[s]) ** 2 for s in "1ijk")))
        ub, de = wpt(x, t) + wpt(y, t), wpt(x, t) - wpt(y, t)
        Ni, _ = form_spread(x, y, t, "i", pts=PTS[:2]); kap = Ni / (C_PRED["i"] * th(2, de, t))
        RR = sum(R[s] ** 2 for s in "ijk")
        u2c = max(u2c, float(abs(RR / ((kap / d1(t)) ** 2 * th(1, ub, t) ** 2 * th(1, de, t) ** 2) - 1)))
        u2d = min(u2d, float(abs(RR) / sum(abs(R[s]) ** 2 for s in "ijk")))
OUT["U2"] = {"a_det_max": u2a, "b_null_quaternion_max": u2b, "c_RR_vs_formula_max": u2c, "d_triplet_isotropy_min": u2d,
             "holds": u2a < 1e-30 and u2b < 1e-30 and u2c < 1e-20 and u2d > 1e-3}

# ---------------------------------------------------------------- U3, rank <= 2 at the puncture
def ratio(Y): s = sv(Y); return float(s[2] / s[0])


u3a = max(ratio(coupling(S, RES[(ti, pi_)])) for ti in range(3) for pi_ in range(5) for S in SS)
LINES = {}
for t, tn in ((OMEGA, "omega"), (TAUS[0], "generic")):
    for (p1, p2) in [(mp.mpf(1) / 2, 0), (0, mp.mpf(1) / 2), (mp.mpf(1) / 2, mp.mpf(1) / 2)]:
        LINES[("half", tn, float(p1), float(p2))] = (line_w(p1, p2, t), t)
third, ninth = mp.mpf(1) / 3, mp.mpf(1) / 9
for i_ in range(3):
    for j_ in range(3):
        if (i_, j_) != (0, 0):
            LINES[("torsion3", "omega", i_ / 3, j_ / 3)] = (line_w(i_ * third, j_ * third, OMEGA), OMEGA)
for base in (ninth, 2 * ninth):
    for i_ in range(3):
        for j_ in range(3):
            LINES[("higgs", "omega", float(base + i_ * third), float(base + j_ * third))] = (line_w(base + i_ * third, base + j_ * third, OMEGA), OMEGA)
u3b = 0.0; SECT_RES = {}; RR_read = {}
for key, (wl, t) in LINES.items():
    for sec, (f1, f2) in SECTORS.items():
        Rb = res_bil(field(wl, f1, t), field(wl, f2, t), t); SECT_RES[(key, sec)] = Rb
        R = {s: pair_from(Rb, UNITS[s]) for s in "ijk"}
        RR_read[str(key) + " " + sec] = float(abs(sum(R[s] ** 2 for s in "ijk")) / sum(abs(R[s]) ** 2 for s in "ijk"))
        u3b = max(u3b, max(ratio(coupling(S, Rb)) for S in SS[:5]))
# the two-point control: S1 at the puncture plus S2 at a regular point (value bilinear), every draw
u0p = mp.mpc(0.3, 0.2); u3c = 1.0
for (x, y) in PAIRS[:3]:
    Rb = res_bil(x, y, TAUS[0]); Vb = bil(x, y, u0p, TAUS[0]); Vb = Vb * (mx(Rb) / mx(Vb))
    for k in range(20):
        u3c = min(u3c, ratio(coupling(SS[k], Rb) + coupling(SS[(k + 7) % 20], Vb)))
OUT["U3"] = {"a_pairs_max": u3a, "b_lines_max": u3b, "c_two_point_min": u3c,
             "holds": u3a < 1e-30 and u3b < 1e-30 and u3c > 1e-6}

# ---------------------------------------------------------------- U4, the shared null state
def overlap(a, b): return abs(sum(mp.conj(a[k]) * b[k] for k in range(3)))       # mpmath; compared in mpmath


u4a = mp.mpf(0); u4b = 0.0                # u4a = max(1 - overlap), in mpmath
cases = [(TAUS[0], wpt(rnd_twist(), TAUS[0])) for _ in range(5)]          # five random lines at a generic tau
cases += [(t, wl) for key, (wl, t) in LINES.items()]
for (t, wl) in cases:
    Su, Sd = SS[rng.integers(20)], SS[rng.integers(20)]
    Yu = coupling(Su, res_bil(field(wl, "Q", t), field(wl, "u", t), t))
    Yd = coupling(Sd, res_bil(field(wl, "Q", t), field(wl, "d", t), t))
    nu, svu, Uu = left_null(Yu); nd, svd_, Ud = left_null(Yd)
    u4a = max(u4a, 1 - overlap(nu, nd))
    V = Uu.H * Ud
    ku = min(range(3), key=lambda i: svu[i]); kd = min(range(3), key=lambda i: svd_[i])
    u4b = max(u4b, max(float(abs(V[ku, j])) for j in range(3) if j != kd), max(float(abs(V[i, kd])) for i in range(3) if i != ku))
# the control: a down-type sector whose left field carries 6Y = 2
u4c = 1.0
for (t, wl) in cases[:5]:
    Yu = coupling(SS[0], res_bil(field(wl, "Q", t), field(wl, "u", t), t))
    Yx = coupling(SS[1], res_bil(twist_of(2 * wl, t), field(wl, "d", t), t))
    u4c = min(u4c, float(1 - overlap(left_null(Yu)[0], left_null(Yx)[0])))
OUT["U4"] = {"a_max_1_minus_overlap": mp.nstr(u4a, 5), "b_V_offblock_max": u4b, "c_control_min_1_minus_overlap": u4c,
             "holds": u4a < mp.mpf("1e-25") and u4b < 1e-20 and u4c > 1e-3}

# ---------------------------------------------------------------- U5, a regular point
u5a = 0.0; u5b = 0.0
for (x, y) in PAIRS:
    for u in PTS:
        Vb = bil(x, y, u, TAUS[0])
        u5a = max(u5a, float(abs(det2(Vb)) / mx(Vb) ** 2))
        u5b = max(u5b, max(ratio(coupling(S, Vb)) for S in SS[:5]))
OUT["U5"] = {"a_det_max": u5a, "b_rank_ratio_max": u5b, "holds": u5a < 1e-30 and u5b < 1e-30}

# ---------------------------------------------------------------- U6, profiles (a: acts as the point; b-d: the lift)
NT = 64
c0 = mp.mpc(0.3, 0.2)
RADII_REG = [mp.mpf(x) for x in ("0.01", "0.025", "0.04", "0.055", "0.07", "0.085", "0.1")]
RADII_PUN = [mp.mpf(x) for x in ("0.02", "0.035", "0.05", "0.065", "0.08", "0.1")]
def g(r): return mp.exp(-r ** 2 / mp.mpf("0.0025"))
PROFILES = {
 "a_radial_regular": (c0, RADII_REG, lambda z, r: g(r)),
 "b_tilted_regular": (c0, RADII_REG, lambda z, r: g(r) * (1 + mp.re(z - c0) / mp.mpf("0.05"))),
 "c_elliptic_regular": (c0, RADII_REG, lambda z, r: mp.exp(-(mp.re(z - c0) / mp.mpf("0.1")) ** 2 - (mp.im(z - c0) / mp.mpf("0.03")) ** 2)),
 "d_radial_puncture": (mp.mpc(0, 0), RADII_PUN, lambda z, r: g(r)),
}
u6 = {}
for name, (cen, radii, w) in PROFILES.items():
    dets, rats = [], []
    for (x, y) in PAIRS[:3]:
        M = mp.matrix(2, 2)
        for r in radii:
            for k in range(NT):
                z = cen + r * mp.exp(2 * I * mp.pi * k / NT); M += w(z, r) * r * bil(x, y, z, TAUS[0])
        dets.append(float(abs(det2(M)) / mx(M) ** 2)); rats.append(min(ratio(coupling(S, M)) for S in SS))
    u6[name] = {"det_min": min(dets), "det_max": max(dets), "ratio_min": min(rats), "ratio_max": max(rats)}
OUT["U6"] = {**u6, "holds": (u6["a_radial_regular"]["det_max"] < 1e-30 and u6["a_radial_regular"]["ratio_max"] < 1e-30
                              and u6["b_tilted_regular"]["det_min"] > 1e-5 and u6["b_tilted_regular"]["ratio_min"] > 1e-6
                              and u6["c_elliptic_regular"]["det_min"] > 1e-4 and u6["c_elliptic_regular"]["ratio_min"] > 1e-6
                              and u6["d_radial_puncture"]["det_min"] > 1e-2 and u6["d_radial_puncture"]["ratio_min"] > 1e-3)}

# ---------------------------------------------------------------- U7, read-outs
OUT["U7_read_out"] = {"c1_at_each_case": c_read["c1_over_ci"], "kappa_at_each_case": c_read["kappa"],
                      "RR_triplet_per_line_sector": RR_read, "two_point_min_ratio": u3c}

(HERE / "the_rank_of_a_point_coupling.json").write_text(json.dumps(OUT, indent=1, default=str))
for k in ("plumbing", "U0", "U1", "U2", "U3", "U4", "U5", "U6"):
    print(k, {kk: vv for kk, vv in OUT[k].items()})
