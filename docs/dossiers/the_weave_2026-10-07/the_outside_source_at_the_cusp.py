"""W48 (the rule: W48_RULE.md, committed before this script). The outside source's dressing law and the c = 24
candidates for the unit at the weave's cusp (the owner's choice, 2026-10-09; GENESIS FK10).

  S1  the lattice family Theta_L / Delta (rank l = 0, 8, 16, 24; weight l/2 - 12, trivial multiplier) and the weight law
      for w in {+4, 0, -4, -8, -12, -24}: the dressed four-dimensional index at the four puncture conditions, the L6 row
      against its H0 form, the canonical counts (24 - l)/8.
  S2  the oscillator family 1/eta^c (c = 8, 12, 16, 24; weight -c/2, multiplier v_eta^-c): the dressed index.
  S3  the second route: q-expansion dimensions (W45's dims) of every dressed space, against chi.
  S4  the analytic facts: E4(omega) = 0, E4^2's first coefficients, the root counts of E8 + E8 and D16+, one zero of
      j - 744 on the open surface.

A dressed zero mode is f = g F with F holomorphic: a piece rho at weight k becomes F at weight k - w with multiplier
rho (x) mu_g^-1, mu_g the source's multiplier.

Run: python3 the_outside_source_at_the_cusp.py  ->  the_outside_source_at_the_cusp.json beside it.
"""
import json
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_end_conditions_on_the_weaves_surface as EC  # noqa: E402  (W46: the pieces from the record's lifts)
import the_index_on_the_weaves_surface as IW  # noqa: E402  (W45: chi, allowed, dims)

H = EC.H
OUT = HERE / "the_outside_source_at_the_cusp.json"
TOL = 1e-9
BASE = {"T": Fraction(3, 2), "T-bar": Fraction(1, 2), "V2": Fraction(1), "V4": Fraction(1)}
LATTICE = {0: "1/Delta (24 oscillators)", 8: "E4/Delta (an E8 lattice and 16 oscillators)",
           16: "E4^2/Delta (the heterotic left-movers, E8 x E8 or Spin(32)/Z2)", 24: "(j + const) (a Niemeier lattice)"}
OSC = (8, 12, 16, 24)


def dress(R, w, r):
    """the pieces of F: weight k - w, multiplier rho (x) v_eta^r (r = c for 1/eta^c, 0 for a trivial multiplier)"""
    es, et = np.exp(-1j * np.pi * r / 4), np.exp(2j * np.pi * r / 24)
    return {n: (BASE[n] - w, (es * np.array(R[n][0]), et * np.array(R[n][1]))) for n in BASE}


def chi0(k, rho):
    return IW.chi(k, *rho)[0] if IW.allowed(k, rho[0]) else 0.0


def dressed_index(D):
    out = {}
    for cond, pieces in EC.CONDITIONS.items():
        v = -chi0(*D["T"])
        for p in pieces:
            v += chi0(*D[p])
        out[cond] = round(v, 9)
    out["L6 by its H0 form"] = round(chi0(*D["T-bar"]), 9)
    return out


def second_route(D):
    out = {}
    for n, (k, rho) in D.items():
        M = IW.dims(*rho, k) if k > 0 else (0, None)
        dual = (np.conj(rho[0]), np.conj(rho[1]))
        S = IW.dims(*dual, 2 - k, cusp=True) if 2 - k > 0 else (0, None)
        out[n] = {"weight": str(k), "dim M (null count, gap)": M, "dim S of the dual (null count, gap)": S,
                  "chi": round(chi0(k, rho), 9), "dim M - dim S": M[0] - S[0]}
    return out


# ---------------------------------------------------------------- S4: q-series
def sigma(n, p):
    return sum(d ** p for d in range(1, n + 1) if n % d == 0)


def E4_coeffs(N):
    return [1] + [240 * sigma(n, 3) for n in range(1, N)]


def series(coeffs, q):
    return sum(c * q ** n for n, c in enumerate(coeffs))


def delta(tau, N=60):
    q = np.exp(2j * np.pi * tau)
    p = 1.0 + 0j
    for n in range(1, N):
        p *= (1 - q ** n) ** 24
    return q * p


