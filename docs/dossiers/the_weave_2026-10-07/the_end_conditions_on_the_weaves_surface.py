"""W46 (the rule: W46_RULE.md, committed before this script). The four-dimensional index for every end condition the
weave keeps on its own surface: W28's four conditions at the puncture, and uniform units at the cusp.

  H1  structure, with the record's lifts (W21's lift_choices, as W38 and W45): T by W21's on_V (a pullback, so its
      monodromy is the inverse) and the six local solutions by W24's blocks_action (a pushforward, the monodromy
      itself); sigma1 = L, sigma2 = R^-1, S = S~^-1, T = L. The braid relation; rho6(S)^2 = -I and S~^4 = I on the six
      (-I on T); V2 and V4 (W28 E2) invariant, their traces and exponents; the six's exponents the union of the two
      triplets'; the central characters on the puncture's exact sequence.
  H2  the formula (W45's, calibrated there): chi_1 on V2 and V4, chi_1(rho6) against chi_{3/2}(rho_T) +
      chi_{1/2}(rho-bar_T); eta^2 at weight 1.
  H3  the other overall lift sign (the base direction's other square root): everything again.
  H4  the second route: q-expansion dimensions (W45's dims) at weight 1, and W45's four spaces under the other sign;
      eta^2 first.
  H5  the table: the index for each puncture condition and n in {-1, 0, 1} uniform cusp units.

Run: python3 the_end_conditions_on_the_weaves_surface.py  ->  the_end_conditions_on_the_weaves_surface.json beside it.
"""
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_mixing_patterns_verified as MV  # noqa: E402  (W35: T, on_T; W21's triplets and lift_choices)
import the_six_dimensional_census as SC  # noqa: E402  (W24: blocks_action on the six local solutions)
import the_index_on_the_weaves_surface as IW  # noqa: E402  (W45: chi, allowed, dims)

CP, CT, H = MV.CP, MV.CT, MV.H
OUT = HERE / "the_end_conditions_on_the_weaves_surface.json"
I2 = np.eye(2)
Q2 = np.vstack([I2, I2, I2]) / np.sqrt(3)                 # V2 = {(v, v, v)} (W28 E2)
Q4 = np.linalg.svd(Q2.conj().T)[2][2:].conj().T           # V4 = {v1 + v2 + v3 = 0}, orthonormal
CONDITIONS = {"0": (), "V2": ("V2",), "V4": ("V4",), "L6": ("V2", "V4")}
TOL = 1e-9


def close(A, B):
    return bool(np.allclose(A, B, atol=TOL))


def neg(g):
    return tuple(-x for x in g)


def frame():
    named, _ = H.triplets()
    C = named["T"]
    Qt = C.conj().T @ H.gram_V() @ C
    K = np.linalg.cholesky((Qt + Qt.conj().T) / 2).conj().T
    return C, K


def reps(gL, gR, C, K):
    """the record's lifts gL, gR -> (rho_T, rho-bar_T, rho6, rho2, rho4), each as (rho(S), rho(T)), plus the raw
    matrices for the structural checks"""
    tL = MV.on_T(C, K, CT.on_V(CP.AUT["L"], gL))
    tR = MV.on_T(C, K, CT.on_V(CP.AUT["R"], gR))
    aL = SC.blocks_action(CP.AUT["L"], gL)
    aR = SC.blocks_action(CP.AUT["R"], gR)
    A = tL @ np.linalg.inv(tR) @ tL                         # T's matrix of S~ (a palindrome: either convention)
    rho_T = (A, np.linalg.inv(tL))                          # monodromy = inverse of the pullback; S = S~^-1, T = L
    rho_bar = (np.linalg.inv(A), tL)                        # W45's other kept identification
    s6 = aL @ np.linalg.inv(aR) @ aL                        # the six's matrix of S~ (pushforward = monodromy)
    rho6 = (np.linalg.inv(s6), aL)
    piece = lambda Q: (Q.conj().T @ rho6[0] @ Q, Q.conj().T @ rho6[1] @ Q)
    return {"T": rho_T, "T-bar": rho_bar, "six": rho6, "V2": piece(Q2), "V4": piece(Q4)}, (tL, tR, aL, aR, A, s6)


