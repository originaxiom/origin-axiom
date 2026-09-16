#!/usr/bin/env python3
"""xB003 ADDENDUM 4 - the founding-cluster audit: where the genesis probes stand relative to
the point the object actually occupies.  Every cell asserts its own mathematics."""
import sympy as sp
x, m, t, tau = sp.symbols('x m t tau')
w = sp.Rational(-1, 2) + sp.sqrt(-3)/2

def b67_is_one_substitution_away():
    """B67 built the T^2 fixed locus and kappa on it.  kappa = -2 gives the object's point."""
    kap = (x**4 - 3*x**3 + x**2 + 4*x - 2)/(x-1)**2          # B67, verbatim
    num = sp.factor(sp.numer(sp.together(sp.simplify(kap + 2))))
    assert sp.simplify(num - x**2*(x**2 - 3*x + 3)) == 0, num
    roots = sp.solve(sp.Eq(x**2 - 3*x + 3, 0), x)
    assert any(sp.simplify(r - (2 + w)) == 0 for r in roots)
    assert any(sp.simplify(r - (2 + sp.conjugate(w))) == 0 for r in roots)
    disc = sp.discriminant(x**2 - 3*x + 3, x)
    assert disc == -3, disc
    print(f"B67  kappa(x) = -2  ->  x^2(x^2 - 3x + 3) = 0  ->  x = 2+omega, 2+conj(omega)")
    print(f"     minimal polynomial x^2 - 3x + 3, discriminant {disc} = the object's trace-field disc")
    print("     B67 had the locus and kappa; it never took this substitution (target was A(M,L)).")

def the_point_is_the_complete_structure():
    """B67's own meridian-longitude identity, at kappa = -2, gives the parabolic meridian."""
    sols = sp.solve(sp.Eq(m**4 - 5*m**2 + 2, -2), m)          # B67: kappa = tr(t)^4 - 5 tr(t)^2 + 2
    assert set(sols) == {-2, -1, 1, 2}, sols
    print(f"B67  kappa = m^4 - 5m^2 + 2 at kappa = -2  ->  m = {sorted(sols, key=lambda s: float(s))}")
    print("     m = +-2 is the PARABOLIC meridian: the fixed point IS the complete hyperbolic structure.")

def b13_is_on_the_other_leaf():
    I = 1**2 + 1**2 + 1**2 - 2*1*1*1 - 1                       # half-trace invariant at (1,1,1)
    assert I == 0 and 4*I + 2 == 2
    print("B13  its point (1,1,1) has I = 0, kappa = +2 -- B1341's leaf, B1342's 'nothing' leaf.")

def b6_sits_on_the_boundary():
    """B6/P15/P16's potential has its stationary points at the MOBIUS fixed points of A,
    which are real, i.e. on the boundary of H -- A is hyperbolic, so it fixes no point of H."""
    A = sp.Matrix([[2, 1], [1, 1]])
    fx = sp.solve(sp.Eq((A[0,0]*tau + A[0,1])/(A[1,0]*tau + A[1,1]), tau), tau)
    assert all(sp.im(r) == 0 for r in fx), fx
    phi = (1 + sp.sqrt(5))/2
    assert any(sp.simplify(r - phi) == 0 for r in fx)
    assert sp.simplify(sp.expand((tau**2 - tau - 1) - sp.prod([tau - r for r in fx]))) == 0
    assert abs(A.trace()) > 2
    print(f"B6   V'(tau) = kappa(tau^2 - tau - 1); its roots {[sp.nsimplify(r) for r in fx]} are the")
    print("     MOBIUS fixed points of A. |tr A| = 3 > 2, so A is hyperbolic and fixes NO point of H:")
    print("     both are REAL, on the boundary. B6 itself lists 'tau as a field rather than a")
    print("     coordinate on H' as an INSERTED choice; B7/B8/B9 build on that vacuum.")

if __name__ == "__main__":
    b67_is_one_substitution_away(); print()
    the_point_is_the_complete_structure(); print()
    b13_is_on_the_other_leaf(); print()
    b6_sits_on_the_boundary()
    print("\nVERIFIED")
