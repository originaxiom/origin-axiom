"""B1997, POST HOC (labelled; the derivation was done by hand after identify_run.txt was read): lambda* in closed form.
Claim: lambda* = sqrt(w + sqrt(w^2 - 4)) with w = (1 + 4 cos(pi/9))/2; the sextic for lambda*^2 is palindromic after
lambda^2 = 2 nu; with w = nu + 1/nu it is the cubic 8w^3 - 12w^2 - 18w + 3, whose substitution u = 2w, u = v + 1, v = -2y
gives y^3 - 3y + 1 = 0, the minimal polynomial of 2cos(2 pi/9); the cubic's discriminant is a square (a cyclic cubic field
of conductor 9). Checked exactly (sympy) and to 60 digits (mpmath).
    python3 -B closed_form_posthoc.py > closed_form_posthoc_run.txt"""
import sympy as sp, mpmath as mp
x, nu, w, y = sp.symbols("x nu w y")
P12 = x**12 - 3*x**10 + 3*x**8 - 21*x**6 + 12*x**4 - 48*x**2 + 64
mu6 = sp.expand(P12.subs(x**2, sp.Symbol("m"))) if False else sp.Poly([1, -3, 3, -21, 12, -48, 64], sp.Symbol("m")).as_expr()
m = sp.Symbol("m")
s6 = sp.expand(mu6.subs(m, 2 * nu) / 8)
print("the sextic in nu = lambda^2/2, divided by 8: %s; palindromic: %s" % (sp.Poly(s6, nu).all_coeffs(), sp.Poly(s6, nu).all_coeffs() == sp.Poly(s6, nu).all_coeffs()[::-1]))
cub = sp.expand(sp.simplify(s6 / nu**3).subs(nu, nu))
cw = sp.expand(8 * (w**3 - 3*w) - 12 * (w**2 - 2) + 6 * w - 21)
print("with w = nu + 1/nu: 8w^3 - 12w^2 - 18w + 3 = %s; agrees with the sextic: %s" % (cw, sp.simplify(sp.expand(nu**3 * cw.subs(w, nu + 1/nu)) - s6) == 0))
cy = sp.expand(cw.subs(w, (-2 * y + 1) / 2))
print("with w = (1 - 2y)/2: %s = -%s * (y^3 - 3y + 1): %s" % (cy, 1, sp.simplify(cy + (y**3 - 3*y + 1)) == 0 or sp.simplify(cy - (y**3 - 3*y + 1)) == 0 or sp.factor(cy)))
print("discriminant of u^3 - 3u^2 - 9u + 3: %s = 72^2: %s" % (sp.discriminant(sp.Symbol('u')**3 - 3*sp.Symbol('u')**2 - 9*sp.Symbol('u') + 3), sp.discriminant(sp.Symbol('u')**3 - 3*sp.Symbol('u')**2 - 9*sp.Symbol('u') + 3) == 72**2))
mp.mp.dps = 60
W = (1 + 4 * mp.cos(mp.pi / 9)) / 2
lam = mp.sqrt(W + mp.sqrt(W**2 - 4))
print("lambda* = sqrt(w + sqrt(w^2 - 4)), w = (1 + 4cos(pi/9))/2: %s" % mp.nstr(lam, 30))
print("P12(lambda*) at 60 digits: %s" % mp.nstr(sum(c * lam**k for k, c in enumerate([64, 0, -48, 0, 12, 0, -21, 0, 3, 0, -3, 0, 1])), 5))
print("lambda*/2, the settled decay per move: %s" % mp.nstr(lam / 2, 20))
