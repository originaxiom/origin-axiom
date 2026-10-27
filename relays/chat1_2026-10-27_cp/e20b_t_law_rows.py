#!/usr/bin/env python3
"""e20b (data-free; POST HOC, labelled; a diagnostic of e20's F3, after e20's output was read): e20's F3 reported the
medians of the T-step shifts with spreads of order one and changes of the singular-value ratios of order one, which
the T-law should not allow for a covariant Higgs direction.  This prints F3's rows one by one on (2/5, 1/10) at e20's
three points: per direction and horocycle, the shifts of arg det Y_u, arg det Y_d and theta_Y (over pi), |delta J| and
the largest |delta log10| of the six singular-value ratios.  Same instrument and conventions as e20 (imported from it).
    python3 -B e20b_t_law_rows.py      # writes e20b_t_law_rows_out.txt"""
import contextlib, importlib.util, io, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
src = (HERE / "e20_cp_facts_for_p323.py").read_text().split("out = []")[0]     # e20's definitions only
e20 = {"__file__": str(HERE / "e20_cp_facts_for_p323.py"), "__name__": "e20_definitions"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src, str(HERE / "e20_cp_facts_for_p323.py"), "exec"), e20)
rbs, zfc, yuk, summary, wrap_pi = e20["rbs"], e20["zfc"], e20["yuk"], e20["summary"], e20["wrap_pi"]
out = []
a, b = Fr(2, 5), Fr(1, 10)
for re_t, im_t in [(0.3, 3.03), (0.55, 2.6), (1.2, 3.4)]:
    M0 = rbs.channels(re_t, im_t, float(a), float(b)); M1 = rbs.channels(re_t + 1, im_t, float(a), float(b - a))
    for dname in e20["DIRS"]:
        Y0, _ = yuk(re_t, im_t, a, b, zfc.direction(dname, re_t, im_t), M0)
        Y1, _ = yuk(re_t + 1, im_t, a, b - a, zfc.direction(dname, re_t + 1, im_t), M1)
        for hor in rbs.HORS:
            s0, s1 = summary(*Y0[hor]), summary(*Y1[hor])
            out.append(f"tau {re_t} + {im_t}i {dname:5s} {hor:5s}: up {wrap_pi(s1['up'] - s0['up']):+.6f}, "
                       f"down {wrap_pi(s1['down'] - s0['down']):+.6f}, theta_Y {wrap_pi(s1['theta'] - s0['theta']):+.6f}; "
                       f"|dJ| {abs(s1['J'] - s0['J']):.1e}; max |dlog10 ratio| "
                       f"{float(np.max(np.abs(np.log10(s1['ratios'] / s0['ratios'])))):.1e}")
(HERE / "e20b_t_law_rows_out.txt").write_text("\n".join(out) + "\n")
print("written")
