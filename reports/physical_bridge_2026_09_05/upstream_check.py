"""Source-informed exact checks of B1250/B1252/B1253 after integration.

No upstream producer is executed on import or overwritten by this module.
"""
import argparse
from collections import Counter, deque
from fractions import Fraction as F
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import subprocess
import sys
import time

import sympy as sp

from . import vacuum as v

ROOT = Path(__file__).resolve().parents[2]


def load_metric_module():
    src = ROOT / "frontier/B1252_metric_and_descent/verification/cartan_metric_and_descent.py"
    spec = importlib.util.spec_from_file_location("upstream_metric", src)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def components(vertices, edges):
    left = set(vertices)
    out = []
    while left:
        stack = [min(left)]
        seen = set(stack)
        while stack:
            a = stack.pop()
            for b in edges.get(a, set()):
                if b not in seen:
                    seen.add(b)
                    stack.append(b)
        left -= seen
        out.append(sorted(seen))
    return sorted(out, key=lambda x: (len(x), x))


def weight_blocks(indices, labels, roots):
    inds = set(indices)
    edges = {i: set() for i in inds}
    for label in labels:
        m = roots[label]
        for i, j in itertools.product(range(27), repeat=2):
            if m[i, j]:
                assert (i in inds) == (j in inds), "proposed block is not invariant"
                if i in inds:
                    edges[i].add(j)
                    edges[j].add(i)
    return components(inds, edges)


