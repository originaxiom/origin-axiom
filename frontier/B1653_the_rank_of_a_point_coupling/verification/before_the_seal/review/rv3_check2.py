"""Reviewer, third pass: the five plumbing quantities against < 1e-30, with the reviewer's jtheta-based reimplementation
of the documented formulas (not the instrument), on the seeded PAIRS; and the changed code's Python constructs."""
import itertools, json
import numpy as np
import mpmath as mp
mp.mp.dps = 40
I = mp.mpc(0, 1)

def thj(n, u, t):
    q = mp.exp(I * mp.pi * t); x = mp.pi * u
    if n in (3, 4): return mp.jtheta(n, x, q)
    q4 = mp.exp(I * mp.pi * t / 4); s = x + mp.pi * t / 2
    return q4 * mp.exp(I * x) * mp.jtheta(3, s, q) if n == 2 else -I * q4 * mp.exp(I * x) * mp.jtheta(4, s, q)
def thc(a, b, u, T): return mp.exp(I * mp.pi * a * a * T + 2 * I * mp.pi * a * (u + b)) * thj(3, u + a * T + b, T)
def ser(n, u, t, N=30):
    e = lambda x: mp.exp(I * mp.pi * x); K = range(-N, N + 1); h = mp.mpf(1) / 2
    if n == 1: return -I * mp.fsum((-1) ** k * e(t * (k + h) ** 2 + (2 * k + 1) * u) for k in K)
    if n == 2: return mp.fsum(e(t * (k + h) ** 2 + (2 * k + 1) * u) for k in K)
    if n == 3: return mp.fsum(e(t * k * k + 2 * k * u) for k in K)
    return mp.fsum((-1) ** k * e(t * k * k + 2 * k * u) for k in K)
eta = lambda t: mp.exp(I * mp.pi * t / 12) * mp.qp(mp.exp(2 * I * mp.pi * t))
OMEGA = mp.exp(2 * I * mp.pi / 3)
TAUS = [mp.mpc(0.13, 1.07), mp.mpc(-0.31, 0.88), OMEGA]
PTS = [mp.mpc(0.21, 0.17), mp.mpc(0.33, -0.12), mp.mpc(-0.4, 0.29)]
rng = np.random.default_rng(16531)
rnd_twist = lambda: (mp.mpf(rng.uniform(-0.5, 0.5)), mp.mpf(rng.uniform(-1, 1)))
PAIRS = [(rnd_twist(), rnd_twist()) for _ in range(5)]

pl = {}
pl["jtheta_vs_series"] = max(abs(thj(n, u, t) / ser(n, u, t) - 1) for n in (1, 2, 3, 4) for u in PTS for t in (TAUS[0], OMEGA))
pl["th1p_vs_2pi_eta3"] = max(abs(mp.diff(lambda u: thj(1, u, t), 0) / (2 * mp.pi * eta(t) ** 3) - 1) for t in TAUS)
pl["thc_vs_series"] = max(abs(thc(a, b, u, 2 * TAUS[0]) / mp.fsum(mp.exp(I * mp.pi * 2 * TAUS[0] * (n + a) ** 2 + 2 * I * mp.pi * (n + a) * (u + b)) for n in range(-30, 31)) - 1)
                          for (a, b) in [(mp.mpf("0.1"), mp.mpf("0.3")), (mp.mpf("-0.27"), mp.mpf("0.6"))] for u in PTS)
def omega_fixed(z):
    d = OMEGA * z - z; n = mp.im(d) / mp.im(OMEGA); m = mp.re(d) - n * mp.re(OMEGA)
    return max(abs(n - mp.nint(n)), abs(m - mp.nint(m)))
line_w = lambda p1, p2, t: p1 * t - p2
pl["w59_both_families"] = max(omega_fixed(3 * line_w(base + i_ / mp.mpf(3), base + j_ / mp.mpf(3), OMEGA))
                              for base in (mp.mpf(1) / 9, mp.mpf(2) / 9) for i_ in range(3) for j_ in range(3))
QI = mp.matrix([[I, 0], [0, -I]]); QJ = mp.matrix([[0, 1], [-1, 0]]); QK = QI * QJ; ONE = mp.eye(2)
UNITS = {"1": ONE, "i": QI, "j": QJ, "k": QK}
def bil(x, y, u, t):
    (ax, bx), (ay, by) = x, y; T = 2 * t; t1 = thj(1, u, t)
    den = I * mp.exp(-I * mp.pi * t / 2) * mp.exp(-I * mp.pi * u) * t1
    X0, X1, Y0, Y1 = thc(ax, bx, u, T), thc(ax, bx, u + t, T), thc(ay, by, u, T), thc(ay, by, u + t, T)
    return mp.matrix([[X0 * Y0 / t1, mp.exp(I * mp.pi * by) * X0 * Y1 / den],
                      [mp.exp(I * mp.pi * bx) * X1 * Y0 / den, mp.exp(I * mp.pi * (bx + by)) * X1 * Y1 / thj(1, u + t, t)]])
def four(x, y, t, u):
    M = bil(x, y, u, t); return [sum((QJ * UNITS[s])[m, n] * M[m, n] for m in range(2) for n in range(2)) for s in "1ijk"]
def spe(v, w):
    best = None
    for p in itertools.permutations(range(4)):
        vp = [v[k] for k in p]; k0 = max(range(4), key=lambda k: abs(vp[k])); lam = w[k0] / vp[k0]
        e = max(min(abs(w[k] - lam * vp[k]), abs(w[k] + lam * vp[k])) for k in range(4)) / max(abs(z) for z in w)
        best = e if best is None or e < best else best
    return best
pl["half_period_signed_perm"] = max(spe(four(x, y, TAUS[0], PTS[0]), four((x[0] + sh[0], x[1] + sh[1]), y, TAUS[0], PTS[0]))
                                    for (x, y) in PAIRS[:3] for sh in [(0, 1), (mp.mpf(1) / 2, 0), (mp.mpf(1) / 2, 1)])
for k, v in pl.items(): print(f"  {k:26s} {mp.nstr(v, 3):>10s}   < 1e-30: {v < 1e-30}")

# the changed code's constructs
u6 = {"a": {"det_min": 1e-38, "det_max": 2e-38}}
out = {"U6": {**u6, "holds": True}, "U4": {"a_max_1_minus_overlap": mp.nstr(mp.mpf(0), 5), "holds": mp.mpf(-1e-41) < mp.mpf("1e-25")}}
print(" ", json.dumps(out, default=str), "| type of mp comparison:", type(mp.mpf(1) < mp.mpf(2)).__name__)
