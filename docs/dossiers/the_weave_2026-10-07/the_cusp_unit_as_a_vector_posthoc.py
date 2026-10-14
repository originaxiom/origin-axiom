"""W64, POST HOC (written after W64's one run and its read-out; labelled; W64's JSON is unchanged). K2, K4 and K5 failed
in the run because of one instrument error: R was built from mpmath's jtheta(2, 0, q), which takes the principal fourth
root of the nome q = e^{i pi tau}. That is theta_2(tau) only while -1 < Re tau <= 1, so at tau + 1 with Re tau > 0 it
returned theta_2 times the wrong eighth root of unity. K2's fit of R(tau + 1) then found no signed permutation (it
settled on the identity with residual 0.88), and K4 and K5 used that wrong representation.

  PH1  the error shown: the run's R(tau + 1) against R built from the theta series summed directly, at the ten tau
  PH2  K2 re-scored with the direct series: R(tau + 1) and R(-1/tau) against signed permutations
  PH3  K4 and K5 re-scored with the representation PH2 finds (W64's own collocation, with W64's R replaced by the
       direct series)

Run: python3 the_cusp_unit_as_a_vector_posthoc.py  ->  the_cusp_unit_as_a_vector_posthoc.json beside it.
"""
import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_cusp_unit_as_a_vector as CU  # noqa: E402  (W64: its taus, fit, collocation and cells)

OUT = HERE / "the_cusp_unit_as_a_vector_posthoc.json"
I = mp.mpc(0, 1)
NS = range(-40, 41)


def theta_direct(t):
    """theta_2, theta_3, theta_4 at z = 0 by their series in tau, with no branch of the nome"""
    e = lambda x: mp.exp(I * mp.pi * x)  # noqa: E731
    t2 = mp.fsum(e(t * (n + mp.mpf(1) / 2) ** 2) for n in NS)
    t3 = mp.fsum(e(t * n * n) for n in NS)
    t4 = mp.fsum((-1) ** n * e(t * n * n) for n in NS)
    return t2, t3, t4


def Rdirect(t):
    t2, t3, t4 = theta_direct(t)
    D = mp.pi * t2 * t3 * t4
    return mp.matrix([-t2 ** 2 / D, -t4 ** 2 / D, I * t3 ** 2 / D])


def PH1():
    rows = []
    for t in CU.TAUS:
        a, b = CU.Rvec(t + 1), Rdirect(t + 1)
        same = max(abs(a[k] - b[k]) for k in range(3)) / max(abs(b[k]) for k in range(3))
        ratio_i = a[0] / b[0]
        rows.append({"tau": [float(t.real), float(t.imag)], "relative difference at tau + 1": float(same),
                     "run's R_i / direct R_i": [float(mp.re(ratio_i)), float(mp.im(ratio_i))]})
    at_own = max(float(max(abs(CU.Rvec(t)[k] - Rdirect(t)[k]) for k in range(3))) for t in CU.TAUS)
    return {"rows": rows, "largest difference at tau itself (Re tau in (-1, 1])": at_own}


def main():
    L = CU.move_on_M("L")
    ph1 = PH1()                                         # before the replacement: the run's R against the series
    CU.Rvec = Rdirect                                   # the direct series everywhere below
    k2, PT, Ps = CU.K2(L)
    rS, rT = CU.reps(PT, Ps)
    k4 = CU.K4(rS, rT)
    k5 = CU.K5(rS, rT)
    out = {"status": "W64 post hoc: the theta_2 branch error traced; K2, K4 and K5 re-scored with the direct series "
                     "(labelled; W64's JSON unchanged)",
           "PH1": ph1, "PH2 (K2 re-scored)": k2, "PH3 (K4 re-scored)": k4, "PH3 (K5 re-scored)": k5}
    out["re-scored"] = {"K2": k2["holds"], "K4": k4["holds"], "K5": k5["holds"]}

    def enc(x):
        if isinstance(x, complex):
            return [float(np.real(x)), float(np.imag(x))]
        return float(x) if isinstance(x, (np.floating, float)) else str(x)
    OUT.write_text(json.dumps(out, indent=1, default=enc) + "\n", encoding="utf-8")
    print(json.dumps(out["re-scored"], indent=1))


if __name__ == "__main__":
    main()
