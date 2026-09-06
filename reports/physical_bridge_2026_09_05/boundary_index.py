"""Exact relative cubical topology and properly typed cusp-map controls; no physical index identification."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import subprocess
import time

import sympy as sp

MAIN = "2901ae9f6dba964870b44d5eb6e01066c62b7f62"
PHYSICS = "f4d747281ce9ec65fe2806404c01672cc73deb54"
SM = "2a7f88553652b9b28efefaf89925c116e008b639"


class Cubes:
    def __init__(self, periods):
        self.periods = tuple(periods)
        self.dim = len(periods)

    def cell(self, base, mask):
        return (tuple(x % n if n else x for x, n in zip(base, self.periods)), mask)

    def boundary(self, cell):
        base, mask = cell
        axes = [i for i in range(self.dim) if mask & (1 << i)]
        out = []
        for pos, axis in enumerate(axes):
            hi = list(base)
            hi[axis] += 1
            smaller = mask ^ (1 << axis)
            out += [(self.cell(hi, smaller), (-1)**pos),
                    (self.cell(base, smaller), -(-1)**pos)]
        return out

    def closure(self, cells):
        out = set(cells)
        todo = list(out)
        while todo:
            for face, _ in self.boundary(todo.pop()):
                if face not in out:
                    out.add(face)
                    todo.append(face)
        return out

    def complex(self, bases):
        return self.closure(self.cell(b, (1 << self.dim)-1) for b in bases)

    def cohomology(self, cells, relative=frozenset()):
        cells, relative = set(cells), set(relative)
        if self.closure(cells) != cells:
            raise ValueError("complex is not closed under faces")
        if not relative <= cells or self.closure(relative) != relative:
            raise ValueError("relative set is not a subcomplex")
        basis = [sorted(c for c in cells-relative if c[1].bit_count() == k)
                 for k in range(self.dim+1)]
        matrices = [None]
        ranks = [0]
        for k in range(1, self.dim+1):
            idx = {c: i for i, c in enumerate(basis[k-1])}
            entries = defaultdict(int)
            for j, cell in enumerate(basis[k]):
                for face, coeff in self.boundary(cell):
                    if face not in relative:
                        entries[idx[face], j] += coeff
            mat = sp.MutableSparseMatrix(len(basis[k-1]), len(basis[k]), dict(entries))
            if k > 1:
                assert (matrices[-1]*mat).is_zero_matrix
            matrices.append(mat)
            ranks.append(int(mat.to_DM().convert_to(sp.QQ).rank()) if entries else 0)
        ranks.append(0)
        counts = list(map(len, basis))
        betti = [counts[k]-ranks[k]-ranks[k+1] for k in range(self.dim+1)]
        assert all(b >= 0 for b in betti)
        chi = sum((-1)**k*n for k, n in enumerate(counts))
        assert chi == sum((-1)**k*b for k, b in enumerate(betti))
        return dict(cells=counts, boundary_ranks=ranks[1:-1], betti=betti, chi=chi)

    def frontier(self, cells):
        tops = [c for c in cells if c[1].bit_count() == self.dim]
        incidence = Counter(face for c in tops for face, _ in self.boundary(c))
        assert all(n in (1, 2) for n in incidence.values())
        return self.closure(face for face, n in incidence.items() if n == 1)


def surface_data(grid, faces):
    cells = grid.complex(faces)
    out = grid.cohomology(cells)
    boundary = grid.frontier(cells)
    edges = {c for c in boundary if c[1].bit_count() == 1}
    adjacent = defaultdict(list)
    for edge in edges:
        lo, hi = (c for c, _ in grid.boundary(edge))
        adjacent[lo].append((hi, edge))
        adjacent[hi].append((lo, edge))
    assert all(len(links) == 2 for links in adjacent.values()), "not a regular surface boundary"
    unused, loops = set(edges), []
    while unused:
        first = min(unused)
        start = (first[0], 0)
        here = start
        length, delta = 0, [0, 0]
        while True:
            nxt, edge = next((v, e) for v, e in adjacent[here] if e in unused)
            axis = edge[1].bit_length()-1
            delta[axis] += 1 if here[0] == edge[0] else -1
            length += 1
            unused.remove(edge)
            here = nxt
            if here == start:
                break
        assert all(d % n == 0 for d, n in zip(delta, grid.periods))
        loops.append(dict(edges=length, winding=[d//n for d, n in zip(delta, grid.periods)]))
    out.update(boundary_loops=loops, faces=sorted(faces))
    return out


def torus_examples():
    n = 12
    grid = Cubes((n, n))
    whole = set(product(range(n), repeat=2))

    def disk(cx, cy, radius=1):
        return {(i % n, j % n) for i in range(cx-radius, cx+radius)
                for j in range(cy-radius, cy+radius)}

    disks = disk(0, 0) | disk(6, 0) | disk(0, 6)
    nested = disk(0, 0) | (whole-disk(0, 0, 2))
    annuli = {(i, j) for i, j in whole if i % 6 < 3}
    samples = dict(torus=whole, two_annuli=annuli, three_disks=disks,
                   torus_minus_three_disks=whole-disks, nested_null_circles=nested)
    rows = {}
    theta = lambda fs: {((-i-1) % n, (-j-1) % n) for i, j in fs}
    for name, faces in samples.items():
        row = surface_data(grid, faces)
        row["theta_preserves"] = theta(faces) == faces
        row["theta_exchanges_sides"] = theta(faces) == whole-faces
        row["half_translation_preserves"] = {
            f"{du},{dv}": {((i+du) % n, (j+dv) % n) for i, j in faces} == faces
            for du, dv in ((6, 0), (0, 6), (6, 6))}
        other = grid.complex(whole-faces)
        intersection = grid.complex(faces) & other
        row["complement_chi"] = grid.cohomology(other)["chi"]
        row["intersection_chi"] = grid.cohomology(intersection)["chi"]
        assert row["chi"]+row["complement_chi"]-row["intersection_chi"] == 0
        row["relative_chi_if_core_chi_zero"] = -row["chi"]
        rows[name] = row
    return dict(size=n, examples=rows)


def arc_excision():
    grid = Cubes((8, 0, 0))
    cubes = set(product(range(8), range(4), range(2)))
    Q = grid.complex(cubes)
    boundary_Q = grid.frontier(Q)
    rows = []
    for k in range(4):
        blocks = [{(i, 1, z) for z in range(2)} for i in (1, 3, 5)[:k]]
        removed = set().union(*blocks) if blocks else set()
        C, N = grid.complex(cubes-removed), grid.complex(removed)
        T, E = C & N, C & boundary_Q
        assert C | N == Q
        assert grid.frontier(C) == T | E
        data = {name: grid.cohomology(cells) for name, cells in
                (("Q", Q), ("C", C), ("N", N), ("T", T), ("E", E),
                 ("boundary_C", grid.frontier(C)), ("endpoint_caps", N & boundary_Q))}
        assert data["Q"]["chi"] == data["C"]["chi"]+data["N"]["chi"]-data["T"]["chi"]
        assert data["boundary_C"]["chi"] == 2*data["C"]["chi"]
        data["arcs"] = k
        if k == 2:
            tubes = [C & grid.complex(block) for block in blocks]
            signs = []
            for pattern in ((1, 1), (-1, -1), (1, -1)):
                A = set().union(*(tube for tube, sign in zip(tubes, pattern) if sign == 1))
                relative = grid.cohomology(C, A)
                assert relative["chi"] == data["C"]["chi"]-grid.cohomology(A)["chi"]
                signs.append(dict(signs=pattern, A_chi=grid.cohomology(A)["chi"],
                                  relative=relative, sign_only_claim=-sum(pattern)))
            data["positive_tubes_only_cusp_empty"] = signs
            data["all_positive_tubes"] = grid.cohomology(C, T)
            data["complementary_boundary"] = grid.cohomology(C, E)
        rows.append(data)
    return rows


def det_minus_identity(A):
    a, b = A[0]
    c, d = A[1]
    return (a-1)*(d-1)-b*c


def cusp_interpretation(A, source, target):
    if source != target:
        return dict(kind="different_cusp_not_a_self_map", count=None)
    det = det_minus_identity(A)
    if det:
        return dict(kind="finite_fixed_set", count=abs(det))
    return dict(kind="singular_linear_part_translation_required", count=None)


def affine_grid(A, b, n):
    points = []
    for i, j in product(range(n), repeat=2):
        x = (F(i, n), F(j, n))
        diff = [sum(A[k][l]*x[l] for l in range(2))+b[k]-x[k] for k in range(2)]
        if all(z.denominator == 1 for z in diff):
            points.append([str(z) for z in x])
    return points


def affine_controls():
    samples = [("identity", [[1, 0], [0, 1]], [F(0), F(0)], (4, 8)),
               ("half_translation", [[1, 0], [0, 1]], [F(1, 2), F(0)], (4, 8)),
               ("reflection", [[1, 0], [0, -1]], [F(0), F(0)], (4, 8)),
               ("free_glide", [[1, 0], [0, -1]], [F(1, 2), F(0)], (4, 8)),
               ("inversion", [[-1, 0], [0, -1]], [F(0), F(0)], (4, 8)),
               ("shifted_inversion", [[-1, 0], [0, -1]], [F(1, 2), F(0)], (4, 8)),
               ("order_three", [[0, -1], [1, -1]], [F(0), F(0)], (6, 12))]
    return {name: dict(matrix=A, shift=list(map(str, b)), determinant=det_minus_identity(A),
                       grid_counts=[len(affine_grid(A, b, n)) for n in ns], grid_sizes=ns)
            for name, A, b, ns in samples}


def snappy_witnesses():
    import snappy
    results = {}
    for name in ("m004", "m202", "m125", "s960"):
        M = snappy.Manifold(name)
        G = M.symmetry_group()
        isometries = []
        for pos, iso in enumerate(G.isometries()):
            images = list(map(int, iso.cusp_images()))
            maps = [[[int(m[i, j]) for j in range(2)] for i in range(2)] for m in iso.cusp_maps()]
            assert sorted(images) == list(range(M.num_cusps()))
            rows = []
            for source, (target, A) in enumerate(zip(images, maps)):
                assert int(sp.det(sp.Matrix(A))) in (-1, 1)
                rows.append(dict(source=source, target=target, matrix=A,
                                 raw_abs_det_minus_I=abs(det_minus_identity(A)),
                                 interpretation=cusp_interpretation(A, source, target)))
            isometries.append(dict(index=pos, cusp_images=images, peripheral=rows))
        group = M.fundamental_group()
        results[name] = dict(cusps=M.num_cusps(), orientable=M.is_orientable(),
                             symmetry_order=G.order(), generators=group.generators(),
                             relators=group.relators(), homology=str(M.homology()),
                             isometries=isometries)
    return dict(version=snappy.version(), manifolds=results)


def source_receipts():
    paths = [(MAIN, "frontier/B1290_the_index_formula/verification/index_formula.py"),
             (MAIN, "frontier/B1291_the_parity_of_the_cusp/verification/dividing_set.py"),
             (MAIN, "frontier/B1291_the_parity_of_the_cusp/verification/parity.py"),
             (PHYSICS, "reports/fresh_physics_seat_2026-09-01/R61_THE_GEOMETRY_OF_THETA.md"),
             (PHYSICS, "reports/fresh_physics_seat_2026-09-01/computations/r69_arcs_cut_corners.py"),
             (SM, "frontier/B1277_the_vacuum_manifold_of_the_closing/ADDENDUM_2026-09-06_the_arcs_and_the_corners.md")]
    return [dict(commit=commit, path=path, sha256=sha256(subprocess.check_output(
        ["git", "show", f"{commit}:{path}"])).hexdigest()) for commit, path in paths]


def run():
    start = time.monotonic()
    result = dict(torus=torus_examples(), excision=arc_excision(), affine=affine_controls(),
                  snappy=snappy_witnesses(), source_receipts=source_receipts())
    result["runtime_seconds"] = time.monotonic()-start
    result["interpretation"] = "Finite-pair topology and instrument audit only; no sourced physical chiral spectrum."
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    result = run()
    with args.output.open("x") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({"runtime_seconds": result["runtime_seconds"],
                      "torus_chi": {k: r["chi"] for k, r in result["torus"]["examples"].items()},
                      "excised_chi": [r["C"]["chi"] for r in result["excision"]]}))
