"""The web seat's card W-P1, the process reading (its branch at 3f4fccbcf): its [E] statements held on main.  Nothing of the
seat's is run (its wp1_iteration.py read as text).
 P1  gamma = [[2, 1], [1, 1]] exactly (sympy): trace, stretch factor and entropy; eigen-directions' slopes; |2 - tr gamma^n| for
     n = 1..8 and the fixed points of gamma^n on the torus F counted directly for n = 1..4; fixed points on the line; the axis's
     centre and radius; i and 1 + i on it; gamma(i); translation length 2 arccosh(3/2) = 2 log of the stretch.
 P2  the axis radius sqrt(t^2 - 4)/(2|c|) of L^n R = [[n + 1, n], [1, 1]] for n = 1..5 and 8; the golden thread's closed geodesic
     on the modular surface: the largest axis radius over the conjugates of gamma whose axes meet the standard domain.
 P3  the quotations of main's record it gives in its section 1.2, each found in main's files at 60ed90808."""
import subprocess, itertools
import sympy as sp
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
g = sp.Matrix([[2, 1], [1, 1]]); tr = g.trace(); lam = max(g.eigenvals(), key=lambda e: float(e))
vecs = {sp.nsimplify(ev): v[0] for ev, m, v in g.eigenvects()}
slopes = {sp.simplify(ev): sp.simplify(v[1] / v[0]) for ev, v in vecs.items()}
seq = [abs(2 - (g ** n).trace()) for n in range(1, 9)]
def torus_fixed(n):                                     # points of (R/Z)^2 fixed by g^n: solutions of (g^n - 1) x in Z^2, counted as |det|
    return abs((g ** n - sp.eye(2)).det())
z = sp.symbols("z"); fp = sp.solve(sp.Eq(z, (2 * z + 1) / (z + 1)), z); centre = (fp[0] + fp[1]) / 2; radius = sp.Abs(fp[0] - fp[1]) / 2
on = lambda w: sp.simplify(sp.Abs(w - centre) ** 2 - radius ** 2)
gi = sp.simplify((2 * sp.I + 1) / (sp.I + 1)); TL = 2 * sp.acosh(sp.Rational(3, 2))
print("P1: trace %s; stretch %s = %s; entropy %s; slopes %s; |2 - tr g^n|, n = 1..8: %s; |det(g^n - 1)| (torus fixed points), n = 1..4: %s; fixed points %s; centre %s, radius %s = %s; i and 1 + i on the axis: %s, %s; g(i) = %s; translation length %s = 2 log(stretch): %s"
      % (tr, lam, sp.N(lam, 12), sp.N(sp.log(lam), 6), slopes, seq, [torus_fixed(n) for n in range(1, 5)], fp, centre, radius, sp.N(radius, 6), on(sp.I) == 0, on(1 + sp.I) == 0, gi, sp.N(TL, 6), abs(sp.N(TL - 2 * sp.log(lam), 40)) < 1e-35))
rad = lambda M: sp.sqrt(M.trace() ** 2 - 4) / (2 * abs(M[1, 0]))
L, R = sp.Matrix([[1, 1], [0, 1]]), sp.Matrix([[1, 0], [1, 1]])
print("P2: axis radius of L^n R: %s" % {n: sp.N(rad(L ** n * R), 4) for n in (1, 2, 3, 4, 5, 8)})
best = 0                                               # conjugates h g h^-1 with |entries| <= 6 whose axis meets the domain |Re| <= 1/2, |z| >= 1
for a, b, c, d in itertools.product(range(-6, 7), repeat=4):
    if a * d - b * c != 1: continue
    h = sp.Matrix([[a, b], [c, d]]); k = h * g * h.inv()
    if k[1, 0] == 0: continue
    cen = sp.Rational(k[0, 0] - k[1, 1], 2 * k[1, 0]); r = rad(k)
    top = sp.sqrt(r ** 2) if abs(cen) <= sp.Rational(1, 2) else (sp.sqrt(r ** 2 - (abs(cen) - sp.Rational(1, 2)) ** 2) if r > abs(cen) - sp.Rational(1, 2) else 0)
    if top ** 2 >= 1 and float(top) > best: best = float(top)
print("P2: the highest point of the golden closed geodesic in the standard domain, over conjugates with entries up to 6: %.6f (sqrt 5/2 = %.6f)" % (best, float(sp.sqrt(5) / 2)))
AT = "60ed90808"
quotes = {"Nothing computed selects any direction": None, "leave tau free": None, "No clock studied here selects a point": None, "the democratic thread sum is flat": None, "is yet a weave result by minimization": None}
for q in quotes:
    out = git("grep", "-l", "-F", q, AT, "--", "frontier", "docs", "THE_WEAVE.md").split("\n")
    quotes[q] = sorted({x.split(":", 1)[1].split("/")[1] if x.count("/") >= 2 else x.split(":", 1)[-1] for x in out if x})[:4]
print("P3: the quotations of its section 1.2 found in main's files at %s: %s" % (AT, quotes))
