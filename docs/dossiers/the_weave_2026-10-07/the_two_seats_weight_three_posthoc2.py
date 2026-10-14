"""W79, SECOND POST HOC (labelled; written after the first post hoc's read-out). The first post hoc found the two seats'
weight-3 spaces equal through an exact intertwiner at moderate Im tau (angles 1e-11 to 1e-13), but 6.5e-4 apart at
Im tau = 6.6. A hypothesis, from main's construction: main's forms are eta^-18 times polynomials of degree k + 9 in the
theta squares whose coefficients come from a double-precision SVD, and near the cusp those polynomials cancel down to
the size of eta^18, so main's forms carry an error of order 1e-16 |eta|^-18 ~ 1e-16 e^{(3 pi / 2) Im tau}. This tests it.

  PH3  the angle between main's weight-3 span (carried by the intertwiner) and this seat's, at x = 0.1 and
       Im tau = 2, 3, 4, 5, 6, 7, 8; the slope of log(angle) against Im tau, against 3 pi / 2 = 4.71
  PH4  at main's up-sector tau (B1637's F3, -0.0737 + 6.6640i): the up sector alone fitted in main's own weight-3 forms
       (300 starts); that fit's Y carried into this seat's frame and projected onto this seat's span; the masses' chi^2
       of the projected Y, and the relative size of the part the projection removes

Main's code is used read-only, extracted from 60c5470ae as in W79.

Run: python3 the_two_seats_weight_three_posthoc2.py  ->  the_two_seats_weight_three_posthoc2.json beside it.
"""
import json
import math
import sys
import tempfile
from pathlib import Path

import numpy as np
from scipy.linalg import subspace_angles
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_fit_at_the_geometrys_weight as FW  # noqa: E402
import the_rank_thirteen_structures as RT  # noqa: E402
import the_two_seats_weight_three as W79  # noqa: E402
import the_two_seats_weight_three_posthoc as PH  # noqa: E402

OUT = HERE / "the_two_seats_weight_three_posthoc2.json"
TAU_U = complex(-0.07371773130317516, 6.663964995864581)


def u_res(Y):
    s = np.linalg.svd(Y, compute_uv=False)
    logs = np.log(np.maximum(np.sort(s), 1e-300))
    return RT.mass_res("u", logs, FW.A_MAIN)


def main_():
    out = {"status": "W79 SECOND POST HOC (labelled): the precision of main's weight-3 forms near the cusp"}
    oS, oT = W79.our_rho()
    with tempfile.TemporaryDirectory() as tmp:
        main, _ = W79.load_main(tmp)
        N = PH.intertwiner(main.c35.rS, main.c35.rT, oS, oT)
        P = N[:, 0].reshape(3, 3)
        P = P / abs(np.linalg.det(P)) ** (1 / 3)
        carry = lambda Y: np.conj(P) @ Y @ np.conj(P).T        # noqa: E731
        main.FORMS[3] = main.forms(3)
        ys = [2, 3, 4, 5, 6, 7, 8]
        rows = []
        for y in ys:
            t = complex(0.1, y)
            A = np.array([carry(Y).reshape(9) for Y in main.basis_at(3, t)]).T
            B = np.array([Y.reshape(9) for Y in RT.forms_at("T (x) T", 3, t)]).T
            ang = float(max(subspace_angles(A, B)))
            rows.append({"Im tau": y, "largest angle": ang,
                         "1e-16 |eta|^-18": 1e-16 * math.exp(1.5 * math.pi * y)})
        good = [(r["Im tau"], math.log(r["largest angle"])) for r in rows if r["largest angle"] > 1e-15]
        slope = float(np.polyfit([a for a, _ in good], [b for _, b in good], 1)[0]) if len(good) >= 2 else None
        out["PH3"] = {"rows": rows, "slope of log(angle) against Im tau": slope, "3 pi / 2": 1.5 * math.pi}
        Bm = main.basis_at(3, TAU_U)
        rng = np.random.default_rng(7950)
        best = None
        for _ in range(300):
            def res(p):
                c = p[:2] + 1j * p[2:]
                return u_res(c[0] * Bm[0] + c[1] * Bm[1])
            r = least_squares(res, rng.normal(size=4), method="trf", xtol=1e-14, ftol=1e-14, gtol=1e-14,
                              max_nfev=3000)
            chi = float(np.sum(r.fun ** 2))
            if best is None or chi < best[0]:
                best = (chi, r.x)
        c = best[1][:2] + 1j * best[1][2:]
        Ymain = carry(c[0] * Bm[0] + c[1] * Bm[1])
        Bo = np.array([Y.reshape(9) for Y in RT.forms_at("T (x) T", 3, TAU_U)]).T
        coef, *_ = np.linalg.lstsq(Bo, Ymain.reshape(9), rcond=None)
        Yproj = (Bo @ coef).reshape(3, 3)
        removed = float(np.linalg.norm(Ymain - Yproj) / np.linalg.norm(Ymain))
        sv_main = sorted(np.linalg.svd(Ymain, compute_uv=False))
        sv_proj = sorted(np.linalg.svd(Yproj, compute_uv=False))
        out["PH4"] = {"tau": [TAU_U.real, TAU_U.imag], "main's forms: chi^2 of the up masses": best[0],
                      "projected onto this seat's span: chi^2": float(np.sum(u_res(Yproj) ** 2)),
                      "the removed part, relative": removed,
                      "singular values / largest (main's fit)": [float(v / sv_main[-1]) for v in sv_main],
                      "singular values / largest (projected)": [float(v / sv_proj[-1]) for v in sv_proj],
                      "data m_u/m_t, m_c/m_t": [float(math.exp(FW.LOGM["u"][0] - FW.LOGM["u"][2])),
                                                float(math.exp(FW.LOGM["u"][1] - FW.LOGM["u"][2]))]}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main_()
