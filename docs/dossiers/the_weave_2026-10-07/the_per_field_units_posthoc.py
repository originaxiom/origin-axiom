"""W92 POST HOC (labelled; written after the read-out of W92's one run, where V3 failed as worded). V3 again, with the
neutral R evaluated by analytic theta sums instead of mpmath's jtheta.

The diagnosis (found in scratch after the read-out, disclosed):
  - On L R^n with n = 1, 2 mod 4 the integrands Y failed to close even with every charge zero, while the K norms
    closed everywhere. W72's units at weights 3/2 and -1/2 transform by one matrix, and h by that matrix times a
    uniform character; only the theta-built R disagreed, by a sign on its theta_2 component.
  - W72's collocation R (Rser) equals the theta-built R to 1e-39 near Re tau = 0, but at tau = -5.7 + i their
    theta_2 components have opposite signs.
  - The cause: mpmath's jtheta(2, z, q) takes q^(1/4) on the principal branch of the nome q = e^{i pi tau}. So
    theta_2(0)^2 from it flips sign when Re tau mod 4 lies in (1, 3]. V3's period start tau0 has Re tau0 ~ -n, which
    lies there exactly when n = 1, 2 mod 4.
  - The dressing (V1, V2, V3's D) uses theta_2 only as a ratio with the same nome power, so it is unaffected; V6 and V8
    are evaluated at Re tau in (-1, 1]; chat1's instrument and PerFieldSource use explicit analytic sums.
The prediction, fixed before this script's run: with R from analytic sums, V3 holds as the rule worded it (the Y
integrands return with exp(2 pi i eps c (qL^2 + qR^2 - qH^2) / N) and the K norms are equal, to 1e-25; the +qH^2 law
misses by more than 1e-3 wherever c 2 qH^2 != 0 mod N), on the same 90 rows.

Run: python3 the_per_field_units_posthoc.py  ->  the_per_field_units_posthoc.json beside it.
"""
import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_per_field_units as PF  # noqa: E402

OUT = HERE / "the_per_field_units_posthoc.json"
CH0 = {2: (mp.mpf(1) / 2, mp.mpf(0)), 4: (mp.mpf(0), mp.mpf(1) / 2), 3: (mp.mpf(0), mp.mpf(0))}


def theta_sum(a, b, t, M=60):
    """theta[a, b](0 | tau) = sum_n exp(i pi (n + a)^2 tau + 2 pi i (n + a) b), analytic in tau"""
    return mp.fsum(mp.exp(1j * mp.pi * ((n + a) ** 2 * t + 2 * (n + a) * b)) for n in range(-M, M + 1))


def neutral_R_analytic(t):
    q = mp.exp(2j * mp.pi * t)
    d1 = 2 * mp.pi * (mp.exp(2j * mp.pi * t / 24) * mp.qp(q)) ** 3
    return [-2 * mp.pi * PF.CQ[c] * theta_sum(*CH0[PF.S_OF[c]], t) ** 2 / d1 for c in range(3)]


def main():
    t0 = time.time()
    out = {"status": "POST HOC (labelled), after W92's read-out; V3 with R from analytic theta sums"}
    mp.mp.dps = 50
    checks = []
    for t in (mp.mpc("-5.7", "1.0"), mp.mpc("-4.7", "1.0"), mp.mpc("0.72", "0.92"), mp.mpc("0.1", "1.1")):
        a, b = PF.neutral_R(t), neutral_R_analytic(t)
        checks.append({"tau": [float(t.real), float(t.imag)], "jtheta / analytic per component":
                       [[float(mp.re(a[c] / b[c])), float(mp.im(a[c] / b[c]))] for c in range(3)]})
    out["the two R's compared"] = checks
    PF.neutral_R = neutral_R_analytic
    U = PF.build_units()
    U.update({"F32c": [PF.to_comp(s) for s in U["F32"]], "FM12c": [PF.to_comp(s) for s in U["FM12"]],
              "E4Fc": [PF.to_comp(s) for s in U["E4F"]], "fc": PF.to_comp(U["fser"]), "h5c": PF.to_comp(U["h5"]),
              "h9c": PF.to_comp(U["h9"])})
    print("units built", round(time.time() - t0, 1), flush=True)
    out["V3 post hoc"] = PF.V3(U)
    out["seconds"] = round(time.time() - t0, 1)
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    print("V3 post hoc holds", out["V3 post hoc"]["holds"], "seconds", out["seconds"], flush=True)


if __name__ == "__main__":
    main()
