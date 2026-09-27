"""Finite identity/application controls, not a global PDE proof; stdout only."""
from functools import lru_cache
from pathlib import Path
import json
import sys
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "monomial_exceptional_locus_2026_09_27"))
import verify_exceptional as ex
from verify_global_seed import eye, pullback
from verify_topology import cover


def inputs():
    return json.loads((HERE / "INPUTS.json").read_text())


@lru_cache(None)
def anchored_control():
    r, R = sp.symbols("r R", real=True)
    f = sp.Function("f")(r)
    w = sp.exp(-r)*f
    assert sp.simplify(sp.diff(w, r)+w-sp.exp(-r)*sp.diff(f, r)) == 0
    x = sp.Symbol("x", nonnegative=True)
    assert sp.integrate(sp.exp(-x), (x, 0, sp.oo)) == 1
    assert sp.integrate(sp.exp(-2*x), (x, 0, sp.oo)) == sp.Rational(1, 2)
    # Constant primitive is normalizable; its derivative is zero, so an
    # unanchored/global no-kernel bound would already fail this control.
    assert sp.integrate(sp.exp(-2*r), (r, R, sp.oo)) == sp.exp(-2*R)/2
    one_form_density = sp.exp(2*r)*sp.exp(-2*r)
    assert one_form_density == 1
    assert sp.integrate(one_form_density, (r, R, sp.oo)) == sp.oo
    v = sp.Function("v")(r)
    hardy = sp.exp(-2*r)*sp.diff(sp.exp(r)*v, r)**2
    assert sp.simplify(hardy-sp.diff(v, r)**2-v**2-sp.diff(v**2, r)) == 0
    return {"anchored_identity": True, "young_kernel_L1": 1,
            "slice_factor_squared": "1/2", "constant_primitive_is_L2": True,
            "stationary_tangential_period_is_not_L2": True}


@lru_cache(None)
def frame_control():
    frame = sp.Matrix([[2, 1], [0, 1]])
    metric = frame.inv().T*frame.inv()
    x = sp.Matrix([2, -3])
    assert (frame*x).T*metric*(frame*x) == x.T*x
    assert (frame*x).T*(frame*x) != x.T*x
    assert metric.det() > 0 and metric[0, 0] > 0
    r = sp.Symbol("r", nonnegative=True)
    a = sp.Symbol("a", positive=True)
    # D=d+a dr has an unbounded flattening frame exp(a r).
    # A closed transported torus period exp(-a r) dx becomes L2; this
    # is deliberately NOT a background satisfying our bounded-end premise.
    p = sp.exp(-a*r)
    assert sp.diff(p, r)+a*p == 0
    assert sp.integrate(p*p, (r, 0, sp.oo)) == 1/(2*a)
    assert sp.limit(sp.exp(a*r), r, sp.oo) == sp.oo
    q = sp.Function("q")(r)
    bounded_model = sp.exp(sp.exp(-r))
    potential = sp.diff(bounded_model, r)/bounded_model
    assert sp.simplify(sp.diff(bounded_model*q, r)/bounded_model-sp.diff(q, r)-potential*q) == 0
    return {"transformed_gram": metric, "wrong_norm_rejected": True,
            "unbounded_frame_counterexample_norm": "1/(2*a)",
            "chain_conjugacy_sign": True}


@lru_cache(None)
def projection_control():
    d = sp.Matrix([[1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 0]])
    d1 = sp.Matrix([[1, -1, 1, 0]])
    g0 = sp.diag(2, 3, 5)
    v = sp.Matrix([1, -1, 2, 1])
    g1 = sp.eye(4)+v*v.T
    adjoint = g0.inv()*d.T*g1
    lap = adjoint*d
    kernel = sp.diag(0, 0, 1)
    assert lap.det() == 0 and lap.rank() == 2
    green = (lap+kernel).inv()-kernel
    assert lap*green == green*lap == sp.eye(3)-kernel
    assert kernel*adjoint == sp.zeros(3, 4)
    alpha = sp.Matrix([0, 0, 0, 1])+d*sp.Matrix([2, -1, 7])
    beta = alpha-d*green*adjoint*alpha
    assert d1*d == sp.zeros(1, 3) and d1*beta == sp.zeros(1, 1)
    assert adjoint*beta == sp.zeros(3, 1) and beta != sp.zeros(4, 1)
    assert d.row_join(beta-alpha).rank() == d.rank()
    assert adjoint*(alpha+d*green*adjoint*alpha) != sp.zeros(3, 1)
    exact = d*sp.Matrix([3, 1, 9])
    assert exact-d*green*adjoint*exact == sp.zeros(4, 1)
    assert (beta.T*g1*beta)[0] > 0
    return {"kernel_dimension": 1, "reduced_inverse_identity": True,
            "beta": beta, "norm_squared": (beta.T*g1*beta)[0],
            "exact_class_removed": True, "wrong_sign_rejected": True}


