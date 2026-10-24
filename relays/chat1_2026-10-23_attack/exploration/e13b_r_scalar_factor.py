"""Data-free follow-up to e13 (labelled; committed before its run).  e13 found X'/(eps/theta) = -1 at eight tau and -i at
four with Re tau > 1/2, where mpmath's jtheta takes q^(1/4) on the principal branch.  Here eps = Theta2(2 tau) is summed
with the analytic factor 2 e^{i pi tau / 2} (and eta(tau) = e^{2 pi i tau/24} prod (1 - q^n)), and two things are printed
at the same twelve tau: (i) R's (a, b, c) on (e1, n, n-bar) against (-sqrt2 eps theta, eps^2, -theta^2) - each ratio and
the spread of the three; (ii) whether the common factor is a constant times eta^(-3) (R has weight -1/2, the triplet
weight 1)."""
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


def forms(t):
    q = mp.exp(2j * mp.pi * t)
    theta = 1 + 2 * mp.fsum(q ** (n * n) for n in range(1, 40))
    eps = 2 * mp.exp(1j * mp.pi * t / 2) * mp.fsum(q ** (n * n + n) for n in range(0, 40))
    eta = mp.exp(2j * mp.pi * t / 24) * mp.fprod(1 - q ** n for n in range(1, 200))
    return complex(theta), complex(eps), complex(eta)


out = []
for re_t, im_t in [(0.0, 0.9), (0.1, 1.2), (0.25, 1.5), (0.3, 1.8), (0.4, 2.0), (0.5, 2.2), (0.6, 2.4), (0.7, 2.6),
                   (0.8, 2.8), (0.9, 3.0), (0.175, 3.2), (0.325, 3.4)]:
    th, ep, et = forms(mp.mpc(re_t, im_t))
    v = rbs.at(rbs.R, re_t, im_t)
    a, b, c = v @ F2, v @ F1, v @ F3
    Y = np.array([-math.sqrt(2) * ep * th, ep * ep, -th * th])
    rat = np.array([a, b, c]) / Y
    k = rat.mean()
    out.append({"tau": [re_t, im_t], "spread of the three ratios / their mean": float(np.max(np.abs(rat - k)) / abs(k)),
                "common factor times eta^3": [complex(k * et ** 3).real, complex(k * et ** 3).imag]})
print(json.dumps(out, indent=1))
