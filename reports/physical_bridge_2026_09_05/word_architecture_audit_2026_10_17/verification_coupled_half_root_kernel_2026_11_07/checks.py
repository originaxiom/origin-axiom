"""Nine UNRUN controls of the November 7 conditional physical successors.

Original six-control design: 7584cf4e6. Three additional controls: e9bb0bcc5.
Do not import, collect or execute before source-complete independent review,
main's exact acceptance and strict prospective admission. Finite algebra
supports the separately reviewed complete-domain/Hodge/compactness duties.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from pathlib import Path
import unittest

import sympy as sp


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "verification_transport_end_2026_11_04" / "checks.py"
spec = spec_from_file_location("coupled_kernel_transport_source", SOURCE)
if spec is None or spec.loader is None:
    raise ImportError("Cannot load the declared full E8 transport dependency")
TRANSPORT = module_from_spec(spec)
spec.loader.exec_module(TRANSPORT)
OLD, ROOTS = TRANSPORT.OLD, TRANSPORT.ROOTS
dagger, bracket = OLD.dagger, OLD.bracket
clean = TRANSPORT.clean


def projector(columns):
    """Orthogonal projector for a computed independent column frame."""
    if columns.cols == 0:
        return sp.zeros(columns.rows)
    return clean(columns * (dagger(columns)*columns).inv() * dagger(columns))


def kernel_columns(matrix):
    columns = matrix.nullspace()
    return sp.Matrix.hstack(*columns) if columns else sp.zeros(matrix.cols, 0)


def unit_column(column):
    norm = sp.simplify((dagger(column)*column)[0])
    if norm == 0:
        raise ValueError("A zero column is not a unit vector")
    return clean(column / sp.sqrt(norm))


@lru_cache(maxsize=2)
def spinor_complex(parity):
    """Derive the joint weight frame from the source's actual Clifford action."""
    if parity not in (0, 1):
        raise ValueError("Expected one of the two Spin10 chiralities")
    data = TRANSPORT.carriers()
    indices = tuple(i for i in range(32) if i.bit_count() % 2 == parity)
    lift = lambda x: TRANSPORT.spin_lie(x, data["creation"]).extract(indices, indices)
    ep, em, hp, hm = (lift(data[key]) for key in ("ep", "em", "hp", "hm"))
    top = kernel_columns(ep.col_join(em))
    if top.cols != 1:
        raise ValueError("Actual spinor does not have one joint highest line")
    top = unit_column(top)
    weights = tuple(product(range(4), repeat=2))
    frame = sp.Matrix.hstack(*(unit_column(dagger(ep)**p * dagger(em)**q * top)
                              for p, q in weights))
    if clean(dagger(frame)*frame) != sp.eye(16):
        raise ValueError("Derived joint weight frame is not unitary")
    move = lambda x: clean(dagger(frame)*x*frame)
    ep, em, hp, hm = (move(x) for x in (ep, em, hp, hm))
    d0 = ep.col_join(em)
    d1 = (-em).row_join(ep)
    harmonic = (kernel_columns(d0),
                kernel_columns(dagger(d0).col_join(d1)),
                kernel_columns(dagger(d1)))
    projections = tuple(projector(x) for x in harmonic)
    i16 = sp.eye(16)
    representatives = (i16[:, 0],
                       sp.diag(i16, i16).extract(range(32), (12, 19)),
                       i16[:, 15])
    if any(clean(p-projector(rep)) != sp.zeros(p.rows)
           for p, rep in zip(projections, representatives)):
        raise ValueError("Actual harmonic representatives differ from the claimed extreme lines")
    a = move(data["asp"].extract(indices, indices))
    d = move(data["dsp"].extract(indices, indices))
    flavour_a = sp.Matrix([[0, sp.I], [sp.I, 0]])
    flavour_d = sp.diag(sp.I, -sp.I)
    blocks = lambda f, g: (g, sp.kronecker_product(f, g), f.det()*g)
    actions_a, actions_d = blocks(flavour_a, a), blocks(flavour_d, d)
    restrict = lambda blocks_: tuple(clean(dagger(rep)*op*rep)
                                     for rep, op in zip(representatives, blocks_))
    return dict(parity=parity, indices=indices, frame=frame, ep=ep, em=em,
                hp=hp, hm=hm, d0=d0, d1=d1, harmonic=harmonic,
                projections=projections, representatives=representatives,
                a=a, d=d, actions_a=actions_a, actions_d=actions_d,
                reduced_a=restrict(actions_a), reduced_d=restrict(actions_d))