def exact_checks():
    weights, rep, roots, positive, _ = v.representation()
    metric = load_metric_module().cartan_metric()
    assert metric == v.CARTAN.inv()
    root_lengths = Counter((r.T*metric*r)[0] for r in map(sp.Matrix, roots))
    weight_lengths = Counter((w.T*metric*w)[0] for w in weights)
    naive = Counter(sum(x*x for x in r) for r in roots)
    assert root_lengths == {2: 72} and weight_lengths == {sp.Rational(4, 3): 27}
    assert len(naive) > 1
    data = json.loads((ROOT / "frontier/B916_lambda_bridge/results.json").read_text())
    d2 = data["H_prime_diag_vs_H_plus"]["D2"]
    char = weights[13]
    assert [(-1)**int((char.T*w)[0]+1) for w in weights] == d2
    even = sorted(r for r in roots if (char.T*sp.Matrix(r))[0] % 2 == 0)
    positive_even = {r for _, r, _ in positive if r in even}
    simple = sorted(r for r in positive_even if not any(
        tuple(x-y for x, y in zip(r, a)) in positive_even for a in positive_even))
    d5_cartan = sp.Matrix([[(sp.Matrix(a).T*metric*sp.Matrix(b))[0]
                            for b in simple] for a in simple])
    assert len(even) == 40 and len(simple) == 5 and d5_cartan.det() == 4
    degrees = sorted(sum(1 for j in range(5) if d5_cartan[i, j] == -1) for i in range(5))
    assert degrees == [1, 1, 1, 2, 3]
    blocks = weight_blocks(range(27), even, roots)
    assert list(map(len, blocks)) == [1, 10, 16] and blocks[0] == [13]
    sixteen = blocks[-1]
    witness = sp.Matrix([0, -5, -4, 5, -2, 2])
    h = metric*witness
    charges = [(h.T*w)[0] for w in weights]
    six_charge = next(q for q, n in Counter(charges[i] for i in sixteen).items() if n == 6)
    h /= 6*six_charge
    charges = [(h.T*w)[0] for w in weights]
    sm_roots = sorted(r for r in even if (h.T*sp.Matrix(r))[0] == 0)
    root_edges = {r: {s for s in sm_roots if r != s and
                      (sp.Matrix(r).T*metric*sp.Matrix(s))[0] != 0} for r in sm_roots}
    weak, color = components(sm_roots, root_edges)
    assert (len(weak), len(color)) == (2, 6)
    multiplets = weight_blocks(sixteen, sm_roots, roots)
    derived = []
    for block in multiplets:
        qs = {charges[i] for i in block}
        assert len(qs) == 1
        cb = weight_blocks(block, color, roots)
        wb = weight_blocks(block, weak, roots)
        dc, dw = len(cb[0]), len(wb[0])
        assert all(len(x) == dc for x in cb) and all(len(x) == dw for x in wb)
        assert len(block) == dc*dw
        derived.append({"indices": block, "color_dimension": dc, "weak_dimension": dw,
                        "Y": str(next(iter(qs)))})
    pattern = sorted((x["color_dimension"], x["weak_dimension"], x["Y"]) for x in derived)
    assert pattern == sorted([(3, 2, "1/6"), (3, 1, "-2/3"), (3, 1, "1/3"),
                              (1, 2, "-1/2"), (1, 1, "1"), (1, 1, "0")])
    hc = metric*sp.Matrix(color[0])
    hw = metric*sp.Matrix(weak[0])
    cs = [(hc.T*w)[0] for w in weights]
    ws = [(hw.T*w)[0] for w in weights]
    traces = {"Y": sum(charges[i] for i in sixteen),
              "Y3": sum(charges[i]**3 for i in sixteen),
              "color2Y": sum(cs[i]**2*charges[i] for i in sixteen),
              "weak2Y": sum(ws[i]**2*charges[i] for i in sixteen),
              "color3": sum(cs[i]**3 for i in sixteen)}
    assert set(traces.values()) == {0}
    # A generic Cartan element detects SU3's cubic invariant; a root coroot
    # alone has tr(H^3)=0 even on a single 3 and would be a vacuous control.
    hc2 = metric*sp.Matrix(color[1])
    cg = [((hc+2*hc2).T*w)[0] for w in weights]
    color_blocks = weight_blocks(sixteen, color, roots)
    cubic_parts = [sum(cg[i]**3 for i in b) for b in color_blocks]
    assert any(cubic_parts) and sum(cubic_parts) == 0
    traces["generic_color3"] = sum(cubic_parts)
    weak_blocks = weight_blocks(sixteen, weak, roots)
    doublets = sum(len(b) == 2 for b in weak_blocks)
    assert doublets == 4
    ec = next(b[0] for b in multiplets if len(b) == 1 and charges[b[0]] == 1)
    wrong = list(charges)
    wrong[ec] += sp.Rational(1, 6)
    assert sum(wrong[i]**3 for i in sixteen) != 0
    assert all(sum(charges[i] for i in t) == 0 for t in v.cubic()[0])
    # Canonical rational nullspace; coefficients are integers in the declared box.
    ns = sp.Matrix(sm_roots).nullspace()
    assert len(ns) == 3
    ns = [sp.Matrix([F(x) for x in a]) for a in ns]
    basis_charges = [[F((a.T*weights[i])[0]) for i in sixteen] for a in ns]
    target = {F(1, 6): 6, F(-2, 3): 3, F(1, 3): 3, F(-1, 2): 2, F(1): 1, F(0): 1}
    hits = set()
    for co in itertools.product(range(-6, 7), repeat=3):
        gr = Counter(sum(c*row[j] for c, row in zip(co, basis_charges)) for j in range(16))
        if sorted(gr.values()) != [1, 1, 2, 3, 3, 6] or gr.get(F(0)) != 1:
            continue
        g6 = next(g for g, n in gr.items() if n == 6)
        if not g6:
            continue
        scale = F(1, 6)/g6
        if {g*scale: n for g, n in gr.items()} == target:
            hits.add(tuple(F(sum(c*a[k] for c, a in zip(co, ns)))*scale for k in range(6)))
    # Existence and all hits are reported; no assertion encodes a hoped-for count.
    assert hits
    s, _, _, _, _, psi = v.embedding()
    source = next(i for i in range(27) if s[i])
    lookup = {tuple(w): i for i, w in enumerate(weights)}
    todo, paths = deque([source]), {source: []}
    while todo and 13 not in paths:
        i = todo.popleft()
        for k in range(6):
            j = lookup[tuple(weights[i]-weights[i][k]*v.CARTAN[:, k])]
            if j not in paths:
                paths[j] = paths[i]+[k]
                todo.append(j)
    u = sp.eye(27)
    for k in paths[13]:
        e = roots[tuple(v.CARTAN[:, k])]
        a = e-e.T
        assert a**3 == -a
        u = (sp.eye(27)+a+a*a)*u
    assert u.T*u == sp.eye(27)
    assert set(i for i in range(27) if (u*s)[i]) == {13}
    old = sp.diag(*(1 if x == 1 else -1 for x in psi))
    assert u*old*u.T == sp.diag(*d2)
    # Signed permutation acts on each tensor entry, including zeros.
    mapping = {j: next((i, u[i, j]) for i in range(27) if u[i, j]) for j in range(27)}
    assert all(sum(bool(u[i, j]) for i in range(27)) == 1 for j in range(27))
    transformed = {}
    for t, value in v.cubic()[3].items():
        dest = tuple(mapping[j][0] for j in t)
        transformed[dest] = value*sp.prod(mapping[j][1] for j in t)
    assert transformed == v.cubic()[3]
    return {"metric_equals_prior_Cartan_inverse": True,
            "metric": [[str(x) for x in row] for row in metric.tolist()],
            "root_length_counts": {str(k): n for k, n in root_lengths.items()},
            "weight_length_counts": {str(k): n for k, n in weight_lengths.items()},
            "d5_simple_roots": simple, "d5_Cartan": d5_cartan.tolist(),
            "derived_multiplets": derived, "trace_anomalies": traces,
            "nonvacuous_color_cubic_block_traces": cubic_parts,
            "weak_doublets": doublets, "normalized_witness_functional": list(h),
            "fixed_subsystem_box": [-6, 6], "distinct_normalized_histogram_hits": len(hits),
            "hit_functionals": [[str(x) for x in row] for row in sorted(hits)],
            "Weyl_path_simple_indices_zero_based": paths[13],
            "Weyl_transports_R4_grading_to_D2_and_preserves_cubic": True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--upstream-tests", action="store_true")
    args = parser.parse_args()
    with args.output.open("x") as output:
        start = time.monotonic()
        result = {"code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
                  "exact": exact_checks()}
        if args.upstream_tests:
            prefixes = ["b1242", "b1247", "b1248", "b1249", "b1250", "b1251", "b1252", "b1253"]
            paths = [str(p.relative_to(ROOT)) for prefix in prefixes
                     for p in sorted((ROOT / "tests").glob(f"test_{prefix}_*.py"))]
            cmd = [sys.executable, "-m", "pytest", *paths, "-q", "-p", "no:randomly"]
            run = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
            result["upstream_tests"] = {"command": cmd, "returncode": run.returncode,
                                        "stdout": run.stdout, "stderr": run.stderr}
        result["elapsed_seconds"] = time.monotonic()-start
        json.dump(result, output, indent=2, default=str)
        output.write("\n")
    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
