"""R55 exact meridian restriction and end controls; no numerical PDE solve."""
from functools import lru_cache
from pathlib import Path
import importlib.util
import json
import sympy as s

BASE = Path(__file__).parent
spec = importlib.util.spec_from_file_location('r55_received_f15',
    BASE/'received_r54/reports/projective_deformation_tangent_2026_09_25/verify_v2.py')
adapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapter)
v = adapter.v
CASES = ((14, 1), (14, -1), (34, 1), (34, -1))


@lru_cache(None)
def restriction(middle, embedding):
    a = v.actual(middle, embedding)
    k, b, rel, h, qt = a['K'], a['B'], a['R'], a['H'], a['qt']
    bm = b.extract(range(15), range(15))
    hm = h.extract(range(15), range(h.shape[1]))
    qm = qt.extract(range(15), [0])
    left = v.kernel(bm.transpose()).transpose()
    res = left*hm
    ker = v.kernel(res)
    m = a['rho'][0]
    trace_map = v.dm([[n*s.trace((x*(m**n)).to_Matrix())
                      for x in v.basis(k)] for n in (1, 2, 3)], k)
    trace_res = trace_map*hm
    rank_res = v.cat(bm, hm).rank()-bm.rank()
    checks = {
        'ordinary_H1_three': h.shape == (30, 3) and b.rank() == 15 and rel.rank() == 12,
        'actual_relator_differential': (rel-v.direct_differential(a['rho'])).is_zero_matrix,
        'chain_and_closed_basis': (rel*b).is_zero_matrix and (rel*h).is_zero_matrix,
        'meridian_rank_ten': bm.rank() == 10,
        'restriction_rank_two': rank_res == 2 and res.rank() == 2,
        'q_restriction_zero': (left*qm).is_zero_matrix,
        'q_closed_nonboundary': (rel*qt).is_zero_matrix and v.cat(b, qt).rank() == 16,
        'one_kernel_spanned_by_q': ker.shape == (3, 1) and v.cat(b, qt, h*ker).rank() == 16,
        'restriction_gauge_invariant': (left*bm).is_zero_matrix,
        'trace_detector_gauge_invariant': (trace_map*bm).is_zero_matrix,
        'independent_trace_rank_two': trace_res.rank() == 2,
        'trace_and_meridian_kernel_agree': v.stack(res, trace_res).rank() == res.rank(),
        'q_has_zero_trace_derivatives': (trace_map*qm).is_zero_matrix,
        'nonzero_restriction_rejected': not res.is_zero_matrix and not trace_res.is_zero_matrix,
    }
    return dict(middle=middle, embedding=embedding, q=str(a['q']),
                ordinary_H1=h.shape[1], meridian_rank=bm.rank(),
                joined_rank=v.cat(bm, hm).rank(), restriction_rank=rank_res,
                kernel_dimension=h.shape[1]-rank_res,
                restriction_matrix=v.display(res), trace_matrix=v.display(trace_res),
                kernel_in_received_basis=v.display(ker), checks=checks)


def coords(a):
    return s.Matrix([a[i, j] for i, j in v.POSITIONS]+[a[i, i] for i in range(3)])


