"""UNRUN finite controls, implemented after design commit 76941fbf4.

No import, collection or execution without independent review and strict
prospective admission. These finite controls do not prove the weighted
global domains, Hodge multiplication maps or physical pole masses.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
import unittest

import sympy as s


F = Fraction
ZERO = (F(0), F(0))
CHI = (F(1, 3), F(0))
EM = (F(2, 3),)*3+(F(0),)*5
QY = (F(5, 2),)*3+(F(-3, 2),)*5


def clean(matrix):
    return matrix.applyfunc(s.cancel)


def raising_chain(n, t, ell):
    """n is the dimension 2j+1, with the source's normalized c_i."""
    if n < 1:
        raise ValueError('A raising chain has positive dimension')
    out = t*s.eye(n)
    pivots = []
    for i in range(n-1):
        c = s.sqrt((i+1)*(n-1-i))/(2*ell)
        out[i+1, i] = c
        pivots.append(c)
    return out, tuple(pivots)


def eliminate_raising_pivots(original, t):
    """Return D=L M R, L,R and their explicitly accumulated inverses.

    Only old subdiagonal entries are pivots. The source coordinate map
    is R^-1; the target map is L. No inverse of t may enter.
    """
    n = original.rows
    if original.cols != n or n == 0:
        raise ValueError('Expected a nonempty square raising chain')
    out = s.Matrix(original)
    left, right, left_inv, right_inv = (s.eye(n) for _ in range(4))
    for col in range(n-1):
        row = col+1
        pivot = s.cancel(out[row, col])
        if pivot == 0 or pivot.has(t):
            raise ValueError('Only a nonzero shift-independent raising pivot is admitted')
        for other in range(n):
            if other == row:
                continue
            coefficient = s.cancel(out[other, col]/pivot)
            if coefficient != 0:
                op, inv = s.eye(n), s.eye(n)
                op[other, row], inv[other, row] = -coefficient, coefficient
                out, left = clean(op*out), clean(op*left)
                left_inv = clean(left_inv*inv)
        for other in range(n):
            if other == col:
                continue
            coefficient = s.cancel(out[row, other]/pivot)
            if coefficient != 0:
                op, inv = s.eye(n), s.eye(n)
                op[col, other], inv[col, other] = -coefficient, coefficient
                out, right = clean(out*op), clean(right*op)
                right_inv = clean(inv*right_inv)
    # Pivot targets come first; the old lowest target is retained last.
    perm = s.zeros(n)
    for i in range(n-1):
        perm[i, i+1] = 1
    perm[n-1, 0] = 1
    return (clean(perm*out), clean(perm*left), right,
            clean(left_inv*perm.T), right_inv)


def koszul(a, b):
    return a.col_join(b), (-b).row_join(a)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


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
    a = F(a)
    if a.denominator != 1:
        raise ValueError('Only total integral S powers are admitted')
    a = int(a)
    return a//2 if a <= 0 else (a+1)//2-1


def h0(a, line):
    """Source endpoint law at the declared TRIVIAL extending spin."""
    degree = pole(a)
    if degree < 0:
        return 0
    if degree > 0:
        return degree
    return int(all(x % 1 == 0 for x in line))


def h1(a, line):
    return h0(2-a, tuple(-x for x in line))


def pair_dimensions(a, b, line):
    return h0(a, line), h0(b, line), h1(a, line), h1(b, line)


def pair_cohomology(dims, rank0, rank1):
    """LES accounting, conditional on the declared ACTUAL map ranks.

    This does not infer a global multiplication rank from dimensions.
    """
    a0, b0, a1, b1 = dims
    if not (0 <= rank0 <= min(a0, b0) and 0 <= rank1 <= min(a1, b1)):
        raise ValueError('Rank is incompatible with its source and target')
    return a0-rank0, b0-rank0+a1-rank1, b1-rank1


def neutral_count(j, k, line=ZERO):
    return h0(j+k+2, tuple(-x for x in line))+h0(1+j-k, line)+h0(1-j+k, line)


def coefficient_populations(roots):
    """Literal roots bind the inherited coefficient and flat-line labels."""
    d5, a3 = set(), set()
    cross, halves = defaultdict(set), defaultdict(set)
    for root in roots:
        if all(abs(x) == F(1, 2) for x in root):
            halves[root[:3]].add(root)
        elif not any(root[:3]):
            d5.add(root)
        elif not any(root[3:]):
            a3.add(root)
        else:
            cross[root[:3]].add(root)
    return d5, a3, dict(cross), dict(halves)


