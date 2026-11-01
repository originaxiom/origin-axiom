"""UNRUN exact controls, implemented after design commit da004d178.

Do not import, collect or execute before separate genuine review and
prospective admission. No prior P210 approval covers this module.
The full E8 group-component and complete-domain proofs remain analytic
review duties: finite matrix checks are not substituted for them.
"""

from collections import Counter, deque
from fractions import Fraction
from itertools import combinations, permutations, product
from math import gcd
import unittest

import sympy as s


F = Fraction
ZERO = (F(0), F(0))
SPINS = tuple(product((F(0), F(1, 2)), repeat=2))


def comm(a, b):
    return a * b - b * a


def spin_five():
    e, f = s.zeros(5), s.zeros(5)
    for i in range(4):
        e[i + 1, i] = 4 - i
        f[i, i + 1] = i + 1
    h = s.diag(-4, -2, 0, 2, 4)
    gram = s.diag(*(1 / s.binomial(4, i) for i in range(5)))
    j = s.zeros(5)
    for i in range(5):
        j[i, 4 - i] = (-1) ** i
    return e, f, h, gram, j


def char_mul(character, n):
    return tuple((n * x) % 1 for x in character)


def char_add(a, b):
    return tuple((x + y) % 1 for x, y in zip(a, b))


def h0(power, character, spin):
    degree = power // 2 if power <= 0 else (power - 1) // 2
    if degree < 0:
        return 0
    if degree > 0:
        return degree
    return int(char_add(character, char_mul(spin, power)) == ZERO)


def kernel_counts(j, character, spin):
    a = h0(j + 2, char_mul(character, -1), spin)
    u = h0(j + 1, character, spin)
    r = h0(1 - j, character, spin)
    vector = h0(-j, character, spin)
    return a + u + r, vector, r


def full_branches():
    rows = [(0, 0, 12), (0, 5, 6), (0, -5, 6)]
    rows += [(j, 0, 1) for j in range(1, 5)]
    for sign in (-1, 1):
        rows += [(2, sign * q, dim) for q, dim in ((1, 6), (-4, 3), (6, 1))]
        rows += [(j, sign * q, dim)
                 for j in (1, 3) for q, dim in ((-2, 3), (3, 2))]
    return tuple(rows)


def total_kernels(character, spin):
    out = [0, 0, 0]
    for j, charge, dim in full_branches():
        for i, count in enumerate(kernel_counts(j, char_mul(character, charge), spin)):
            out[i] += dim * count
    return tuple(out)


def source_roster_holds(character, spin):
    kappa = 1 + 2 * int(spin == ZERO)
    for j, charge, _ in full_branches():
        if j == 0:
            expected = kappa if charge == 0 else 0
        elif j == 1:
            expected = 3 if charge == 0 else 1
        else:
            expected = j
        if kernel_counts(j, char_mul(character, charge), spin)[0] != expected:
            return False
    return True


def torsion(n):
    return {(F(a, n), F(b, n)) for a, b in product(range(n), repeat=2)}


def primitive_pairs(n):
    return {(a, b) for a, b in product(range(n), repeat=2)
            if gcd(gcd(a, b), n) == 1}


def canon(pair, n):
    pair = tuple(x % n for x in pair)
    return min(pair, tuple((-x) % n for x in pair))


def move(pair, generator, n):
    a, b = pair
    if generator == "L":
        return a % n, (a + b) % n
    if generator == "R":
        return (a + b) % n, b % n
    raise ValueError(generator)


def orbit(n, quotient):
    start = (1 % n, 0)
    if quotient:
        start = canon(start, n)
    seen, pending = {start}, deque([start])
    while pending:
        pair = pending.popleft()
        for generator in ("L", "R"):
            target = move(pair, generator, n)
            if quotient:
                target = canon(target, n)
            if target not in seen:
                seen.add(target)
                pending.append(target)
    return seen


