"""Separate Fraction arithmetic and full polynomial convolution, never jets."""
import importlib.util
import json
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('nil_flat_old_fraction', HERE.parent/'silver_cover_neutral_2026_10_12/reference.py')
old = importlib.util.module_from_spec(spec); spec.loader.exec_module(old)
c = old.c; r = old.r; K = c.K; ETA = dict(zip('abt', (-1, -1, 1)))


def ad(w, x):
    return c.mm(c.mm(w, x), c.inverse(w))


def coordinates(x):
    return [x[i][j] for i in range(5) for j in range(5) if i != j]+[x[i][i] for i in range(4)]


def flag(x):
    return all(not x[i][j] for i in range(5) for j in range(5) if j != 4 or i == 4)


def crossed(w, x, text):
    letters = {**w, **{g.upper(): c.inverse(a) for g, a in w.items()}}
    vals = {**x, **{g.upper(): c.scale(ad(c.inverse(w[g]), v), -ETA[g]) for g, v in x.items()}}
    hol = c.I(5); value = c.Z(5); eta = 1
    for letter in text:
        value = c.add(value, c.scale(ad(hol, vals[letter]), eta))
        hol = c.mm(hol, letters[letter]); eta *= ETA[letter.lower()]
    return hol, value, eta


def trim(a):
    while len(a) > 1 and c.zero(a[-1]):
        a.pop()
    return a


