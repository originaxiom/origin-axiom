#!/usr/bin/env python3
"""e20 (data-free; POST HOC, labelled): facts for main's P-323 (theta-bar in the mass frame) and P-328 (the CP lines),
first seen on 2026-10-27 in this seat's read-only referee's checks of its CP relay (scripts not committed); recomputed
here on the committed instrument so that the relay can cite them.  B1656's frame is main's B1720 instrument at
3412bf09d, unchanged, loaded through this seat's zero_free_census.py (channels, S_of, St, coupling, the Higgs
directions; ckm_left for J).  The Standard Model's reading with one Higgs direction h: up reads S~ = S(conj h), down
reads S(h).  theta_Y = arg det(Y_u) + arg det(Y_d).  No data are read; no target appears.
  F1  the Higgs's overall phase: h -> e^{i phi} h, three phases at six points: largest shift of theta_Y (mod 2 pi);
  F2  P-323's number: theta_Y / pi at B1726's best six-row (0.55 + 3.05i, line (2/5, 1/2), L_max, main's Higgs dR),
      at Re tau 0.35 and 0.85 on that line, and at 0.3145 + 3.0345i on (2/5, 1/10);
  F3  the frame's T-law (tau -> tau + 1, b -> b - alpha, the direction evaluated at tau + 1): the shift of arg det Y_u,
      arg det Y_d and theta_Y, over pi, on each of the ten (2/5, k/10) lines and on (1/3, 1/5), at three points each,
      both horocycles, the directions dR, F_2, F_6, F_22; with the masses' and J's changes;
  F4  the CP lines: on each of the ten lines, the Re tau = k/2 (k = -5..9) where k alpha = -2b (mod 1) and where
      k alpha = +2b (mod 1); J and theta_Y / pi there at Im tau 2.2, 2.6, 3.03, 3.4 (dR, L_max).
    python3 -B e20_cp_facts_for_p323.py      # writes e20_cp_facts_for_p323_out.txt"""
import cmath, contextlib, importlib.util, io, math, pathlib, sys
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ZF = HERE.parent / "chat1_2026-10-23_zero_free_frame"
_argv = sys.argv; sys.argv = ["x"]
_spec = importlib.util.spec_from_file_location("zfc", ZF / "zero_free_census.py")
zfc = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    _spec.loader.exec_module(zfc)
sys.argv = _argv
rbs, B, tic = zfc.rbs, zfc.B, zfc.tic
DIRS = ["dR", "F_2", "F_6", "F_22"]
TEN = [(Fr(2, 5), Fr(k, 10)) for k in range(10)]


def wrap_pi(x):                                       # x / pi into (-1, 1]
    y = math.fmod(x / math.pi, 2.0)
    return y - 2 if y > 1 else (y + 2 if y <= -1 else y)


def yuk(re_t, im_t, a, b, h, M=None):
    if M is None:
        M = rbs.channels(re_t, im_t, float(a), float(b))
    S = rbs.S_of(h); St = rbs.St(S)
    return {hor: (B.coupling(St, M[("up", hor)]), B.coupling(S, M[("down", hor)])) for hor in rbs.HORS}, M


def summary(Yu, Yd):
    du, dd = np.linalg.det(Yu), np.linalg.det(Yd)
    su = np.linalg.svd(Yu, compute_uv=False); sd = np.linalg.svd(Yd, compute_uv=False)
    return {"up": cmath.phase(du), "down": cmath.phase(dd), "theta": cmath.phase(du) + cmath.phase(dd),
            "J": tic.ckm_left(Yu, Yd)[3], "ratios": np.concatenate([su[1:] / su[0], sd[1:] / sd[0]])}


out = []

# F1
PTS = [(0.3, 3.0, 1), (0.5, 2.5, 3), (1.7, 3.5, 0), (0.4, 2.7, 5), (3.3, 2.9, 7), (4.6, 3.2, 2)]
f1 = 0.0
for re_t, im_t, k in PTS:
    a, b = TEN[k]
    h = zfc.direction("dR", re_t, im_t)
    Y0, M = yuk(re_t, im_t, a, b, h)
    for phi in (0.7, 2.1, -1.3):
        Y1, _ = yuk(re_t, im_t, a, b, cmath.exp(1j * phi) * h, M)
        for hor in rbs.HORS:
            f1 = max(f1, abs(wrap_pi(summary(*Y1[hor])["theta"] - summary(*Y0[hor])["theta"])))
