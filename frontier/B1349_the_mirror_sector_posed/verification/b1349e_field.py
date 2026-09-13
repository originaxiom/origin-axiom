"""Does the ear-dependent reading LEAVE Q(zeta_60)?  Proved, not asserted from a printed radical.

The printed char-poly coefficients carried sqrt6/sqrt30/sqrt(5+-sqrt5) -- those are sympy's
non-canonical radical forms of elements that are in Q(zeta_60) by construction. So the field
question must be settled on the EIGENVALUE's own minimal polynomial, and on whether sqrt2
lies in Q(zeta_60) -- decided by factoring Phi_60 over Q(sqrt2).
"""
import sympy as sp
t, x = sp.symbols('t x')
phi = (1 + sp.sqrt(5)) / 2

print("=" * 78)
print("1. the ear-dependent eigenvalues and their minimal polynomials over Q")
print("=" * 78)
for name, val in [("phi^2/(2 sqrt2)", phi**2 / (2 * sp.sqrt(2))),
                  ("sqrt10/4",        sp.sqrt(10) / 4),
                  ("-1/(2 phi)",      -1 / (2 * phi)),
                  ("1/2",             sp.Rational(1, 2))]:
    mp = sp.minimal_polynomial(val, t)
    print(f"  {name:>16s} : min poly {str(mp):<34s} degree {sp.degree(mp, t)}"
          f"   numeric {float(sp.N(val)):+.12f}")

print()
print("=" * 78)
print("2. is sqrt2 in Q(zeta_60)?   <=>  does Phi_60 stay irreducible over Q(sqrt2)?")
print("=" * 78)
PHI60 = sp.cyclotomic_poly(60, x)
print(f"  deg Phi_60 = {sp.degree(PHI60, x)}  (so [Q(zeta_60):Q] = 16)")
fl = sp.factor_list(PHI60, x, extension=sp.sqrt(2))
degs = sorted(sp.degree(f, x) for f, _ in fl[1])
print(f"  factor degrees of Phi_60 over Q(sqrt2): {degs}")
irred_over_sqrt2 = (degs == [16])
print(f"  Phi_60 irreducible over Q(sqrt2) ? {irred_over_sqrt2}")
print(f"  => [Q(sqrt2, zeta_60):Q] = {2 * (16 if irred_over_sqrt2 else 0)}"
      f"  vs [Q(zeta_60):Q] = 16   =>  sqrt2 NOT in Q(zeta_60): {irred_over_sqrt2}")
assert irred_over_sqrt2, "if this fails the field claim is WRONG"
# independent cross-check: conductor of Q(sqrt2) is 8, and 8 does not divide 60 (Kronecker-Weber)
print(f"  cross-check (Kronecker-Weber): conductor(Q(sqrt2)) = 8, 8 | 60 ? {60 % 8 == 0}")

print()
print("=" * 78)
print("3. CONTROL: the ear-INDEPENDENT values DO lie in Q(zeta_60)")
print("=" * 78)
for name, val in [("sqrt5", sp.sqrt(5)), ("-1/(2phi)", -1 / (2 * phi))]:
    fl2 = sp.factor_list(PHI60, x, extension=val)
    d2 = sorted(sp.degree(f, x) for f, _ in fl2[1])
    print(f"  Phi_60 over Q({name}): factor degrees {d2}"
          f"  ->  {name} IS in Q(zeta_60): {d2 != [16]}")
    assert d2 != [16], f"{name} should be inside Q(zeta_60)"
print()
print("  CONCLUSION: the four ear-INDEPENDENT readings {0, 1/2, -1/(2phi), 1} lie in")
print("  Q(sqrt5) subset Q(zeta_60) -- the field of the modular data itself.")
print("  The ear-DEPENDENT extremes phi^2/(2sqrt2), sqrt10/4 generate Q(sqrt2,sqrt5) and")
print("  do NOT: selecting an ear costs an extension the modular data does not contain.")