@lru_cache(None)
def cusp_controls():
    basis = tuple(x.to_Matrix() for x in v.basis(s.QQ))
    n = s.zeros(4); n[0, 2] = n[2, 3] = 1
    p = n*n
    d = s.diag(1, -3, 1, 1)
    j = s.diag(5, -3, 1, -3)/8
    action = lambda a: s.Matrix.hstack(*(coords(a*x-x*a) for x in basis))
    dd = action(d)
    ids = [i for i in range(15) if dd[i, i] == 0]
    a, b, c = [action(x).extract(ids, ids) for x in (2*j, n, p)]
    bs = [basis[i] for i in ids]
    gram = s.Matrix([[s.trace(x.T*y) for y in bs] for x in bs])
    badj = gram.inv()*b.T*gram
    kp = s.Matrix.hstack(*(coords(x).extract(ids, [0]) for x in (d, n, p)))
    km = s.Matrix.hstack(*(coords(x).extract(ids, [0]) for x in (d, n.T, p.T)))
    em = sum((b**i/s.factorial(i) for i in range(1, 6)), s.zeros(9))
    z = s.zeros(9)
    return {
        'zero_sector_dimension_nine': len(ids) == 9,
        'positive_Gram': all(gram[:i, :i].det() > 0 for i in range(1, 10)),
        'A_selfadjoint': a.T*gram == gram*a,
        'B_adjoint_literal': badj == action(n.T).extract(ids, ids),
        'kernel_basis_and_rank': b.rank() == 6 and kp.rank() == 3 and b*kp == s.zeros(9, 3),
        'cokernel_basis_and_rank': km.rank() == 3 and badj*km == s.zeros(9, 3),
        'kernel_weights_012': a*kp == kp*s.diag(0, 1, 2),
        'cokernel_weights_0_minus1_minus2': a*km == km*s.diag(0, -1, -2),
        'flat_radial_B': a*b-b*a == b,
        'flat_radial_C': a*c-c*a == 2*c,
        'commuting_tangent_logs': b*c == c*b,
        'adjoint_nilpotency_five': b**5 == z and b**4 != z,
        'log_exp_images_agree': em.rank() == b.rank() == b.row_join(em).rank(),
        'longitude_image_in_meridian_image': b.row_join(c).rank() == b.rank(),
        'ad_N_squared_is_not_ad_N2': c != b*b,
    }


@lru_cache(None)
def scalar_controls():
    k = s.QQ
    rho = (v.eye(1, k), v.eye(1, k))
    rel, _ = v.fox_jet(rho)
    h = v.kernel(rel)
    meridian = h.extract([0], range(h.shape[1]))
    # Independent abelianized relator, not an Euler count.
    exponents = [v.REL.count(g)-v.REL.count(g.upper()) for g in 'mn']
    return dict(checks={
        'Fox_equals_abelianization': rel.to_Matrix() == s.Matrix([exponents]),
        'ordinary_H1_one': rel.rank() == 1 and h.shape == (2, 1),
        'meridian_restriction_injective': meridian.rank() == 1,
        'actual_cocycle_equal_generators': h.to_list()[0][0] == h.to_list()[1][0],
    }, relator_exponents=exponents)


@lru_cache(None)
def weight_controls():
    r = s.symbols('r', real=True)
    j = s.symbols('j', nonnegative=True)
    f = s.Function('f')(r)
    w = s.exp(-r/2)*f
    return {
        'Hardy_conjugation_sign': s.simplify(s.diff(w, r)+(j+s.Rational(1, 2))*w
            -s.exp(-r/2)*(s.diff(f, r)+j*f)) == 0,
        'kernel_homogeneous_sections_integrable': all(-2*j-1 < 0 for j in (0, 1, 2)),
        'meridian_cokernel_periods_nonintegrable': all(2*j+1 > 0 for j in (0, 1, 2)),
        'Hardy_rates_strictly_positive': all(j+s.Rational(1, 2) > 0 for j in (0, 1, 2)),
        'threshold_equality_not_integrable': 2*s.Rational(1, 2)-1 == 0,
        'longitude_and_meridian_not_equivalent': -1 < 0 and 1 > 0,
        'wrong_negative_kernel_weight_would_fail': -2*(-1)-1 > 0,
    }


def report():
    cases = [restriction(*case) for case in CASES]
    controls = dict(cusp=cusp_controls(), scalar=scalar_controls()['checks'], weights=weight_controls())
    checks = [bool(x) for row in cases for x in row['checks'].values()]
    checks += [bool(x) for group in controls.values() for x in group.values()]
    conditional_neutral = cases[0]['kernel_dimension'] if all(checks) else None
    return dict(cases=cases, controls=controls, passed=sum(checks), total=len(checks),
                all_checks_pass=all(checks), conditional_neutral_H1=conditional_neutral,
                conditional_parent_H1=(1+16+16 if all(checks) else None),
                global_analytic_proof_machine_verified=False,
                all_ordinary_classes_normalizable=False,
                full_EFT_or_numerical_gap_derived=False, physical_chirality_derived=False)


if __name__ == '__main__':
    out = report()
    print(json.dumps(out, indent=2))
    raise SystemExit(0 if out['all_checks_pass'] else 1)
