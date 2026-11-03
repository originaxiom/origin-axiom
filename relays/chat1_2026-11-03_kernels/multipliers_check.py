"""The web seat's check of the written proof in its kernels note, section 1 (data-free; no measured value is read).

Main's bilinear bil(x, y; u) (b1656_funcs, through B1821's cm_zero_line) has entries b00, b01, b10, b11. The proof
claims, with a_S = a_x + a_y and b_S = b_x + b_y:
  under u -> u + 1:   b00 -> -e^{2 pi i a_S} b00,  b11 -> -e^{2 pi i a_S} b11,  b01 -> e^{2 pi i a_S} b01,  b10 -> e^{2 pi i a_S} b10;
  under u -> u + tau: b00 -> e^{-i pi b_S} b11,     b11 -> e^{-i pi b_S} b00,     b01 -> -e^{-i pi b_S} b10, b10 -> -e^{-i pi b_S} b01.
It prints the largest relative deviation of the eight claims over random twists, tau and u.

Usage: python3 multipliers_check.py <main checkout>   (main at 0f3e71a24)
"""
import cmath
import contextlib
import io
import pathlib
import sys

import numpy as np

sys.dont_write_bytecode = True
ROOT = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
with contextlib.redirect_stdout(io.StringIO()):
    import cm_zero_line as Z
    B = Z.mods()["B"]
rng = np.random.default_rng(1103)
worst = 0.0
for _ in range(20):
    t = complex(rng.uniform(-0.5, 0.5), rng.uniform(1.0, 2.5))
    x = (rng.uniform(-1, 1), rng.uniform(-2, 2)); y = (rng.uniform(-1, 1), rng.uniform(-2, 2))
    u = complex(rng.uniform(-0.4, 0.4), rng.uniform(-0.4, 0.4))
    aS, bS = x[0] + y[0], x[1] + y[1]
    b0, b1, bt = (np.asarray(B.bil(x, y, v, t)).reshape(2, 2) for v in (u, u + 1, u + t))
    e1, et = cmath.exp(2j * cmath.pi * aS), cmath.exp(-1j * cmath.pi * bS)
    dev = [b1[0, 0] + e1 * b0[0, 0], b1[1, 1] + e1 * b0[1, 1], b1[0, 1] - e1 * b0[0, 1], b1[1, 0] - e1 * b0[1, 0],
           bt[0, 0] - et * b0[1, 1], bt[1, 1] - et * b0[0, 0], bt[0, 1] + et * b0[1, 0], bt[1, 0] + et * b0[0, 1]]
    worst = max(worst, max(abs(d) for d in dev) / float(np.max(np.abs(b0))))
print("20 random (x, y, tau, u): largest relative deviation of the eight multiplier claims: %.1e" % worst)
