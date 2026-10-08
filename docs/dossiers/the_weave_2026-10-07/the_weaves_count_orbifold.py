#!/usr/bin/env python3
"""W20, a third route (after its census): THE WEAVE'S COUNT AS AN ORBIFOLD INDEX, from the traces at the elliptic points.

W20 counted -chi(G; 27) for G = Aut+(F2), the 27 carried by the moves' own SL(2) on the records through each SL(2) in
E6, by the amalgam and by Eichler-Shimura. This route uses neither. Brown's formula for a group with a torsion-free
subgroup of finite index (Cohomology of Groups, IX.7) gives the Euler characteristic with rational coefficients as a sum
over the conjugacy classes of elements of finite order, each weighted by the orbifold Euler characteristic of its
centralizer and the trace of the element:
    chi(SL(2, Z); V) = -(1/12)[tr(I) + tr(-I)] + (1/4)[tr(S) + tr(S^-1)] + (1/6)[tr(U) + tr(U^-1) + tr(U^2) + tr(U^-2)],
with S of order 4 (the square torus) and U of order 6 (the hexagonal torus). Under an SL(2) in E6 with semisimple
element h, these elements act on a weight vector of h-eigenvalue m by i^m, e^(i pi m / 3), e^(2 i pi m / 3) and (-1)^m.
The fibre adds -chi(SL(2, Z); H (x) V), with the traces of H, the records, multiplied in.

So the count is a sum of a bulk term (the rank over twelve, twice) and the contributions of the weave's orbifold
points: the shape of an orbifold index, with the twisted sectors at the square and hexagonal tori.

    python3 the_weaves_count_orbifold.py   ->  the_weaves_count_orbifold.json beside it
"""
import cmath
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_weaves_count_in_e6 as E  # noqa: E402

# name: (j, n) for the element conjugate to diag(e^(i pi j / n), e^(-i pi j / n)), acting on h-eigenvalue m by
# exp(i pi j m / n): S = diag(i, -i) is (1, 2), U = diag(e^(i pi / 3), e^(-i pi / 3)) is (1, 3), -I is (1, 1)
ELEMENTS = {"I": (0, 1), "-I": (1, 1), "S": (1, 2), "S^-1": (-1, 2), "U": (1, 3), "U^-1": (-1, 3), "U^2": (2, 3),
            "U^-2": (-2, 3)}
WEIGHT = {"I": Fraction(-1, 12), "-I": Fraction(-1, 12), "S": Fraction(1, 4), "S^-1": Fraction(1, 4),
          "U": Fraction(1, 6), "U^-1": Fraction(1, 6), "U^2": Fraction(1, 6), "U^-2": Fraction(1, 6)}


def phase(j, n, m):
    """exp(i pi j m / n)"""
    if n == 1:
        return 1 if j == 0 else (-1) ** m
    return cmath.exp(1j * cmath.pi * j * m / n)


def traces(eigs):
    return {g: sum(phase(j, n, m) for m in eigs) for g, (j, n) in ELEMENTS.items()}


def chi_brown(tr):
    s = sum(complex(WEIGHT[g]) * tr[g] for g in ELEMENTS)
    assert abs(s.imag) < 1e-9 and abs(s.real - round(s.real)) < 1e-9, s
    return int(round(s.real))


def main():
    hs, _ = E.orbits()
    rows = {}
    h_eigs = [1, -1]                                    # the records: H, eigenvalues of the standard sl2's H
    for name, c in hs.items():
        e27 = [int(v) for v in E.weight_values(c, E.W27)]
        t27 = traces(e27)
        # H (x) 27: eigenvalues m + 1 and m - 1
        t_h27 = traces([m + s for m in e27 for s in h_eigs])
        chi = chi_brown(t27) - chi_brown(t_h27)
        rows[name] = {"-chi(G; 27), Brown": -chi,
                      "traces on the 27 at the elliptic elements": {g: round(t27[g].real, 9) for g in ("S", "U", "U^2", "-I")},
                      "the bulk term, 27/12 twice": float(Fraction(27, 6)),
                      "the square torus's term": round(float(-(Fraction(1, 4)) * 2 * t27["S"].real), 9)}
    w20 = json.loads((HERE / "the_weaves_count_in_e6.json").read_text(encoding="utf-8"))
    agree = all(rows[n]["-chi(G; 27), Brown"] == w20["-chi(G; 27) by orbit"][n] for n in rows)
    dist = {n: rows[n] for n in ("E6", "E6(a1)", "E6(a3)")}
    out = {"route": "Brown's formula over the elliptic elements of SL(2, Z), with the fibre's term",
           "agrees with W20's two routes on all 21 orbits": agree,
           "the distinguished orbits": dist,
           "-chi(G; 27) by orbit (Brown)": {n: r["-chi(G; 27), Brown"] for n, r in rows.items()},
           "rows": rows}
    return out


if __name__ == "__main__":
    res = main()
    with open(HERE / "the_weaves_count_orbifold.json", "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    print("agrees with W20 on all 21:", res["agrees with W20's two routes on all 21 orbits"])
    for n, r in res["the distinguished orbits"].items():
        print(n, r["-chi(G; 27), Brown"], r["traces on the 27 at the elliptic elements"])
