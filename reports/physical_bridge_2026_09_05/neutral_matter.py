"""R54 reuses F15: finite obstruction/action controls, not a PDE or mass solver."""
from functools import lru_cache
from pathlib import Path
import importlib.util
import json
import sympy as s

BASE = Path(__file__).parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    out = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(out)
    return out


adapter = load('r54_f15_adapter', BASE/'received_r54/reports/projective_deformation_tangent_2026_09_25/verify_v2.py')
v = adapter.v
f11 = load('r54_f11_symbolic', BASE/'received_r46/reports/projective_cusp_spectrum_2026_09_21/verify.py')
f05 = load('r54_parent_roots', BASE/'received_r46/reports/parent_twist_gap_2026_09_20/verify.py')
CASES = ((14, 1, s.I), (14, -1, s.I), (14, 1, -s.I),
         (14, -1, -s.I), (34, 1, -s.S.One), (34, -1, -s.S.One))


def zero(a):
    return all(s.simplify(x) == 0 for x in (list(a) if isinstance(a, s.MatrixBase) else [a]))


@lru_cache(None)
def obstruction(middle, embedding, phase, dual):
    k, q0, rho, _ = v.context(middle, embedding)
    raw = v.f10.generators()
    drho = tuple(v.dm(q0*g.diff(v.f10.q).subs(v.f10.q, q0), k) for g in raw)
    tangent = v.stack(*(v.coords(d*r.inv()) for d, r in zip(drho, rho)))
    m = v.matter_complex(rho, phase, dual)
    dj = v.matter_derivative(rho, phase, dual, tangent)
    scalar = m['left']*dj*m['H']
    # Distinct existing symbolic Fox pipeline, differentiated before specialization.
    bq, jq = f11.complex_matrices(f11.q, phase, dual)
    b = v.dm(bq.subs(f11.q, q0), k)
    j = v.dm(jq.subs(f11.q, q0), k)
    db = v.dm((f11.q*bq.diff(f11.q)).subs(f11.q, q0), k)
    direct = v.dm((f11.q*jq.diff(f11.q)).subs(f11.q, q0), k)
    image = dj*m['H']
    checks = {
        'actual_complex_matches_independent_F11': (b-m['B']).is_zero_matrix and (j-m['R']).is_zero_matrix,
        'rank_B4_J3': b.rank() == 4 and j.rank() == 3,
        'one_H1_one_H2': m['H'].shape == (8, 1) and m['left'].shape == (1, 4),
        'chain_identity': (j*b).is_zero_matrix,
        'independent_derivative_matches': (dj-direct).is_zero_matrix,
        'differentiated_chain_identity': (dj*b+j*db).is_zero_matrix,
        'boundary_shift_invariance': (m['left']*dj*b).is_zero_matrix,
        'nonzero_log_q_obstruction': scalar.rank() == 1,
        'no_first_order_lift': v.cat(j, image).rank() == 4,
        'nonzero_matter_class': v.cat(b, m['H']).rank() == 5 and (j*m['H']).is_zero_matrix,
    }
    return dict(checks=checks, raw_basis_dependent_log_q_obstruction=v.display(scalar),
                q=str(q0), phase=str(phase), dual=dual)


@lru_cache(None)
def toy_controls():
    t, a, b = s.symbols('t a b', real=True)
    simple, double = s.diag(1, t), s.diag(1, t*t)
    left = s.Matrix([[0, 1]])
    beta = s.Matrix([0, 1])
    D = s.Matrix([[1], [0], [0]])
    source = s.Matrix([2, 3, 0])
    h = source-D*(D.T*D).inv()*D.T*source
    shifted = source+D*s.Matrix([a])
    norm = (shifted.T*shifted)[0]
    exact = s.Matrix([2, 0, 0])
    return {
        'same_isolated_rank_jump': simple.subs(t, 0).rank() == double.subs(t, 0).rank() == 1
            and simple.subs(t, 2).rank() == double.subs(t, 2).rank() == 2,
        'simple_zero_obstructs': (left*simple.diff(t).subs(t, 0)*beta)[0] == 1,
        'double_zero_first_derivative_vanishes': (left*double.diff(t).subs(t, 0)*beta)[0] == 0,
        'zero_obstruction_not_nonlinear_survival': double.det() == t*t,
        'mixed_residual_survives_exact_relaxation': h == s.Matrix([0, 3, 0]) and zero(norm-9-(a+2)**2),
        'exact_source_can_be_removed': zero(exact-D*(D.T*D).inv()*D.T*exact),
        'unit_dual_overlap_positive': (h.T*source)[0]/3 == 3,
        'nonzero_basis_rescaling_changes_coefficient': (2*left*simple.diff(t).subs(t, 0)*(3*beta))[0] == 6,
    }


@lru_cache(None)
def parent_controls():
    roots = f05.e8_roots()
    eta = tuple(s.Rational(x, 2) for x in (-1, 1, 1, 1, 1, -1, 1, 1))
    neutral = (0, 0, 0, 0, 0, 1, -1, 0)
    summed = tuple(x+y for x, y in zip(neutral, eta))
    opposite = tuple(-x for x in summed)
    # A defining-module embedding for the coefficient contraction, not an E8 model.
    A = s.diag(1, -1, 0, 0, 0)
    B, G = s.zeros(5), s.zeros(5)
    B[0, 4] = 1
    G[4, 0] = 1
    comm = A*B-B*A
    eps, aa, bb = s.symbols('eps aa bb', real=True)
    residual = eps**2*aa*bb*comm
    potential = s.trace(residual.conjugate().T*residual)
    return {
        'actual_E8_root_triple': all(x in roots for x in (eta, neutral, summed, opposite)),
        'root_string_nonzero_bracket': sum(x*y for x, y in zip(neutral, eta)) == -1,
        'neutral_root_in_structure_A3': all(x == 0 for x in neutral[:5]),
        'charged_roots_have_opposite_spinor_weights': eta[:5] == tuple(-x for x in opposite[:5])
            and all(abs(x) == s.Rational(1, 2) for x in eta[:5]),
        'trace_vertex_is_defining_action': s.trace(G*comm) == 1,
        'pure_scalar_residual_square_is_quartic': s.expand(potential).coeff(eps, 4) == aa**2*bb**2
            and s.expand(potential).coeff(eps, 3) == 0,
        'wrong_commuting_action_rejected': not zero(comm) and not zero(G*comm),
    }


def report():
    cases = [obstruction(*case, dual) for case in CASES for dual in (False, True)]
    extra = dict(toy=toy_controls(), parent=parent_controls())
    checks = [bool(x) for row in cases for x in row['checks'].values()]
    checks += [bool(x) for group in extra.values() for x in group.values()]
    return dict(cases=cases, controls=extra, passed=sum(checks), total=len(checks),
                all_checks_pass=all(checks), existing_F15_result_received=True,
                global_analytic_proof_machine_verified=False,
                numerical_normalized_Yukawa_computed=False, nearby_pole_mass_law_proved=False,
                physical_chirality_derived=False)


if __name__ == '__main__':
    result = report()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['all_checks_pass'] else 1)
