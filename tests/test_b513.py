"""B513 locks — the boundary-type attractors (solid) + the signature tombstone (kappa-independence)."""
import mpmath as mp
import sympy as sp


def test_pointer_commutator_order4():
    mp.mp.dps = 25
    z0 = mp.mpf(1); ze = (z0 + mp.sqrt(mp.mpc(z0*z0 - 4)))/2
    A = mp.matrix([[1, -1], [1, 0]]); B = mp.matrix([[0, ze], [-1/ze, 1]])
    C = A*B*A**-1*B**-1
    assert abs(C[0, 0] + C[1, 1]) < 1e-18            # tr[A,B] = 0 (pointer, kappa=0)
    assert abs((C**4)[0, 0] - 1) < 1e-18             # [A,B]^4 = I, order 4 exact


def test_signature_not_kappa_controlled():
    # the tombstone: det(Hessian of kappa) factors through x^2+y^2+z^2+xyz-4, NOT kappa
    x, y, z = sp.symbols('x y z')
    kap = x**2 + y**2 + z**2 - x*y*z - 2
    detH = sp.factor(sp.hessian(kap, (x, y, z)).det())
    assert detH == -2*(x**2 + x*y*z + y**2 + z**2 - 4)
    # this surface != kappa-level-set (differs by sign of xyz), so signature cuts across kappa-shells
