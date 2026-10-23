"""Data-free: main's DR = q R' + E2 R / 24 (the Serre derivative in weight -1/2, checked by a least-squares fit of DR on
q R' and E2 R at three tau); the family h(lambda) = DR + lambda R (R null, R.DR = 0, so h.h = DR.DR for every lambda)
and its departures from the leading null eigenline; the Maass-Shimura derivative of R in main's weight -1/2,
q R' + R/(8 pi y) = DR - (E2*/24) R (E2* = E2 - 3/(pi y)), as one member."""
import contextlib, importlib.util, io, sys, math, pathlib
import numpy as np
import mpmath as mp
ZF = pathlib.Path(__file__).resolve().parents[2] / "chat1_2026-10-23_zero_free_frame"
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("zfc", ZF / "zero_free_census.py"); zfc = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(zfc)
rbs = zfc.rbs
mp.mp.dps = 30
f1 = np.array([0, 1, -1j]) / math.sqrt(2); f2 = np.array([1, 0, 0], dtype=complex); f3 = np.array([0, 1, 1j]) / math.sqrt(2)
def E2(t):
    q = mp.exp(2j * mp.pi * t); return complex(1 - 24 * mp.fsum(n * q ** n / (1 - q ** n) for n in range(1, 80)))
def R_at(t): return rbs.at(rbs.R, t.real, t.imag)
def DR_at(t): return rbs.at(rbs.H1, t.real, t.imag)
def dep(v):
    c = np.array([np.vdot(f2, v), np.vdot(f3, v), np.vdot(f1, v)])
    lead = 1 if abs(c[1]) >= abs(c[2]) else 2
    return abs(c[0] / c[lead]), abs(c[3 - lead] / c[lead]), ["h0", "conj h0"][lead - 1], abs(v @ v) / np.vdot(v, v).real
for t in (complex(0.3, 2.2), complex(0.1, 1.2)):
    h = 1e-6; qRp = (R_at(t + h) - R_at(t - h)) / (2 * h) / (2j * math.pi)
    A = np.stack([qRp, E2(t) * R_at(t)], axis=1); D = DR_at(t)
    coef = np.linalg.lstsq(A, D, rcond=None)[0]
    print(f"tau {t}: DR = a qR' + b E2 R with a = {coef[0]:.6f}, b = {coef[1]:.6f} (1/24 = {1/24:.6f}), residual {np.linalg.norm(D - A @ coef) / np.linalg.norm(D):.1e}")
for y in (2.3, 2.6, 3.0):
    t = complex(0.3, y); r = math.exp(-math.pi * y); R0, D0 = R_at(t), DR_at(t)
    lam_maass = -(E2(t) - 3 / (math.pi * y)) / 24
    print(f"Im tau {y}: |R.DR| / (|R||DR|) = {abs(R0 @ D0) / (np.linalg.norm(R0) * np.linalg.norm(D0)):.1e}")
    for lab, lam in (("DR (lambda 0)", 0), ("Maass, weight -1/2", lam_maass), ("lambda = -0.02", -0.02), ("lambda = -0.035", -0.035), ("lambda = +0.02", 0.02)):
        v = D0 + lam * R0
        de, ep, lead, nul = dep(v)
        print(f"   {lab:20s} lambda {complex(lam).real:+.4f}: delta {de:.4f} ({de / r ** 0.5:6.2f} r^1/2), eps {ep:.5f} ({ep / r:6.2f} r), lead {lead}, |h.h|/|h|^2 {nul:.4f}, delta^2/2eps {de * de / (2 * ep):.2f}")
