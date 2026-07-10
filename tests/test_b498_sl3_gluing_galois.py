"""Locks for B498 (Gate A class 2d: the SL(3) gluing-variety class, sealed).

Loads the banked JSON for the assembled claims and INDEPENDENTLY recomputes the
decisive facts with the probe's machinery (so the lock does not merely trust
the JSON): (1) the CONTROL -- B71/P24 reproduced: Fix(T_1^2) = V0 + W1 + W2,
exactly three components, each dim 2, by a complete exact case split, with the
Sym^2 shadow on V0 and the M^3 = L / M^3 L = 1 scalar criteria; (2) the
inversion involution psi (order 4, psi^2 = theta, conjugates T_1^2 to its
inverse, swaps W1 <-> W2, fixes V0); (3) the exact Sym^2 -> V0 identity and the
geometric pair ((1 +- 3 sqrt-3)/2, e-syms 1 and 7); (4) the degree=rank scalar
c = 1 on BOTH W1 and W2 at 40 digits at an exact rational point; (5) the exact
transverse-Jacobian torsion (tau_V0 = -4(p-1)(q-1)(pq-4), tau_W = -3(p-q)^2,
tau_V0(geo) = -84, multiplier quartic u^2 - 9u + 42, disc -87); (6) the Ptolemy
N=3 class-0 fields from the BUNDLED B444 equations (offline sympy Groebner:
degree 6, eliminant (c-1)(4c^2-c+4), fields Q(sqrt-3) + Q(sqrt-7)); (7) the
seal / documentation integrity. SnapPy (obstruction class 1) is behind
importorskip. Total runtime well under 60 s.
"""
import importlib.util
import json
import pathlib

import pytest
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_DIR = _ROOT / "frontier" / "B498_sl3_gluing_galois"

_spec = importlib.util.spec_from_file_location("b498_probe", _DIR / "probe.py")
P = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P)

R = json.load(open(_DIR / "b498_sl3_gluing.json"))

t, p, q = P.t, P.p, P.q


# ---------------- (1) the control, recomputed ----------------
def test_control_exact_decomposition_three_components_dim_two():
    comps = P.exact_decomposition()               # asserts the complete case split
    assert set(comps) == {"V0", "W1", "W2"}
    # each component is 2-parameter (dim 2) and T_1^2-fixed (checked inside):
    for _nm, (params, _coord) in comps.items():
        assert len(params) == 2
    assert R["controls"]["n_components"] == 3
    assert R["controls"]["dims"] == [2, 2, 2]


def test_control_sym2_shadow_lands_on_V0():
    dev = P.sym2_shadow_numeric()                 # B67 chain via B71 (importlib reuse)
    assert dev < 1e-10


def test_control_dehn_filling_relations_scalar_criterion():
    sd = P.b71_symbolic_dehn()
    med1, n1 = sd.dehn_scalar_residual(sd.per.W1, "D2", seeds=(5,), npts=3)
    med2, n2 = sd.dehn_scalar_residual(sd.per.W2, "D3", seeds=(5,), npts=3)
    assert n1 >= 2 and n2 >= 2
    assert med1 < 1e-6 and med2 < 1e-6            # M^3 = L on W1; M^3 L = 1 on W2


# ---------------- (2) the involution ----------------
def test_involution_psi_exact():
    assert P.involution_exact()
    assert R["involution"]["conjugates_trace_map_to_inverse"] is True
    assert R["involution"]["orbit_W"] == "W1 <-> W2 swapped"
    assert R["involution"]["theta_fixes_V0"] == "pointwise"


# ---------------- (3) the Sym^2 leg ----------------
def test_sym2_exact_identity_and_geometric_pair():
    p_geo, q_geo = P.sym2_exact()                 # asserts the identity inside
    assert sp.simplify(q_geo - sp.conjugate(p_geo)) == 0
    assert sp.simplify(p_geo + q_geo) == 1
    assert sp.simplify(sp.expand(p_geo * q_geo)) == 7
    assert R["sym2"]["esym"] == [1, 7]
    assert R["sym2"]["psi_is_sigma3_at_geo"] is True
    assert R["sym2"]["algebra_rank"] == 9


