#!/usr/bin/env python3
"""B1653 -- THE TWISTED ZERO MODE (sealed before this runs; PREREGISTRATION.md).

The record's zero mode (W21; B1642): F = (f(u), f(u + tau)), f(u) = th3(u; 2 tau)/sqrt(th1(u; tau)), in the PERIOD-1
convention (u has periods 1 and tau), carrying rho_Q: a -> QI = diag(i, -i), b -> QJ = [[0, 1], [-1, 0]].  A flat U(1)
twist replaces th3(u; 2 tau) by th[a, b](u; 2 tau); in the record's frame the doublet is (f(u), e^{i pi b} f(u + tau))
(the hand derivation, PREREGISTRATION section 1.2); the field's line point is w = a tau + b/2.  Every quantity is read
through bilinears, with B1642's fixed branch sqrt(th1(u) th1(u + tau)) := i e^{-i pi tau/2} e^{-i pi u} th1(u).

INDEPENDENT INSTRUMENT: thetas from mpmath's jtheta (argument pi u, nome q = e^{i pi tau}; th1 and th2 built from th4
and th3 with the nome root q^(1/4) := e^{i pi tau/4} explicit, as in B1651), characteristics by the shift formula
th[a, b](u | T) = e^{i pi a^2 T + 2 pi i a (u + b)} th3(u + a T + b | T).  (The exploration before the seal used
hand-written series in B1642's style.)

  U0  the record-frame bilinears obey the twisted holonomy law (QI on u + 1, QJ on u + tau); the naive frame fails
  U1  P_s(u) = kappa c_s th_s(delta) e^{2 pi i A u} th_s(u + ubar)/th1(u) for the four units C = 1, i, j, k
      (s = 1, 2, 4, 3); N_s/(c_s th_s(delta)) common; the untwisted case = B1642's R2
  U2  R.R from contour residues = kappa^2 th1(ubar)^2 th1(delta)^2 / th1'(0)^2; Majorana pairs null; the quartic
      identity; the eps^2 scaling
  U3  shifts: a lattice shift of one field changes the four-pairing vector by a common scalar; a half-period shift
      by a signed permutation and a common scalar
  U4  the lines on the record, sector by sector (charges in units of 6Y: Q 1, u^c -4, d^c 2, L -3, e^c 6, H 3)
  U5  the masses' zero pattern: the smallest Takagi value of Y(a; R) = a R^T + R a^T - (a.R) 1 against U4
  U6  read-outs

    python3 -B twisted_zero_mode.py      # writes twisted_zero_mode.json beside itself
"""
import json, pathlib
import mpmath as mp
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
mp.mp.dps = 40
I = mp.mpc(0, 1)
QI = mp.matrix([[I, 0], [0, -I]]); QJ = mp.matrix([[0, 1], [-1, 0]]); QK = QI * QJ; ONE = mp.eye(2)
EPS = QJ
UNITS = {"1": ONE, "i": QI, "j": QJ, "k": QK}
TH_OF = {"1": 1, "i": 2, "j": 4, "k": 3}
OUT = {}


# ---------------------------------------------------------------- thetas, period-1 convention, by jtheta
def th(n, u, t):
    q = mp.exp(I * mp.pi * t); x = mp.pi * u
    if n == 3: return mp.jtheta(3, x, q)
    if n == 4: return mp.jtheta(4, x, q)
    q4 = mp.exp(I * mp.pi * t / 4); s = x + mp.pi * t / 2
    if n == 2: return q4 * mp.exp(I * x) * mp.jtheta(3, s, q)
    return -I * q4 * mp.exp(I * x) * mp.jtheta(4, s, q)          # th1, sign fixed by the plumbing check below


def thc(a, b, u, T):
    """th[a, b](u | T) = e^{i pi a^2 T + 2 pi i a (u + b)} th3(u + a T + b | T)"""
    return mp.exp(I * mp.pi * a * a * T + 2 * I * mp.pi * a * (u + b)) * th(3, u + a * T + b, T)


def th_series(n, u, t, N=30):
    """B1642's series, for the plumbing check only"""
    e = lambda x: mp.exp(I * mp.pi * x); K = range(-N, N + 1); h = mp.mpf(1) / 2
    if n == 1: return -I * mp.fsum((-1) ** k * e(t * (k + h) ** 2 + (2 * k + 1) * u) for k in K)
    if n == 2: return mp.fsum(e(t * (k + h) ** 2 + (2 * k + 1) * u) for k in K)
    if n == 3: return mp.fsum(e(t * k * k + 2 * k * u) for k in K)
    return mp.fsum((-1) ** k * e(t * k * k + 2 * k * u) for k in K)


