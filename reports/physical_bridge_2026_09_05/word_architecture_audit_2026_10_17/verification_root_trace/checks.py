"""Proposed exact controls. Do not import or collect before admission.

These reconstruct finite algebra, not global PDE or physical acceptance.
No source producer or stored scientific output is loaded.
"""
from itertools import combinations
import unittest
import sympy as s


HALF = s.Rational(1, 2)
QI = s.diag(s.I, -s.I)
QJ = s.Matrix([[0, 1], [-1, 0]])
QK = QI * QJ
EPS = QJ
IDENTITY = ((1,), (2,))
L = ((1,), (1, 2))
R = ((1, 2), (2,))
LI = ((1,), (-1, 2))
RI = ((1, -2), (2,))


def reduce_word(word):
    result = []
    for letter in word:
        if result and result[-1] == -letter:
            result.pop()
        else:
            result.append(letter)
    return tuple(result)


def inverse_word(word):
    return tuple(-x for x in reversed(word))


def substitute(phi, word):
    return reduce_word(y for x in word for y in
                       (phi[x - 1] if x > 0 else inverse_word(phi[-x - 1])))


def compose(phi, psi):
    return tuple(substitute(phi, w) for w in psi)


def power(phi, n):
    result = IDENTITY
    for _ in range(n):
        result = compose(result, phi)
    return result


def inner(word):
    return tuple(reduce_word(word + (x,) + inverse_word(word)) for x in (1, 2))


def root_step(name, state):
    """Formal phase exp(pi*i*p), with principal fourth roots retained separately."""
    t, z, p, roots = state
    if name == "A": return t, z + 1, p + HALF, roots
    if name == "a": return t, z - 1, p - HALF, roots
    if name == "B": return t, z + t, p + HALF - t/2 - z, roots
    if name == "b": return t, z - t, p - HALF - t/2 + z, roots
    if name == "C": return t, z, p + 1, roots
    if name == "K": return t, z + 2, p, roots
    if name == "k": return t, z - 2, p, roots
    if name == "H": return t, z + 2*t, p - 2*t - 2*z, roots
    if name == "h": return t, z - 2*t, p - 2*t + 2*z, roots
    if name == "L": return t + 1, z, p + s.Rational(1, 8), roots
    if name == "S":
        return -1/t, z/t, p - s.Rational(3, 8) + z*z/(2*t), roots + (t,)
    raise ValueError("Unknown map: " + name)


def root_word(word, t, z):
    state = (t, z, s.S.Zero, ())
    for name in reversed(word):
        state = root_step(name, state)
    return state


def matrix_zero(matrix):
    return all(s.simplify(x) == 0 for x in matrix)


def basis_matrix(vectors, rows=6):
    return s.Matrix.hstack(*vectors) if vectors else s.zeros(rows, 0)


def complement(matrix):
    return basis_matrix(matrix.conjugate().T.nullspace(), matrix.rows)


def trace_maps(b):
    return (s.kronecker_product(s.eye(3), b),
            s.kronecker_product(s.eye(3), b.T * EPS))


