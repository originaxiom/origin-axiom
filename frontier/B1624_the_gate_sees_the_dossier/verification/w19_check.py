#!/usr/bin/env python3
"""B1624 -- the SM seat's W19, its numerical facts checked on main by two routes (exact fractions; no data):
 F1  the dimension of M_{1,2}: 3g - 3 + n = 2 (a complex surface: the even-dimensional object FK11 asks for);
 F2  chi(SL(2, Z)) by the amalgam Z/4 *_{Z/2} Z/6: 1/4 + 1/6 - 1/2 = -1/12 (= chi(M_{1,1}));
 F3  chi(Aut+(F_2)) by the extension 1 -> Inn(F_2) = F_2 -> Aut+(F_2) -> Out+(F_2) = SL(2, Z) -> 1: chi(F_2) chi(SL(2, Z));
 F4  chi(M_{1,2}) by the Harer--Zagier forgetful recursion chi(M_{g,n+1}) = (2 - 2g - n) chi(M_{g,n}) from chi(M_{1,1});
 F5  F3 and F4 agree (= 1/12, non-zero).
The orbifold-locus sentence of W19 ("the three parities are its orbifold locus") is not checked here.  Writes w19_check.json."""
import json, pathlib
from fractions import Fraction as Q
HERE = pathlib.Path(__file__).resolve().parent


def main():
    g, n = 1, 2
    dim = 3 * g - 3 + n
    chi_sl2z = Q(1, 4) + Q(1, 6) - Q(1, 2)
    chi_f2 = Q(1 - 2)                                   # a free group of rank 2: 1 - 2
    chi_aut = chi_f2 * chi_sl2z
    chi_m11 = chi_sl2z
    chi_m12 = (2 - 2 * 1 - 1) * chi_m11
    out = {"F1_dim_C_M12": dim, "F2_chi_SL2Z": str(chi_sl2z), "F3_chi_AutPlus_F2": str(chi_aut),
           "F4_chi_M12_harer_zagier": str(chi_m12), "F5_agree_and_nonzero": chi_aut == chi_m12 != 0}
    json.dump(out, open(HERE / "w19_check.json", "w"), indent=1); print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