def S4():
    c4 = E4_coeffs(40)
    omega = np.exp(2j * np.pi / 3)
    e4w = series(c4, np.exp(2j * np.pi * omega))
    sq = np.convolve(c4[:3], c4[:3])[:3].tolist()
    roots_e8 = 240                                             # E8's roots
    roots_d16 = 2 * 16 * 15                                    # D16's roots; D16+'s spinor coset starts at norm 4
    thetas = np.linspace(np.pi / 3 + 1e-6, np.pi / 2, 4001)    # the arc from omega to i, where j is real
    vals = []
    for th in thetas:
        tau = np.exp(1j * th)
        j = series(c4, np.exp(2j * np.pi * tau)) ** 3 / delta(tau)
        vals.append(j.real - 744)
    changes = int(sum(1 for a, b in zip(vals, vals[1:]) if a * b < 0))
    return {"|E4(omega)|": float(abs(e4w)), "E4^2's first coefficients": [int(round(x)) for x in sq],
            "roots of E8 + E8": 2 * roots_e8, "roots of D16+": roots_d16,
            "j - 744 on the arc from omega to i: sign changes": changes,
            "j at the arc's ends (omega, i)": [round(float(vals[0] + 744), 3), round(float(vals[-1] + 744), 3)]}


def main():
    C, K = EC.frame()
    (_, gL, gR) = H.lift_choices()[0]
    R, _ = EC.reps(gL, gR, C, K)
    law = {}
    for w in (4, 0, -4, -8, -12, -24):
        law[str(w)] = dressed_index(dress(R, Fraction(w), 0))
    lattice, lattice_dims = {}, {}
    for l, name in LATTICE.items():
        D = dress(R, Fraction(l, 2) - 12, 0)
        lattice[name] = dressed_index(D)
        lattice_dims[name] = second_route(D)
    osc, osc_dims = {}, {}
    for c in OSC:
        D = dress(R, Fraction(-c, 2), c)
        osc["1/eta^%d" % c] = dressed_index(D)
        osc_dims["1/eta^%d" % c] = second_route(D)
    s4 = S4()
    want_law = {"4": [1, 0, 0, -1], "0": [0, 0, 0, 0], "-4": [-1, 0, 0, 1], "-8": [-2, -1, 1, 2],
                "-12": [-3, -1, 1, 3], "-24": [-6, -2, 2, 6]}
    conds = ["0", "V2", "V4", "L6"]
    canon_lat = [-lattice[LATTICE[l]]["0"] for l in (0, 8, 16, 24)]
    canon_osc = [-osc["1/eta^%d" % c]["0"] for c in OSC]
    all_dims = list(lattice_dims.values()) + list(osc_dims.values())
    checks = {
        "S1: the weight law's table at the four puncture conditions, and the L6 row equals its H0 form": bool(
            all(abs(law[w][c] - v) < TOL for w, row in want_law.items() for c, v in zip(conds, row))
            and all(abs(r["L6"] - r["L6 by its H0 form"]) < TOL for r in law.values())),
        "S1: the lattice family's canonical counts are (24 - l)/8 = 3, 2, 1, 0": bool(
            all(abs(x - y) < TOL for x, y in zip(canon_lat, [3, 2, 1, 0]))),
        "S2: the oscillator family's canonical counts are 1, 1, 2, 3 for c = 8, 12, 16, 24": bool(
            all(abs(x - y) < TOL for x, y in zip(canon_osc, [1, 1, 2, 3]))),
        "S2: at c = 24 the four conditions give -3, -1, +1, +3": bool(
            all(abs(osc["1/eta^24"][c] - v) < TOL for c, v in zip(conds, [-3, -1, 1, 3]))),
        "S3: the q-expansion dimension differences equal chi for every candidate and piece": bool(
            all(abs(v["dim M - dim S"] - v["chi"]) < TOL for D in all_dims for v in D.values())),
        "S3: T's dressed spaces have dimension 1, 2, 3 for l = 16, 8, 0, every dual cusp space zero": bool(
            [lattice_dims[LATTICE[l]]["T"]["dim M (null count, gap)"][0] for l in (16, 8, 0)] == [1, 2, 3]
            and all(lattice_dims[LATTICE[l]]["T"]["dim S of the dual (null count, gap)"][0] == 0 for l in (16, 8, 0))),
        "S4: E4(omega) = 0; E4^2 begins 1, 480, 61920; 480 roots each; j - 744 has one zero on the arc": bool(
            s4["|E4(omega)|"] < 1e-8 and s4["E4^2's first coefficients"] == [1, 480, 61920]
            and s4["roots of E8 + E8"] == 480 and s4["roots of D16+"] == 480
            and s4["j - 744 on the arc from omega to i: sign changes"] == 1),
    }
    out = {"status": "W48: the outside source's dressing law and the c = 24 candidates (the rule first)",
           "S1: the weight law (trivial multiplier), by w": law, "S1: the lattice family": lattice,
           "S2: the oscillator family": osc, "S3: the lattice family's dressed spaces": lattice_dims,
           "S3: the oscillator family's dressed spaces": osc_dims, "S4: the analytic facts": s4,
           "checks": {k: bool(v) for k, v in checks.items()}, "every check holds": bool(all(checks.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["checks"], indent=1))
    print("every check holds:", out["every check holds"])


if __name__ == "__main__":
    main()
