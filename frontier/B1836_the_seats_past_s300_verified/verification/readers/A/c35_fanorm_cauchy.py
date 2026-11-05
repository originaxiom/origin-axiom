"""S301-A check c35 (value-free; symbolic).  B1832 sec. 1.5 (T-FA-NORM): v.v = X^n + Y^n - (X+Y)^n, X = theta_2^4, Y = theta_4^4
(Jacobi: X + Y = theta_3^4), XY(X+Y) = 16 eta^12, E_4 = X^2 + XY + Y^2.  B1832 left 'E_4 divides for n = 5 mod 6, E_4^2 for
n = 1 mod 6' as numerical.  Claim checked: it is Cauchy's classical divisibility of (X+Y)^n - X^n - Y^n -- by XY(X+Y) iff n odd,
by X^2+XY+Y^2 iff n = +-1 mod 6, by (X^2+XY+Y^2)^2 iff n = 1 mod 6 (n > 1) -- so the census's odd n make h.h a multiple of
eta^12 for every census direction, in closed form."""
import sympy as sp
X, Y = sp.symbols("X Y")
E4 = X ** 2 + X * Y + Y ** 2
bad = []
for n in range(2, 41):
    p = sp.expand(X ** n + Y ** n - (X + Y) ** n)
    by_xy = sp.Poly(p, X, Y).as_expr().subs(X, 0) == 0
    by_xpy = sp.expand(p.subs(Y, -X)) == 0
    q1 = sp.div(sp.Poly(p, X), sp.Poly(E4, X))[1].is_zero
    q2 = sp.div(sp.Poly(p, X), sp.Poly(sp.expand(E4 ** 2), X))[1].is_zero
    exp = (by_xy, by_xpy == (n % 2 == 1), q1 == (n % 6 in (1, 5)), q2 == (n % 6 == 1))
    if not all(exp):
        bad.append((n, by_xy, by_xpy, q1, q2))
print("c35: n = 2..40: XY | p always; (X+Y) | p iff n odd; E4 | p iff n = +-1 mod 6; E4^2 | p iff n = 1 mod 6 ->", "ALL HOLD" if not bad else bad)
for n in (3, 5):
    print("   n = %d: p = %s" % (n, sp.factor(X ** n + Y ** n - (X + Y) ** n)))
