#!/usr/bin/env python3
"""Sealed exact diagnostic controls. No foreign scientific producer imported."""
from itertools import combinations
from math import comb
import json
from sympy import Matrix, Rational, diag, diff, eye, expand, symbols, zeros


def row_polynomial_action(M, n):
    """Literal sep16 convention, independently implemented by binomial sums."""
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    S = zeros(n+1)
    for j in range(n+1):
        for u in range(n-j+1):
            for v in range(j+1):
                S[u+v, j] += (comb(n-j, u)*comb(j, v)*a**(n-j-u)
                              * b**u * c**(j-v) * d**v)
    return S


def column_polynomial_action(M, n):
    return row_polynomial_action(M.T, n)


def coefficient_controls():
    A, B = Matrix([[1, 1], [0, 1]]), Matrix([[1, 0], [1, 1]])
    C = A*B
    assert A.det() == B.det() == C.det() == 1
    rows = []
    for n in range(5):
        S_A, S_B, S_C = [row_polynomial_action(M, n) for M in (A, B, C)]
        H_A, H_B, H_C = [column_polynomial_action(M, n) for M in (A, B, C)]
        assert S_C == S_B*S_A and H_C == H_A*H_B
        assert row_polynomial_action(A.inv(), n) == S_A.inv()
        assert column_polynomial_action(B.inv(), n) == H_B.inv()
        wrong = S_A*S_B*S_C.inv()-eye(n+1)
        assert (wrong == zeros(n+1)) == (n == 0)
        rows.append({"degree": n, "row_action_reverses_composition": True,
                     "column_action_preserves_composition": True,
                     "transformed_c_equals_ab_relation_fails": n > 0,
                     "wrong_relation_residual_rank": int(wrong.rank())})
    return rows


def commutant_control():
    m = diag(2, 3, 5, 7, Rational(1, 210))
    n = eye(5)
    for i in range(4):
        n[i, i+1] = 1
    generators = (m, n)
    columns = []
    for i in range(5):
        for j in range(5):
            E = zeros(5); E[i, j] = 1
            columns.append(Matrix([entry for M in generators for entry in E*M-M*E]))
    rank = Matrix.hstack(*columns).rank()
    assert rank == 24 and m.det() == n.det() == 1
    for k in range(1, 5):
        for M in generators:
            assert M[k:5, :k] == zeros(5-k, k)
    assert (m-eye(5)).det() != 0 and (m.inv().T-eye(5)).det() != 0
    return {"SL5": True, "commutant_dimension": 25-int(rank),
            "proper_invariant_flag_dimensions": [1, 2, 3, 4],
            "fixed_vectors_both_sides": [0, 0],
            "figure_eight_module": False, "credit": "R83 M4"}


def axis_control():
    x, y, a, c, d, J1, J2 = symbols("x y a c d J1 J2", real=True)
    V = a*(x*x+y*y)+c*(x**4+y**4)+d*x*x*y*y-J1*x-J2*y
    transverse_x = diff(V, y).subs(y, 0)
    transverse_y = diff(V, x).subs(x, 0)
    assert transverse_x == -J2 and transverse_y == -J1
    assert expand(c*(x*x+y*y)**2+(d-2*c)*x*x*y*y
                  -c*(x**4+y**4)-d*x*x*y*y) == 0
    return {"x_axis_transverse_derivative": str(transverse_x),
            "y_axis_transverse_derivative": str(transverse_y),
            "finite_quartic_not_exact_generic_source_selector": True,
            "zero_source_fixed_radius_axis_preference_retained": True,
            "credit": "R83 M1"}


def punctured_sphere_relative(N, negative):
    """H2 boundary inclusion and H0 LES maps, not a physical source chooser."""
    negative = tuple(negative)
    assert 0 < len(negative) < N and len(set(negative)) == len(negative)
    assert all(0 <= i < N for i in negative)
    # First N-1 spheres are a basis; last is minus their sum.
    boundary_to_H2 = Matrix.hstack(eye(N-1), -Matrix.ones(N-1, 1))
    assert boundary_to_H2*Matrix.ones(N, 1) == zeros(N-1, 1)
    assert boundary_to_H2.rank() == N-1
    inclusion = boundary_to_H2[:, list(negative)]
    H0_boundary_to_bulk = Matrix.ones(1, len(negative))
    r2, r0 = inclusion.rank(), H0_boundary_to_bulk.rank()
    b1, b2 = len(negative)-r0, N-1-r2
    chi = N-2*len(negative)
    assert r2 == len(negative) and r0 == 1
    assert b2-b1 == chi
    return {"balls": N, "negative_spheres": list(negative),
            "b1_relative": int(b1), "b2_relative": int(b2),
            "b0_relative": 0, "b3_relative": 0, "relative_Euler": int(chi)}


