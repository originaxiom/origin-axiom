"""W41: the weight of the weave's zero modes (the rule, W41_RULE.md, was committed before this file existed).

The form (W21's second route): F = (f(z), f(z + tau)) dz, f(z) = theta_3(z | 2 tau) / sqrt(theta_1(z | tau)).

K1  the weight by the norm. N(tau) = 2 int_E (|f(z)|^2 + |f(z + tau)|^2) dx dy (the periods script's l2_norm, here with
    96 Gauss-Legendre points per direction, fixed before the run). If F has weight -3/4, g(tau) = N(tau) / (Im tau)^(3/4)
    is invariant under every move. Checked at tau0 = 0.23 + 1.07i and tau1 = -0.41 + 0.83i, for T, S, U, the record's L
    and R, and the matrix products RL = R L and LRR = L R R; the controls use exponents 1/4 and 1 for S at tau0.
K2  the numerator pair (theta_3, theta_2)(z | 2 tau): with z' = z / (c tau + d),
        (theta_3, theta_2)(z' | 2 gamma tau) = (c tau + d)^(1/2) exp(i pi c z^2 / (2 (c tau + d))) W(gamma) (theta_3, theta_2)(z | 2 tau),
    W fitted at two z, checked at three more and at tau1, for T, S, U.
K3  theta_1(z' | gamma tau) = eps1(gamma) (c tau + d)^(1/2) exp(i pi c z^2 / (c tau + d)) theta_1(z | tau), eps1 an eighth root of
    unity (a control).
K4  so f has weight 1/4 and index 0, M_f = W / sqrt(eps1), and the one-form F has weight -3/4.

The theta functions in K2 and K3 are summed as series in tau, not through mpmath's nome q = exp(i pi tau): mpmath
takes the principal q^(1/4), which misplaces a fourth root of unity once |Re tau| > 1 (|Re 2 tau| > 1 for the
numerators). A first launch that used the nome-based functions was stopped before it wrote any output, on finding
this; disclosed. K1 uses only moduli, which the branch does not touch, and keeps the periods script's norm. A control
compares the series with mpmath at the base point, where the two agree.

Run: python3 the_zero_modes_weight.py  ->  the_zero_modes_weight.json beside it.
"""
import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_holomorphic_triplet_periods as PS  # noqa: E402  (W21's second route: the form and its norm)

OUT = HERE / "the_zero_modes_weight.json"
TAU0, TAU1 = complex(0.23, 1.07), complex(-0.41, 0.83)
MATS = {
    "T": ((1, 1), (0, 1)),
    "S": ((0, -1), (1, 0)),
    "U": ((0, -1), (1, 1)),
    "L (the record's)": ((1, 1), (0, 1)),
    "R (the record's)": ((1, 0), (1, 1)),
}
mm = lambda A, B: tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
MATS["RL = R L"] = mm(MATS["R (the record's)"], MATS["L (the record's)"])
MATS["LRR = L R R"] = mm(MATS["L (the record's)"], mm(MATS["R (the record's)"], MATS["R (the record's)"]))
ZS = (complex(0.13, 0.07), complex(0.21, -0.05), complex(-0.17, 0.11), complex(0.05, 0.19), complex(0.30, 0.02))


def act(M, t):
    (a, b), (c, d) = M
    return (a * t + b) / (c * t + d)


def g_of(t, k=0.75, npts=96):
    return PS.l2_norm(t, npts=npts) / t.imag ** k


def th(n, z, t):
    """theta_n(z | t) as a series in t (n = 1, 2, 3), at the working precision"""
    z, t = mp.mpc(z), mp.mpc(t)
    K = int(mp.sqrt(40 * mp.log(10) / (mp.pi * t.imag))) + 3
    if n == 1:
        return 2 * mp.fsum((-1) ** k * mp.exp(1j * mp.pi * t * (k + 0.5) ** 2) * mp.sin((2 * k + 1) * mp.pi * z)
                           for k in range(K))
    if n == 2:
        return 2 * mp.fsum(mp.exp(1j * mp.pi * t * (k + 0.5) ** 2) * mp.cos((2 * k + 1) * mp.pi * z) for k in range(K))
    return 1 + 2 * mp.fsum(mp.exp(1j * mp.pi * t * k * k) * mp.cos(2 * k * mp.pi * z) for k in range(1, K))


def theta_pair(z, t):
    return np.array([complex(th(3, z, 2 * t)), complex(th(2, z, 2 * t))])


def theta1(z, t):
    return complex(th(1, z, t))


