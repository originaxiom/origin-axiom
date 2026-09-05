"""Independent controls for the second upstream landing; no old file writes."""
import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import time

import sympy as sp

from . import vacuum as v

ROOT = Path(__file__).resolve().parents[2]


def module_at(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def polynomial_square(poly, symbols):
    coefficient, factors = sp.factor_list(poly, *symbols)
    return bool(sp.sqrt(coefficient).is_Rational and all(power % 2 == 0 for _, power in factors))


def kappa(a, b):
    return sp.trace(a*b*a.inv()*b.inv())


def dynamics_controls():
    old = module_at(ROOT / "frontier/B1254_class_dynamics/verification/class_dynamics.py")
    x, y, z = old.x, old.y, old.z
    kap = x*x+y*y+z*z-x*y*z-2
    traces = {"metallic": (z, x, x*z-y),
              "decimation": (x*x-2, y*y-2, x*y*z-x*x-y*y+2),
              "Thue_Morse": (z, z, x*y*z-x*x-y*y+2)}
    factors = {"metallic": sp.Integer(1), "decimation": x*x*y*y,
               "Thue_Morse": x*x+y*y-x*y*z}
    identities = {}
    for name, triple in traces.items():
        kp = kap.subs(dict(zip([x, y, z], triple)), simultaneous=True)
        identities[name] = str(sp.expand(kp-2-(kap-2)*factors[name]))
        assert identities[name] == "0"
    controls = []
    for p in [(x*y)**2, x*x+y*y-x*y*z, x*x+1]:
        controls.append({"polynomial": str(p), "upstream": bool(old.is_perfect_square(p)),
                         "factorization": polynomial_square(p, [x, y, z])})
    assert controls[0]["factorization"] and not controls[1]["factorization"]
    assert not controls[2]["factorization"]
    a, b = sp.Matrix([[0, -1], [1, 0]]), sp.diag(2, sp.Rational(1, 2))
    collapse = {"kappa_before": str(kappa(a, b)), "kappa_after": str(kappa(a*a, b*b)),
                "trace_A": str(sp.trace(a)), "A": [[str(t) for t in row] for row in a.tolist()],
                "B": [[str(t) for t in row] for row in b.tolist()]}
    assert kappa(a, b) != 2 and kappa(a*a, b*b) == 2
    a, b = sp.Matrix([[1, 1], [0, 1]]), sp.Matrix([[1, 0], [1, 1]])
    anew = a*b*a.inv()*b.inv()*a
    det_one = {"word_images": ["abABa", "b"], "abelianization": [[1, 0], [0, 1]],
               "kappa_before": str(kappa(a, b)), "kappa_after": str(kappa(anew, b)),
               "matrix_images_commute": anew*b == b*anew}
    assert kappa(anew, b) != kappa(a, b) and anew*b != b*anew
    tm = {"kappa_before": str(kappa(a, b)), "kappa_after": str(kappa(a*b, b*a)),
          "square_class_ratio": str((2-kappa(a*b, b*a))/(2-kappa(a, b)))}
    assert not sp.sqrt(sp.Rational(tm["square_class_ratio"])).is_Rational
    return {"exact_named_identity_remainders": identities, "square_predicate_controls": controls,
            "decimation_to_undefined_class": collapse, "determinant_one_not_Aut_witness": det_one,
            "rational_Thue_Morse_class_change": tm}


def rebuild_object():
    source = ROOT / "frontier/B854_centralizer_exact/e6_centralizer.py"
    raw = source.read_bytes()
    capture = io.StringIO()
    # The original producer writes results beside __file__; isolate that write.
    # All scientific outputs and the exact invariants are copied into our result.
    with tempfile.TemporaryDirectory(prefix="oa-b854-second-check-") as scratch:
        frame = {"__file__": str(Path(scratch) / "e6_centralizer.py"), "__name__": "b854_rebuilt"}
        with contextlib.redirect_stdout(capture):
            exec(compile(raw, str(source), "exec"), frame)
        side_result = json.loads((Path(scratch) / "results.json").read_text())
    assert frame["bad"] == 0 and side_result["invariant_rank"] == 4
    assert side_result["all_brackets_vanish"]
    _, rep, _, _, _ = v.representation()
    matrices = {n: sum((sp.Rational(c.numerator, c.denominator)*rep[i]
                        for i, c in enumerate(frame["INV"][n]) if c), sp.zeros(27))
                for n in frame["ns"]}
    mc = sum((co*matrices[n] for n, co in {8: 3, 14: 7, 16: 13, 22: 17}.items()), sp.zeros(27))
    signs = json.loads((ROOT / "frontier/B916_lambda_bridge/results.json").read_text())["H_prime_diag_vs_H_plus"]["D2"]
    d2 = sp.diag(*signs)
    old = module_at(ROOT / "frontier/B1255_generation_type/verification/generation_type.py")
    wt = v.representation()[0]
    assert [(-1)**int(sum(old.W13[i]*w[i] for i in range(6))+1) for w in wt] == signs
    columns, degree = old.colored_block(mc)
    basis = sp.Matrix.hstack(*columns)
    cm, dm = basis.solve(mc*basis), basis.solve(d2*basis)
    assert d2*basis == basis*dm
    plus, minus = [i for i, val in enumerate(signs) if val == 1], [i for i, val in enumerate(signs) if val == -1]
    split = [basis[plus, :].rank(), basis[minus, :].rank()]
    assert len(columns) == 18 and split == [12, 6]
    comm = cm*dm-dm*cm
    assert not comm.is_zero_matrix
    homogeneous = {}
    for sign in [-1, 1]:
        probe = dm-sign*sp.eye(18)
        stacked, current = probe, probe
        for power in range(1, 18):
            if stacked.rank() == 18:
                break
            current = current*cm
            stacked = stacked.col_join(current)
        rank = stacked.rank()
        assert rank == 18
        homogeneous[str(sign)] = {"observability_rank": rank, "kernel_dimension": 18-rank,
                                  "largest_power_used": stacked.rows//18-1}
    types = {name: old.cubic_type(coeff)[:4] for name, coeff in [("mu13", old.MU13), ("HIER", old.HIER_COEFFS)]}
    assert all(row[0] and row[1] == [7, 11] and row[2:] == ("S3", 3) for row in types.values())
    commuting_control = (d2*rep[0]-rep[0]*d2).is_zero_matrix
    assert commuting_control
    return {"B854_source_sha256": hashlib.sha256(raw).hexdigest(), "B854_stdout": capture.getvalue(),
            "B854_results": side_result,
            "B854_invariants": {str(n): list(map(str, frame["INV"][n])) for n in frame["ns"]},
            "cubic_types": {name: [bool(row[0]), list(map(int, row[1])), row[2], row[3]] for name, row in types.items()},
            "W18_dimension": len(columns), "color_factor_degree": int(degree), "D2_split": split,
            "commutator_rank": comm.rank(), "D2_homogeneous_C_eigenvector_controls": homogeneous,
            "commuting_Cartan_control": bool(commuting_control),
            "scope": "specified algebraic carrier and grading, not a complete classification of physical multiplicity"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    with args.output.open("x", encoding="utf-8") as handle:
        start = time.monotonic()
        result = {"dynamics": dynamics_controls(), "generation": rebuild_object(),
                  "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  "elapsed_seconds": time.monotonic()-start}
        json.dump(result, handle, indent=2, allow_nan=False)
        handle.write("\n")
    brief = {**result, "generation": {k: val for k, val in result["generation"].items()
                                     if k not in ["B854_invariants", "B854_stdout"]}}
    print(json.dumps(brief, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