def exps(rT):
    """the exponents lambda_j in [0, 1) of rho(T) = diag e^{2 pi i lambda_j}"""
    return sorted(round(float(np.angle(z) / (2 * np.pi)) % 1.0, 9) % 1.0 for z in np.linalg.eigvals(np.array(rT)))


def tr(M):
    t = complex(np.trace(M))
    return [round(t.real, 9), round(t.imag, 9)]


def structure(R, raw):
    tL, tR, aL, aR, A, s6 = raw
    tRi, aRi = np.linalg.inv(tR), np.linalg.inv(aR)
    S6, T6 = R["six"]
    P2 = Q2 @ Q2.conj().T
    inv = all(close((np.eye(6) - P2) @ X @ P2, np.zeros((6, 6))) and close(P2 @ X @ (np.eye(6) - P2), np.zeros((6, 6)))
              for X in (aL, aR))
    scal = lambda M, z: close(M, z * np.eye(len(M)))
    out = {
        "the braid relation on T": close(tL @ tRi @ tL, tRi @ tL @ tRi),
        "the braid relation on the six": close(aL @ aRi @ aL, aRi @ aL @ aRi),
        "rho6(S)^2 = -I": scal(S6 @ S6, -1),
        "S~^4 on the six is I": scal(np.linalg.matrix_power(s6, 4), 1),
        "S~^4 on T is -I": scal(np.linalg.matrix_power(A, 4), -1),
        "V2 and V4 are invariant under the lifts": bool(inv),
        "tr rho(S): V2, V4": [tr(R["V2"][0]), tr(R["V4"][0])],
        "tr rho(ST): V2, V4": [tr(R["V2"][0] @ R["V2"][1]), tr(R["V4"][0] @ R["V4"][1])],
        "exponents: T, T-bar, six, V2, V4": [exps(R[n][1]) for n in ("T", "T-bar", "six", "V2", "V4")],
        "rho(S)^2 as a scalar: T, six, T-bar": [tr(R[n][0] @ R[n][0] / len(R[n][0])) for n in ("T", "six", "T-bar")],
    }
    out["the six's exponents are the union of T's and T-bar's"] = (
        sorted(out["exponents: T, T-bar, six, V2, V4"][2]) == sorted(out["exponents: T, T-bar, six, V2, V4"][0]
                                                                     + out["exponents: T, T-bar, six, V2, V4"][1]))
    # the puncture's exact sequence: rho(S)^2 e^{i pi k} at the untwisted weights 0 (H1), -1/2 (the six), -1 (H0) agree
    zs = [complex(np.trace(R[n][0] @ R[n][0])) / len(R[n][0]) * np.exp(1j * np.pi * w)
          for n, w in (("T", 0.0), ("six", -0.5), ("T-bar", -1.0))]
    out["the central scalars on the exact sequence (weights 0, -1/2, -1)"] = [tr(np.array([[z]])) for z in zs]
    out["the central scalars agree"] = bool(max(abs(z - zs[0]) for z in zs) < 1e-9)
    out["the twisted weights 3/2, 1, 1/2 are allowed"] = [IW.allowed(Fraction(3, 2), R["T"][0]),
                                                         IW.allowed(Fraction(1), R["six"][0]),
                                                         IW.allowed(Fraction(1, 2), R["T-bar"][0])]
    return out


def chis(R):
    c = lambda k, n: round(IW.chi(k, R[n][0], R[n][1])[0], 9)
    return {"chi_1(V2)": c(Fraction(1), "V2"), "chi_1(V4)": c(Fraction(1), "V4"), "chi_1(six)": c(Fraction(1), "six"),
            "chi_3/2(T)": c(Fraction(3, 2), "T"), "chi_1/2(T-bar)": c(Fraction(1, 2), "T-bar")}


