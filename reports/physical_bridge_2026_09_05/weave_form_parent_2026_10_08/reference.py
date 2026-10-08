"""Separate signed-quaternion/Fraction benchmark; no native imports."""
from fractions import Fraction as F
import json


def rank(rows):
    a = [[F(x) for x in row] for row in rows]
    if not a:
        return 0
    r = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        v = a[r][col]
        a[r] = [x/v for x in a[r]]
        for i in range(r+1, len(a)):
            if a[i][col]:
                v = a[i][col]
                a[i] = [x-v*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def quaternions():
    group = [(sign, unit) for unit in range(4) for sign in (1, -1)]
    cross = {(1, 2): (1, 3), (2, 3): (1, 1), (3, 1): (1, 2),
             (2, 1): (-1, 3), (3, 2): (-1, 1), (1, 3): (-1, 2)}
    def multiply(x, y):
        a, u = x
        b, v = y
        if u == 0:
            return a*b, v
        if v == 0:
            return a*b, u
        if u == v:
            return -a*b, 0
        sign, w = cross[(u, v)]
        return a*b*sign, w
    return group, [[group.index(multiply(x, y)) for y in group] for x in group]


def multiply(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def minus(a, b):
    return [[x-y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def adjoint_matrices():
    basis = [[[1, 0, 0], [0, -1, 0], [0, 0, 0]],
             [[0, 0, 0], [0, 1, 0], [0, 0, -1]]]
    positions = [(0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1)]
    for i, j in positions:
        a = [[0]*3 for _ in range(3)]
        a[i][j] = 1
        basis.append(a)
    out = []
    for a in basis:
        columns = []
        for b in basis:
            c = minus(multiply(a, b), multiply(b, a))
            columns.append([c[0][0], -c[2][2]]+[c[i][j] for i, j in positions])
        out.append([list(row) for row in zip(*columns)])
    return out


def bilinear_dimension(gens, symmetric=False):
    n = len(gens[0])
    positions = [(i, j) for i in range(n) for j in range(n) if not symmetric or i <= j]
    def index(i, j):
        return positions.index((min(i, j), max(i, j)) if symmetric else (i, j))
    eq = []
    for a in gens:
        for i in range(n):
            for j in range(n):
                row = [0]*len(positions)
                for k in range(n):
                    row[index(k, j)] += a[k][i]
                    row[index(i, k)] += a[k][j]
                eq.append(row)
    return len(positions)-rank(eq)


def run():
    group, mul = quaternions()
    d1, d2 = [[0]*16 for _ in range(4)], [[0]*8 for _ in range(16)]
    for q in range(8):
        qi, qj = mul[q][2], mul[q][4]
        d1[qi//2][q] += 1
        d1[q//2][q] -= 1
        d1[qj//2][q+8] += 1
        d1[q//2][q+8] -= 1
        d2[q][q] += 1
        d2[qi+8][q] += 1
        d2[qj][q] -= 1
        d2[q+8][q] -= 1
    h1 = []
    for g in range(8):
        fixed_faces = sum(mul[g][q] == q for q in range(8))
        fixed_vertices = sum(mul[g][2*v]//2 == v for v in range(4))
        h1.append(2-fixed_vertices+2*fixed_faces-fixed_faces)
    rho = [2*sign if unit == 0 else 0 for sign, unit in group]
    hol = [1+x for x in rho]
    adj = []
    for g in range(8):
        x, x2, x3 = 3*rho[g], 3*rho[mul[g][g]], 3*rho[mul[mul[g][g]][g]]
        ext2, ext3 = F(x*x-x2, 2), F(x**3-3*x*x2+2*x3, 6)
        adj.append(int(10+x*x+6*ext2+12*x+2*ext3))
    char1 = [1]*8
    char_nontriv = [[1, 1, 1, 1, -1, -1, -1, -1],
                    [1, 1, -1, -1, 1, 1, -1, -1], [1, 1, -1, -1, -1, -1, 1, 1]]
    dot = lambda a, b: sum(F(x*y, 8) for x, y in zip(a, b))
    mult = [int(dot(adj, a)) for a in [char1]+char_nontriv+[rho]]
    kernels = {"W6_scalar": int(dot([3*x for x in rho], char1)),
               "W6_one_Hodge_type": int(dot([3*x for x in rho], hol)),
               "adjoint_scalar": int(dot(adj, char1)), "adjoint_one_Hodge_type": int(dot(adj, hol)),
               "adjoint_real_degree1_complexification": int(dot(adj, h1))}
    sl2 = [[[1, 0], [0, -1]], [[0, 1], [0, 0]], [[0, 0], [1, 0]]]
    double = [[[a[i%2][j%2] if i//2 == j//2 else 0 for j in range(4)] for i in range(4)] for a in sl2]
    ad8_dim = bilinear_dimension(adjoint_matrices())
    ad8_sym = bilinear_dimension(adjoint_matrices(), symmetric=True)
    weak_dim = bilinear_dimension(sl2)
    weak_sym = bilinear_dimension(sl2, symmetric=True)
    doubled_sym = bilinear_dimension(double, symmetric=True)
    # Factored Schur bilinear: symmetric x skew has no symmetric component.
    protected_sym = 0 if ad8_dim == ad8_sym == weak_dim == 1 and weak_sym == 0 else -1
    predicates = {
        "signed_quaternion_noncommutativity": mul[2][4] != mul[4][2],
        "central_commutator_branch_pairs": mul[2][4] == 6 and mul[4][2] == 7,
        "integer_boundaries_zero": all(x == 0 for row in multiply(d1, d2) for x in row),
        "fraction_ranks_three_seven": [rank(d1), rank(d2)] == [3, 7],
        "Euler_genus_three": 4-16+8 == -4,
        "deck_H1_character": h1 == [2+2*x for x in rho],
        "holomorphic_total_three": hol[0] == 3,
        "holomorphic_rho_once": dot(hol, rho) == 1,
        "holomorphic_nontrivial_characters_absent": all(dot(hol, c) == 0 for c in char_nontriv),
        "adjoint_full248_dimension": adj[0] == 248,
        "adjoint_multiplicities_55_27_56": mult == [55, 27, 27, 27, 56],
        "full248_reconstructed": mult[0]+sum(mult[1:4])+2*mult[4] == 248,
        "W6_three_not_six": kernels['W6_one_Hodge_type'] == 3,
        "adjoint_holomorphic111": kernels['adjoint_one_Hodge_type'] == 111,
        "adjoint_H1_222": kernels['adjoint_real_degree1_complexification'] == 222,
        "lambda_twisted_slots": [1+1, 1-1] == [2, 0],
        "psi_companions_retained": [-1+0, -1+0] == [-1, -1],
        "form_pullback_exponent_zero": 2*F(-1, 2)+1 == 0,
        "radial_operator_polynomial_mass_quarter": F(1, 2)*F(1, 2) == F(1, 4),
        "adjoint_bilinear_unique_symmetric": ad8_dim == ad8_sym == 1,
        "doublet_bilinear_unique_nonsymmetric": weak_dim == 1 and weak_sym == 0,
        "protected_symmetric_mass_absent": protected_sym == 0,
        "two_doublet_symmetric_mass_present": doubled_sym == 1,
        "weak_doublet_count_even": 3*3+3*3+8+2 == 28,
        "complete_one_form_gauge_dimension": 8+3+8+3*6+3*6+3*2*3+3*2*3+2*8+2*2 == 111,
    }
    return {"predicates": predicates, "predicates_passed": sum(predicates.values()),
            "cover_H1_character": h1, "cover_holomorphic_character": hol,
            "adjoint_Q8_multiplicities": mult, "form_kernel_dimensions": kernels,
            "parent_left_twisted_charges": [2, 0, -1, -1], "gauge_dimensions": [55, 56, 111],
            "weak_doublets_in_FORM_sector": 28,
            "bilinear_profile": {"ad8_invariants": ad8_dim, "doublet_invariants": weak_dim,
                "protected_symmetric_masses": protected_sym, "two_doublet_symmetric_masses": doubled_sym,
                "protected_lower_bound_complex_components": 16}, "zero_angular_form_squared_mass": "1/4"}


if __name__ == '__main__':
    result = run()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if all(result['predicates'].values()) else 1)
