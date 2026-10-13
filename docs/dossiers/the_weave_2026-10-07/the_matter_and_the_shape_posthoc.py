"""W62, POST HOC (written after W62's one run and its read-out; labelled; W62's JSON is unchanged; no new spectrum). Two
things to trace from the stored numbers:

  PH1  A1 failed as worded only at tau = omega, where tau + 1 = -conj(tau) is omega's mirror image and S_(1/2,1/2) is
       mirror-symmetric, so its change under T is 0 there; the mirror identity S(tau + 1) = S(-conj(tau)) is checked at
       omega, and T's change is listed at the other four points
  PH2  the shape of the diffractive part D: the fits of dD to dE(tau, 2), alone and with dE(tau, 3), for the values at
       n, at 4n, and extrapolated as O(h) and as O(h^2); the E(tau, 2) coefficient set beside 31/1024, which it
       approaches (an observation, not a claim)
  PH3  the content window read against the cusp: for a content built from the trivial sector and rho_Q alone, the ratio
       r = dV_rho/dE3 per axis interval rises from about 0.017 toward its cusp limit 31/1024 (the periodic parts'
       ratio); a content with W_triv/W_rho above every r is stable at the cusp, and its axis minimum is then at i

Run: python3 the_matter_and_the_shape_posthoc.py  ->  the_matter_and_the_shape_posthoc.json beside it.
"""
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_matter_and_the_shape as MS  # noqa: E402  (W62: S, E_cs, OMEGA)

OUT = HERE / "the_matter_and_the_shape_posthoc.json"
D = json.loads((HERE / "the_matter_and_the_shape.json").read_text(encoding="utf-8"))


def ph1():
    w = MS.OMEGA
    mirror = abs(MS.S(w + 1, (0.5, 0.5), M=600) - MS.S(complex(-w.real, w.imag), (0.5, 0.5), M=600))
    others = {str(r["tau"]): r["S: tau -> tau + 1 (absolute change)"] for r in D["A1"]["rows"][1:]}
    ident = max(r["|copies - (E/16 - S_(1/2,1/2))| / E"] for r in D["A1"]["rows"])
    return {"omega + 1 is omega's mirror image": abs((w + 1) - complex(-w.real, w.imag)) < 1e-15,
            "|S(omega + 1) - S(-conj(omega))|": mirror, "T's change at the other four points": others,
            "the identity's largest error at all five": ident,
            "A1 holds at every point where T is not the mirror": bool(min(others.values()) > 1e-3 and ident < 1e-10)}


def fits(dd, e2, e3):
    c2 = float(dd @ e2 / (e2 @ e2))
    X = np.stack([e3, e2], axis=1)
    coef, *_ = np.linalg.lstsq(X, dd, rcond=None)
    return {"E2 alone: coefficient": c2,
            "E2 alone: rms residual / rms dD": float(np.sqrt(np.mean((dd - c2 * e2) ** 2) / np.mean(dd ** 2))),
            "E3 and E2: coefficients": coef.tolist(),
            "E3 and E2: rms residual / rms dD": float(np.sqrt(np.mean((dd - X @ coef) ** 2) / np.mean(dd ** 2))),
            "E2 alone: coefficient / (31/1024)": c2 / (31 / 1024)}


def ph2():
    vals = D["the values (W59 units, against the reference)"]
    names = [m[0] for m in D["the family"]["members"][1:] if m[0] != "other hexagonal"]
    e2 = np.array([vals["4n"][k]["dE2"] for k in names])
    e3 = np.array([vals["4n"][k]["dE3"] for k in names])
    dn = np.array([vals["n"][k]["dD"] for k in names])
    d4 = np.array([vals["4n"][k]["dD"] for k in names])
    return {"n": fits(dn, e2, e3), "4n": fits(d4, e2, e3), "O(h)": fits(2 * d4 - dn, e2, e3),
            "O(h^2)": fits((4 * d4 - dn) / 3, e2, e3), "31/1024": 31 / 1024}


def ph3():
    win = D["read-outs"]["the content window"]
    r4 = win["the ratio dV_rho / dE3 per interval"]["4n"]
    vals = D["the values (W59 units, against the reference)"]["4n"]
    arc = [m[0] for m in D["the family"]["members"] if m[0].startswith("arc")]
    r_arc = [vals[k]["dV_rho"] / vals[k]["dE3"] for k in arc]
    return {"r per axis interval (4n)": r4, "rising": bool(all(np.diff(r4) > 0)),
            "r on the arc against omega (4n)": dict(zip(arc, r_arc)),
            "the cusp limit (31/1024)": 31 / 1024,
            "the cusp-stability threshold for W_triv/W_rho, from Sum W kappa < 0": 31 / 1024,
            "every measured r below the threshold": bool(max(r4 + r_arc) < 31 / 1024),
            "reading": "with W_rho < 0, f' along the axis has the sign of W_triv/W_rho - r; a cusp-stable content has "
                       "W_triv/W_rho > 31/1024 > r, so f rises from i up the axis and from omega to i on the arc: its "
                       "minimum on the sampled curves is at omega; a content with W_triv/W_rho inside the window has "
                       "a stationary point on the axis that is a maximum, and runs to the cusp (assumes r keeps "
                       "rising beyond y = 2.02, not computed)"}


def main():
    out = {"status": "W62 post hoc: A1 traced; the shape of D from the stored values; the content window against the "
                     "cusp (labelled; W62's JSON unchanged; no new spectrum)",
           "PH1": ph1(), "PH2": ph2(), "PH3": ph3()}
    OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: out["PH2"][k]["E2 alone: coefficient / (31/1024)"] for k in ("n", "4n", "O(h)", "O(h^2)")},
                     indent=1))
    print(out["PH1"]["A1 holds at every point where T is not the mirror"], out["PH3"]["every measured r below the "
                                                                                     "threshold"])


if __name__ == "__main__":
    main()
