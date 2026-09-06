"""R13 locks; scoped equations and discriminating controls, not a TOE test."""
import importlib.util
from pathlib import Path
import sys

import numpy as np
import pytest
import sympy as sp

PATH = Path(__file__).resolve().parents[1] / "reports/physical_bridge_2026_09_05/harmonic_cusp.py"
SPEC = importlib.util.spec_from_file_location("physical_bridge_harmonic_cusp", PATH)
HC = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = HC
SPEC.loader.exec_module(HC)


def test_exact_hyperbolic_kernel_and_wrong_cylinder_control():
    geo = HC.exact_geometry()
    assert geo["bessel_ode_residual"] == geo["normal_derivative_residual"] == "0"
    assert geo["cylinder_kernel_residual"] != "0"
    assert geo["relator_residual"] == "Matrix([[0, 0], [0, 0]])"
    assert geo["relator_period"] == 0


def test_symmetry_basis_has_both_leading_and_faster_mixed_mode():
    modes = HC.mode_basis(2)
    assert (modes[0].k, modes[0].l, modes[0].kind) == (2, 0, "SC")
    mixed = next(m for m in modes if m.k and m.l)
    assert (mixed.k, mixed.l, mixed.kind) == (2, 1, "CS")
    assert mixed.norm2 == 4*modes[0].norm2
    assert set(HC.exact_geometry()["symmetry_residuals"]) == {"0"}
    assert not any(m.k == 1 or (m.k == 0 and m.l == 1) for m in modes)
    assert any(m.k == 1 for m in HC.mode_basis(2, symmetry=False))


def test_word_action_and_period_cocycle_compose():
    u, v = "aBaba", "AbAB"
    w, z = .173+.82j, .63
    w1, z1 = HC.action(HC.word_matrix(v), w, z)
    w2, z2 = HC.action(HC.word_matrix(u), w1, z1)
    direct = HC.action(HC.word_matrix(u+v), w, z)
    assert np.allclose([w2, z2], direct, rtol=1e-12, atol=1e-12)
    assert HC.period(u+v) == HC.period(u)+HC.period(v)
    assert HC.period(HC.inverse_word(u)) == -HC.period(u)
    assert np.allclose(HC.word_matrix(u)@HC.word_matrix(HC.inverse_word(u)), np.eye(2), atol=1e-11)


def test_pullback_trace_recovers_actual_point_and_meridian_integer():
    moves = HC.moves(5)
    original = (2.23+3.17j, .53)
    w, z, ab, trace = HC.pullback(moves, *original, keep_trace=True)
    wr, zr = original
    counted = 0
    for kind, data in trace:
        if kind == "word":
            wr, zr = HC.action(HC.word_matrix(data), wr, zr)
            counted += HC.period(data)
        else:
            mu, lam = data
            wr -= mu+1j*HC.LENGTH*lam
            counted -= mu
    assert np.allclose([w, z], [wr, zr], atol=1e-12)
    assert ab == counted
    assert z >= original[1]
    assert HC.reduce_lattice(2.2+1j*HC.LENGTH)[1] == -2


def test_decaying_one_form_norm_is_finite_and_matches_boundary_identity():
    rows = HC.normalizable_control()
    assert all(r["integral"] > 0 and abs(r["difference"]) < 1e-12 for r in rows)
    assert rows[0]["integral"] > rows[1]["integral"] > rows[2]["integral"]
    p, q, L, z, z0, Z = sp.symbols("p q L z z0 Z", positive=True)
    norm = sp.integrate((L*p*p+q*q/L)/z, (z, z0, Z))
    assert sp.simplify(sp.diff(norm, Z)*Z-(L*p*p+q*q/L)) == 0
    assert sp.limit(norm.subs({p: 1, q: 0, L: 2, z0: 1}), Z, sp.oo) == sp.oo
    assert sp.integrate(L/z**3, (z, z0, sp.oo)) == L/(2*z0*z0)


def test_coweight_is_mixed_not_theta_odd():
    e6 = HC.coweight_parity()
    assert e6["root_count"] == 72 and e6["theta_cartan_fixed"] == 4
    assert e6["theta_isometry"] and e6["omega1_to_omega6"]
    rows = e6["directions"]
    assert not rows["omega1"]["even"] and not rows["omega1"]["odd"]
    assert rows["sum"]["even"] and rows["difference"]["odd"]
    assert rows["omega1"]["centralizer_dimension"] == rows["omega6"]["centralizer_dimension"] == 46
    assert rows["sum"]["centralizer_dimension"] == 30


def test_fit_controls_distinguish_period_and_manufactured_input():
    result = HC.fit(6, .65, 1302, HC.moves(5), controls=True)
    controls = result["controls"]
    assert result["rank"] == result["mode_count"]
    assert controls["zero_period_max_coefficient"] == 0
    assert controls["manufactured_field_holdout"] < 1e-10
    assert controls["manufactured_leading_error"] < 1e-10
    assert controls["wrong_cocycle_genuine_holdout"] > 1e-2


def test_acceptance_rejects_rank_residual_spread_and_zero_failures():
    base = {"rank": 20, "mode_count": 20, "holdout_max": 1e-7,
            "leading_coefficient": 1., "symmetry_restricted": True, "cutoff": 10}
    rows = [dict(base), dict(base), dict(base), dict(base, symmetry_restricted=False)]
    assert HC.acceptance(rows)["status"] == "NUMERICAL_CANDIDATE"
    for key, value in [("rank", 19), ("holdout_max", .01), ("leading_coefficient", 1.1)]:
        bad = [dict(r) for r in rows]
        bad[0][key] = value
        assert HC.acceptance(bad)["status"] == "UNRESOLVED"
    zero = [dict(r, leading_coefficient=0.) for r in rows]
    assert HC.acceptance(zero)["status"] == "UNRESOLVED"


def test_zero_columns_are_rejected_not_silently_normalized():
    with pytest.raises(ValueError, match="zero collocation column"):
        HC.least_squares(np.zeros((5, 2)), np.zeros(5))
