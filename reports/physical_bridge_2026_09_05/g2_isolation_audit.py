"""Exact audit of the element/subgroup fixed-space inference; no chirality claim."""
import argparse
from collections import Counter
from contextlib import redirect_stdout
from functools import lru_cache
import hashlib
import io
import itertools
import json
from pathlib import Path
import runpy
import subprocess
import sys
import time

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
UPSTREAM = "9a79adfdee23e6dfde8b9f2b12515a314c896b13"
UPSTREAM_PATH = "frontier/B1259_flat_orbifolds_cannot_isolate/verification/flat_cannot_isolate.py"
FLOAT_PATH = ROOT / "frontier/B1084_g2_cone/float_crosscheck.py"
FLOAT_SHA = "b693e638e24b511e775320a8af1c62f5c5577d7fd90084f48eff583563915d29"
PHI = {(0, 1, 2): 1, (0, 3, 4): 1, (0, 5, 6): 1,
       (1, 3, 5): 1, (1, 4, 6): -1, (2, 3, 6): -1, (2, 4, 5): -1}


def wedge(left, right):
    result = Counter()
    for a, av in left.items():
        for b, bv in right.items():
            word = a+b
            if len(set(word)) != len(word):
                continue
            inversions = sum(word[i] > word[j] for i in range(len(word))
                             for j in range(i+1, len(word)))
            result[tuple(sorted(word))] += (-1)**inversions*av*bv
    return {k: v for k, v in result.items() if v}


def interior(form, index):
    return {key[:key.index(index)]+key[key.index(index)+1:]:
            (-1)**key.index(index)*value for key, value in form.items() if index in key}


def form_metric(form):
    return sp.Matrix(7, 7, lambda i, j: sp.Rational(
        wedge(wedge(interior(form, i), interior(form, j)), form).get(tuple(range(7)), 0), 6))


def preserves_form(matrix, form):
    """Exterior-cube pullback by minors, not a sign-character assumption."""
    for target in itertools.combinations(range(7), 3):
        coefficient = sum(value*matrix.extract(source, target).det()
                          for source, value in form.items())
        if coefficient != form.get(target, 0):
            return False
    return True


def common_dimension(matrices):
    if not matrices:
        return 7
    return 7-sp.Matrix.vstack(*(m-sp.eye(7) for m in matrices)).rank()


def binary_span(generators):
    values = {0}
    for generator in generators:
        values |= {x ^ generator for x in tuple(values)}
    return tuple(sorted(values))


@lru_cache(maxsize=1)
def exact_example():
    metric = form_metric(PHI)
    assert metric == sp.eye(7)
    group = [sp.diag(*[(-1)**((a & char).bit_count()) for char in range(1, 8)])
             for a in range(8)]
    assert len({tuple(m) for m in group}) == 8
    for a, ga in enumerate(group):
        assert ga.T*ga == sp.eye(7) and ga.det() == 1
        assert preserves_form(ga, PHI)
        for b, gb in enumerate(group):
            assert ga*gb == group[a ^ b]
    subgroups = {binary_span(subset) for n in range(8)
                 for subset in itertools.combinations(range(1, 8), n)}
    rows = []
    for elements in sorted(subgroups, key=lambda x: (len(x), x)):
        mats = [group[i] for i in elements]
        dim = common_dimension(mats)
        projector = sum(mats, sp.zeros(7))/len(mats)
        assert projector*projector == projector and projector.T == projector
        assert projector.rank() == sp.trace(projector) == dim
        rows.append({"elements": list(elements), "order": len(elements), "fixed_dimension": dim,
                     "Reynolds_projector": [list(map(int, row)) for row in projector.tolist()]})
    census = Counter((r["order"], r["fixed_dimension"]) for r in rows)
    assert census == {(1, 7): 1, (2, 3): 7, (4, 1): 7, (8, 0): 1}
    element_dims = [common_dimension([g]) for g in group[1:]]
    assert element_dims == [3]*7
    assert common_dimension(group) == 0
    # A generic point of a fixed plane, an axis, a free point, and the apex.
    points = {"plane": sp.Matrix([0, 1, 0, 1, 0, 1, 0]),
              "axis": sp.eye(7)[:, 0], "free": sp.ones(7, 1), "apex": sp.zeros(7, 1)}
    isotropy = {name: sum(g*p == p for g in group) for name, p in points.items()}
    assert isotropy == {"plane": 2, "axis": 4, "free": 1, "apex": 8}
    wrong = sp.diag(-1, -1, 1, 1, 1, 1, 1)
    assert wrong.T*wrong == sp.eye(7) and wrong.det() == 1
    assert not preserves_form(wrong, PHI)
    return {"group": [[list(map(int, row)) for row in g.tolist()] for g in group],
            "positive_form": {str(k): v for k, v in PHI.items()},
            "metric": [list(map(int, row)) for row in metric.tolist()],
            "nonidentity_fixed_dimensions": element_dims, "common_fixed_dimension": 0,
            "subgroups": rows, "point_isotropy_orders": isotropy,
            "SO7_not_G2_control_rejected": True,
            "single_generator_fixed_dimension": common_dimension([group[1]]),
            "isolated_maximal_isotropy_stratum": True,
            "isolated_point_of_total_singular_set": False,
            "physical_chiral_index_computed": False}


