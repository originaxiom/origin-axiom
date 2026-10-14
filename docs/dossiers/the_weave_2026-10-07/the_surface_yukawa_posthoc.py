"""W72, POST HOC (written after W72's one run and its read-out; labelled; W72's JSON is unchanged). Three cells failed
as worded on instruments, not on content:
  - X2 evaluated truncated series of growing forms at Im(-1/tau) = 1/4 (tau = 4i), where the series is not valid;
  - X5 and the f-exponent read-out filtered coefficients relative to the largest one, and these forms' coefficients
    grow so fast that the filter discarded the leading coefficients.

  PH1  the T and S laws of every f_ab(a) and G_ab at five points on the unit arc, where tau and -1/tau both have
       Im >= 0.9 (tau = e^{i theta}, theta = 65, 75, 90, 105, 115 degrees)
  PH2  each matter mode's coefficient at its negative exponent, read unfiltered, and the largest coefficient's size
  PH3  every exponent of every f_ab(a) and G_ab series, unfiltered: the classes 1/2 + Z and rho''s; and f's true
       lowest exponent per pair and Higgs

Run: python3 the_surface_yukawa_posthoc.py  ->  the_surface_yukawa_posthoc.json beside it.
"""
import json
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_surface_yukawa as SY  # noqa: E402  (W72: the sections, the series, the evaluation)

OUT = HERE / "the_surface_yukawa_posthoc.json"
mp.mp.dps = 40
POINTS = [mp.exp(SY.I * mp.pi * mp.mpf(d) / 180) for d in (65, 75, 90, 105, 115)]


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
    G = {(a, b): SY.G_series(F[a], F[b], R) for a, b in SY.PAIRS}
    fab = {(a, b, hn): SY.dot_series(sec[hn], G[(a, b)]) for a, b in SY.PAIRS for hn, _ in SY.HIGGS}
    worst_T, worst_S = 0.0, 0.0
    for t in POINTS:
        for a, b in SY.PAIRS:
            Gt, G1, Gs_ = SY.ev_vec(G[(a, b)], t), SY.ev_vec(G[(a, b)], t + 1), SY.ev_vec(G[(a, b)], -1 / t)
            want1 = SY.SU.matvec(SY.RT2, Gt)
            wantS = [mp.power(t, mp.mpf(5) / 2) * z for z in SY.SU.matvec(SY.RS2, Gt)]
            nG = max(abs(z) for z in Gt)
            worst_T = max(worst_T, float(max(abs(G1[k] - want1[k]) for k in range(3)) / nG))
            worst_S = max(worst_S, float(max(abs(Gs_[k] - wantS[k]) for k in range(3)) / max(abs(z) for z in wantS)))
            for hn, _ in SY.HIGGS:
                s = fab[(a, b, hn)]
                f0, f1, fS = SY.ev_scal(s, t), SY.ev_scal(s, t + 1), SY.ev_scal(s, -1 / t)
                worst_T = max(worst_T, float(abs(f1 + f0) / abs(f0)))
                worst_S = max(worst_S, float(abs(fS + t * t * f0) / abs(t * t * f0)))
    out = {"status": "W72 POST HOC (labelled): the instruments of X2, X5 and the exponent read-out, corrected"}
    out["PH1"] = {"largest relative deviation, T law": worst_T, "largest relative deviation, S law": worst_S,
                  "holds": bool(worst_T < 1e-10 and worst_S < 1e-10)}
    neg = {}
    for name, _ in SY.MATTER:
        s = sec[name]
        neg[name] = {"negative exponents and coefficients": {str(Fraction(n8, 8)): [float(mp.re(a)), float(mp.im(a))]
                                                              for (l, n8), a in s.items() if n8 < 0},
                     "largest |coefficient|": float(max(abs(a) for a in s.values()))}
    out["PH2"] = {"per mode": neg,
                  "holds": bool(all(len(v["negative exponents and coefficients"]) == 1 for v in neg.values()))}
    f_all = all(n8 % 8 == 4 for s in fab.values() for n8 in s)
    G_all = all((n8 - SY.E8P[l]) % 8 == 0 for s in G.values() for (l, n8) in s)
    lowest = {f"{a}{b}:{hn}": str(Fraction(min(n8 for n8, v in s.items() if abs(v) > mp.mpf("1e-30")), 8))
              for (a, b, hn), s in fab.items()}
    out["PH3"] = {"every f exponent in 1/2 + Z (unfiltered)": f_all, "every G exponent in rho' classes": G_all,
                  "f's lowest exponent per pair and Higgs (|coefficient| > 1e-30)": lowest,
                  "holds": bool(f_all and G_all)}
    out["cells"] = {k: out[k]["holds"] for k in ("PH1", "PH2", "PH3")}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main()