def quaternion_data():
    one = s.eye(2)
    qi = s.diag(s.I, -s.I)
    qj = s.Matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    lifts = {"L": (one + qi) / s.sqrt(2), "R": (one - qj) / s.sqrt(2)}
    labels = {"A": (1, 0), "B": (0, 1), "C": (1, 1),
              "D": (1, 2), "E": (1, 3), "F": (2, 1)}
    axes = {"A": qj, "B": qi, "C": qk, "D": -qj, "E": -qk, "F": -qi}
    return qi, qj, lifts, labels, axes


def gauge_blocks():
    # Components of one 10 and one 5; copy populations include conjugates.
    specs = {"Q": (3, 2, s.Rational(1, 6), 4),
             "U": (3, 1, s.Rational(-2, 3), 4),
             "E": (1, 1, s.Integer(1), 4),
             "D": (3, 1, s.Rational(-1, 3), 8),
             "L": (1, 2, s.Rational(1, 2), 8)}
    rows = {}
    for name, (d3, d2, y, copies) in specs.items():
        indices = s.Matrix([s.Rational(3, 5) * y**2 * d2 * d3,
                            s.Rational(d3, 2) if d2 == 2 else 0,
                            s.Rational(d2, 2) if d3 == 3 else 0])
        casimirs = s.Matrix([s.Rational(3, 5) * y**2,
                            s.Rational(3, 4) if d2 == 2 else 0,
                            s.Rational(4, 3) if d3 == 3 else 0])
        rows[name] = indices, casimirs, copies
    return rows


