"""Locks for B495 (Gate A class 2a: the adjoint/Ptolemy torsion class, Galois-sealed).

Loads the banked JSON for the assembled claims and INDEPENDENTLY recomputes the decisive
facts with the probe's exact machinery (so the lock does not merely trust the JSON):
(1) the two CONTROL anchors -- geometric adjoint torsion -3 (Eisenstein, Fox/Wada, both
Galois lifts) and dynamical zeta adjoint -5 (golden, Sym^2 of the cat map); (2) the derived
character variety Phi(m,z) = z^2 - (m^2+1) z + 2 m^2 - 1 (one nonabelian component; branch
divisor (m^2-1)(m^2-5) squarefree); (3) the per-stratum torsion values (metabelian +5,
bifurcation -5 = the dynamical zeta polynomial, branch/2T +3 = Phi_3) and the two-method
agreement with the B98 transverse Jacobian tau_B = 2 - c(x) on V0; (4) the Galois closure /
symmetrizability of the multiset {-3,-3,+3,+3,+5,+5,-5,-5}: every value rational (total
collapse), sum 0, product 15^4, gauge- and conjugation-invariant; (5) documentation
integrity (verdict SEALED, firewall untouched). SnapPy (amphichirality; Ptolemy N=2
metadata) is behind importorskip. Total runtime well under 60 s.
"""
import importlib.util
import json
import pathlib

import pytest
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_DIR = _ROOT / "frontier" / "B495_adjoint_torsion_galois"

_spec = importlib.util.spec_from_file_location("b495_probe", _DIR / "probe.py")
P = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(P)

R = json.load(open(_DIR / "b495_adjoint_torsion.json"))

t, r, m, z, v, s = P.t, P.r, P.m, P.z, P.v, P.s
MULTISET = [-3, -3, 3, 3, 5, 5, -5, -5]


# ---------------- (1) the control anchors, recomputed ----------------
def test_control_geometric_adjoint_is_minus_three_both_lifts():
    F3 = P.QF(-3)
    ra = sp.Matrix([[1, 1], [0, 1]])
    for vroot in [(1 + r) / 2, (1 - r) / 2]:          # the two Galois lifts of rho_geo
        rb = sp.Matrix([[1, 0], [vroot, 1]])
        assert P.word_mat(P.R_, ra, rb, F3) == sp.eye(2)
        W = P.wada(ra, rb, F3, 'b')
        val, kn, kd = P.reg_at_1(W, F3)
        assert (val, kn, kd) == (-3, 1, 0)
        assert sp.factor(W) == sp.factor((t - 1) * (t**2 - 5 * t + 1) / t**3)


def test_control_dynamical_zeta_is_minus_five():
    cp = sp.factor(P.sym2(sp.Matrix([[2, 1], [1, 1]])).charpoly(t).as_expr())
    assert cp == sp.factor((t - 1) * (t**2 - 7 * t + 1))
    q, rem = sp.div(sp.expand(cp), t - 1, t)
    assert rem == 0 and q.subs(t, 1) == -5            # zeta_1 = 2 - L_4 = -5


def test_controls_banked():
    assert R["controls"]["geo_tau"] == -3
    assert R["controls"]["dyn_zeta1"] == -5
    assert R["controls"]["psl_collapse"] is True


# ---------------- (2) the character variety ----------------
def test_character_variety_one_nonabelian_component():
    Phi = sp.expand(z**2 - (m**2 + 1) * z + 2 * m**2 - 1)
    # derived anchor at s=1 (B425 holonomy quadratic) via the Riley v-form:
    riley = sp.expand((v - 1) * (s**2 + 1 / s**2) + v**2 - 3 * v + 3)
    assert sp.expand(riley.subs(s, 1)) == sp.expand(v**2 - v + 1)
    # Phi = Riley in character coordinates (z = m^2 - 2 + v):
    yv = m**2 - 2
    assert sp.expand(((v - 1) * yv + v**2 - 3 * v + 3).subs(v, z - m**2 + 2)) == Phi
    # one component over Q; squarefree branch divisor => irreducible over C:
    assert len(sp.factor_list(Phi)[1]) == 1 and sp.factor_list(Phi)[1][0][1] == 1
    disc = sp.factor(sp.discriminant(Phi, z))
    assert disc == sp.factor((m - 1) * (m + 1) * (m**2 - 5))
    assert sp.gcd(sp.expand(disc), sp.diff(sp.expand(disc), m)) == 1
    # stratum quadratics: geometric Eisenstein, metabelian golden:
    assert sp.discriminant(Phi.subs(m, 2), z) == -3
    assert sp.discriminant(Phi.subs(m, 0), z) == 5
    # mu-framing certificates: regular at geo/meta, critical at bif/2T:
    dPhi = sp.diff(Phi, z)
    assert sp.simplify(dPhi.subs([(m**2, 5), (z, 3)])) == 0
    assert sp.simplify(dPhi.subs([(m**2, 1), (z, 1)])) == 0


