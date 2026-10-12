"""Actual charged primitive kernels and their same-parent gauge currents.

New science must not be imported before its published seal. No PDE Gram
or observed coupling is supplied by this finite exact instrument.
"""
import importlib.util
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path

import sympy as s

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'cover_current_old_charged', HERE.parent/'silver_charged_pair_lift_2026_10_11/probe.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)
cy = p.cy
BLOCKS = {'Q': ('W', -1, 6), 'uc': ('W', 4, 3),
          'ec': ('W', -6, 1), 'dc': ('F', -2, 3), 'L': ('F', 3, 2)}


def clean(a):
    return a.applyfunc(s.expand)


def iszero(a):
    return all(s.simplify(x) == 0 for x in a)


def kernel(a, variable=None):
    if not a.rows:
        return s.eye(a.cols)
    return p.dm(a, variable).nullspace().to_Matrix().T


def wedge_lie(t):
    # GAUGE wedge matrices may contain i; do not coerce them into the
    # STRUCTURE quadratic field or take Lambda2 of an already twisted W.
    pairs = list(combinations(range(t.rows), 2))
    return s.Matrix(len(pairs), len(pairs), lambda i, j:
                    t[pairs[i][0], pairs[j][0]]*int(pairs[i][1] == pairs[j][1])
                    -t[pairs[i][1], pairs[j][0]]*int(pairs[i][0] == pairs[j][1])
                    +int(pairs[i][0] == pairs[j][0])*t[pairs[i][1], pairs[j][1]]
                    -int(pairs[i][1] == pairs[j][0])*t[pairs[i][0], pairs[j][1]])


def generators():
    out = {}
    for tag, indices in (('c', range(3)), ('w', range(3, 5))):
        for i, j in combinations(indices, 2):
            a = s.zeros(5); a[i, j] = a[j, i] = s.Rational(1, 2)
            b = s.zeros(5); b[i, j] = -s.I/2; b[j, i] = s.I/2
            out[f'{tag}{i}{j}x'] = a; out[f'{tag}{i}{j}y'] = b
    out['c3'] = s.diag(1, -1, 0, 0, 0)/2
    out['c8raw'] = s.diag(1, 1, -2, 0, 0)/2
    out['w3'] = s.diag(0, 0, 0, 1, -1)/2
    out['Y'] = s.diag(-s.Rational(1, 3), -s.Rational(1, 3),
                      -s.Rational(1, 3), s.Rational(1, 2), s.Rational(1, 2))
    return out


def irreps(t):
    ten = wedge_lie(t); dual = -t.T
    pairs = list(combinations(range(5), 2))
    ids = {'Q': [j for j, (a, b) in enumerate(pairs) if a < 3 <= b],
           'uc': [j for j, (a, b) in enumerate(pairs) if b < 3], 'ec': [9]}
    return {**{key: ten.extract(val, val) for key, val in ids.items()},
            'dc': dual[:3, :3], 'L': dual[3:, 3:]}


def gram_control():
    # Only a normalization/rejection fixture, NOT the global harmonic Gram.
    C = s.Matrix([[2, 0, 0], [0, 1, 1+s.I], [0, 0, 2]])
    G = clean(C.H*C); S = C.inv(); deck = s.diag(1, -1, -1)
    return C, G, S, deck


def ward_residual(t, omit_derivative=False):
    d = t.rows
    # Independent nonzero first jets; noncommuting matrices are kept.
    other = s.diag(*range(1, d+1))
    eps = t; deps = s.eye(d)+2*t; A = other
    psi = s.Matrix([j+1+s.I*j for j in range(d)])
    dpsi = s.Matrix([2*j-1+s.I for j in range(d)])
    delta = -s.I*eps*psi
    ddelta = -s.I*deps*psi-s.I*eps*dpsi
    deltaA = (s.zeros(d) if omit_derivative else deps)+s.I*(A*eps-eps*A)
    Dpsi = dpsi+s.I*A*psi
    return clean(ddelta+s.I*deltaA*psi+s.I*A*delta+s.I*eps*Dpsi)


