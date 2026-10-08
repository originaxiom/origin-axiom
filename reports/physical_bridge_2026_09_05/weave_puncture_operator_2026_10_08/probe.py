"""Exact local operator benchmark, not a global physical spectrum solver.

No imports of another seat's science or stored results. Run only after
the research seal is committed, pushed and server-confirmed.
"""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


def sheaf_index(rank: int, weights: tuple[Fraction, ...], allowed: int) -> int:
    """RR on a genus-one curve for a length-allowed upper modification.

The unitary parabolic-degree theorem and RR are proved/cited in PROOF.md;
this function checks their exact bookkeeping, not an analytic PDE index.
"""
    if rank < 1 or len(weights) != rank or not 0 <= allowed <= rank:
        raise ValueError("inconsistent rank, weights or modification length")
    if any(not 0 <= a < 1 for a in weights):
        raise ValueError("canonical weights must lie in [0,1)")
    degree = -sum(weights, Fraction())
    if degree.denominator != 1:
        raise ValueError("nonintegral degree: not a compatible unitary datum")
    return int(degree) + allowed


def coefficient_domain(projector: sp.Matrix) -> dict:
    """Finite critical coefficients ONLY; no global ellipticity assertion."""
    n = projector.rows
    if projector.cols != n:
        raise ValueError("square channel projector required")
    p = projector
    i = sp.eye(n)
    if p != p.H or p * p != p:
        raise ValueError("orthogonal projector required")
    green = sp.zeros(2 * n)
    green[:n, n:] = i
    green[n:, :n] = i
    columns = [sp.Matrix.vstack(v, sp.zeros(n, 1)) for v in p.columnspace()]
    columns += [sp.Matrix.vstack(sp.zeros(n, 1), v) for v in (i-p).columnspace()]
    k = sp.Matrix.hstack(*columns)
    gamma = sp.diag(*([1] * n + [-1] * n))
    return {
        "plus_rank": p.rank(), "total_rank": k.rank(),
        "green_zero": k.H * green * k == sp.zeros(n),
        "grading_kept": sp.Matrix.hstack(k, gamma*k).rank() == n,
    }


def radial_class(s: Fraction, kind: str) -> str:
    """Leading norm integrability for f~r^s with nonzero coefficient.

One-form/smooth spin: r^(2s+1)dr. Canonically transported cusp spin:
r^(2s)/|log r| dr. Borderline cusp exponent -1 diverges logarithmically.
"""
    if kind in ("one_form", "smooth_spin"):
        return "finite" if 2*s + 1 > -1 else "divergent"
    if kind == "cusp_spin":
        return "finite" if 2*s > -1 else "divergent"
    raise ValueError("unknown kinetic norm")


