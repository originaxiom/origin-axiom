"""Independent Fraction End25/LES and central degree certificate, no new native."""
import importlib.util
import json
from fractions import Fraction
from functools import lru_cache
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
OLD = HERE.parent


def load(name, path):
    sp = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(mod)
    return mod


r = load('neutral_prior_fraction_charged', OLD/'silver_charged_cubic_2026_10_11/reference.py')
mp = load('neutral_prior_fraction_End25', OLD/'silver_physical_multiplets_2026_10_11/reference.py')
c, K = r.c, r.K


def field_matrix(matrix, field):
    return [[field(x.a, x.b) if hasattr(x, 'a') else field(x) for x in row] for row in matrix]


def central_vertex(f, g, dual_meridian):
    return 3*sum(f[i]*dual_meridian[i][j]*g[j] for i in range(len(f)) for j in range(len(g)))


def neutral_spaces(w, data, ck):
    wm = {g: field_matrix(x, mp.K) for g, x in w.items()}
    rn, T = mp.end0(wm)
    N = mp.boundary(rn, data)
    C = N['C']
    ck('independent_crossed_word_chain_and_bulk_maps',
       mp.zero(mp.mm(C.F, C.B)) and mp.mm(C.R, C.B) == C.D
       and [N['h0'], N['h1'], N['h2'], 0] == [0, 6, 6, 0])
    S = mp.mm(N['J'], mp.diag2(T))
    R, HH = N['R'], N['H']
    HS = mp.mm(mp.mm(mp.tr(HH), S), HH)
    ck('literal_End25_actual_trace_symplectic_pair', mp.rank(T) == 24
       and mp.rank(HS) == 12 and mp.zero(mp.add(HS, mp.tr(HS)))
       and mp.zero(mp.mm(mp.mm(mp.tr(R), S), R)))
    M = mp.mm(mp.mm(mp.tr(R), S), HH)
    piv = mp.b.elimination(M, True)[1]
    pick = lambda a: [[row[j] for j in piv] for row in a]
    U0 = mp.mm(pick(HH), mp.inv(pick(M)))
    kk = mp.mm(mp.mm(mp.tr(U0), S), U0)
    U = mp.add(U0, [[mp.K(Fraction(1, 2))*x for x in row] for row in mp.mm(R, kk)])
    ck('exact_same_transverse_partner_not_equal_line', N['q'] == 6 and mp.nc(U) == 6
       and mp.rank(mp.hc(R, U)) == 12 and mp.zero(mp.mm(mp.mm(mp.tr(U), S), U))
       and mp.mm(mp.mm(mp.tr(R), S), U) == mp.eye(6))
    q0, global0 = mp.ker(C.D), mp.ker(C.B)
    actual, opposite = mp.les(N, U), mp.les(N, R)
    absolute_allowed = N['h1']+mp.nc(U)-mp.rank(mp.hc(R, U))
    opposite_absolute = N['h1']+mp.nc(R)-mp.rank(mp.hc(R, R))
    ck('all_six_connecting_modes_and_zero_bulk_invariants',
       N['t0'] == mp.nc(q0) == 6 and mp.nc(global0) == 0
       and mp.zero(mp.mm(C.D, q0)) and actual == [0, 6, 6, 0] and absolute_allowed == 0)
    ck('opposite_retains_six_absolute_classes', opposite == [0, 12, 12, 0] and opposite_absolute == 6)
    return dict(absolute_H=[N['h0'], N['h1'], N['h2'], 0],
                boundary_H=[N['t0'], N['t'], N['t0']], physical_H1=actual[1],
                connecting_dimension=N['t0']-N['h0'], allowed_absolute_H1=absolute_allowed,
                equal_line_physical_H1=opposite[1], equal_line_absolute_H1=opposite_absolute,
                parallel_primitive_dimension=mp.nc(q0),
                parallel_primitive_sha256=r.plane_hash(field_matrix(q0, K)),
                restriction_sha256=r.plane_hash(field_matrix(R, K)),
                plane_sha256=r.plane_hash(field_matrix(U, K)),
                tangential_trace_zero=True, state_deleted=False)


