#!/usr/bin/env python3
"""SM-C4: the number of free parameters of the Standard Model, counted from its field content alone, before any table.

Yukawa sector: the real parameters of the Yukawa matrices, less the dimension of the flavour symmetry they break, plus the
dimension of what stays unbroken; each count split into moduli (real magnitudes and angles) and phases, since a unitary
U(n) has n(n-1)/2 angles and n(n+1)/2 phases.  Then the gauge couplings, the vacuum angle and the Higgs potential.
Three sectors: massless neutrinos; Dirac neutrinos (a Yukawa matrix for three right-handed neutrinos); Majorana
neutrinos (the dimension-five operator, a complex symmetric 3 x 3 matrix).  No value is used or written: only counts.
Usage: parameter_count.py OUT.json"""
import json
import sys

N = 3                                      # generations


def unitary(n):
    return {"angles": n * (n - 1) // 2, "phases": n * (n + 1) // 2}


def general(n):                             # a complex n x n matrix
    return {"moduli": n * n, "phases": n * n}


def symmetric(n):                           # a complex symmetric n x n matrix
    k = n * (n + 1) // 2
    return {"moduli": k, "phases": k}


def count(yukawas, flavour_factors, unbroken_phases):
    mod = sum(y["moduli"] for y in yukawas) - flavour_factors * unitary(N)["angles"]
    ph = sum(y["phases"] for y in yukawas) - flavour_factors * unitary(N)["phases"] + unbroken_phases
    return {"moduli": mod, "phases": ph, "total": mod + ph}


GAUGE, THETA, HIGGS = 3, 1, 2               # g1, g2, g3; the strong vacuum angle; the Higgs quadratic and quartic
sectors = {
    # Y_u, Y_d, Y_e; U(3) for Q, u, d, L, e; unbroken U(1)_B x U(1)_e x U(1)_mu x U(1)_tau
    "massless neutrinos": count([general(N)] * 3, 5, 4),
    # Y_u, Y_d, Y_e, Y_nu; U(3) for Q, u, d, L, e, nu; unbroken U(1)_B x U(1)_L
    "Dirac neutrinos": count([general(N)] * 4, 6, 2),
    # Y_u, Y_d, Y_e and the symmetric Weinberg coefficient; U(3) for Q, u, d, L, e; unbroken U(1)_B
    "Majorana neutrinos": count([general(N)] * 3 + [symmetric(N)], 5, 1),
}
out = {"generations": N, "gauge_couplings": GAUGE, "vacuum_angles": THETA, "higgs_potential": HIGGS, "flavour": sectors}
for k, v in sectors.items():
    v["all"] = v["total"] + GAUGE + THETA + HIGGS
base = sectors["massless neutrinos"]
expected = {  # what the rows of the table must add up to, by kind
    "massless neutrinos": {"masses": 9, "mixing angles": 3, "CP phases": 1},
    "Dirac neutrinos": {"masses": 12, "mixing angles": 6, "CP phases": 2},
    "Majorana neutrinos": {"masses": 12, "mixing angles": 6, "CP phases": 4},
}
out["checks"] = {
    "massless: 13 flavour parameters, 19 in all": base["total"] == 13 and base["all"] == 19,
    "Dirac: 7 more than massless (26 in all)": sectors["Dirac neutrinos"]["all"] - base["all"] == 7,
    "Majorana: 9 more than massless (28 in all)": sectors["Majorana neutrinos"]["all"] - base["all"] == 9,
    "moduli = masses + angles and phases = CP phases, in each sector": all(
        sectors[k]["moduli"] == e["masses"] + e["mixing angles"] and sectors[k]["phases"] == e["CP phases"] for k, e in expected.items()),
}
out["by_kind_the_table_must_match"] = expected
# planted: a sector's count with one flavour factor left out must disagree
planted = count([general(N)] * 3, 4, 4)
out["PLANTED_one_flavour_factor_omitted"] = planted
out["PLANTED_caught"] = planted["total"] != 13
out["all_hold"] = all(out["checks"].values()) and out["PLANTED_caught"]
json.dump(out, open(sys.argv[1], "w"), indent=1)
print(json.dumps(out, indent=1))
