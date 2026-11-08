"""Exact candidate cusp response formulas. Scientific source: UNRUN at implementation."""
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Mode:
    ell2: Fraction
    cut: Fraction
    nu: Fraction
    s: Fraction
    b_power: Fraction
    v_power: Fraction
    b_other: Fraction
    v_other: Fraction
    response_b: Fraction
    response_v: Fraction


def mode(nu, ell2=1, cut=1):
    nu, ell2, cut = map(Fraction, (nu, ell2, cut))
    if nu < 1 or ell2 <= 0 or cut <= 0:
        raise ValueError("Require Euclidean nu>=1 and positive ell^2,cut")
    return Mode(ell2, cut, nu, (nu*nu-1)/(4*ell2),
                -(1+nu)/2, (1-nu)/2, (nu-1)/2, (nu+1)/2,
                cut*(1+nu)/(2*ell2), (nu-1)/(2*cut))


def response_derivatives(item):
    """Derivatives with respect to s, keeping ell^2 and the cut fixed."""
    return item.cut/item.nu, item.ell2/(item.cut*item.nu)


def normalized_power_integral(power, cut, y_weight=0, coefficient=1):
    """Integral of coefficient*y^weight*(y/cut)^power over [cut,infinity)."""
    power, cut, coefficient = map(Fraction, (power, cut, coefficient))
    if not isinstance(y_weight, int) or cut <= 0:
        raise ValueError("Integral requires an integer weight and positive cut")
    total = power+y_weight+1
    if total >= 0:
        raise ValueError("Nonconvergent weighted power integral")
    return -coefficient*cut**(y_weight+1)/total


def cubic_factors(first, second, third):
    if any(x.ell2 != first.ell2 or x.cut != first.cut for x in (second, third)):
        raise ValueError("One common cusp geometry is required")
    total = first.nu+second.nu+third.nu-1
    return 2*first.cut/total, 2*first.ell2/(first.cut*total)


def static_shell(ell2, lower, upper):
    ell2, lower, upper = map(Fraction, (ell2, lower, upper))
    if ell2 <= 0 or not 0 < lower < upper:
        raise ValueError("Require positive geometry with lower<upper")
    conductance = lower*upper/(ell2*(upper-lower))
    return ((conductance, -conductance), (-conductance, conductance))
