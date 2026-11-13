#!/usr/bin/env python3
"""SM-C6 E5 part 1: the deck's Z/3 anomaly on s961 (card relays/cards/SM_C6_E5_the-decks-anomaly-on-s961.md, pushed
first).  Reads B1432's census of s961 from a checkout of main (first argument).  Data-free.
    python3 run_e5.py MAIN_CHECKOUT [out.json]"""
import sys, json, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
MAIN = pathlib.Path(sys.argv[1]).resolve()
CEN = MAIN / "frontier" / "B1432_the_three_fold_cover_fires_off_the_lift" / "verification" / "census_M1_M5.json"
# the chosen dictionary: sector -> (SU(3) index T, SU(2) index T, dimension, hypercharge Y)
SECT = {"Q": (Fr(1, 2) * 2, Fr(1, 2) * 3, 6, Fr(1, 6)), "u^c": (Fr(1, 2), 0, 3, Fr(-2, 3)), "e^c": (0, 0, 1, Fr(1)),
        "d^c": (Fr(1, 2), 0, 3, Fr(1, 3)), "L": (0, Fr(1, 2), 2, Fr(-1, 2)), "nu^c": (0, 0, 1, Fr(0))}


def coeffs(members):
    """members: list of (charge q, sign sigma) with the generation content sigma * (every sector once)"""
    su3 = sum(q * s * SECT[k][0] for q, s in members for k in SECT)
    su2 = sum(q * s * SECT[k][1] for q, s in members for k in SECT)
    grav = sum(q * s * SECT[k][2] for q, s in members for k in SECT)
    cub = sum(q ** 3 * s * SECT[k][2] for q, s in members for k in SECT)
    y2 = sum(q * s * SECT[k][2] * SECT[k][3] ** 2 for q, s in members for k in SECT)
    return {"Z3-SU(3)^2": su3, "Z3-SU(2)^2": su2, "Z3-grav^2": grav, "Z3^3": cub, "Z3-U(1)_Y^2 (information)": y2}


def mod3(x):
    x = Fr(x)
    return None if x.denominator % 3 == 0 else (x.numerator * pow(x.denominator, -1, 3)) % 3


def main():
    d = json.load(open(CEN))["M3"]
    assert d["backgrounds_by_orbit_size"] == {"3": 48} and d["index_deck_invariant"] and d["background_orbits_closed"]
    assert d["abs_counts"] == {"1": 48} and d["nuc"]["same_sign_as_generation"] == 48
    n_orbits = d["background_orbits"]["3"]; plus = d["signs"]["1"] // 3; minus = d["signs"]["-1"] // 3
    assert plus + minus == n_orbits
    rows = []
    for sigma, count in ((1, plus), (-1, minus)):
        c = coeffs([(q, sigma) for q in (0, 1, 2)])
        rows.append({"sign": sigma, "orbits": count, "coefficients": {k: str(v) for k, v in c.items()},
                     "mod3": {k: mod3(v) for k, v in c.items()}})
    tot = {k: sum(Fr(r["coefficients"][k]) * r["orbits"] for r in rows) for k in rows[0]["coefficients"]}
    robust = [k for k in tot if "information" not in k]
    p1 = coeffs([(q, 1) for q in (0, 0, 1)]); p2 = coeffs([(1, 1)])
    out = {"orbits": {"+": plus, "-": minus}, "per_orbit": rows, "total": {k: str(v) for k, v in tot.items()},
           "total_mod3": {k: mod3(v) for k, v in tot.items()},
           "robust_all_zero_mod3": all(mod3(Fr(r["coefficients"][k])) == 0 for r in rows for k in robust),
           "P1_charges_001_nonzero": any(mod3(p1[k]) not in (0,) for k in robust),
           "P2_fixed_background_nonzero": any(mod3(p2[k]) not in (0,) for k in robust),
           "P1": {k: str(v) for k, v in p1.items()}, "P2": {k: str(v) for k, v in p2.items()}}
    json.dump(out, open(pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "e5_results.json", "w"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
