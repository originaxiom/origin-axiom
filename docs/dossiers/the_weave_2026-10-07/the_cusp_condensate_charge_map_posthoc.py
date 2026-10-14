"""W70, POST HOC (written after W70's one run and its read-out, at main's ask in its S122 relay, section 4: "Main needs
the charge normalisation before W1's seal"; labelled; W70's JSON is unchanged). The hypercharge's normalisation in the
audit lane's registered E8 embedding, with W70's own coordinates and functions.

  PN1  k_Y = |Y|^2 / |T3|^2 for each of W70's six admissible Y, by two routes: the Cartan norms, and the sums of
       (r.Y)^2 and (r.T3)^2 over the 240 roots
  PN2  the control: the standard SU(5)-type hypercharge Y5 = -1/3 (e0 + e1 + e2) + 1/2 (e3 + e4). Is it orthogonal to
       colour and weak, in the span of the 6's weights, does it pass W70's five field conditions, what is its k_Y, and
       is it block-scalar (that is, does it commute with the weave's quaternion holonomies)?
  PN3  context, not a test: with the Standard Model's one-loop running from M_Z (B915's PDG 2024 inputs,
       1/alpha_em(M_Z) = 127.951 and sin^2 theta_W(M_Z) = 0.23122, MSbar), the scale where alpha_Y^-1 / alpha_2^-1
       equals k_Y, for k_Y = 5/3 and for PN1's value

Run: python3 the_cusp_condensate_charge_map_posthoc.py  ->  the_cusp_condensate_charge_map_posthoc.json beside it.
"""
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

import sympy as sy

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_cusp_condensate_charge_map as CM  # noqa: E402  (W70: the roots, the weights of the 6, the field test)

OUT = HERE / "the_cusp_condensate_charge_map_posthoc.json"
T3 = CM.scale(CM.WEAK, F(1, 2))
MZ, INV_AEM, SW2 = 91.1876, 127.951, 0.23122
B_Y, B_2 = F(41, 6), F(-19, 6)


def k_two_routes(Y):
    by_norm = CM.dot(Y, Y) / CM.dot(T3, T3)
    by_roots = sum(CM.dot(r, Y) ** 2 for r in CM.RR) / sum(CM.dot(r, T3) ** 2 for r in CM.RR)
    return by_norm, by_roots


def passes(Y):
    has = {"Q": False, "u^c": False, "d^c": False, "L": False, "e^c": False}
    for r in CM.RR:
        yr, c, w = CM.dot(r, Y), CM.colour(r), abs(CM.dot(r, CM.WEAK))
        has["Q"] |= c in CM.THREE and w == 1 and yr == F(1, 6)
        has["u^c"] |= c in CM.THREEBAR and w == 0 and yr == F(-2, 3)
        has["d^c"] |= c in CM.THREEBAR and w == 0 and yr == F(1, 3)
        has["L"] |= c == (0, 0) and w == 1 and yr == F(-1, 2)
        has["e^c"] |= c == (0, 0) and w == 0 and yr == 1
    return has


def coefficients(Y):
    """c with Y = sum_k c_k ws_k (sum c = 0), if Y lies in the span of the 6's weights"""
    W = sy.Matrix([[sy.Rational(x.numerator, x.denominator) for x in w] for w in CM.WS]).T     # 8 x 6
    A = W.col_join(sy.Matrix([[1] * 6]))
    b = sy.Matrix([sy.Rational(x.numerator, x.denominator) for x in Y] + [0])
    try:
        sol, params = A.gauss_jordan_solve(b)
    except ValueError:                                  # inconsistent: Y is not in the span
        return None
    if params.shape[0]:
        sol = sol.subs({p: 0 for p in params})
    ok = (A * sol - b).is_zero_matrix
    return [F(int(sy.fraction(x)[0]), int(sy.fraction(x)[1])) for x in sol] if ok else None


def crossing(k):
    """t = ln(mu / M_Z) where alpha_Y^-1 = k alpha_2^-1 at one loop (Standard Model content)"""
    ay, a2 = INV_AEM * (1 - SW2), INV_AEM * SW2
    t = (ay - k * a2) / (float(B_Y) / (2 * math.pi) - k * float(B_2) / (2 * math.pi))
    return {"ratio at M_Z": ay / a2, "t = ln(mu/M_Z)": t, "mu (GeV)": MZ * math.exp(t), "above M_Z": t > 0}


def main():
    out = {"status": "W70 POST HOC (labelled): the hypercharge's normalisation, at main's S122 ask"}
    w70 = json.loads((HERE / "the_cusp_condensate_charge_map.json").read_text(encoding="utf-8"))
    adm = [tuple(F(x) for x in y) for y in w70["N2"]["admissible"]]
    pn1 = {}
    for y in adm:
        a, b = k_two_routes(CM.ycartan(y))
        pn1[",".join(str(x) for x in y)] = {"k_Y by the Cartan norms": str(a), "k_Y by the 240 roots": str(b),
                                            "|Y|^2": str(CM.dot(CM.ycartan(y), CM.ycartan(y)))}
    vals = {v["k_Y by the Cartan norms"] for v in pn1.values()} | {v["k_Y by the 240 roots"] for v in pn1.values()}
    out["PN1"] = {"per admissible Y": pn1, "|T3|^2": str(CM.dot(T3, T3)), "the distinct values": sorted(vals)}
    Y5 = CM.vec((0, F(-1, 3)), (1, F(-1, 3)), (2, F(-1, 3)), (3, F(1, 2)), (4, F(1, 2)))
    c = coefficients(Y5)
    a, b = k_two_routes(Y5)
    out["PN2"] = {"orthogonal to colour and weak": all(CM.dot(Y5, v) == 0 for v in CM.COLOUR + [CM.WEAK]),
                  "coefficients on the 6's weights (blocks b, a, ab)": None if c is None else [str(x) for x in c],
                  "block-scalar": None if c is None else bool(c[0] == c[1] and c[2] == c[3] and c[4] == c[5]),
                  "the five field conditions": passes(Y5),
                  "k_Y by the Cartan norms": str(a), "k_Y by the 240 roots": str(b)}
    ks = sorted({F(v) for v in vals} | {F(5, 3)})
    out["PN3"] = {"inputs": {"1/alpha_em(M_Z)": INV_AEM, "sin^2 theta_W(M_Z)": SW2, "b_Y": str(B_Y), "b_2": str(B_2),
                             "source": "B915's PDG 2024 MSbar inputs (frontier/B915_the_crossing/crossing.py)"},
                  "per k_Y": {str(k): crossing(float(k)) for k in ks}}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)


if __name__ == "__main__":
    main()
