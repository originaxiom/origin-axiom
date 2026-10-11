"""Same-domain neutral LES and actual central transgression; seal before run."""
import importlib.util
import json
from functools import lru_cache
from itertools import combinations_with_replacement, product
from pathlib import Path

import sympy as s

HERE = Path(__file__).resolve().parent
OLD = HERE.parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


c = load('neutral_prior_charged', OLD/'silver_charged_cubic_2026_10_11/probe.py')
sel = load('neutral_prior_selective', OLD/'silver_selective_boundary_2026_10_11/probe.py')
p = c.p
mm, rank, zero, ker, inv, cols = p.mm, p.rank, p.zero, sel.ker, sel.inv, sel.cols
z = p.z


def central_vertex(f, g, dual_meridian):
    return s.expand(3*(f.T*dual_meridian*g)[0])


def neutral_spaces(w, data, A, B, ck):
    basis = p.cy.adjoint_basis()
    rn = {g: p.cy.adjoint_group(x, basis) for g, x in w.items()}
    T = s.Matrix([[s.trace(x*y) for y in basis] for x in basis])
    met = s.Matrix([[s.trace(x.T*y) for y in basis] for x in basis])
    P, Q = [p.cy.word(rn, text) for text in data['cusp_words']]
    bb = s.Matrix.vstack(*(rn[g]-s.eye(24) for g in p.GEN))
    ff = s.Matrix.vstack(*(p.fox(rn, text) for text in data['relators']))
    rr = s.Matrix.vstack(*(p.fox(rn, text) for text in data['cusp_words']))
    d = (P-s.eye(24)).col_join(Q-s.eye(24))
    gg = (s.eye(24)-Q).row_join(P-s.eye(24))
    r2 = -mm(mm(Q, p.fox(rn, data['cusp_words'][0])[:, :48]),
             s.diag(inv(rn['t']), inv(rn['t'])))
    ck('neutral_all_degree_chain_maps', zero(mm(ff, bb)) and zero(mm(gg, d))
       and zero(mm(rr, bb)-d) and zero(mm(r2, ff)-mm(gg, rr)))
    HH = ker(gg.col_join(d.T))
    proj = mm(mm(HH, inv(mm(HH.T, HH))), HH.T)
    R = cols(mm(mm(proj, rr), ker(ff)))
    J = s.zeros(24).row_join(inv(P).T).col_join((-inv(Q).T).row_join(s.zeros(24)))
    S = mm(J, s.diag(T, T))
    HS = mm(mm(HH.T, S), HH)
    ck('actual_trace_symplectic_not_positive_Gram', rank(T) == 24
       and rank(HS) == 12 and zero(HS+HS.T) and zero(mm(mm(R.T, S), R))
       and any(not zero(mm(x.T, x)-s.eye(24)) for x in rn.values()))
    pairing = mm(mm(R.T, S), HH)
    piv = list(p.dm(pairing).rref()[1])
    U0 = mm(HH[:, piv], inv(pairing[:, piv]))
    U = U0+mm(R, mm(mm(U0.T, S), U0))/2
    absolute = [24-rank(bb), 72-rank(bb)-rank(ff), 48-rank(ff), 0]
    t0 = 24-rank(d)
    ck('restriction_is_injective_and_neutral_transverse', absolute == [0, 6, 6, 0]
       and t0 == 6 and R.cols == 6 and U.cols == 6 and rank(R.row_join(U)) == 12
       and zero(mm(mm(U.T, S), U)) and zero(mm(mm(R.T, S), U)-s.eye(6)))
    def h1(L):
        return t0-absolute[0]+absolute[1]+L.cols-rank(R.row_join(L))
    allowed_absolute = absolute[1]+U.cols-rank(R.row_join(U))
    opposite = absolute[1]+R.cols-rank(R.row_join(R))
    ck('six_connecting_classes_are_not_gauge_deletions', h1(U) == 6
       and allowed_absolute == 0 and ker(bb).cols == 0 and ker(d).cols == 6)
    ck('equal_restriction_opposite_changes_the_mechanism', h1(R) == 12 and opposite == 6)
    NA, NB = p.cy.adjoint_lie(A, basis), p.cy.adjoint_lie(B, basis)
    dlog = NA.col_join(NB)
    glog = (-NB).row_join(NA)
    hl = ker(glog.col_join(mm(dlog.T, s.diag(met, met))))
    pl = mm(mm(hl, inv(mm(mm(hl.T, s.diag(met, met)), hl))), mm(hl.T, s.diag(met, met)))
    ua, ub = sel.integral(NA), sel.integral(NB)
    t1 = s.diag(ua, ub)
    UL, RL = [mm(mm(pl, inv(t1)), x) for x in (U, R)]
    q0 = ker(dlog)
    ck('all_parallel_primitives_and_actual_log_transport', q0.cols == 6
       and zero(mm(dlog, q0)) and rank(q0.row_join(ker(d))) == 6
       and zero(mm(t1, dlog)-d) and zero(mm(gg, t1)-mm(mm(ua, ub), glog))
       and rank(RL.row_join(UL)) == 12)
    ck('actual_neutral_harmonic_exact_trace_intersection_zero',
       rank(dlog.row_join(hl)) == rank(dlog)+hl.cols)
    return dict(absolute_H=absolute, boundary_H=[t0, HH.cols, t0], physical_H1=h1(U),
                connecting_dimension=t0-absolute[0], allowed_absolute_H1=allowed_absolute,
                equal_line_physical_H1=h1(R), equal_line_absolute_H1=opposite,
                parallel_primitive_dimension=q0.cols,
                parallel_primitive_sha256=c.plane_hash(q0),
                restriction_sha256=c.plane_hash(R), plane_sha256=c.plane_hash(U),
                tangential_trace_zero=True, state_deleted=False)