def table(R):
    """the four-dimensional index: -chi_{3/2 + 12n}(rho_T) + sum over the condition's pieces of chi_{1 + 12n}"""
    out = {}
    for name, pieces in CONDITIONS.items():
        row = {}
        for n in (-1, 0, 1):
            v = -IW.chi(Fraction(3, 2) + 12 * n, *R["T"])[0] + sum(IW.chi(Fraction(1) + 12 * n, *R[p])[0] for p in pieces)
            row[str(n)] = round(v, 9)
        out[name] = row
    out["L6 by its H0 (chi_{1/2 + 12n}(T-bar))"] = {str(n): round(IW.chi(Fraction(1, 2) + 12 * n, *R["T-bar"])[0], 9)
                                                     for n in (-1, 0, 1)}
    return out


def second_route(R, with_T):
    dual = lambda n: (np.conj(R[n][0]), np.conj(R[n][1]))
    out = {"V2: M_1": IW.dims(*R["V2"], Fraction(1)), "V2: S_1 of the dual": IW.dims(*dual("V2"), Fraction(1), cusp=True),
           "V4: M_1": IW.dims(*R["V4"], Fraction(1)), "V4: S_1 of the dual": IW.dims(*dual("V4"), Fraction(1), cusp=True),
           "six: M_1": IW.dims(*R["six"], Fraction(1)),
           "six: S_1 of the dual": IW.dims(*dual("six"), Fraction(1), cusp=True)}
    if with_T:
        out.update({"T: M_3/2": IW.dims(*R["T"], Fraction(3, 2)),
                    "T: S_1/2 of the dual": IW.dims(*dual("T"), Fraction(1, 2), cusp=True),
                    "T-bar: M_1/2": IW.dims(*R["T-bar"], Fraction(1, 2)),
                    "T-bar: S_3/2 of the dual": IW.dims(*dual("T-bar"), Fraction(3, 2), cusp=True)})
    return out