def eta(t):
    return mp.exp(I * mp.pi * t / 12) * mp.qp(mp.exp(2 * I * mp.pi * t))


def d1(t): return mp.diff(lambda u: th(1, u, t), 0)


# ---------------------------------------------------------------- the twisted doublet's bilinears
def bil(x, y, u, t, frame=True):
    """the record-frame bilinears F~_x(u)_m F~_y(u)_n (m, n in {0, 1}); frame=False is the naive frame D = 1"""
    (ax, bx), (ay, by) = x, y
    T = 2 * t; t1 = th(1, u, t)
    den = I * mp.exp(-I * mp.pi * t / 2) * mp.exp(-I * mp.pi * u) * t1       # sqrt(th1(u) th1(u + tau)), B1642
    X0, X1 = thc(ax, bx, u, T), thc(ax, bx, u + t, T)
    Y0, Y1 = thc(ay, by, u, T), thc(ay, by, u + t, T)
    px = mp.exp(I * mp.pi * bx) if frame else 1
    py = mp.exp(I * mp.pi * by) if frame else 1
    return mp.matrix([[X0 * Y0 / t1, py * X0 * Y1 / den], [px * X1 * Y0 / den, px * py * X1 * Y1 / th(1, u + t, t)]])


def pairing(C, x, y, u, t, frame=True):
    """F~_x^T eps C F~_y = sum_mn (eps C)_mn B_mn"""
    M = EPS * C; B = bil(x, y, u, t, frame)
    return sum(M[m, n] * B[m, n] for m in range(2) for n in range(2))


def wpt(x, t): return x[0] * t + x[1] / 2


def rnd_twist(rng): return (mp.mpf(rng.uniform(-0.5, 0.5)), mp.mpf(rng.uniform(-1, 1)))


rng = np.random.default_rng(1653)
TAUS = [mp.mpc(0.13, 1.07), mp.mpc(-0.31, 0.88), mp.exp(2 * I * mp.pi / 3)]      # two generic, and omega
PTS = [mp.mpc(0.21, 0.17), mp.mpc(0.33, -0.12), mp.mpc(-0.4, 0.29)]
PAIRS = [(rnd_twist(rng), rnd_twist(rng)) for _ in range(5)]

# ---------------------------------------------------------------- plumbing (known cases only)
t0 = TAUS[0]; plumb = {}
plumb["jtheta_vs_series"] = float(max(abs(th(n, uu, t0) / th_series(n, uu, t0) - 1) for n in (1, 2, 3, 4) for uu in PTS))
plumb["th1p_vs_2pi_eta3"] = float(abs(d1(t0) / (2 * mp.pi * eta(t0) ** 3) - 1))
plumb["thc_vs_series"] = float(max(abs(thc(a, b, uu, 2 * t0) / mp.fsum(mp.exp(I * mp.pi * 2 * t0 * (n + a) ** 2 + 2 * I * mp.pi * (n + a) * (uu + b)) for n in range(-30, 31)) - 1)
                                   for (a, b) in [(mp.mpf("0.1"), mp.mpf("0.3")), (mp.mpf("-0.27"), mp.mpf("0.6"))] for uu in PTS))
OUT["plumbing"] = plumb

# ---------------------------------------------------------------- U0, the frame
def holonomy_err(x, y, u, t, frame=True):
    (ax, bx), (ay, by) = x, y
    B0 = bil(x, y, u, t, frame)
    B1 = bil(x, y, u + 1, t, frame); Bt = bil(x, y, u + t, t, frame)
    la = mp.exp(2 * I * mp.pi * (ax + ay)); lb = mp.exp(2 * I * mp.pi * (-(bx + by) / 2))
    Ea = B1 - la * QI * B0 * QI.T; Eb = Bt - lb * QJ * B0 * QJ.T
    nrm = max(abs(B0[m, n]) for m in range(2) for n in range(2))
    return (float(max(abs(Ea[m, n]) for m in range(2) for n in range(2)) / nrm),
            float(max(abs(Eb[m, n]) for m in range(2) for n in range(2)) / nrm))


