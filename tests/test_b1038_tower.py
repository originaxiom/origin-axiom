"""B1038 locks — the tower cluster, re-verified symbolically before restoration.

These recompute the algebra (WORKING_RULES rule 7). If any breaks, the restored LAW_MAP row is
wrong and must move with it.
"""
import importlib.util
import pathlib

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_SPEC = importlib.util.spec_from_file_location(
    "b1038", _ROOT / "frontier" / "B1038_tower_restored" / "verify.py")
v = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(v)


def test_every_check_passes():
    failed = [k for k, c in v.R["checks"].items() if not c["pass"]]
    assert failed == [], failed


def test_the_dimension_surplus_vanishes_at_exactly_one_rank():
    """(n+1)(n+2)/2 - (n^2-1) = -(n-4)(n+1)/2, zero iff n = 4 among ranks."""
    n = sp.symbols("n")
    surplus = sp.simplify((n + 1) * (n + 2) / 2 - (n**2 - 1))
    assert sp.simplify(surplus + (n - 4) * (n + 1) / 2) == 0
    assert [r for r in sp.solve(sp.Eq(surplus, 0), n) if r >= 2] == [4]


def test_the_two_bands_assemble_to_exactly_the_adjoint_dimension():
    n = sp.symbols("n")
    expr = sp.expand((n + 1) * (n + 2) / 2 + (n - 1) * (n - 2) / 2 - 3)
    assert sp.simplify(expr - (n**2 - 1)) == 0


def test_the_functorial_step_is_what_makes_it_a_module_identity():
    """Sym^a(V+1) = sum of Sym^k(V), k <= a. Over GL(2) a single element's character does not
    imply module-iso; this functorial decomposition is what closes that gap (B122's hinge)."""
    assert v.R["checks"]["Sym_of_V_plus_trivial_is_the_contiguous_band"]["pass"]


def test_the_grading_is_external_not_principal():
    """det Sym^d(M) = (det M)^{d(d+1)/2}, so det = -1 gives an ALTERNATING parity, which no
    all-even-weight principal grading can match — the obstruction for every n >= 3."""
    assert v.R["checks"]["B121_det_Sym_d_equals_det_to_the_d_d_plus_1_over_2"]["pass"]
    p = v.R["checks"]["B121_so_a_det_minus_one_monodromy_gives_an_ALTERNATING_parity"]
    assert p["pass"] and set(p["parity_by_d"].values()) == {1, -1}


def test_the_instrument_has_its_own_control():
    """Two independent routes to the Sym character (direct enumeration vs generating function)
    agree — so a bug in one would not silently produce a passing identity."""
    assert v.R["checks"]["the_two_independent_routes_to_the_Sym_character_agree"]["pass"]


def test_what_is_carried_by_citation_is_named_not_implied():
    assert "the tower's own construction" in v.R["carried_by_citation"]
    assert "B103" in v.R["carried_by_citation"]["the tower's own construction"]


def test_the_restoration_landed_with_its_scope():
    lawmap = (_ROOT / "docs" / "LAW_MAP.md").read_text(encoding="utf-8")
    assert "THE TRIVIAL-POINT TOWER IS TWO Sym BANDS" in lawmap
    assert "character level n=2..11" in lawmap and "module level at n=3,4" in lawmap
    for b in ("B117", "B122", "B121", "B118"):
        assert b in lawmap, b