# ---------------- (4) the degree=rank scalars ----------------
def test_degree_rank_scalar_c_is_one_on_both_components():
    wd, wc, n = P.scalars_50digit(pts=((2, 3),), dps=40)
    assert n == 1
    assert wd < 1e-28 and wc < 1e-28              # thresholds re-asserted inside too
    assert R["scalars"]["c_W1"] == 1 and R["scalars"]["c_W2"] == 1
    assert R["scalars"]["k_pair"] == [3, -3]


# ---------------- (5) the transverse-Jacobian torsion ----------------
def test_jacobian_torsion_exact():
    tauV0, tauW = P.jacobian_torsion()            # asserts everything inside
    assert sp.expand(tauV0 + 4 * (p - 1) * (q - 1) * (p * q - 4)) == 0
    assert sp.expand(tauW + 3 * (p - q)**2) == 0
    assert R["jacobian"]["tau_geo"] == -84
    assert R["jacobian"]["geo_u_disc"] == -87
    assert R["jacobian"]["geo_u_esym"] == [9, 42]
    assert R["jacobian"]["charpoly_W1_equals_W2"] is True


# ---------------- (6) the Ptolemy fields, offline (bundled equations) ----------------
def test_ptolemy_class0_fields_exact_offline():
    d = json.load(open(P.B444_JSON))
    r0 = P.solve_ptolemy_class(d["4_1"]["eqs"], d["4_1"]["vars"])
    assert r0["nonempty"] and r0["degree"] == 6
    assert r0["fields"] == [-7, -3]
    c0 = sp.symbols('c_1101_0')
    elim = sp.sympify(r0["eliminants"]["c_1101_0"], locals={'c_1101_0': c0})
    assert sp.expand(elim - sp.expand((c0 - 1) * (4 * c0**2 - c0 + 4))) == 0


# ---------------- (7) the seal + documentation integrity ----------------
def test_seal_banked_and_symmetrized():
    assert R["seal"]["verdict"] == "SEALED"
    assert R["seal"]["k_pair_esym"] == [0, -9]
    assert R["seal"]["geo_esym"] == [1, 7]
    assert R["seal"]["u_esym"] == [9, 42]
    assert R["seal"]["rational_values"] == [1, 1, -84]
    assert R["seal"]["counts"] == [3, 2, 2, 2, 6, 2]
    bins = {row["bin"] for row in R["seal"]["table"]}
    assert bins == {"F", "G", "P", "C"}           # no unsymmetrizable bin exists


def test_verdict_sealed_with_guardrail_and_named_blocks():
    assert R["verdict"]["outcome"] == "SEALED"
    assert "computable horizon" in R["verdict"]["phrasing"]
    blocked = R["verdict"]["tool_blocked"]
    assert len(blocked) >= 4
    assert any("magma" in b for b in blocked)
    assert any("B495" in b for b in blocked)      # adjoint torsion cross-referenced
    find = (_DIR / "FINDINGS.md").read_text(encoding="utf-8")
    assert "SEALED" in find
    assert "Nothing to `CLAIMS.md`" in find
    assert "TOOL-BLOCKED" in find
    assert "−84" in find or "-84" in find
    assert "√−7" in find or "sqrt-7" in find


# ---------------- SnapPy cross-checks (optional dependency) ----------------
def test_snappy_obstruction_class_1_is_eisenstein_pair():
    snappy = pytest.importorskip("snappy")
    M = snappy.Manifold("4_1")
    Vs = M.ptolemy_variety(3, obstruction_class='all')
    assert len(Vs) == 2                           # exactly two classes at N = 3
    r1 = P.solve_ptolemy_class([str(e) for e in Vs[1].equations],
                               [str(v) for v in Vs[1].variables])
    assert r1["nonempty"] and r1["degree"] == 2
    assert r1["fields"] == [-3]                   # Q(sqrt-3) only (PGL(3)-only pair)
    if isinstance(R.get("ptolemy", {}).get("class1"), dict):
        assert R["ptolemy"]["class1"]["degree"] == 2
        assert R["ptolemy"]["class1"]["fields"] == [-3]
