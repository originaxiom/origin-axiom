"""Exact safeguards for the modular-base Chern calculation; no physical index."""
import sympy as sp

COUNT = 0


def eq(a, b):
    global COUNT
    assert sp.simplify(sp.expand(a - b)) == 0, (a, b)
    COUNT += 1


def check(condition):
    global COUNT
    assert bool(condition)
    COUNT += 1


def main():
    x = sp.Symbol("x", real=True)
    y, g, ell, Y = sp.symbols("y g ell Y", positive=True)
    k, n, s, k0 = sp.symbols("k n s k0", real=True)
    I, pi = sp.I, sp.pi

    def curvature(phi):
        return sp.simplify(I * (sp.diff(phi, x, 2) + sp.diff(phi, y, 2)) / 2)

    phi = k * sp.log(y)
    Fxy = curvature(phi)
    eq(Fxy, -I * k / (2 * y**2))
    Ax, Ay = -I * sp.diff(phi, y) / 2, I * sp.diff(phi, x) / 2
    eq(sp.diff(Ay, x) - sp.diff(Ax, y), Fxy)
    eq(curvature(sp.Integer(0)), 0)
    eq(curvature(x**2 - y**2), 0)  # real part of a holomorphic quadratic
    check(curvature(y**2) != 0)
    check(sp.diff(curvature(y**2) * y**2, y) != 0)  # local non-YM control

    # Direct fibre Hodge norm, using w=u+z*v.
    z, zbar = x + I*y, x - I*y
    eq(I * (zbar - z) / 2, y)

    # Mobius imaginary part, det=1. d!=0 chart plus S separately.
    b, c = sp.symbols("b c", real=True)
    d = sp.Symbol("d", real=True, nonzero=True)
    a = (1 + b*c) / d
    mob = (a*z + b) / (c*z + d)
    Q = (c*x + d)**2 + c**2*y**2
    eq((mob-sp.conjugate(mob))/(2*I), y/Q)
    smob = -1/z
    eq((smob-sp.conjugate(smob))/(2*I), y/(x*x+y*y))
    for weight in (-24, -12, 0, 12, 24):
        eq((y/Q)**weight * Q**weight, y**weight)

    # Check exact stabilizer characters with algebraic roots, not float phases.
    sixth = (1 + I*sp.sqrt(3))/2
    for weight in range(-36, 37):
        trivial = sp.simplify(I**weight - 1) == 0 and sp.simplify(sixth**weight - 1) == 0
        check(trivial == (weight % 12 == 0))

    vertical_integral = sp.integrate(y**-2, (y, sp.sqrt(1-x*x), sp.oo))
    eq(vertical_integral, 1/sp.sqrt(1-x*x))
    area = sp.integrate(1/sp.sqrt(1-x*x), (x, -sp.Rational(1,2), sp.Rational(1,2)))
    eq(area, pi/3)
    Funit = sp.simplify(Fxy.subs(k, 12*n) * y*y)
    eq(I * Funit * area / (2*pi), n)
    energy = sp.simplify(sp.conjugate(Funit)*Funit*area/(2*g*g))
    eq(energy, 6*pi*n*n/(g*g))
    eq(sp.diff(Funit, x), 0)
    eq(sp.diff(Funit, y), 0)
    eq(energy.subs(n, 0), 0)
    check(energy.subs(n, 1).is_positive)
    eq(energy.subs(n, -1), energy.subs(n, 1))

    # Fixed-flux square identity is algebraic; its integral cross term is zero.
    f, mean = sp.symbols("f mean", real=True)
    eq(f*f, (f-mean)**2 + 2*mean*(f-mean) + mean*mean)
    eq((2*pi*n/area)**2 * area/(2*g*g), energy)
    eq((6*n/ell**2)**2 * (ell**2*area)/(2*g*g), energy/ell**2)
    eq((6*n/ell**2)*(ell**2*area)/(2*pi), n)

    # HDelta supplies a harmonic term. Leading term and harmonic controls
    # verify the local differential calculation, not Delta's modularity.
    phis = 12*s*sp.log(y) - 4*pi*s*y
    Fs = curvature(phis)
    eq(Fs, -6*I*s/y**2)
    eq(curvature(phis + s*(x*x-y*y)), Fs)
    top_Ax = -I*sp.diff(phis, y)/2
    top_integral = -sp.integrate(top_Ax.subs(y, Y), (x, -sp.Rational(1,2), sp.Rational(1,2)))
    truncated_flux = I * (-6*I*s) * (area-1/Y)/(2*pi)
    eq(I*top_integral/(2*pi), truncated_flux)
    eq(sp.limit(truncated_flux, Y, sp.oo), s)
    for mult in (1, 2, 4):
        eq(I*(-6*I*n)*(area/mult)/(2*pi), n/mult)

    # A scalar norm identity suffices componentwise for a vector-valued form.
    delta_abs, numerator_abs = sp.symbols("delta_abs numerator_abs", positive=True)
    for integer_n in (-2, -1, 0, 1, 2):
        lhs = (numerator_abs/delta_abs**integer_n)**2 * y**k0 * y**(12*integer_n) * delta_abs**(2*integer_n)
        rhs = numerator_abs**2 * y**(k0+12*integer_n)
        eq(lhs, rhs)
    for lam in (sp.Rational(1,8), sp.Rational(3,8), sp.Rational(7,8)):
        for power in (-2, 0, 12, 24):
            # log-density divided by y separates exponential from polynomial.
            eq(sp.limit((-4*pi*lam*y + power*sp.log(y))/y, y, sp.oo), -4*pi*lam)
            eq(sp.limit((-4*pi*(lam-1)*y + power*sp.log(y))/y, y, sp.oo), 4*pi*(1-lam))

    print(f"PASS: {COUNT} exact safeguards")
    print("Base: effective PSL(2,Z) modular orbifold, real dimension two")
    print("F=-6*i*n*dA; flux=n; E=6*pi*n**2/g**2")
    print("HDelta identification conditional; no unit selection or physical index certified")


if __name__ == "__main__":
    main()
