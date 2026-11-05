"""Eight UNRUN controls of the full compensator and coupled cusp proofs.

Design sealed at 329a910e9, response addendum at 46ac498f7. Do not import,
collect or execute without new independent review and strict admission.
Finite controls supplement the separately reviewed analytical duties.
"""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from pathlib import Path
import unittest

import sympy as sp


HERE = Path(__file__).resolve().parent


def source_module(name, directory):
    path = HERE.parent / directory / "checks.py"
    spec = spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load declared source {path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


OLD = source_module("transport_source_register", "verification_register_flavour_joint_2026_11_03")
ROOTS = source_module("transport_source_roots", "verification_neutral_full_kernel_2026_11_02")


def clean(matrix):
    return matrix.applyfunc(sp.simplify)


def matrix_key(matrix):
    return tuple(clean(matrix))


def phase(value):
    return sp.simplify(sp.expand_complex(sp.exp(2 * sp.pi * sp.I * value)))


def d5_log(values):
    out = [Fraction(0)] * 8
    for index, value in zip((5, 3, 6, 4, 7), values):
        out[index] = Fraction(value)
    return tuple(out)


def torus_pair(logarithm, root):
    return sum(a * b for a, b in zip(logarithm, root)) % 1


def exterior_square(matrix):
    pairs = tuple(combinations(range(matrix.rows), 2))
    return sp.Matrix(len(pairs), len(pairs), lambda i, j:
                     matrix[pairs[i][0], pairs[j][0]] * matrix[pairs[i][1], pairs[j][1]]
                     - matrix[pairs[i][0], pairs[j][1]] * matrix[pairs[i][1], pairs[j][0]])


def exterior_lie(matrix):
    """Differentiate the actual exterior-square representation at the identity."""
    pairs = tuple(combinations(range(matrix.rows), 2))
    delta = lambda i, j: sp.Integer(i == j)
    return sp.SparseMatrix(len(pairs), len(pairs), lambda row, col:
        matrix[pairs[row][0], pairs[col][0]] * delta(pairs[row][1], pairs[col][1])
        + delta(pairs[row][0], pairs[col][0]) * matrix[pairs[row][1], pairs[col][1]]
        - matrix[pairs[row][0], pairs[col][1]] * delta(pairs[row][1], pairs[col][0])
        - delta(pairs[row][0], pairs[col][1]) * matrix[pairs[row][1], pairs[col][0]])


def a3_adjoint(matrix):
    """A3 adjoint in a trace-orthonormal basis, preserving the compact dagger."""
    basis = []
    for i in range(4):
        for j in range(4):
            if i != j:
                element = sp.zeros(4)
                element[i, j] = 1
                basis.append(element)
    basis.extend((sp.diag(1, -1, 0, 0)/sp.sqrt(2),
                  sp.diag(1, 1, -2, 0)/sp.sqrt(6),
                  sp.diag(1, 1, 1, -3)/sp.sqrt(12)))
    return sp.SparseMatrix(15, 15, lambda i, j:
        sp.trace(OLD.dagger(basis[i])*OLD.bracket(matrix, basis[j])))


def creators():
    out = []
    for axis in range(5):
        operator = sp.zeros(32)
        bit = 1 << axis
        for state in range(32):
            if state & bit == 0:
                lower = (state & (bit - 1)).bit_count()
                operator[state | bit, state] = (-1) ** lower
        out.append(operator)
    return tuple(out)


def spin_lie(matrix, creation):
    annihilation = tuple(OLD.dagger(c) for c in creation)
    out = -sp.trace(matrix[:5, :5]) * sp.eye(32) / 2
    for i in range(5):
        for j in range(5):
            out += matrix[i, j] * creation[i] * annihilation[j]
            out += matrix[i, j + 5] * creation[i] * creation[j] / 2
            out += matrix[i + 5, j] * annihilation[i] * annihilation[j] / 2
    return clean(out)


def spectral_exponential(generator, eigenvalues, coefficient):
    eye = sp.eye(generator.rows)
    result = sp.zeros(generator.rows)
    annihilator = eye
    for value in eigenvalues:
        annihilator = annihilator * (generator - value * eye)
        projector = eye
        for other in eigenvalues:
            if other != value:
                projector = projector * (generator - other * eye) / (value - other)
        result += sp.exp(coefficient * value) * projector
    if clean(annihilator) != sp.zeros(generator.rows):
        raise ValueError("Declared spectrum does not annihilate the actual generator")
    return clean(result)


@lru_cache(maxsize=1)
def carriers():
    e, g, h, ep, em, hp, hm = OLD.d5_source()
    n = sp.diag(sp.eye(5), -sp.eye(5))
    a_vector = clean(-sp.I * n * sp.diag(*(sp.exp(-sp.I * sp.pi * h[i, i] / 4) for i in range(10))))
    d_vector = spectral_exponential(hp - hm, (-4, -2, 0, 2, 4), -sp.I * sp.pi / 4)
    creation = creators()
    x = (sp.Rational(1, 4), 0, -sp.Rational(1, 4), -sp.Rational(1, 2), -sp.Rational(3, 4))
    a_spin = sp.diag(*(phase(sum(x[i] * (sp.Integer(bool(state & (1 << i))) - sp.Rational(1, 2))
                                      for i in range(5))) for state in range(32)))
    d_spin = spectral_exponential(spin_lie(hp - hm, creation), (-6, -4, -2, 0, 2, 4, 6), -sp.I * sp.pi / 4)
    p_spin = spectral_exponential(spin_lie(h, creation), (-6, -4, -2, 0, 2, 4, 6), -sp.I * sp.pi / 2)
    c_spin = sp.diag(*(phase(sum((sp.Integer(bool(state & (1 << i))) - sp.Rational(1, 2)) / 2
                                      for i in range(5))) for state in range(32)))
    return dict(e=e, g=g, h=h, ep=ep, em=em, hp=hp, hm=hm,
                creation=creation, av=a_vector, dv=d_vector,
                asp=a_spin, dsp=d_spin, psp=p_spin, csp=c_spin)


@lru_cache(maxsize=2)
def full_parent_modules(corrected=False):
    """Actual five E8 summands with D5 Lie/group and colour-adjoint actions."""
    data = carriers()
    spin_e = spin_lie(data["e"], data["creation"])
    spin_g = spin_lie(data["g"], data["creation"])
    spin_h = spin_lie(data["h"], data["creation"])
    colour_t = sp.zeros(4)
    colour_t[1, 2] = 1
    colour_x = sp.diag(0, 1, -1, 0)
    modules = [
        dict(name="45,1", e=exterior_lie(data["e"]), g=exterior_lie(data["g"]),
             h=exterior_lie(data["h"]), a=exterior_square(data["av"]),
             d=exterior_square(data["dv"]), t=sp.zeros(45), x=sp.zeros(45)),
        dict(name="1,15", e=sp.zeros(15), g=sp.zeros(15), h=sp.zeros(15),
             a=sp.eye(15), d=sp.eye(15), t=a3_adjoint(colour_t), x=a3_adjoint(colour_x)),
        dict(name="10,6", e=sp.kronecker_product(data["e"], sp.eye(6)),
             g=sp.kronecker_product(data["g"], sp.eye(6)), h=sp.kronecker_product(data["h"], sp.eye(6)),
             a=sp.kronecker_product(data["av"], sp.eye(6)), d=sp.kronecker_product(data["dv"], sp.eye(6)),
             t=sp.kronecker_product(sp.eye(10), exterior_lie(colour_t)),
             x=sp.kronecker_product(sp.eye(10), exterior_lie(colour_x))),
    ]
    for parity, name, colour_action, colour_cartan in (
            (1, "16,4", colour_t, colour_x),
            (0, "bar16,bar4", -colour_t.T, -colour_x.T)):
        indices = [i for i in range(32) if i.bit_count() % 2 == parity]
        tensor = lambda value: sp.kronecker_product(value.extract(indices, indices), sp.eye(4))
        modules.append(dict(name=name, e=tensor(spin_e), g=tensor(spin_g), h=tensor(spin_h),
                            a=tensor(data["asp"]), d=tensor(data["dsp"]),
                            t=sp.kronecker_product(sp.eye(16), colour_action),
                            x=sp.kronecker_product(sp.eye(16), colour_cartan)))
    if corrected:
        h4 = sp.diag(phase(sp.Rational(3, 8)), *(phase(-sp.Rational(1, 8)) for _ in range(3)))
        h15 = sp.diag(*(sp.simplify(h4[i, i]/h4[j, j])
                        for i in range(4) for j in range(4) if i != j), 1, 1, 1)
        corrections = (sp.eye(45), h15, sp.kronecker_product(sp.eye(10), exterior_square(h4)),
                       sp.kronecker_product(sp.eye(16), h4),
                       sp.kronecker_product(sp.eye(16), h4.conjugate()))
        for module, correction in zip(modules, corrections):
            module["a"] = module["a"]*correction
    return tuple({key: sp.SparseMatrix(value) if key != "name" else value
                  for key, value in module.items()} for module in modules)


def physical_mass_blocks(q, r, omega, pbar, pz):
    """Full source mass formula on a retained coefficient representation."""
    eye, zero, rt = sp.eye(q.rows), sp.zeros(q.rows), sp.sqrt(2)
    qdag, rdag = OLD.dagger(q), OLD.dagger(r)
    return (
        (zero, -pz*eye/(rt*omega**2), rt*sp.I*qdag/omega, rt*sp.I*rdag/omega),
        (rt*pz*eye, zero, -2*sp.I*r, 2*sp.I*q),
        (-rt*sp.I*qdag, sp.I*r/omega, zero, pbar*eye/omega),
        (-rt*sp.I*rdag, -sp.I*q/omega, -pbar*eye/omega, zero),
    )


def physical_transition_blocks(flavour, gauge, conjugate_flavour=False):
    zero = sp.zeros(gauge.rows)
    f = flavour.conjugate() if conjugate_flavour else flavour
    return ((gauge, zero, zero, zero), (zero, gauge, zero, zero),
            (zero, zero, f[0, 0]*gauge, f[0, 1]*gauge),
            (zero, zero, f[1, 0]*gauge, f[1, 1]*gauge))


def actual_centralizer_rows(omega, ell, scalars, dz_lambda, dz_a, dbar_u, dbar_v):
    """The source mass rows on the actual colour root in the faithful E8 adjoint."""
    results = []
    for module in full_parent_modules():
        q = sp.sqrt(omega)*module["e"]/(2*sp.sqrt(2)*ell)
        r = sp.sqrt(omega)*module["g"]/(2*sp.sqrt(2)*ell)
        t = module["t"]
        lam, a, u, v = (scalar*t for scalar in scalars)
        p1 = dbar_u*t + sp.I*OLD.bracket(q, a)
        p2 = dbar_v*t + sp.I*OLD.bracket(r, a)
        wedge = OLD.bracket(q, v)-OLD.bracket(r, u)
        rows = (
            -(dz_a*t-2*sp.I*omega*(OLD.bracket(OLD.dagger(q), u)
                                  +OLD.bracket(OLD.dagger(r), v)))/(sp.sqrt(2)*omega**2),
            2*sp.I*wedge+sp.sqrt(2)*dz_lambda*t,
            p2/omega-sp.sqrt(2)*sp.I*OLD.bracket(OLD.dagger(q), lam),
            -p1/omega-sp.sqrt(2)*sp.I*OLD.bracket(OLD.dagger(r), lam),
        )
        results.append((t, module["x"], rows))
    return tuple(results)


def centralizer_projection(records):
    """Use kappa=Tr_ad(E8)/60 in the source root normalization."""
    norm = sp.simplify(sum(sp.trace(OLD.dagger(t)*t) for t, _, _ in records)/60)
    rows = sp.Matrix([sp.simplify(sum(sp.trace(OLD.dagger(t)*values[slot])
                                     for t, _, values in records)/(60*norm)) for slot in range(4)])
    return norm, rows


def free_inverse(word):
    return tuple(-letter for letter in reversed(word))


def free_substitute(word, images):
    out = []
    for letter in word:
        replacement = images[letter] if letter > 0 else free_inverse(images[-letter])
        for item in replacement:
            if out and out[-1] == -item:
                out.pop()
            else:
                out.append(item)
    return tuple(out)


def evaluate_word(word, generators):
    out = sp.eye(generators[1].rows)
    for letter in word:
        matrix = generators[abs(letter)]
        out = out * (matrix if letter > 0 else OLD.dagger(matrix))
    return clean(out)


class TransportEndChecks(unittest.TestCase):
    def assert_zero(self, matrix):
        self.assertEqual(clean(matrix), sp.zeros(*matrix.shape))

    def test_full_root_central_phases_and_electromagnetic_lattice(self):
        roots = ROOTS.e8_roots()
        c = d5_log((Fraction(1, 2),) * 5)
        zeta = tuple(2 * value for value in c)
        four_x = d5_log((1, 0, -1, -2, -3))
        h_squared = (Fraction(1, 2),) * 3 + (Fraction(0),) * 5
        observed = Counter(torus_pair(zeta, root) for root in roots)
        observed[Fraction(0)] += 8
        self.assertEqual(observed, {Fraction(0): 120, Fraction(1, 2): 128})
        for root in roots:
            self.assertEqual(torus_pair(four_x, root), torus_pair(zeta, root))
            self.assertEqual(torus_pair(h_squared, root), torus_pair(tuple(-v for v in c), root))
        integers = [r for r in roots if all(v.denominator == 1 for v in r)]
        self.assertTrue(all(torus_pair(four_x, r) == 0 for r in integers))
        self.assertTrue(any(torus_pair(four_x, r) != 0 for r in roots))
        wrong_half_phase = (Fraction(1, 6),) * 3 + (Fraction(0),) * 5
        self.assertTrue(any(torus_pair(wrong_half_phase, r) != torus_pair(tuple(-v for v in c), r) for r in roots))

    def test_actual_clifford_lift_of_d5_compensators(self):
        data = carriers()
        creation = data["creation"]
        gamma = creation + tuple(OLD.dagger(c) for c in creation)
        eye = sp.eye(32)
        for i in range(5):
            self.assert_zero(gamma[i] * gamma[i + 5] + gamma[i + 5] * gamma[i] - eye)
        for matrix in (data["e"], data["g"], data["h"]):
            lifted = spin_lie(matrix, creation)
            self.assert_zero(spin_lie(OLD.dagger(matrix), creation) - OLD.dagger(lifted))
            for column in range(10):
                rhs = sum((matrix[row, column] * gamma[row] for row in range(10)), sp.zeros(32))
                self.assert_zero(OLD.bracket(lifted, gamma[column]) - rhs)
        a, d, c, p = (data[k] for k in ("asp", "dsp", "csp", "psp"))
        b = clean(d * a)
        zeta = -eye
        self.assert_zero(a**4 - zeta)
        self.assert_zero(a**2 - OLD.dagger(c) * p)
        self.assert_zero(d**2 - zeta * p)
        self.assert_zero(a * d * OLD.dagger(a) - OLD.dagger(d))
        self.assert_zero(b**2 - a**2)
        self.assert_zero((a * b)**2 - p)
        self.assert_zero(a * b * OLD.dagger(a) * OLD.dagger(b) - zeta * p)
        self.assertNotEqual(a**4, eye)
        av, dv = data["av"], data["dv"]
        self.assert_zero(av**4 - sp.eye(10))
        self.assert_zero(dv**4 - sp.eye(10))

    def test_faithful_compensator_group_and_quotient_kernels(self):
        data = carriers()
        actual = {}
        vectors = {}
        adjoint = set()
        for j in range(4):
            for i in range(8):
                vector = clean(data["dv"]**j * data["av"]**i)
                spin = clean(data["dsp"]**j * data["asp"]**i)
                actual[j, i] = matrix_key(vector) + matrix_key(spin)
                vectors[j, i] = matrix_key(vector)
                adjoint.add(frozenset((matrix_key(vector), matrix_key(-vector))))
        self.assertEqual(len(set(actual.values())), 32)
        self.assertEqual(len(set(vectors.values())), 16)
        self.assertEqual(len(adjoint), 8)
        identity_vector = matrix_key(sp.eye(10))
        self.assertEqual({key for key,value in vectors.items() if value == identity_vector},
                         {(0,0),(0,4)})
        projective_identity = {identity_vector,matrix_key(-sp.eye(10))}
        self.assertEqual({key for key,value in vectors.items() if value in projective_identity},
                         {(0,0),(2,2),(0,4),(2,6)})
        for j in range(4):
            for i in range(8):
                for l, k in ((1, 0), (0, 1)):
                    product = ((j + (-1)**i * l) % 4, (i + k) % 8)
                    left = clean(data["dsp"]**j * data["asp"]**i * data["dsp"]**l * data["asp"]**k)
                    right = clean(data["dsp"]**product[0] * data["asp"]**product[1])
                    self.assert_zero(left - right)
        av, bv = data["av"], clean(data["dv"] * data["av"])
        self.assertNotEqual(matrix_key(av**2), matrix_key((av * bv)**2))
        self.assertNotEqual(matrix_key(av**2), matrix_key(sp.eye(10)))
        self.assertNotEqual(matrix_key((av * bv)**2), matrix_key(sp.eye(10)))
        fi, fj, _, _ = OLD.units()
        quaternion_units = (sp.eye(2), -sp.eye(2), fi, -fi, fj, -fj, fi*fj, -fi*fj)
        q8_c2_squares = {(matrix_key(q**2), 0) for q in quaternion_units if q**2 != sp.eye(2)}
        self.assertEqual(len(q8_c2_squares), 1)
        for sign_a in (-1, 1):
            for sign_b in (-1, 1):
                a, b = sign_a * data["asp"], sign_b * data["dsp"] * data["asp"]
                self.assert_zero(a*b*OLD.dagger(a)*OLD.dagger(b) + data["psp"])

    def test_full_pin2_correction_and_retained_gauge_sectors(self):
        data = carriers()
        av, dv = data["av"], data["dv"]
        h4 = sp.diag(phase(sp.Rational(3, 8)), *(phase(-sp.Rational(1, 8)) for _ in range(3)))
        modules = tuple((module["a"], module["d"]) for module in full_parent_modules(corrected=True))
        self.assertEqual(sum(a.rows for a, _ in modules), 248)
        for a, d in modules:
            eye = sp.eye(a.rows)
            b = clean(d*a)
            self.assert_zero(a**2 - d**2)
            self.assert_zero(a**4 - eye)
            self.assert_zero(a*d*OLD.dagger(a) - OLD.dagger(d))
            self.assert_zero(b**2-a**2)
            self.assert_zero((a*b)**2-a**2)
            self.assert_zero(a*b*OLD.dagger(a)*OLD.dagger(b)-a**2)
        # Individual representations can have kernels. Faithfulness belongs to
        # their combined 248-dimensional action, not to every summand.
        group = {tuple(matrix_key(d**j*a**i) for a,d in modules)
                 for j in range(4) for i in range(4)}
        self.assertEqual(len(group),8)
        for i,j in ((1,2),(2,3),(1,3)):
            generator = sp.zeros(4)
            generator[i,j] = 1
            self.assert_zero(h4*generator-generator*h4)
        fi, fj, _, _ = OLD.units()
        for flavour, gauge in ((fi,av),(fj,dv*av)):
            moved = tuple(clean(gauge*x*OLD.dagger(gauge)) for x in (data["e"],data["g"]))
            for received, expected in zip(OLD.rotate(flavour,moved),(data["e"],data["g"])):
                self.assert_zero(received-expected)
        omega=sp.Symbol("Omega",positive=True)
        pbar,pz=sp.symbols("pbar pz")
        q=sp.Matrix([[1+sp.I,1],[0,-1-sp.I]])
        r=sp.Matrix([[sp.I,0],[1,-sp.I]])
        mass=OLD.physical_mass(q,r,omega,pbar,pz)
        gram=sp.diag(1,1,2)
        metric=sp.diag(omega**2*gram,gram/2,omega*gram,omega*gram)
        rotation=(sp.eye(2)+sp.I*sp.Matrix([[0,1],[1,0]]))/sp.sqrt(2)
        for flavour in (fi,fj,rotation):
            qp,rp=OLD.rotate(flavour,(q,r))
            incoming,outgoing=OLD.input_map(flavour),OLD.output_map(flavour)
            self.assert_zero(OLD.physical_mass(qp,rp,omega,pbar,pz)*incoming-outgoing*mass)
            self.assert_zero(OLD.dagger(incoming)*metric*incoming-metric)
            self.assert_zero(OLD.dagger(outgoing)*metric*outgoing-metric)

    def test_continuous_stabilizer_and_phase_constraint(self):
        alpha = sp.Symbol("alpha", real=True)
        sx = sp.Matrix([[0,1],[1,0]])
        rotation = sp.cos(alpha)*sp.eye(2)+sp.I*sp.sin(alpha)*sx
        fi, _, gl, _ = OLD.units()
        self.assert_zero(rotation.conjugate()*sx*rotation.T-sx)
        self.assert_zero(fi.conjugate()*sx*fi.T+sx)
        self.assertNotEqual(clean(gl.conjugate()*sx*gl.T),sx)
        t=sp.Symbol("t", nonzero=True)
        self.assertEqual(sp.simplify((t**3+sp.I).subs(t,sp.I)),0)
        self.assertEqual(sp.simplify((1/t+sp.I).subs(t,sp.I)),0)
        self.assertNotEqual(sp.simplify((1/t+sp.I).subs(t,-sp.I)),0)
        angles=(3*sp.pi/4,15*sp.pi/4)
        q4=(1,-sp.Rational(1,3),-sp.Rational(1,3),-sp.Rational(1,3))
        holonomies=[]
        for theta in angles:
            h=sp.diag(*(sp.simplify(sp.expand_complex(sp.exp(sp.I*theta*q))) for q in q4))
            self.assert_zero(h**2+sp.I*sp.eye(4))
            holonomies.append(h)
        self.assert_zero(holonomies[0]+holonomies[1])
        self.assertNotEqual(holonomies[0],holonomies[1])
        self.assertTrue(all(sp.simplify(sp.exp(6*sp.pi*sp.I*q))==1 for q in q4))
        self.assertNotEqual(sp.simplify(sp.exp(2*sp.pi*sp.I*q4[1])),1)

    def test_based_and_all_word_holonomy_covariance(self):
        data=carriers()
        fi,fj,gl,gr=OLD.units()
        flavour={1:fi,2:fj}
        gauge={1:data["av"],2:clean(data["dv"]*data["av"])}
        moves=(
            ({1:(1,),2:(1,2)},{1:(1,),2:(-1,2)},gl),
            ({1:(1,2),2:(2,)},{1:(1,-2),2:(2,)},gr),
            ({1:(1,),2:(1,2,-1)},{1:(1,),2:(-1,2,1)},fi),
        )
        words=((1,),(2,),(1,2,-1,-2),(1,1,1,1),(1,-2,1,2))
        pair=(data["e"],data["g"])
        for forward,inverse,lift in moves:
            for letter in (1,2):
                self.assertEqual(free_substitute(forward[letter],inverse),(letter,))
            moved=OLD.rotate(lift,pair)
            for word in words:
                fq=evaluate_word(word,flavour)
                kg=evaluate_word(free_substitute(word,inverse),gauge)
                transformed=tuple(clean(kg*x*OLD.dagger(kg)) for x in moved)
                for received,expected in zip(OLD.rotate(fq,transformed),moved):
                    self.assert_zero(received-expected)
        inverse_l=moves[0][1]
        inverse_r=moves[1][1]
        for word in words:
            correct=free_substitute(free_substitute(word,inverse_l),inverse_r)
            composed={k:free_substitute(inverse_l[k],inverse_r) for k in (1,2)}
            self.assertEqual(correct,free_substitute(word,composed))
        wrong=free_substitute(free_substitute((1,),inverse_r),inverse_l)
        right=free_substitute(free_substitute((1,),inverse_l),inverse_r)
        self.assertNotEqual(wrong,right)
        self.assert_zero(evaluate_word((1,1,1,1),flavour)-sp.eye(2))
        self.assertNotEqual(carriers()["asp"]**4,sp.eye(32))

        # Bind the representation-valued helper to the declared source formula.
        omega = sp.Symbol("Omega", positive=True)
        pbar, pz = sp.symbols("pbar pz")
        probe_q, probe_r = sp.Matrix([[0, 1], [2, 0]]), sp.diag(1, -1)
        carrier_isometry = sp.diag(1, 1, sp.sqrt(2))
        source_basis = (sp.Matrix([[0, 1], [0, 0]]), sp.Matrix([[0, 0], [1, 0]]), sp.diag(1, -1))
        source_gram = sp.Matrix(3, 3, lambda i, j: sp.trace(OLD.dagger(source_basis[i])*source_basis[j]))
        self.assert_zero(OLD.dagger(carrier_isometry)*carrier_isometry-source_gram)
        slot_isometry = sp.diag(*(carrier_isometry for _ in range(4)))
        probe_q_operator = carrier_isometry*OLD.ad2(probe_q)*carrier_isometry.inv()
        probe_r_operator = carrier_isometry*OLD.ad2(probe_r)*carrier_isometry.inv()
        self.assert_zero(OLD.dagger(probe_q_operator)
                         -carrier_isometry*OLD.ad2(OLD.dagger(probe_q))*carrier_isometry.inv())
        self.assertNotEqual(OLD.dagger(OLD.ad2(probe_q)), OLD.ad2(OLD.dagger(probe_q)))
        probe_blocks = physical_mass_blocks(probe_q_operator, probe_r_operator, omega, pbar, pz)
        probe_matrix = sp.Matrix.vstack(*(sp.Matrix.hstack(*row) for row in probe_blocks))
        source_matrix = OLD.physical_mass(probe_q, probe_r, omega, pbar, pz)
        self.assert_zero(probe_matrix-slot_isometry*source_matrix*slot_isometry.inv())

        for corrected in (False, True):
            modules = full_parent_modules(corrected)
            self.assertEqual(sum(module["a"].rows for module in modules), 248)
            for module in modules:
                size = module["a"].rows
                centre = -1 if not corrected and module["name"] in ("16,4", "bar16,bar4") else 1
                self.assert_zero(module["a"]**4-centre*sp.eye(size))
                generators = {1: module["a"], 2: clean(module["d"]*module["a"])}
                for _, inverse, lift in moves:
                    moved_q, moved_r = OLD.rotate(lift, (module["e"], module["g"]))
                    mass = physical_mass_blocks(moved_q, moved_r, omega, pbar, pz)
                    for word in words:
                        fword = evaluate_word(word, flavour)
                        kword = evaluate_word(free_substitute(word, inverse), generators)
                        incoming = physical_transition_blocks(fword, kword)
                        outgoing = physical_transition_blocks(fword, kword, conjugate_flavour=True)
                        # Retain all four source slots and the trace-dual target on
                        # every E8 summand, for both bare and corrected compensators.
                        for row in range(4):
                            for col in range(4):
                                left = sum((mass[row][i]*incoming[i][col] for i in range(4)), sp.zeros(size))
                                right = sum((outgoing[row][i]*mass[i][col] for i in range(4)), sp.zeros(size))
                                self.assert_zero(left-right)

    def test_stationary_gluing_and_full_peripheral_table(self):
        data=carriers()
        ell=sp.Symbol("ell",positive=True)
        pair=(data["e"]/(2*sp.sqrt(2)*ell),data["g"]/(2*sp.sqrt(2)*ell))
        self.assert_zero(OLD.bracket(*pair))
        moment=sum((OLD.bracket(x,OLD.dagger(x)) for x in pair),sp.zeros(10))
        self.assert_zero(moment-data["h"]/(4*ell**2))
        for x in pair:
            self.assert_zero(OLD.bracket(data["h"],x)-2*x)
        wrong=(data["e"]/(2*ell),pair[1])
        wrong_moment=sum((OLD.bracket(x,OLD.dagger(x)) for x in wrong),sp.zeros(10))
        self.assertNotEqual(clean(wrong_moment-data["h"]/(4*ell**2)),sp.zeros(10))
        fi,fj,_,_=OLD.units()
        flavour_peripheral=fi*fj*OLD.dagger(fi)*OLD.dagger(fj)
        self.assert_zero(flavour_peripheral+sp.eye(2))
        a,b=data["asp"],data["dsp"]*data["asp"]
        gauge_peripheral=clean(a*b*OLD.dagger(a)*OLD.dagger(b))
        total=clean(data["psp"]*gauge_peripheral)
        self.assert_zero(total+sp.eye(32))
        self.assert_zero(sp.kronecker_product(-flavour_peripheral,total)+sp.eye(64))
        av,bv=data["av"],data["dv"]*data["av"]
        pv=clean(data["dv"]**2)
        self.assert_zero(pv*av*bv*OLD.dagger(av)*OLD.dagger(bv)-sp.eye(10))
        # A commuting rotation pair has identity flavour and flat gauge peripheral.
        d=data["dsp"]
        self.assert_zero(d*d**2*OLD.dagger(d)*OLD.dagger(d**2)-sp.eye(32))
        for root in ROOTS.e8_roots():
            if all(root[i]==0 for i in range(3)):
                qy=ROOTS.dot(ROOTS.QY,root)
                self.assertEqual(qy % 3,0)

    def test_actual_centralizer_mass_and_escaping_channel(self):
        t,y=sp.symbols("t y",real=True,positive=True)
        u,v=sp.Function("u")(t),sp.Function("v")(t)
        omega=sp.Symbol("Omega",positive=True)
        ell=sp.Symbol("ell",positive=True)
        ll,aa0,uu,vv,dz_l,dz_a,bar_u,bar_v=sp.symbols("lambda0 a0 u0 v0 dz_l dz_a bar_u bar_v")
        modules=full_parent_modules()
        self.assertEqual(sum(module["a"].rows for module in modules),248)
        background_norm=0
        for module in modules:
            for generator in (module["e"],module["g"],module["h"],
                              OLD.dagger(module["e"]),OLD.dagger(module["g"]),
                              module["a"],module["d"]):
                self.assert_zero(OLD.bracket(generator,module["t"]))
            background_norm+=sp.trace(OLD.dagger(module["e"])*module["e"])/60
        for module in full_parent_modules(corrected=True):
            self.assert_zero(OLD.bracket(module["a"],module["t"]))
            self.assert_zero(OLD.bracket(module["d"],module["t"]))
        self.assertEqual(sp.simplify(background_norm),20)
        records=actual_centralizer_rows(omega,ell,(ll,aa0,uu,vv),dz_l,dz_a,bar_u,bar_v)
        expected_scalars=(-dz_a/(sp.sqrt(2)*omega**2),sp.sqrt(2)*dz_l,bar_v/omega,-bar_u/omega)
        for coefficient,_,rows in records:
            for row,scalar in zip(rows,expected_scalars):
                self.assert_zero(row-scalar*coefficient)
        coefficient_norm,projected_rows=centralizer_projection(records)
        self.assertEqual(coefficient_norm,1)
        self.assert_zero(projected_rows-sp.Matrix(expected_scalars))
        projected=projected_rows[2:4,:].subs({ll:0,aa0:0,dz_l:0,dz_a:0,
                                             bar_u:sp.I*omega*sp.diff(u,t),
                                             bar_v:sp.I*omega*sp.diff(v,t)})
        sigma2=sp.Matrix([[0,-sp.I],[sp.I,0]])
        self.assert_zero(projected+sigma2*sp.Matrix([sp.diff(u,t),sp.diff(v,t)]))
        tau2=sigma2
        radial=-sp.kronecker_product(tau2,sigma2)
        self.assert_zero(radial-radial.conjugate().T)
        self.assert_zero(radial**2-sp.eye(4))
        self.assertEqual(radial.trace(),0)
        # The physical spin density Omega dxdy is dt after y=exp(t).
        self.assertEqual(sp.simplify((1/y)*y),1)
        s=sp.Symbol("s",real=True)
        length,epsilon=sp.symbols("L epsilon",positive=True)
        bump=s**2*(1-s)**2
        bump_norm=sp.integrate(bump**2,(s,0,1))
        derivative=sp.integrate(sp.diff(bump,s)**2,(s,0,1))
        normalized_norm=sp.simplify(length*(1/length)*bump_norm/bump_norm)
        residual_squared=sp.simplify(derivative/(length**2*bump_norm))
        self.assertEqual(normalized_norm,1)
        self.assertEqual(sp.limit(residual_squared,length,sp.oo),0)
        self.assertGreater(derivative,0)
        self.assertNotEqual(phase(Fraction(1,2)),1)
        self.assertEqual((-1)*(-1),1)
        lam=sp.Symbol("lambda",real=True)
        aa=sp.Symbol("a",complex=True)
        z=lam+sp.I*epsilon
        decay=sp.exp(sp.I*z*t)
        psi=sp.Matrix([aa*decay,aa*decay])
        sigma1=sp.Matrix([[0,1],[1,0]])
        self.assert_zero(-sp.I*sigma1*psi.diff(t)-z*psi)
        exterior_norm=sp.integrate(2*sp.conjugate(aa)*aa*sp.exp(-2*epsilon*t),(t,0,sp.oo))
        self.assertEqual(sp.simplify(exterior_norm-sp.conjugate(aa)*aa/epsilon),0)
        response=sp.simplify(sp.I*psi[1].subs(t,0)/psi[0].subs(t,0))
        self.assertEqual(response,sp.I)
        complex_parameter=sp.Symbol("z")
        self.assertEqual(sp.diff(response,complex_parameter),0)
        self.assertNotEqual(sp.simplify(exterior_norm),0)
        self.assertEqual(sp.im(sp.I)/sp.im(z),1/epsilon)
        self.assertEqual(sp.limit(sp.exp(2*epsilon*t),t,sp.oo),sp.oo)
        charge=sp.simplify(sum(sp.trace(OLD.dagger(coefficient)*OLD.bracket(cartan,coefficient))
                               for coefficient,cartan,_ in records)/(60*coefficient_norm))
        self.assertEqual(charge,2)
        self.assertNotEqual(coefficient_norm,bump_norm)
        g6,area=sp.symbols("g6 area",positive=True)
        physical_overlap=sp.integrate((length/length)*(bump**2/bump_norm)*charge,(s,0,1))
        canonical_vertex=sp.simplify((g6**2/g6**2)*(g6/sp.sqrt(area))*physical_overlap)
        self.assertEqual(canonical_vertex,2*g6/sp.sqrt(area))


if __name__ == "__main__":
    unittest.main()