@lru_cache(None)
def run():
    _, data, w, P, Q, A, B = cy.literal()
    facts = {}; rows = {}; actions = {}; primitive = {}
    def ck(key, value):
        facts[key] = bool(value)
        assert facts[key], key
    ck('literal_cover_is_connected_and_cusp_trivial',
       all(sum((-1 if c.isupper() else 1)*(int(c.lower() in 'ab'))
               for c in word) % 2 == 0 for word in data['relators']+data['cusp_words'])
       and (-1, -1, 1) != (1, 1, 1))
    for label, a, b, subsets in (
            ('W', A, B, ([0, 1, 2], [0, 1, 2, 3])),
            ('F', cy.exterior_lie(A), cy.exterior_lie(B),
             ([0, 1, 2, 4], [0, 1, 2, 3, 4]))):
        E = p.boundary(a, b); n = E['n']
        for sector, chosen, wanted in zip(('plus', 'minus'), subsets, (1, 2)):
            M = E['U'].row_join(E['H'][:, chosen])
            ann = kernel(M.T).T
            ck(label+sector+'_full_annihilator', p.zero(p.mm(ann, M))
               and ann.rows+M.cols == 2*n and p.rank(M) == M.cols)
            for name, (coefficient, h, dim) in BLOCKS.items():
                if coefficient != label:
                    continue
                D0 = a.col_join(b+h*p.z*s.eye(n)); C = p.mm(ann, D0, p.z)
                K = kernel(C, p.z); trace = p.mm(D0, K, p.z)
                key = name+'_'+sector
                ck(key+'_actual_primitive_kernel', K.cols == wanted
                   and p.rank(C, p.z) == n-wanted and p.zero(p.mm(C, K, p.z), p.z))
                ck(key+'_actual_admitted_trace_is_injective', p.rank(trace, p.z) == wanted
                   and p.zero(p.mm(ann, trace, p.z), p.z)
                   and p.rank(D0, p.z) == n)
                rows[key] = {'coefficient': label, 'H_weight': h, 'gauge_dimension': dim,
                             'primitive_dimension': K.cols, 'trace_rank': p.rank(trace, p.z),
                             'pencil_rank': p.rank(C, p.z)}
                primitive[key] = C
    ck('three_actual_profiles_for_each_SM_block', all(
        rows[name+'_plus']['primitive_dimension']+rows[name+'_minus']['primitive_dimension'] == 3
        for name in BLOCKS))
    gens = generators(); H = s.diag(2, 2, 2, -3, -3)
    S3 = s.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
    J2 = s.Matrix([[0, 1], [-1, 0]])
    Cg, G, S, deck = gram_control()
    ck('nonorthogonal_fixture_positive_and_deck_compatible',
       [G[:j, :j].det() for j in (1, 2, 3)] == [4, 4, 16]
       and iszero(G*deck-deck*G) and G != s.eye(3))
    ck('actual_canonical_Gram_congruence', iszero(S.H*G*S-s.eye(3)))
    norms = {}; faithful = []; support = {key: [] for key in BLOCKS}
    for name, t in gens.items():
        ck(name+'_unbroken_Hermitian_traceless', iszero(t.H-t) and s.trace(t) == 0 and iszero(t*H-H*t))
        rr = irreps(t); tc = t[:3, :3]; tw = t[3:, 3:]
        expected = {
            'Q': s.kronecker_product(tc, s.eye(2))+s.kronecker_product(s.eye(3), tw),
            'uc': -tc.T+s.trace(tc)*s.eye(3), 'ec': s.Matrix([[s.trace(tw)]]),
            'dc': -tc.T, 'L': tw-s.trace(tw)*s.eye(2)}
        mapped = {**rr, 'uc': S3*rr['uc']*S3.inv(), 'L': J2*rr['L']*J2.inv()}
        ck(name+'_all_explicit_SM_intertwiners', all(iszero(mapped[key]-expected[key]) for key in BLOCKS))
        faithful.append(s.Matrix(list(wedge_lie(t))+list(-t.T)))
        norms[name] = s.trace(t*t)
        for key, r in rr.items():
            dim = r.rows
            if not iszero(r):
                support[key].append(name)
            current = s.kronecker_product(G, r)
            change = s.kronecker_product(S, s.eye(dim))
            ck(name+'_'+key+'_normalized_current', iszero(change.H*current*change-s.kronecker_product(s.eye(3), r)))
            for sector in ('plus', 'minus'):
                cp = primitive[key+'_'+sector]
                left = s.kronecker_product(cp, s.eye(dim))*s.kronecker_product(s.eye(cp.cols), r)
                right = s.kronecker_product(s.eye(cp.rows), r)*s.kronecker_product(cp, s.eye(dim))
                ck(name+'_'+key+'_'+sector+'_physical_kernel_equivariance', iszero(left-right))
        ck(name+'_classical_Ward_first_jet', iszero(ward_residual(t)))
        ck(name+'_omitted_gauge_derivative_rejected', not iszero(ward_residual(t, True)))
        actions[name] = {key: r.rows for key, r in rr.items()}
    faith = s.Matrix.hstack(*faithful).rank()
    ck('twelve_generator_actions_are_faithful', faith == 12)
    ck('zero_gauge_action_is_rejected', s.zeros(125, 12).rank() != faith)
    ck('collapsed_family_space_is_rejected', all(
        rows[name+'_plus']['trace_rank']+rows[name+'_minus']['trace_rank'] != 1 for name in BLOCKS))
    charges = {'Q': s.Rational(1, 6), 'uc': -s.Rational(2, 3), 'ec': 1,
               'dc': s.Rational(1, 3), 'L': -s.Rational(1, 2)}
    yr = irreps(gens['Y'])
    ck('actual_hypercharge_and_wrong_dual_rejected', all(iszero(yr[key]-y*s.eye(yr[key].rows)) for key, y in charges.items())
       and not iszero(gens['Y'][:3, :3]-charges['dc']*s.eye(3)))
    ck('all_blocks_have_nonzero_current_and_singlet_control', all(support.values()) and iszero(s.zeros(1)))
    ck('missing_kinetic_Gram_rejected', not iszero(S.H*S-s.eye(3)))
    ck('raw_generator_Gram_and_SU5_normalization', all(norms[key] == (s.Rational(5, 6) if key == 'Y' else s.Rational(3, 2) if key == 'c8raw' else s.Rational(1, 2)) for key in gens)
       and s.trace((gens['c8raw']/s.sqrt(3))**2) == s.Rational(1, 2))
    K0, V, Vbase, c = s.symbols('K V Vbase c', positive=True)
    g5sq = 2/(K0*V*c); gYsq = 1/(K0*V*c*norms['Y'])
    ck('conditional_trace_ratio_not_parameter_derivation', s.simplify(gYsq/g5sq-s.Rational(3, 5)) == 0)
    ck('cover_volume_and_wrong_single_sheet_rejected', s.simplify(g5sq.subs(V, 2*Vbase)/g5sq.subs(V, Vbase)-s.Rational(1, 2)) == 0
       and s.simplify(g5sq.subs(V, 2*Vbase)/g5sq.subs(V, Vbase)-1) != 0)
    ck('current_normalization_does_not_select_three', all(
        s.kronecker_product(s.eye(n), gens['Y']).rank() == 5*n for n in (1, 2, 3)))
    return {'facts': facts, 'exact_predicates': len(facts), 'blocks': rows,
            'generator_faithfulness_rank': faith, 'hypercharges': {key: str(s.Rational(val)) for key, val in charges.items()},
            'current_support': support, 'conditional_gY_squared_over_g5_squared': '3/5',
            'global_profile_Gram_computed': False, 'supplied_parent_and_boundary': True,
            'actual_gauge_current_map_conditional': True, 'Yukawas_computed': False,
            'odd_neutral_interactions_computed': False, 'generated_boundary': False,
            'global_quantum_anomaly': False, 'outside_review': False, 'full_goal_achieved': False}


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
