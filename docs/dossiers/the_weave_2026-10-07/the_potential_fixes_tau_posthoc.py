"""W67, POST HOC (written after W67's one run and its read-out; labelled; W67's JSON is unchanged). F1 and F3 failed as
worded on R' alone, in two ways:
  - R' reached qA = 1/3 (an 8-orbit line) at two more points of the modular curve besides omega, near
    0.5 + 1.0347i and -0.2146 + 0.9767i, so its minimum with c > 0 is a tie;
  - with c < 0, qA(R') is flat at 1/2 to double precision by y = 6, so the refinement stopped at y = 6.39, below the
    rule's y > 7 mark for "runs to the cusp".

  PH1  R''s extra 8-orbit points at 40 digits: a root of one component of R'(tau) x w for the nearest 8-orbit line w,
       the full cross product there, and j at the root
  PH2  the plateau at 40 digits: 1/2 - qA(R'(iy)) and 1/2 - qA(R(iy)) for y = 4 to 8
  PH3  m2/m3 for every pair of parameter-free sections at the extra points (40 digits)

Run: python3 the_potential_fixes_tau_posthoc.py  ->  the_potential_fixes_tau_posthoc.json beside it.
"""
import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_second_unit as SU  # noqa: E402  (W65: the collocation and the 40-digit tools)
import the_cusp_unit_as_a_vector as CU  # noqa: E402  (W64: the orbits of special lines)
import the_parameter_free_census as PF  # noqa: E402  (W66: the pairs)

OUT = HERE / "the_potential_fixes_tau_posthoc.json"
mp.mp.dps = 40
GUESSES = [mp.mpc("0.4999999986543566", "1.0347106827387773"), mp.mpc("-0.214626", "0.976696")]


def qA(a):
    n = mp.fsum(abs(x) ** 2 for x in a)
    return mp.fsum(abs(x) ** 4 for x in a) / n ** 2


def main():
    _, _, _, _, orbits, lines = CU.K1()
    eight = [lines[k] for o in orbits if len(o) == 8 for k in o]
    sec = {}
    for name, units, lead in (("E", (1, 0, 0), "e_i"), ("R'", (0, 0, 1), "v-"), ("R", (0, 1, 0), "v+")):
        terms, _ = SU.solve_section(units, lead)
        sec[name] = (lambda tm: (lambda t: SU.evaluate(tm, t)))(terms)
    ph1 = []
    roots = []
    for g in GUESSES:
        v = np.array([complex(x) for x in sec["R'"](g)])
        w = min(eight, key=lambda u: float(abs(np.cross(v, u)).max() / (np.linalg.norm(v) * np.linalg.norm(u))))
        wm = [mp.mpc(complex(x)) for x in w]
        t0 = mp.findroot(lambda t: SU.cross(sec["R'"](t), wm)[0], g)   # one component; the full sine is checked
        val = sec["R'"](t0)
        jj = SU.kleinj(t0)
        ph1.append({"guess": [float(mp.re(g)), float(mp.im(g))], "root": [float(mp.re(t0)), float(mp.im(t0))],
                    "the 8-orbit line w": [[float(np.real(x)), float(np.imag(x))] for x in w],
                    "sine of the angle between R'(root) and w": float(SU.sine(val, wm)),
                    "qA(R'(root)) - 1/3": float(qA(val) - mp.mpf(1) / 3),
                    "R'.R' / |R'|^2 at the root": float(abs(SU.dot(val, val)) / SU.norm(val) ** 2),
                    "j at the root": [float(mp.re(jj)), float(mp.im(jj))]})
        roots.append(t0)
    ph2 = {}
    for name in ("R'", "R"):
        ph2[name] = {str(y): float(mp.mpf(1) / 2 - qA(sec[name](mp.mpc(0, y)))) for y in (4, 5, 6, 6.3872, 7, 8)}
    ph2["strictly below 1/2 and rising toward it, for both"] = bool(all(
        all(v > 0 for v in ph2[n].values()) and list(ph2[n].values()) == sorted(ph2[n].values(), reverse=True)
        for n in ("R'", "R")))
    ph3 = {}
    for t0 in roots:
        vals = {k: sec[k](t0) for k in ("E", "R", "R'")}
        row = {}
        for pair, (a, c) in PF.PAIRS.items():
            S = mp.svd_c(SU.Yuk(vals[a], vals[c]), compute_uv=False)
            row[pair] = float(S[1] / S[0])
        ph3[mp.nstr(t0, 8)] = row
    out = {"status": "W67 post hoc: R''s extra 8-orbit points and the plateau at 40 digits (labelled; W67's JSON "
                     "unchanged)", "PH1 (R''s extra 8-orbit points)": ph1, "PH2 (1/2 - qA along tau = iy)": ph2,
           "PH3 (m2/m3 for every pair at the extra points)": ph3}
    OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(ph1, indent=1))


if __name__ == "__main__":
    main()