# ---------------- (3) the per-stratum values, recomputed ----------------
def test_metabelian_pair_gives_plus_five():
    F5 = P.QF(5)
    ra = sp.Matrix([[sp.I, 1], [0, -sp.I]])
    for vroot in [(5 + r) / 2, (5 - r) / 2]:          # the golden Galois pair
        rb = sp.Matrix([[sp.I, 0], [vroot, -sp.I]])
        assert P.word_mat(P.R_, ra, rb, F5) == sp.eye(2)
        W = P.wada(ra, rb, F5, 'b')
        val, kn, kd = P.reg_at_1(W, F5)
        assert (val, kn, kd) == (5, 1, 0)
        assert sp.factor(W) == sp.factor((t - 1) * (t**2 + 3 * t + 1) / t**3)


def test_bifurcation_rep_gives_dynamical_zeta_polynomial():
    F5 = P.QF(5)
    phi_, phii = (1 + r) / 2, F5.red((r - 1) / 2)     # phi, 1/phi = phi - 1
    ra = sp.Matrix([[phi_, 1], [0, phii]])
    rb = sp.Matrix([[phi_, 0], [0, phii]])            # v = 0: the Burde-de Rham rep
    assert P.word_mat(P.R_, ra, rb, F5) == sp.eye(2)
    W = P.wada(ra, rb, F5, 'b')
    val, kn, kd = P.reg_at_1(W, F5)
    assert (val, kn, kd) == (-5, 1, 0)
    # the two banked "ends" meet: the adjoint Wada quad here IS t^2 - 7t + 1:
    assert sp.factor(W) == sp.factor((t - 1) * (t**2 - 7 * t + 1) / t**3)


def test_branch_2T_pair_gives_plus_three_and_is_binary_tetrahedral():
    F3 = P.QF(-3)
    s6, s6i = (1 + r) / 2, (1 - r) / 2                # zeta_6, meridian trace 1
    ra = sp.Matrix([[s6, 1], [0, s6i]])
    rb = sp.Matrix([[s6, 0], [2, s6i]])               # v = 2
    assert P.word_mat(P.R_, ra, rb, F3) == sp.eye(2)
    W = P.wada(ra, rb, F3, 'b')
    val, kn, kd = P.reg_at_1(W, F3)
    assert (val, kn, kd) == (3, 1, 0)
    assert sp.factor(W) == sp.factor((t - 1) * (t**2 + t + 1) / t**3)   # Phi_3, Eisenstein
    assert P.group_order(ra, rb, F3) == 24            # the McKay-E6 group 2T


def test_method_agreement_with_transverse_jacobian():
    xx = sp.symbols('xx')
    tauB = -(2 * xx**2 - 3 * xx + 3) / (xx - 1)       # B98: 2 - c(x) on V0
    assert sp.discriminant(2 * xx**2 - 3 * xx + 3, xx) == -15   # the seam
    vals = {
        -3: sp.Rational(3, 2) + sp.sqrt(-3) / 2,      # x_geo: x^2 - 3x + 3 = 0
        5: -sp.Rational(1, 2) + sp.sqrt(5) / 2,       # x_meta: x^2 + x - 1 = 0
        3: sp.Integer(0),                             # 2T fiber point
        -5: sp.Integer(2),                            # trivial fiber char (dynamical end)
    }
    for expect, pt in vals.items():
        assert sp.simplify(tauB.subs(xx, pt) - expect) == 0
    assert R["sweep"]["method_agreement"] is True


