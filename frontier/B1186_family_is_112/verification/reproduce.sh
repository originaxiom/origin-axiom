#!/usr/bin/env bash
# B1186 -- the family-definition cell: |F| = 112 (census- and bound-scoped), criteria nested.
# Fast path: exact symbolic certification of the corrective member t06829 + witnesses +
# count assertions against the committed enumeration. Full 212,641-manifold sweep:
#   OA_SLOW=1 bash reproduce.sh   (runs family_census.py, ~3 min, rewrites family_census.json)
set -euo pipefail
cd "$(dirname "$0")"
if [ "${OA_SLOW:-}" = "1" ]; then python3 family_census.py family_census.json; fi
python3 - << 'PY' 2>/dev/null | tee family_checks.txt
import json, snappy, sympy as sp, mpmath as mp
from fractions import Fraction
mp.mp.dps = 60
S3 = sp.sqrt(3)

d = json.load(open("family_census.json"))
assert d["census_size"] == 212641
assert d["B_shape_field_in_Qsqrt3"] == 112 and d["A_all_regular"] == 77 and d["in_B_not_A"] == 35
assert len(d["members_B"]) == 112 and len(d["members_A"]) == 77
assert "t06829" in d["members_B"] and "t06829" not in d["members_A"]
assert d["carriers_2sqrt3i_excl_m004"] == ["o10_150684","o10_150685","o10_150693","o9_41001","o9_41009","t12840"]
assert d["amphichirality_failures"] == [] and d["quine_collisions"] == []
assert all(d["known_member_control"].values())
print("counts: |B| = 112, |A| = 77, B\\A = 35; six 2sqrt3i carriers; amphichirality 112/112;")
print("        zero quine collisions; all nine named witnesses members. (committed enumeration)")

def exact_certify(name):
    M = snappy.Manifold(name).high_precision()
    zs = []
    for z in M.tetrahedra_shapes('rect'):
        re = mp.mpf(str(z.real()).replace(' ','')); im = mp.mpf(str(z.imag()).replace(' ',''))
        fr = Fraction(float(re)).limit_denominator(256)
        fi = Fraction(float(im/mp.sqrt(3))).limit_denominator(256)
        if abs(mp.mpf(fr.numerator)/fr.denominator - re) > mp.mpf(10)**-40: return None
        if abs(mp.mpf(fi.numerator)/fi.denominator - im/mp.sqrt(3)) > mp.mpf(10)**-40: return None
        zs.append(sp.Rational(fr.numerator, fr.denominator) + sp.Rational(fi.numerator, fi.denominator)*S3*sp.I)
    for a, b, c in M.gluing_equations("rect"):
        prod = sp.Integer(c)
        for zj, aj, bj in zip(zs, a, b):
            prod *= zj**int(aj) * (1 - zj)**int(bj)
        if sp.simplify(sp.expand(prod - 1)) != 0: return False
    return True

assert exact_certify("t06829") is True      # THE CORRECTIVE MEMBER: exact solution in Q(sqrt-3)
assert exact_certify("t12840") is True      # member control
assert exact_certify("o9_41001") is True    # member control (den-7/14 shapes)
assert exact_certify("m006") is None        # non-member control: correctly excluded
print("EXACT: t06829's Q(sqrt-3) shapes solve the gluing equations SYMBOLICALLY (den 98 -- past")
print("       a bound-64 test); controls behave. THE FAMILY IS 112 at census scope, den bound 256.")
print("REPRODUCES")
PY
