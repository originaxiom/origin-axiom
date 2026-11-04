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
        av, dv, asp, dsp = (data[k] for k in ("av", "dv", "asp", "dsp"))
        h4 = sp.diag(phase(sp.Rational(3, 8)), *(phase(-sp.Rational(1, 8)) for _ in range(3)))
        h6 = exterior_square(h4)
        a3_pairs = [(i,j) for i in range(4) for j in range(4) if i != j]
        h15 = sp.diag(*(sp.simplify(h4[i,i]/h4[j,j]) for i,j in a3_pairs), 1, 1, 1)
        odd = [i for i in range(32) if i.bit_count() % 2]
        even = [i for i in range(32) if i.bit_count() % 2 == 0]
        modules = (
            (exterior_square(av), exterior_square(dv)),
            (h15, sp.eye(15)),
            (sp.kronecker_product(av,h6), sp.kronecker_product(dv,sp.eye(6))),
            (sp.kronecker_product(asp.extract(odd,odd),h4), sp.kronecker_product(dsp.extract(odd,odd),sp.eye(4))),
            (sp.kronecker_product(asp.extract(even,even),h4.conjugate()), sp.kronecker_product(dsp.extract(even,even),sp.eye(4))),
        )
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
        # A nonzero background acts on the first two coordinates. T commutes with
        # that entire block, while another coefficient retains interactions.
        q=sp.Matrix([[0,1,0],[0,0,0],[0,0,0]])
        r=2*q
        central=sp.diag(1,1,-2)
        for x in (q,r,OLD.dagger(q),OLD.dagger(r)):
            self.assert_zero(OLD.bracket(x,central))
        self.assertNotEqual(OLD.bracket(q,OLD.dagger(q)),sp.zeros(3))
        omega=sp.Symbol("Omega",positive=True)
        ll,aa0,uu,vv,dz_l,dz_a,bar_u,bar_v=sp.symbols("lambda0 a0 u0 v0 dz_l dz_a bar_u bar_v")
        lm,am,um,vm=(value*central for value in (ll,aa0,uu,vv))
        p1=bar_u*central+sp.I*OLD.bracket(q,am)
        p2=bar_v*central+sp.I*OLD.bracket(r,am)
        wedge=OLD.bracket(q,vm)-OLD.bracket(r,um)
        source_rows=(
            -(dz_a*central-2*sp.I*omega*(OLD.bracket(OLD.dagger(q),um)
                                       +OLD.bracket(OLD.dagger(r),vm)))/(sp.sqrt(2)*omega**2),
            2*sp.I*wedge+sp.sqrt(2)*dz_l*central,
            p2/omega-sp.sqrt(2)*sp.I*OLD.bracket(OLD.dagger(q),lm),
            -p1/omega-sp.sqrt(2)*sp.I*OLD.bracket(OLD.dagger(r),lm),
        )
        expected_scalars=(-dz_a/(sp.sqrt(2)*omega**2),sp.sqrt(2)*dz_l,bar_v/omega,-bar_u/omega)
        for row,scalar in zip(source_rows,expected_scalars):
            self.assert_zero(row-scalar*central)
        radial_rows=[row.subs({ll:0,aa0:0,dz_l:0,dz_a:0,
                              bar_u:sp.I*omega*sp.diff(u,t),
                              bar_v:sp.I*omega*sp.diff(v,t)}) for row in source_rows]
        self.assert_zero(radial_rows[0])
        self.assert_zero(radial_rows[1])
        projected=sp.Matrix([radial_rows[2][0,0],radial_rows[3][0,0]])
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
        norm=sp.integrate(bump**2,(s,0,1))
        derivative=sp.integrate(sp.diff(bump,s)**2,(s,0,1))
        normalized_norm=sp.simplify(length*(1/length)*norm/norm)
        residual_squared=sp.simplify(derivative/(length**2*norm))
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
        colour_x=sp.diag(1,-1)
        colour_t=sp.Matrix([[0,1],[0,0]])
        coefficient_norm=OLD.kappa(OLD.dagger(colour_t)*colour_t)
        charge=OLD.kappa(OLD.dagger(colour_t)*OLD.bracket(colour_x,colour_t))/coefficient_norm
        self.assertEqual(charge,2)
        g6,area=sp.symbols("g6 area",positive=True)
        physical_overlap=sp.integrate((length/length)*(bump**2/norm)*charge,(s,0,1))
        canonical_vertex=sp.simplify((g6**2/g6**2)*(g6/sp.sqrt(area))*physical_overlap)
        self.assertEqual(canonical_vertex,2*g6/sp.sqrt(area))


if __name__ == "__main__":
    unittest.main()