u0a = []; u0b_naive = []
for t in TAUS[:2]:
    for (x, y) in PAIRS:
        for uu in PTS:
            u0a.append(max(holonomy_err(x, y, uu, t)))
            u0b_naive.append(holonomy_err(x, y, uu, t, frame=False)[1])
OUT["U0"] = {"a_max_rel_err": max(u0a), "b_naive_tau_law_min_rel_err": min(u0b_naive),
             "holds": max(u0a) < 1e-25 and min(u0b_naive) > 1e-6}

# ---------------------------------------------------------------- U1, the form
C_OF = {"i": -1, "j": -1, "k": I}


def form(x, y, t, pts=PTS):
    A = x[0] + y[0]; ub = wpt(x, t) + wpt(y, t); de = wpt(x, t) - wpt(y, t); res = {}
    for s in "1ijk":
        vals = [pairing(UNITS[s], x, y, uu, t) * th(1, uu, t) * mp.exp(-2 * I * mp.pi * A * uu) / th(TH_OF[s], uu + ub, t) for uu in pts]
        res[s] = (vals[0], float(max(abs(v / vals[0] - 1) for v in vals[1:])))
    return res, ub, de


u1a = []; u1b = []; c1_over = []
for t in TAUS[:2]:
    for (x, y) in PAIRS:
        res, ub, de = form(x, y, t)
        u1a.append(max(res[s][1] for s in "1ijk"))
        rat = {s: res[s][0] / (C_OF[s] * th(TH_OF[s], de, t)) for s in "ijk"}
        u1b.append(float(max(abs(rat[s] / rat["i"] - 1) for s in "ijk")))
        c1_over.append(res["1"][0] / (th(1, de, t) * rat["i"]))           # the odd unit's c_1, read out
ref = []
for t in TAUS[:2]:
    for uu in PTS:
        for s in "ijk":
            ref.append(abs(pairing(UNITS[s], (0, 0), (0, 0), uu, t) / (C_OF[s] * th(TH_OF[s], 0, t) * th(TH_OF[s], uu, t) / th(1, uu, t)) - 1))
c1_spread = float(max(abs(c / c1_over[0] - 1) for c in c1_over))
OUT["U1"] = {"a_const_in_u_max": max(u1a), "b_common_ratio_max": max(u1b), "c_untwisted_vs_R2_max": float(max(ref)),
             "c1_read_out": mp.nstr(c1_over[0], 12), "c1_spread": c1_spread,
             "holds": max(u1a) < 1e-25 and max(u1b) < 1e-25 and float(max(ref)) < 1e-25 and c1_spread < 1e-20}

# ---------------------------------------------------------------- U2, R.R
def residues(x, y, t, rad=mp.mpf("0.02"), N=96):
    out = {}
    for s in "1ijk":
        acc = 0
        for m in range(N):
            uu = rad * mp.exp(2 * I * mp.pi * m / N); acc += pairing(UNITS[s], x, y, uu, t) * uu
        out[s] = acc / N
    return out


def rr(R): return sum(R[s] ** 2 for s in "ijk")
def rel_rr(R): return float(abs(rr(R)) / sum(abs(R[s]) ** 2 for s in "ijk"))


u2a = []; u2b = []
for t in TAUS[:2]:
    for (x, y) in PAIRS:
        R = residues(x, y, t); res, ub, de = form(x, y, t, PTS[:2])
        kap = res["i"][0] / (C_OF["i"] * th(2, de, t))
        pred = (kap / d1(t)) ** 2 * th(1, ub, t) ** 2 * th(1, de, t) ** 2
        u2a.append(float(abs(rr(R) / pred - 1)))
        u2b.append(rel_rr(residues(x, x, t)))
Xq, Yq = mp.mpc(0.17, 0.23), mp.mpc(-0.31, 0.12); t = TAUS[0]
quartic = float(abs((th(2, Xq, t) ** 2 * th(2, Yq, t) ** 2 + th(4, Xq, t) ** 2 * th(4, Yq, t) ** 2 - th(3, Xq, t) ** 2 * th(3, Yq, t) ** 2)
                    / (th(1, Xq, t) ** 2 * th(1, Yq, t) ** 2) - 1))
