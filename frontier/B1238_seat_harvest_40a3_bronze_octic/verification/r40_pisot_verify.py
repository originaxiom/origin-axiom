"""fc R40 / B516: 'among the metallic means only golden gives a Pisot number under x -> x(1+sqrt x)'.
Exact: x_m = (m+sqrt(m^2+4))/2 has minpoly x^2 - m x - 1; beta_m = x_m (1 + sqrt x_m) lies in
Q(sqrt(x_m)) (degree 4 over Q): with s = sqrt(x_m), s^4 - m s^2 - 1 = 0 and beta = s^2 + s^3.
Minimal polynomial of beta = resultant_s(s^4 - m s^2 - 1, x - s^2 - s^3); Pisot iff beta > 1 real and
all other conjugates have |.| < 1. Roots from sympy at 50 digits."""
import sympy as sp
s, x = sp.symbols('s x')
for m in (1, 2, 3, 4, 5):
    P = sp.resultant(s**4 - m*s**2 - 1, x - s**2 - s**3, s); P = sp.Poly(sp.factor(P), x)
    facs = sp.factor_list(P.as_expr())[1]
    xm = (m + sp.sqrt(m*m+4))/2; beta = xm*(1+sp.sqrt(xm)); bv = sp.N(beta, 50)
    # the factor beta actually satisfies
    F = [f for f, e in facs if abs(sp.N(f.subs(x, beta), 60)) < 1e-40][0]
    roots = sp.Poly(F, x).nroots(n=40)
    others = sorted(abs(r) for r in roots if abs(r - bv) > 1e-20)
    pisot = all(o < 1 for o in others) and F == sp.Poly(F, x).as_expr() and sp.Poly(F,x).is_monic
    print(f"m={m}: beta={sp.N(beta,9)} minpoly={F} deg={sp.degree(F,x)} monic={sp.Poly(F,x).is_monic} | other |conj| = {[float(sp.N(o,6)) for o in others]} | PISOT: {pisot}")
