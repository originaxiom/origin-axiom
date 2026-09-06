"""Native-scalar export wrapper; the sealed G2 inference instrument is unchanged."""
import argparse
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from . import g2_isolation_audit as original

ORIGINAL_SHA = "1202a721b478daa6e91b46af9f17507c34c1fa259315799db683c3204485cc5d"


def native(value):
    if isinstance(value, np.generic):
        return native(value.item())
    if isinstance(value, dict):
        return {native(key): native(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [native(item) for item in value]
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    raise TypeError(f"Unsupported export type: {type(value).__name__}")


def analyze():
    assert hashlib.sha256(Path(original.__file__).read_bytes()).hexdigest() == ORIGINAL_SHA
    return native(original.analyze())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    start = time.monotonic()
    result = {**analyze(), "original_source_sha256": ORIGINAL_SHA,
              "export_source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "elapsed_seconds": time.monotonic()-start}
    payload = json.dumps(result, indent=2, allow_nan=False)+"\n"
    with args.output.open("x", encoding="utf-8") as handle:
        handle.write(payload)
    print(json.dumps({"G2_example_element_fixed_dimensions": result["exact_G2_counterexample"]["nonidentity_fixed_dimensions"],
                      "G2_example_common_fixed_dimension": result["exact_G2_counterexample"]["common_fixed_dimension"],
                      "B1084_common_fixed_dimension": result["actual_B1084_group"]["exact_common_fixed_dimension"],
                      "B1084_element_census": result["actual_B1084_group"]["nonidentity_element_census"],
                      "B1084_A1_E6_intersections": result["actual_B1084_group"]["A1_E6_intersection_dimensions"],
                      "upstream_returncode": result["upstream_B1259_selftest"]["returncode"],
                      "elapsed_seconds": result["elapsed_seconds"], "scope": result["scope"]}, indent=2))


if __name__ == "__main__":
    main()
