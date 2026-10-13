#!/usr/bin/env python3
"""B1642 -- THE GOLDEN COUPLING AS THE ZERO MODES' RESIDUE AT THE PUNCTURE (sealed before this runs; PREREGISTRATION.md).

The zero mode (the SM seat's W21): F = (f(z), f(z + tau)) dz, f(z) = theta_3(z; 2 tau) / sqrt(theta_1(z; tau)); in parity
block p, F_p = C_p F with C_p = j, i, k for the parities (1/2, 0), (0, 1/2), (1/2, 1/2).  Theta functions in the pi z
convention, summed as series in tau (no nome root).  The branch: f(z)^2 and f(z + tau)^2 are single-valued; the product
f(z) f(z + tau) is taken as theta_3(z; 2tau) theta_3(z + tau; 2tau) / (i e^{-i pi tau/2} e^{-i pi z} theta_1(z; tau)), the
square root of theta_1(z) theta_1(z + tau) = -e^{-i pi tau} e^{-2 pi i z} theta_1(z)^2 fixed once (disclosed).

  R1  F^T eps F = 0                         R2  F^T eps C F = c theta_r(0) theta_r(z) / theta_1(z), (i,2), (j,4), (k,3)
  R3  residues at z = 0 by a contour        R4  Y_pq = Res F_p^T eps F_q against B1636's golden coupling; the tick's axis
  R5  the characters of the off-diagonal    R6  control: B = diag(1, 2) does not factor

    python3 -B residue_coupling.py      # writes residue_coupling.json beside itself
"""
import json, pathlib
import mpmath as mp
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
mp.mp.dps = 40
NS = range(-30, 31)
I = mp.mpc(0, 1)


def th(n, z, t):
    e = lambda x: mp.exp(I * mp.pi * x)
    if n == 1: return -I * mp.fsum((-1) ** k * e(t * (k + mp.mpf(1) / 2) ** 2 + (2 * k + 1) * z) for k in NS)
    if n == 2: return mp.fsum(e(t * (k + mp.mpf(1) / 2) ** 2 + (2 * k + 1) * z) for k in NS)
    if n == 3: return mp.fsum(e(t * k * k + 2 * k * z) for k in NS)
    if n == 4: return mp.fsum((-1) ** k * e(t * k * k + 2 * k * z) for k in NS)


def eta(t):
    return mp.exp(I * mp.pi * t / 12) * mp.fprod(1 - mp.exp(2 * I * mp.pi * t * n) for n in range(1, 200))


def quad(z, t):
    """(f^2, f f', f'^2) with f' = f(z + tau), the branch fixed as in the docstring"""
    t1 = th(1, z, t)
    a = th(3, z, 2 * t); b = th(3, z + t, 2 * t)
    ff = a * a / t1
    fpfp = b * b / th(1, z + t, t)
    ffp = a * b / (I * mp.exp(-I * mp.pi * t / 2) * mp.exp(-I * mp.pi * z) * t1)
    return ff, ffp, fpfp


QI = mp.matrix([[I, 0], [0, -I]]); QJ = mp.matrix([[0, 1], [-1, 0]]); QK = QI * QJ
EPS = QJ
UNITS = {"i": QI, "j": QJ, "k": QK}
R_OF = {"i": 2, "j": 4, "k": 3}
BLOCKS = [("(1/2,0)", QJ), ("(0,1/2)", QI), ("(1/2,1/2)", QK)]


def bil(M, z, t):
    ff, ffp, fpfp = quad(z, t)
    return M[0, 0] * ff + (M[0, 1] + M[1, 0]) * ffp + M[1, 1] * fpfp


def residue(M, t, rad=mp.mpf("0.05"), N=64):
    s = 0
    for n in range(N):
        w = mp.exp(2 * I * mp.pi * n / N); z = rad * w
        s += bil(M, z, t) * z
    return s / N


rng = np.random.default_rng(1642)
rt = lambda: mp.mpc(rng.uniform(-0.5, 0.5), rng.uniform(0.7, 1.8))
rz = lambda: mp.mpc(rng.uniform(0.05, 0.45), rng.uniform(0.05, 0.4))
out = {}

# R1
out["R1_max_abs"] = float(max(abs(bil(EPS, rz(), rt())) for _ in range(20)))

