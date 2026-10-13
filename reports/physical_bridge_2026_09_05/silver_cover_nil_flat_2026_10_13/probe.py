"""Actual flag representative and untruncated exact polynomial holonomies."""
import importlib.util
import json
from functools import lru_cache
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('nil_flat_old_native', HERE.parent/'silver_cover_neutral_2026_10_12/probe.py')
old = importlib.util.module_from_spec(spec); spec.loader.exec_module(old)
p = old.p; cy = old.cy; q = s.Symbol('q'); ETA = dict(zip('abt', (-1, -1, 1)))


def ad(w, x):
    return p.mm(p.mm(w, x), cy.inv(w))


def coordinates(x):
    return s.Matrix([x[i, j] for i in range(5) for j in range(5) if i != j]+[x[i, i] for i in range(4)])


def flag(x):
    return all(x[i, j] == 0 for i in range(5) for j in range(5) if j != 4 or i == 4)


def crossed(w, x, text):
    letters = {**w, **{g.upper(): cy.inv(a) for g, a in w.items()}}
    vals = {**x, **{g.upper(): -ETA[g]*ad(cy.inv(w[g]), v) for g, v in x.items()}}
    hol = s.eye(5); value = s.zeros(5); eta = 1
    for letter in text:
        value += eta*ad(hol, vals[letter]); hol = p.mm(hol, letters[letter]); eta *= ETA[letter.lower()]
    return hol, value.applyfunc(s.expand), eta


def curve_letters(w, y):
    out = {g: p.mm(s.eye(5)+q*y[g], a, q) for g, a in w.items()}
    out.update({g.upper(): p.mm(cy.inv(a), s.eye(5)-ETA[g]*q*y[g], q) for g, a in w.items()})
    return out


def curve_word(letters, text):
    value = s.eye(5); eta = 1
    for letter in text:
        value = p.mm(value, letters[letter].subs(q, eta*q), q); eta *= ETA[letter.lower()]
    return value.applyfunc(s.expand), eta


def polynomial_coefficients(a):
    polys = [s.Poly(x, q, extension=s.sqrt(2)) for x in a]
    degree = max((int(x.degree()) for x in polys if not x.is_zero), default=0)
    return [a.applyfunc(lambda x: s.expand(x).coeff(q, j)) for j in range(degree+1)]


def encode(a):
    return old.pair_matrix(a)


