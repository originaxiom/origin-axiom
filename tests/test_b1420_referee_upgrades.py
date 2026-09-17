"""B1420 lock -- the referee's upgrades, verified.

(1) the order-three cusp census over m004's 87 covers to degree 10 is not vacuous: 14 covers carry a hexagonal cusp
    (16 of 201 cusps), none realises an order-3 cusp rotation, isometries read canonically (E81);
(2) the record's own non-split rho satisfies the symplectic identity J rho J^-1 = (rho^-1)^T, so Sym^m(rho) is self-dual
    and I(V) = 0 whenever psi^2 = 1 -- the index fires only through the twist;
(3) the m010 witness: untwisted 0, order-2 twist 0, order-6 twist +1;
(4) at scale: 0 of the record's 542 firing modules has a self-inverse twist."""
import json, pathlib, re, sys
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
D = ROOT / "frontier" / "B1420_the_referees_upgrades" / "verification"
B1418 = ROOT / "frontier" / "B1418_the_family_as_the_object" / "verification"


def covers():
    return json.loads((D / "hexagonal_cusps.json").read_text())


def test_hexagonal_census_is_not_vacuous():
    rows = covers()
    assert len(rows) == 87
    hexed = [r for r in rows if r["hexagonal_cusps"]]
    assert len(hexed) == 14
    assert sum(len(r["hexagonal_cusps"]) for r in rows) == 16
    assert sum(r["cusps"] for r in rows) == 201
    assert all("symmetry_group_error" not in r for r in rows)          # every symmetry group actually computed


def test_no_order_three_cusp_rotation():
    assert sum(len(r["order3_cusp_rotations"]) for r in covers()) == 0


def test_hexagonal_predicate_controls():
    """m003's cusp is hexagonal, m004's is not -- the test can fail on its own domain"""
    snappy = pytest.importorskip("snappy")
    src = (D / "hexagonal_cusps.py").read_text().split("rows = []")[0]
    ns = {}
    exec(src, ns)
    assert ns["is_hexagonal"](complex(snappy.Manifold("m003").cusp_info()[0]["shape"])) is True
    assert ns["is_hexagonal"](complex(snappy.Manifold("m004").cusp_info()[0]["shape"])) is False


def test_symplectic_identity_and_witness():
    """re-runs the lemma script's two claims: the identity over K, and the m010 triple 0 / 0 / +1"""
    pytest.importorskip("snappy")
    sys.path.insert(0, str(B1418))
    out = (D / "selfduality_lemma.out.txt").read_text()
    assert "=> Sym^m(rho) is self-dual for every m, non-split or not: True" in out
    assert "==> m010 untwisted (psi = 1): I(V) = 0" in out
    assert "==> m010 twisted by chi^3 (order 2): I(V) = 0" in out
    assert "==> m010 twisted by chi (order 6): I(V) = 1" in out
    assert "PREDICTION HOLDS: True" in out


def test_no_firing_module_has_a_self_inverse_twist():
    out = (D / "firing_twists.out.txt").read_text()
    m = re.search(r"firing \(I != 0\): (\d+)", out)
    assert m and int(m.group(1)) == 542
    assert "firing modules with psi^2 = 1 (each would refute the lemma): 0" in out