@lru_cache(maxsize=1)
def original_group():
    raw = FLOAT_PATH.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == FLOAT_SHA
    # Independently transcribed Hamilton multiplication, exact over Q(sqrt(2)).
    ri = sp.Matrix([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]])
    rk = sp.Matrix([[0, 0, 0, -1], [0, 0, 1, 0], [0, -1, 0, 0], [1, 0, 0, 0]])
    li = sp.Matrix([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]])
    central = sp.diag(1, 1, 1, -1, -1, -1, -1)
    tau = sp.diag(sp.diag(1, -1, -1), ri)
    sigma = sp.diag(sp.diag(-1, -1, 1), (sp.eye(4)+li)*rk/sp.sqrt(2))
    for matrix in [central, tau, sigma]:
        assert sp.simplify(matrix.T*matrix) == sp.eye(7)
        assert sp.simplify(matrix.det()) == 1
    exact_dim = common_dimension([central, tau, sigma])
    assert exact_dim == 0
    assert common_dimension([central, tau]) == common_dimension([central, sigma]) == 1
    stdout = io.StringIO()
    with redirect_stdout(stdout):
        old = runpy.run_path(str(FLOAT_PATH))
    group = old["group"]
    assert len(group) == 96 and old["census"] == {3: 53, 1: 42}
    assert sorted(old["orbits"]) == [6, 12, 12]
    assert old["axis_stab"] == [48, 48, 48]
    for exact in [central, tau, sigma]:
        assert any(np.max(np.abs(np.array(exact, float)-g)) < 1e-12 for g in group)
    stack = np.vstack([m-np.eye(7) for m in group])
    full_dim = 7-int(np.linalg.matrix_rank(stack, tol=1e-9))
    assert full_dim == exact_dim
    basis_e6 = np.eye(7)[:, :3]
    intersections = []
    for projector in old["plane_P"].values():
        # P v=v with v already in the actual E6 plane.
        intersections.append(3-int(np.linalg.matrix_rank((np.eye(7)-projector)@basis_e6, tol=1e-9)))
    assert intersections == [1]*30
    return {"input_sha256": FLOAT_SHA, "group_order": len(group),
            "nonidentity_element_census": old["census"],
            "exact_common_fixed_dimension": exact_dim,
            "full_96_action_float_common_fixed_dimension": full_dim,
            "exact_generators": [[[str(x) for x in row] for row in g.tolist()]
                                 for g in [central, tau, sigma]],
            "A1_E6_intersection_dimensions": intersections,
            "A1_orbit_sizes": sorted(old["orbits"]), "axis_stabilizer_orders": old["axis_stab"],
            "original_float_producer_stdout": stdout.getvalue(),
            "physical_chiral_index_computed": False}


def upstream_selftest():
    raw = subprocess.run(["git", "show", f"{UPSTREAM}:{UPSTREAM_PATH}"], cwd=ROOT,
                         capture_output=True, check=True).stdout
    result = subprocess.run([sys.executable, "-c", raw.decode()], cwd=ROOT,
                            capture_output=True, text=True, timeout=60)
    assert result.returncode == 0, result.stderr
    return {"commit": UPSTREAM, "path": UPSTREAM_PATH,
            "source_sha256": hashlib.sha256(raw).hexdigest(),
            "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr,
            "scope": "the original selftest samples single-element eigenvalues, not common fixed spaces"}


@lru_cache(maxsize=1)
def analyze():
    return {"exact_G2_counterexample": exact_example(), "actual_B1084_group": original_group(),
            "upstream_B1259_selftest": upstream_selftest(),
            "scope": "element-to-subgroup inference correction only; no AW geometry or chiral spectrum derived"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    with args.output.open("x", encoding="utf-8") as handle:
        start = time.monotonic()
        result = analyze()
        result = {**result, "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  "elapsed_seconds": time.monotonic()-start}
        json.dump(result, handle, indent=2, allow_nan=False)
        handle.write("\n")
    print(json.dumps({"exact_G2_group_order": 8,
                      "every_nonidentity_element_fixed_dimension": 3,
                      "G2_common_fixed_dimension": result["exact_G2_counterexample"]["common_fixed_dimension"],
                      "B1084_common_fixed_dimension": result["actual_B1084_group"]["exact_common_fixed_dimension"],
                      "B1084_A1_E6_intersections": result["actual_B1084_group"]["A1_E6_intersection_dimensions"],
                      "upstream_selftest_returncode": result["upstream_B1259_selftest"]["returncode"],
                      "elapsed_seconds": result["elapsed_seconds"], "scope": result["scope"]}, indent=2))


if __name__ == "__main__":
    main()
