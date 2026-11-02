"""UNRUN finite controls, implemented after design commit b061fd9a9.

No import, collection or execution without independent review and strict
prospective admission. Finite matrices do not certify global Hodge pairings,
closed range, stationary variation or the actual infinite-dimensional gap.
"""

from fractions import Fraction
from itertools import combinations, product
import unittest

import sympy as s


F = Fraction
SPINS = tuple(product((F(0), F(1, 2)), repeat=2))
ZERO = (F(0), F(0))
CHI = (F(1, 3), F(0))
EM = (F(2, 3),)*3+(F(0),)*5


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def comm(a, b):
    return a*b-b*a


def dagger(a):
    return a.conjugate().T


def skew(i, j):
    out = s.zeros(5)
    out[i, j], out[j, i] = 1, -1
    return out


def ten(a=None, b=None, c=None):
    a = s.zeros(5) if a is None else a
    b = s.zeros(5) if b is None else b
    c = s.zeros(5) if c is None else c
    return a.row_join(b).col_join(c.row_join(-a.T))


def source_matrices():
    """Literal source defining-five basis, transported to the faithful ten."""
    e5, j5 = s.zeros(5), s.zeros(5)
    for i in range(4):
        e5[i+1, i] = s.sqrt((i+1)*(4-i))
    for i in range(5):
        j5[i, 4-i] = (-1)**i
    bz = s.sqrt(s.Rational(2, 5))*skew(1, 4)-s.sqrt(s.Rational(3, 5))*skew(2, 3)
    return (ten(e5), s.sqrt(10)*ten(b=bz, c=j5*bz*j5),
            ten(s.diag(-4, -2, 0, 2, 4)))


def e8_roots():
    out = set()
    for i, j in combinations(range(8), 2):
        for a, b in product((-1, 1), repeat=2):
            row = [F(0)]*8
            row[i], row[j] = F(a), F(b)
            out.add(tuple(row))
    for signs in product((-1, 1), repeat=8):
        if sum(x == -1 for x in signs) % 2 == 0:
            out.add(tuple(F(x, 2) for x in signs))
    return out


def pole(a):
    return a//2 if a <= 0 else (a+1)//2-1


def h0(a, eta, line):
    degree = pole(a)
    if degree < 0:
        return 0
    if degree > 0:
        return degree
    return int(all((a*eta[i]+line[i]) % 1 == 0 for i in range(2)))


def h1(a, eta, line):
    # Source's ACTUAL Hermitian Hodge dual, not ordinary compact RR.
    return h0(2-a, eta, tuple(-x for x in line))


