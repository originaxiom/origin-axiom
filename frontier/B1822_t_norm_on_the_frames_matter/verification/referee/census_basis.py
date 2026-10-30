#!/usr/bin/env python3
"""Referee check (data-free): (1) the frame's coupling() is the bilinear of the modes C_a F_x and C_b F_y, read against my
own product-formula modes; (2) T-NORM is load-bearing: on a frame-built Y (b1656_funcs' residues, cA, weighted_M, a
generic imaginary-quaternion S, a generic end radius), a kinetic metric H != I moves the outputs, within the bound
sqrt(cond H_L cond H_R) for the ratios; H = c I leaves them unchanged.  No census row is read; no measured value is used.
    OMP_NUM_THREADS=1 nice -n 10 python3 -I census_basis.py"""
import contextlib, importlib.util, io, json, math, pathlib, sys
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "frontier").is_dir() and (p / "GENESIS.md").is_file())
sys.path.insert(0, str(HERE))
import independent as I

spec = importlib.util.spec_from_file_location("b1656_ro", next(ROOT.glob("frontier/B1691_*/verification")) / "correction" / "b1656_funcs.py")
B = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(B)

rng = np.random.default_rng(31)
out = {}
# (1) the coupling's basis, pointwise
worst = 0.0
for _ in range(20):
    tau = complex(rng.uniform(0, 0.5), rng.uniform(1.0, 3.5)); line = (Fr(int(rng.integers(0, 12)), 12), Fr(int(rng.integers(0, 12)), 12))
    ql, qr = [(1, -4), (1, 2), (-3, 6)][int(rng.integers(0, 3))]
    x = (float(ql * line[0]), float(-2 * ql * line[1])); y = (float(qr * line[0]), float(-2 * qr * line[1]))
    z = complex(rng.uniform(0.1, 0.9), 0) + rng.uniform(0.1, 0.9) * tau
    S = sum(c * Q for c, Q in zip(rng.normal(size=3) + 1j * rng.normal(size=3), (B.QI, B.QJ, B.QK)))
    Mf = np.array(B.bil(x, y, np.array(z), tau), dtype=complex)
    # my modes' holomorphic bilinear F_x F_y^T with the frame's branch (s0 s1 = den)
    T = 2 * tau; t0 = I.theta1(np.array(z), tau); t1 = I.theta1(np.array(z + tau), tau)
    den = 1j * np.exp(-1j * np.pi * tau / 2) * np.exp(-1j * np.pi * z) * t0
    X0 = I.theta_ab(Fr(x[0]).limit_denominator(1000), x[1], np.array(z), T); X1 = np.exp(1j * np.pi * x[1]) * I.theta_ab(Fr(x[0]).limit_denominator(1000), x[1], np.array(z + tau), T)
    Y0 = I.theta_ab(Fr(y[0]).limit_denominator(1000), y[1], np.array(z), T); Y1 = np.exp(1j * np.pi * y[1]) * I.theta_ab(Fr(y[0]).limit_denominator(1000), y[1], np.array(z + tau), T)
    Mm = np.array([[X0 * Y0 / t0, X0 * Y1 / den], [X1 * Y0 / den, X1 * Y1 / t1]], dtype=complex)
    Yf = B.coupling(S, Mf)
    Yd = np.array([[np.sum((Ca.T @ B.EPS @ S @ Cb) * Mm) for Cb in I.BL] for Ca in I.BL])
    worst = max(worst, float(np.max(np.abs(Yf - Yd)) / np.max(np.abs(Yd))), float(np.max(np.abs(Mf - Mm)) / np.max(np.abs(Mm))))
out["(1) frame's coupling/bil vs (C_a F_x)^T eps S (C_b F_y) from my modes, max rel"] = worst
print("(1)", worst, flush=True)


def outputs(Yu, Yd):
    r = {}
    U = {}
    for nm, Y in (("up", Yu), ("down", Yd)):
        u_, s, _ = np.linalg.svd(Y); o = np.argsort(s); s = s[o]; U[nm] = u_[:, o]; r[nm] = [s[0] / s[2], s[1] / s[2]]
    V = U["up"].conj().T @ U["down"]; r["V"] = [abs(V[0, 1]), abs(V[1, 2]), abs(V[0, 2])]
    r["J"] = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    return r


def phys(Y, HL, HR):
    def mhalf(H):
        w, v = np.linalg.eigh(H); return v @ np.diag(w ** -0.5) @ v.conj().T
    return mhalf(HL).T @ Y @ mhalf(HR)


# (2) a frame-built Y at one configuration (generic S and end radius; not a census row)
tau = 0.31 + 1.73j; line = (Fr(2, 5), Fr(3, 10)); Lr = 2.0
S = 0.6 * B.QI + (0.3 + 0.2j) * B.QJ + (0.5 - 0.4j) * B.QK
Ys = {}
for sn, ql, qr in (("up", 1, -4), ("down", 1, 2)):
    w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
    R = B.residues(x, yy, tau); c = B.cA(x, yy, tau, R)
    u = {k: (math.sqrt(2 * math.pi * Lr + c[k]) * R[k] if c[k] is not None and 2 * math.pi * Lr + c[k] > 0 else 0) for k in B.UNITS}
    Ys[sn] = B.coupling(S, B.weighted_M(u))
base = outputs(Ys["up"], Ys["down"])
out["(2) base outputs (H = I), generic S, L = 2, tau = 0.31+1.73i, line (2/5, 3/10)"] = base
cases = {}
for nm, (HQ, Hu, Hd) in {
        "H = 3.7 I on Q (a scale)": (3.7 * np.eye(3), np.eye(3), np.eye(3)),
        "H_Q = diag(1, 1, 1.1) (a weight on the k mode)": (np.diag([1, 1, 1.1]), np.eye(3), np.eye(3)),
        "H_Q with a 0.05 mixing (j, k)": (np.array([[1, 0, 0.05], [0, 1, 0], [0.05, 0, 1]], dtype=complex), np.eye(3), np.eye(3)),
        "H_u = H_d = I + 0.1 (J - I) (democratic, the SU(2)-diagonal family)": (np.eye(3), np.eye(3) + 0.1 * (np.ones((3, 3)) - np.eye(3)), np.eye(3) + 0.1 * (np.ones((3, 3)) - np.eye(3)))}.items():
    o = outputs(phys(Ys["up"], HQ, Hu), phys(Ys["down"], HQ, Hd))
    dmax = max(abs(math.log10(o[s][i] / base[s][i])) for s in ("up", "down") for i in range(2))
    bound = max(0.5 * math.log10(np.linalg.cond(HQ) * np.linalg.cond(H)) for H in (Hu, Hd))
    dV = max(abs(o["V"][i] - base["V"][i]) for i in range(3))
    cases[nm] = {"max |log10 ratio change|": dmax, "bound log10 sqrt(cond_L cond_R)": bound, "within bound": bool(dmax <= bound + 1e-12), "max |V change|": dV}
    print(nm, cases[nm], flush=True)
out["(2) kinetic metrics"] = cases
json.dump(out, open(HERE / "census_basis.json", "w"), indent=1, default=str)