@lru_cache(None)
def run():
    _, data, w, P, Q, A, B = cy.literal(); facts = {}
    def ck(key, value):
        facts[key] = bool(value); assert facts[key], key
    frozen = json.loads((HERE.parent/'silver_cover_neutral_2026_10_12/results/science/probe.stdout.log').read_text())
    x = {g: s.Matrix([[s.Rational(a)+s.sqrt(2)*s.Rational(b) for a, b in row] for row in mat])
         for g, mat in frozen['odd_absolute_cocycle_matrices'].items()}
    C = s.diag(1, 1, 1, 1, -4); f = -C/2
    cob = {g: ETA[g]*ad(a, f)-f for g, a in w.items()}
    y = {g: (x[g]-cob[g]).applyfunc(s.expand) for g in w}
    ck('original_relative_class_rechecked_on_literal_words',
       all(p.zero(crossed(w, x, word)[1]) and crossed(w, x, word)[2] == 1 for word in data['relators']+data['cusp_words']))
    ck('boundary_parallel_primitive_not_global_parallel', p.zero(ad(P, f)-f) and p.zero(ad(Q, f)-f)
       and any(not p.zero(v) for v in cob.values()))
    ck('compensated_relative_class_rechecked', all(p.zero(crossed(w, y, word)[1]) for word in data['relators']+data['cusp_words']))
    basis = cy.adjoint_basis(); rn = {g: ETA[g]*cy.adjoint_group(a, basis) for g, a in w.items()}
    BB = s.Matrix.vstack(*(rn[g]-s.eye(24) for g in 'abt'))
    xv = s.Matrix.vstack(*(coordinates(x[g]) for g in 'abt'))
    yv = s.Matrix.vstack(*(coordinates(y[g]) for g in 'abt'))
    cv = s.Matrix.vstack(*(coordinates(cob[g]) for g in 'abt'))
    ranks = {'bulk_coboundary': p.rank(BB), 'with_original': p.rank(BB.row_join(xv)),
             'with_compensated': p.rank(BB.row_join(yv)), 'two_physical_vectors': p.rank(xv.row_join(yv))}
    ck('whole_adjoint_nonexactness_not_only_flag_quotient', ranks['with_original'] == ranks['with_compensated'] == ranks['bulk_coboundary']+1)
    ck('same_absolute_class_distinct_retained_relative_vectors', p.zero(xv-yv-cv) and p.zero(p.mm(BB, coordinates(f))-cv)
       and ranks['two_physical_vectors'] == 2 and p.rank(BB.row_join(cv)) == ranks['bulk_coboundary'])
    ck('candidate_is_actual_nonzero_nil_ideal_cocycle', all(flag(v) for v in y.values()) and any(not p.zero(v) for v in y.values()))
    ideals = []
    for i in range(4):
        a = s.zeros(5); a[i, 4] = 1; ideals.append(a)
    ck('global_invariant_flag_not_a_bulk_splitting', all(flag(ad(a, z)) and flag(ad(cy.inv(a), z)) for a in w.values() for z in ideals)
       and all(a[4, j] == int(j == 4) for a in w.values() for j in range(5)))
    ck('entire_nil_ideal_products_vanish', all(p.zero(p.mm(a, b)) for a in ideals for b in ideals))
    wrong = next(z for z in basis if not (p.zero(ad(P, z)-z) and p.zero(ad(Q, z)-z)))
    fp = f+wrong; yp = {g: x[g]-(ETA[g]*ad(a, fp)-fp) for g, a in w.items()}
    ck('nonparallel_primitive_changes_actual_relative_trace', any(not p.zero(crossed(w, yp, word)[1]) for word in data['cusp_words']))
    ys = {g: x[g]+cob[g] for g in w}
    ck('wrong_sign_cannot_inherit_nil_proof', not all(flag(v) for v in ys.values()))
    ck('genuine_coboundary_rejected_as_nonexact', p.rank(BB.row_join(cv)) == p.rank(BB) and not p.zero(cv))
    letters = curve_letters(w, y); words = {}
    for text in data['relators']+data['cusp_words']+['bA', 't', 'aa', 'ab', 'atA']:
        curve, eta = curve_word(letters, text); coeff = polynomial_coefficients(curve)
        ck('untruncated_polynomial_degree_'+text, len(coeff) <= 2)
        ck('actual_first_derivative_'+text, p.zero((coeff[1] if len(coeff)>1 else s.zeros(5))-p.mm(crossed(w, y, text)[1], cy.word(w, text))))
        if text in data['relators']:
            ck('exact_all_parameter_relator_'+text, p.zero(curve-s.eye(5), q) and eta == 1)
        if text in data['cusp_words']:
            ck('exact_all_parameter_boundary_'+text, p.zero(curve-cy.word(w, text), q) and eta == 1)
        words[text] = {'eta': eta, 'coefficients': [encode(a) for a in coeff]}
    ck('ordinary_cover_has_nonzero_polynomial_witness', all(words[text]['eta'] == 1 for text in ['bA', 't', 'aa', 'ab', 'atA'])
       and any(len(words[text]['coefficients']) == 2 for text in ['bA', 't', 'aa', 'ab', 'atA']))
    frames = {}; globally_based_changes = False
    inverse_a = letters['A'].subs(q, -q)
    for text in data['cusp_words']:
        based, eta = curve_word(letters, 'a'+text+'A')
        actual = p.mm(p.mm(inverse_a, based, q), letters['a'], q)
        ck('second_cusp_actual_moving_frame_'+text, p.zero(actual-cy.word(w, text), q) and eta == 1)
        globally_based_changes |= not p.zero(based-cy.word(w, 'a'+text+'A'), q)
        frames[text] = [encode(a) for a in polynomial_coefficients(based)]
    z = ideals[0]; zz = z.T; comm = p.mm(z, zz)-p.mm(zz, z)
    ck('full_parent_bracket_and_higher_polynomial_opposite', not p.zero(comm)
       and not p.zero(((s.eye(5)+q*z)*(s.eye(5)+q*zz)).applyfunc(lambda x: s.expand(x).coeff(q, 2))))
    ck('nil_flatness_does_not_imply_zero_Hermitian_commutator', any(not p.zero(p.mm(a, a.T)-p.mm(a.T, a)) for a in y.values()))
    ck('trace_null_not_zero_positive_local_density', all(s.trace(a*a) == 0 for a in y.values())
       and bool(sum(s.trace(a.T*a) for a in y.values()) > 0))
    return {'facts': facts, 'exact_predicates': len(facts), 'ranks': ranks,
            'compensated_cocycle_matrices': {g: encode(v) for g, v in y.items()},
            'connecting_cocycle_matrices': {g: encode(v) for g, v in cob.items()},
            'curve_words': words, 'based_second_peripheral_polynomials': frames,
            'globally_based_second_peripheral_changes': bool(globally_based_changes),
            'all_order_holomorphic_line_conditional': True, 'connecting_direction_deleted': False,
            'all_neutral_directions_flat': False, 'global_harmonic_profile_computed': False,
            'global_positive_Gram_computed': False, 'real_moment_vacuum_derived': False,
            'generated_selection': False, 'global_quantum_anomaly': False,
            'outside_review': False, 'full_goal_achieved': False}


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