def relative_controls():
    rows = []
    for N in range(2, 9):
        for k in range(1, N):
            for subset in combinations(range(N), k):
                row = punctured_sphere_relative(N, subset)
                complement = tuple(i for i in range(N) if i not in subset)
                dual = punctured_sphere_relative(N, complement)
                assert row["relative_Euler"] == -dual["relative_Euler"]
                assert row["b1_relative"] == dual["b2_relative"]
                # Equal positive charges and equal negative charges, total zero.
                charges = [-Rational(N-k, k) if i in subset else Rational(1) for i in range(N)]
                assert sum(charges) == 0
                rows.append(row)
    return rows


def exterior_differential_control():
    x, y, z, q = symbols("x y z q", real=True)
    coordinates = (x, y, z)
    f = x*x+y*y-2*z*z+x*y*z
    gradient = [diff(f, s) for s in coordinates]
    assert any(a != 0 for a in gradient)
    assert sum(diff(f, s, 2) for s in coordinates) == 0
    bases = [tuple(combinations(range(3), k)) for k in range(4)]

    def D(k, coefficient_vector):
        out = zeros(len(bases[k+1]), 1)
        for j, indices in enumerate(bases[k]):
            for a, coordinate in enumerate(coordinates):
                if a in indices:
                    continue
                destination = tuple(sorted((a,)+indices))
                sign = (-1)**sum(i < a for i in indices)
                coefficient = diff(coefficient_vector[j], coordinate)+q*gradient[a]*coefficient_vector[j]
                out[bases[k+1].index(destination)] += sign*coefficient
        return out.applyfunc(expand)

    checked = 0
    for k in range(2):
        for j in range(len(bases[k])):
            v = zeros(len(bases[k]), 1); v[j] = 1+x*y+z*z
            assert D(k+1, D(k, v)) == zeros(len(bases[k+2]), 1)
            checked += 1
    return {"nonconstant_local_harmonic_f": str(f),
            "D_squared_zero_test_forms": checked,
            "bulk_gauge_curvature": 0,
            "global_sourced_Poisson_solution_computed": False,
            "OA_source_law_derived": False}


def torus_scope_control():
    rows = []
    for cusps in (1, 2, 4, 12):
        boundary_chi = cusps*(1-2+1)
        chi_M = Rational(boundary_chi, 2)
        for annuli in (0, 2, 4, 8):
            chi_minus = annuli*(1-1)
            assert chi_M-chi_minus == 0
            rows.append({"torus_cusps": cusps, "annuli": annuli, "relative_Euler": 0})
    return rows


def run():
    print("COEFFICIENT", json.dumps(coefficient_controls()), flush=True)
    print("COMMUTANT", json.dumps(commutant_control()), flush=True)
    print("AXIS", json.dumps(axis_control()), flush=True)
    rows = relative_controls()
    diagnostic = punctured_sphere_relative(5, (4,))
    reversed_diagnostic = punctured_sphere_relative(5, (0, 1, 2, 3))
    print("RELATIVE", json.dumps({"proper_partitions_checked": len(rows),
          "all_rows": rows, "diagnostic_not_OA_state": diagnostic,
          "sign_reversed": reversed_diagnostic}), flush=True)
    print("FLAT_DIFFERENTIAL", json.dumps(exterior_differential_control()), flush=True)
    print("TORUS_SCOPE", json.dumps(torus_scope_control()), flush=True)
    print("SUMMARY", json.dumps({"elementary_controls_verified": True,
          "flatness_alone_not_universal_boundary_index_kill": True,
          "known_torus_annulus_obstruction_retained": True,
          "foreign_censuses_verified": False, "derived_source_or_domain": False,
          "parameter_free_SM_derived": False, "full_physical_theory_derived": False}), flush=True)
    print("PASS: exact scoped controls, not physical-theory completion", flush=True)


if __name__ == "__main__":
    run()
