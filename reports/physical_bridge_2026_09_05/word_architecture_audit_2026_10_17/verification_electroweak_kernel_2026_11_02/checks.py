"""UNRUN finite controls, implemented after design commit f5f1042d6.

Do not import, collect or execute without genuine review and strict
prospective admission. Finite arithmetic cannot certify graph-domain
contraction or the full physical map. No older acceptance applies.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
import unittest

import sympy as s


F = Fraction
ZERO = (F(0), F(0))
SPINS = tuple(product((F(0), F(1, 2)), repeat=2))
CHI = (F(1, 3), F(0))
ORDER = (5, 3, 6, 4, 7)
W = (0, 0, 0, -1, 1, -2, 0, 2)
QY = (F(5, 2),)*3+(F(-3, 2),)*5
EM = (F(2, 3),)*3+(F(0),)*5
BLOCKS = ((F(1), F(0), "1"), (F(3), F(0), "1"),
          (F(0), F(1), "1"), (F(0), F(3), "1"),
          (F(2), F(2), "1"), (F(0), F(0), "15"),
          (F(2), F(0), "6"), (F(0), F(2), "6"),
          (F(3, 2), F(3, 2), "4"), (F(3, 2), F(3, 2), "bar4"))


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def comm(a, b):
    return a*b-b*a


def dagger(a):
    return a.conjugate().T


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


def source_matrices():
    h5 = s.diag(-4, -2, 0, 2, 4)
    e5, j5 = s.zeros(5), s.zeros(5)
    for i in range(4):
        e5[i+1, i] = s.sqrt((i+1)*(4-i))
    for i in range(5):
        j5[i, 4-i] = (-1)**i
    bz = s.sqrt(s.Rational(2, 5))*skew(1, 4)-s.sqrt(s.Rational(3, 5))*skew(2, 3)
    e, g, h = ten(e5), s.sqrt(10)*ten(b=bz, c=j5*bz*j5), ten(h5)
    return e5, j5, bz, e, g, h


def split_triples(e, g):
    plus, minus = (e+g)/2, (e-g)/2
    return plus, minus, comm(plus, dagger(plus)), comm(minus, dagger(minus))


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


def populations(roots):
    d5 = {r for r in roots if not any(r[:3])}
    a3 = {r for r in roots if not any(r[3:])}
    halves = {r for r in roots if all(abs(x) == F(1, 2) for x in r)}
    cross = roots-d5-a3-halves
    return d5, a3, cross, halves


def root_matrix(root):
    row = [root[i] for i in ORDER]
    plus, minus = [i for i, x in enumerate(row) if x == 1], [i for i, x in enumerate(row) if x == -1]
    if len(plus) == len(minus) == 1:
        return ten(elementary(5, plus[0], minus[0]))
    if len(plus) == 2 and not minus:
        return ten(b=skew(*plus))
    if len(minus) == 2 and not plus:
        return ten(c=-skew(*minus))
    raise ValueError(root)


@lru_cache(None)
def creators():
    out = []
    for i in range(5):
        matrix = s.zeros(32)
        for mask in range(32):
            if not mask & (1 << i):
                matrix[mask | (1 << i), mask] = (-1)**((mask & ((1 << i)-1)).bit_count())
        out.append(matrix)
    return tuple(out)


@lru_cache(None)
def spin_image(immutable_matrix):
    x = immutable_matrix
    a, b, c = x[:5, :5], x[:5, 5:], x[5:, :5]
    creation = creators()
    annihilation = tuple(dagger(matrix) for matrix in creation)
    out = -s.trace(a)*s.eye(32)/2
    for i, j in product(range(5), repeat=2):
        if a[i, j] != 0:
            out += a[i, j]*creation[i]*annihilation[j]
        if b[i, j] != 0:
            out += b[i, j]*creation[i]*creation[j]/2
        if c[i, j] != 0:
            out += c[i, j]*annihilation[i]*annihilation[j]/2
    return s.ImmutableMatrix(out)


def spin(x):
    return spin_image(s.ImmutableMatrix(x))


def spectral_projector(h, value, values):
    out = s.eye(h.rows)
    for other in values:
        if other != value:
            out = out*(h-other*s.eye(h.rows))/(value-other)
    return out


def weight_pairs(j, k):
    return list(product(range(-int(2*j), int(2*j)+1, 2),
                        range(-int(2*k), int(2*k)+1, 2)))


def coefficient_rows(roots, label):
    _, a3, cross, halves = populations(roots)
    if label == "1":
        return [(F(0), F(0), "neutral")]
    if label == "15":
        rows = [(dot(QY, r), dot(EM, r), "color_adj" if dot(EM, r) == 0 else "exotic")
                for r in sorted(a3)]
        return rows+[(F(0), F(0), "color_adj")]*2+[(F(0), F(0), "neutral")]
    groups = defaultdict(list)
    population = cross if label == "6" else halves
    for root in population:
        first = root[:3]
        if label == "4" and sum(x < 0 for x in first) % 2 != 0:
            continue
        if label == "bar4" and sum(x < 0 for x in first) % 2 != 1:
            continue
        groups[first].append(root)
    rows = []
    for first, group in sorted(groups.items()):
        residues = {dot(QY, root) % 3 for root in group}
        if len(residues) != 1:
            raise ValueError("Internal source weights have different flat characters")
        charge = sum(first)*F(2, 3)
        if label == "6":
            category = "up+" if charge > 0 else "up-"
        elif abs(charge) == 1:
            category = "lepton+" if charge > 0 else "lepton-"
        else:
            category = "down+" if charge < 0 else "down-"
        rows.append((next(iter(residues)), charge, category))
    return rows


def rational_module(j):
    n = int(2*j)
    e, f = s.zeros(n+1), s.zeros(n+1)
    for i in range(n):
        e[i+1, i], f[i, i+1] = n-i, i+1
    h = s.diag(*range(-n, n+1, 2))
    gram = s.diag(*(1/s.binomial(n, i) for i in range(n+1)))
    return e, f, h, gram


def koszul(a, b):
    return a.col_join(b), (-b).row_join(a)


def graded_koszul(j, k, a, b):
    n = a.rows
    d0, d1 = koszul(a, b)
    weights = [F(x+y, 2) for x, y in weight_pairs(j, k)]
    exponents = [[-weight for weight in weights],
                 [1-weight for weight in weights]*2,
                 [2-weight for weight in weights]]
    out = Counter()
    for power in set(sum(exponents, [])):
        indices = [[i for i, value in enumerate(row) if value == power] for row in exponents]
        b0, b1 = d0.extract(indices[1], indices[0]), d1.extract(indices[2], indices[1])
        ranks = b0.rank(), b1.rank()
        dims = (len(indices[0])-ranks[0], len(indices[1])-sum(ranks), len(indices[2])-ranks[1])
        for degree, dimension in enumerate(dims):
            if dimension:
                out[(degree, power)] = dimension
    return out


def char_mul(character, n):
    return tuple((x*n) % 1 for x in character)


def char_add(a, b):
    return tuple((x+y) % 1 for x, y in zip(a, b))


def pole_bound(power):
    if F(power).denominator != 1:
        raise ValueError("An additional fractional spin line was not admitted")
    power = int(power)
    return power//2 if power <= 0 else (power-1)//2


def h0(power, line, eta, wrong_endpoint=False):
    degree = 1 if wrong_endpoint and power == 2 else pole_bound(power)
    if degree < 0:
        return 0
    if degree > 0:
        return degree
    return int(char_add(char_mul(eta, power), line) == ZERO)


def new_counts(j, k, line, eta):
    total = j+k
    chiral = h0(total+2, char_mul(line, -1), eta)
    chiral += h0(1+j-k, line, eta)+h0(1-j+k, line, eta)
    vector = h0(-total, line, eta)
    gaugino = h0(-total, char_mul(line, -1), eta)
    return chiral, vector, gaugino


def new_population(roots, eta, blocks=BLOCKS):
    totals, roster = [0, 0, 0], Counter()
    for j, k, label in blocks:
        for residue, _, category in coefficient_rows(roots, label):
            counts = new_counts(j, k, char_mul(CHI, residue), eta)
            for i, value in enumerate(counts):
                totals[i] += value
            roster[category] += counts[0]
    return tuple(totals), roster


def old_population(roots, eta):
    # Reconstruct the old complete diagonal-triple strings from actual roots.
    groups = defaultdict(Counter)
    for root in roots:
        key = (dot(QY, root), dot(EM, root), root[0]-root[1], root[1]-root[2])
        groups[key][2*dot(W, root)] += 1
    groups[(F(0), F(0), F(0), F(0))][F(0)] += 8
    chiral, vector = 0, 0
    for key, weights in groups.items():
        line = char_mul(CHI, key[0])
        for j in range(5):
            copies = weights[2*j]-weights[2*j+2]
            if copies < 0:
                raise ValueError("Diagonal string reconstruction is incomplete")
            nc = h0(j+2, char_mul(line, -1), eta)+h0(j+1, line, eta)+h0(1-j, line, eta)
            chiral += copies*nc
            vector += copies*h0(-j, line, eta)
    return chiral, vector


class ElectroweakKernelChecks(unittest.TestCase):
    def assert_zero(self, expression):
        entries = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
        self.assertTrue(all(s.simplify(x) == 0 for x in entries), str(expression))

    def test_explicit_two_triple_split_and_orthogonal_form(self):
        e5, j5, bz, e, g, h = source_matrices()
        self.assert_zero(bz*j5-e5/s.sqrt(10))
        form = s.zeros(5).row_join(s.eye(5)).col_join(s.eye(5).row_join(s.zeros(5)))
        u = s.diag(s.eye(5), j5)
        hadamard = s.Matrix([[1, 1], [1, -1]])/s.sqrt(2)
        v = s.kronecker_product(hadamard, s.eye(5))
        for matrix in (u, v):
            self.assert_zero(dagger(matrix)*matrix-s.eye(10))
        self.assert_zero(u*e*dagger(u)-s.kronecker_product(s.eye(2), e5))
        self.assert_zero(u*g*dagger(u)-s.kronecker_product(s.Matrix([[0, 1], [1, 0]]), e5))
        self.assertNotEqual(g, s.kronecker_product(s.Matrix([[0, 1], [1, 0]]), e5))
        transform = v*u
        transported = transform.conjugate()*form*dagger(transform)
        self.assert_zero(transported-s.diag(j5, -j5))
        plus, minus, hp, hm = split_triples(e, g)
        self.assert_zero(plus+minus-e)
        self.assert_zero(plus-minus-g)
        self.assert_zero(hp+hm-h)
        for raising, grading in ((plus, hp), (minus, hm)):
            self.assert_zero(comm(grading, raising)-2*raising)
            self.assert_zero(raising.T*form+form*raising)
        for x in (plus, dagger(plus), hp):
            for y in (minus, dagger(minus), hm):
                self.assert_zero(comm(x, y))
        self.assert_zero(transform*plus*dagger(transform)-s.diag(e5, s.zeros(5)))
        self.assert_zero(transform*minus*dagger(transform)-s.diag(s.zeros(5), e5))
        collapsed_plus, collapsed_minus, _, collapsed_hm = split_triples(e, e)
        self.assertEqual(collapsed_minus, s.zeros(10))
        self.assertEqual(collapsed_hm, s.zeros(10))
        self.assertNotEqual(minus, collapsed_minus)
        self.assertEqual(s.trace(dagger(minus)*minus)/2, 10)
        self.assertEqual(s.trace(dagger(collapsed_minus)*collapsed_minus)/2, 0)
        self.assertNotEqual(collapsed_plus, s.zeros(10))

    def test_full_D5_A3_population_and_actual_half_spinors(self):
        roots = e8_roots()
        d5, a3, cross, halves = populations(roots)
        self.assertTrue(all(dot(root, root) == 2 for root in roots))
        self.assertEqual((len(d5), len(a3), len(cross), len(halves)), (40, 12, 60, 128))
        self.assertEqual(len(roots)+8, 248)
        basis = [root_matrix(root) for root in sorted(d5)]
        basis += [ten(elementary(5, i, i)) for i in range(5)]
        simple = [ten(elementary(5, i, i+1)) for i in range(4)]+[ten(b=skew(3, 4))]
        generators = simple+[dagger(x) for x in simple]+basis[-5:]
        creation = creators()
        for i, j in product(range(5), repeat=2):
            self.assert_zero(creation[i]*dagger(creation[j])+dagger(creation[j])*creation[i]
                             -int(i == j)*s.eye(32))
            self.assert_zero(creation[i]*creation[j]+creation[j]*creation[i])
        for x in basis:
            self.assert_zero(spin(dagger(x))-dagger(spin(x)))
            for y in generators:
                self.assert_zero(spin(comm(x, y))-comm(spin(x), spin(y)))
        even = [mask for mask in range(32) if mask.bit_count() % 2 == 0]
        odd = [mask for mask in range(32) if mask.bit_count() % 2 == 1]
        for x in basis:
            self.assert_zero(spin(x).extract(even, odd))
            self.assert_zero(spin(x).extract(odd, even))
        # Bind the Fock Cartan weights to the literal last-five E8 half weights.
        for i in range(5):
            expected_cartan = s.diag(*(s.Rational(1, 2) if mask & (1 << i)
                                       else s.Rational(-1, 2) for mask in range(32)))
            self.assert_zero(spin(ten(elementary(5, i, i)))-expected_cartan)
        half_root_masks = defaultdict(set)
        for root in halves:
            mask = sum((1 << i) for i, coordinate in enumerate(ORDER) if root[coordinate] > 0)
            first_parity = sum(value < 0 for value in root[:3]) % 2
            self.assertEqual(mask.bit_count() % 2, (1-first_parity) % 2)
            half_root_masks[root[:3]].add(mask)
        for first, masks in half_root_masks.items():
            first_parity = sum(value < 0 for value in first) % 2
            self.assertEqual(masks, set(odd if first_parity == 0 else even))
        _, _, _, e, g, _ = source_matrices()
        plus, minus, hp, hm = split_triples(e, g)
        weights = (-3, -1, 1, 3)
        actual_spinors = []
        for parity in (0, 1):
            indices = [mask for mask in range(32) if mask.bit_count() % 2 == parity]
            self.assertEqual(len(indices), 16)
            a, b = spin(hp).extract(indices, indices), spin(hm).extract(indices, indices)
            self.assert_zero(comm(a, b))
            for grading in (a, b):
                polynomial = s.eye(16)
                for weight in weights:
                    polynomial = polynomial*(grading-weight*s.eye(16))
                self.assert_zero(polynomial)
            pa = {weight: spectral_projector(a, weight, weights) for weight in weights}
            pb = {weight: spectral_projector(b, weight, weights) for weight in weights}
            self.assert_zero(sum(pa.values(), s.zeros(16))-s.eye(16))
            self.assert_zero(sum(pb.values(), s.zeros(16))-s.eye(16))
            for projectors in (pa, pb):
                for x, y in product(weights, repeat=2):
                    self.assert_zero(projectors[x]*projectors[y]
                                     -(projectors[x] if x == y else s.zeros(16)))
            character = Counter()
            for x, y in product(weights, repeat=2):
                value = s.simplify(s.trace(pa[x]*pb[y]))
                self.assertEqual(value, 1)
                character[(x, y)] = int(value)
            actual_spinors.append(character)
        vector_weights = weight_pairs(2, 0)+weight_pairs(0, 2)
        actual = Counter()
        for a, b in combinations(vector_weights, 2):
            actual[(a[0]+b[0], a[1]+b[1])] += 1  # adjoint45=exterior-square10
        actual[(0, 0)] += 15
        actual.update({key: 6*value for key, value in Counter(vector_weights).items()})
        for character in actual_spinors:
            actual.update({key: 4*value for key, value in character.items()})
        expected = Counter()
        for j, k, label in BLOCKS:
            expected.update({key: value*len(coefficient_rows(roots, label))
                             for key, value in Counter(weight_pairs(j, k)).items()})
        self.assertEqual(actual, expected)
        self.assertEqual(sum(actual.values()), 248)
        diagonal = Counter()
        for (x, y), copies in actual.items():
            diagonal[x+y] += copies
        self.assertEqual(tuple(diagonal[2*j]-diagonal[2*j+2] for j in range(5)), (24, 11, 21, 11, 1))
        missing = actual.copy()
        missing.subtract({key: 4*value for key, value in actual_spinors[1].items()})
        self.assertEqual(sum(missing.values()), 184)
        wrong_diagonal = Counter()
        for (x, y), copies in missing.items():
            wrong_diagonal[x+y] += copies
        self.assertNotEqual(tuple(wrong_diagonal[2*j]-wrong_diagonal[2*j+2] for j in range(5)), (24, 11, 21, 11, 1))

    def test_actual_Koszul_generator_change_and_extreme_grading(self):
        for j, k in sorted({(j, k) for j, k, _ in BLOCKS}):
            ej, fj, hj, gj = rational_module(j)
            ek, fk, hk, gk = rational_module(k)
            gram = s.kronecker_product(gj, gk)
            a = s.kronecker_product(ej, s.eye(ek.rows))
            b = s.kronecker_product(s.eye(ej.rows), ek)
            self.assert_zero(gram.inv()*a.T*gram-s.kronecker_product(fj, s.eye(ek.rows)))
            self.assert_zero(gram.inv()*b.T*gram-s.kronecker_product(s.eye(ej.rows), fk))
            self.assertTrue(all(value > 0 for value in gram.diagonal()))
            n = a.rows
            q, r = 3*(a+b)/5, 4*(a-b)/5
            old0, old1 = koszul(q, r)
            new0, new1 = koszul(a, b)
            change = s.Matrix([[s.Rational(3, 5), s.Rational(3, 5)],
                               [s.Rational(4, 5), s.Rational(-4, 5)]]).inv()
            change1 = s.kronecker_product(change, s.eye(n))
            change2 = change.det()*s.eye(n)
            self.assert_zero(new0-change1*old0)
            self.assert_zero(new1*change1-change2*old1)
            self.assert_zero(old1*old0)
            self.assert_zero(new1*new0)
            self.assertNotEqual(change.det(), 0)
            expected = Counter({(0, -j-k): 1, (2, 2+j+k): 1})
            expected[(1, 1+j-k)] += 1
            expected[(1, 1-j+k)] += 1
            self.assertEqual(graded_koszul(j, k, a, b), expected)
            if j and k:
                endpoint0, endpoint1 = koszul(q, s.zeros(n))
                self.assertEqual(2*n-endpoint0.rank()-endpoint1.rank(), 2*(int(2*min(j, k))+1))
                self.assertNotEqual(2*n-endpoint0.rank()-endpoint1.rank(), 2)
                singular_change = s.Matrix([[s.Rational(3, 5), s.Rational(3, 5)], [0, 0]])
                self.assertEqual(singular_change.det(), 0)

    def test_full_root_flat_phases_and_colour_EM_assignment(self):
        roots = e8_roots()
        d5, a3, cross, halves = populations(roots)
        self.assertTrue(all(dot(QY, root) % 3 == 0 for root in d5))
        self.assertEqual(Counter(row[1] for row in coefficient_rows(roots, "6")), {F(2, 3): 3, F(-2, 3): 3})
        for residue, charge, _ in coefficient_rows(roots, "6"):
            self.assertEqual(residue, 1 if charge > 0 else 2)
        for label, wanted in (("4", {F(1): 1, F(-1, 3): 3}),
                              ("bar4", {F(-1): 1, F(1, 3): 3})):
            self.assertEqual(Counter(row[1] for row in coefficient_rows(roots, label)), wanted)
            for residue, charge, _ in coefficient_rows(roots, label):
                self.assertEqual(residue, 0 if abs(charge) == 1 else (1 if label == "4" else 2))
        adjoint = coefficient_rows(roots, "15")
        self.assertEqual(sum(row[0] % 3 == 0 for row in adjoint), 9)
        self.assertEqual(sum(row[0] % 3 != 0 for row in adjoint), 6)
        self.assertEqual(Counter(dot(QY, r) for r in halves), Counter(dot(QY, tuple(-x for x in r)) for r in halves))
        for root in roots:
            self.assertEqual(dot(QY, root).denominator, 1)
        self.assertTrue(any(dot(QY, root) == 4 for root in cross))
        self.assertNotEqual(char_mul(CHI, 4), char_mul(CHI, -3))
        self.assertEqual(char_mul((F(1, 7), F(0)), 4), char_mul((F(1, 7), F(0)), -3))
        self.assertEqual(len(d5)+len(a3)+len(cross)+len(halves)+8, 248)

    def test_exact_pole_counts_all_spins_and_complete_physical_totals(self):
        roots = e8_roots()
        self.assertEqual([pole_bound(a) for a in (0, 1, 2)], [0, 0, 0])
        nontrivial_line = CHI
        for eta in SPINS:
            trivial = eta == ZERO
            totals, _ = new_population(roots, eta)
            expected = 87 if trivial else 63
            self.assertEqual(totals, (expected, 9, 9))
            self.assertEqual(totals[0]+totals[2], 96 if trivial else 72)
            self.assertEqual(old_population(roots, eta), (136 if trivial else 112, 12))
            physical_rows = []
            for j, k, label in BLOCKS:
                for residue, _, _ in coefficient_rows(roots, label):
                    nc, _, ng = new_counts(j, k, char_mul(CHI, residue), eta)
                    physical_rows.extend((("chiral", nc), ("gaugino", ng)))
            full_physical = sum(count for _, count in physical_rows)
            without_c3 = sum(count for slot, count in physical_rows if slot != "gaugino")
            self.assertEqual(full_physical, 96 if trivial else 72)
            self.assertEqual(without_c3, expected)
            self.assertNotEqual(without_c3, full_physical)
            self.assertEqual(new_counts(F(2), F(0), nontrivial_line, eta), (2, 0, 0))
            self.assertEqual(new_counts(F(0), F(2), char_mul(nontrivial_line, -1), eta), (2, 0, 0))
        self.assertEqual(h0(2, nontrivial_line, ZERO), 0)
        self.assertEqual(h0(2, nontrivial_line, ZERO, wrong_endpoint=True), 1)
        with self.assertRaises(ValueError):
            pole_bound(F(1, 2))

    def test_charged_roster_pairs_and_massless_up_control(self):
        roots = e8_roots()
        for eta in SPINS:
            trivial = eta == ZERO
            totals, roster = new_population(roots, eta)
            wanted = {"neutral": 19 if trivial else 15,
                      "color_adj": 24 if trivial else 8,
                      "up+": 12, "up-": 12, "down+": 6, "down-": 6,
                      "lepton+": 4 if trivial else 2, "lepton-": 4 if trivial else 2}
            self.assertEqual(+roster, Counter(wanted))
            self.assertEqual(sum(roster.values()), totals[0])
            for plus, minus, dimension, multiplicity in (("up+", "up-", 3, 4),
                                                        ("down+", "down-", 3, 2),
                                                        ("lepton+", "lepton-", 1, 4 if trivial else 2)):
                self.assertEqual(roster[plus], roster[minus])
                self.assertEqual(roster[plus]//dimension, multiplicity)
                self.assertEqual(roster[plus] % dimension, 0)
            no_minus_triple = [row for row in BLOCKS if row != (F(0), F(2), "6")]
            missing, bad_roster = new_population(roots, eta, no_minus_triple)
            self.assertNotEqual(missing[0], totals[0])
            self.assertEqual(bad_roster["up+"], 6)
            doubled, doubled_roster = new_population(roots, eta, BLOCKS+tuple(row for row in BLOCKS if row[2] == "bar4"))
            self.assertNotEqual(doubled[0], totals[0])
            self.assertNotEqual(doubled_roster["down+"], doubled_roster["down-"])
            self.assertEqual(old_population(roots, eta)[1]-totals[1], 3)


if __name__ == "__main__":
    raise SystemExit("UNRUN scientific controls: require independent review and strict prospective admission")