# R2
R2 = {}
for name, C in UNITS.items():
    r = R_OF[name]; cs = []; errs = []
    for _ in range(20):
        z, t = rz(), rt()
        g = bil(EPS * C, z, t)
        closed = th(r, 0, t) * th(r, z, t) / th(1, z, t)
        c = g / closed; cs.append(c)
    c0 = cs[0]
    R2[name] = {"theta": r, "c_values": sorted({(round(float(c.real), 12), round(float(c.imag), 12)) for c in cs}),
                "max_rel_spread": float(max(abs(c - c0) for c in cs) / abs(c0))}
out["R2"] = R2

# R3
R3 = {}
for name, C in UNITS.items():
    r = R_OF[name]; errs = []; cs = []
    for _ in range(10):
        t = rt()
        res = residue(EPS * C, t)
        pred = th(r, 0, t) ** 2 / (mp.pi * th(2, 0, t) * th(3, 0, t) * th(4, 0, t))
        pred_eta = th(r, 0, t) ** 2 / (2 * mp.pi * eta(t) ** 3)
        cs.append(res / pred); errs.append(abs(pred - pred_eta) / abs(pred))
    R3[name] = {"c_values": sorted({(round(float(c.real), 12), round(float(c.imag), 12)) for c in cs}),
                "max_rel_spread": float(max(abs(c - cs[0]) for c in cs) / abs(cs[0])),
                "theta1prime_equals_2eta3_max_rel": float(max(errs))}
out["R3"] = R3


# R4
def Y_of(t):
    Y = np.zeros((3, 3), dtype=complex)
    for a, (_, Ca) in enumerate(BLOCKS):
        for b, (_, Cb) in enumerate(BLOCKS):
            M = Ca.T * EPS * Cb
            Y[a, b] = complex(residue(M, t))
    return Y


def golden(t):
    t2, t3, t4 = (complex(th(n, 0, t) ** 2) for n in (2, 3, 4))
    return np.array([[0, t4, t3], [t4, 0, t2], [t3, t2, 0]], dtype=complex)


def sv(A):
    s = np.linalg.svd(A, compute_uv=False); return s / s[0]


R4 = {"diag_max_abs": 0.0, "sv_max_diff_random": 0.0, "axis": []}
for _ in range(10):
    t = rt(); Y = Y_of(t)
    R4["diag_max_abs"] = max(R4["diag_max_abs"], float(max(abs(Y[k, k]) for k in range(3)) / np.abs(Y).max()))
    R4["sv_max_diff_random"] = max(R4["sv_max_diff_random"], float(np.max(np.abs(sv(Y) - sv(golden(t))))))
phi = (1 + 5 ** 0.5) / 2
gold = np.array([1, 1 / phi, 1 / phi ** 2])
for th_ in (0.4, 0.9, 1.3, 1.9, 2.6):
    t = mp.mpf(1) / 2 + mp.sqrt(5) / 2 * mp.exp(I * th_)
    s = sv(Y_of(t)); R4["axis"].append({"theta": th_, "sv": [round(float(x), 15) for x in s], "max_diff_from_golden": float(np.max(np.abs(s - gold)))})
out["R4"] = R4

# R5
R5 = {}
for name, C in UNITS.items():
    r = R_OF[name]; ch = set()
    for _ in range(10):
        z, t = rz(), rt()
        g0 = bil(EPS * C, z, t); g1 = bil(EPS * C, z + 1, t); gt = bil(EPS * C, z + t, t)
        ch.add((round(float((g1 / g0).real), 9), round(float((gt / g0).real), 9)))
    R5[name] = {"theta": r, "characters_(a,b)": sorted(ch)}
out["R5"] = R5

# R6
B = mp.matrix([[1, 0], [0, 2]]); R6 = {}
for r in (2, 3, 4):
    t = rt(); rat = []
    for _ in range(8):
        z = rz()
        rat.append(bil(B, z, t) * th(1, z, t) / (th(r, 0, t) * th(r, z, t)))
    m = mp.fsum(rat) / len(rat)
    R6[f"theta{r}"] = float(max(abs(x - m) for x in rat) / abs(m))
out["R6_misfit"] = R6

json.dump(out, open(HERE / "residue_coupling.json", "w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
