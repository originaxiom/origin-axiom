#!/usr/bin/env python3
"""Exact certificate for the Riley component's peripheral sheet conjugacy.

Requires only SymPy.  It distinguishes two statements that coincide at the
parabolic holonomy but not on the full nonabelian component:

  * number-field conjugation at x^2 = 4: kappa -> 3-kappa;
  * the component's quadratic deck involution: kappa -> x^2-1-kappa.
"""

import sympy as sp


s, t, x, z, K = sp.symbols("s t x z K")

# Generalized Riley factor and its trace-coordinate form.
phi = s**4*t - s**4 + s**2*t**2 - 3*s**2*t + 3*s**2 + t - 1
P = z**2 - x**2*z + 2*x**2 - z - 1

# x=s+s^-1 and z=x^2-2+t=s^2+s^-2+t.
trace_substitution = sp.factor(
    phi.subs(t, z - (s**2 + s**-2))
    - s**2 * P.subs(x, s + s**-1)
)
assert trace_substitution == 0

disc_z = sp.factor(sp.discriminant(P, z))
assert sp.expand(disc_z - (x**2 - 5) * (x**2 - 1)) == 0

tau = x**2 - z
kappa = 2*x**2 + z**2 - x**2*z - 2

def mod_component(expr):
    return sp.factor(sp.rem(sp.Poly(expr, z), sp.Poly(P, z)).as_expr())

assert mod_component(kappa) == z - 1
defect = mod_component(tau + kappa - 3)
assert sp.expand(defect - (x**2 - 4)) == 0
assert sp.expand(tau + kappa - 3 - (P + x**2 - 4)) == 0

# The genuine global sheet involution exchanges the two z-roots of P.
sigma_z = x**2 + 1 - z
assert sp.expand(sigma_z.subs(z, sigma_z) - z) == 0
assert mod_component(P.subs(z, sigma_z)) == 0
sigma_kappa = mod_component(kappa.subs(z, sigma_z))
assert sp.expand(sigma_kappa - tau) == 0
assert mod_component(tau + kappa - (x**2 - 1)) == 0

# Equivalently kappa has this component-generic minimal polynomial.
kappa_minpoly = K**2 - (x**2 - 1)*K + (x**2 - 1)
assert mod_component(kappa_minpoly.subs(K, kappa)) == 0

# The constant root-sum 3 occurs exactly on the parabolic divisor x^2=4.
assert sp.expand(sp.resultant(P, x**2 - 4, z) - (x**2 - 4)**2) == 0
for meridian_trace in (2, -2):
    assert sp.rem(
        sp.Poly((tau + kappa - 3).subs(x, meridian_trace), z),
        sp.Poly(P.subs(x, meridian_trace), z),
    ).as_expr() == 0

# Selected x=2 holonomy and its Galois mate.
q = sp.Rational(1, 2) + sp.sqrt(3)*sp.I/2
selected = {x: 2, z: 2 + q}
assert sp.simplify(P.subs(selected)) == 0
assert sp.simplify(kappa.subs(selected) - (1 + q)) == 0
assert sp.simplify(tau.subs(selected) - (2 - q)) == 0

# A point on the same irreducible Riley component refutes a global 3-kappa identity.
zg = (1 + sp.sqrt(5))/2
counterexample = {x: 0, z: zg}
assert sp.simplify(P.subs(counterexample)) == 0
assert sp.simplify((tau + kappa - 3).subs(counterexample)) == -4

print("Riley trace component: P =", P)
print("disc_z(P) =", disc_z)
print("kappa mod P =", mod_component(kappa))
print("tau + kappa - 3 mod P =", defect)
print("global deck map: z ->", sigma_z)
print("global deck conjugate of kappa =", sigma_kappa)
print("generic kappa polynomial =", kappa_minpoly)
print("parabolic specialization: x^2=4 gives kappa + tau = 3")
print("selected x=2 values: kappa=1+q, tau=2-q")
print("counterexample: x=0, z=(1+sqrt(5))/2 gives tau+kappa-3=-4")
print("VERDICT: GLOBAL SHEET CONJUGACY PROVED; CONSTANT 3-KAPPA IS PERIPHERAL ONLY")
