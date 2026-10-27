#!/usr/bin/env python3
"""e20d (data-free; POST HOC, labelled): written after reading e20c's output, where the CP points of (2/5, 1/10) and of
its T-image, taken with the representative b = 7/10 in place of -3/10, did not differ by e20c's T-step shift.  The
question: does relabelling the same line, b -> b + 1 (the same w on E_tau), move theta_Y?  The expectation, stated
before the run: B1656's characteristic for charge q is (q alpha, 2 q b) and thc(a, beta + n) = e^{2 pi i a n} thc(a, beta),
so each zero mode of charge q gains e^{4 pi i alpha q^2}, each sector's coupling e^{4 pi i alpha (q_L^2 + q_R^2)}, and
theta_Y moves by 12 pi alpha [(q_Q^2 + q_u^2) + (q_Q^2 + q_d^2)] = 264 pi alpha (mod 2 pi): -2 pi/5 on the ten
(2/5, k/10) lines, 0 on (1/3, 1/5).  Same instrument and conventions as e20 (its definitions imported).
  H1  on the ten lines and (1/3, 1/5), at e20's three points, both horocycles, dR, F_6 and F_22: theta_Y(b + 1) - theta_Y(b)
      and theta_Y(b - 1) - theta_Y(b) over pi, against 264 alpha (mod 2); |delta J| and |delta log10 ratio|.
    python3 -B e20d_relabelling_b.py      # writes e20d_relabelling_b_out.txt"""
import contextlib, io, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
src = (HERE / "e20_cp_facts_for_p323.py").read_text().split("out = []")[0]     # e20's definitions only
e20 = {"__file__": str(HERE / "e20_cp_facts_for_p323.py"), "__name__": "e20_definitions"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src, str(HERE / "e20_cp_facts_for_p323.py"), "exec"), e20)
rbs, zfc, yuk, summary, wrap_pi, TEN = e20["rbs"], e20["zfc"], e20["yuk"], e20["summary"], e20["wrap_pi"], e20["TEN"]
out = []
for a, b in TEN + [(Fr(1, 3), Fr(1, 5))]:
    expect = float(Fr(264) * a % 2)
    expect = expect - 2 if expect > 1 else expect
    dev, dj, dr = 0.0, 0.0, 0.0
    for re_t, im_t in [(0.3, 3.03), (0.55, 2.6), (1.2, 3.4)]:
        M0 = rbs.channels(re_t, im_t, float(a), float(b))
        for sgn in (+1, -1):
            M1 = rbs.channels(re_t, im_t, float(a), float(b + sgn))
            for d in ("dR", "F_6", "F_22"):
                h = zfc.direction(d, re_t, im_t)
                Y0, _ = yuk(re_t, im_t, a, b, h, M0); Y1, _ = yuk(re_t, im_t, a, b + sgn, h, M1)
                for hor in rbs.HORS:
                    s0, s1 = summary(*Y0[hor]), summary(*Y1[hor])
                    shift = wrap_pi(s1["theta"] - s0["theta"])
                    dev = max(dev, abs(wrap_pi((shift - sgn * expect) * np.pi)))
                    dj = max(dj, abs(s1["J"] - s0["J"]))
                    dr = max(dr, float(np.max(np.abs(np.log10(s1["ratios"] / s0["ratios"])))))
    out.append(f"H1 line ({a}, {b}): b -> b +- 1 moves theta_Y by +-{expect:+.4f} pi expected (264 alpha mod 2); largest "
               f"deviation {dev:.1e} (in pi); |dJ| <= {dj:.1e}; |dlog10 ratio| <= {dr:.1e}")
(HERE / "e20d_relabelling_b_out.txt").write_text("\n".join(out) + "\n")
print("written")
