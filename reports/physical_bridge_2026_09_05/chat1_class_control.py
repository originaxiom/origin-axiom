"""Exact arithmetic/regular-tessellation checks; separate certified geometry mode."""
from __future__ import annotations
import argparse
from collections import Counter, deque
import json
import platform
import sys

ZERO, ONE, Z = (0, 0), (1, 0), (0, 1)
IDENTITY = (ONE, ZERO, ZERO, ONE)
A = (ZERO, ONE, (-1, 0), ONE)
B = (ZERO, (1, -1), (0, -1), ZERO)


def add(x, y):
    return (x[0]+y[0], x[1]+y[1])


def neg(x):
    return (-x[0], -x[1])


def mul(x, y):
    a, b = x
    c, d = y
    return (a*c-b*d, a*d+b*c+b*d)


def mm(x, y):
    return tuple(add(mul(x[2*i], y[j]), mul(x[2*i+1], y[2+j]))
                 for i in range(2) for j in range(2))


def determinant(x):
    return add(mul(x[0], x[3]), neg(mul(x[1], x[2])))


def parent_group():
    group, todo = {IDENTITY}, deque([IDENTITY])
    while todo:
        g = todo.popleft()
        for h in (A, B):
            product = mm(g, h)
            if product not in group:
                group.add(product)
                todo.append(product)
                if len(group) > 96:
                    raise ValueError('Finite-group control exceeded its sealed bound')
    points = ((ZERO, ONE), (ONE, ONE), (Z, ONE), (ONE, ZERO))
    permutations = set()
    for g in group:
        permutation = []
        for x, y in points:
            gx, gy = add(mul(g[0], x), mul(g[1], y)), add(mul(g[2], x), mul(g[3], y))
            matches = [i for i, (u, v) in enumerate(points) if mul(gx, v) == mul(gy, u)]
            if len(matches) != 1:
                raise ValueError('Matrix does not permute the actual tetrahedron vertices')
            permutation.append(matches[0])
        permutations.add(tuple(permutation))
    even = lambda p: sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4)) % 2 == 0
    center = sorted(g for g in group if all(mm(g, h) == mm(h, g) for h in group))
    return dict(matrices=sorted(group), permutations=sorted(permutations), center=center,
                matrix_count=len(group), projective_count=len(permutations),
                all_determinants_one=all(determinant(g) == ONE for g in group),
                all_vertex_permutations_even=all(even(p) for p in permutations),
                a_cube=mm(mm(A, A), A), b_square=mm(B, B))


def coloring(neighbors):
    colors = {}
    components, conflicts = 0, []
    for start in range(len(neighbors)):
        if start in colors:
            continue
        components += 1
        colors[start] = 0
        queue = deque([start])
        while queue:
            i = queue.popleft()
            for j in neighbors[i]:
                if j < 0 or j >= len(neighbors):
                    raise ValueError('Missing or out-of-range face neighbor')
                if j not in colors:
                    colors[j] = 1-colors[i]
                    queue.append(j)
                elif colors[j] == colors[i]:
                    conflicts.append([i, j])
    return dict(components=components, two_colorable=not conflicts,
                colors=[colors[i] for i in range(len(neighbors))], conflicts=conflicts)


def inverse_faces(data):
    try:
        for i, (neighbors, permutations) in enumerate(data):
            if len(neighbors) != 4 or len(permutations) != 4:
                return False
            for face, (j, p) in enumerate(zip(neighbors, permutations)):
                if sorted(p) != list(range(4)) or not 0 <= j < len(data):
                    return False
                target_face = p[face]
                if data[j][0][target_face] != i:
                    return False
                q = data[j][1][target_face]
                if any(q[p[k]] != k for k in range(4)):
                    return False
        return True
    except (IndexError, TypeError):
        return False


def regular_log_certificate(rows, n, cusps):
    return (len(rows) == n+2*cusps and all(len(row) == 3*n for row in rows)
            and [sum(row) for row in rows] == [6]*n+[0]*(2*cusps))


def triangulation_row(name):
    import snappy
    m = snappy.Manifold(name)
    n, cusps = int(m.num_tetrahedra()), int(m.num_cusps())
    data = [([int(j) for j in neighbors], [[int(k) for k in p] for p in perms])
            for neighbors, perms in m._get_tetrahedra_gluing_data()]
    rows = [[int(x) for x in row] for row in m.gluing_equations()]
    color = coloring([row[0] for row in data])
    regular = (inverse_faces(data) and bool(m.is_orientable())
               and all(m.cusp_info('complete?')) and color['components'] == 1
               and regular_log_certificate(rows, n, cusps))
    return dict(name=name, tetrahedra=n, cusps=cusps,
                isosig=m.triangulation_isosig(decorated=False),
                face_data=data, face_inverses=inverse_faces(data),
                gluing_equations=rows, logarithmic_row_sums=[sum(r) for r in rows],
                regular_shape_certificate=regular, coloring=color,
                pgl_cover_index=12*n if regular else None,
                psl_cover_index=6*n if regular and color['two_colorable'] else None)