def charged_counts(kplus, kminus):
    up = 2*int(kminus == 0)+2*int(kplus == 0)
    down_dims = pair_dimensions(-3, 1, CHI)
    down = pair_cohomology(down_dims, 0, 0)[1]
    if kplus == 0 and kminus == 0:
        lepton = h1(-3, ZERO)+2*h0(1, ZERO)
    else:
        # Rank1 is the analytically proved dual nonzero injection, not
        # an extra fitted texture or an inference from equal dimensions.
        first = pair_cohomology(pair_dimensions(-3, 1, ZERO), 0, 1)
        second = pair_cohomology(pair_dimensions(1, 5, ZERO), 1, 0)
        lepton = first[1]+second[0]
    return up, down, lepton


class NeutralFullKernelChecks(unittest.TestCase):
    def assert_zero(self, expression):
        if isinstance(expression, s.MatrixBase):
            self.assertEqual(expression.applyfunc(s.simplify), s.zeros(*expression.shape))
        else:
            self.assertEqual(s.simplify(expression), 0)

    def test_shifted_Jordan_elimination_without_scalar_inverse(self):
        t = s.symbols('t')
        ell = s.symbols('ell', positive=True)
        for n in (1, 3, 4, 5, 7):
            original, pivots = raising_chain(n, t, ell)
            reduced, left, right, left_inv, right_inv = eliminate_raising_pivots(original, t)
            retained = (-1)**(n-1)*t**n/s.prod(pivots)
            expected = s.diag(*pivots, retained)
            self.assert_zero(reduced-expected)
            self.assert_zero(left*original*right-expected)
            self.assert_zero(left*left_inv-s.eye(n))
            self.assert_zero(left_inv*left-s.eye(n))
            self.assert_zero(right*right_inv-s.eye(n))
            self.assert_zero(right_inv*right-s.eye(n))
            self.assert_zero(s.prod(pivots)-s.factorial(n-1)/(2*ell)**(n-1))
            for matrix in (left, right, left_inv, right_inv):
                for entry in matrix:
                    self.assertFalse(s.denom(s.cancel(entry)).has(t))
                    s.Poly(entry, t)  # rejects non-polynomial hidden t inverses
            self.assert_zero(original.det()-t**n)
            self.assertEqual(original.subs(t, 0).rank(), n-1)
            self.assertEqual(original.subs({t: 1, ell: 1}).rank(), n)
            self.assert_zero(reduced.subs(t, 0)-s.diag(*pivots, 0))
        # A scalar-shift inverse would fail this polynomial criterion.
        with self.assertRaises(s.PolynomialError):
            s.Poly(1/t, t)

    def test_tensor_reduction_total_spin_and_Koszul_signs(self):
        x, y = s.symbols('x y')
        for n, m in ((5, 1), (1, 5), (4, 4)):
            ma, _ = raising_chain(n, x, s.Integer(1))
            mb, _ = raising_chain(m, y, s.Integer(1))
            da, la, ra, lai, rai = eliminate_raising_pivots(ma, x)
            db, lb, rb, lbi, rbi = eliminate_raising_pivots(mb, y)
            a, b = s.kronecker_product(ma, s.eye(m)), s.kronecker_product(s.eye(n), mb)
            d0, d1 = koszul(a, b)
            self.assert_zero(d1*d0)
            self.assertNotEqual(clean(b.row_join(a)*d0), s.zeros(n*m))
            g0 = s.kronecker_product(rai, rbi)
            g0i = s.kronecker_product(ra, rb)
            g1 = s.diag(s.kronecker_product(la, rbi), s.kronecker_product(rai, lb))
            g1i = s.diag(s.kronecker_product(lai, rb), s.kronecker_product(ra, lbi))
            g2 = s.kronecker_product(la, lb)
            ar, br = s.kronecker_product(da, s.eye(m)), s.kronecker_product(s.eye(n), db)
            r0, r1 = koszul(ar, br)
            self.assert_zero(g0*g0i-s.eye(n*m))
            self.assert_zero(g1*g1i-s.eye(2*n*m))
            self.assert_zero(g1*d0*g0i-r0)
            self.assert_zero(g2*d1*g1i-r1)
            corner = n*m-1
            fa, fb = da[n-1, n-1], db[m-1, m-1]
            self.assert_zero(r0.extract([corner, n*m+corner], [corner])-s.Matrix([fa, fb]))
            self.assert_zero(r1.extract([corner], [corner, n*m+corner])-s.Matrix([[-fb, fa]]))
            self.assertEqual(s.degree(fa, x), n)
            self.assertEqual(s.degree(fb, y), m)
            j, k = F(n-1, 2), F(m-1, 2)
            powers = (-j-k, 1+j-k, 1-j+k, 2+j+k)
            self.assertTrue(all(v.denominator == 1 for v in powers))
            self.assertEqual(powers[1]-powers[0], n)
            self.assertEqual(powers[2]-powers[0], m)
            self.assertEqual(powers[3]-powers[2], n)
            self.assertEqual(powers[3]-powers[1], m)
            weights = product((F(2*i-n+1, 2) for i in range(n)),
                              (F(2*i-m+1, 2) for i in range(m)))
            self.assertTrue(all((a+b).denominator == 1 for a, b in weights))
            # Every other scalar Koszul summand has a fixed pivot unit.
            for i, j_index in product(range(n), range(m)):
                if (i, j_index) != (n-1, m-1):
                    aa, bb = da[i, i].subs(x, 0), db[j_index, j_index].subs(y, 0)
                    self.assertTrue(aa != 0 or bb != 0)
                    z0, z1 = koszul(s.Matrix([[aa]]), s.Matrix([[bb]]))
                    self.assertEqual((1-z0.rank(), 2-z0.rank()-z1.rank(), 1-z1.rank()), (0, 0, 0))
        # Two different up companions are required before any total count.
        self.assertNotEqual(Counter(((5, 1), (1, 5))), Counter(((5, 1),)))
        p, q = s.symbols('p q')
        change = s.Matrix([[1, 1], [0, 1]])
        old0, old1 = s.Matrix([p, q]), s.Matrix([[-q, p]])
        new0 = change*old0
        new1 = change.det()*old1*change.inv()
        self.assert_zero(new1-s.Matrix([[-new0[1], new0[0]]]))
        # A determinant-changing example checks that degree2 must travel.
        change = s.diag(2, 3)
        self.assert_zero(change.det()*old1*change.inv()-s.Matrix([[-3*q, 2*p]]))

    def test_pole_duality_and_long_exact_sequence_rank_accounting(self):
        self.assertEqual([pole(i) for i in range(-4, 7)], [-2, -2, -1, -1, 0, 0, 0, 1, 1, 2, 2])
        for sign in (-1, 1):
            line = tuple(sign*x for x in CHI)
            self.assertEqual(pair_dimensions(-2, 3, line), (0, 1, 1, 0))
            self.assertEqual(pair_dimensions(-1, 4, line), (0, 1, 1, 0))
            self.assertEqual(pair_cohomology(pair_dimensions(-2, 3, line), 0, 0), (0, 2, 0))
            self.assertEqual(pair_cohomology(pair_dimensions(-1, 4, line), 0, 0), (0, 2, 0))
            # The vertical psi map has true source nonzero maps as a
            # separate analytical premise; these are its dimension data.
            self.assertEqual((h1(-2, line), h1(-1, line)), (1, 1))
            self.assertEqual((h0(3, line), h0(4, line)), (1, 1))
            self.assertEqual((pole(-2), pole(-1), pole(3), pole(4)), (-1, -1, 1, 1))
            self.assertEqual(pair_dimensions(-3, 1, line), (0, 0, 2, 0))
            self.assertEqual(pair_dimensions(1, 5, line), (0, 2, 0, 0))
            self.assertEqual(pair_cohomology(pair_dimensions(-3, 1, line), 0, 0), (0, 2, 0))
            self.assertEqual(pair_cohomology(pair_dimensions(1, 5, line), 0, 0), (0, 2, 0))
        first, second = pair_dimensions(-3, 1, ZERO), pair_dimensions(1, 5, ZERO)
        self.assertEqual(first, (0, 1, 2, 1))
        self.assertEqual(second, (1, 2, 1, 0))
        self.assertEqual(pair_cohomology(first, 0, 1), (0, 2, 0))
        self.assertEqual(pair_cohomology(second, 1, 0), (0, 2, 0))
        injection = s.Matrix([1, 0])
        self.assertEqual(injection.rank(), 1)
        self.assertEqual(injection.T.rank(), 1)
        with self.assertRaises(ValueError):
            pair_cohomology(first, 0, 2)
        self.assertNotEqual(pair_cohomology(first, 0, 0), pair_cohomology(first, 0, 1))
        # Wrong b(4)=0 loses the nontrivial flat-line target completely.
        wrong_target = int(all(x % 1 == 0 for x in CHI))
        self.assertNotEqual(wrong_target, h0(4, CHI))
        matrix, _ = raising_chain(4, s.Integer(1), s.Integer(1))
        self.assertEqual(matrix.rank(), 4)
        self.assertEqual(pair_cohomology(pair_dimensions(-3, 1, CHI), 0, 0)[1], 2)
        # Full fibre rank does not authorize deleting this global datum.

    def test_complete_charged_roster_all_neutral_strata(self):
        roots = e8_roots()
        d5, a3, cross, halves = coefficient_populations(roots)
        self.assertEqual((len(roots), len(d5), len(a3)), (240, 40, 12))
        self.assertEqual(sorted(map(len, cross.values())), [10]*6)
        self.assertEqual(sorted(map(len, halves.values())), [16]*8)
        self.assertEqual(40+12+60+128+8, 248)
        self.assertEqual({dot(EM, r) for r in d5}, {F(0)})
        self.assertEqual({dot(QY, r) % 3 for r in d5}, {F(0)})
        cross_charges, half_charges, half_phases = Counter(), Counter(), defaultdict(set)
        for rows in cross.values():
            em = {dot(EM, r) for r in rows}
            phase = {dot(QY, r) % 3 for r in rows}
            self.assertEqual(len(em), 1)
            charge = next(iter(em))
            self.assertEqual(phase, {F(1) if charge > 0 else F(2)})
            cross_charges[charge] += 1
        self.assertEqual(cross_charges, Counter({F(2, 3): 3, F(-2, 3): 3}))
        for prefix, rows in halves.items():
            self.assertEqual({sum(x < 0 for x in r) % 2 for r in rows}, {0})
            em, phases = {dot(EM, r) for r in rows}, {dot(QY, r) % 3 for r in rows}
            self.assertEqual(len(em), 1)
            charge = next(iter(em))
            half_charges[charge] += 1
            half_phases[charge].update(phases)
            self.assertEqual({sum(x < 0 for x in r[3:]) % 2 for r in rows}, {sum(x < 0 for x in prefix) % 2})
        self.assertEqual(half_charges, Counter({F(1): 1, F(-1): 1, F(-1, 3): 3, F(1, 3): 3}))
        self.assertEqual(dict(half_phases), {F(1): {F(0)}, F(-1): {F(0)}, F(-1, 3): {F(1)}, F(1, 3): {F(2)}})
        a3_neutral = sum(dot(EM, r) == 0 for r in a3)+3
        self.assertEqual(a3_neutral, 9)
        exotics = Counter(dot(EM, r) for r in a3 if dot(EM, r) != 0)
        self.assertEqual(exotics, Counter({F(4, 3): 3, F(-4, 3): 3}))
        for r in a3:
            if dot(EM, r) != 0:
                self.assertNotEqual(dot(QY, r) % 3, 0)
        self.assertEqual(neutral_count(0, 0, CHI), 0)
        d5_neutral = sum(neutral_count(j, k) for j, k in ((1, 0), (3, 0), (0, 1), (0, 3), (2, 2)))
        adjoint_multiplicity = neutral_count(0, 0)
        singlets = d5_neutral+adjoint_multiplicity
        self.assertEqual((adjoint_multiplicity, singlets), (3, 19))
        neutral_dim = d5_neutral+a3_neutral*adjoint_multiplicity
        self.assertEqual(neutral_dim, 43)
        for jp, kp, line in ((2, 0, CHI), (0, 2, CHI), (F(3, 2), F(3, 2), CHI),
                             (F(3, 2), F(3, 2), ZERO), (0, 0, CHI)):
            self.assertEqual(h0(-jp-kp, line), 0)
            self.assertEqual(h0(-jp-kp, tuple(-x for x in line)), 0)
        for plus, minus, expected in ((0, 0, (4, 2, 4, 87, 96)),
                                       (1, 0, (2, 2, 2, 71, 80)),
                                       (0, 1, (2, 2, 2, 71, 80)),
                                       (1, 1, (0, 2, 2, 59, 68)),
                                       (1, s.I, (0, 2, 2, 59, 68))):
            up, down, lepton = charged_counts(plus, minus)
            dim = neutral_dim+sum(cross_charges.values())*up
            dim += sum(n*lepton if abs(q) == 1 else n*down for q, n in half_charges.items())
            self.assertEqual((up, down, lepton, dim, dim+a3_neutral), expected)
            self.assertNotEqual(dim, expected[-1])  # gaugino omission
            self.assertNotEqual(2*dim+a3_neutral, expected[-1])  # antiparticle doubling
            self.assertGreater(down, 0)
            self.assertGreater(lepton, 0)
        # Dropping the conjugate half-spinor loses actual coefficient rows.
        one_half = [p for p in halves if sum(x < 0 for x in p) % 2 == 0]
        self.assertEqual(len(one_half), 4)
        self.assertNotEqual(len(one_half), len(halves))
        one_half_charges = Counter(dot(EM[:3], prefix) for prefix in one_half)
        self.assertEqual(one_half_charges, Counter({F(1): 1, F(-1, 3): 3}))
        self.assertNotEqual(one_half_charges, Counter({-q: n for q, n in one_half_charges.items()}))
        up0, down0, lepton0 = charged_counts(0, 0)
        missing_up = neutral_dim+sum(cross_charges.values())*(up0//2)+6*down0+2*lepton0
        self.assertNotEqual(missing_up, 87)

    def test_fourth_order_transfer_and_exact_survivor_controls(self):
        eps, kp, km, psi = s.symbols('eps kp km psi')
        t = s.symbols('t')
        chain, _ = raising_chain(4, t, s.Integer(1))
        reduced, _, _, _, _ = eliminate_raising_pivots(chain, t)
        f = reduced[3, 3]
        self.assertEqual(s.degree(f, t), 4)
        fp, fm = f.subs(t, eps*kp*psi), f.subs(t, eps*km*psi)
        # Basis form of the two analytical rank-one Hodge maps. This is
        # a rank control, not a computation of their physical magnitudes.
        coho = s.Matrix([[fp, 0, 0, 0], [fm, 0, 0, 0],
                         [0, 0, -fm, fp], [0, 0, 0, 0]])
        for order in range(4):
            self.assert_zero(coho.applyfunc(lambda entry: s.diff(entry, eps, order).subs(eps, 0)))
        self.assert_zero(coho.extract([0, 2], [0, 3]).det()-fp**2)
        self.assert_zero(coho.extract([1, 2], [0, 2]).det()+fm**2)
        for rows, cols in product(combinations(range(4), 3), repeat=2):
            self.assert_zero(coho.extract(rows, cols).det())
        for p, q in ((1, 0), (0, 1), (1, 2), (1, s.I)):
            actual = coho.subs({kp: p, km: q, eps: s.Rational(1, 10), psi: 1})
            self.assertEqual(actual.rank(), 2)
            self.assertEqual(4-actual.rank(), 2)
        self.assert_zero(coho.subs({kp: 0, km: 0}))
        self.assertEqual(charged_counts(1, 1)[1:], (2, 2))
        linear_chain, _ = raising_chain(1, eps, s.Integer(1))
        linear, _, _, _, _ = eliminate_raising_pivots(linear_chain, eps)
        self.assertEqual(s.degree(linear[0, 0], eps), 1)
        up_map = s.diag(km*linear[0, 0], km*linear[0, 0], kp*linear[0, 0], kp*linear[0, 0])
        self.assertEqual(up_map.subs({kp: 1, km: 1, eps: 1}).rank(), 4)
        self.assertEqual(up_map.subs({kp: 1, km: 0, eps: 1}).rank(), 2)
        self.assertEqual(charged_counts(1, 0)[0], 2)
        # The exact exceptional two-term LES retains these modes even
        # with its nonzero fifth-order raising-chain differential.
        self.assertEqual(pair_cohomology(pair_dimensions(-2, 3, CHI), 0, 0)[1], 2)