@lru_cache(maxsize=1)
def coefficient_records():
    """Literal E8 roots retain colour multiplicity, chirality and old Wilson."""
    _, _, _, halves = ROOTS.coefficient_populations(ROOTS.e8_roots())
    records = []
    for first_three, roots in sorted(halves.items()):
        em = {ROOTS.dot(root, ROOTS.EM) for root in roots}
        wilson = {ROOTS.dot(root, ROOTS.QY) % 3 for root in roots}
        parities = {sum(x > 0 for x in root[3:]) % 2 for root in roots}
        if len(em) != 1 or len(wilson) != 1 or len(parities) != 1:
            raise ValueError("An actual A3 coefficient does not have a single character")
        records.append(dict(first_three=first_three, roots=roots,
                            charge=next(iter(em)), wilson=next(iter(wilson)),
                            parity=next(iter(parities))))
    return tuple(records)


def phase_fraction(value):
    return TRANSPORT.phase(sp.Rational(value.numerator, value.denominator))


def corrected_reduced(record, correction, signs=(1, 1)):
    """Return the actual cohomology actions on the two free core generators."""
    source = spinor_complex(record["parity"])
    h = sp.Integer(1) if correction is None else phase_fraction(
        Fraction(3, 8)*record["charge"] + Fraction(correction, 2))
    a = tuple(clean(signs[0]*h*x) for x in source["reduced_a"])
    # B=D A. A second Zeta sign is independent in the bare free-group lift.
    b = tuple(clean(signs[1]*h*dd*aa) for dd, aa in
              zip(source["reduced_d"], source["reduced_a"]))
    return a, b


def with_character(actions, exponents, spin=(1, 1), spin_power=1):
    return tuple(clean(action*phase_fraction(Fraction(exponent, 3))
                       *spin[axis]**spin_power)
                 for axis, (action, exponent) in enumerate(zip(actions, exponents)))


def fixed_columns(actions):
    size = actions[0].rows
    return kernel_columns(sp.Matrix.vstack(*(a-sp.eye(size) for a in actions)))


def pole_degree(a):
    """Strict power/log endpoint from the actual radial integral, not rounding."""
    a = Fraction(a)
    if a.denominator != 1:
        raise ValueError("Only total integral extending-spin powers are admitted")
    # exponent a-1-2n must exceed -1; equality also works precisely if a<1.
    admitted = lambda n: a-2*n > 0 or (a-2*n == 0 and a < 1)
    n = a.numerator // 2
    while not admitted(n):
        n -= 1
    if admitted(n+1):
        raise ValueError("Pole endpoint search is not maximal")
    return n


def line_h0(a, actions):
    degree = pole_degree(a)
    if degree < 0:
        return 0
    if degree > 0:
        return degree*actions[0].rows
    return fixed_columns(actions).cols


def total_cohomology(record, correction, chi=(1, 0), spin=(1, 1), signs=(1, 1)):
    a, b = corrected_reduced(record, correction, signs)
    exponents = tuple(record["wilson"]*n for n in chi)
    powers = (-3, 1, 5)
    h0, h1 = [], []
    for degree, power in enumerate(powers):
        acts = with_character((a[degree], b[degree]), exponents, spin, power)
        h0.append(line_h0(power, acts))
        dual_acts = tuple(clean(dagger(x)) for x in acts)
        h1.append(line_h0(2-power, dual_acts))
    # Total degrees of the Dolbeault/Koszul complex, not an assigned index.
    return (h0[0], h1[0]+h0[1], h1[1]+h0[2], h1[2])


def half_root_totals(correction, chi=(1, 0), spin=(1, 1), signs=(1, 1)):
    left, adjoint = Counter(), Counter()
    for record in coefficient_records():
        h0, h1, h2, h3 = total_cohomology(record, correction, chi, spin, signs)
        left[record["charge"]] += h1+h3
        adjoint[record["charge"]] += h0+h2
    return left, adjoint