def main():
    C, K = frame()
    choices = H.lift_choices()
    (_, gL, gR) = choices[0]
    signs = {}
    for sL, sR in itertools.product((1, -1), (1, -1)):
        hL, hR = (gL if sL > 0 else neg(gL)), (gR if sR > 0 else neg(gR))
        tL = MV.on_T(C, K, CT.on_V(CP.AUT["L"], hL))
        tR = MV.on_T(C, K, CT.on_V(CP.AUT["R"], hR))
        aL, aR = SC.blocks_action(CP.AUT["L"], hL), SC.blocks_action(CP.AUT["R"], hR)
        tRi, aRi = np.linalg.inv(tR), np.linalg.inv(aR)
        signs["L %+d, R %+d" % (sL, sR)] = [close(tL @ tRi @ tL, tRi @ tL @ tRi), close(aL @ aRi @ aL, aRi @ aL @ aRi)]
    eta2 = ([[np.exp(-1j * np.pi / 2)]], [[np.exp(2j * np.pi * 2 / 24)]])
    calib = {"eta^2: chi_1": round(IW.chi(Fraction(1), *eta2)[0], 9), "eta^2: M_1": IW.dims(*eta2, Fraction(1))}
    res = {}
    for label, (hL, hR) in (("the record's lifts", (gL, gR)), ("the other overall sign", (neg(gL), neg(gR)))):
        R, raw = reps(hL, hR, C, K)
        res[label] = {"H1: structure": structure(R, raw), "H2/H3: the formula": chis(R),
                      "H4: the second route (null count, gap)": second_route(R, label != "the record's lifts"),
                      "H5: the four-dimensional index, by condition and cusp units n": table(R)}
    d, o = res["the record's lifts"], res["the other overall sign"]
    size = {"0": 0, "V2": 2, "V4": 4, "L6": 6}
    want = {name: {str(n): n * (size[name] - 3) for n in (-1, 0, 1)} for name in CONDITIONS}

    def all_zero_dims(r):
        return all(v[0] == 0 for v in r.values())

    s1 = d["H1: structure"]
    checks = {
        "H1: the braid relation holds on T and on the six for exactly the same two of the four sign pairs": bool(
            sum(all(v) for v in signs.values()) == 2 and all(v[0] == v[1] for v in signs.values())),
        "H1: rho6(S)^2 = -I; S~^4 is I on the six and -I on T": bool(
            s1["rho6(S)^2 = -I"] and s1["S~^4 on the six is I"] and s1["S~^4 on T is -I"]),
        "H1: V2 and V4 invariant; tr rho(S) = 0, 0; tr rho(ST) = 1, -1": bool(
            s1["V2 and V4 are invariant under the lifts"] and s1["tr rho(S): V2, V4"] == [[0.0, 0.0], [0.0, 0.0]]
            and s1["tr rho(ST): V2, V4"] == [[1.0, 0.0], [-1.0, 0.0]]),
        "H1: the exponents of V2 and V4 are {1/8, 7/8} and {1/8, 3/8, 5/8, 7/8}": bool(
            s1["exponents: T, T-bar, six, V2, V4"][3] == [0.125, 0.875]
            and s1["exponents: T, T-bar, six, V2, V4"][4] == [0.125, 0.375, 0.625, 0.875]),
        "H1: the six's exponents are the union of T's and T-bar's (the lifts as built)": bool(
            s1["the six's exponents are the union of T's and T-bar's"]),
        "H1: the central scalars fit the exact sequence, and the twisted weights 3/2, 1, 1/2 are allowed": bool(
            s1["the central scalars agree"] and all(s1["the twisted weights 3/2, 1, 1/2 are allowed"])),
        "H2: chi_1(V2) = chi_1(V4) = 0 and chi_1(six) = chi_3/2(T) + chi_1/2(T-bar) = 0": bool(
            all(abs(v) < TOL for v in d["H2/H3: the formula"].values())),
        "H2: the calibration eta^2 at weight 1 gives 1": abs(calib["eta^2: chi_1"] - 1) < TOL,
        "H3: under the other overall sign the braid relation holds and every chi is 0, W45's included": bool(
            o["H1: structure"]["the braid relation on T"] and o["H1: structure"]["the braid relation on the six"]
            and all(abs(v) < TOL for v in o["H2/H3: the formula"].values())),
        "H4: eta^2 has dimension 1": calib["eta^2: M_1"][0] == 1,
        "H4: every space of the second route is zero, under both signs": bool(
            all_zero_dims(d["H4: the second route (null count, gap)"])
            and all_zero_dims(o["H4: the second route (null count, gap)"])),
        "H5: the index is n(|Lambda+| - 3) for every condition and n in {-1, 0, 1}, under both signs": bool(
            all(abs(r["H5: the four-dimensional index, by condition and cusp units n"][name][k] - v) < TOL
                for r in (d, o) for name, row in want.items() for k, v in row.items())
            and all(abs(r["H5: the four-dimensional index, by condition and cusp units n"]["L6"][k]
                        - r["H5: the four-dimensional index, by condition and cusp units n"][
                            "L6 by its H0 (chi_{1/2 + 12n}(T-bar))"][k]) < TOL for r in (d, o) for k in ("-1", "0", "1"))),
    }
    out = {"status": "W46: the four-dimensional index for every end condition the weave keeps (the rule first)",
           "the lift sign pairs: [braid relation on T, on the six]": signs,
           "the lift pairs W21 keeps (lift_choices)": len(choices),
           "the calibration": calib, **res,
           "checks": {k: bool(v) for k, v in checks.items()}, "every check holds": bool(all(checks.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["checks"], indent=1))
    print("every check holds:", out["every check holds"])


if __name__ == "__main__":
    main()
