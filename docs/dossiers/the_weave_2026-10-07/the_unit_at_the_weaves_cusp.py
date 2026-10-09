"""W47 (the rule: W47_RULE.md, committed before this script). Is one unit of end data at the weave's cusp forced?

  K1  exact: the coinvariants of H1(F2) under L and R (so the inner automorphisms die in the abelianization); the
      abelianization of B3 (sigma -> 1) on S~^8; the 24 characters eps_r = v_eta^r, eps_r(S) = e^{-i pi r/4},
      eps_r(T) = e^{2 pi i r/24}; which of them keep the forced weights 3/2 (T), 1 (the six) and 1/2 (T-bar).
  K2  the cusp exponents of T, T-bar, the six, V2 and V4 under every allowed twist, as numerators over 24.
  K3  the twisted index at n = 0 for W28's four puncture conditions and every r (0 when the twisted field has no
      sections); the L6 row against its H0 form chi_{1/2}(T-bar (x) eps_r).
  K4  the second route: q-expansion dimensions (W45's dims) for every allowed twist and piece.
  K5  the full table over the four conditions, the 24 characters and n in {-1, 0, 1} uniform cusp units.

Run: python3 the_unit_at_the_weaves_cusp.py  ->  the_unit_at_the_weaves_cusp.json beside it.
"""
import json
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_end_conditions_on_the_weaves_surface as EC  # noqa: E402  (W46: the pieces from the record's lifts)
import the_index_on_the_weaves_surface as IW  # noqa: E402  (W45: chi, allowed, dims)

CP, H = EC.CP, EC.H
OUT = HERE / "the_unit_at_the_weaves_cusp.json"
TOL = 1e-9
WEIGHT = {"T": Fraction(3, 2), "T-bar": Fraction(1, 2), "six": Fraction(1), "V2": Fraction(1), "V4": Fraction(1)}
FIBRE = {"0": -3, "V2": -1, "V4": 1, "L6": 3}


def eps(r):
    return np.exp(-1j * np.pi * r / 4), np.exp(2j * np.pi * r / 24)


def twisted(R, r):
    es, et = eps(r)
    return {n: (es * np.array(R[n][0]), et * np.array(R[n][1])) for n in R}


def chi_or_zero(k, rho):
    """the formula's chi_k, or 0 when the central character forbids the weight (no sections, no index)"""
    return IW.chi(k, *rho)[0] if IW.allowed(k, rho[0]) else 0.0


def index(Rr, cond, n):
    v = -chi_or_zero(Fraction(3, 2) + 12 * n, Rr["T"])
    for p in EC.CONDITIONS[cond]:
        v += chi_or_zero(Fraction(1) + 12 * n, Rr[p])
    return v


def K1(R):
    Lm, Rm = sp.Matrix(CP.MAT["L"]), sp.Matrix(CP.MAT["R"])
    snf = smith_normal_form((Lm - sp.eye(2)).row_join(Rm - sp.eye(2)), domain=sp.ZZ)
    invariants = [int(snf[i, i]) for i in range(min(snf.shape))]
    ab_St8 = 8 * 3                                          # S~ = sigma1 sigma2 sigma1 -> 3 under sigma -> 1
    keeps = {}
    for r in range(24):
        Rr = twisted(R, r)
        keeps[r] = [IW.allowed(WEIGHT[n], Rr[n][0]) for n in ("T", "six", "T-bar")]
    allowed = [r for r, v in keeps.items() if all(v)]
    return {"the coinvariants of H1(F2) under L and R: Smith invariants of [L - 1 | R - 1]": invariants,
            "the coinvariants vanish": all(abs(x) == 1 for x in invariants),
            "the abelianization of B3 (sigma -> 1) on S~^8": ab_St8,
            "eps_r keeps the weights 3/2 (T), 1 (six), 1/2 (T-bar)": {str(r): v for r, v in keeps.items()},
            "the allowed r": allowed,
            "no r keeps only some of the three": all(all(v) or not any(v) for v in keeps.values())}, allowed


def K2(R, allowed):
    out, odd = {}, True
    for r in allowed:
        Rr = twisted(R, r)
        row = {}
        for n in ("T", "T-bar", "six", "V2", "V4"):
            nums = sorted(int(round(24 * x)) % 24 for x in EC.exps(Rr[n][1]))
            row[n] = nums
            odd &= all(x % 2 == 1 for x in nums)
        out[str(r)] = row
    return {"the exponents times 24, by allowed r and piece": out, "every numerator is odd": bool(odd)}


def K3(R):
    tab, h0 = {}, {}
    for r in range(24):
        Rr = twisted(R, r)
        tab[str(r)] = {c: round(index(Rr, c, 0), 9) for c in EC.CONDITIONS}
        h0[str(r)] = round(chi_or_zero(Fraction(1, 2), Rr["T-bar"]), 9)
    return {"the twisted index at n = 0, by r and puncture condition": tab,
            "the L6 row's H0 form, chi_{1/2}(T-bar (x) eps_r)": h0}


