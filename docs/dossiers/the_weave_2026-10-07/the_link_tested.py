#!/usr/bin/env python3
"""W27 of the weave: THE DERIVATION WITH ITS ONE LINK STATED, AND THE LINK TESTED. The rule is W27_RULE.md, committed
before this ran (6da777ea). Exact rational arithmetic.

  T1 anomalies: three 27s of E6 under SU(3) x SU(2) x U(1)_Y (the standard hypercharge, F-MC's direction), per 27 and
     for three; SU(3)^3, SU(3)^2 Y, SU(2)^2 Y, Y^3, grav^2 Y, and the SU(2) global anomaly (doublets even); controls: one
     Standard Model generation with nu^c, and the 27's remainder.
  T2 the count under the link: W24 D0's commutants (2 without the parity grading, 1 with it) re-read from the record.
  T3 the six-dimensional reading: Dobrescu-Poppitz's N(2+) - N(2-) = 0 mod 6 for k parity sectors of rank 2 with the
     left-handed fields of one 6d chirality; and the unbalanced local count stated.
  T4 what the link with F-MC implies beyond the three: the 27's content.

    python3 the_link_tested.py   ->  the_link_tested.json beside it
"""
import json
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent

# left-handed Weyl fermions: (name, SU(3) rep as 3 / -3 (anti) / 1, SU(2) dim, Y)
SM_GENERATION = [("Q", 3, 2, F(1, 6)), ("u^c", -3, 1, F(-2, 3)), ("d^c", -3, 1, F(1, 3)),
                 ("L", 1, 2, F(-1, 2)), ("e^c", 1, 1, F(1)), ("nu^c", 1, 1, F(0))]
REMAINDER = [("D", 3, 1, F(-1, 3)), ("D^c", -3, 1, F(1, 3)), ("H_u", 1, 2, F(1, 2)), ("H_d", 1, 2, F(-1, 2)),
             ("S", 1, 1, F(0))]
TWENTY_SEVEN = SM_GENERATION + REMAINDER


def dim3(r):
    return 3 if abs(r) == 3 else 1


def anomalies(fields):
    a = {"SU(3)^3": F(0), "SU(3)^2 Y": F(0), "SU(2)^2 Y": F(0), "Y^3": F(0), "grav^2 Y": F(0), "SU(2) doublets": 0}
    for _, r3, d2, y in fields:
        n3 = dim3(r3)
        if abs(r3) == 3:
            a["SU(3)^3"] += (1 if r3 > 0 else -1) * d2
            a["SU(3)^2 Y"] += F(1, 2) * d2 * y
        if d2 == 2:
            a["SU(2)^2 Y"] += F(1, 2) * n3 * y
            a["SU(2) doublets"] += n3
        a["Y^3"] += n3 * d2 * y ** 3
        a["grav^2 Y"] += n3 * d2 * y
    return a


def clean(a):
    return {k: (str(v) if isinstance(v, F) else v) for k, v in a.items()}


def free(a):
    return all(v == 0 for k, v in a.items() if k != "SU(2) doublets") and a["SU(2) doublets"] % 2 == 0


def run():
    res = {"rule": "W27_RULE.md (committed 6da777ea before this ran)"}
    a27 = anomalies(TWENTY_SEVEN)
    a3 = anomalies(TWENTY_SEVEN * 3)
    asm = anomalies(SM_GENERATION)
    arem = anomalies(REMAINDER)
    dims = sum(dim3(r) * d for _, r, d, _ in TWENTY_SEVEN)
    res["T1 anomalies"] = {
        "the 27's dimension (check)": dims,
        "one 27": clean(a27), "three 27s": clean(a3),
        "control: one Standard Model generation with nu^c": clean(asm),
        "control: the 27's remainder (D, D^c, H_u, H_d, S)": clean(arem),
        "all free": bool(free(a27) and free(a3) and free(asm) and free(arem))}
    w24 = json.load(open(HERE / "the_six_dimensional_census.json"))["D the gauge side"]
    res["T2 the count under the link"] = {
        "W24 D0: commutant of the moves' lifts on the six local solutions": w24[
            "D0 commutant of the moves' lifts on the six local solutions"],
        "W24 D0: the indices the moves alone keep": w24["D0 the conditions every move keeps and their indices"],
        "W24 D0: with the parity grading (the link keeps the sectors apart)": w24[
            "D0 with the parity grading added: commutant"],
        "under the link the index is +-3 only": bool(w24["D0 with the parity grading added: commutant"] == 1)}
    doublets_per_generation = sum(dim3(r) for _, r, d, _ in SM_GENERATION if d == 2)
    t3 = {"SU(2) doublets of one Standard Model generation (Q's colours and L)": doublets_per_generation,
          "rank of each parity sector's bundle (chi_p (x) rho_Q)": 2}
    rows = {}
    for k in range(1, 7):
        n = 2 * doublets_per_generation * k
        rows[str(k)] = {"N(2+) - N(2-)": n, "= 0 mod 6": bool(n % 6 == 0)}
    t3["by the number of parity sectors k"] = rows
    t3["passes exactly when k = 0 mod 3"] = all(rows[str(k)]["= 0 mod 6"] == (k % 3 == 0) for k in range(1, 7))
    weyl_per_generation = sum(dim3(r) * d for _, r, d, _ in SM_GENERATION)
    t3["the local gravitational count (all one 6d chirality): Weyl fermions per sector, unbalanced"] = 2 * weyl_per_generation
    res["T3 the six-dimensional reading (Dobrescu-Poppitz's global SU(2) condition)"] = t3
    res["T4 what the link with F-MC implies beyond the three (per generation, three of each)"] = {
        name: {"SU(3)": ("3" if r == 3 else "3-bar" if r == -3 else "1"), "SU(2)": d, "Y": str(y)}
        for name, r, d, y in REMAINDER + [SM_GENERATION[-1]]}
    res["verdict"] = {"T1 anomaly-free": res["T1 anomalies"]["all free"],
                      "T2 the count is three under the link": res["T2 the count under the link"][
                          "under the link the index is +-3 only"],
                      "T3 the six-dimensional global condition selects k = 0 mod 3": bool(t3["passes exactly when k = 0 mod 3"])}
    return res


if __name__ == "__main__":
    out = run()
    with open(HERE / "the_link_tested.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(json.dumps(out, indent=1, ensure_ascii=False))