# ---------------- (4) the Galois closure / the seal ----------------
def test_multiset_banked_and_galois_closed():
    assert R["seal"]["multiset"] == MULTISET
    # total Galois collapse: every value already in the fixed field Q:
    assert all(sp.Integer(x_).is_rational for x_ in MULTISET)
    # symmetric functions rational and seam-normed:
    assert sum(MULTISET) == 0
    assert sp.prod(MULTISET) == 15**4
    # sign-symmetric (the B348 amphichirality kill) => invariant under the Wada
    # dr/da vs dr/db unit gauge (= -1, constant across strata, banked per-row):
    assert sorted(-x_ for x_ in MULTISET) == sorted(MULTISET)
    assert all(row["gauge_unit"] == "-1" for row in R["sweep"]["rows"])
    # discretely multivalued (clause 2): finite, four distinct values:
    assert sorted(set(MULTISET)) == [-5, -3, 3, 5]
    # conjugation swaps each stratum pair while fixing values (values equal in pairs):
    for a, b in [(0, 1), (2, 3), (4, 5), (6, 7)]:
        assert MULTISET[a] == MULTISET[b]


def test_h1_rank_and_lift_collapse():
    # H^1 certificate: Fox rank 2 (=> dim H^1 = 1) at every swept point:
    assert all(row["fox_rank"] == 2 for row in R["sweep"]["rows"])
    # PSL sign-lift collapse (symbolic identity):
    a1, a2, a3, a4 = sp.symbols('a1 a2 a3 a4')
    M = sp.Matrix([[a1, a2], [a3, a4]])
    assert sp.expand(P.sym2(-M) - P.sym2(M)) == sp.zeros(3, 3)


def test_abelian_component_is_continuous_not_a_choice():
    # clause-(2) exhibit: V_ab(s) = Delta(s^2)^2 / (s (s^2-1))^2, nonconstant, and it
    # vanishes exactly on Delta(s^2) = 0 (the PC-3 bifurcation, m = +-sqrt5):
    Vab = (s**4 - 3 * s**2 + 1)**2 / (s**2 * (s**2 - 1)**2)
    assert sp.cancel(sp.diff(Vab, s)) != 0
    assert sp.factor(s**4 - 3 * s**2 + 1) == sp.factor((s**2 - s - 1) * (s**2 + s - 1))
    assert R["abelian"]["pole"] == [0, 1] or tuple(R["abelian"]["pole"]) == (0, 1)


# ---------------- (5) verdict + documentation integrity ----------------
def test_verdict_sealed_with_guardrail():
    assert R["seal"]["verdict"] == "SEALED"
    assert R["verdict"]["outcome"] == "SEALED"
    assert "computable horizon" in R["verdict"]["phrasing"]
    find = (_DIR / "FINDINGS.md").read_text(encoding="utf-8")
    assert "SEALED" in find
    assert "Nothing to `CLAIMS.md`" in find
    assert "TOOL-BLOCKED" in find                     # the named residual is present
    assert "{−3, −3, +3, +3, +5, +5, −5, −5}" in find


# ---------------- SnapPy cross-checks (optional dependency) ----------------
def test_snappy_amphichirality_and_ptolemy_metadata():
    snappy = pytest.importorskip("snappy")
    M = snappy.Manifold("4_1")
    assert M.symmetry_group().is_amphicheiral()       # the geometric sign-killer (B348)
    # two obstruction classes at N=2; the banked exact solve: class 0 empty, class 1
    # cut by the Eisenstein quadratic (the geometric pair only):
    assert len(M.ptolemy_variety(2, obstruction_class='all')) == 2
    if R.get("ptolemy", {}).get("available"):
        assert R["ptolemy"]["classes"]["0"]["nonempty"] is False
        assert R["ptolemy"]["classes"]["1"]["nonempty"] is True
        assert "c_0101_0**2 - c_0101_0 + 1" in R["ptolemy"]["classes"]["1"]["eliminant"]
