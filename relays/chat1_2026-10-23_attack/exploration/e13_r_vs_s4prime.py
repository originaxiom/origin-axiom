"""Data-free check (labelled; committed before its run): is main's record Higgs form R (B1691, weight -1/2, exactly null)
projectively the S4' weight-1 triplet of Novichkov-Penedo-Petcov (arXiv:2006.03058), Y = (sqrt2 eps theta, eps^2,
-theta^2) with theta = Theta3(2 tau), eps = Theta2(2 tau)?  (The literature dive's import 1.)
Every null vector of the bilinear form a^2 + 2bc can be written (sqrt2 s t, s^2, -t^2) up to scale, so with R = a e1 + b n
+ c n-bar (n = F3, n-bar = F1, n.n-bar = 1; b leads at the cusp) the check is whether X = (a/b)/(-sqrt2), whose square is
-c/b, equals eps/theta up to one constant factor.  Printed at twelve tau (Re 0 .. 0.9, Im 0.9 .. 3.4): X / (eps/theta),
the nullity residual, and the same for DR (B1700's h1, the Serre derivative, null too) against the same ratio."""
import contextlib, importlib.util, io, json, math, sys, pathlib
import numpy as np
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parents[1]
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("zfc", HERE.parent / "chat1_2026-10-23_zero_free_frame" / "zero_free_census.py")
zfc = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(zfc)
rbs = zfc.rbs
mp.mp.dps = 30
F1 = np.array([0, 1, -1j]) / math.sqrt(2); F2 = np.array([1, 0, 0], dtype=complex); F3 = np.array([0, 1, 1j]) / math.sqrt(2)
out = []
for re_t, im_t in [(0.0, 0.9), (0.1, 1.2), (0.25, 1.5), (0.3, 1.8), (0.4, 2.0), (0.5, 2.2), (0.6, 2.4), (0.7, 2.6),
                   (0.8, 2.8), (0.9, 3.0), (0.175, 3.2), (0.325, 3.4)]:
    q = mp.exp(2j * mp.pi * mp.mpc(re_t, im_t))
    ratio = complex(mp.jtheta(2, 0, q) / mp.jtheta(3, 0, q))          # Theta2(2 tau) / Theta3(2 tau)
    row = {"tau": [re_t, im_t], "eps/theta": [ratio.real, ratio.imag]}
    for name, sec in (("R", rbs.R), ("DR", rbs.H1)):
        v = rbs.at(sec, re_t, im_t)
        a, b, c = v @ F2, v @ F1, v @ F3                                  # v = a e1 + b n + c n-bar (bilinear)
        X = (a / b) / (-math.sqrt(2))
        row[name] = {"nullity |a^2 + 2bc| / |v|^2": float(abs(a * a + 2 * b * c) / np.vdot(v, v).real),
                     "X / (eps/theta)": [complex(X / ratio).real, complex(X / ratio).imag],
                     "X^2 / (-c/b) - 1": float(abs(X * X / (-c / b) - 1))}
    out.append(row)
print(json.dumps(out, indent=1))