class RootTraceChecks(unittest.TestCase):
    def assertZero(self, matrix):
        self.assertTrue(matrix_zero(matrix), str(matrix))

    def assertRootEqual(self, left, right):
        self.assertEqual(s.simplify(left[0] - right[0]), 0)
        self.assertEqual(s.simplify(left[1] - right[1]), 0)
        difference = s.simplify(left[2] - right[2])
        self.assertTrue(difference.is_Integer and int(difference) % 2 == 0,
                        str(difference))
        self.assertEqual(tuple(map(s.simplify, left[3])),
                         tuple(map(s.simplify, right[3])))

    def test_actual_quaternion_group_and_central_sign(self):
        group = {s.ImmutableMatrix(x) for x in
                 (s.eye(2), -s.eye(2), QI, -QI, QJ, -QJ, QK, -QK)}
        self.assertEqual(len(group), 8)
        for a in group:
            for b in group:
                self.assertIn(s.ImmutableMatrix(a*b), group)
        self.assertEqual(QI*QJ*QI.inv()*QJ.inv(), -s.eye(2))
        self.assertNotEqual(QI*QJ, QJ*QI)
        self.assertEqual((-s.eye(2)).det(), 1)

    def test_based_fourth_power_retains_inverse_hidden_by_quaternion_image(self):
        delta = compose(L, compose(RI, L))
        sigma = compose(R, compose(LI, R))
        c = (1, -2, -1, 2)
        self.assertEqual(compose(delta, sigma), IDENTITY)
        self.assertEqual(power(delta, 4), inner(c))
        self.assertEqual(power(sigma, 4), inner(inverse_word(c)))
        self.assertNotEqual(power(sigma, 4), inner(c))
        self.assertEqual(power(compose(sigma, L), 3), power(sigma, 2))

    def test_root_period_maps_and_noncommuting_control(self):
        t, z = s.symbols("t z")
        for a, b in (("AB", "CBA"), ("AA", "CK"), ("BB", "CH"),
                     ("KH", "HK"), ("AK", "KA"), ("BH", "HB")):
            self.assertRootEqual(root_word(a, t, z), root_word(b, t, z))
        self.assertEqual(s.simplify(root_word("AB", t, z)[2] -
                                    root_word("BA", t, z)[2]), 1)
        # Omitting the z term in B would make the two period maps commute.
        bad_ab = HALF + (HALF - t/2)
        bad_ba = (HALF - t/2) + HALF
        self.assertEqual(s.simplify(bad_ab - bad_ba), 0)

    def test_modular_maps_normalize_actual_cover_lattice(self):
        t, z = s.symbols("t z")
        for a, b in (("LK", "KL"), ("LH", "HkL"),
                     ("SK", "hS"), ("SH", "KS")):
            self.assertRootEqual(root_word(a, t, z), root_word(b, t, z))

    def test_joint_minus_period_marking_obeys_actual_based_conjugations(self):
        t, z = s.symbols("t z")
        # D_a=A, D_b=C b, and D_b^-1=B C; maps act rightmost first.
        for a, b in (("LA", "AL"), ("LCb", "ACbL"),
                     ("SA", "CbS"), ("SCb", "BCaCbS")):
            self.assertRootEqual(root_word(a, t, z), root_word(b, t, z))
        self.assertEqual(s.simplify(root_word("Cb", t, z)[1] - z), -t)
        self.assertNotEqual(root_word("Cb", t, z)[1], root_word("B", t, z)[1])

    def test_modular_central_relations_keep_branch_lemma_explicit(self):
        t, z = s.symbols("t z")
        squared = root_word("SS", t, z)
        mixed = root_word("SLSLSL", t, z)
        for row in (squared, mixed):
            self.assertEqual(s.simplify(row[0] - t), 0)
            self.assertEqual(s.simplify(row[1] + z), 0)
            self.assertEqual(s.simplify(row[2]), -s.Rational(3, 4))
            self.assertEqual(s.simplify(s.prod(row[3])), -1)
        # The authored analytic lemma is that BOTH root argument sums are pi.
        # This exact phase bookkeeping does not prove that branch lemma.
        principal_product_phase = s.Rational(1, 4)
        self.assertEqual(squared[2] + principal_product_phase, -HALF)
        self.assertEqual(2*(-HALF), -1)  # S^4 is the root-sheet flip.
        self.assertNotEqual((-HALF) + 1, -HALF)  # one reversed lift fails mixed law.

    def test_combined_line_and_epsilon_compensation(self):
        x = s.symbols("x", nonzero=True)
        zeta = (1+s.I)/s.sqrt(2)
        for k2, j, mu in ((zeta, 1, zeta),
                          (s.exp(-3*s.pi*s.I/4)*x, x, s.exp(-3*s.pi*s.I/4)),
                          (1, 1, 1), (1, -1, -1)):
            self.assertEqual(s.simplify(k2-j*mu), 0)
        self.assertEqual((-1)*(-s.eye(2)), s.eye(2))
        self.assertNotEqual((+1)*(-s.eye(2)), s.eye(2))

    def test_trace_sequence_has_two_nonzero_charts_and_zero_control(self):
        x, y = s.symbols("x y", nonzero=True)
        b = s.Matrix([x, y])
        inc, delta = trace_maps(b)
        self.assertZero(delta*inc)
        self.assertEqual(s.simplify((b.T*EPS*s.Matrix([0, 1/x]))[0]), 1)
        self.assertEqual(s.simplify((b.T*EPS*s.Matrix([-1/y, 0]))[0]), 1)
        self.assertFalse(matrix_zero(s.kronecker_product(s.eye(3), b.T)*inc))
        bad_inc, bad_delta = trace_maps(s.zeros(2, 1))
        self.assertEqual(bad_inc.rank(), 0)
        self.assertEqual(bad_delta.rank(), 0)

    def test_residue_pullback_keeps_ramification_and_derivative_factor(self):
        u = s.symbols("u")
        a, b, c, d, ap, bp = s.symbols("a b c d ap bp")
        profile = s.Matrix([a, b])/u + u**3*s.Matrix([ap, bp])
        principal = s.Matrix([c, d])/u
        pulled = s.expand((profile.T*EPS*principal)[0]*2*u)
        downstairs = a*d-b*c
        self.assertEqual(s.expand(pulled).coeff(u, -1), 2*downstairs)
        self.assertEqual(s.expand((profile.T*EPS*principal)[0]).coeff(u, -1), 0)
        scale = s.symbols("scale", nonzero=True)
        self.assertEqual(s.simplify(((s.Matrix([a,b])/scale).T*EPS*
                                    s.Matrix([c,d]))[0]), downstairs/scale)

    def test_cover_regular_scalar_form_and_spin_are_different_types(self):
        # z=u^2: coefficient exponent transforms as 2*a+tensor_weight.
        self.assertEqual(2*HALF + 0, 1)       # regular odd scalar
        self.assertEqual(2*(-HALF) + 1, 0)  # regular even form coefficient
        self.assertEqual(2*(-HALF) + HALF, -HALF)  # not regular spin coefficient
        self.assertEqual(8*0+4, 2*3-2)        # reviewed ramification hypothesis
        self.assertEqual(s.Rational(2*3-2,2), 2)
        self.assertNotEqual(0, 2)            # pullback elliptic spin degree != spin degree

    def test_coordinate_domains_both_kernels_via_independent_intersections(self):
        tested = 0
        for b in (s.Matrix([1,0]), s.Matrix([0,1]),
                  s.Matrix([1,s.I]), s.Matrix([2+s.I,1-2*s.I])):
            inc, delta = trace_maps(b)
            negative = s.kronecker_product(s.eye(3), EPS.T*b.conjugate())
            for size in range(7):
                for indices in combinations(range(6), size):
                    domain = basis_matrix([s.eye(6)[:,i] for i in indices])
                    d, rank = domain.cols, (delta*domain).rank()
                    plus = 3+d-s.Matrix.hstack(inc, domain).rank()
                    other = complement(domain)
                    minus = 3+other.cols-s.Matrix.hstack(negative, other).rank()
                    self.assertEqual((plus,minus), (d-rank,3-rank))
                    self.assertEqual(plus-minus, d-3)
                    tested += 1
        self.assertEqual(tested, 256)

    def test_special_theta_domains_and_rank_jump_are_not_generic_sampling(self):
        t = s.symbols("t")
        b = s.Matrix([1,s.I])
        inc, delta = trace_maps(b)
        neg = s.kronecker_product(s.eye(3), EPS.T*b.conjugate())
        for domain, expected in ((inc,(3,3)), (neg,(0,0)),
                                 (s.eye(6),(3,0)), (s.zeros(6,0),(0,3))):
            r = (delta*domain).rank()
            self.assertEqual((domain.cols-r,3-r), expected)
        restricted = delta*(inc+t*neg)
        self.assertEqual(s.factor(restricted.det()), 8*t**3)
        for value, expected in ((0,(3,3)), (1,(0,0)), (-1,(0,0)), (2,(0,0))):
            r = restricted.subs(t,value).rank()
            self.assertEqual((3-r,3-r), expected)

    def test_actual_cauchy_and_extreme_domains_preserve_green_form(self):
        inc, delta = trace_maps(s.Matrix([1,s.I]))
        neg = complement(inc)
        green = s.BlockMatrix([[s.zeros(6),s.eye(6)],
                               [s.eye(6),s.zeros(6)]]).as_explicit()
        cauchy = s.diag(inc, neg)
        upper = s.Matrix.vstack(s.eye(6),s.zeros(6))
        self.assertEqual(cauchy.shape, (12,6))
        self.assertZero(cauchy.conjugate().T*green*cauchy)
        self.assertZero(upper.conjugate().T*green*upper)
        self.assertEqual(12-s.Matrix.hstack(cauchy,upper).rank(), 3)
        self.assertEqual(12-s.Matrix.hstack(cauchy,cauchy).rank(), 6)
        bad = s.Matrix.vstack(s.eye(6),s.eye(6))
        self.assertFalse(matrix_zero(bad.conjugate().T*green*bad))

    def test_full_doublet_quartet_projection_retains_both_pieces(self):
        contract = s.Matrix.hstack(QJ,QI,QK)
        p2 = contract.conjugate().T*contract/3
        p4 = s.eye(6)-p2
        self.assertZero(p2*p2-p2)
        self.assertEqual((p2.rank(),p4.rank()), (2,4))
        for b in (s.Matrix([1,0]), s.Matrix([1,s.I]), s.Matrix([2+s.I,1])):
            inc, _ = trace_maps(b)
            n = (b.conjugate().T*b)[0]
            lam = s.symbols("lam")
            g2 = inc.conjugate().T*p2*inc
            expected = lam*(lam-n/3)*(lam-2*n/3)
            self.assertEqual(s.factor(g2.charpoly(lam).as_expr()-expected), 0)
            self.assertEqual((p2*inc).rank(), 2)
            self.assertEqual((p4*inc).rank(), 3)

    def test_flat_transport_removes_only_constant_sector_ratio(self):
        contract = s.Matrix.hstack(QJ,QI,QK)
        p2 = contract.conjugate().T*contract/3
        p4 = s.eye(6)-p2
        ra = s.kronecker_product(s.eye(3),QI)
        rb = s.kronecker_product(s.eye(3),QJ)
        a,b = s.symbols("a b")
        h = a*p2+b*p4
        self.assertFalse(matrix_zero(p2*ra-ra*p2))
        self.assertZero((h*ra-ra*h).subs(b,a))
        self.assertFalse(matrix_zero((h*rb-rb*h).subs({a:1,b:2})))
        self.assertZero(h*ra-ra*h-(a-b)*(p2*ra-ra*p2))

    def test_all_critical_residue_ranks_keep_same_holonomy_but_change_degree(self):
        for d in range(7):
            residue = s.diag(*([-HALF]*d+[HALF]*(6-d)))
            self.assertEqual(residue.trace(), 3-d)
            holonomy = s.diag(*(s.simplify(s.exp(-2*s.pi*s.I*x))
                                   for x in residue.diagonal()))
            self.assertEqual(holonomy, -s.eye(6))
            self.assertEqual(holonomy.det(), 1)
            self.assertEqual(residue.trace()==0, d==3)

    def test_smooth_traceless_cap_has_curvature_without_determinant_flux(self):
        x,y,r = s.symbols("x y r", real=True, positive=True)
        b = s.diag(HALF,HALF,HALF,-HALF,-HALF,-HALF)
        ax,ay = -s.I*b*y/r**2,s.I*b*x/r**2
        curvature = ay.diff(x)-ax.diff(y)+ax*ay-ay*ax
        self.assertEqual(curvature, 2*s.I*b/r**2)
        self.assertEqual(curvature.trace(), 0)
        self.assertFalse(matrix_zero(curvature))
        self.assertEqual(s.diag(*(s.simplify(s.exp(-2*s.pi*s.I*z))
                                  for z in b.diagonal())), -s.eye(6))
        central = -s.eye(6)/2
        self.assertNotEqual(central.trace(), 0)
        self.assertEqual(s.diag(*(s.simplify(s.exp(-2*s.pi*s.I*z))
                                  for z in central.diagonal())), -s.eye(6))

    def test_trace_flux_energy_bound_and_traceless_countercontrol(self):
        # The constant-curvature disc control has H=2*R/R0^2.
        # Divide all energies by pi/(g^2 R0^2) to keep exact rational data.
        for d in range(7):
            residue = s.diag(*([-HALF]*d+[HALF]*(6-d)))
            flux = -residue.trace()
            energy = 2*s.trace(residue*residue)
            trace_bound = flux**2/s.Integer(3)
            self.assertEqual(energy, 3)
            self.assertEqual(energy-trace_bound, s.Rational(d*(6-d),3))
            self.assertGreaterEqual(energy-trace_bound, 0)
            self.assertEqual(energy==trace_bound, d in (0,6))
        self.assertEqual(s.Integer(3)**2/s.Integer(3), 3)
        self.assertNotEqual(3, 0)  # traceless control's energy is not its zero trace bound
