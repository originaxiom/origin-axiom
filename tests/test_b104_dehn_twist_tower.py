"""B104 -- locking tests: the Dehn-twist route to the all-n tower.

GATE: the composed Dehn-twist word ['U','S'] at SL(4) reproduces B80's proved metallic tower.
Universality (SL(4)): char(J(N)) = the two-sequence catalog prod_d char(Sym^d N)^{mu_d} for metallic
(det -1) AND non-metallic (det +1) monodromies; J factors through N.
SL(5): the Dehn-twist engine inherits the eps-series gauge degeneracy (21/24 Dickson factors resolve) --
the wall is computational (B61/B66), not the representation theory.
"""
import importlib.util
import pathlib

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b104", _ROOT / "frontier" / "B104_dehn_twist_tower" / "probe.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_gate_sl4_reproduces_b80_tower():
    """The Dehn-twist engine is correct: ['U','S'] at SL(4) == B80's proved metallic tower."""
    assert B.gate_sl4() is True


def test_two_sequence_multiplicities():
    assert B.two_sequence_mult(4) == {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
    assert B.two_sequence_mult(5) == {0: 1, 1: 1, 2: 2, 3: 1, 4: 1, 5: 1}


def test_sl4_universality_metallic_and_nonmetallic():
    """char(J(N)) = the two-sequence catalog for metallic (det -1) and genuine non-metallic (det +1)."""
    metallic = B.universality_sl4(["U", "S"])                 # N = M_1, det -1
    assert metallic["engine_ok"] and metallic["char_eq_catalog"] is True
    nonmetallic = B.universality_sl4(["U", "U", "L"])         # N = [[3,2],[1,1]] = U^2 L, det +1
    assert nonmetallic["det"] == 1 and nonmetallic["char_eq_catalog"] is True


def test_sl4_factors_through_N():
    assert B.factors_through_N_sl4() is True


def test_sl5_wall_partial_resolution():
    """SL(5): the Dehn-twist engine inherits the eps-series gauge degeneracy -- the char does NOT match the
    catalog, but most Dickson factors resolve (the wall is computational, not the rep theory)."""
    r = B.sl5_attempt()
    assert r["engine_consistent"] is True
    assert r["char_eq_catalog"] is False                      # the gauge wall (B61/B66), characterized
    assert r["factors_resolved"] >= 20                        # 21/24 survive -> partial, not total, failure
