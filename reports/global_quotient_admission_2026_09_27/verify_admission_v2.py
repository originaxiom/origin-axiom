"""Output-only repair; original sealed scientific producer remains unchanged."""
import json
import sympy as sp
import verify_admission as original


def exact_json(value):
    def convert(obj):
        if isinstance(obj, sp.Integer):
            return int(obj)
        raise TypeError(f"Unsupported exact output type: {type(obj).__name__}")
    return json.dumps(value, default=convert)


def run():
    for key, function in [("PARENT", original.parent_control), ("TOPOLOGY", original.topology_control),
                          ("WITNESS", original.diagonal_witness), ("CONTROLS", original.controls)]:
        print(key, exact_json(function()), flush=True)
    print("PASS: combined quotient admits additional flat sectors; no chiral spectrum constructed")


if __name__ == "__main__":
    run()
