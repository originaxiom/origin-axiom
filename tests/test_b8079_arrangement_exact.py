"""B8079 — the rung arrangement exact over ℚ, and the 64 Levi subsystems.

Reads `results.json` (computed) and never prose. The cross-arc assertions are the point:
B8078 reached the same arrangement from the charges, mod three primes; this one reaches it
from the E₆ root system over ℚ. Neither can see the other's code.
"""
import json
import os

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(HERE, "..", "frontier")
ELEVEN = [12, 14, 16, 18, 20, 26, 28, 30, 36, 46, 78]


@pytest.fixture(scope="module")
def r():
    with open(os.path.join(F, "B8079_arrangement_exact", "results.json")) as fh:
        return json.load(fh)


@pytest.fixture(scope="module")
def prev():
    with open(os.path.join(F, "B8078_rung_spectrum_attained", "results.json")) as fh:
        return json.load(fh)


def test_the_residue_is_closed_the_lattice_is_exact_over_Q(r):
    assert r["exact_over_Q"] is True
    assert r["n_flats"] == 109
    assert r["spectrum"] == ELEVEN
    assert r["bound_is_tight"] is True


def test_two_independent_routes_agree(r, prev):
    """B8078: charges → ad-matrices → charpoly orbits → three primes.
    B8079: E₆ roots → restrict to (A₂)-perp → over ℚ. Same lattice, same spectrum."""
    assert r["n_flats"] == prev["n_flats"]
    assert r["spectrum"] == prev["spectrum"]
    assert r["attained_at_subspace_dims"] == prev["attained_at_subspace_dims"]


def test_the_weight_profile_matches_the_charge_side_computation(r, prev):
    """12×1 + 18×3 = 66 = 72 − 6. B8078 got this from the charges; here it falls out of
    the root system. A disagreement would mean one of the two constructions is not the
    object's."""
    assert r["weight_multiplicity_profile"] == [[1, 12], [3, 18]]
    assert sum(m * c for m, c in r["weight_multiplicity_profile"]) == 66
    assert r["zero_weight_roots"] == 6
    assert r["n_weights"] == prev["n_weights"] == 30


def test_the_no_moduli_reduction(r):
    """dim z(C) = 12 = 6 (Cartan) + 6 (the A₂ vanishing on C), and C = (A₂)-perp is
    4-dimensional. If either number moved, C would not be the object's charge algebra."""
    assert r["a2_perp_dim"] == 4
    assert 6 + r["zero_weight_roots"] == 12


def test_the_64_levi_subsystems_are_deposited(r):
    """Campaign item 3: block (b) → block (a)."""
    assert r["levi_root_counts"] == [0, 2, 4, 6, 8, 10, 12, 14, 20, 22, 24, 30, 40, 72]
    assert r["ambient_levi_dims"] == [6, 8, 10, 12, 14, 16, 18, 20, 26, 28, 30, 36, 46, 78]
    assert sum(r["levi_subsets_by_count"].values()) == 64


def test_twenty_four_is_not_a_levi_dimension(r):
    """Load-bearing for the paper's gap claims, and independently found by cc."""
    assert r["twenty_four_is_levi"] is False
    assert 24 not in r["ambient_levi_dims"]


def test_the_three_ambiguous_dimensions_are_12_18_20(r):
    """Rmk (leviscope) claims exactly these three carry two Levi types, and claims no
    type at any of them."""
    assert r["dims_with_two_types"] == [12, 18, 20]


def test_the_four_counts_the_paper_leans_on_are_unambiguous(r):
    """46→40→D5, 30→24→D4, 26→20→A4, 14→8→A2+A1. The terminus rests on the last one."""
    t = r["levi_types_by_count"]
    assert t["40"] == ["D5"] and t["24"] == ["D4"]
    assert t["20"] == ["A4"] and t["8"] == ["A1+A2"]
    assert r["levi_subsets_by_count"]["20"] == 4


def test_every_realized_value_is_an_ambient_levi_dimension(r):
    for v in r["spectrum"]:
        assert v in r["ambient_levi_dims"], v