out.append(f"F1 largest shift of theta_Y / pi under h -> e^(i phi) h (3 phases, 6 points, both horocycles): {f1:.2e}")

# F2
for re_t, im_t, a, b in ((0.55, 3.05, Fr(2, 5), Fr(1, 2)), (0.35, 3.05, Fr(2, 5), Fr(1, 2)), (0.85, 3.05, Fr(2, 5), Fr(1, 2)),
                         (0.3145, 3.0345, Fr(2, 5), Fr(1, 10))):
    Y, _ = yuk(re_t, im_t, a, b, zfc.direction("dR", re_t, im_t))
    s = summary(*Y["L_max"])
    out.append(f"F2 tau {re_t} + {im_t}i, line ({a}, {b}), L_max, dR: theta_Y / pi = {wrap_pi(s['theta']):+.4f} "
               f"(up {wrap_pi(s['up']):+.4f}, down {wrap_pi(s['down']):+.4f}); J {s['J']:+.3e}")

# F3
LINES3 = TEN + [(Fr(1, 3), Fr(1, 5))]
TP = [(0.3, 3.03), (0.55, 2.6), (1.2, 3.4)]
f3 = {}
for a, b in LINES3:
    for re_t, im_t in TP:
        M0 = rbs.channels(re_t, im_t, float(a), float(b)); M1 = rbs.channels(re_t + 1, im_t, float(a), float(b - a))
        for dname in DIRS:
            Y0, _ = yuk(re_t, im_t, a, b, zfc.direction(dname, re_t, im_t), M0)
            Y1, _ = yuk(re_t + 1, im_t, a, b - a, zfc.direction(dname, re_t + 1, im_t), M1)
            for hor in rbs.HORS:
                s0, s1 = summary(*Y0[hor]), summary(*Y1[hor])
                f3.setdefault((a, b), []).append((wrap_pi(s1["up"] - s0["up"]), wrap_pi(s1["down"] - s0["down"]),
                                                  wrap_pi(s1["theta"] - s0["theta"]), abs(s1["J"] - s0["J"]),
                                                  float(np.max(np.abs(np.log10(s1["ratios"] / s0["ratios"]))))))
for (a, b), rows in f3.items():
    r = np.array(rows)
    frac = [str(Fr(float(np.median(r[:, c]))).limit_denominator(100)) for c in range(3)]
    out.append(f"F3 line ({a}, {b}): T-step shift / pi: up {np.median(r[:, 0]):+.6f} (spread {np.ptp(r[:, 0]):.1e}, ~{frac[0]}), "
               f"down {np.median(r[:, 1]):+.6f} (spread {np.ptp(r[:, 1]):.1e}, ~{frac[1]}), theta_Y {np.median(r[:, 2]):+.6f} "
               f"(spread {np.ptp(r[:, 2]):.1e}, ~{frac[2]}); largest |delta J| {r[:, 3].max():.1e}, "
               f"largest |delta log10 ratio| {r[:, 4].max():.1e}")

# F4
for k10, (a, b) in enumerate(TEN):
    minus = [k for k in range(-5, 10) if (k * a + 2 * b) % 1 == 0]
    plus = [k for k in range(-5, 10) if (k * a - 2 * b) % 1 == 0]
    rows = []
    for label, ks in (("k alpha = -2b", minus), ("k alpha = +2b", plus)):
        for k in ks[:2]:
            for im_t in (2.2, 2.6, 3.03, 3.4):
                Y, _ = yuk(k / 2, im_t, a, b, zfc.direction("dR", k / 2, im_t))
                s = summary(*Y["L_max"])
                rows.append(f"{label} Re tau {k / 2:+.1f}, Im {im_t}: J {s['J']:+.1e}, theta_Y/pi {wrap_pi(s['theta']):+.4f}")
    out.append(f"F4 line ({a}, {b}):\n    " + "\n    ".join(rows))

(HERE / "e20_cp_facts_for_p323_out.txt").write_text("\n".join(out) + "\n")
print("written")
