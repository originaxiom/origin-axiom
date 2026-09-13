#!/usr/bin/env python3
"""Is the cusp shape QUADRATIC?  No LLL needed -- solve for the coefficients directly.

If tau^2 + b tau + c = 0 with b, c rational, then splitting into real and imaginary parts:
    Im: Im(tau^2) + b Im(tau) = 0      =>  b = -Im(tau^2)/Im(tau)
    Re: Re(tau^2) + b Re(tau) + c = 0  =>  c = -Re(tau^2) - b Re(tau)
so b and c are FORCED; the only question is whether they are rational.

Every quadratic field is abelian, so this is exactly the boundary where a Kronecker-Weber
CONDUCTOR -- and hence B1002's gcd -- can exist in the two instances B675 banks.
"""
from fractions import Fraction
import mpmath as mp
import snappy
mp.mp.dps = 60

def is_rat(x, maxden=10**6, tol=mp.mpf(10) ** -30):
    """Rational reconstruction AT FULL PRECISION.

    A first version did Fraction(float(x)).limit_denominator(...) and then compared against a
    1e-30 tolerance -- but float() truncates to ~1e-16, so no rational with a non-dyadic
    denominator (13/12, say) could EVER pass. The controls missed it because they used only
    0, 1, 4 and -1, all exactly representable: a control that does not vary the thing which
    can break is not a control.
    """
    if abs(x) < tol:
        return True, Fraction(0)
    rel = mp.pslq([x, mp.mpf(1)], tol=mp.mpf(10) ** -40, maxcoeff=10**8, maxsteps=10000)
    if not rel or rel[0] == 0:
        return False, None
    f = Fraction(-int(rel[1]), int(rel[0]))
    return (abs(mp.mpf(f.numerator) / f.denominator - x) < tol), f

# CONTROLS: the routine must accept known quadratics and reject a known cubic
def quad_test(tau):
    t2 = tau * tau
    if abs(mp.im(tau)) < mp.mpf(10) ** -30:
        return None
    b = -mp.im(t2) / mp.im(tau)
    c = -mp.re(t2) - b * mp.re(tau)
    okb, fb = is_rat(b); okc, fc = is_rat(c)
    return (okb and okc), fb, fc

print("  CONTROLS")
for nm, v, want in [("i", mp.mpc(0, 1), True), ("-2i", mp.mpc(0, -2), True),
                    ("(1+sqrt-3)/2", (1 + mp.sqrt(-3)) / 2, True),
                    ("2^(1/3)+i*0.7", mp.mpc(mp.mpf(2) ** (mp.mpf(1)/3), 0.7), False),
                    ("1+sqrt(-3)/6  <- the m=1 case, c = 13/12 non-dyadic",
                     1 + mp.sqrt(-3) / 6, True)]:
    r = quad_test(v)
    print(f"    {nm:>14}: quadratic={r[0]}  (expected {want})   x^2 + ({r[1]})x + ({r[2]})")

print()
print("=" * 84)
print("THE METALLIC FAMILY: is the cusp shape quadratic?")
print("=" * 84)
print(f"  {'m':>3} {'manifold':>10} {'volume':>10} {'cusp shape tau':>30} {'quadratic?':>11}")
for m in range(1, 9):
    try:
        # HIGH PRECISION: going through Python complex() truncates to ~1e-16, and then a
        # 1e-40 PSLQ can never find the relation -- the same float-before-exact-test bug
        # that has now bitten three times this session (E75's family).
        M = snappy.Manifold("b++" + "R" * m + "L" * m).high_precision()
        sh = M.cusp_info('shape')[0]
        tau = mp.mpmathify(mp.mpc(mp.mpf(str(sh.real()).replace(' ', '')), mp.mpf(str(sh.imag()).replace(' ', ''))))
        q, fb, fc = quad_test(tau)
        extra = f"  x^2 + ({fb})x + ({fc})" if q else ""
        print(f"  {m:>3} {M.name():>10} {float(M.volume()):>10.6f} {mp.nstr(tau,10):>30} {str(q):>11}{extra}")
    except Exception as e:
        print(f"  {m:>3}  FAILED {type(e).__name__}: {e}")
