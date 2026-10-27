#!/usr/bin/env python3
"""e20c (data-free; POST HOC, labelled): e20's F3 and F4 row by row, written after a read-only referee pass on the relay
that cites them found two scopes the committed outputs did not show: e20's F3 printed medians pooled over four
directions (F_2, which is not covariant under the T-law, included), and e20b printed rows on (2/5, 1/10) only; e20's F4
used dR on L_max only and tested J's non-vanishing only on the mirror family.  Same instrument and conventions as e20
(its definitions imported from its committed file; main's B1720 instrument at 3412bf09d, unchanged).
  G3  the T-law (tau -> tau + 1, b -> b - alpha, the direction at tau + 1) on each of the ten (2/5, k/10) lines and on
      (1/3, 1/5), at e20's three points, both horocycles, per direction (dR, F_6, F_22, and F_2 apart): the shifts of
      arg det Y_u, arg det Y_d and theta_Y over pi (largest spread over points and horocycles), the largest |delta J|
      and the largest |delta log10| of the six singular-value ratios;
  G4  every half-integer Re tau = k/2 (k = 0..9, a full period of each line's CP condition) on each of the ten lines, at
      Im tau 3.03: whether k alpha = -2b (mod 1); |J| and theta_Y / pi for dR, F_6 and F_22 on both horocycles; per
      line, the largest |J| where the condition holds and the least |J| where it does not; at the points where it
      holds, the spread of theta_Y mod pi over the six (direction, horocycle) pairs.
    python3 -B e20c_t_law_and_cp_points_by_direction.py      # writes e20c_t_law_and_cp_points_by_direction_out.txt"""
import contextlib, io, math, pathlib
from fractions import Fraction as Fr
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
src = (HERE / "e20_cp_facts_for_p323.py").read_text().split("out = []")[0]     # e20's definitions only
e20 = {"__file__": str(HERE / "e20_cp_facts_for_p323.py"), "__name__": "e20_definitions"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src, str(HERE / "e20_cp_facts_for_p323.py"), "exec"), e20)
rbs, zfc, yuk, summary, wrap_pi, TEN = e20["rbs"], e20["zfc"], e20["yuk"], e20["summary"], e20["wrap_pi"], e20["TEN"]
COV = ["dR", "F_6", "F_22"]
out = []


def mod_pi(x):                                        # x / pi folded into (-1/2, 1/2]
    y = math.fmod(x / math.pi, 1.0)
    return y - 1 if y > 0.5 else (y + 1 if y <= -0.5 else y)


# G3
TP = [(0.3, 3.03), (0.55, 2.6), (1.2, 3.4)]
for a, b in TEN + [(Fr(1, 3), Fr(1, 5))]:
    rows = {d: [] for d in COV + ["F_2"]}
    for re_t, im_t in TP:
        M0 = rbs.channels(re_t, im_t, float(a), float(b)); M1 = rbs.channels(re_t + 1, im_t, float(a), float(b - a))
        for d in rows:
            Y0, _ = yuk(re_t, im_t, a, b, zfc.direction(d, re_t, im_t), M0)
            Y1, _ = yuk(re_t + 1, im_t, a, b - a, zfc.direction(d, re_t + 1, im_t), M1)
            for hor in rbs.HORS:
                s0, s1 = summary(*Y0[hor]), summary(*Y1[hor])
                rows[d].append((wrap_pi(s1["up"] - s0["up"]), wrap_pi(s1["down"] - s0["down"]),
                                wrap_pi(s1["theta"] - s0["theta"]), abs(s1["J"] - s0["J"]),
                                float(np.max(np.abs(np.log10(s1["ratios"] / s0["ratios"]))))))
    parts = []
    for d in COV:
        r = np.array(rows[d])
        fr = [str(Fr(float(r[0, c])).limit_denominator(200)) for c in range(3)]
        parts.append(f"{d}: up {fr[0]}, down {fr[1]}, theta_Y {fr[2]} (spreads {np.ptp(r[:, 0]):.1e}, {np.ptp(r[:, 1]):.1e}, "
                     f"{np.ptp(r[:, 2]):.1e}; |dJ| <= {r[:, 3].max():.1e}; |dlog10 ratio| <= {r[:, 4].max():.1e})")
    r2 = np.array(rows["F_2"])
    out.append(f"G3 line ({a}, {b}), shifts over pi:\n    " + "\n    ".join(parts) +
               f"\n    F_2 (apart): theta_Y in [{r2[:, 2].min():+.3f}, {r2[:, 2].max():+.3f}]; |dlog10 ratio| up to {r2[:, 4].max():.2f}")

# G4
for a, b in TEN:
    held, notheld, spreads, vals = [], [], [], []
    for k in range(10):
        cond = (k * a + 2 * b) % 1 == 0
        M = rbs.channels(k / 2, 3.03, float(a), float(b))
        th, js = [], []
        for d in COV:
            Y, _ = yuk(k / 2, 3.03, a, b, zfc.direction(d, k / 2, 3.03), M)
            for hor in rbs.HORS:
                s = summary(*Y[hor]); th.append(s["theta"]); js.append(abs(s["J"]))
        (held if cond else notheld).append(max(js) if cond else min(js))
        if cond:
            m = [mod_pi(x) for x in th]
            spreads.append(max(abs(mod_pi((x - th[0]))) for x in th))
            vals.append(f"Re tau {k / 2:.1f}: theta_Y/pi (dR, L_max) {wrap_pi(th[0]):+.4f}, mod pi {m[0]:+.4f}")
    out.append(f"G4 line ({a}, {b}): condition holds at {len(held)} of 10 half-integers, largest |J| there {max(held):.1e}; "
               f"least |J| elsewhere {min(notheld):.1e}; theta_Y mod pi agrees over the six (direction, horocycle) pairs "
               f"to {max(spreads):.1e}\n    " + "; ".join(vals))

(HERE / "e20c_t_law_and_cp_points_by_direction_out.txt").write_text("\n".join(out) + "\n")
print("written")