def series_control():
    """the series against mpmath's jtheta at tau0, where |Re tau0| and |Re 2 tau0| are below 1"""
    q = mp.exp(1j * mp.pi * mp.mpc(TAU0))
    worst = 0.0
    for z in ZS:
        worst = max(worst,
                    abs(th(1, z, TAU0) - mp.jtheta(1, mp.pi * z, q)),
                    abs(th(2, z, 2 * TAU0) - mp.jtheta(2, mp.pi * z, q ** 2)),
                    abs(th(3, z, 2 * TAU0) - mp.jtheta(3, mp.pi * z, q ** 2)))
    return float(worst)


def laws(M, t):
    (a, b), (c, d) = M
    j = c * t + d
    tp = act(M, t)
    A = lambda z: np.sqrt(j) * np.exp(1j * np.pi * c * z * z / (2 * j))
    lhs = [theta_pair(z / j, tp) / A(z) for z in ZS]
    rhs = [theta_pair(z, t) for z in ZS]
    W = np.array(lhs[:2]).T @ np.linalg.inv(np.array(rhs[:2]).T)
    resid = max(float(np.max(abs(W @ r - l))) for r, l in zip(rhs[2:], lhs[2:]))
    eps = [theta1(z / j, tp) / (np.sqrt(j) * np.exp(1j * np.pi * c * z * z / j) * theta1(z, t)) for z in ZS]
    return W, resid, eps


def main():
    mp.mp.dps = 20
    k1 = {}
    for name, t in (("tau0", TAU0), ("tau1", TAU1)):
        g0 = g_of(t)
        rows = {}
        for mname, M in MATS.items():
            tp = act(M, t)
            rows[mname] = {"gamma tau": [round(tp.real, 6), round(tp.imag, 6)],
                           "relative change of g": float("%.3g" % abs(g_of(tp) / g0 - 1))}
        k1[name] = {"g(tau)": float("%.12g" % g0), "under the moves": rows}
    ts = act(MATS["S"], TAU0)
    controls = {"exponent %s" % k: float("%.3g" % abs(g_of(ts, k) / g_of(TAU0, k) - 1)) for k in (0.25, 1.0)}

    k23 = {}
    for mname in ("T", "S", "U"):
        M = MATS[mname]
        W0, r0, e0 = laws(M, TAU0)
        W1, r1, e1 = laws(M, TAU1)
        eps = np.array(e0 + e1)
        k23[mname] = {
            "W (fitted at tau0)": [[str(np.round(x, 9)) for x in row] for row in W0],
            "W unitary": bool(np.allclose(W0.conj().T @ W0, np.eye(2), atol=1e-9)),
            "residual at three more z (tau0, tau1)": [float("%.3g" % r0), float("%.3g" % r1)],
            "W the same at tau1": float("%.3g" % float(np.max(abs(W1 - W0)))),
            "eps1": str(np.round(eps[0], 9)),
            "eps1 constant": float("%.3g" % float(np.max(abs(eps - eps[0])))),
            "eps1 an eighth root of unity": bool(abs(eps[0] ** 8 - 1) < 1e-9),
            "M_f = W / sqrt(eps1)": [[str(np.round(x, 9)) for x in row] for row in W0 / np.sqrt(eps[0])],
        }
    control = series_control()
    res = {
        "status": "W41: the rule (W41_RULE.md) committed before this file existed; one run (a first launch stopped "
                  "before any output, disclosed in the docstring)",
        "the series against mpmath at tau0 (max abs difference)": float("%.3g" % control),
        "K1: g = N / (Im tau)^(3/4) under the moves": k1,
        "K1 controls: S at tau0 with other exponents": controls,
        "K2, K3: the laws of the numerator pair and of theta_1": k23,
    }
    worst = max(r["relative change of g"] for b in k1.values() for r in b["under the moves"].values())
    res["checks"] = {
        "the theta series agree with mpmath at tau0 (to 1e-15)": control < 1e-15,
        "K1: g invariant to 1e-6 under every listed move at both base points": worst < 1e-6,
        "K1: the controls fail by more than 1e-2": all(v > 1e-2 for v in controls.values()),
        "K2: W constant (three more z, and tau1) to 1e-10 and unitary": all(
            max(v["residual at three more z (tau0, tau1)"]) < 1e-10 and v["W the same at tau1"] < 1e-10 and v["W unitary"]
            for v in k23.values()),
        "K3: eps1 constant and an eighth root of unity": all(
            v["eps1 constant"] < 1e-10 and v["eps1 an eighth root of unity"] for v in k23.values()),
    }
    res["checks"]["K4: f has weight 1/4 and index 0, so F has weight -3/4"] = (
        res["checks"]["K2: W constant (three more z, and tau1) to 1e-10 and unitary"]
        and res["checks"]["K3: eps1 constant and an eighth root of unity"])
    res["the largest relative change of g"] = worst
    res["every check holds"] = all(res["checks"].values())
    OUT.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