def K4(R, allowed):
    out = {}
    for r in allowed:
        Rr = twisted(R, r)
        row = {}
        for n in ("T", "T-bar", "V2", "V4"):
            k = WEIGHT[n]
            M = IW.dims(*Rr[n], k)
            dual = (np.conj(Rr[n][0]), np.conj(Rr[n][1]))
            S = IW.dims(*dual, 2 - k, cusp=True) if 2 - k > 0 else (0, None)
            c = round(chi_or_zero(k, Rr[n]), 9)
            row[n] = {"dim M_k (null count, gap)": M, "dim S_(2-k) of the dual (null count, gap)": S, "chi_k": c,
                      "dim M_k - dim S_(2-k)": M[0] - S[0]}
        out[str(r)] = row
    return out


def K5(R):
    tab = {}
    for r in range(24):
        Rr = twisted(R, r)
        tab[str(r)] = {c: {str(n): round(index(Rr, c, n), 9) for n in (-1, 0, 1)} for c in EC.CONDITIONS}
    return tab


def main():
    C, K = EC.frame()
    (_, gL, gR) = H.lift_choices()[0]
    R, _ = EC.reps(gL, gR, C, K)
    k1, allowed = K1(R)
    k2 = K2(R, allowed)
    k3 = K3(R)
    k4 = K4(R, allowed)
    k5 = K5(R)
    want0 = {str(r): {c: 0.0 for c in EC.CONDITIONS} for r in range(24)}
    for r, c in ((4, "0"), (4, "V4"), (20, "V2"), (20, "L6")):
        want0[str(r)][c] = -1.0
    t3 = k3["the twisted index at n = 0, by r and puncture condition"]
    threes = sorted((r, c, n) for r, row in k5.items() for c, v in row.items() for n, x in v.items() if abs(abs(x) - 3) < TOL)
    al = [str(r) for r in allowed]
    want_threes = sorted((r, c, n) for r in al for c in ("0", "L6") for n in ("-1", "1") if abs(t3[r][c]) < TOL)
    checks = {
        "K1: the coinvariants vanish; S~^8 maps to 24; exactly r = 0 mod 4 keep the forced weights": bool(
            k1["the coinvariants vanish"] and k1["the abelianization of B3 (sigma -> 1) on S~^8"] == 24
            and allowed == [0, 4, 8, 12, 16, 20] and k1["no r keeps only some of the three"]),
        "K2: every cusp exponent is an odd multiple of 1/24 under every allowed twist": k2["every numerator is odd"],
        "K3: the twisted index at n = 0 is 0 except -1 at r = 4 (0, V4) and r = 20 (V2, L6)": bool(
            all(abs(t3[r][c] - want0[r][c]) < TOL for r in t3 for c in t3[r])),
        "K3: the L6 row equals its H0 form at every r": bool(
            all(abs(t3[r]["L6"] - k3["the L6 row's H0 form, chi_{1/2}(T-bar (x) eps_r)"][r]) < TOL for r in t3)),
        "K3: no twist gives +-3 at n = 0": bool(all(abs(abs(v) - 3) > TOL for row in t3.values() for v in row.values())),
        "K4: the q-expansion dimension differences equal chi for every allowed twist and piece": bool(
            all(abs(v["dim M_k - dim S_(2-k)"] - v["chi_k"]) < TOL for row in k4.values() for v in row.values())),
        "K5: I = n f + t at every allowed twist, and |I| = 3 only at 0 or L6 with t = 0 and n = +-1": bool(
            all(abs(k5[r][c][n] - (int(n) * FIBRE[c] + t3[r][c])) < TOL for r in al for c in k5[r] for n in k5[r][c])
            and threes == want_threes),
        "K5: a twist that does not keep the forced weights gives 0 for every condition and n (no sections)": bool(
            all(abs(k5[r][c][n]) < TOL for r in k5 if r not in al for c in k5[r] for n in k5[r][c])),
    }
    out = {"status": "W47: is one unit of end data at the weave's cusp forced? (the rule first)",
           "K1: the flat line bundles": k1, "K2: the cusp exponents": k2, "K3: the twisted index": k3,
           "K4: the second route (by allowed r and piece)": k4,
           "K5: the full table (r, condition, n)": k5, "K5: where |I| = 3": [list(x) for x in threes],
           "checks": {k: bool(v) for k, v in checks.items()}, "every check holds": bool(all(checks.values()))}
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["checks"], indent=1))
    print("every check holds:", out["every check holds"])


if __name__ == "__main__":
    main()
