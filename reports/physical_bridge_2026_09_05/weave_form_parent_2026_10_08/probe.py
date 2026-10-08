"""Exact finite benchmark; global analytic and physical duties stay priced."""
from collections import Counter
from functools import lru_cache
import json
import sympy as s


def quaternion_complex():
    eye = s.eye(2)
    a = s.diag(s.I, -s.I)
    b = s.Matrix([[0, 1], [-1, 0]])
    c = a*b
    group = [eye, -eye, a, -a, b, -b, c, -c]
    def pos(m):
        return group.index(m)
    mul = [[pos(g*h) for h in group] for g in group]
    vertices = [(0, 1), (2, 3), (4, 5), (6, 7)]
    vertex = {q: k for k, v in enumerate(vertices) for q in v}
    d1, d2 = s.zeros(4, 16), s.zeros(16, 8)
    for q in range(8):
        qi, qj = mul[q][2], mul[q][4]
        d1[vertex[qi], q] += 1
        d1[vertex[q], q] -= 1
        d1[vertex[qj], 8+q] += 1
        d1[vertex[q], 8+q] -= 1
        d2[q, q] += 1
        d2[8+qi, q] += 1
        d2[qj, q] -= 1
        d2[8+q, q] -= 1
    equivariant = True
    traces = []
    for g in range(8):
        p2, p1, p0 = s.zeros(8), s.zeros(16), s.zeros(4)
        for q in range(8):
            gq = mul[g][q]
            p2[gq, q] = 1
            p1[gq, q] = p1[8+gq, 8+q] = 1
        for v in range(4):
            p0[vertex[mul[g][vertices[v][0]]], v] = 1
        equivariant &= d1*p1 == p0*d1 and d2*p2 == p1*d2
        traces.append(int(2-p0.trace()+p1.trace()-p2.trace()))
    return group, mul, d1, d2, equivariant, traces


def inner(a, b):
    return s.Rational(sum(x*y for x, y in zip(a, b)), 8)


def adjoint_character(group):
    out = []
    for g in group:
        x, x2, x3 = [3*(g**n).trace() for n in (1, 2, 3)]
        w2 = (x*x-x2)/2
        w3 = (x**3-3*x*x2+2*x3)/6
        out.append(int(11+x*x-1+6*w2+12*x+2*w3))
    return out


def parent_slots(twist=1):
    left = [("lambda_plus", 1, 1), ("lambda_minus", 1, -1),
            ("psi_B1", -1, 0), ("psi_B2", -1, 0)]
    rows = []
    for name, q45, qa in left:
        rows.append({"slot": name, "q45": q45, "qa": qa,
                     "qt": q45+twist*qa, "independent_left": True})
    return rows


def dual_key(key):
    colour, weak, x, y = key
    return (-colour if abs(colour) == 3 else colour, weak, -x, -y)


def charge_asymmetry(left):
    return {k: left[k]-left[dual_key(k)] for k in set(left)|{dual_key(k) for k in left}}


def gauge_roster():
    f = [(1, 0), (0, 1), (-1, -1)]
    z = (0, 0)
    one, rho = Counter(), Counter()
    def add(dst, colour, weak, w, n=1):
        dst[(colour, weak, *w)] += n
    add(one, 8, 1, z)
    add(one, 1, 3, z)
    add(one, 1, 1, z, 2)
    add(rho, 1, 2, z, 4)
    for i in range(3):
        add(rho, 3, 2, tuple(-x for x in f[i]))
        add(rho, -3, 2, f[i])
        for j in range(3):
            if i != j:
                w = tuple(f[i][k]-f[j][k] for k in range(2))
                add(one, 1, 1, w)
                add(rho, 1, 2, w)
            if i <= j:
                w = tuple(f[i][k]+f[j][k] for k in range(2))
                add(one, 3, 1, w)
                add(one, -3, 1, tuple(-x for x in w))
    return one, rho


def dimension(rows):
    return sum(abs(k[0])*k[1]*v for k, v in rows.items())


def sl3_adjoint():
    def e(i, j):
        x = s.zeros(3)
        x[i, j] = 1
        return x
    basis = [s.diag(1, -1, 0), s.diag(0, 1, -1)] + [
        e(i, j) for i, j in [(0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1)]]
    coords = s.Matrix.hstack(*(m.reshape(9, 1) for m in basis))
    mats = []
    for a in basis:
        mats.append(s.Matrix.hstack(*[coords.gauss_jordan_solve((a*b-b*a).reshape(9, 1))[0] for b in basis]))
    gram = s.Matrix(8, 8, lambda i, j: s.trace(basis[i].H*basis[j]))
    return basis, mats, gram


