#!/usr/bin/env python3
"""SM-C2, harvest row 1527 (ELECTROWEAK_VECTOR_MATCHING_AND_HEAVY_RESPONSE @ 7f59ec2b9): this seat's own exact check of
(4)-(6) the leading mass block and its eigenvalues m_W^2 = 5s/l^2, m_Z^2 = 8s/l^2, sin^2 = 3/8; kappa(t_Z^2) = 1/2;
(7) d_perp = d - (4/5)(1,...,1), kappa(d_perp^2) = 14/25, its grade-ordered form -(1/5)diag(2,-1,-2,-1,2), and that it is
the m = 0 member of the principal spin-two in sl5 (proportional to 3 J3^2 - 6); (9) the neutral second-order coefficient
56/15 from the stated source (5/(2 l^2)) sqrt(8/5) d_perp and P0 eigenvalue 3/l^2; (10)-(11) the charged 4/3; the wedge
coefficient 2/5 of b0^b1^b2^b3^b4 in b2 ^ Z_high ^ Z_low; (12) rho = 1 + s/5 + O(s^2). No measured value enters.
Planted: a P0 eigenvalue of 2/l^2 (j = 1 instead of 2) must change (9)."""
import json
import sys
from itertools import permutations
from pathlib import Path

import sympy as sp

s, l = sp.symbols("s ell", positive=True)
R = sp.Rational
out = {}
block = 5 / l ** 2 * sp.Matrix([[1, -sp.sqrt(R(3, 5))], [-sp.sqrt(R(3, 5)), R(3, 5)]])
ev = sorted(block.eigenvals().keys(), key=lambda x: float(x.subs(l, 1)))
out["neutral_block_eigenvalues"] = [str(sp.simplify(x)) for x in ev]
photon = sp.Matrix([sp.sqrt(R(3, 5)), 1])
sin2 = sp.simplify(photon[0] ** 2 / (photon.T * photon)[0])
out["sin2_theta"] = str(sin2)
kZ = sp.simplify((R(1, 2) + R(3, 5) * R(1, 2)) / R(8, 5))
out["kappa_tZ2"] = str(kZ)
d = sp.Matrix([1, 1, R(2, 5), R(6, 5), R(2, 5)])
dperp = d - R(4, 5) * sp.ones(5, 1)
out["d_perp"] = [str(x) for x in dperp]
kd = sum(x ** 2 for x in dperp)        # kappa = (1/2) Tr_10 of diag(d, -d) = sum d_i^2
out["kappa_dperp2"] = str(kd)
order = [6, 4, 7, 5, 8]                 # coordinates 4..8 -> indices 0..4
graded = sp.Matrix([dperp[c - 4] for c in order])
out["graded"] = [str(x) for x in graded]
J3 = sp.diag(-2, -1, 0, 1, 2)
m0 = 3 * J3 ** 2 - 6 * sp.eye(5)
prop = sp.simplify(sp.Matrix([m0[i, i] for i in range(5)]) / m0[0, 0] - graded / graded[0])
out["graded_is_spin2_m0"] = all(x == 0 for x in prop)


def second_order(source_norm2, eig, kappa_norm):
    return sp.simplify(source_norm2 / eig / kappa_norm)


src_Z2 = (5 / (2 * l ** 2)) ** 2 * R(8, 5) * kd
cZ = second_order(src_Z2, 3 / l ** 2, kZ)
cW = second_order((2 / l ** 2) ** 2, 3 / l ** 2, 1)
out["neutral_coefficient"], out["charged_coefficient"] = str(sp.simplify(cZ * l ** 2)), str(sp.simplify(cW * l ** 2))
mW2 = (5 * s - sp.simplify(cW * l ** 2) * s ** 2) / l ** 2
mZ2 = (8 * s - sp.simplify(cZ * l ** 2) * s ** 2) / l ** 2
rho = sp.series(sp.simplify(mW2 / (mZ2 * R(5, 8))), s, 0, 2).removeO()
out["rho_series"] = str(sp.simplify(rho))
# the wedge coefficient: b2 ^ Z_high ^ Z_low, coefficient of b0^b1^b2^b3^b4
def wedge_coeff(terms):
    tot = 0
    for coef, idx in terms:
        if len(set(idx)) < 5:
            continue
        perm = list(idx)
        sign = 1
        for i in range(5):
            for j in range(i + 1, 5):
                if perm[i] > perm[j]:
                    sign = -sign
        tot += sign * coef
    return sp.simplify(tot)


Zh = [(sp.sqrt(R(2, 5)), (1, 4)), (-sp.sqrt(R(3, 5)), (2, 3))]
Zl = [(sp.sqrt(R(2, 5)), (0, 3)), (-sp.sqrt(R(3, 5)), (1, 2))]
terms = [(c1 * c2, (2,) + i1 + i2) for c1, i1 in Zh for c2, i2 in Zl]
out["wedge_coefficient_abs"] = str(abs(wedge_coeff(terms)))
ok = ([sp.simplify(x * l ** 2) for x in ev] == [0, 8] and sin2 == R(3, 8) and kZ == R(1, 2) and kd == R(14, 25)
      and list(graded) == [R(-2, 5), R(1, 5), R(2, 5), R(1, 5), R(-2, 5)] and out["graded_is_spin2_m0"]
      and sp.simplify(cZ * l ** 2) == R(56, 15) and sp.simplify(cW * l ** 2) == R(4, 3)
      and sp.simplify(rho - (1 + s / 5)) == 0 and abs(wedge_coeff(terms)) == R(2, 5))
bad = second_order(src_Z2, 2 / l ** 2, kZ)
out["PLANTED_wrong_P0_eigenvalue_caught"] = bool(sp.simplify(bad * l ** 2) != R(56, 15))
out["all_claims_hold_and_plants_caught"] = bool(ok and out["PLANTED_wrong_P0_eigenvalue_caught"])
Path(sys.argv[1]).write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
print(json.dumps(out, indent=1))
