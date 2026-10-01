"""R69 separately sealed Gaussian normal-form repair; original files unchanged."""
import importlib.util
import json
from pathlib import Path

import sympy as s
from sympy.polys.polyerrors import CoercionFailed

PATH = Path(__file__).with_name("level_action.py")
SPEC = importlib.util.spec_from_file_location("level_action_original_r69_control", PATH)
C = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C)
original_rank = C.rank


def rank(a):
    return original_rank(C.clean(a))


C.rank = rank
cover = C.cover
exact_controls = C.exact_controls
source_controls = C.source_controls
action_controls = C.action_controls


def normalization_controls():
    product = s.Mul(-1-s.I, 1+s.I, evaluate=False)
    expression = s.Add(1, product, s.I, evaluate=False)
    zero = s.Add(1, product, s.I, -1, s.I, evaluate=False)
    refused = False
    try:
        original_rank(s.Matrix([[expression]]))
    except CoercionFailed:
        refused = True
    return {"checks": {
        "original_noncanonical_rejected": refused,
        "canonical_gaussian_rank": rank(s.Matrix([[expression]])) == 1,
        "canonical_zero_rank": rank(s.Matrix([[zero]])) == 0,
    }}


def run():
    prior = C.run()
    groups = dict(prior["groups"], normalization=normalization_controls())
    checks = {k+"/"+n: bool(v) for k,g in groups.items() for n,v in g["checks"].items()}
    return dict(groups=groups, checks=checks, all_checks_pass=all(checks.values()),
                scope=prior["scope"]+"; separately sealed expression normalization")


if __name__ == "__main__":
    output = run()
    print(json.dumps(output, sort_keys=True, default=str))
    raise SystemExit(0 if output["all_checks_pass"] else 1)