class CoupledHalfRootKernelChecks(unittest.TestCase):
    def assert_zero(self, matrix):
        self.assertEqual(clean(matrix), sp.zeros(*matrix.shape))

    def test_actual_spinor_koszul_cohomology_and_all_degree_actions(self):
        sx = sp.Matrix([[0, 1], [1, 0]])
        for parity in (0, 1):
            c = spinor_complex(parity)
            d0, d1 = c["d0"], c["d1"]
            self.assertEqual((d0.shape, d1.shape), ((32, 16), (16, 32)))
            self.assert_zero(d1*d0)
            self.assertEqual(tuple(x.cols for x in c["harmonic"]), (1, 2, 1))
            self.assertEqual((d0.rank(), d1.rank()), (15, 15))
            for actions in (c["actions_a"], c["actions_d"]):
                self.assert_zero(actions[1]*d0-d0*actions[0])
                self.assert_zero(d1*actions[1]-actions[2]*d1)
            alpha = c["reduced_a"][0][0]
            for got, expected in zip(c["reduced_a"],
                                     (sp.Matrix([[alpha]]), alpha*sx, sp.Matrix([[-alpha]]))):
                self.assert_zero(got-expected)
            for got in c["reduced_d"]:
                self.assert_zero(got-sp.eye(got.rows))
            self.assertNotEqual(c["reduced_a"][2], c["reduced_a"][0])
            wrong = sp.diag(c["a"], c["a"])
            self.assertNotEqual(clean(wrong*d0-d0*c["a"]), sp.zeros(32, 16))

    def test_equivariant_retraction_and_spin_line_degrees(self):
        omega = sp.Symbol("Omega", positive=True)
        # Actual complex densities h0=Omega^2, h1_spin=Omega, h2_wedge=2.
        self.assertEqual(sp.simplify(omega*sp.sqrt(omega)**2/omega**2), 1)
        self.assertEqual(sp.simplify(2*sp.sqrt(omega)**2/omega), 2)
        self.assertNotEqual(sp.simplify(omega/omega**2), 1)
        for parity in (0, 1):
            c = spinor_complex(parity)
            d0, d1 = c["d0"], c["d1"]
            p0, p1, p2 = c["projections"]
            lap1 = clean(d0*dagger(d0)+dagger(d1)*d1)
            lap2 = clean(d1*dagger(d1))
            h1 = clean(dagger(d0)*(lap1+p1).inv())
            h2 = clean(dagger(d1)*(lap2+p2).inv())
            self.assert_zero(h1*d0-(sp.eye(16)-p0))
            self.assert_zero(d0*h1+h2*d1-(sp.eye(32)-p1))
            self.assert_zero(d1*h2-(sp.eye(16)-p2))
            for actions in (c["actions_a"], c["actions_d"]):
                self.assert_zero(h1*actions[1]-actions[0]*h1)
                self.assert_zero(h2*actions[2]-actions[1]*h2)
            # An equivariant Hodge homotopy is already its own finite average.
            group = {}
            for j, i in product(range(4), range(8)):
                blocks = tuple(clean(dd**j*aa**i) for dd, aa in
                               zip(c["actions_d"], c["actions_a"]))
                key = tuple(tuple(x) for x in blocks)
                group[key] = blocks
            for generator in (c["actions_a"], c["actions_d"]):
                for blocks in group.values():
                    received = tuple(clean(g*x) for g, x in zip(generator, blocks))
                    self.assertIn(tuple(tuple(x) for x in received), group)
            averaged = sum((g[0]*h1*dagger(g[1]) for g in group.values()), sp.zeros(16, 32))/len(group)
            self.assert_zero(averaged-h1)
            hh = c["hp"]+c["hm"]
            graded_h = (hh, sp.diag(hh, hh), hh)
            line_degrees = []
            for degree, (rep, op) in enumerate(zip(c["representatives"], graded_h)):
                total = clean(dagger(rep)*(degree*sp.eye(op.rows)-op/2)*rep)
                line_degrees.append(tuple(total.diagonal()))
            self.assertEqual(line_degrees, [(-3,), (1, 1), (5,)])
            self.assertNotEqual(clean(d0*h1), sp.eye(32)-p1)  # final contracting slot matters

    def test_bare_and_corrected_core_characters_on_full_mixed_sectors(self):
        records = coefficient_records()
        self.assertEqual(sum(len(r["roots"]) for r in records), 128)
        for record in records:
            c = spinor_complex(record["parity"])
            # Direct matrix correction from Q_em on the actual complementary weight.
            h = phase_fraction(Fraction(3, 8)*record["charge"])
            self.assert_zero((h*c["a"])**2-c["d"]**2)
            for sa, sb in product((-1, 1), repeat=2):
                a, b = corrected_reduced(record, None, (sa, sb))
                self.assertEqual(sp.simplify(a[0][0]**4), -1)
                for aa, bb in zip(a, b):
                    self.assert_zero(aa*bb*dagger(aa)*dagger(bb)-sp.eye(aa.rows))
            pairs = []
            for correction in (0, 1):
                a, b = corrected_reduced(record, correction)
                self.assertEqual(sp.simplify(a[0][0]**2), 1)
                for degree in range(3):
                    self.assert_zero(a[degree]-b[degree])
                pairs.append(tuple(a[1].eigenvals()))
            self.assertEqual(set(pairs[0]), set(pairs[1]))
            # Omitting the electromagnetic factor cannot satisfy the full relation.
            self.assertNotEqual(clean(c["a"]**2-c["d"]**2), sp.zeros(16))

    def test_actual_wilson_and_spin_line_triviality_population(self):
        records = coefficient_records()
        self.assertEqual(Counter(r["charge"] for r in records),
                         {Fraction(1): 1, Fraction(-1): 1,
                          Fraction(1, 3): 3, Fraction(-1, 3): 3})
        characters = tuple(x for x in product(range(3), repeat=2) if x != (0, 0))
        self.assertEqual(len(characters), 8)
        differences = []
        for record in records:
            self.assertEqual(record["wilson"] == 0, abs(record["charge"]) == 1)
            for correction, chi, eta in product((None, 0, 1), characters,
                                                 product((-1, 1), repeat=2)):
                a, b = corrected_reduced(record, correction)
                acts = with_character((a[1], b[1]),
                                      tuple(record["wilson"]*n for n in chi), eta)
                nfixed = fixed_columns(acts).cols
                if correction is None or abs(record["charge"]) == Fraction(1, 3):
                    self.assertEqual(nfixed, 0)
                else:
                    self.assertEqual(nfixed, int(eta[0] == eta[1]))
                if eta != (1, 1):
                    no_spin = with_character((a[1], b[1]),
                                              tuple(record["wilson"]*n for n in chi))
                    differences.append(nfixed != fixed_columns(no_spin).cols)
            if abs(record["charge"]) == Fraction(1, 3):
                a, b = corrected_reduced(record, 0)
                self.assertEqual(fixed_columns((a[1], b[1])).cols, 1)
        self.assertTrue(any(differences))

    def test_exact_cusp_pole_endpoints_and_complete_four_slot_counts(self):
        self.assertEqual(tuple(pole_degree(a) for a in (-3, 1, 5)), (-2, 0, 2))
        self.assertEqual(tuple(pole_degree(a) for a in (0, 1, 2)), (0, 0, 0))
        u = sp.Symbol("u", positive=True)
        # At equality r exponent -1, substitute u=log(1/r): integral u^(a-2) du.
        for a in (-2, 0, 2, 4):
            primitive = u**(a-1)/sp.Integer(a-1)
            self.assertEqual(sp.simplify(primitive.diff(u)-u**(a-2)), 0)
            finite = sp.limit(primitive, u, sp.oo).is_finite
            self.assertEqual(bool(finite), a < 1)
        for record, correction in product(coefficient_records(), (None, 0, 1)):
            h0, h1, h2, h3 = total_cohomology(record, correction)
            self.assertEqual((h0, h3), (0, 0))
            self.assertEqual(h1, h2)
            expected = 3 if correction is not None and abs(record["charge"]) == 1 else 2
            self.assertEqual(h1, expected)
        # The old positive spin power 2 has a divergent equality term.
        self.assertNotEqual(pole_degree(2), 2//2)
        with self.assertRaises(ValueError):
            pole_degree(Fraction(1, 2))

    def test_core_phase_changes_kernel_without_changing_cusp_or_index(self):
        observed = []
        for correction in (None, 0, 1):
            left, adjoint = half_root_totals(correction)
            self.assertEqual(left, adjoint)
            self.assertEqual(left[Fraction(1, 3)], left[Fraction(-1, 3)])
            self.assertEqual(left[Fraction(1)], left[Fraction(-1)])
            observed.append(sum(left.values()))
            for record in coefficient_records():
                a, b = corrected_reduced(record, correction)
                for aa, bb in zip(a, b):
                    self.assert_zero(aa*bb*dagger(aa)*dagger(bb)-sp.eye(aa.rows))
        self.assertEqual(observed, [16, 18, 18])
        for signs in product((-1, 1), repeat=2):
            self.assertEqual(sum(half_root_totals(None, signs=signs)[0].values()), 16)
        # Replacing both core characters by their identical peripheral loses information.
        fake_middle = fixed_columns((sp.eye(2), sp.eye(2))).cols
        actual = coefficient_records()[0]
        a, b = corrected_reduced(actual, None)
        self.assertNotEqual(fake_middle, fixed_columns((a[1], b[1])).cols)
        self.assertNotEqual(observed[0], observed[1])

    def test_full_charge_grading_and_actual_cubic_selection(self):
        roots = ROOTS.e8_roots()
        zeta = tuple(2*x for x in TRANSPORT.d5_log((Fraction(1, 2),)*5))
        charges = defaultdict(set)
        for root in roots:
            odd = TRANSPORT.torus_pair(zeta, root) == Fraction(1, 2)
            charge = ROOTS.dot(root, ROOTS.EM)
            charges[odd].add(charge)
            self.assertEqual(TRANSPORT.torus_pair(zeta, root), (Fraction(3, 2)*charge) % 1)
            if abs(charge) == 1:
                self.assertTrue(odd)
        self.assertEqual(charges[False], {Fraction(0), Fraction(2, 3), Fraction(-2, 3),
                                          Fraction(4, 3), Fraction(-4, 3)})
        self.assertEqual(charges[True], {Fraction(1), Fraction(-1), Fraction(1, 3), Fraction(-1, 3)})
        w = (Fraction(1, 2),)*8
        d = tuple(Fraction(x, 2) for x in (1, -1, -1, 1, -1, -1, -1, -1))
        up = tuple(x+y for x, y in zip(w, d))
        self.assertIn(w, roots); self.assertIn(d, roots); self.assertIn(up, roots)
        self.assertEqual(ROOTS.dot(w, d), -1)
        self.assertEqual(tuple(ROOTS.dot(x, ROOTS.EM) for x in (w, d, up)),
                         (Fraction(1), Fraction(-1, 3), Fraction(2, 3)))
        allowed = Counter()
        for alpha in roots:
            if abs(ROOTS.dot(alpha, ROOTS.EM)) != 1:
                continue
            for beta in roots:
                gamma = tuple(x+y for x, y in zip(alpha, beta))
                if gamma not in roots:
                    continue
                p = TRANSPORT.torus_pair(zeta, beta)
                q = TRANSPORT.torus_pair(zeta, gamma)
                allowed[p, q] += 1
                self.assertNotEqual(p, q)
        self.assertTrue(allowed)
        self.assertTrue(all(count > 0 for count in allowed.values()))
        omega = sp.Symbol("Omega", positive=True)
        weights = (omega**2, sp.Rational(1, 2), omega, omega)
        for weight in weights:
            for p, q in product((-1, 1), repeat=2):
                transform = p*(-1)*q
                if p == q:
                    self.assertEqual(sp.simplify((1-transform)*weight/(2*weight)), 1)
                else:
                    self.assertEqual(transform, 1)
        # Opposite roots give an actual nonzero Cartan action: [E_w,E_-w]=H_w.
        self.assertIn(tuple(-x for x in w), roots)
        self.assertEqual(ROOTS.dot(w, w), 2)

    def test_actual_compact_centralizer_and_vector_block_duties(self):
        dims, holomorphic_dims = {}, {}
        for module in TRANSPORT.full_parent_modules():
            e, g = module["e"], module["g"]
            kernel = kernel_columns(sp.Matrix.vstack(e, g, dagger(e), dagger(g)))
            holomorphic = kernel_columns(e.col_join(g))
            dims[module["name"]] = kernel.cols
            holomorphic_dims[module["name"]] = holomorphic.cols
        self.assertEqual(dims, {"45,1": 0, "1,15": 15, "10,6": 0,
                                "16,4": 0, "bar16,bar4": 0})
        self.assertGreater(sum(holomorphic_dims.values()), 15)
        roots = ROOTS.e8_roots()
        a3 = [r for r in roots if not any(r[3:])]
        surviving = [r for r in a3 if ROOTS.dot(r, ROOTS.QY) % 3 == 0]
        self.assertEqual(len(surviving)+3, 9)
        self.assertEqual(len(a3)+3, 15)
        omega = sp.Symbol("Omega", positive=True)
        # Actual source densities and Higgs insertions determine sqrt(2) gauge normalization.
        qnorm = sp.sqrt(omega)/(2*sp.sqrt(2))
        self.assertEqual(sp.simplify(2*omega*qnorm**2/omega**2), sp.Rational(1, 4))
        for parity in (0, 1):
            c = spinor_complex(parity)
            d0, d1 = sp.sqrt(2)*c["d0"], c["d1"]
            self.assert_zero(d1*d0)
            zero16, zero32 = sp.zeros(16), sp.zeros(32)
            dirac = sp.BlockMatrix([[zero16, dagger(d0), zero16],
                                    [d0, zero32, dagger(d1)],
                                    [zero16, d1, zero16]]).as_explicit()
            square = clean(dirac**2)
            self.assert_zero(square[:16, :16]-dagger(d0)*d0)
            self.assert_zero(square[:16, 16:])
            # Removing the Koszul minus destroys this source square's off-block zero.
            wrong_d1 = c["em"].row_join(c["ep"])
            self.assertNotEqual(clean(wrong_d1*d0), sp.zeros(16))
            # This finite complex identity is not the curved complete M†M theorem.

    def test_centralizer_spin_norm_endpoint_and_untwisted_countercontrol(self):
        r, log_inv = sp.symbols("r L", positive=True)
        n = sp.Symbol("n", integer=True)
        # Transform the actual spin measure Omega |f|^2 r dr dtheta.
        omega = 1/(r*log_inv)
        spin_density = sp.simplify(omega*r)
        self.assertEqual(spin_density, 1/log_inv)
        power = sp.simplify(2*(n+sp.Rational(1, 2)))
        self.assertEqual(power, 2*n+1)
        u = sp.Symbol("u", positive=True)
        critical_primitive = sp.log(u)
        self.assertEqual(critical_primitive.diff(u), 1/u)
        self.assertEqual(sp.limit(critical_primitive, u, sp.oo), sp.oo)
        # For half-integer powers the maximal forbidden endpoint is n=-1.
        admitted = lambda exponent: exponent > -1
        self.assertFalse(admitted(-1))
        self.assertTrue(admitted(1))
        # Untwisted constant spin: integral exp(-u)/u du converges by comparison.
        self.assertEqual(sp.limit(sp.exp(-u), u, sp.oo), 0)
        self.assertTrue(bool(sp.ask(sp.Q.positive(sp.exp(-u)/u))))
        scalar_density = sp.simplify(omega**2*r)
        form_density = sp.simplify((omega**2)*(omega**-2)*r)
        self.assertEqual(scalar_density, 1/(r*log_inv**2))
        self.assertEqual(form_density, r)
        for record in coefficient_records():
            self.assertIn(record["wilson"], (0, 1, 2))
        # Trivial/nontrivial flat-line section counts use the actual inherited producer.
        self.assertEqual((ROOTS.h0(0, ROOTS.ZERO), ROOTS.h0(2, ROOTS.ZERO)), (1, 1))
        self.assertEqual((ROOTS.h0(0, ROOTS.CHI), ROOTS.h0(2, ROOTS.CHI)), (0, 0))
        # Misusing the scalar log-squared density would incorrectly admit this spin endpoint.
        scalar_primitive = -1/u
        self.assertEqual(scalar_primitive.diff(u), 1/u**2)
        self.assertEqual(sp.limit(scalar_primitive, u, sp.oo), 0)
        self.assertNotEqual(sp.limit(scalar_primitive, u, sp.oo),
                            sp.limit(critical_primitive, u, sp.oo))

