"""Generic deterministic record tests and exact old-detector controls.

Not a physical observer or a consciousness instrument. See the sealed design.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]


def validate(q, update=None, output=None):
    q = tuple(q)
    if not q or any(type(v) is not int or v < 0 for v in q):
        raise ValueError("nonempty integer quotient required")
    if set(q) != set(range(max(q) + 1)):
        raise ValueError("quotient labels must be contiguous and surjective")
    if update is not None:
        update = tuple(update)
        if len(update) != len(q) or any(type(v) is not int or not 0 <= v < len(q) for v in update):
            raise ValueError("total deterministic update required")
    if output is not None and len(output) != len(q):
        raise ValueError("one output per state required")
    return q


def descended_update(q, update):
    q = validate(q, update=update)
    images = {}
    for x, block in enumerate(q):
        image = q[update[x]]
        if block in images and images[block] != image:
            return None
        images[block] = image
    return tuple(images[b] for b in range(max(q) + 1))


def descended_output(q, output):
    q = validate(q, output=output)
    images = {}
    for x, block in enumerate(q):
        if block in images and images[block] != output[x]:
            return None
        images[block] = output[x]
    return tuple(images[b] for b in range(max(q) + 1))


def canonical_labels(keys):
    labels = {}
    return tuple(labels.setdefault(key, len(labels)) for key in keys)


def sufficient_record(updates, output):
    n = len(output)
    validate(tuple(range(n)), output=output)
    updates = tuple(tuple(t) for t in updates)
    for t in updates:
        validate(tuple(range(n)), update=t)
    q = canonical_labels(output)
    while True:
        refined = canonical_labels((q[x], tuple(q[t[x]] for t in updates)) for x in range(n))
        if refined == q:
            return q
        q = refined


def load_old(relative):
    spec = importlib.util.spec_from_file_location("old_record_probe", ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def source_controls():
    x, y, z, r, k = sp.symbols("x y z r k")
    invariant = x*x + y*y + z*z - 2*x*y*z - 1
    update = (z, x, 2*x*z-y)
    rewritten = (z, x, update[2]+r-invariant)
    same_graph = all(sp.expand(b.subs(r, invariant)-a) == 0 for a, b in zip(update, rewritten))
    equations = (x*(x-1), x*k)
    basis = sp.groebner(equations, x, k, order="lex")
    k_only = [p.as_expr() for p in basis.polys if p.as_expr().free_symbols <= {k}]
    point_basis = sp.groebner((x-1, k), x, k, order="lex")
    point_k_only = [p.as_expr() for p in point_basis.polys if p.as_expr().free_symbols <= {k}]
    jacobian = sp.Matrix(equations).jacobian((x, k)).subs({x: 1, k: 0})
    old = load_old("frontier/B130_no_forced_choice/probe.py")
    old_elimination = old.kappa_elimination(2)
    field_equal = sp.simplify(sp.sqrt(20)-2*sp.sqrt(5)) == 0
    old_matrices = [sp.Matrix([[m, 1], [1, 0]]) for m in (1, 4)]
    checks = {
        "original_trace_invariant": sp.expand(invariant.subs(dict(zip((x,y,z), update)), simultaneous=True)-invariant) == 0,
        "original_update_nonlinear": sp.Poly(update[2], x,y,z).total_degree() == 2,
        "original_literal_record_absent": not any(a.has(r) for a in update),
        "rewritten_literal_record_present": any(a.has(r) for a in rewritten),
        "rewritten_same_on_record_graph": same_graph,
        "syntactic_insertion_not_new_dynamics": sp.expand(rewritten[2]-update[2]) == r-invariant,
        "line_projects_to_every_k": all(sp.expand(e.subs(x, 0)) == 0 for e in equations),
        "isolated_point_satisfies": all(e.subs({x:1,k:0}) == 0 for e in equations),
        "isolated_point_full_jacobian_rank": jacobian.det() == 1,
        "global_elimination_empty_with_isolated_point": k_only == [],
        "point_only_opposite_elimination": point_k_only == [k],
        "actual_old_m2_empty_elimination_retained": old_elimination["k_only_elimination_polys"] == [],
        "perron_fields_one_and_four_equal": field_equal,
        "one_and_four_matrix_traces_distinct": old_matrices[0].trace() != old_matrices[1].trace(),
        "complex_conjugation_does_not_fix_K": sp.conjugate(sp.sqrt(-3)) == -sp.sqrt(-3),
    }
    if not all(type(v) is bool for v in checks.values()):
        raise TypeError("only ground boolean controls count")
    return {"checks": checks, "old_m2_groebner_generators": old_elimination["num_gens"],
            "mixed_variety_jacobian": str(jacobian),
            "scope": "generic detector countermodels; no actual-family component classification"}


def record_controls():
    q = (0,1,0,1)
    toggle = (1,2,3,0)
    unsafe = (1,1,2,2)
    delayed = sufficient_record((unsafe,), q)
    safe = sufficient_record((toggle,), q)
    checks = {
        "safe_update_descends": descended_update(q,toggle) == (1,0),
        "safe_output_descends": descended_output(q,q) == (0,1),
        "unsafe_update_rejected": descended_update(q,unsafe) is None,
        "unsafe_output_rejected": descended_output(q,(0,0,1,1)) is None,
        "faithful_update_retention": descended_update((0,1,2,3),unsafe) == unsafe,
        "delayed_difference_requires_more_record": delayed[0] != delayed[2],
        "safe_record_does_not_retain_every_history": safe[0] == safe[2] and safe[1] == safe[3],
        "no_declared_output_allows_trivial_record": sufficient_record((unsafe,), (0,0,0,0)) == (0,0,0,0),
    }
    return {"checks":checks,"safe_record":safe,"delayed_record":delayed}


def main():
    groups = {"source":source_controls(),"records":record_controls()}
    checks = [v for g in groups.values() for v in g["checks"].values()]
    result = {"groups":groups,"passed":sum(checks),"total":len(checks),"all_checks_pass":all(checks)}
    print(json.dumps(result,indent=2))
    return 0 if result["all_checks_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
