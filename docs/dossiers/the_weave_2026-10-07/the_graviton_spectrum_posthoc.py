#!/usr/bin/env python3
"""W124, post hoc (labelled so; after the one run's read-out). G2(a) failed: the constant mode came out 0.44% (Weeks)
and 0.62% (Meyerhoff) below 2 e^{1/(2 w^2)}. The constant mode weights the geodesic sum by e^l, so its geometric weight
is a Gaussian in l centred at 1/w^2 = 2.25 with spread 1/w = 1.5 (the prime geodesic theorem's main term reproduces
2 e^{1/(2 w^2)} exactly), and cutting at R = 6 drops the tail beyond 2.5 spreads: about 0.62%. This check re-enumerates
(the run's own functions, unchanged), keeps every axis, and recomputes every sector with the cutoffs R' = 5.0, 5.5 and
6.0 at the same window: the constant-mode deficit against the main-term prediction, the Cornish-Spergel difference,
the coexact and TT values near 0, the TT peaks and the TT count's 0.5 crossing. Real eigenvalues do not move with R'.

    python3 -B the_graviton_spectrum_posthoc.py      # writes the_graviton_spectrum_posthoc.json beside itself
"""
import contextlib
import io
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_graviton_spectrum as GS  # noqa: E402

W = GS.W


def tail_prediction(Rc):
    """the main term's share beyond Rc: 2 e^{1/(2w^2)} (1 - Phi((Rc - 1/w^2) w))"""
    z = (Rc - 1 / W ** 2) * W
    return 2 * math.exp(1 / (2 * W ** 2)) * 0.5 * math.erfc(z / math.sqrt(2))


def main():
    out = {"arc": "W124", "status": "post hoc, labelled; after the one run's read-out", "window w": W}
    for label, name in (("Weeks", "m003(-3,1)"), ("Meyerhoff", "m004(5,1)")):
        M, P, normals, info = GS.domain(name)
        E = GS.enumerate_axes(P, normals, info["out_radius"])
        vol = info["volume"]
        rows = {}
        for Rc in (5.0, 5.5, 6.0):
            sel = E["ell"] <= Rc
            Es = {"ell": E["ell"][sel], "cos": E["cos"][sel], "w": E["w"][sel]}
            S, hTi, _ = GS.sectors(Es, vol)
            S0n = S[0] - hTi
            N2 = GS.count(S[2])
            row = {"constant mode: S0(0) - h0(i)": round(GS.at(S[0], 0.0) - float(hTi[0]), 5),
                   "main-term tail beyond R'": round(tail_prediction(Rc), 5),
                   "S1 at 0": round(GS.at(S[1], 0.0), 4), "S2 at 0": round(GS.at(S[2], 0.0), 4),
                   "S2 min": round(float(S[2].min()), 4), "TT peaks": GS.peaks(S[2]),
                   "N2 reaches 0.5 at": GS.first_cross(N2),
                   "N2 at 2,3,4,5,6,8": [round(float(N2[int(t * 100)]), 3) for t in (2, 3, 4, 5, 6, 8)],
                   "coexact peaks": GS.peaks(S[1]), "scalar peaks": GS.peaks(S0n)}
            if label == "Weeks":
                rj = np.array([math.sqrt(l - 1) for l, _ in GS.CS_WEEKS])
                mj = np.array([k for _, k in GS.CS_WEEKS])
                Gf = lambda d: np.exp(-d ** 2 / (2 * W ** 2))
                Scs = sum(mm * (Gf(GS.TGRID - r_) + Gf(GS.TGRID + r_)) for r_, mm in zip(rj, mj))
                row["Cornish-Spergel max |diff| on [0,7]"] = round(float(np.abs(S0n - Scs)[GS.TGRID <= 7.0].max()), 4)
            rows[str(Rc)] = row
            print(label, "R'", Rc, row, flush=True)
        out[label] = rows
    (HERE / "the_graviton_spectrum_posthoc.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