def run() -> dict:
    facts: dict[str, bool] = {}
    def check(name: str, predicate) -> None:
        facts[name] = bool(predicate)
        if not facts[name]:
            raise AssertionError(name)

    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    a, b = sp.I * sx, sp.I * sy
    comm = a*b*a.inv()*b.inv()
    check("quaternion_commutator_minus_I", comm == -sp.eye(2))
    wcomm = sp.diag(comm, comm, comm)
    check("all_six_puncture_channels_minus_I", wcomm == -sp.eye(6))
    weights = (Fraction(1, 2),) * 6
    indices = [sheaf_index(6, weights, d) for d in range(7)]
    check("sheaf_degree_minus_three", sheaf_index(6, weights, 0) == -3)
    check("all_seven_sheaf_indices", indices == list(range(-3, 4)))
    check("dual_complement_indices_opposite", all(indices[d] == -indices[6-d] for d in range(7)))
    profiles = []
    for d in range(7):
        p = sp.diag(*([1]*d + [0]*(6-d)))
        profile = coefficient_domain(p)
        profiles.append(profile)
        check(f"rank_{d}_maximal_isotropic_graded", profile == {
            "plus_rank": d, "total_rank": 6, "green_zero": True, "grading_kept": True})
    u = sp.eye(6)
    u[:2, :2] = sp.Matrix([[1, 1], [-1, 1]]) / sp.sqrt(2)
    p3 = u * sp.diag(1, 0, 1, 1, 0, 0) * u.H
    check("non_diagonal_rank3_domain", coefficient_domain(p3)["green_zero"] and p3.rank() == 3)
    rotation = sp.eye(6)
    rotation[:2, :2] = sp.diag(1, -1)
    check("local_coefficient_does_not_imply_full_U6", rotation*p3 != p3*rotation)
    green = sp.Matrix([[0, 1], [1, 0]])
    bad = sp.Matrix([1, 1])
    check("nonisotropic_control_detected", (bad.H*green*bad)[0] != 0)

    x, y = sp.symbols("x y", real=True)
    omega = sp.Function("Omega")(x, y)
    psi = sp.Matrix([sp.Function("u")(x, y), sp.Function("v")(x, y)])
    def dflat(v):
        return -sp.I*(sx*v.diff(x) + sy*v.diff(y))
    def dconformal(v):
        return -sp.I/omega*(sx*v.diff(x) + sy*v.diff(y)
            + (sx*omega.diff(x) + sy*omega.diff(y))*v/(2*omega))
    conformal_residual = sp.simplify(dconformal(psi/sp.sqrt(omega)) - dflat(psi)/omega**sp.Rational(3, 2))
    check("spin_connection_confirms_correct_weight", conformal_residual == sp.zeros(2, 1))
    wrong = sp.simplify(dconformal(psi/omega) - dflat(psi)/omega**2)
    check("wrong_conformal_weight_fails", wrong != sp.zeros(2, 1))
    zpole = (x+sp.I*y)**(-sp.Rational(1, 2))
    check("actual_square_root_pole_solves_flat_chiral_equation",
          sp.simplify(dflat(sp.Matrix([zpole, 0]))) == sp.zeros(2, 1))
    theta = sp.symbols("theta", real=True)
    local_pair = sp.diag(sp.exp(-sp.I*theta/2), sp.exp(sp.I*theta/2))
    cliff = sp.Matrix([[0, sp.exp(-sp.I*theta)], [sp.exp(sp.I*theta), 0]])
    check("polar_current_reduces_to_coefficient_green_form",
          sp.simplify(local_pair.H*cliff*local_pair) == green)

    norms = {kind: radial_class(Fraction(-1, 2), kind)
             for kind in ("one_form", "smooth_spin", "cusp_spin")}
    check("one_form_pole_stays_integrable", norms["one_form"] == "finite")
    check("smooth_spin_pole_integrable", norms["smooth_spin"] == "finite")
    check("complete_cusp_spin_pole_not_integrable", norms["cusp_spin"] == "divergent")
    check("regular_cusp_spin_control", radial_class(Fraction(1, 2), "cusp_spin") == "finite")
    r = sp.symbols("r", positive=True)
    norm_primitive = sp.log(-sp.log(r))
    check("log_log_divergence_exact_derivative",
          sp.simplify(-sp.diff(norm_primitive, r) - 1/(r*(-sp.log(r)))) == 0)
    spin_boundary = -sp.eye(6)
    total = spin_boundary*wcomm
    check("twisted_tangent_holonomy_periodic", total == sp.eye(6))
    check("six_zero_vertical_plus_channels", len((total-sp.eye(6)).nullspace()) == 6)
    check("untwisted_bounding_control_has_no_vertical_zero",
          len((spin_boundary-sp.eye(6)).nullspace()) == 0)

    s, t = sp.symbols("s t", real=True)
    rho = sp.exp(-t)
    v = sp.Function("v")(t)
    # Before unitary volume conjugation: partial_t + rho'/2rho.
    radial = sp.simplify(sp.sqrt(rho)*(
        sp.diff(v/sp.sqrt(rho), t) + sp.diff(rho, t)/(2*rho)*v/sp.sqrt(rho)))
    check("unitary_cusp_radial_operator_has_no_mass", radial == sp.diff(v, t))
    bump = s**2*(1-s)**2
    n0 = sp.integrate(bump**2, (s, 0, 1))
    n1 = sp.integrate(sp.diff(bump, s)**2, (s, 0, 1))
    check("weyl_bump_norm_exact", n0 == sp.Rational(1, 630))
    check("weyl_bump_derivative_exact", n1 == sp.Rational(2, 105))
    check("weyl_residual_squared_twelve_over_L_squared", n1/n0 == 12)
    check("bump_and_derivative_glue_in_H1", all(
        sp.diff(bump, s, order).subs(s, endpoint) == 0 for order in (0, 1) for endpoint in (0, 1)))
    n = sp.symbols("n", integer=True, positive=True)
    check("weyl_supports_escape_and_are_disjoint", sp.expand((n+1)**3-(n**3+n)).is_positive)
    check("weyl_residual_tends_to_zero", sp.limit(12/n**2, n, sp.oo) == 0)
    lam = sp.symbols("lambda", real=True)
    radial_symbol = sp.Matrix([[0, -sp.I*lam], [sp.I*lam, 0]])
    eigenvector = sp.Matrix([1, sp.I])/sp.sqrt(2)
    check("weyl_symbol_eigenvector_all_real_lambda", radial_symbol*eigenvector == lam*eigenvector)
    return {
        "schema": "weave-puncture-operator-v1",
        "grade": "conditional_local_and_sheaf_research_not_physical_spectrum",
        "facts": facts, "predicates_passed": len(facts),
        "sheaf_indices": indices, "local_coefficient_domains": profiles,
        "pole_norms": norms, "weyl_residual_squared": "12/L^2",
        "hodge_triplet_refuted": False, "physical_chiral_SM_derived": False,
        "finite_distance_global_graph_index_certified": False,
        "complete_massless_standard_spin_cusp_fredholm_at_zero": False,
        "generated_action_or_domain_selected": False,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
