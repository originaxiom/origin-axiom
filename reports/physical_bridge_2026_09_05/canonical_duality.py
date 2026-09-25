"""R48 finite controls, not a numerical proof of global convex-domain uniqueness."""
from functools import lru_cache
import importlib.util
import itertools
import json
from pathlib import Path

import sympy as s

spec = importlib.util.spec_from_file_location(
    'r48_exact_prior', Path(__file__).with_name('neutral_pairing_diagnostic.py'))
exact = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exact)
v, q = exact.v, exact.q
cc = v.cc
R, k = cc.R, cc.K


def zeros(matrix):
    """Rational identities in all displayed variables; not tolerance comparison."""
    return all(s.cancel(s.together(s.expand(x))) == 0 for x in matrix)


def reduce_word(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == letter.swapcase():
            stack.pop()
        else:
            stack.append(letter)
    return ''.join(stack)


def inverse_word(word):
    return word[::-1].swapcase()


@lru_cache(None)
def representation_checks():
    j = v.pairing_witness()
    gens = cc.prior.generators(q)
    rows = []
    for phase in (s.Integer(1), s.Integer(-1), s.I, -s.I):
        twisted = tuple(phase*a for a in gens)
        for word in ('m', 'n', 'mnM', v.LONGITUDE, v.RELATOR):
            a = cc.prior.word(word, twisted)
            theta = cc.prior.word(word.swapcase(), twisted)
            rows.append(exact.zero_matrix(a.inv().T*j-j*theta))
    product = cc.prior.word('mn', gens)
    return {
        'all_twists_and_words': all(rows),
        'symmetric': j == j.T,
        'determinant': exact.exact_zero(j.det()+q*(q*q+q+1)**3/(16*(q+1)**4)),
        'transpose_only_word_rejected': not exact.zero_matrix(product.T*j-j*product),
        'wrong_twist_rejected': not exact.zero_matrix(
            (s.I*gens[0]).inv().T*j-j*(s.I*gens[0].inv())),
        'wrong_witness_rejected': any(not exact.zero_matrix(
            a.T*(j+s.eye(4))-(j+s.eye(4))*a) for a in gens)}


def conormal_frames():
    f = s.Matrix([[1,1,0,0],[0,1,2,0],[0,0,1,3],[0,0,0,1]])
    signs = s.diag(1,-1,-1,-1)
    dual = f.inv().T*signs
    h = f.inv().T*f.inv()
    hd = dual.inv().T*dual.inv()
    return f, dual, h, hd, signs


def product_conormal():
    x0, z, y = s.symbols('x0 z y', real=True)
    rad = x0-y*y/2
    logu = s.log(z)/4+3*s.log(rad)/8
    coords = s.Matrix([x0,z,y])
    gradient = s.Matrix([s.diff(logu,x) for x in coords])
    normal = gradient.col_join(s.Matrix([1-coords.dot(gradient)]))
    expected = s.Matrix([1,2*rad/(3*z),-y,x0])
    return normal, expected, rad, (x0,z,y)


def leading_metric():
    return s.Matrix([[s.Rational(15,64),0,3*k/8],
                     [0,3/(8*R),0], [3*k/8,0,3*k*k]])


def shear_jacobian(include_shear=True):
    a = -1/(4*k) if include_shear else s.Integer(0)
    return s.Matrix([[1,0,0],[0,-1,0],[a,0,-1]])


def ellipse_countercontrol():
    # Trivial holonomy satisfies every intertwiner equation. Its domain is
    # NOT selected by that equation. Projective conormal ratios suffice.
    quadratic = s.diag(1,-4,-1,-1)
    chosen_intertwiner = s.diag(1,-1,-1,-1)
    point = s.Matrix([1,s.Rational(2,5),0,0])
    alleged_image = chosen_intertwiner.inv()*quadratic*point
    return ((point.T*quadratic*point)[0],
            (alleged_image.T*quadratic*alleged_image)[0])


def exterior_square(a):
    return v.pc.group_action('6',a)


def volume_tensor():
    pairs = tuple(itertools.combinations(range(4),2))
    return s.Matrix([[s.LeviCivita(*ab,*cd) for cd in pairs] for ab in pairs])


@lru_cache(None)
def vertex_checks():
    j = v.pairing_witness()
    w = exterior_square(j)
    tensor = volume_tensor()
    phase = (1+s.I)/s.sqrt(2)
    b = s.eye(4)
    b[0,0] = b[3,3] = 0
    b[0,3] = b[3,0] = 1
    unit = phase*b
    induced = exterior_square(unit)
    return {
        'volume_identity': exact.zero_matrix(w.T*tensor*w-j.det()*tensor),
        'missing_normalization_rejected': not exact.zero_matrix(w.T*tensor*w-tensor),
        'unit_phase_determinant': s.simplify(unit.det()) == 1,
        'unit_phase_metric': zeros(unit.conjugate().T*unit-s.eye(4)),
        'normalized_vertex': zeros(induced.T*tensor*induced-tensor),
        'exterior_unitary': zeros(induced.conjugate().T*induced-s.eye(6))}


@lru_cache(None)
def parent_weyl_checks():
    roots = set(v.pc.pb.pv.e8_direct())
    e = s.eye(8)
    reflecting = (e[:,0]+e[:,5], e[:,0]-e[:,5],
                  e[:,6]+e[:,7], e[:,6]-e[:,7])
    actual = s.eye(8)
    for a in reflecting:
        actual = (s.eye(8)-a*a.T)*actual
    expected = s.diag(-1,1,1,1,1,-1,-1,-1)
    wrong = s.diag(-1,1,1,1,1,1,1,1)
    half = [r for r in roots if abs(r[0]) == s.Rational(1,2)]
    return {
        'root_population': len(roots) == 240 and len(half) == 128,
        'actual_reflection_roots': all(tuple(a) in roots for a in reflecting),
        'reflection_product': actual == expected,
        'full_root_set': {tuple(actual*s.Matrix(r)) for r in roots} == roots,
        'wrong_single_flip_rejected': {tuple(wrong*s.Matrix(r)) for r in roots} != roots,
        'spinor_and_A3_dual': all(
            s.prod((actual*s.Matrix(r))[:5]) == -s.prod(r[:5])
            and tuple((actual*s.Matrix(r))[5:]) == tuple(-x for x in r[5:])
            for r in half)}


def response_control():
    operator = s.diag(1,2,4)
    unit = s.Matrix([[s.Rational(3,5),-s.Rational(4,5),0],
                     [s.Rational(4,5),s.Rational(3,5),0],[0,0,1]])
    source = s.Matrix([1,1,2])
    shifted = 2*s.eye(3)+2*operator
    first = (source.T*shifted.inv()*source)[0]
    transformed = unit*operator*unit.T
    paired = ((unit*source).T*(2*s.eye(3)+2*transformed).inv()*(unit*source))[0]
    wrong = ((unit*source).T*shifted.inv()*(unit*source))[0]
    return first, paired, wrong


def run():
    f,dual,h,hd,signs = conormal_frames()
    normal,expected,rad,_ = product_conormal()
    metric, jac = leading_metric(), shear_jacobian()
    inside,outside = ellipse_countercontrol()
    first,paired,wrong = response_control()
    checks = {
        'presented_automorphism': reduce_word(v.RELATOR.swapcase())
            == reduce_word('N'+inverse_word(v.RELATOR)+'n'),
        'longitude_inverted': v.LONGITUDE.swapcase() == inverse_word(v.LONGITUDE),
        'conormal_pairings': f.T*dual == signs,
        'dual_positive_metric': hd == h.inv() and h.det() == hd.det() == 1,
        'orientation_signs': dual.det() == -1 and s.diag(1,1,1,-1).det()*dual.det() == 1,
        'product_conormal': zeros(8*rad*normal/3-expected),
        'leading_isometry': zeros(jac.T*metric*jac-metric),
        'leading_involution': jac*jac == s.eye(3) and jac.det() == 1,
        'naive_flip_rejected': not zeros(shear_jacobian(False).T*metric*shear_jacobian(False)-metric),
        'domain_shortcut_rejected': inside > 0 and outside < 0,
        'whole_response': first == paired and first > 0,
        'wrong_operator_rejected': first != wrong}
    checks.update(representation_checks())
    checks.update(vertex_checks())
    checks.update(parent_weyl_checks())
    return {'checks': {name:bool(value) for name,value in checks.items()},
            'all_checks_pass': bool(all(checks.values())),
            'global_grade':'Authored analytic application with explicit external dependencies; not proved by these tests.',
            'global_PDE_numerically_solved':False,
            'independent_global_proof_review':False,
            'actual_nonzero_coupling_computed':False,
            'physical_chirality_derived':False}


if __name__ == '__main__':
    data = run()
    print(json.dumps(data,sort_keys=True))
    raise SystemExit(0 if data['all_checks_pass'] else 1)