def invariant_bilinears(generators):
    n = generators[0].rows
    equations = []
    for a in generators:
        for i in range(n):
            for j in range(n):
                row = [0]*(n*n)
                for k in range(n):
                    row[k*n+j] += a[k, i]
                    row[i*n+k] += a[k, j]
                equations.append(row)
    return [v.reshape(n, n) for v in s.Matrix(equations).nullspace()]


def invariant(m, generators):
    return all(a.T*m+m*a == s.zeros(m.rows) for a in generators)


def symmetric_mass_dimension(basis):
    if not basis:
        return 0
    size = basis[0].rows
    constraints = s.Matrix.hstack(*[(b-b.T).reshape(size*size, 1) for b in basis])
    return len(basis)-constraints.rank()


@lru_cache(None)
def run():
    group, mul, d1, d2, equivariant, h1 = quaternion_complex()
    rho_char = [int(g.trace()) for g in group]
    hol = [1+x for x in rho_char]
    adj = adjoint_character(group)
    chars = [[1]*8, [1, 1, 1, 1, -1, -1, -1, -1],
             [1, 1, -1, -1, 1, 1, -1, -1], [1, 1, -1, -1, -1, -1, 1, 1], rho_char]
    mult = [int(inner(adj, x)) for x in chars]
    one, r = gauge_roster()
    full = one+r
    weak_count = sum(abs(k[0])*v for k, v in full.items() if k[1] == 2)
    basis3, ad3, gram = sl3_adjoint()
    sl2 = [s.diag(1, -1), s.Matrix([[0, 1], [0, 0]]), s.Matrix([[0, 0], [1, 0]])]
    bil3, bil2 = invariant_bilinears(ad3), invariant_bilinears(sl2)
    protected = s.kronecker_product(bil3[0], bil2[0])
    pg = [s.kronecker_product(a, s.eye(2)) for a in ad3] + [s.kronecker_product(s.eye(8), a) for a in sl2]
    two_gen = [s.kronecker_product(s.eye(2), a) for a in sl2]
    two_bil = invariant_bilinears(two_gen)
    eps = s.Matrix([[0, 1], [-1, 0]])
    two_mass = s.kronecker_product(eps, eps)
    wrong = s.kronecker_product(s.diag(1, -1, *([0]*6)), eps)
    single_complex = Counter({(3, 2, 1, 0): 1})
    opposite = Counter({dual_key(k): v for k, v in single_complex.items()})
    rows = parent_slots()
    t = s.symbols('t', real=True)
    u = s.Function('u')(t)
    f = s.exp(t/2)*u
    laplace = s.simplify(s.exp(-t/2)*(-s.diff(f, t, 2)+s.diff(f, t)))
    lower = lambda x: s.diff(x, t)+x/2
    upper = lambda x: -s.diff(x, t)+x/2
    sx = s.Matrix([[0, 1], [1, 0]])
    sy = s.Matrix([[0, -s.I], [s.I, 0]])
    qgrade = s.diag(1, -1)
    w = s.symbols('w', positive=True)
    branch = s.simplify((w*w)**s.Rational(-1, 2)*2*w)
    # Declared kernel/Euler profiles, not a full physical Fredholm index.
    kernels = {"W6_scalar": int(inner([3*x for x in rho_char], chars[0])),
               "W6_one_Hodge_type": int(inner([3*x for x in rho_char], hol)),
               "adjoint_scalar": mult[0], "adjoint_one_Hodge_type": int(inner(adj, hol)),
               "adjoint_real_degree1_complexification": int(inner(adj, h1))}
    facts = {
        "Q8_commutator_is_minus_I": group[2]*group[4]*group[2].inv()*group[4].inv() == -s.eye(2),
        "chain_boundaries_compose_to_zero": d1*d2 == s.zeros(4, 8),
        "chain_ranks_three_seven": [d1.rank(), d2.rank()] == [3, 7],
        "all_eight_deck_maps_equivariant": equivariant,
        "compact_H1_six_and_genus_three": 16-d1.rank()-d2.rank() == 6 and 4-16+8 == -4,
        "H1_character_two_trivial_two_rho": h1 == [2+2*x for x in rho_char],
        "holomorphic_character_one_trivial_one_rho": hol[0] == 3 and inner(hol, rho_char) == 1 and inner(hol, chars[0]) == 1,
        "adjoint_character_rebuilt_through_exteriors": adj == [248, 24, 28, 28, 28, 28, 28, 28],
        "complete_Q8_adjoint_multiplicities": mult == [55, 27, 27, 27, 56],
        "complete_form_kernel_roster": kernels == {"W6_scalar": 0, "W6_one_Hodge_type": 3, "adjoint_scalar": 55, "adjoint_one_Hodge_type": 111, "adjoint_real_degree1_complexification": 222},
        "family_three_not_multiplied_again": kernels['adjoint_one_Hodge_type'] != 55+3*56,
        "all_four_independent_left_parent_slots_retained": len(rows) == 4 and [x['qt'] for x in rows] == [2, 0, -1, -1],
        "untwisted_dictionary_detected": [x['qt'] for x in parent_slots(0)] != [2, 0, -1, -1],
        "form_symbol_clifford": sx*sx == s.eye(2) and sy*sy == s.eye(2) and sx*sy+sy*sx == s.zeros(2),
        "form_symbol_graded": sx*qgrade+qgrade*sx == s.zeros(2) and sy*qgrade+qgrade*sy == s.zeros(2),
        "square_root_pole_pulls_back_regular": branch == 2,
        "form_radial_squared_mass_quarter": laplace == -s.diff(u, t, 2)+u/4 and s.simplify(upper(lower(u))-laplace) == 0 and s.simplify(lower(upper(u))-laplace) == 0,
        "form_radial_not_ordinary_spin_massless": s.simplify(laplace+s.diff(u, t, 2)) == u/4,
        "gauge_subgroup_dimensions_all_retained": dimension(one) == 55 and dimension(r) == 56 and dimension(full) == 111,
        "all_generic_SM_charges_pair_in_FORM_sector": all(v == 0 for v in charge_asymmetry(full).values()),
        "FORM_weak_mod_two_even": weak_count == 28 and weak_count % 2 == 0,
        "single_complex_left_Weyl_is_unpaired": any(v != 0 for v in charge_asymmetry(single_complex).values()),
        "adding_independent_left_mirror_changes_census": all(v == 0 for v in charge_asymmetry(single_complex+opposite).values()),
        "family_adjoint_invariant_bilinear_unique_symmetric": len(bil3) == 1 and bil3[0].T == bil3[0] and bil3[0].det() != 0,
        "weak_doublet_invariant_bilinear_unique_skew": len(bil2) == 1 and bil2[0].T == -bil2[0] and symmetric_mass_dimension(bil2) == 0,
        "protected_16_bilinear_invariant_skew_full_rank": invariant(protected, pg) and protected.T == -protected and protected.rank() == 16,
        "protected_symmetric_mass_zero": protected+protected.T == s.zeros(16) and len(bil3)*len(bil2) == 1,
        "two_doublets_have_one_symmetric_mass": len(two_bil) == 4 and symmetric_mass_dimension(two_bil) == 1,
        "two_doublet_mass_invariant_full_rank": invariant(two_mass, two_gen) and two_mass.T == two_mass and two_mass.rank() == 4,
        "wrong_family_bilinear_rejected": not invariant(wrong, pg),
        "nonzero_family_gauge_vertex_retained": any(a != s.zeros(16) for a in pg[:8]),
        "positive_kinetic_Gram": all(gram[:n, :n].det() > 0 for n in range(1, 9)),
    }
    result = {"facts": {k: bool(v) for k, v in facts.items()}, "predicates_passed": sum(bool(x) for x in facts.values()),
              "cover_H1_character": h1, "cover_holomorphic_character": hol,
              "adjoint_Q8_multiplicities": mult, "form_kernel_dimensions": kernels,
              "parent_left_twisted_charges": [x['qt'] for x in rows],
              "gauge_dimensions": [dimension(one), dimension(r), dimension(full)],
              "weak_doublets_in_FORM_sector": weak_count,
              "bilinear_profile": {"ad8_invariants": len(bil3), "doublet_invariants": len(bil2), "protected_symmetric_masses": 0, "two_doublet_symmetric_masses": symmetric_mass_dimension(two_bil), "protected_lower_bound_complex_components": 16},
              "zero_angular_form_squared_mass": "1/4",
              "complex_SM_asymmetry_in_FORM_sector": 0,
              "complete_companion_spectrum_computed": False,
              "full_curved_interacting_parent_certified": False,
              "global_physical_Fredholm_index_certified": False,
              "generated_twist_or_action_selected": False,
              "physical_chiral_SM_derived": False,
              "nonauthor_acceptance": False}
    return result


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if all(result['facts'].values()) else 1)
