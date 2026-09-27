"""R49 post-failure QQ spectrum diagnostic; original science is immutable."""
import importlib.util
import json
from pathlib import Path

import sympy as s

spec = importlib.util.spec_from_file_location(
    "r49_original_end", Path(__file__).with_name("neutral_regularity.py"))
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def qq_coefficients(poly):
    values = poly.all_coeffs()
    if any(not value.is_Rational for value in values):
        raise ValueError("Not a polynomial with exact rational coefficients")
    return tuple(s.Rational(value) for value in values)


def target_poly(gen, multiplicities):
    expression = s.prod((gen-eigen)**count
                        for eigen, count in zip((0, 2, 6), multiplicities))
    return s.Poly(expression, gen, domain=s.QQ)


def matrix_projectors(matrix):
    ident = s.eye(matrix.rows)
    projectors = []
    for eigen in (0, 2, 6):
        proj = ident
        for other in (0, 2, 6):
            if other != eigen:
                proj = proj*(matrix-other*ident)/s.Integer(eigen-other)
        projectors.append(r.clean(proj))
    return tuple(projectors)


def analyze(matrix, multiplicities):
    if any(not value.is_Rational for value in matrix):
        raise ValueError("The diagnostic requires a rational matrix")
    cp = matrix.charpoly(r.Z)
    ident = s.eye(matrix.rows)
    projectors = matrix_projectors(matrix)
    expected = target_poly(r.Z, multiplicities)
    ranks = [(matrix-eigen*ident).rows-(matrix-eigen*ident).rank()
             for eigen in (0, 2, 6)]
    checks = {
        "qq_coefficient_identity": qq_coefficients(cp) == qq_coefficients(expected),
        "returned_generator_identity": r.zero(cp.as_expr()-target_poly(cp.gen, multiplicities).as_expr()),
        "kernel_multiplicities": ranks == list(multiplicities),
        "annihilating_polynomial": r.zero(matrix*(matrix-2*ident)*(matrix-6*ident)),
        "projector_sum": r.zero(sum(projectors, s.zeros(matrix.rows))-ident),
        "projector_idempotence": all(r.zero(p*p-p) for p in projectors),
        "projector_orthogonality": all(r.zero(p*q) for i,p in enumerate(projectors)
                                        for j,q in enumerate(projectors) if i != j),
        "projector_ranks": [p.rank() for p in projectors] == list(multiplicities),
        "projector_reconstruction": r.zero(sum((e*p for e,p in zip((0,2,6),projectors)),
                                               s.zeros(matrix.rows))-matrix),
    }
    return {
        "dimension": matrix.rows,
        "requested_generator": str(r.Z),
        "returned_generator": str(cp.gen),
        "requested_assumptions": r.Z.assumptions0,
        "returned_assumptions": cp.gen.assumptions0,
        "same_generator": cp.gen == r.Z,
        "same_printed_generator": str(cp.gen) == str(r.Z),
        "original_residual_zero": r.zero(cp.as_expr()-expected.as_expr()),
        "polynomial": str(s.factor(cp.as_expr())),
        "kernel_dimensions": ranks,
        "checks": checks,
    }


def controls():
    zreal = s.Symbol("toy_z", real=True)
    zplain = s.Symbol("toy_z")
    toy = s.diag(2, 6).charpoly(zreal)
    good = s.Poly((zreal-2)*(zreal-6), zreal, domain=s.QQ)
    bad = s.Poly(good.as_expr()+1, zreal, domain=s.QQ)
    altered = r.operators()[5].copy()
    altered[0,0] += 1
    rejected_symbolic = False
    try:
        qq_coefficients(s.Poly(zreal+s.Symbol("unrelated_coefficient"), zreal))
    except ValueError:
        rejected_symbolic = True
    return {
        "toy_exact_coefficients_recovered": qq_coefficients(toy) == qq_coefficients(good),
        "wrong_coefficient_rejected": qq_coefficients(toy) != qq_coefficients(bad),
        "same_name_symbols_not_merged": zreal != zplain and not r.zero(zreal-zplain),
        "symbolic_coefficient_rejected": rejected_symbolic,
        "changed_actual_spectrum_rejected": qq_coefficients(altered.charpoly())
            != qq_coefficients(target_poly(r.Z,(1,3,11))),
        "changed_actual_annihilator_rejected": not r.zero(
            altered*(altered-2*s.eye(15))*(altered-6*s.eye(15))),
        "toy_expression_in_actual_generator": r.zero(
            toy.as_expr()-(toy.gen-2)*(toy.gen-6)),
    }


def run():
    _, _, _, _, _, matrix = r.operators()
    inclusion, small, residual = r.zero_weight_restriction()
    full = analyze(matrix, (1,3,11))
    restricted = analyze(small, (1,3,5))
    checks = controls()
    checks["unchanged_invariant_restriction"] = inclusion.cols == 9 and r.zero(residual)
    return {
        "sympy_version": s.__version__,
        "full": full,
        "zero_longitude": restricted,
        "controls": checks,
        "all_exact_checks_pass": all(full["checks"].values())
            and all(restricted["checks"].values()) and all(checks.values()),
        "generator_mismatch_diagnosis": all(row["same_printed_generator"]
            and not row["same_generator"] and not row["original_residual_zero"]
            for row in (full, restricted)),
        "original_failures_preserved": True,
        "independent_PDE_review": False,
        "physical_spectrum_derived": False,
    }


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["all_exact_checks_pass"]
                     and result["generator_mismatch_diagnosis"] else 1)