def poly_mm(a, b):
    # No truncation. Include EVERY coefficient before removing proved zeros.
    out = [c.Z(5) for _ in range(len(a)+len(b)-1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = c.add(out[i+j], c.mm(x, y))
    return trim(out)


def curve_letters(w, y):
    out = {g: [a, c.mm(y[g], a)] for g, a in w.items()}
    out.update({g.upper(): [c.inverse(a), c.scale(c.mm(c.inverse(a), y[g]), -ETA[g])] for g, a in w.items()})
    return out


def curve_word(letters, text):
    value = [c.I(5)]; eta = 1
    for letter in text:
        value = poly_mm(value, [c.scale(a, eta**j) for j, a in enumerate(letters[letter])])
        eta *= ETA[letter.lower()]
    return value, eta


def positive(v):
    v = v if isinstance(v, K) else K(v)
    a, b = v.a, v.b
    if a >= 0 and b >= 0:
        return bool(v)
    if a <= 0 and b <= 0:
        return False
    return a*a > 2*b*b if a > 0 else 2*b*b > a*a


def col(x):
    return [[v] for g in 'abt' for v in coordinates(x[g])]


@lru_cache(None)
def run():
    data, w, P, Q, A, B = c.literal(); checks = {}
    def ck(key, value):
        checks[key] = bool(value); assert checks[key], key
    # Its own old Fraction observation, not the new native/output import.
    frozen = json.loads((HERE.parent/'silver_cover_neutral_2026_10_12/results/science/reference.stdout.log').read_text())
    x = {g: [[K(a, b) for a, b in row] for row in mat]
         for g, mat in frozen['odd_absolute_cocycle_matrices'].items()}
    C = c.Z(5)
    for j, value in enumerate((1, 1, 1, 1, -4)):
        C[j][j] = value
    f = c.scale(C, K(-1)/2)
    cob = {g: c.add(c.scale(ad(a, f), ETA[g]), f, -1) for g, a in w.items()}
    y = {g: c.add(x[g], cob[g], -1) for g in w}
    ck('original_cocycle_fresh_literal_relator_and_boundary',
       all(c.zero(crossed(w, x, word)[1]) and crossed(w, x, word)[2] == 1 for word in data['relators']+data['cusp_words']))
    ck('parallel_boundary_not_parallel_bulk', c.equal(ad(P, f), f) and c.equal(ad(Q, f), f) and any(not c.zero(v) for v in cob.values()))
    ck('new_relative_cocycle_equations', all(c.zero(crossed(w, y, word)[1]) for word in data['relators']+data['cusp_words']))
    basis = c.basis5(); rn = {g: c.scale(c.ad_group(a, basis), ETA[g]) for g, a in w.items()}
    BB = sum((c.add(rn[g], c.I(24), -1) for g in 'abt'), [])
    xv, yv, cv = col(x), col(y), col(cob)
    ranks = {'bulk_coboundary': r.rank(BB), 'with_original': r.rank(c.cat(BB, xv)),
             'with_compensated': r.rank(c.cat(BB, yv)), 'two_physical_vectors': r.rank(c.cat(xv, yv))}
    ck('full_adjoint_absolute_nonexactness', ranks['with_original'] == ranks['with_compensated'] == ranks['bulk_coboundary']+1)
    ck('basis_change_not_physical_gauge_deletion', c.equal(c.add(xv, yv, -1), cv)
       and c.equal(c.mm(BB, [[v] for v in coordinates(f)]), cv)
       and ranks['two_physical_vectors'] == 2 and r.rank(c.cat(BB, cv)) == ranks['bulk_coboundary'])
    ck('actual_nonzero_n_valued_relative_class', all(flag(v) for v in y.values()) and any(not c.zero(v) for v in y.values()))
    ideals = []
    for i in range(4):
        a = c.Z(5); a[i][4] = 1; ideals.append(a)
    ck('literal_global_flat_invariant_n', all(flag(ad(a, z)) and flag(ad(c.inverse(a), z)) for a in w.values() for z in ideals)
       and all(a[4][j] == int(j == 4) for a in w.values() for j in range(5)))
    ck('all_nil_basis_products_zero', all(c.zero(c.mm(a, b)) for a in ideals for b in ideals))
    wrong = next(z for z in basis if not (c.equal(ad(P, z), z) and c.equal(ad(Q, z), z)))
    fp = c.add(f, wrong)
    yp = {g: c.add(x[g], c.add(c.scale(ad(a, fp), ETA[g]), fp, -1), -1) for g, a in w.items()}
    ck('changed_primitive_has_nonzero_boundary_cocycle', any(not c.zero(crossed(w, yp, word)[1]) for word in data['cusp_words']))
    ck('opposite_sign_fails_nil_hypothesis', not all(flag(c.add(x[g], cob[g])) for g in w))
    ck('exact_coboundary_not_new_absolute_mode', r.rank(c.cat(BB, cv)) == r.rank(BB) and not c.zero(cv))
    letters = curve_letters(w, y); words = {}
    for text in data['relators']+data['cusp_words']+['bA', 't', 'aa', 'ab', 'atA']:
        curve, eta = curve_word(letters, text)
        ck('complete_polynomial_degree_'+text, len(curve) <= 2)
        ck('actual_crossed_first_coefficient_'+text, c.equal(curve[1] if len(curve)>1 else c.Z(5), c.mm(crossed(w, y, text)[1], c.word(w, text))))
        if text in data['relators']:
            ck('full_relator_identity_'+text, len(curve) == 1 and c.equal(curve[0], c.I(5)) and eta == 1)
        if text in data['cusp_words']:
            ck('full_peripheral_identity_'+text, len(curve) == 1 and c.equal(curve[0], c.word(w, text)) and eta == 1)
        words[text] = {'eta': eta, 'coefficients': [old.pair_matrix(a) for a in curve]}
    ck('nontrivial_ordinary_kernel_representation_witness', all(words[text]['eta'] == 1 for text in ['bA', 't', 'aa', 'ab', 'atA'])
       and any(len(words[text]['coefficients']) == 2 for text in ['bA', 't', 'aa', 'ab', 'atA']))
    frames = {}; globally_based_changes = False
    inverse_a = [c.scale(a, (-1)**j) for j, a in enumerate(letters['A'])]
    for text in data['cusp_words']:
        based, eta = curve_word(letters, 'a'+text+'A')
        actual = poly_mm(poly_mm(inverse_a, based), letters['a'])
        ck('second_cusp_transported_frame_'+text, len(actual) == 1 and c.equal(actual[0], c.word(w, text)) and eta == 1)
        globally_based_changes |= not (len(based) == 1 and c.equal(based[0], c.word(w, 'a'+text+'A')))
        frames[text] = [old.pair_matrix(a) for a in based]
    z = ideals[0]; zz = c.tr(z); comm = c.add(c.mm(z, zz), c.mm(zz, z), -1)
    quadratic = poly_mm([c.I(5), z], [c.I(5), zz])
    ck('nonzero_parent_bracket_and_untruncated_quadratic_control', not c.zero(comm) and len(quadratic) == 3 and not c.zero(quadratic[2]))
    ck('actual_nil_does_not_zero_Hermitian_commutator', any(not c.equal(c.mm(a, c.tr(a)), c.mm(c.tr(a), a)) for a in y.values()))
    density = sum(sum(c.mm(c.tr(a), a)[j][j] for j in range(5)) for a in y.values())
    ck('trace_null_is_not_positive_norm_zero', all(sum(c.mm(a, a)[j][j] for j in range(5)) == 0 for a in y.values()) and positive(density))
    return {'checks': checks, 'exact_predicates': len(checks), 'ranks': ranks,
            'compensated_cocycle_matrices': {g: old.pair_matrix(v) for g, v in y.items()},
            'connecting_cocycle_matrices': {g: old.pair_matrix(v) for g, v in cob.items()},
            'curve_words': words, 'based_second_peripheral_polynomials': frames,
            'globally_based_second_peripheral_changes': bool(globally_based_changes),
            'all_order_holomorphic_line_conditional': True, 'connecting_direction_deleted': False,
            'all_neutral_directions_flat': False, 'global_harmonic_profile_computed': False,
            'global_positive_Gram_computed': False, 'real_moment_vacuum_derived': False,
            'generated_selection': False, 'global_quantum_anomaly': False,
            'outside_review': False, 'full_goal_achieved': False, 'new_native_imported': False}


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
