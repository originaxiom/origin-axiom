"""B1957: the physical lane's reply on the hypotheses H1 and H3 of B1959 for its own gauge operator (M10_H1_H3_SOURCE_REPLY.md
at 6f074b770; a hand argument, nothing run by the lane).  What main can decide by computation (data-free; nothing run or
imported from the lane).
 Q1  the cusp: for g = ell^2 (dx^2 + dy^2)/y^2 the orthonormal frame's connection form is -dx/y, of curvature -1/ell^2.
 Q2  H1's form: with D_x = d_x + i w/(2y) and D_y = d_y, the operator -(y^2/ell^2)(D_x^2 + D_y^2) + m^2 on e^(i nu x) f(log y)
     is ell^-2 [-f'' + f' + (nu e^t + w/2)^2 f] + m^2 f, the lane's (1) and B1959's channel with mu = m^2.
 Q3  the cancellation it states: with [H, E] = 2E and A_spin = s H/2, i s E - i [A_spin, E] = 0.
 Q4  the lane's roster of the adjoint of E6 under two commuting principal su(2)s, rebuilt by main from one construction that
     yields it (the principal su(2)s of so(5) + so(5) in so(10) in E6; that this is the lane's pair is main's reading): the
     spins, the dimensions, and the number of trivial summands (the kernel of its M_g).
 Q5  the inequality behind its (3): 2ab <= a^2/2 + 2 b^2."""
import itertools
from fractions import Fraction as Fr
import sympy as sp
x, y, ell, nu, w, m, t = sp.symbols("x y ell nu w m t", positive=True); f = sp.Function("f")
om = -1 / y                                                    # the connection form is om dx
curv = sp.diff(-om, y)                                          # d(om dx) = -d_y(om) dx ^ dy
coef = -sp.diff(om, y)                                         # d(om dx) = d_y(om) dy ^ dx = -d_y(om) dx ^ dy
print("Q1: d(-dx/y) = (%s) dx ^ dy; the area form is (ell^2/y^2) dx ^ dy, so the curvature is %s" % (sp.simplify(coef), sp.simplify(coef / (ell ** 2 / y ** 2))))
u = sp.exp(sp.I * nu * x) * f(sp.log(y)); Dx = lambda v: sp.diff(v, x) + sp.I * w / (2 * y) * v
P = -(y ** 2 / ell ** 2) * (Dx(Dx(u)) + sp.diff(u, y, 2)) + m ** 2 * u
got = sp.simplify((P / sp.exp(sp.I * nu * x)).subs(y, sp.exp(t)).doit())
want = (-sp.diff(f(t), t, 2) + sp.diff(f(t), t) + (nu * sp.exp(t) + w / 2) ** 2 * f(t)) / ell ** 2 + m ** 2 * f(t)
g = sp.Function("g"); test = sp.exp(-sp.Rational(3, 7) * t) * sp.cos(2 * t) + t ** 3
P2 = -(y ** 2 / ell ** 2) * (Dx(Dx(sp.exp(sp.I * nu * x) * test.subs(t, sp.log(y)))) + sp.diff(sp.exp(sp.I * nu * x) * test.subs(t, sp.log(y)), y, 2)) + m ** 2 * sp.exp(sp.I * nu * x) * test.subs(t, sp.log(y))
w2 = (-sp.diff(test, t, 2) + sp.diff(test, t) + (nu * sp.exp(t) + w / 2) ** 2 * test) / ell ** 2 + m ** 2 * test
print("Q2: on a test profile the operator with A_x = -w/(2y) gives the lane's channel (1): residual %s; with the sign of the drift reversed the residual is %s" % (sp.simplify((P2 / sp.exp(sp.I * nu * x)).subs(y, sp.exp(t)) - w2), sp.simplify(sp.simplify((P2 / sp.exp(sp.I * nu * x)).subs(y, sp.exp(t)) - w2.subs(w, -w)))))
s = sp.Symbol("s"); H = sp.Matrix([[1, 0], [0, -1]]); E = sp.Matrix([[0, 1], [0, 0]]); A = s * H / 2
print("Q3: [H, E] = 2E: %s; i s E - i [s H/2, E] = %s" % ((H * E - E * H) == 2 * E, (sp.I * s * E - sp.I * (A * E - E * A)).tolist()))
# Q4: weights.  so(5) = B2: roots +-e1, +-e2, +-e1+-e2; the principal grading is <rho_dual, .> with rho_dual = (2, 1) (simple roots e1 - e2 and e2 have height 1)
rho = (Fr(2), Fr(1)); gr = lambda v: sum(a * b for a, b in zip(rho, v))
adj = [(0, 0), (0, 0)] + [(a, 0) for a in (1, -1)] + [(0, a) for a in (1, -1)] + [(a, b) for a in (1, -1) for b in (1, -1)]
vec = [(0, 0)] + [(a, 0) for a in (1, -1)] + [(0, a) for a in (1, -1)]; spn = [(Fr(a, 2), Fr(b, 2)) for a in (1, -1) for b in (1, -1)]
def spins(grades):
    c = {}; out = []
    for g_ in grades: c[g_] = c.get(g_, 0) + 1
    while c:
        j = max(c); out.append(j)
        for k in range(int(2 * j) + 1):
            c[j - k] -= 1
            if c[j - k] == 0: del c[j - k]
    return sorted(out)
sa, sv, ss = spins([gr(v) for v in adj]), spins([gr(v) for v in vec]), spins([gr(v) for v in spn])
def tensor(j1, j2): return (j1, j2)
roster = [(Fr(0), Fr(0))] + [(j, Fr(0)) for j in sa] + [(Fr(0), j) for j in sa] + [(a, b) for a in sv for b in sv] + 2 * [(a, b) for a in ss for b in ss]
dims = [int((2 * a + 1) * (2 * b + 1)) for a, b in roster]
print("Q4: under the principal su(2) of so(5): the adjoint 10 has spins %s, the vector 5 spins %s, the spinor 4 spins %s; E6 = u(1) + so(10) + 16 + 16bar with so(10) = (10,1) + (1,10) + (5,5) and 16 = (4,4) gives the roster %s of dimensions %s, sum %d, with %d trivial summand(s)"
      % ([str(j) for j in sa], [str(j) for j in sv], [str(j) for j in ss], [(str(a), str(b)) for a, b in roster], dims, sum(dims), sum(1 for a, b in roster if a == 0 and b == 0)))
a_, b_ = sp.symbols("a b", real=True); print("Q5: a^2/2 + 2 b^2 - 2ab = %s, a square: so the tested identity gives the lane's (3)" % sp.factor(a_ ** 2 / 2 + 2 * b_ ** 2 - 2 * a_ * b_))
