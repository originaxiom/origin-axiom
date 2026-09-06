"""Exact SymPy domain adapter for sealed R11; no change to its mathematics."""
import argparse
from contextlib import contextmanager
import hashlib
import json
from pathlib import Path

import sympy as sp

from . import family_action as f

ORIGINAL_INTEGERIZE = f.integerize
PINS = {
    "reports/physical_bridge_2026_09_05/family_action.py": "a26d0c0451a360a6d2d1e8ff5044a84eb6a2b6bc3e6089db4e7b61b914e4b02f",
    "tests/test_physical_bridge_family_action.py": "e5cbc92349c8c5805070f056d2d0d530ce58ddc586a42f6f27804c999046f3b9",
}


def integerize(coords, denominator=None):
    ints, den = ORIGINAL_INTEGERIZE(coords, denominator)
    converted = ints.to_DM(domain=sp.ZZ).to_Matrix()
    assert converted == ints and converted.to_DM().domain == sp.ZZ
    return converted, den


@contextmanager
def exact_domain():
    for name, digest in PINS.items():
        assert hashlib.sha256((f.ROOT/name).read_bytes()).hexdigest() == digest, name
    previous = f.integerize
    f.integerize = integerize
    try:
        yield
    finally:
        f.integerize = previous


def run():
    with exact_domain():
        result = f.run()
    result["runtime_adapter"] = "family_action_domain: exact integral QQ-to-ZZ conversion only"
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    result = run()
    blob = json.dumps(result, default=f.json_default, indent=2, sort_keys=True)+"\n"
    with args.output.open("x", encoding="utf-8") as handle:
        handle.write(blob)
    print(json.dumps({"actions": len(result["all_twenty_actions"]),
                      "lattice_det": result["lattice"]["gram_determinant"],
                      "covariance_checks": result["unit_conjugation_covariance_checks"],
                      "runtime_seconds": result["runtime_seconds"]}))


if __name__ == "__main__":
    main()
