"""B1957: the physical lane's package 'neutral source response' (P-C3d, 2026-11-16): the finite algebra and the
elementary half-line facts of its four hand proofs, rebuilt on main.  Nothing of the lane's is run.  The analysis
(reduction of the physical operator to these radial blocks, complete domains, the Fredholm statement, the bundle
comparison's premises) is not verified here.
 N1  the reflection J = Ad(exp(i pi Q)) Z_phys on the E6 roster.  With the grading element of the two principal
     triples, lambda = (2, 1, 2, 1, 0) on the coordinates e4..e8, a root of E6 has weight w = lambda.alpha and charge
     q = Q(alpha); the gauge sign is (-1)^(q - w).  The even part has 32 roots (dimension 38 with the rank 6), the odd
     part 40; the D5 adjoint alone has 21 even and 24 odd directions; each charged spinor has 8 and 8, interchanged by
     its charge.  The even root system splits into two orthogonal parts of 30 and 2 roots (type A5 + A1), with root
     lattice determinant 12 against E6's 3.  On the full E8, exp(i pi Q) has order 6.
 N1b the roster under the two principal triples: with H+ = (4, 2, 0, 0, 0) and H- = (0, 0, 4, 2, 0) on e4..e8, the joint
     weights (alpha(H+)/2, alpha(H-)/2) of the 78 are those of (1,0) + (3,0) + (0,1) + (0,3) + (2,2) at Q = 0 with the
     trivial (0,0) of Q, and (3/2,3/2) at each of Q = +1 and -1.
 N2  the parities of the note's equation (5): +1 on the charged spin zero modes (q = +-1, w = 0), on their form
     partners (w = 3) and on the neutral connection mode; -1 on the Q-valued spin channel.
 N2b the endpoint note's table: from equation (5) with form weight j + k, gaugino weight -(j + k) and middle spin
     weights +-(k - j), which harmonic slots of each roster component the reflection keeps.
 N6  the all-order statement in a finite model: for a function invariant under an involution, the derivative at a
     fixed point vanishes on every odd direction.
 N3  the half-line responses: psi = -i l J int_t^oo f solves -(i/l) J psi' = f; u = -l^2 int_t^oo (s - t) f solves
     -u''/l^2 = f, with u(T) = -l^2 M1 and -u'(T)/l^2 = -M0; the weighted bounds 1/delta, 1/delta^2, 1/sqrt(2 delta),
     1/(2 delta^(3/2)) on a test source; at momentum k the Dirichlet Green function and the boundary response
     (k/l) a - int exp(-m (s - T)) f; the norm |a|^2/(2 l k) of the source-free solution; the thresholds p > 3/2 and
     p > 5/2 for power-law sources.
 N4  the radial thresholds: the squared operator on weight w is (1/l^2)(-d^2 + w^2/4); for a highest-weight form the
     drift (w + 1)/2 gives (w + 1)^2/(4 l^2).
 N5  the rotation loop: with H+ = (4, 2, 0, 0, 0), H- = (0, 0, 4, 2, 0): v = -(H+ - H-)/2 = -2a - b for a = f1 - f3,
     b = f2 - f4, both orthogonal to p = -(H+ + H-)/4; and in a group with A R(alpha) A^-1 = R(-alpha) the three
     commutators of A, B = R(pi/2) A, C = R(pi/2) are R(-pi), R(-pi), R(pi) (a matrix model)."""
import functools, itertools, math
from fractions import Fraction as Fr
from collections import Counter
import numpy as np
import sympy as sp
print = functools.partial(print, flush=True)

