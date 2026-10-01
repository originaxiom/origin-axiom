"""R69 separately sealed algebraic-zero equality repair; prior outputs immutable."""
import importlib.util
import json
from pathlib import Path

import sympy as s

PATH = Path(__file__).with_name("level_action_control.py")
SPEC = importlib.util.spec_from_file_location("level_action_control_original_r69_v2", PATH)
A = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(A)
cover = A.cover
source_controls = A.source_controls
action_controls = A.action_controls


def exact_controls():
    previous = A.exact_controls()
    _, _, coc, jac, _ = A.C.candidates()
    checks = dict(previous["checks"])
    checks["cocycle_relations"] = A.C.clean(jac*coc) == s.zeros(jac.rows,1)
    return dict(previous, checks=checks)


def equality_controls():
    _, _, coc, jac, _ = A.C.candidates()
    raw = jac*coc
    perturbation = next(j for j in range(jac.cols) if A.C.clean(jac[:,j]) != s.zeros(jac.rows,1))
    opposite = coc+s.eye(jac.cols)[:,perturbation]
    return {"checks": {
        "previous_structural_failure_retained": not A.exact_controls()["checks"]["cocycle_relations"],
        "canonical_cocycle_zero": A.rank(A.C.clean(raw)) == 0,
        "perturbed_cocycle_nonzero": A.rank(A.C.clean(jac*opposite)) != 0,
    }}


def run():
    original = A.run()
    groups = dict(original["groups"], exact=exact_controls(), equality=equality_controls())
    checks = {k+"/"+n: bool(v) for k,g in groups.items() for n,v in g["checks"].items()}
    return dict(groups=groups, checks=checks, all_checks_pass=all(checks.values()),
                scope=original["scope"]+"; separately sealed canonical cocycle equality")


if __name__ == "__main__":
    output = run()
    print(json.dumps(output, sort_keys=True, default=str))
    raise SystemExit(0 if output["all_checks_pass"] else 1)
