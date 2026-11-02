"""UNRUN controls, implemented after design commit e181282de.

Do not import, collect or execute without separate review and strict
prospective admission. No old P210 or physical-family approval applies.
Finite matrices do not certify global bundles, domains or quantum physics.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import unittest

import sympy as s


F = Fraction
ORDER = (5, 3, 6, 4, 7)  # Zero-based E8 coordinates: (6,4,7,5,8).
W = (0, 0, 0, -1, 1, -2, 0, 2)
QY = (F(5, 2),) * 3 + (F(-3, 2),) * 5
T3 = (F(1, 4),) * 8


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def coordinate(i):
    return tuple(F(int(i == j)) for j in range(8))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def subtract(a, b):
    return tuple(x-y for x, y in zip(a, b))


def e8_roots():
    roots = set()
    for i, j in combinations(range(8), 2):
        for a, b in product((-1, 1), repeat=2):
            row = [F(0)]*8
            row[i], row[j] = F(a), F(b)
            roots.add(tuple(row))
    for signs in product((-1, 1), repeat=8):
        if sum(value == -1 for value in signs) % 2 == 0:
            roots.add(tuple(F(value, 2) for value in signs))
    return roots


def d5_roots():
    roots = set()
    for i, j in combinations(range(3, 8), 2):
        for a, b in product((-1, 1), repeat=2):
            row = [F(0)]*8
            row[i], row[j] = F(a), F(b)
            roots.add(tuple(row))
    return roots


def four_roots():
    return (add(coordinate(3), coordinate(7)),
            add(coordinate(4), coordinate(6)),
            tuple(-x for x in add(coordinate(4), coordinate(5))),
            tuple(-x for x in add(coordinate(3), coordinate(6))))


def elementary(n, i, j):
    out = s.zeros(n)
    out[i, j] = 1
    return out


def skew(i, j):
    return elementary(5, i, j)-elementary(5, j, i)


def ten(a=None, b=None, c=None):
    a = s.zeros(5) if a is None else a
    b = s.zeros(5) if b is None else b
    c = s.zeros(5) if c is None else c
    return a.row_join(b).col_join(c.row_join(-a.T))


def dagger(a):
    return a.conjugate().T


def inner(a, b):
    return s.trace(dagger(a)*b)/2


def comm(a, b):
    return a*b-b*a


def root_cartan(root):
    if not all(root[i] == 0 for i in range(3)):
        raise ValueError("Cartan vector is outside the declared D5 subsystem")
    return ten(s.diag(*(s.Rational(root[i].numerator, root[i].denominator)
                        for i in ORDER)))


def root_matrix(root):
    row = [root[i] for i in ORDER]
    positive = [i for i, value in enumerate(row) if value == 1]
    negative = [i for i, value in enumerate(row) if value == -1]
    if len(positive) == len(negative) == 1:
        return ten(elementary(5, positive[0], negative[0]))
    if len(positive) == 2 and not negative:
        return ten(b=skew(*positive))
    if len(negative) == 2 and not positive:
        return ten(c=-skew(*negative))
    raise ValueError(root)


def matrices():
    h5 = s.diag(-4, -2, 0, 2, 4)
    e5 = s.zeros(5)
    for i in range(4):
        e5[i+1, i] = s.sqrt((i+1)*(4-i))
    j5 = s.zeros(5)
    for i in range(5):
        j5[i, 4-i] = (-1)**i
    bz = s.sqrt(s.Rational(2, 5))*skew(1, 4)-s.sqrt(s.Rational(3, 5))*skew(2, 3)
    hm, hp = ten(b=bz), ten(c=j5*bz*j5)
    return h5, e5, j5, ten(h5), ten(e5), hm, hp


def field_gram(q, r):
    return s.Matrix([[inner(q, q), inner(q, r)],
                     [inner(r, q), inner(r, r)]])


def normalized_fields(e, g):
    x, y = s.symbols("x y", real=True)
    normalization = s.sqrt(1+x*x+y*y)
    a, b = 1/normalization, (x+s.I*y)/normalization
    return x, y, a, b, a*e, b*g


def su_basis(n):
    out = []
    for i, j in combinations(range(n), 2):
        out += [elementary(n, i, j)+elementary(n, j, i),
                s.I*(elementary(n, i, j)-elementary(n, j, i))]
    out += [elementary(n, i, i)-elementary(n, i+1, i+1)
            for i in range(n-1)]
    return out


def neutral_response(matrix, higgs=None):
    if higgs is None:
        f = s.zeros(5, 1)
        f[4] = 1
    else:
        f = higgs
    # Fundamental and dual infinitesimal actions are both retained.
    return (matrix*f).col_join(-matrix.T*s.conjugate(f))


class ElectroweakBranchChecks(unittest.TestCase):
    def assert_zero(self, expression):
        entries = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
        self.assertTrue(all(s.simplify(x) == 0 for x in entries), str(expression))

    def test_actual_D5_roots_and_E8_embedding(self):
        full, sub = e8_roots(), d5_roots()
        self.assertEqual(len(full), 240)
        self.assertEqual(len(sub), 40)
        self.assertTrue(sub <= full)
        self.assertTrue(all(dot(r, r) == 2 for r in full))
        self.assertEqual({r for r in full if r[:3] == (0, 0, 0)}, sub)
        for a, b in product(sub, repeat=2):
            if add(a, b) in full:
                self.assertIn(add(a, b), sub)
        roots = four_roots()
        self.assertTrue(set(roots) <= sub)
        self.assertEqual([dot(W, r) for r in roots], [1]*4)
        self.assertEqual([dot(QY, r) for r in roots], [-3, -3, 3, 3])
        self.assertEqual([dot(T3, r) for r in roots], [F(1, 2)]*2+[F(-1, 2)]*2)
        self.assertTrue(all(dot(T3, r)+dot(QY, r)/6 == 0 for r in roots))
        differences = [subtract(a, b) for a, b in combinations(roots, 2)]
        self.assertEqual(Counter(dot(r, r) for r in differences), {4: 3, 6: 3})
        self.assertTrue(all(r not in full for r in differences))
        actual_first = subtract(coordinate(3), coordinate(5))
        wrong_first = subtract(coordinate(4), coordinate(3))
        self.assertEqual(dot(W, actual_first), 1)
        self.assertNotEqual(dot(W, wrong_first), 1)

    def test_compact_ten_matrix_metric_and_principal_triple(self):
        h5, e5, j5, h, e, hm, hp = matrices()
        form = s.zeros(5).row_join(s.eye(5)).col_join(s.eye(5).row_join(s.zeros(5)))
        f = dagger(e)
        self.assert_zero(comm(h, e)-2*e)
        self.assert_zero(comm(e, f)-h)
        self.assert_zero(comm(h, f)+2*f)
        self.assert_zero(dagger(h)-h)
        self.assert_zero(j5*j5-s.eye(5))
        self.assert_zero(j5*e5*j5+e5.T)
        self.assertEqual(inner(e, e), 20)
        self.assertEqual(inner(h, h), 40)
        for r in d5_roots():
            matrix = root_matrix(r)
            self.assert_zero(matrix.T*form+form*matrix)
            self.assertEqual(inner(matrix, matrix), 1)
            self.assert_zero(comm(matrix, dagger(matrix))-root_cartan(r))
            self.assert_zero(comm(h, matrix)-2*dot(W, r)*matrix)
        for matrix in (e, f, h, hm, hp):
            self.assert_zero(matrix.T*form+form*matrix)
        missing_partner = s.diag(e5, s.zeros(5))
        self.assertNotEqual(missing_partner.T*form+form*missing_partner, s.zeros(10))

    def test_highest_doublets_and_actual_involution(self):
        _, _, j5, h, e, hm, hp = matrices()
        k = s.diag(j5, j5)
        theta = lambda x: -k*x.T*k
        qy = ten(-s.Rational(3, 2)*s.eye(5))
        t3 = ten(s.Rational(1, 4)*s.eye(5))
        self.assertEqual(inner(hm, hm), 1)
        self.assertEqual(inner(hp, hp), 1)
        self.assert_zero(inner(hm, hp))
        for vector, charge in ((hm, -3), (hp, 3)):
            self.assert_zero(comm(h, vector)-2*vector)
            self.assert_zero(comm(e, vector))
            self.assert_zero(comm(qy, vector)-charge*vector)
            self.assert_zero(comm(t3+qy/6, vector))
            self.assert_zero(theta(theta(vector))-vector)
            self.assert_zero(theta(dagger(vector))-dagger(theta(vector)))
        self.assert_zero(theta(hm)-hp)
        self.assert_zero(theta(hp)-hm)
        for vector in (h, e, dagger(e)):
            self.assert_zero(theta(vector)-vector)
        for incomplete in (ten(b=skew(1, 4)), ten(b=skew(2, 3))):
            self.assertNotEqual(comm(e, incomplete), s.zeros(10))

    def test_moment_closure_in_roots_and_matrices(self):
        _, _, _, h, e, hm, hp = matrices()
        roots = four_roots()
        weights = (F(2, 5), F(3, 5), F(2, 5), F(3, 5))
        cartan = tuple(sum(c*r[i] for c, r in zip(weights, roots)) for i in range(8))
        self.assertEqual(cartan, tuple(F(value, 5) for value in W))
        self.assert_zero(root_cartan(cartan)-h/10)
        y0 = hm+hp
        self.assert_zero(comm(y0, dagger(y0))-h/10)
        self.assert_zero(comm(e, y0))
        components = (s.sqrt(s.Rational(2, 5))*ten(b=skew(1, 4)),
                      -s.sqrt(s.Rational(3, 5))*ten(b=skew(2, 3)),
                      s.sqrt(s.Rational(2, 5))*ten(c=skew(0, 3)),
                      -s.sqrt(s.Rational(3, 5))*ten(c=skew(1, 2)))
        self.assert_zero(sum(components, s.zeros(10))-y0)
        for vector, weight, root in zip(components, weights, roots):
            self.assert_zero(comm(vector, dagger(vector))-s.Rational(weight.numerator, weight.denominator)*root_cartan(root))
        for a, b in combinations(components, 2):
            self.assert_zero(comm(a, dagger(b)))
        qy = ten(-s.Rational(3, 2)*s.eye(5))
        one_moment = comm(hm, dagger(hm))
        self.assertEqual(inner(qy, one_moment), -3)
        self.assertNotEqual(one_moment, h/10)
        self.assert_zero(inner(qy, comm(y0, dagger(y0))))

    def test_second_triple_gram_and_independent_flavour_direction(self):
        _, _, _, h, e, hm, hp = matrices()
        g = s.sqrt(10)*(hm+hp)
        self.assert_zero(comm(g, dagger(g))-h)
        self.assert_zero(comm(h, g)-2*g)
        self.assert_zero(comm(e, g))
        self.assertEqual(inner(g, g), 20)
        self.assert_zero(inner(e, g))
        a, b = s.symbols("a b", real=True)
        q, r = a*e, b*g
        determinant = s.factor(field_gram(q, r).det())
        self.assert_zero(determinant-400*a*a*b*b)
        self.assert_zero(field_gram(a*e, b*e).det())
        u5 = s.diag(1, s.I, -1, -s.I, 1)
        unitary = s.diag(u5, u5.inv().T)
        self.assert_zero(dagger(unitary)*unitary-s.eye(10))
        form = s.zeros(5).row_join(s.eye(5)).col_join(s.eye(5).row_join(s.zeros(5)))
        self.assert_zero(unitary.T*form*unitary-form)
        self.assertEqual(unitary.det(), 1)
        self.assert_zero(field_gram(unitary*q*dagger(unitary),
                                   unitary*r*dagger(unitary))-field_gram(q, r))
        rotation = s.Matrix([[s.Rational(3, 5), 4*s.I/5],
                             [4*s.I/5, s.Rational(3, 5)]])
        self.assert_zero(dagger(rotation)*rotation-s.eye(2))
        self.assertEqual(rotation.det(), 1)
        qp, rp = rotation[0, 0]*q+rotation[0, 1]*r, rotation[1, 0]*q+rotation[1, 1]*r
        self.assert_zero(field_gram(qp, rp).det()-determinant)

    def test_complete_scaled_vacuum_and_backreaction_control(self):
        _, _, _, h, e, hm, hp = matrices()
        g = s.sqrt(10)*(hm+hp)
        _, _, a, b, q, r = normalized_fields(e, g)
        self.assert_zero(a*s.conjugate(a)+b*s.conjugate(b)-1)
        self.assert_zero(comm(h, q)-2*q)
        self.assert_zero(comm(h, r)-2*r)
        self.assert_zero(comm(q, r))
        self.assert_zero(comm(q, dagger(q))+comm(r, dagger(r))-h)
        qa, ra = s.Rational(3, 5)*e, 4*s.I*g/5
        self.assert_zero(comm(qa, dagger(qa))+comm(ra, dagger(ra))-h)
        wrong = comm(e, dagger(e))+comm(ra, dagger(ra))-h
        self.assert_zero(wrong-s.Rational(16, 25)*h)
        self.assertNotEqual(wrong, s.zeros(10))

    def test_radius_norm_balance_and_nonzero_domain_comparators(self):
        _, _, _, h, e, hm, hp = matrices()
        g = s.sqrt(10)*(hm+hp)
        x, y, a, b, q, r = normalized_fields(e, g)
        ell, coupling = s.symbols("ell coupling", positive=True)
        qhat, rhat = q/(2*ell), r/(2*ell)
        curvature = -h/(4*ell*ell)
        self.assert_zero(curvature+comm(qhat, dagger(qhat))+comm(rhat, dagger(rhat)))
        total = inner(qhat, qhat)+inner(rhat, rhat)
        self.assert_zero(total-5/ell**2)
        self.assert_zero(2*s.pi*ell**2*total/coupling**2-10*s.pi/coupling**2)
        determinant = s.simplify(field_gram(qhat, rhat).det())
        self.assert_zero(determinant-25*a*a*b*s.conjugate(b)/ell**4)
        self.assert_zero(determinant.subs({x: 0, y: 0}))
        self.assertEqual(determinant.subs({x: 1, y: 0, ell: 1}), s.Rational(25, 4))
        bad_rhat = r/(2*ell**2)
        wrong = curvature+comm(qhat, dagger(qhat))+comm(bad_rhat, dagger(bad_rhat))
        self.assertNotEqual(s.simplify(wrong.subs({x: 1, y: 0, ell: 2})), s.zeros(10))

    def test_actual_SM_neutral_stabilizer_and_three_broken_directions(self):
        color = [s.diag(matrix, s.zeros(2)) for matrix in su_basis(3)]
        weak = [s.diag(s.zeros(3), matrix) for matrix in su_basis(2)]
        qy = s.diag(-2, -2, -2, 3, 3)
        sm = color+weak+[qy]
        self.assertEqual(len(sm), 12)
        self.assertTrue(all(matrix == dagger(matrix) and s.trace(matrix) == 0 for matrix in sm))
        self.assertEqual(s.Matrix.hstack(*(s.Matrix(25, 1, list(m)) for m in sm)).rank(), 12)
        constraints = s.Matrix.hstack(*(neutral_response(matrix) for matrix in sm))
        self.assertEqual(constraints.rank(), 3)
        real_constraints = s.re(constraints).col_join(s.im(constraints))
        self.assertEqual(real_constraints.rank(), 3)
        self.assertEqual(12-constraints.rank(), 9)
        hermitian3 = su_basis(3)+[s.eye(3)]
        stabilizer = [s.diag(matrix, s.Matrix([[-s.trace(matrix)]]), s.zeros(1))
                      for matrix in hermitian3]
        self.assertEqual(len(stabilizer), 9)
        for matrix in stabilizer:
            self.assert_zero(neutral_response(matrix))
            self.assertEqual(s.trace(matrix), 0)
        self.assertEqual(s.Matrix.hstack(*(s.Matrix(25, 1, list(m)) for m in stabilizer)).rank(), 9)
        em = s.diag(s.Rational(-1, 3), s.Rational(-1, 3), s.Rational(-1, 3), 1, 0)
        self.assert_zero(neutral_response(em))
        raising, lowering = elementary(5, 3, 4), elementary(5, 4, 3)
        self.assert_zero(comm(em, raising)-raising)
        self.assert_zero(comm(em, lowering)+lowering)
        mass = s.Matrix(3, 3, lambda i, j:
                        s.re((dagger(neutral_response(weak[i]))*neutral_response(weak[j]))[0]))
        self.assert_zero(mass-2*s.eye(3))
        self.assertTrue(all(value > 0 for value in mass.eigenvals()))
        no_higgs = s.Matrix.hstack(*(neutral_response(matrix, s.zeros(5, 1))
                                    for matrix in sm))
        self.assertEqual(12-no_higgs.rank(), 12)


if __name__ == "__main__":
    raise SystemExit("UNRUN scientific controls: require separate review and strict prospective admission")