# the eps^2 scaling: delta fixed by y, ubar = eps * u0 by choosing x = (eps*u0 - w_y) ... in twist coordinates
yb = (mp.mpf("0.11"), mp.mpf("0.37")); wy = wpt(yb, t); u0 = mp.mpc(0.6, 0.35)
def twist_of(w, t): return (mp.im(w) / mp.im(t), 2 * (mp.re(w) - mp.re(t) * mp.im(w) / mp.im(t)))
epss = [mp.mpf(10) ** (-k) for k in (1, 2, 3, 4)]; vals = []
for ep in epss:
    xw = ep * u0 - wy; xb = twist_of(xw, t)
    vals.append(rel_rr(residues(xb, yb, t)))
slopes = [float((mp.log(vals[k + 1]) - mp.log(vals[k])) / (mp.log(epss[k + 1]) - mp.log(epss[k]))) for k in range(3)]
OUT["U2"] = {"a_RR_vs_formula_max": max(u2a), "b_majorana_max": max(u2b), "c_quartic": quartic,
             "d_eps_slopes": slopes,
             "holds": max(u2a) < 1e-20 and max(u2b) < 1e-25 and quartic < 1e-25 and all(abs(s - 2) < 0.05 for s in slopes)}

# ---------------------------------------------------------------- U3, the shifts
def four(x, y, t, uu): return [pairing(UNITS[s], x, y, uu, t) for s in "1ijk"]


def common_scalar_err(v, w):
    lam = w[0] / v[0] if abs(v[0]) > abs(v[1]) else w[1] / v[1]
    return float(max(abs(w[k] - lam * v[k]) for k in range(4)) / max(abs(z) for z in w))


def signed_perm_err(v, w):
    """smallest error over permutations p and signs: w ~ lam * (signs * v[p])"""
    import itertools
    best = 1e9
    for p in itertools.permutations(range(4)):
        vp = [v[k] for k in p]
        k0 = max(range(4), key=lambda k: abs(vp[k])); lam = w[k0] / vp[k0]
        errs = [min(abs(w[k] - lam * vp[k]), abs(w[k] + lam * vp[k])) for k in range(4)]
        best = min(best, max(errs) / max(abs(z) for z in w))
    return float(best)


u3a = []; u3b = []
for t in TAUS[:2]:
    for (x, y) in PAIRS[:3]:
        for uu in PTS[:2]:
            v = four(x, y, t, uu)
            # lattice shifts of x: w -> w + tau (a -> a + 1), w -> w + 1 (b -> b + 2); the e^{2 pi i A u} factor
            # changes by e^{2 pi i u} under a -> a + 1, a common scalar at fixed u
            u3a.append(common_scalar_err(v, four((x[0] + 1, x[1]), y, t, uu)))
            u3a.append(common_scalar_err(v, four((x[0], x[1] + 2), y, t, uu)))
            # half-period shifts of x: w -> w + 1/2 (b -> b + 1), w -> w + tau/2 (a -> a + 1/2), and both
            for sh in [(0, 1), (mp.mpf(1) / 2, 0), (mp.mpf(1) / 2, 1)]:
                u3b.append(signed_perm_err(v, four((x[0] + sh[0], x[1] + sh[1]), y, t, uu)))
OUT["U3"] = {"a_lattice_max": max(u3a), "b_half_period_max": max(u3b),
             "holds": max(u3a) < 1e-20 and max(u3b) < 1e-20}

# ---------------------------------------------------------------- U4, the lines on the record
SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
SECTORS = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}


def field_twist(w_line, f, t):
    """the field's twist (a, b) for line point 6Y * w_line"""
    return twist_of(SIXY[f] * w_line, t)


def line_point(p, q, t): return p * t + q          # the line w = p tau + q, (p, q) in the SM seat's lattice coordinates


def sector_R(wl, sec, t):
    f1, f2 = SECTORS[sec]
    return residues(field_twist(wl, f1, t), field_twist(wl, f2, t), t)


def prop_err(Ra, Rb):
    va = [Ra[s] for s in "ijk"]; vb = [Rb[s] for s in "ijk"]
    k0 = max(range(3), key=lambda k: abs(va[k])); lam = vb[k0] / va[k0]
    return float(max(abs(vb[k] - lam * va[k]) for k in range(3)) / max(abs(z) for z in vb))