def representation_control():
    fundamental_color = [1, 1, -2]
    grade = fundamental_color*9
    actual_27 = fundamental_color*3+[-v for v in fundamental_color]*3+[0]*9
    cube = lambda xs: sum(v**3 for v in xs)
    return dict(grade_dimension=len(grade), fundamental_dimension=len(actual_27),
                grade_color_weights=dict(Counter(grade)),
                fundamental_color_weights=dict(Counter(actual_27)),
                grade_cubic_trace=cube(grade), dual_grade_cubic_trace=cube([-v for v in grade]),
                fundamental_cubic_trace=cube(actual_27),
                grade_anomaly=cube(grade)//cube(fundamental_color),
                paired_grade_cubic_trace=cube(grade+[-v for v in grade]))


def exact_run():
    import snappy
    group = parent_group()
    rows = [triangulation_row(n) for n in ('m004', 'm202', 's959', 's958', 'otet06_0000')]
    rep = representation_control()
    minus_identity = tuple(neg(x) for x in IDENTITY)
    checks = dict(binary_tetrahedral_order=group['matrix_count'] == 24,
                  projective_tetrahedral_action=group['projective_count'] == 12 and group['all_vertex_permutations_even'],
                  actual_sl_parent=group['all_determinants_one'],
                  exact_spin_center=group['center'] == sorted([IDENTITY, minus_identity]),
                  finite_orders=group['a_cube'] == minus_identity and group['b_square'] == minus_identity,
                  actual_regular_shapes=all(r['regular_shape_certificate'] for r in rows),
                  proposed_indices=[r['psl_cover_index'] for r in rows[:3]] == [12, 24, 36],
                  published_coloring_rejector=not rows[-1]['coloring']['two_colorable'],
                  different_27_representations=rep['grade_cubic_trace'] == -54 and rep['fundamental_cubic_trace'] == 0,
                  paired_anomaly_cancels=rep['paired_grade_cubic_trace'] == 0)
    return dict(checks=checks, all_checks_pass=all(checks.values()), parent=group,
                manifolds=rows, representation=rep, snappy_version=snappy.__version__,
                python_version=platform.python_version(),
                scope='Exact regular-shape/cover and representation controls, not a fermion index or a physical action.')


def canonical_run():
    import snappy
    rows = []
    for name, expected_order, expected_c3 in (('m004', 8, 0), ('m202', 12, 2), ('s959', 12, 2), ('s958', 2, 0)):
        try:
            m = snappy.Manifold(name)
            k = m.canonical_retriangulation(verified=True)
            isos = k.isomorphisms_to(k)
            records = []
            for iso in isos:
                images = [int(i) for i in iso.cusp_images()]
                matrices = [[[int(a[i, j]) for j in range(2)] for i in range(2)] for a in iso.cusp_maps()]
                rotational_c3 = (images == list(range(len(images))) and bool(matrices)
                                 and all(a[0][0]+a[1][1] == -1 and a[0][0]*a[1][1]-a[0][1]*a[1][0] == 1 for a in matrices))
                records.append(dict(cusp_images=images, cusp_matrices=matrices, rotational_c3=rotational_c3))
            count = sum(r['rotational_c3'] for r in records)
            rows.append(dict(name=name, canonical_verified=True,
                             canonical_isosig=k.triangulation_isosig(decorated=False),
                             symmetry_count=len(isos), rotational_c3_count=count, isometries=records,
                             expected_counts_match=len(isos) == expected_order and count == expected_c3))
        except Exception as error:
            rows.append(dict(name=name, canonical_verified=False, error=type(error).__name__+': '+str(error), expected_counts_match=False))
    return dict(manifolds=rows, all_checks_pass=all(r['expected_counts_match'] for r in rows),
                snappy_version=snappy.__version__, python_version=platform.python_version(),
                scope='Certified canonical cells and exact cusp-action census, not a lift of each isometry into the chosen parent or a physical spectrum.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--canonical', action='store_true')
    args = parser.parse_args()
    result = canonical_run() if args.canonical else exact_run()
    print(json.dumps(result, indent=2, sort_keys=True))
    sys.exit(0 if result['all_checks_pass'] else 1)