@lru_cache(None)
def moment_control():
    # Pointwise jet expansion of (d_A+Psi)^dagger(d_A+Psi) on zero-forms.
    # Connection and Hermitian Higgs genuinely do NOT commute.
    a = sp.Matrix([[0, 1], [-1, 0]])
    p = sp.Matrix([[2, 1], [1, -1]])
    assert a.T == -a and p.T == p and a*p-p*a != sp.zeros(2)
    v = sp.Matrix(sp.symbols("v0:2"))
    dv = sp.Matrix(sp.symbols("w0:2"))
    ddv = sp.Matrix(sp.symbols("u0:2"))
    dp = -(a*p-p*a)  # covariant divergence vanishes in this one-jet control
    full = -ddv-(a+p)*dv-dp*v+(-a+p)*(dv+(a+p)*v)
    unitary_lap = -ddv-2*a*dv-a*a*v
    assert sp.simplify(full-unitary_lap-p*p*v) == sp.zeros(2, 1)
    bad_dp = sp.eye(2)
    bad = -ddv-(a+p)*dv-bad_dp*v+(-a+p)*(dv+(a+p)*v)
    residual = -(bad_dp+a*p-p*a)*v
    assert sp.simplify(bad-unitary_lap-p*p*v-residual) == sp.zeros(2, 1)
    assert residual != sp.zeros(2, 1)
    return {"noncommuting_fixture": True, "moment_zero_cancels_cross_term": True,
            "nonzero_moment_residual_retained": True}


@lru_cache(None)
def torus_control():
    p = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    identity = sp.eye(3)
    d0 = sp.Matrix.vstack(sp.zeros(3), p-identity)
    d1 = sp.Matrix.hstack(-(p-identity), sp.zeros(3))
    assert d1*d0 == sp.zeros(3)
    assert 3-d0.rank() == 1 and 6-d0.rank()-d1.rank() == 2
    # Nontrivial unitary meridian, exactly -1, removes all torus cohomology.
    charged0 = sp.Matrix.vstack(-2*identity, p-identity)
    charged1 = sp.Matrix.hstack(-(p-identity), -2*identity)
    assert charged1*charged0 == sp.zeros(3)
    assert 3-charged0.rank() == 0 and 6-charged0.rank()-charged1.rank() == 0
    return {"invariant_channel_H0_H1": [1, 2], "nontrivial_unitary_mu_H0_H1": [0, 0]}


@lru_cache(None)
def actual_point(number, point_name):
    inp = inputs()
    point = next(p for p in inp["points"] if p["name"] == point_name)
    value = ex.companion(point["polynomial"])
    degree = value.nrows()
    mods = ex.modules(ex.inputs()["seeds"][number])
    out = {"seed": number, "point": point_name, "field_degree": degree, "coefficients": {}}
    rels, mu, lam = cover(inp["cover"])
    for name in inp["coefficients"]:
        rep = pullback(ex.specialization(mods[name], value))
        assert rep.word(mu) == eye(rep.d)
        longitude = rep.word(lam)
        assert longitude.transpose()*longitude == eye(rep.d)
        assert all(rep.word(r) == eye(rep.d) for r in rels)
        record, _ = ex.indexed(rep, inp["cover"], degree)
        a, b = record["V"], record["dual"]
        n, nd = a[1]-a[4], b[1]-b[4]
        assert a[0] == b[0]
        assert a[2] == b[2] == inp["prior_boundary_fixed_dimensions"][name]
        # C is an ANALYTIC consequence of PROOF.md, not computed PDE kernels.
        conditional_degrees = (a[0], n, nd, b[0])
        left_minus_right = n+b[0]-a[0]-nd
        assert left_minus_right == record["I"]
        if name == "E":
            assert n == nd == inp["prior_E_interior_counts"][point_name]
            assert a[0] == inp["prior_E_H0_counts"][point_name]
        out["coefficients"][name] = {"ordinary": record,
            "conditional_harmonic_degrees": conditional_degrees,
            "conditional_left_minus_right": left_minus_right}
        if point_name == "two":
            # Rational real matrices: entrywise conjugate equals original,
            # but the contragredient need not equal it.
            assert any(g.inv().transpose() != g for g in rep.mats)
    return out


def serializable(value):
    if isinstance(value, sp.MatrixBase):
        return [[str(x) for x in row] for row in value.tolist()]
    if isinstance(value, sp.Basic):
        return str(value)
    if isinstance(value, dict):
        return {k: serializable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serializable(x) for x in value]
    return value


def main():
    for label, fun in (("ANCHORED", anchored_control), ("FRAME", frame_control),
                       ("PROJECTION", projection_control), ("MOMENT", moment_control),
                       ("TORUS", torus_control)):
        print(label, json.dumps(serializable(fun())), flush=True)
    for number in inputs()["seeds"]:
        for point in inputs()["points"]:
            print("APPLICATION", json.dumps(actual_point(number, point["name"])), flush=True)
    print("SCOPE", json.dumps({"analytic_grade": "authored, not machine-certified",
          "physical_model": "supplied action/metric/complete domain",
          "global_PDE_numerically_solved": False, "all_t_from_this_grid": False,
          "isolated_4d_EFT": False, "full_gauge_centralizer_classified": False}), flush=True)
    print("PASS: finite bridge controls and exact application inputs, not independent analytic review")


if __name__ == "__main__":
    main()
