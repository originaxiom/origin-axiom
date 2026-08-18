"""B8078 — the rung spectrum is attained; the paper's eleven-element bound is tight.

These read `results.json` (computed) and never prose. Each asserts a fact that would be
FALSE if the arrangement picture were wrong — not a restatement of the file.
"""
import json
import os

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "..", "frontier", "B8078_rung_spectrum_attained", "results.json")

# The paper's Theorem thm:rungspec, transcribed from main.tex — NOT read from results.json,
# so a drift in either one breaks this test.
PAPER_BOUND = [12, 14, 16, 18, 20, 26, 28, 30, 36, 46, 78]


@pytest.fixture(scope="module")
def r():
    with open(RES) as fh:
        return json.load(fh)


def test_spectrum_equals_the_papers_bound_so_the_containment_is_tight(r):
    assert r["spectrum"] == PAPER_BOUND
    assert r["bound_is_tight"] is True


def test_the_sample_was_a_strict_subset_of_the_truth(r):
    """B8075's 16 coordinate subsets gave {12,30,78}. If that had been the whole
    spectrum, this arc would have found nothing and the paper's remark would stand."""
    sample = set(r["coordinate_subset_sample"])
    assert sample == {12, 30, 78}
    assert sample < set(r["spectrum"])
    assert len(set(r["spectrum"]) - sample) == 8


def test_the_fourteen_is_attained_discharging_thm_smt(r):
    """thm:smt reads 'if a 14-dimensional locus occurs, its type is forced'. The
    occurrence is what this supplies."""
    assert 14 in r["spectrum"]
    assert r["attained_at_subspace_dims"]["14"] == [3]


def test_weight_orbits_account_for_the_whole_algebra(r):
    """12 + sum(orbit x multiplicity) = 78. This is the decomposition, and it is the
    reason a finite enumeration replaces an infinite lattice."""
    assert r["dim_z_C"] == 12
    assert sorted(r["weight_orbits"]) == [[6, 3], [12, 1], [12, 3]]
    assert r["dim_z_C"] + sum(d * m for d, m in r["weight_orbits"]) == 78
    assert r["n_weights"] == sum(d for d, _ in r["weight_orbits"]) == 30


def test_the_enumeration_is_over_flats_not_a_sample(r):
    assert r["n_flats"] == 109
    assert len(r["faithful_primes"]) >= 3


def test_the_46_is_arithmetic_and_lives_in_K(r):
    """The enhancement cubic is irreducible over Q — so no RATIONAL direction in the
    (8,16)-plane reaches 46 — and generates K. This is why the sample could not see it."""
    assert r["plane_cubic_generates_K"] is True
    assert 46 in r["spectrum"]
    assert r["attained_at_subspace_dims"]["46"] == [1]


def test_every_independently_banked_rung_value_is_in_the_spectrum(r):
    """12 (B874/B8075), 14 and 18 (B892), 30 (B874/B8075), 46 (B866), 78. None of these
    came from this arc's code; if the enumeration were incomplete they would not all land."""
    for v in (12, 14, 18, 30, 46, 78):
        assert v in r["spectrum"], v


def test_scope_names_the_residue_rather_than_hiding_it(r):
    s = r["scope"]
    assert "faithful primes" in s and "Qbar" in s
    assert "exact over Q" in s
