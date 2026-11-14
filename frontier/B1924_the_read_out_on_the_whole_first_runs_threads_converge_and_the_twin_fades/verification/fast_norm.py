"""The channel norm by B1919's closed form, to replace the frame's quadrature (b1656_funcs.cA) in the thread averages.

c_s(tau) = F_u(tau) + pi log Im tau - 2 pi (gamma + log pi),  u = c_s - (1/2, 1/2),  c_s the kernel's characteristic.
F_u, the constant term at s = 1 of sum over (m, n) in u + Z^2 of y^s |m tau + n|^(-2s), from its Fourier expansion:
  a = {u1} != 0:  F_u = -pi (2 log 2 + log y + psi(a) + psi(1 - a)) + sum over m in u1 + Z of (2 pi/|m|) Re[w_m/(1 - w_m)],
  a = 0:          F_u = pi (2 gamma - 2 log 2 - log y) + y pi^2/sin^2(pi b) + the same sum over m != 0,
with w_m = exp(-2 pi |m| y + 2 pi i (m x + u2)), b = {u2}. The kernel characteristic of each channel is taken from
B1906's closed form in the twists' coordinates; which of two conventions is the frame's is decided by comparison with
the frame's own quadrature on random twists, and the substitution is used only if it agrees there."""
import math, sys, pathlib
import numpy as np
from scipy.special import digamma
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1716_the_zeros_derived" / "verification"))
import b1656_funcs as F

EG = 0.5772156649015329
CC = -2 * math.pi * (EG + math.log(math.pi))


def F_u(u1, u2, t):
    x, y = t.real, t.imag
    a = u1 % 1.0; b = u2 % 1.0
    if a > 1e-12 and a < 1 - 1e-12:
        first = -math.pi * (2 * math.log(2) + math.log(y) + digamma(a) + digamma(1 - a))
        zero_row = 0.0
    else:
        first = math.pi * (2 * EG - 2 * math.log(2) - math.log(y))
        zero_row = y * math.pi ** 2 / math.sin(math.pi * b) ** 2 if 1e-12 < b < 1 - 1e-12 else float("inf")
    K = int(40 / (2 * math.pi * y)) + 4
    m = np.arange(-K, K + 1) + a
    m = m[np.abs(m) > 1e-12]
    w = np.exp(-2 * math.pi * np.abs(m) * y + 2j * math.pi * (m * x + u2))
    return first + zero_row + float(np.sum((2 * math.pi / np.abs(m)) * np.real(w / (1 - w))))


def norm_closed(c, t):
    return F_u(c[0] - 0.5, c[1] - 0.5, t) + math.pi * math.log(t.imag) + CC


def kernel_chars(x, yy, convention):
    (ax, bx), (ay, by) = x, yy
    ap, am = ax + ay, ax - ay
    if convention == "B1906":
        bp, bm = (bx + by) / 2, (bx - by) / 2
    else:
        bp, bm = bx + by, bx - by
    return {"1": (ap + 0.5, bp + 0.5), "i": (ap + 0.5, bp), "j": (ap, bp + 0.5), "k": (ap, bp)}


def cA_fast(x, yy, t, R, convention="B1906"):
    ch = kernel_chars(x, yy, convention)
    return {s: (norm_closed(ch[s], t) if abs(R[s]) > 1e-12 else None) for s in F.UNITS}


if __name__ == "__main__":
    import random, time
    rng = random.Random(7)
    worst = {"B1906": 0.0, "full": 0.0}
    for trial in range(6):
        t = complex(rng.uniform(-0.5, 0.5), rng.uniform(0.9, 1.6))
        w = complex(rng.uniform(0, 1), 0) * t + rng.uniform(0, 1)
        x, yy = F.sector_twists(w, t, F.SIXY["Q"], F.SIXY["u"])
        R = F.residues(x, yy, t)
        t0 = time.time(); ref = F.cA(x, yy, t, R); tq = time.time() - t0
        for conv in worst:
            t0 = time.time(); fast = cA_fast(x, yy, t, R, conv); tf = time.time() - t0
            for s in F.UNITS:
                if ref[s] is not None and fast[s] is not None:
                    worst[conv] = max(worst[conv], abs(ref[s] - fast[s]))
        print("trial %d: quadrature %.2f s, closed form %.4f s" % (trial, tq, tf), flush=True)
    print("largest |closed form - quadrature| over 6 random twists and 4 channels:", {k: "%.1e" % v for k, v in worst.items()})