class NeutralUpLiftChecks(unittest.TestCase):
    def assert_zero(self, expression):
        if isinstance(expression, s.MatrixBase):
            self.assertEqual(expression.applyfunc(s.simplify), s.zeros(*expression.shape))
        else:
            self.assertEqual(s.simplify(expression), 0)

    def test_actual_neutral_generator_and_full_residual_compatibility(self):
        roots = e8_roots()
        self.assertEqual(len(roots), 240)
        d5 = {r for r in roots if not any(r[:3])}
        cross = {r for r in roots if sum(x != 0 for x in r[:3]) == 1
                 and sum(x != 0 for x in r[3:]) == 1
                 and all(x.denominator == 1 for x in r)}
        self.assertEqual(len(d5), 40)
        self.assertEqual(len(cross), 60)
        self.assertEqual({dot(EM, r) for r in d5}, {F(0)})
        self.assertEqual({dot(EM, r) for r in cross}, {F(-2, 3), F(2, 3)})
        self.assertEqual(dot(EM, EM), F(4, 3))

        e, g, h = source_matrices()
        self.assert_zero(comm(e, dagger(e))-h)
        self.assert_zero(comm(g, dagger(g))-h)
        self.assert_zero(comm(e, g))
        self.assert_zero(comm(h, e)-2*e)
        self.assert_zero(comm(h, g)-2*g)
        eps = s.symbols('eps', real=True)
        a, b, c, d, psi = s.symbols('a b c d psi', complex=True)
        # On one actual up coefficient Z acts by q_EM times I_10.
        # This is a charged block of the adjoint, not a defining E8 matrix.
        for charge in (s.Rational(2, 3), -s.Rational(2, 3)):
            z = charge*s.eye(10)
            for x in (e, g, dagger(e), dagger(g)):
                self.assert_zero(comm(z, x))
            q, r = a*e+eps*c*psi*z, b*g+eps*d*psi*z
            self.assert_zero(comm(q, r))
            self.assert_zero(comm(q, dagger(q))+comm(r, dagger(r))
                             -(a*s.conjugate(a)+b*s.conjugate(b))*h)
            # Check all four mixed background/neutral adjoint terms
            # separately; moment cancellation alone could hide a bug.
            for old, new in ((a*e, c*psi*z), (b*g, d*psi*z)):
                self.assert_zero(comm(old, dagger(new)))
                self.assert_zero(comm(new, dagger(old)))
                self.assert_zero(comm(new, dagger(new)))
        # A Cartan that charges the principal raising fields is rejected.
        self.assertNotEqual(comm(h, e), s.zeros(10))
        self.assertNotEqual(comm(h, g), s.zeros(10))
        self.assertNotEqual(comm(e+h, g), s.zeros(10))

    def test_spin_pole_and_dual_multiplication_data(self):
        self.assertEqual([pole(i) for i in range(-4, 6)],
                         [-2, -2, -1, -1, 0, 0, 0, 1, 1, 2])
        section_spins = []
        for eta in SPINS:
            if h0(1, eta, ZERO):
                section_spins.append(eta)
            for sign in (-1, 1):
                line = tuple(sign*x for x in CHI)
                self.assertEqual(h0(3, eta, line), 1)
                self.assertEqual(h0(4, eta, line), 1)
                self.assertEqual(h1(-2, eta, line), 1)
                self.assertEqual(h1(-1, eta, line), 1)
                self.assertEqual(h0(-2, eta, line), 0)
                self.assertEqual(h1(4, eta, line), 0)
                # Equal dimensions at nontrivial eta do NOT supply psi.
                if eta != ZERO:
                    self.assertEqual(h0(1, eta, ZERO), 0)
        self.assertEqual(section_spins, [ZERO])
        self.assertNotEqual(len(section_spins), len(SPINS))
        # Wrong equality-endpoint b(4)=0 would lose the nontrivial-line
        # target; degree zero has a section iff that full flat line is O.
        wrong_target = int(all(x % 1 == 0 for x in CHI))
        self.assertEqual(wrong_target, 0)
        self.assertNotEqual(wrong_target, h0(4, ZERO, CHI))

    def test_first_order_physical_mass_blocks_and_exceptional_planes(self):
        a, b = s.symbols('a b', nonzero=True, real=True)
        c, d = s.symbols('c d', complex=True)
        change = s.Matrix([[1/a, 1/b], [1/a, -1/b]])/2
        old = s.Matrix([[a, a], [b, -b]])
        self.assert_zero(change*old-s.eye(2))
        self.assert_zero(change.det()+1/(2*a*b))
        shifted = change*s.Matrix([c, d])
        minus = s.det(s.Matrix([[a, c], [b, d]]))
        plus = s.det(s.Matrix([[a, c], [-b, d]]))
        self.assert_zero(-2*a*b*shifted[1]-minus)
        self.assert_zero(2*a*b*shifted[0]-plus)
        self.assert_zero(minus-(a*d-b*c))
        self.assert_zero(plus-(a*d+b*c))
        # Do not assume unrelated positive physical overlaps are equal.
        i1, i2, j1, j2 = s.symbols('i1 i2 j1 j2', positive=True)
        charge = s.Rational(2, 3)
        left = charge*minus*s.Matrix([[0, i1], [i2, 0]])
        right = charge*plus*s.Matrix([[0, j1], [j2, 0]])
        full = s.diag(left, right)
        self.assert_zero(full.det()-charge**4*i1*i2*j1*j2*minus**2*plus**2)
        sample = {a: s.Rational(3, 5), b: s.Rational(4, 5), c: 0, d: 1,
                  i1: 1, i2: 2, j1: 3, j2: 4}
        self.assertEqual(full.subs(sample).rank(), 4)
        for exceptional in (b*c/a, -b*c/a):
            self.assert_zero(full.det().subs(d, exceptional))
        for sign in (-1, 1):
            values = dict(sample)
            values.update({c: 1, d: sign*s.Rational(4, 3)})
            self.assertEqual(full.subs(values).rank(), 2)
        zero_neutral = dict(sample)
        zero_neutral.update({c: 0, d: 0})
        self.assertEqual(full.subs(zero_neutral).rank(), 0)
        norm_left, norm_right = s.diag(2, 3, 4, 5), s.diag(7, 8, 9, 10)
        normalized = norm_left*full*norm_right
        self.assert_zero(normalized.det()-norm_left.det()*norm_right.det()*full.det())

    def test_full_complement_schur_and_unbounded_inverse_controls(self):
        eps = s.symbols('eps', real=True)
        a = s.diag(1, 2, 3, 4)
        c = s.diag(2, 3)
        d = s.Matrix([[1, 1], [1, -1]])
        x = s.Matrix([[1, 0], [0, 1], [1, 1], [2, -1]])
        y = x.T
        heavy = c+eps*d
        full = (eps*a).row_join(eps*x).col_join((eps*y).row_join(heavy))
        schur = eps*a-eps**2*x*heavy.inv()*y
        elim_l = s.eye(4).row_join(-eps*x*heavy.inv()).col_join(
            s.zeros(2, 4).row_join(s.eye(2)))
        elim_r = s.eye(4).row_join(s.zeros(4, 2)).col_join(
            (-eps*heavy.inv()*y).row_join(s.eye(2)))
        self.assert_zero(elim_l*full*elim_r-s.diag(schur, heavy))
        self.assert_zero(schur.diff(eps).subs(eps, 0)-a)
        self.assert_zero(schur.diff(eps, 2).subs(eps, 0)/2+x*c.inv()*y)
        self.assertNotEqual(x*c.inv()*y, s.zeros(4))
        for value in (s.Rational(1, 100), -s.Rational(1, 100), s.Rational(1, 50)):
            self.assertEqual(heavy.subs(eps, value).rank(), 2)
            self.assertEqual(schur.subs(eps, value).rank(), 4)
            self.assertEqual(full.subs(eps, value).rank(), 6)
        # Independent countercontrol: singular leading rank is NOT an
        # all-orders no-mass result when the massive response is retained.
        singular = s.diag(1, 1, 1, 0)
        tail = s.Matrix([0, 0, 0, 1])
        lifted = (eps*singular).row_join(eps*tail).col_join(
            (eps*tail.T).row_join(s.ones(1)))
        self.assertEqual(singular.rank(), 3)
        self.assert_zero(lifted.det()+eps**5)
        self.assertEqual(lifted.subs(eps, s.Rational(1, 100)).rank(), 5)
        n = s.symbols('n', positive=True, integer=True)
        decay = 1/n
        self.assertEqual(s.limit(decay, n, s.oo), 0)
        self.assertEqual(s.limit(1/decay, n, s.oo), s.oo)
        self.assert_zero(decay*(1/decay)-1)
        # This comparator proves neither a physical cusp estimate nor a
        # uniform inverse for the infinite-dimensional charged complement.