om = TAUS[2]; tg = TAUS[0]
u4 = {"a_zero": [], "b_torsion3": [], "c_half": [], "c_prop": [], "d_quarks": [], "d_leptons": []}
for t in (om, tg):
    for sec in SECTORS:
        u4["a_zero"].append(rel_rr(sector_R(0, sec, t)))
    for (p, q) in [(0, mp.mpf(1) / 2), (mp.mpf(1) / 2, 0), (mp.mpf(1) / 2, mp.mpf(1) / 2)]:
        wl = line_point(p, q, t); Rs = {sec: sector_R(wl, sec, t) for sec in SECTORS}
        u4["c_half"] += [rel_rr(Rs[sec]) for sec in SECTORS]
        u4["c_prop"] += [prop_err(Rs["down"], Rs["up"]), prop_err(Rs["down"], Rs["lep"])]
third = mp.mpf(1) / 3
for (p, q) in [(i * third, j * third) for i in range(3) for j in range(3) if (i, j) != (0, 0)]:
    wl = line_point(p, q, om)
    u4["b_torsion3"] += [rel_rr(sector_R(wl, sec, om)) for sec in SECTORS]
ninth = mp.mpf(1) / 9
higgs_lines = []
for base in [(ninth, ninth), (2 * ninth, 2 * ninth)]:
    for i in range(3):
        for j in range(3):
            higgs_lines.append((base[0] + i * third, base[1] + j * third))
for (p, q) in higgs_lines:
    wl = line_point(p, q, om)
    u4["d_quarks"] += [rel_rr(sector_R(wl, "up", om)), rel_rr(sector_R(wl, "down", om))]
    u4["d_leptons"].append(rel_rr(sector_R(wl, "lep", om)))
OUT["U4"] = {k: [min(v), max(v)] for k, v in u4.items()}
OUT["U4"]["holds"] = (max(u4["a_zero"]) < 1e-25 and max(u4["b_torsion3"]) < 1e-25 and min(u4["c_half"]) > 1e-3
                      and max(u4["c_prop"]) < 1e-20 and min(u4["d_quarks"]) > 1e-3 and max(u4["d_leptons"]) < 1e-25)

# ---------------------------------------------------------------- U5, the masses' zero pattern
def takagi_min_ratio(R, a):
    Rv = np.array([complex(R[s]) for s in "ijk"]); av = np.array(a, dtype=complex)
    Y = np.outer(av, Rv) + np.outer(Rv, av) - (av @ Rv) * np.eye(3)
    sv = np.linalg.svd(Y, compute_uv=False)
    return float(sv[-1] / sv[0])


dirs = [rng.normal(size=3) + 1j * rng.normal(size=3) for _ in range(20)]      # the democratic direction is a read-out (U6)
u5_null = []; u5_lift = []
cases = [(0, "down", om, True), (line_point(third, 0, om), "down", om, True)]
cases += [(line_point(0, mp.mpf(1) / 2, om), sec, om, False) for sec in SECTORS]
cases += [(line_point(ninth, ninth, om), "lep", om, True), (line_point(ninth, ninth, om), "down", om, False)]
for (wl, sec, t, null) in cases:
    R = sector_R(wl, sec, t)
    for a in dirs:
        (u5_null if null else u5_lift).append(takagi_min_ratio(R, a))
OUT["U5"] = {"null_cases_max": max(u5_null), "lifted_cases_min": min(u5_lift),
             "holds": max(u5_null) < 1e-20 and min(u5_lift) > 1e-8}

# ---------------------------------------------------------------- U6, read-outs
ro = {}
for (name, wl) in [("half (0, 1/2)", line_point(0, mp.mpf(1) / 2, om)), ("half (1/2, 0)", line_point(mp.mpf(1) / 2, 0, om)),
                   ("half (1/2, 1/2)", line_point(mp.mpf(1) / 2, mp.mpf(1) / 2, om)), ("higgs (1/9, 1/9)", line_point(ninth, ninth, om))]:
    R = sector_R(wl, "down", om)
    sv = np.linalg.svd((lambda Rv, av: np.outer(av, Rv) + np.outer(Rv, av) - (av @ Rv) * np.eye(3))(
        np.array([complex(R[s]) for s in "ijk"]), np.array([1.0, 1.0, 1.0], dtype=complex)), compute_uv=False)
    ro[name] = {"RR_rel_down": rel_rr(R), "democratic_m1_m3": float(sv[-1] / sv[0]), "democratic_m2_m3": float(sv[1] / sv[0])}
OUT["U6_read_out"] = ro

(HERE / "twisted_zero_mode.json").write_text(json.dumps(OUT, indent=1, default=str))
for k in ("plumbing", "U0", "U1", "U2", "U3", "U4", "U5"):
    print(k, OUT[k])