def beta_matrix(kappa, include_conjugates=True):
    rows = list(gauge_blocks().values())
    if not include_conjugates:
        rows = [(t, c, n // 2) for t, c, n in rows]
    rows += [(s.Matrix([0, 2, 0]), s.Matrix([0, 2, 0]), kappa),
             (s.Matrix([0, 0, 3]), s.Matrix([0, 0, 3]), kappa)]
    adjoint = s.Matrix([0, 2, 3])
    total = sum((n * t for t, _, n in rows), s.zeros(3, 1))
    b = total - 3 * adjoint
    matrix = s.Matrix(3, 3, lambda a, d:
                      2 * adjoint[a] * b[a] * int(a == d)
                      + 4 * sum(n * t[a] * c[d] for t, c, n in rows))
    return b, matrix


def e8_roots():
    roots = set()
    for a, b in combinations(range(8), 2):
        for x, y in product((-1, 1), repeat=2):
            root = [F(0)] * 8
            root[a], root[b] = F(x), F(y)
            roots.add(tuple(root))
    for signs in product((-1, 1), repeat=8):
        if sum(x == -1 for x in signs) % 2 == 0:
            roots.add(tuple(F(x, 2) for x in signs))
    return roots


def surviving_dimension(u, v, only_first=False):
    return 4 + sum((u[i] - u[j]).denominator == 1
                   and (only_first or (v[i] - v[j]).denominator == 1)
                   for i in range(5) for j in range(5) if i != j)


class PhysicalFamilyChecks(unittest.TestCase):
    def assert_zero(self, expression):
        entries = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
        self.assertTrue(all(s.simplify(x) == 0 for x in entries), str(expression))

    def test_principal_module_gram_and_chevalley_J(self):
        e, f, h, gram, j = spin_five()
        adjoint = lambda x: gram.inv() * x.conjugate().T * gram
        theta = lambda x: -gram.inv() * x.T * gram
        self.assert_zero(comm(h, e) - 2 * e)
        self.assert_zero(comm(e, f) - h)
        self.assert_zero(adjoint(e) - f)
        self.assertNotEqual(e.T, f)  # Wrong identity Gram is rejected.
        self.assert_zero(j * j - s.eye(5))
        self.assertEqual(j.det(), 1)
        self.assert_zero(j.T * gram * j - gram)
        for x in (h, e, f):
            self.assert_zero(theta(theta(x)) - x)
            self.assert_zero(j * x * j.inv() - theta(x))
        self.assert_zero(gram.inv() * j.inv().T * gram - j)
        self.assert_zero(s.trace(h * h) - 2 * s.trace(f * e))

    def test_real_gauss_eigenline_and_scalar_vector_ratio(self):
        e, f, h, _, _ = spin_five()
        q, qdag, t = e / 2, f / 2, h / 2
        k2t = (comm(qdag, comm(q, t)) + comm(q, comm(qdag, t))) / 2
        self.assert_zero(k2t - t / 2)
        self.assert_zero(2 * k2t - t)
        self.assertNotEqual(k2t, t)  # Missing sqrt(2) in d fails.
        n0, zt = s.trace(qdag * q), s.trace(t * t)
        self.assertEqual(2 * n0 / zt, 1)
        self.assertEqual((n0, zt), (5, 10))

    def test_projective_orbit_metric_and_second_chart(self):
        x, y, dx, dy = s.symbols("x y dx dy", real=True)
        norm = 1 + x*x + y*y
        z = s.Matrix([1, x + s.I*y]) / s.sqrt(norm)
        tangent = z.diff(x)*dx + z.diff(y)*dy
        phase = s.simplify(s.im((z.conjugate().T*tangent)[0]))
        naive = s.simplify((tangent.conjugate().T*tangent)[0])
        horizontal = s.simplify(naive - phase**2)
        self.assert_zero(horizontal - (dx*dx + dy*dy)/norm**2)
        control = {x: 1, y: 0, dx: 0, dy: 1}
        self.assertEqual(s.simplify((naive-horizontal).subs(control)), s.Rational(1, 4))
        u, v, du, dv = s.symbols("u v du dv", real=True)
        xp, yp = u/(u*u+v*v), -v/(u*u+v*v)
        tx = s.diff(xp, u)*du + s.diff(xp, v)*dv
        ty = s.diff(yp, u)*du + s.diff(yp, v)*dv
        self.assert_zero((tx*tx+ty*ty)/(1+xp*xp+yp*yp)**2
                         - (du*du+dv*dv)/(1+u*u+v*v)**2)

    def test_shear_identity_and_heavy_exchange_controls(self):
        c, l, h1, h2, r1, r2, rho, h = s.symbols("c l h1 h2 r1 r2 rho h")
        q, r, dq, dr = (s.Matrix(3, 3, s.symbols(prefix+":9"))
                        for prefix in ("q", "r", "dq", "dr"))
        w = s.trace(q*dr-r*dq)/2
        ws = s.trace(q*(dr+c*dq)-(r+c*q)*dq)/2
        self.assert_zero(ws-w)
        one_term_change = s.expand(s.trace(q*(dr+c*dq))-s.trace(q*dr))
        self.assertNotEqual(one_term_change, 0)
        positive = r1*(h1+l*l)+r2*(h2-l*l)-c*l*(h1+h2)
        solution = {h1: -l*l, h2: l*l, r1: c*l, r2: c*l}
        for variable in (h1, h2, r1, r2):
            self.assert_zero(s.diff(positive, variable).subs(solution))
        self.assert_zero(positive.subs(solution))
        # Real slice of the nonzero positive pulled-back Kahler interaction.
        kpull = (l*l+c*c+h1*h1+h2*h2+r1*r1+r2*r2).subs(solution)
        self.assert_zero(kpull-(l*l+c*c+2*l**4+2*c*c*l*l))
        negative = rho*(h+l*l)+c*l*h
        bad_solution = {h: -l*l, rho: -c*l}
        for variable in (h, rho):
            self.assert_zero(s.diff(negative, variable).subs(bad_solution))
        self.assert_zero(negative.subs(bad_solution)+c*l**3)
        self.assertNotEqual(s.expand(negative.subs(bad_solution)), 0)

    def test_complete_E8_principal_weight_population(self):
        roots = e8_roots()
        self.assertEqual(len(roots), 240)
        self.assertTrue(all(sum(x*x for x in root) == 2 for root in roots))
        w = (0, 0, 0, -1, 1, -2, 0, 2)
        weights = Counter(2*sum(x*y for x, y in zip(root, w)) for root in roots)
        weights[0] += 8
        self.assertTrue(all(x.denominator == 1 and x % 2 == 0 for x in weights))
        multiplicities = tuple(weights[2*j]-weights[2*j+2] for j in range(5))
        self.assertEqual(multiplicities, (24, 11, 21, 11, 1))
        self.assertEqual(sum(n*(2*j+1) for j, n in enumerate(multiplicities)), 248)
        self.assertEqual(sum(dim*(2*j+1) for j, _, dim in full_branches()), 248)

    def test_complete_light_kernel_and_R_spin_control(self):
        chi = (F(2, 7), F(0))
        for spin in SPINS:
            kappa = 1+2*int(spin == ZERO)
            nc, nv, nr = total_kernels(chi, spin)
            self.assertEqual((nc, nv), (92+12*kappa, 12))
            self.assertEqual(nr, 13 if spin == ZERO else 1)
            self.assertTrue(source_roster_holds(chi, spin))
            self.assertEqual(h0(0, ZERO, spin), 1)
            r_rows = [(j, charge, dim*kernel_counts(j, char_mul(chi, charge), spin)[2])
                      for j, charge, dim in full_branches()]
            principal_rows = [count for j, charge, count in r_rows if (j, charge) == (1, 0)]
            self.assertEqual(principal_rows, [1])
            without_principal = sum(count for j, charge, count in r_rows
                                    if (j, charge) != (1, 0))
            self.assertEqual(without_principal, 12 if spin == ZERO else 0)
            self.assertNotEqual(without_principal, nr)
        self.assertEqual([h0(a, ZERO, ZERO) for a in (0, 1, 2)], [1, 1, 1])

    def test_full_two_loop_matrix_and_weighted_row(self):
        kappa = s.symbols("kappa", integer=True, positive=True)
        b, matrix = beta_matrix(kappa)
        self.assert_zero(b-s.Matrix([10, 4+2*kappa, 1+3*kappa]))
        wanted = s.Matrix([[s.Rational(166, 15), s.Rational(42, 5), s.Rational(416, 15)],
                           [s.Rational(14, 5), 46+24*kappa, 32],
                           [s.Rational(52, 15), 12, s.Rational(178, 3)+54*kappa]])
        self.assert_zero(matrix-wanted)
        weight = s.Matrix([[s.Rational(1, 2), s.Rational(-3, 2), 1]])
        self.assert_zero(weight*b)
        self.assert_zero(weight*matrix-s.Matrix([[s.Rational(24, 5),
                         s.Rational(-264, 5)-36*kappa, s.Rational(126, 5)+54*kappa]]))
        dimensions = (1, 3, 8)
        for a, d in combinations(range(3), 2):
            self.assert_zero(dimensions[a]*matrix[a, d]-dimensions[d]*matrix[d, a])
        self.assertNotEqual(beta_matrix(kappa, False)[1], matrix)
        g, adj = s.symbols("g adj", positive=True)
        normalization = 8*s.pi**2/g**2+adj*s.log(g*g)
        beta = -3*adj*g**3/(16*s.pi**2*(1-adj*g*g/(8*s.pi**2)))
        self.assert_zero(s.diff(normalization, g)*beta-3*adj)

    def test_weighted_determinants_and_copy_frame_change(self):
        weight = s.Matrix([[s.Rational(1, 2), s.Rational(-3, 2), 1]])
        coefficients = {name: (weight*row[0])[0] for name, row in gauge_blocks().items()}
        self.assertEqual(coefficients, {"Q": s.Rational(-6, 5), "U": s.Rational(9, 10),
                          "E": s.Rational(3, 10), "D": s.Rational(3, 5), "L": s.Rational(-3, 5)})
        self.assert_zero(sum(coefficients[name] for name in ("Q", "U", "E")))
        self.assert_zero(coefficients["D"]+coefficients["L"])
        z = s.Matrix([[2, 1], [1, 2]])
        a = s.diag(2, 1)
        zp = a.inv().T*z*a.inv()
        self.assertEqual(zp.det()/z.det(), s.Rational(1, 4))
        t = s.symbols("t", positive=True)
        determinant = s.diag(t, 1).det()
        actual = s.diff(coefficients["Q"]*s.log(determinant), t)
        self.assert_zero(actual-coefficients["Q"]/t)
        self.assertNotEqual(s.simplify(2*actual-actual), 0)

    def test_harmonic_metric_period_covariance_and_scale(self):
        x, y, du, dv = s.symbols("x y du dv", real=True, positive=True)
        metric = s.Matrix([[1, x], [x, x*x+y*y]])
        inverse_norm = s.simplify(y*(s.Matrix([[du, dv]])*metric.inv()*s.Matrix([du, dv]))[0])
        norm = lambda a, b, u, v: ((v-a*u)**2+b*b*u*u)/b
        self.assert_zero(inverse_norm-norm(x, y, du, dv))
        gram = s.Matrix([[x*x+y*y, -x], [-x, 1]])/y
        self.assert_zero(gram.det()-1)
        self.assert_zero(norm(x+1, y, du, dv+du)-inverse_norm)
        denominator = (x+1)**2+y*y
        xp, yp = (x*(x+1)+y*y)/denominator, y/denominator
        self.assert_zero(norm(xp, yp, du+dv, dv)-inverse_norm)
        self.assertNotEqual(s.factor(norm(x+1, y, du, dv)-inverse_norm), 0)
        ell, coupling = s.symbols("ell coupling", positive=True)
        g4inverse = 2*s.pi*ell*ell/coupling**2
        self.assert_zero(s.pi*g4inverse/ell**2-2*s.pi**2/coupling**2)
        self.assert_zero((2*s.pi*ell**2)*20/(4*ell**2*coupling**2)
                         -10*s.pi/coupling**2)

    def test_joint_SM_stratum_and_25_central_points(self):
        y = (-2, -2, -2, 3, 3)
        u = tuple(F(2, 7)*q for q in y)
        zero = (F(0),)*5
        self.assertEqual(surviving_dimension(u, zero), 12)
        generic = tuple(F(a, 101) for a in (1, 2, 4, 8, -15))
        self.assertEqual(surviving_dimension(u, generic), 4)
        self.assertEqual(surviving_dimension(u, generic, True), 12)
        central = 0
        for p, q in product(range(5), repeat=2):
            a = tuple(F(p, 5)*x for x in y)
            b = tuple(F(q, 5)*x for x in y)
            self.assertEqual(surviving_dimension(a, b), 24)
            central += 1
        self.assertEqual(central, 25)
        self.assertEqual(surviving_dimension(tuple(-x for x in u), zero), 12)

    def test_disconnected_torus_action_and_rank_four_control(self):
        roots = e8_roots()
        self.assertEqual({tuple(-x for x in root) for root in roots}, roots)
        projection = s.eye(5)-s.ones(5)/5
        traces = []
        for perm in permutations(range(5)):
            matrix = s.zeros(5)
            for i, j in enumerate(perm):
                matrix[j, i] = 1
            traces.append(s.trace(matrix)-1)
            self.assertNotEqual((matrix+s.eye(5))*projection, s.zeros(5))
        self.assertEqual(len(traces), 120)
        self.assertGreaterEqual(min(traces), -1)
        hypercharge = s.diag(-2, -2, -2, 3, 3)
        self.assertNotEqual(-hypercharge.T, hypercharge)
        fixed = []
        for i, j in combinations(range(5), 2):
            matrix = s.zeros(5)
            matrix[i, j], matrix[j, i] = 1, -1
            self.assert_zero(-matrix.T-matrix)
            fixed.append(matrix)
        self.assertEqual(len(fixed), 10)
        self.assertEqual(s.Matrix.hstack(*(s.Matrix(25, 1, list(matrix))
                                          for matrix in fixed)).rank(), 10)

    def test_uniform_roster_exceptions_and_order_four(self):
        exceptional = torsion(3) | torsion(10)
        self.assertEqual(torsion(3) & torsion(10), {ZERO})
        self.assertEqual(len(exceptional), 108)
        allowed_orders = set()
        for n in range(1, 13):
            for a, b in primitive_pairs(n):
                chi = (F(a, n), F(b, n))
                criterion = char_mul(chi, 3) != ZERO and char_mul(chi, 10) != ZERO
                actual = all(source_roster_holds(chi, spin) for spin in SPINS)
                self.assertEqual(actual, criterion, (n, a, b))
                if actual:
                    allowed_orders.add(n)
        self.assertEqual(min(allowed_orders), 4)
        self.assertEqual(allowed_orders, {4, 6, 7, 8, 9, 11, 12})

    def test_level_four_and_seven_orbits_and_axis_map(self):
        for n, size, reduced in ((4, 12, 6), (7, 48, 24)):
            self.assertEqual(orbit(n, False), primitive_pairs(n))
            self.assertEqual(len(orbit(n, False)), size)
            self.assertEqual(orbit(n, True), {canon(p, n) for p in primitive_pairs(n)})
            self.assertEqual(len(orbit(n, True)), reduced)
        _, _, lifts, labels, axes = quaternion_data()
        inverse = {canon(value, 4): name for name, value in labels.items()}
        expected = {"L": {"A": "C", "C": "D", "D": "E", "E": "A", "B": "B", "F": "F"},
                    "R": {"B": "C", "C": "F", "F": "E", "E": "B", "A": "A", "D": "D"}}
        for generator, g in lifts.items():
            for name, pair in labels.items():
                target = inverse[canon(move(pair, generator, 4), 4)]
                self.assertEqual(target, expected[generator][name])
                self.assert_zero(g*axes[name]*g.inv()-axes[target])

    def test_inner_register_rejects_quotient_map_extension(self):
        qi, qj, lifts, labels, axes = quaternion_data()
        exponent = lambda word: (sum((1 if c == "a" else -1 if c == "A" else 0) for c in word),
                                 sum((1 if c == "b" else -1 if c == "B" else 0) for c in word))
        for word in ("a", "b", "ab", "aB"):
            self.assertEqual(exponent("ab"+word+"BA"), exponent(word))
        self.assert_zero(qi*qj*qi.inv()+qj)
        self.assertNotEqual(qi*axes["A"]*qi.inv(), axes["A"])
        self.assert_zero(lifts["L"]**4+s.eye(2))
        mu_l = (1+s.I)/s.sqrt(2)
        self.assert_zero(mu_l**4+1)
        self.assert_zero((mu_l*lifts["L"])**4-s.eye(2))
        for pair in labels.values():
            moved = pair
            for _ in range(4):
                moved = move(moved, "L", 4)
            self.assertEqual(canon(moved, 4), canon(pair, 4))

    def test_fixed_state_and_covariant_family_are_different(self):
        for n in range(1, 13):
            fixed = {p for p in product(range(n), repeat=2)
                     if all(canon(move(p, g, n), n) == canon(p, n) for g in ("L", "R"))}
            self.assertEqual(fixed, {(0, 0)})
        packet = orbit(4, True)
        self.assertEqual(len(packet), 6)
        for generator in ("L", "R"):
            self.assertEqual({canon(move(p, generator, 4), 4) for p in packet}, packet)

    def test_order_ten_jump_and_order_seven_alias_scope(self):
        chi = (F(1, 10), F(0))
        eta = char_mul(chi, 5)
        self.assertIn(eta, SPINS)
        self.assertNotEqual(eta, ZERO)
        for spin in SPINS:
            for charge in (-5, 5):
                self.assertEqual(kernel_counts(0, char_mul(chi, charge), spin)[0],
                                 2 if spin == eta else 0)
        indices = s.Matrix([s.Rational(3, 5)*s.Rational(5, 6)**2*6,
                            s.Rational(3, 2), 1])
        extra = 4*indices
        self.assertEqual(extra, s.Matrix([10, 6, 4]))
        weight = s.Matrix([[s.Rational(1, 2), s.Rational(-3, 2), 1]])
        self.assert_zero(weight*extra)
        self.assertFalse(source_roster_holds(chi, eta))
        seven, four = (F(1, 7), F(0)), (F(1, 4), F(0))
        for left, right in ((4, -3), (6, -1)):
            self.assertEqual(char_mul(seven, left), char_mul(seven, right))
            self.assertNotEqual(char_mul(four, left), char_mul(four, right))


if __name__ == "__main__":
    raise SystemExit("UNRUN scientific controls: require separate review and strict prospective admission")
