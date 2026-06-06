"""B103 -- locking tests: the SL(n) tower as a GL(2,Z) representation.

Route 1 (universality): the MCG relations lift to the Jacobians; J(3) factors through the abelianization N;
the det-sign catalog law holds for metallic and non-metallic monodromies.
Route 2 (the explicit rep): the constructive module-iso P J(m) = (+)_d Sym^d(M_m)^{mu_d} holds EXACTLY over
Q[m] at n=3 and n=4, with intertwiner dimension = Schur sum mu_d^2.
"""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b103", _ROOT / "frontier" / "B103_tower_equivariance" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


# --- Route 1 ------------------------------------------------------------
def test_mcg_relations_lift_to_jacobians():
    rels = B.relations_lift()
    assert rels == {"S2=I": True, "SUS=L": True, "SLS=U": True}


def test_jacobian_factors_through_abelianization():
    ok, nclasses = B.factors_through_N()
    assert ok is True
    assert nclasses >= 15                                 # many multi-word N-classes checked


def test_det_sign_catalog_law_metallic_and_nonmetallic():
    """The catalog k=2,3 + det-sign k=1 + parity law holds for metallic (det -1) and non-metallic (det +1)."""
    for word in (["U", "S"], ["U", "U", "L"], ["U", "L", "U", "L"], ["U", "U", "L", "S"]):
        assert B.universality_law(word)["law_holds"] is True


# --- Route 2 ------------------------------------------------------------
def test_two_sequence_multiplicities():
    assert B.two_sequence_mult(3) == {0: 1, 2: 1, 3: 1}
    assert B.two_sequence_mult(4) == {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}


def test_constructive_module_iso_n3_exact():
    """P J(m) = (Sym^0 (+) Sym^2 (+) Sym^3)(M_m) P exactly over Q[m]; intertwiner dim = Schur = 3."""
    r = B.module_iso(3)
    assert r["char_eq_catalog"] is True
    assert r["intertwiner_dim"] == r["schur_expect"] == 3
    assert r["P_invertible"] is True
    assert r["exact_identity_over_Qm"] is True


def test_constructive_module_iso_n4_exact():
    """P J(m) = (Sym^0..Sym^4)(M_m) P exactly over Q[m] (B80 Jacobian); intertwiner dim = Schur = 5."""
    r = B.module_iso(4)
    assert r["char_eq_catalog"] is True
    assert r["intertwiner_dim"] == r["schur_expect"] == 5
    assert r["P_invertible"] is True
    assert r["exact_identity_over_Qm"] is True