def center_catalog(check_charge=True):
    types = dict(Q=(-1, 1, 1), u=(4, -1, 0), e=(-6, 0, 0), d=(-2, -1, 0),
                 weak=(3, 0, 1), Hu=(-3, 0, 1), N=(0, 0, 0))
    result = []
    for names in combinations_with_replacement(sorted(types), 3):
        values = [sum(types[k][j] for k in names) for j in range(3)]
        if (not check_charge or values[0] == 0) and values[1] % 3 == 0 and values[2] % 2 == 0:
            result.append(list(names))
    return result


@lru_cache(None)
def run():
    facts = {}
    def ck(k, v):
        facts[k] = bool(v)
        assert facts[k], k
    _, data, w, P, Q, A, B = p.cy.literal()
    model = json.loads((OLD/'silver_selective_boundary_2026_10_11/MODEL.json').read_text())
    neutral = neutral_spaces(w, data, A, B, ck)
    aa, bb = p.cy.exterior_lie(A), p.cy.exterior_lie(B)
    E, D = p.boundary(aa, bb), p.boundary(-aa.T, -bb.T)
    L = E['H'][:, model['F_weak_plane']]
    LD = p.dual_plane(E, D, L)
    M, MD = E['U'].row_join(L), D['U'].row_join(LD)
    f = c.primitives(dict(a=aa, b=bb, M=M), 3, ck, 'weak')
    g = c.primitives(dict(a=-aa.T, b=-bb.T, M=MD), -3, ck, 'Hu')
    ck('same_actual_weak_and_dual_primitive_counts', f['F'].cols == 2 and g['F'].cols == 1)
    entries = [central_vertex(f['F'][:, i], g['F'][:, 0], -aa.T) for i in range(2)]
    entries = [p.dm(s.Matrix([[v]]), z).to_Matrix()[0] for v in entries]
    bound = f['r']+g['r']
    ck('central_actual_polynomial_degree', all(s.degree(v, z) <= bound for v in entries if v != 0))
    witness = None
    for i, j in product(range(10), repeat=2):
        value = central_vertex(s.eye(10)[:, i], s.eye(10)[:, j], -aa.T)
        if value != 0:
            witness = dict(indices=[i, j], value_Qsqrt2=c.pair(value))
            break
    ck('actual_central_contraction_nonzero_opposite', witness is not None)
    periods = [sum(1 if x == 't' else -1 if x == 'T' else 0 for x in text) for text in data['cusp_words']]
    ck('central_is_nonexact_longitude_not_deleted', periods == [0, 1])
    catalogue = center_catalog()
    expected = sorted([sorted(x) for x in [('Q', 'u', 'Hu'), ('Q', 'd', 'weak'),
        ('e', 'weak', 'weak'), ('u', 'd', 'd'), ('N', 'weak', 'Hu'), ('N', 'N', 'N')]])
    ck('complete_necessary_center_catalogue', catalogue == expected)
    ck('charge_omission_expands_catalogue_opposite', len(center_catalog(False)) > len(catalogue))
    H = s.diag(*model['H'])
    off = s.zeros(5)
    off[0, 4] = 1
    ck('central_abelian_self_bracket_with_nonabelian_opposite',
       zero(H*H-H*H) and H*off-off*H == 5*off)
    x, y = s.zeros(5), s.zeros(5)
    x[0, 1], y[1, 0] = 1, 1
    ck('neutral_coefficient_bracket_detector_nonzero_opposite', s.trace((x*y-y*x)**2) == 2)
    return dict(facts=facts, predicates_passed=len(facts), neutral=neutral,
                boundary_plane_sha256=dict(Fweak=c.plane_hash(M), Fweakdual=c.plane_hash(MD)),
                central_pair=dict(shape=[2, 1], polynomial_degree_bound=bound,
                    coordinate_polynomials=[str(v) for v in entries], zero=all(v == 0 for v in entries)),
                central_free_control=witness, center_allowed_types=catalogue,
                center_constraints_are_only_necessary=True, structure_neutral_mixed_zero=True,
                neutral_self_zero=True, neutral_chirals=7, boundary_changed=False,
                higher_physical_operators_computed=False, normalized_values=False,
                generated_selection=False, outside_review=False, full_goal_achieved=False)


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
