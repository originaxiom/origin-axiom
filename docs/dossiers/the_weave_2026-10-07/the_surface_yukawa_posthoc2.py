"""W72, SECOND POST HOC (labelled). The first post hoc's PH1 failed as worded. A scratch diagnosis, run before this
script was committed and disclosed in the record, found why: every failing check had a = R and |f| near 1e-35, so
the relative test divided by functions that vanish. This script re-runs that diagnosis as a committed post hoc.

  PH4  every T and S check of f_ab(a) and G_ab at the five unit-arc points, with |value|: the checks whose value is
       above 1e-25 in absolute size, and their largest relative deviation
  PH5  the vanishing, by hand: R . F+ is a weight-1 form with eta^6's multiplier and no pole, so it is zero. Its series
       coefficients below exponent 4, and the values of R . F_i and R . F- at tau = i (where E_10 vanishes)

Run: python3 the_surface_yukawa_posthoc2.py  ->  the_surface_yukawa_posthoc2.json beside it.
"""
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_surface_yukawa as SY  # noqa: E402  (W72: the sections, the series, the evaluation)

OUT = HERE / "the_surface_yukawa_posthoc2.json"
mp.mp.dps = 40
DEG = (65, 75, 90, 105, 115)
FLOOR = mp.mpf("1e-25")


def main():
    sec = {}
    for name, u in SY.MATTER:
        terms, r, line = SY.best_section(u, Fraction(3, 2))
        sec[name] = SY.to_series(terms, SY.E8)
    for name, u in SY.HIGGS:
        terms, r, line = SY.best_section(u, Fraction(-1, 2))
        sec[name] = SY.to_series(terms, SY.E8)
    F = [sec[n] for n, _ in SY.MATTER]
    R = sec["R"]
    rows = []
    for a, b in SY.PAIRS:
        G = SY.G_series(F[a], F[b], R)
        for d in DEG:
            t = mp.exp(SY.I * mp.pi * d / 180)
            g0, g1, gS = SY.ev_vec(G, t), SY.ev_vec(G, t + 1), SY.ev_vec(G, -1 / t)
            w1 = SY.SU.matvec(SY.RT2, g0)
            wS = [mp.power(t, mp.mpf(5) / 2) * z for z in SY.SU.matvec(SY.RS2, g0)]
            nG = max(abs(x) for x in g0)
            rows.append({"what": f"G{a}{b}", "deg": d, "size": float(nG),
                         "T abs": float(max(abs(g1[k] - w1[k]) for k in range(3))),
                         "S abs": float(max(abs(gS[k] - wS[k]) for k in range(3)))})
            for hn, _ in SY.HIGGS:
                f = SY.dot_series(sec[hn], G)
                f0, f1, fS = SY.ev_scal(f, t), SY.ev_scal(f, t + 1), SY.ev_scal(f, -1 / t)
                rows.append({"what": f"f{a}{b}:{hn}", "deg": d, "size": float(abs(f0)),
                             "T abs": float(abs(f1 + f0)), "S abs": float(abs(fS + t * t * f0))})
    big = [r for r in rows if r["size"] > FLOOR]
    small = [r for r in rows if r["size"] <= FLOOR]
    worst = max(max(r["T abs"], r["S abs"]) / r["size"] for r in big)
    out = {"status": "W72 SECOND POST HOC (labelled): the multiplier checks, sized"}
    out["PH4"] = {"checks": len(rows), "with |value| above 1e-25": len(big),
                  "largest relative deviation among them": worst,
                  "the small ones (what, deg, size)": [[r["what"], r["deg"], r["size"]] for r in small],
                  "holds": bool(worst < 1e-10 and all(r["what"].endswith(":R") for r in small))}
    RFp = SY.dot_series(R, F[1])
    low = max(abs(v) for n8, v in RFp.items() if n8 < 32)
    i_ = mp.mpc(0, 1)
    vals = {"R.F_i at i": float(abs(SY.ev_scal(SY.dot_series(R, F[0]), i_))),
            "R.F- at i": float(abs(SY.ev_scal(SY.dot_series(R, F[2]), i_))),
            "R.F_i at 75 degrees": float(abs(SY.ev_scal(SY.dot_series(R, F[0]), mp.exp(i_ * mp.pi * 75 / 180)))),
            "R.F- at 75 degrees": float(abs(SY.ev_scal(SY.dot_series(R, F[2]), mp.exp(i_ * mp.pi * 75 / 180))))}
    out["PH5"] = {"largest |coefficient| of R.F+ below exponent 4": float(low), "values": vals,
                  "holds": bool(low < 1e-25 and vals["R.F_i at i"] < 1e-25 and vals["R.F- at i"] < 1e-25
                                and vals["R.F_i at 75 degrees"] > 1e-3 and vals["R.F- at 75 degrees"] > 1e-3)}
    out["cells"] = {k: out[k]["holds"] for k in ("PH4", "PH5")}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main()