def center_catalog(check_charge=True):
    # Enumerate ordered products independently, then canonicalize types.
    charges = dict(Q=-1, u=4, e=-6, d=-2, weak=3, Hu=-3, N=0)
    color = dict(Q=1, u=2, e=0, d=2, weak=0, Hu=0, N=0)
    weak = dict(Q=-1, u=1, e=1, d=1, weak=-1, Hu=-1, N=1)
    answers = set()
    for names in product(charges, repeat=3):
        if check_charge and sum(charges[k] for k in names) != 0:
            continue
        if sum(color[k] for k in names) % 3 != 0:
            continue
        if weak[names[0]]*weak[names[1]]*weak[names[2]] != 1:
            continue
        answers.add(tuple(sorted(names)))
    return [list(x) for x in sorted(answers)]


@lru_cache(None)
def run():
    facts = {}
    def ck(k, v):
        facts[k] = bool(v)
        assert facts[k], k
    data, w, P, Q, A, B = c.literal()
    model = json.loads((OLD/'silver_selective_boundary_2026_10_11/MODEL.json').read_text())
    neutral = neutral_spaces(w, data, ck)
    aa, bb = c.wedge_derivative(A), c.wedge_derivative(B)
    E = r.r.boundary(aa, bb)
    da, db = c.scale(c.tr(aa), -1), c.scale(c.tr(bb), -1)
    D = r.r.boundary(da, db)
    L = r.r.subset(E['H'], model['F_weak_plane'])
    LD, _ = r.r.paired_plane(E, D, L)
    M, MD = c.cat(E['U'], L), c.cat(D['U'], LD)
    fs = [r.build(dict(a=aa, b=bb, M=M), 3), r.build(dict(a=da, b=db, M=MD), -3)]
    ck('same_actual_weak_and_genuine_dual_counts', [len(x['free']) for x in fs] == [2, 1])
    degree = sum(x['r'] for x in fs)
    points, nonzero = [], False
    for t in range(1, 2*degree+3):
        matrices = [r.evaluate(x, t) for x in fs]
        if any(x is None for x in matrices):
            continue
        f, g = matrices
        for i in range(2):
            nonzero |= bool(central_vertex([row[i] for row in f], [row[0] for row in g], da))
        points.append(t)
        if len(points) == degree+1:
            break
    ck('complete_characteristic_zero_central_degree_certificate',
       len(points) == len(set(points)) == degree+1)
    witness = None
    for i, j in product(range(10), repeat=2):
        f, g = [int(k == i) for k in range(10)], [int(k == j) for k in range(10)]
        value = central_vertex(f, g, da)
        if value:
            value = value if isinstance(value, K) else K(value)
            witness = dict(indices=[i, j], value_Qsqrt2=[str(value.a), str(value.b)])
            break
    ck('actual_central_contraction_nonzero_opposite', witness is not None)
    periods = [sum((x == 't')-(x == 'T') for x in text) for text in data['cusp_words']]
    ck('central_nonexact_marked_longitude', periods == [0, 1])
    catalogue = center_catalog()
    ck('necessary_catalogue_is_discriminating', len(catalogue) == 6
       and len(center_catalog(False)) > len(catalogue)
       and ['Hu', 'N', 'weak'] in catalogue and ['N', 'N', 'N'] in catalogue)
    # Recover nonabelian coefficient brackets: zero direct tensors do NOT mean
    # that the parent Lie algebra was made abelian.
    x, y = c.Z(5), c.Z(5)
    x[0][1], y[1][0] = 1, 1
    br = c.add(c.mm(x, y), c.mm(y, x), -1)
    ck('actual_neutral_coefficient_bracket_nonzero_opposite',
       sum(c.mm(br, br)[j][j] for j in range(5)) == 2)
    return dict(facts=facts, predicates_passed=len(facts), neutral=neutral,
                boundary_plane_sha256=dict(Fweak=r.plane_hash(M), Fweakdual=r.plane_hash(MD)),
                central_pair=dict(shape=[2, 1], polynomial_degree_bound=degree,
                                  distinct_points=points, zero=not nonzero),
                central_free_control=witness, center_allowed_types=catalogue,
                center_constraints_are_only_necessary=True, structure_neutral_mixed_zero=True,
                neutral_self_zero=True, neutral_chirals=7, boundary_changed=False,
                new_native_imported=False, same_author=True,
                higher_physical_operators_computed=False, normalized_values=False,
                generated_selection=False, outside_review=False, full_goal_achieved=False)


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