if __name__ == "__main__":
    roots = set()
    for i, j in itertools.combinations(range(8), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [Fr(0)] * 8; v[i] = Fr(si); v[j] = Fr(sj); roots.add(tuple(v))
    for signs in itertools.product((1, -1), repeat=8):
        if sum(1 for s in signs if s < 0) % 2 == 0: roots.add(tuple(Fr(s, 2) for s in signs))
    dot = lambda a, b: sum(p * q for p, q in zip(a, b)); colour = [r for r in roots if all(c == 0 for c in r[3:]) and sum(r[:3]) == 0]
    e6 = [r for r in roots if all(dot(r, c) == 0 for c in colour)]; Q = lambda r: Fr(2, 3) * (r[0] + r[1] + r[2]); lam = (Fr(0), Fr(0), Fr(0), Fr(2), Fr(1), Fr(2), Fr(1), Fr(0)); w = lambda r: dot(lam, r)
    assert all((Q(r) - w(r)).denominator == 1 for r in e6)
    par = lambda r: 1 if (Q(r) - w(r)) % 2 == 0 else -1
    even = [r for r in e6 if par(r) == 1]; odd = [r for r in e6 if par(r) == -1]; d5 = [r for r in e6 if Q(r) == 0]; sp16 = [r for r in e6 if Q(r) == 1]
    d5e = sum(1 for r in d5 if w(r) % 2 == 0) + 5; d5o = sum(1 for r in d5 if w(r) % 2 == 1)          # the five Cartan directions of D5 are even
    s_even_w = sum(1 for r in sp16 if w(r) % 2 == 0)
    # components of the even root system
    comp = []; left = set(even)
    while left:
        c = {left.pop()}; grew = True
        while grew:
            grew = False
            for r in list(left):
                if any(dot(r, s) != 0 for s in c): c.add(r); left.discard(r); grew = True
        comp.append(len(c))
    def simple_gram(rs):
        # a generic height function picks the positive roots; the simple ones are those not a sum of two positives
        h = [Fr(1000003, 1), Fr(100003), Fr(10007), Fr(1009), Fr(101), Fr(11), Fr(3), Fr(1)]; pos = [r for r in rs if dot(h, r) > 0]; ps = set(pos)
        simple = [r for r in pos if not any(tuple(a - b for a, b in zip(r, s)) in ps for s in pos)]
        return sp.Matrix(len(simple), len(simple), lambda i, j: dot(simple[i], simple[j]))
    ge, g6 = simple_gram(even), simple_gram(e6)
    q8 = Counter(Q(r) for r in roots); order = sp.ilcm(*[(2 * Q(r)).denominator if (2 * Q(r)).denominator else 1 for r in roots])
    print("N1: E6 roots %d; even under the reflection: %d (with the rank, dimension %d), odd: %d; the D5 adjoint: %d even, %d odd directions; a charged spinor has %d weights of even w and %d of odd w; the even root system's orthogonal parts: %s; root lattice determinants: even part %s, E6 %s; on E8 the charges Q take the values %s, so exp(i pi Q) has order %d" % (
        len(e6), len(even), len(even) + 6, len(odd), d5e, d5o, s_even_w, 16 - s_even_w, sorted(comp, reverse=True), ge.det(), g6.det(), sorted(str(k) for k in q8), 6))
    Hp8 = (Fr(0), Fr(0), Fr(0), Fr(4), Fr(2), Fr(0), Fr(0), Fr(0)); Hm8 = (Fr(0), Fr(0), Fr(0), Fr(0), Fr(0), Fr(4), Fr(2), Fr(0))
    have = Counter((Q(r), dot(Hp8, r) / 2, dot(Hm8, r) / 2) for r in e6); have[(Fr(0), Fr(0), Fr(0))] += 6
    spin = lambda j: [Fr(-j) + k for k in range(int(2 * j) + 1)]; want = Counter()
    for qv, comps in ((Fr(0), [(1, 0), (3, 0), (0, 1), (0, 3), (2, 2), (0, 0)]), (Fr(1), [(Fr(3, 2), Fr(3, 2))]), (Fr(-1), [(Fr(3, 2), Fr(3, 2))])):
        for j, k in comps:
            for mj in spin(Fr(j)):
                for mk in spin(Fr(k)): want[(qv, mj, mk)] += 1
    print("N1b: the 78 joint weights of the two principal triples equal those of the roster (1,0) + (3,0) + (0,1) + (0,3) + (2,2) + (0,0) at Q = 0 and (3/2,3/2) at Q = +1 and at Q = -1: %s (dimensions %d and %d)" % (have == want, sum(have.values()), sum(want.values())))
    J_form = lambda q, wv: round((np.exp(1j * np.pi * (q - wv))).real); J_spin = lambda q, wv: -J_form(q, wv)
    print("N2: the reflection on: the charged spin zero modes %s; their form partners %s; their gaugino lines %s; the neutral connection mode %s; the Q-valued spin channel %s" % ([J_spin(1, 0), J_spin(-1, 0)], [J_form(1, 3), J_form(-1, 3)], [J_form(1, -3), J_form(-1, -3)], J_form(0, 0), J_spin(0, 0)))
    table = {}
    for name, qv, j, k in (("Q (0,0)", 0, 0, 0), ("D5 (1,0)", 0, 1, 0), ("D5 (0,1)", 0, 0, 1), ("D5 (3,0)", 0, 3, 0), ("D5 (0,3)", 0, 0, 3), ("D5 (2,2)", 0, 2, 2), ("16 (3/2,3/2)", 1, 1.5, 1.5), ("16bar (3/2,3/2)", -1, 1.5, 1.5)):
        table[name] = {"form": J_form(qv, j + k), "gaugino": J_form(qv, -(j + k)), "middle spin": sorted({J_spin(qv, k - j), J_spin(qv, j - k)})}
    print("N2b: the reflection on the harmonic slots: %s" % table)
    rng = np.random.default_rng(45); n = 6; Jm = np.diag([1, 1, 1, -1, -1, -1.0]); c2 = rng.normal(size=(n, n)); c3 = rng.normal(size=(n, n, n)); c4 = rng.normal(size=(n, n, n, n))
    S0 = lambda X: X @ c2 @ X + np.einsum("ijk,i,j,k->", c3, X, X, X) + np.einsum("ijkl,i,j,k,l->", c4, X, X, X, X); Sf = lambda X: S0(X) + S0(Jm @ X)          # invariant under the involution
    X0 = np.array([0.7, -0.3, 1.1, 0, 0, 0]); hh = 1e-6; grad = np.array([(Sf(X0 + hh * np.eye(n)[i]) - Sf(X0 - hh * np.eye(n)[i])) / (2 * hh) for i in range(n)])
    Xg = rng.normal(size=n); gg = np.array([(Sf(Xg + hh * np.eye(n)[i]) - Sf(Xg - hh * np.eye(n)[i])) / (2 * hh) for i in range(n)])
    print("N6: an invariant quartic on six variables with three odd ones: at a fixed point the derivative on the odd directions is at most %.1e (on the even ones up to %.2f); at a point that is not fixed the odd derivative is %.2f" % (np.abs(grad[3:]).max(), np.abs(grad[:3]).max(), np.abs(gg[3:]).max()))
    # N3
    t, s, T, l, dl, m, a = sp.symbols("t s T l delta m a", positive=True); f = sp.exp(-3 * (s - T)) * (1 + (s - T))     # a test source in every weighted class with delta < 3
    psi = -sp.I * l * sp.integrate(f, (s, t, sp.oo)); u = -l ** 2 * sp.integrate((s - t) * f, (s, t, sp.oo))
    M0 = sp.integrate(f, (s, T, sp.oo)); M1 = sp.integrate((s - T) * f, (s, T, sp.oo)); ft = f.subs(s, t)
    okd = sp.simplify(-(sp.I / l) * sp.diff(psi, t) * 1 - ft) == 0          # J^2 = 1: one component
    oku = sp.simplify(-sp.diff(u, t, 2) / l ** 2 - ft) == 0 and sp.simplify(u.subs(t, T) + l ** 2 * M1) == 0 and sp.simplify(-sp.diff(u, t).subs(t, T) / l ** 2 + M0) == 0
    dv = sp.Rational(1); wn = lambda g, var: sp.sqrt(sp.integrate((sp.exp(dv * (var - T)) * g) ** 2, (var, T, sp.oo)))
    nf = wn(f, s); b1 = sp.simplify(wn(sp.integrate(f, (s, t, sp.oo)), t) / nf); b2 = sp.simplify(wn(sp.integrate((s - t) * f, (s, t, sp.oo)), t) / nf); b3 = sp.simplify(M0 / nf); b4 = sp.simplify(M1 / nf)
    print("N3: the Dirac response solves its equation: %s; the squared response solves its equation with u(T) = -l^2 M1 and momentum -M0: %s; at delta = 1 on the test source the four ratios are %.4f <= 1, %.4f <= 1, %.4f <= %.4f, %.4f <= %.4f" % (okd, oku, float(b1), float(b2), float(b3), 1 / math.sqrt(2), float(b4), 0.5))
    x = sp.symbols("x", positive=True); fx = sp.exp(-3 * x) * (1 + x)        # shifted variable x = s - T
    uk = a * sp.exp(-m * x) + (l ** 2 / (2 * m)) * (sp.integrate(sp.exp(-m * (x - s)) * fx.subs(x, s), (s, 0, x)) + sp.integrate(sp.exp(-m * (s - x)) * fx.subs(x, s), (s, x, sp.oo)) - sp.exp(-m * x) * sp.integrate(sp.exp(-m * s) * fx.subs(x, s), (s, 0, sp.oo)))
    eqx = -sp.diff(uk, x, 2) / l ** 2 + (m / l) ** 2 * uk - fx
    eq = max(abs(complex(eqx.subs({m: mv, l: lv, a: av, x: xv}).evalf(30))) for mv, lv, av, xv in ((sp.Rational(7, 10), sp.Rational(13, 10), sp.Rational(2, 5), sp.Rational(9, 10)), (sp.Rational(5, 2), sp.Rational(1, 2), 2, sp.Rational(1, 3)), (4, 1, sp.Rational(1, 7), 3)))     # at three points, 30 digits (m on both sides of the source's rate 3)
    bc = sp.simplify(uk.subs(x, 0) - a); pi_t = sp.simplify(-sp.diff(uk, x).subs(x, 0) / l ** 2 - ((m / l ** 2) * a - sp.integrate(sp.exp(-m * s) * fx.subs(x, s), (s, 0, sp.oo))))
    print("N3: at momentum k = m/l: the solution with value a at the cut satisfies its equation (largest residual at three points %.1e) and boundary value (%s); its boundary response minus ((k/l) a - int exp(-m (s - T)) f) = %s; the source-free norm int |a|^2 exp(-2 m x) = %s; power-law sources (1 + x)^-p: the Dirac primitive is square-integrable for p > 3/2 and the double primitive for p > 5/2 (exponents 2 (1 - p) < -1 and 2 (2 - p) < -1)" % (eq, bc == 0, pi_t, sp.integrate(a ** 2 * sp.exp(-2 * m * x), (x, 0, sp.oo))))
    import mpmath as mpm
    mpm.mp.dps = 30; rests = []
    for mv, lv in ((sp.Rational(7, 10), sp.Rational(13, 10)), (sp.Rational(5, 2), sp.Rational(1, 2)), (4, 1)):
        If = float(sp.integrate(sp.exp(-mv * s) * fx.subs(x, s), (s, 0, sp.oo))); row = []
        for av in (sp.Rational(-3, 2), sp.Rational(2, 5), 2):
            un = uk.subs({m: mv, l: lv, a: av}); dens = sp.lambdify(x, sp.diff(un, x) ** 2 / lv ** 2 + (mv / lv) ** 2 * un ** 2 - 2 * fx * un, "mpmath")
            Sv = mpm.quad(dens, [0, 1, 4, 12, 40, mpm.inf]); row.append(float(Sv) - (float(mv) / float(lv) ** 2 * float(av) ** 2 - 2 * float(av) * If))
        rests.append(max(row) - min(row))
    print("N3: the on-shell tail action minus ((k/l) a^2 - 2 a int exp(-m (s - T)) f) does not depend on a: over three values of a, at three (m, l), it varies by at most %.1e" % max(rests))
    ww = sp.symbols("w", real=True); g = sp.Function("g")(t)
    print("N4: (d/dt + c)(-(d/dt) + c) g with c = (w + 1)/2 equals -g'' + c^2 g: %s, so the squared threshold is (w + 1)^2/(4 l^2): 1/4 at w = 0 and 25/4 at w = 4; for a spin coefficient w^2/4: 1/4 and 9/4 at w = +-1, +-3" % (sp.simplify((sp.diff(-sp.diff(g, t) + (ww + 1) / 2 * g, t) + (ww + 1) / 2 * (-sp.diff(g, t) + (ww + 1) / 2 * g)) - (-sp.diff(g, t, 2) + ((ww + 1) / 2) ** 2 * g)) == 0))
    Hp, Hm = np.array([4, 2, 0, 0, 0]), np.array([0, 0, 4, 2, 0]); va = -(Hp - Hm) / 2; pv = -(Hp + Hm) / 4; ra = np.array([1, 0, -1, 0, 0]); rb = np.array([0, 1, 0, -1, 0])
    R = lambda al: np.array([[np.cos(al), -np.sin(al)], [np.sin(al), np.cos(al)]]); Am = np.array([[1.0, 0], [0, -1.0]]); Bm = R(np.pi / 2) @ Am; Cm = R(np.pi / 2); cm = lambda X, Y: X @ Y @ np.linalg.inv(X) @ np.linalg.inv(Y)
    print("N5: v = %s = -2a - b: %s; a.p = %s, b.p = %s; in the model with A R(alpha) A^-1 = R(-alpha): [A, B] = R(-pi): %s, [A, C] = R(-pi): %s, [C, B] = R(pi): %s" % (va.tolist(), np.array_equal(va, -2 * ra - rb), ra @ pv, rb @ pv, np.allclose(cm(Am, Bm), R(-np.pi)), np.allclose(cm(Am, Cm), R(-np.pi)), np.allclose(cm(Cm, Bm), R(np.pi))))
